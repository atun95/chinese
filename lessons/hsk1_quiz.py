# -*- coding: utf-8 -*-
import streamlit as st
import streamlit.components.v1 as components
import random
import csv
import html
import json
import uuid
from datetime import datetime, timezone, timedelta
from pathlib import Path
from ui_utils import render_lesson_intro, render_play_button

# IMPORT SUPABASE CLIENT
try:
    import supabase_client
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parent.parent))
    import supabase_client

# IMPORT ĐỀ QUIZ TỪ FILE DỮ LIỆU RIÊNG BIỆT
try:
    from hsk1_quizzes_data import QUIZZES_DATA
except ImportError:
    from lessons.hsk1_quizzes_data import QUIZZES_DATA

EXAM2_DATA_PATH = Path(__file__).resolve().parent / "hsk1_exam2_data.json"


def _load_exam2_data():
    try:
        return json.loads(EXAM2_DATA_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _as_dict(value):
    if isinstance(value, dict):
        return value
    if isinstance(value, str) and value.strip().startswith("{"):
        try:
            parsed = json.loads(value)
            return parsed if isinstance(parsed, dict) else {}
        except Exception:
            return {}
    return {}


def _exam2_choice(sel, qid):
    blob = _as_dict(sel.get("answers"))
    choices = blob.get("choices") if isinstance(blob.get("choices"), dict) else {}
    item = choices.get(qid)
    if isinstance(item, dict):
        return item
    legacy = blob.get(qid)
    if isinstance(legacy, int) or (isinstance(legacy, str) and str(legacy).isdigit()):
        return {"type": "mcq", "index": int(legacy)}
    if legacy in ("D", "S"):
        return {"type": "tf", "value": legacy}
    return {}


def _exam2_order(sel, qid):
    raw = _as_dict(sel.get("order_answers")).get(qid) or []
    if not isinstance(raw, list):
        return []
    return [str(word) for word in raw if isinstance(word, str) and word]


def _accepted_indexes(q):
    if q.get("id") == "8_6":
        return {1, 3}
    ans = q.get("ans")
    return {ans} if isinstance(ans, int) else set()


def _query_param(name):
    value = st.query_params.get(name, "")
    if isinstance(value, (list, tuple)):
        value = value[0] if value else ""
    return str(value or "")


def _load_exam2_submissions(limit=50):
    client = supabase_client.get_supabase_client()
    if not client:
        return []
    columns = "id,student_name,score,max_score,part_scores,answers,order_answers,essay,submitted_at"
    try:
        res = (
            client.table("hsk1_exam2_answers")
            .select(columns)
            .eq("answers->>status", "submitted")
            .eq("answers->>v", "2")
            .order("id", desc=True)
            .limit(limit)
            .execute()
        )
        rows = res.data or []
    except Exception:
        res = client.table("hsk1_exam2_answers").select(columns).order("id", desc=True).limit(300).execute()
        rows = []
        for row in res.data or []:
            blob = _as_dict(row.get("answers"))
            if blob.get("v") == 2 and blob.get("status") == "submitted":
                rows.append(row)
            if len(rows) >= limit:
                break
    return rows


def _exam2_esc(value):
    return html.escape(str(value or ""), quote=False)


def render_exam2_review(sel):
    """Render bài làm của học viên (từ Supabase) dạng chấm điểm, không phải JSON."""
    data = _load_exam2_data()
    out = []
    zh = "font-family:'PingFang SC','Microsoft YaHei','Noto Sans SC',sans-serif;"
    note_style = (
        "margin-top:8px;font-size:0.85rem;color:#475569;background:#f8fafc;"
        "border-left:3px solid #94a3b8;padding:6px 10px;border-radius:6px;"
    )

    def qcard(inner):
        return (
            '<div style="background:#fff;border:1px solid #e2e8f0;border-radius:14px;'
            f'padding:14px 18px;margin-bottom:10px;">{inner}</div>'
        )

    def mcq_html(q, stem_html):
        user = _exam2_choice(sel, q["id"]).get("index")
        if isinstance(user, str) and user.isdigit():
            user = int(user)
        accepted = _accepted_indexes(q)
        opts = ""
        for oi, opt in enumerate(q.get("options", [])):
            if oi in accepted:
                mark, bg, bd, color = "✅", "#f0fdf4", "#22c55e", "#14532d"
            elif user == oi:
                mark, bg, bd, color = "❌", "#fef2f2", "#ef4444", "#7f1d1d"
            else:
                mark, bg, bd, color = "", "#f8fafc", "#e2e8f0", "#374151"
            opts += (
                f'<div style="display:flex;gap:8px;align-items:center;background:{bg};'
                f'border:1.5px solid {bd};border-radius:10px;padding:8px 12px;margin:5px 0;'
                f'color:{color};font-weight:600;font-size:0.95rem;">'
                f'<span style="min-width:20px;">{mark}</span>'
                f'<span style="{zh}">{_exam2_esc(opt)}</span></div>'
            )
        return qcard(
            f'<div style="font-weight:800;color:#0f172a;margin-bottom:6px;">{stem_html}</div>'
            f"{opts}"
            f'<div style="{note_style}">{_exam2_esc(q.get("exp", ""))}</div>'
        )

    def tf_html(q, idx):
        user = _exam2_choice(sel, q["id"]).get("value")
        correct = "Đúng (Đ)" if q.get("ans") == "D" else "Sai (S)"
        user_txt = "Đúng (Đ)" if user == "D" else ("Sai (S)" if user == "S" else "(bỏ trống)")
        ok = user == q.get("ans")
        color = "#15803d" if ok else "#b91c1c"
        return qcard(
            f'<div style="font-weight:800;color:#0f172a;">{idx}. '
            f'<span style="{zh}font-size:1.1rem;">{_exam2_esc(q.get("zh", ""))}</span> '
            f'<span style="color:#64748b;font-weight:600;">({_exam2_esc(q.get("py", ""))})</span></div>'
            f'<div style="color:#475569;font-size:0.9rem;margin:4px 0 8px 0;">{_exam2_esc(q.get("vi", ""))}</div>'
            f'<div style="font-size:0.9rem;">Học viên chọn: <b style="color:{color};">{user_txt}</b>'
            f' &nbsp;|&nbsp; Đáp án: <b>{correct}</b></div>'
            f'<div style="{note_style}">{_exam2_esc(q.get("exp", ""))}</div>'
        )

    # ---------- PHẦN I: Từ vựng ----------
    qs = data.get("part1Data", [])
    if qs:
        out.append("<h4 style='color:#1d4ed8;margin:18px 0 8px 0;'>Phần I. Chọn nghĩa đúng của từ vựng</h4>")
        for i, q in enumerate(qs, 1):
            stem = (
                f'<span style="color:#2563eb;font-weight:800;">{i}.</span> '
                f'<span style="{zh}font-size:1.2rem;font-weight:800;">{_exam2_esc(q.get("zh", ""))}</span> '
                f'<span style="color:#64748b;">({_exam2_esc(q.get("py", ""))})</span>'
            )
            out.append(mcq_html(q, stem))

    # ---------- PHẦN II: Đúng/Sai ----------
    qs = data.get("part2Data", [])
    if qs:
        out.append("<h4 style='color:#1d4ed8;margin:18px 0 8px 0;'>Phần II. Đọc câu chọn Đúng/Sai</h4>")
        for i, q in enumerate(qs, 1):
            out.append(tf_html(q, i))

    # ---------- PHẦN III: Sắp xếp câu ----------
    qs = data.get("part3Data", [])
    if qs:
        out.append("<h4 style='color:#1d4ed8;margin:18px 0 8px 0;'>Phần III. Sắp xếp từ thành câu</h4>")
        for i, q in enumerate(qs, 1):
            user_words = _exam2_order(sel, q["id"])
            user_sent = "".join(user_words).replace(" ", "")
            target = (q.get("correct") or "").replace(" ", "")
            ok = user_sent == target and bool(user_sent)
            user_disp = " ".join(user_words) if user_words else "(bỏ trống)"
            tokens = " ".join(str(tok) for tok in (q.get("tokens") or []))
            color = "#15803d" if ok else "#b91c1c"
            out.append(qcard(
                f'<div style="font-weight:800;color:#0f172a;margin-bottom:6px;">{i}. Sắp xếp các từ: '
                f'<span style="{zh}color:#64748b;font-weight:600;">{_exam2_esc(tokens)}</span></div>'
                f'<div style="font-size:0.95rem;">Học viên xếp: '
                f'<b style="{zh}color:{color};">{_exam2_esc(user_disp)}</b></div>'
                f'<div style="font-size:0.95rem;margin-top:4px;">Câu đúng: '
                f'<b style="{zh}color:#15803d;">{_exam2_esc(q.get("correct", ""))}</b></div>'
                f'<div style="{note_style}">{_exam2_esc(q.get("exp", ""))}</div>'
            ))

    # ---------- PHẦN IV: Đúng/Sai ----------
    qs = data.get("part4Data", [])
    if qs:
        out.append("<h4 style='color:#1d4ed8;margin:18px 0 8px 0;'>Phần IV. Đối chiếu nghĩa Trung - Việt</h4>")
        for i, q in enumerate(qs, 1):
            out.append(tf_html(q, i))

    # ---------- PHẦN V: Đọc hiểu ----------
    qs = data.get("part5Data", [])
    if qs:
        passage = data.get("passageText", "")
        out.append("<h4 style='color:#1d4ed8;margin:18px 0 8px 0;'>Phần V. Đọc hiểu đoạn văn</h4>")
        if passage:
            out.append(
                '<div style="background:#fff9db;border:1px solid #ffe066;border-left:5px solid #f59f00;'
                'border-radius:10px;padding:14px 18px;margin-bottom:10px;">'
                '<div style="font-weight:800;color:#d9480f;margin-bottom:6px;">📖 Đoạn văn</div>'
                f'<div style="{zh}font-size:1.05rem;line-height:1.9;">{_exam2_esc(passage)}</div></div>'
            )
        for i, q in enumerate(qs, 1):
            stem = (
                f'<span style="color:#2563eb;font-weight:800;">{i}.</span> '
                f'<span style="{zh}font-size:1.1rem;font-weight:800;">{_exam2_esc(q.get("q_zh", ""))}</span> '
                f'<span style="color:#64748b;">({_exam2_esc(q.get("q_py", ""))})</span>'
            )
            out.append(mcq_html(q, stem))

    # ---------- PHẦN VIII: Ngữ pháp ----------
    qs = data.get("part8Data", [])
    if qs:
        out.append("<h4 style='color:#1d4ed8;margin:18px 0 8px 0;'>Phần VI. Ngữ pháp điền từ</h4>")
        for i, q in enumerate(qs, 1):
            stem = (
                f'<span style="color:#2563eb;font-weight:800;">{i}.</span> '
                f'<span style="{zh}font-size:1.15rem;font-weight:800;letter-spacing:1px;">'
                f'{_exam2_esc(q.get("q", ""))}</span>'
            )
            out.append(mcq_html(q, stem))

    return "".join(out) if out else "<p>Không có dữ liệu câu hỏi.</p>"


# POPUP DIALOG CHO HỌC VIÊN ĐIỀN TÊN KHI HOÀN THÀNH BÀI THI
@st.dialog("📝 Nộp bài & Lưu điểm", dismissible=True)
def popup_submit_score(score_display, questions, save_progress, save_score_row_hsk1_consolidated):
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 18px;">
        <span style="font-size: 2.2rem;">🎉</span>
        <h3 style="margin: 6px 0 10px 0; color: #1e3a8a; font-size: 1.5rem; font-weight: 800;">
            Kết quả: <span style="color: #15803d;">{score_display}</span>
        </h3>
        <p style="color: #64748b; font-size: 0.95rem; margin-bottom: 0;">Điền họ và tên học viên để lưu điểm vào hệ thống:</p>
    </div>
    """, unsafe_allow_html=True)

    name = st.text_input("Họ và tên học viên *:", placeholder="Ví dụ: Nguyễn Văn A", key="popup_student_name_input")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("💾 Lưu điểm", type="primary", use_container_width=True):
            clean_name = name.strip() if name else ""
            if clean_name:
                now_str = datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S")

                # 1. Lưu vào Supabase: chỉ lưu tên và điểm (câu đúng/50)
                saved_sb, msg_sb = supabase_client.save_score_to_supabase(
                    student_name=clean_name,
                    score_str=score_display
                )

                # 2. Lưu dự phòng vào CSV
                row_csv = {
                    "thời gian": now_str,
                    "học viên": clean_name,
                    "Đề kiểm tra": "Ôn tập bài cũ (50 câu)",
                    "tổng điểm": score_display,
                    "Kết quả": score_display
                }
                save_score_row_hsk1_consolidated(row_csv)

                st.session_state.hsk1_quiz_submitted = True
                st.session_state.submitted_student_name = clean_name
                save_progress()
                st.rerun()
            else:
                st.error("⚠️ Vui lòng điền họ và tên trước khi lưu điểm!")
    with col2:
        if st.button("🔄 Làm lại bài", use_container_width=True):
            st.session_state.hsk1_quiz_idx = 0
            st.session_state.hsk1_quiz_answers = [None] * len(questions)
            st.session_state.hsk1_quiz_score = 0
            st.session_state.hsk1_quiz_submitted = False
            save_progress()
            st.rerun()


EXAM2_PARTS = [
    ("1", "I. Từ vựng (10 câu)", "I. Chọn nghĩa đúng của từ vựng", "10 câu • 10 điểm"),
    ("2", "II. Đúng / Sai (10 câu)", "II. Đọc câu và chọn Đúng hoặc Sai", "10 câu • 10 điểm"),
    ("3", "III. Sắp xếp câu (10 câu)", "III. Sắp xếp từ thành câu", "10 câu • 10 điểm"),
    ("4", "IV. Đúng / Sai (10 câu)", "IV. Đối chiếu nghĩa Trung - Việt", "10 câu • 10 điểm"),
    ("5", "V. Đọc hiểu đoạn văn (5 câu)", "V. Đọc hiểu đoạn văn", "5 câu • 5 điểm"),
    ("8", "VI. Ngữ pháp (10 câu)", "VI. Chọn từ thích hợp điền vào chỗ trống", "10 câu • 10 điểm"),
    ("9", "VII. Viết đoạn văn ngắn giới thiệu bản thân (tự luận)", "VII. Viết đoạn văn ngắn giới thiệu bản thân", "Tự luận • 5 điểm"),
    ("full", "🏁 Nộp bài & Xem kết quả (toàn bộ đề)", "Toàn bộ đề", ""),
]
EXAM2_LABEL_BY_KEY = {key: label for key, label, _title, _meta in EXAM2_PARTS}
EXAM2_ORDER = [key for key, _label, _title, _meta in EXAM2_PARTS]
EXAM2_PASSAGE_PINYIN = (
    "Wǒ jiào Lǐ Míng, jīnnián èrshí suì, shì yì míng dàxuéshēng. "
    "Wǒ zài Běijīng de yì suǒ dàxué xuéxí Hànyǔ. Wǒ de zhuānyè shì Zhōngwén, "
    "wǒ hěn xǐhuan Hànyǔ hé Zhōngguó wénhuà. Wǒ de jiā yǒu sì kǒu rén: bàba, māma, "
    "wǒ hé mèimei. Wǒ de mèimei jīnnián shíwǔ suì, shì yì míng zhōngxuéshēng. "
    "Tā yě xǐhuan xuéxí Hànyǔ. Wǒmen chángcháng yìqǐ kàn diànyǐng, tīng yīnyuè, "
    "yǒu shíhou yě qù gōngyuán sànbù. Zhōumò wǒ xǐhuan qù túshūguǎn kàn shū, "
    "huòzhě hé péngyou qù dǎ lánqiú."
)
EXAM2_SAMPLE_ESSAY = """你好！我叫阮明，今年二十一岁，是一名大学生。
我很喜欢学习汉语，也喜欢看中国电影。
我家有四口人：爸爸、妈妈、哥哥和我。
周末我常常和朋友去图书馆看书，有时候也去公园散步。
很高兴认识大家！"""


def _exam2_full_width():
    st.markdown(
        """
        <style>
        .block-container, [data-testid="stMainBlockContainer"] {
            max-width: 100% !important;
            padding-left: 0.75rem !important;
            padding-right: 0.75rem !important;
        }
        .exam2-zh {
            font-family: "Microsoft YaHei", "PingFang SC", "Noto Sans SC", sans-serif;
        }
        [class*="st-key-e2order_"] iframe {
            width: 118px !important;
            min-width: 118px;
        }
        [class*="st-key-e2order_"] {
            max-width: 760px;
            background: #ffffff;
            border: 1px solid #e2e8f0 !important;
            border-radius: 18px !important;
            padding: 16px 18px 12px 18px !important;
            margin: 0 0 16px 0;
            box-shadow: 0 6px 18px rgba(15, 23, 42, 0.04);
        }
        .exam2-order-title {
            font-size: 1rem;
            font-weight: 700;
            color: #0f172a;
            line-height: 1.5;
            margin-bottom: 2px;
        }
        .exam2-order-title span {
            display: inline-block;
            background: #1d4ed8;
            color: #ffffff;
            border-radius: 999px;
            padding: 2px 10px;
            margin-right: 8px;
            font-size: 0.82rem;
            letter-spacing: 0.02em;
        }
        .exam2-order-preview {
            font-size: 1.85rem;
            font-weight: 800;
            line-height: 1.55;
            color: #0f172a;
            background: #f8fbff;
            border: 1.5px solid #dbeafe;
            border-radius: 14px;
            padding: 14px 16px;
            margin: 8px 0 4px 0;
        }
        .exam2-order-joined {
            color: #64748b;
            font-size: 1.02rem;
            margin: 0 2px 8px 2px;
        }
        .exam2-order-empty {
            color: #64748b;
            background: #f8fafc;
            border: 1.5px dashed #cbd5e1;
            border-radius: 14px;
            padding: 16px;
            margin: 8px 0 10px 0;
            line-height: 1.5;
        }
        .exam2-order-label {
            font-size: 0.82rem;
            font-weight: 700;
            letter-spacing: 0.03em;
            text-transform: uppercase;
            color: #64748b;
            margin: 8px 0 2px 0;
        }
        [class*="st-key-e2slot_"] [data-testid="stHorizontalBlock"],
        [class*="st-key-e2bank_"] [data-testid="stHorizontalBlock"] {
            flex-wrap: wrap;
            gap: 8px;
        }
        [class*="st-key-e2slot_"] [data-testid="stColumn"],
        [class*="st-key-e2bank_"] [data-testid="stColumn"] {
            width: fit-content !important;
            flex: 0 0 auto !important;
        }
        [class*="st-key-e2slot_"] div.stButton > button,
        [class*="st-key-e2bank_"] div.stButton > button {
            width: auto !important;
            min-height: 48px;
            border-radius: 12px !important;
            font-family: "Microsoft YaHei", "PingFang SC", "Noto Sans SC", sans-serif !important;
            font-size: 1.3rem !important;
            font-weight: 700 !important;
            padding: 0.3rem 0.95rem !important;
            white-space: nowrap;
        }
        [class*="st-key-e2slot_"] div.stButton > button {
            background: #eff6ff !important;
            color: #1e3a8a !important;
            border: 1.5px solid #60a5fa !important;
        }
        [class*="st-key-e2bank_"] div.stButton > button {
            background: #ffffff !important;
            color: #0f172a !important;
            border: 1.5px solid #cbd5e1 !important;
        }
        [class*="st-key-e2bank_"] div.stButton > button:hover,
        [class*="st-key-e2slot_"] div.stButton > button:hover {
            border-color: #2563eb !important;
            background: #f8fafc !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _fresh_exam2_work(data, attempt_id):
    banks = {}
    for q in data.get("part3Data") or []:
        tokens = list(q.get("tokens") or [])
        random.Random(f"{attempt_id}:{q.get('id')}").shuffle(tokens)
        banks[q.get("id")] = tokens
    return {"attempt_id": attempt_id, "choices": {}, "orders": {}, "banks": banks}


def _exam2_work(data, attempt_id):
    work = st.session_state.get("hsk1_exam2_work")
    if not isinstance(work, dict) or work.get("attempt_id") != attempt_id:
        work = _fresh_exam2_work(data, attempt_id)
        st.session_state.hsk1_exam2_work = work
    return work


def _exam2_mcq_correct(q, user):
    if q.get("id") == "8_6":
        return user in (1, 3)
    if q.get("id") == "8_8":
        return user == 3
    return user == q.get("ans")


def _exam2_scores(data, work):
    choices = work.get("choices") or {}
    orders = work.get("orders") or {}
    banks = work.get("banks") or {}

    def count_mcq(questions):
        return sum(1 for q in questions if _exam2_mcq_correct(q, choices.get(q.get("id"))))

    def count_tf(questions):
        return sum(1 for q in questions if choices.get(q.get("id")) == q.get("ans"))

    p3 = 0
    for q in data.get("part3Data") or []:
        picked = orders.get(q.get("id")) or []
        bank = banks.get(q.get("id")) or []
        built = "".join(bank[i] for i in picked if isinstance(i, int) and 0 <= i < len(bank))
        target = (q.get("correct") or "").replace(" ", "")
        if built and built.replace(" ", "") == target:
            p3 += 1
    return {
        "p1": count_mcq(data.get("part1Data") or []),
        "p2": count_tf(data.get("part2Data") or []),
        "p3": p3,
        "p4": count_tf(data.get("part4Data") or []),
        "p5": count_mcq(data.get("part5Data") or []),
        "p8": count_mcq(data.get("part8Data") or []),
    }


def _exam2_export(data, work):
    choices = work.get("choices") or {}
    saved = {}
    for q in (data.get("part1Data") or []) + (data.get("part5Data") or []) + (data.get("part8Data") or []):
        idx = choices.get(q.get("id"))
        options = q.get("options") or []
        if isinstance(idx, int) and 0 <= idx < len(options):
            saved[q["id"]] = {"type": "mcq", "index": idx, "text": options[idx]}
    for q in (data.get("part2Data") or []) + (data.get("part4Data") or []):
        val = choices.get(q.get("id"))
        if val in ("D", "S"):
            saved[q["id"]] = {"type": "tf", "value": val, "text": "Đúng (Đ)" if val == "D" else "Sai (S)"}
    orders = {}
    banks = work.get("banks") or {}
    for q in data.get("part3Data") or []:
        picked = (work.get("orders") or {}).get(q.get("id")) or []
        bank = banks.get(q.get("id")) or []
        words = [bank[i] for i in picked if isinstance(i, int) and 0 <= i < len(bank)]
        if words:
            orders[q["id"]] = words
    return saved, orders


def _save_exam2_submission(student_name):
    data = _load_exam2_data()
    work = st.session_state.get("hsk1_exam2_work") or {}
    client = supabase_client.get_supabase_client()
    if not client:
        return False, "Chưa kết nối được nơi lưu bài."
    scores = _exam2_scores(data, work)
    saved_choices, saved_orders = _exam2_export(data, work)
    attempt_id = work.get("attempt_id") or _query_param("hsk1_exam2")
    essay_key = f"hsk1e2_essay_{attempt_id}"
    essay = st.session_state.get(essay_key, "")
    total = sum(scores.values())
    payload = {
        "student_name": student_name,
        "score": total,
        "max_score": 55,
        "part_scores": scores,
        "answers": {
            "v": 2,
            "attempt_id": attempt_id,
            "status": "submitted",
            "display_name": student_name,
            "choices": saved_choices,
        },
        "order_answers": saved_orders,
        "essay": essay,
        "submitted_at": datetime.now(timezone.utc).isoformat(),
    }
    try:
        client.table("hsk1_exam2_answers").insert(payload).execute()
        return True, ""
    except Exception as exc:
        return False, f"Chưa lưu được bài: {exc}"


def _dismiss_exam2_dialog():
    st.session_state.hsk1_exam2_open_submit = False


@st.dialog("Nộp bài", on_dismiss=_dismiss_exam2_dialog)
def _exam2_submit_dialog():
    st.markdown("Điền họ và tên học viên để lưu bài làm.")
    name = st.text_input("Họ và tên học viên *", placeholder="Nguyễn Văn A", key="hsk1_exam2_modal_name")
    if st.button("💾 Lưu đáp án & điểm", type="primary", use_container_width=True, key="hsk1_exam2_modal_save"):
        clean = (name or "").strip()
        if not clean:
            st.error("Vui lòng điền họ và tên trước khi lưu.")
            return
        ok, message = _save_exam2_submission(clean)
        if ok:
            st.session_state.hsk1_exam2_open_submit = False
            _return_to_hsk1_review_menu(saved=True)
            st.rerun()
        st.error(message)


def _return_to_hsk1_review_menu(saved=False):
    st.session_state.hsk1_exam_view = "menu"
    if saved:
        st.session_state.hsk1_exam2_notice = "Đã lưu bài làm."
    if "hsk1_exam2" in st.query_params:
        del st.query_params["hsk1_exam2"]


def _render_exam2_back_button():
    st.markdown(
        """
        <style>
        div.st-key-hsk1_exam2_back_menu {
            position: sticky;
            top: 3.4rem;
            z-index: 999;
            background: #ffffff;
            padding: 8px 0 10px 0;
            margin-bottom: 8px;
            border-bottom: 1px solid #e2e8f0;
        }
        div.st-key-hsk1_exam2_back_menu button {
            background: #eff6ff !important;
            color: #1e3a8a !important;
            border: 1.5px solid #93c5fd !important;
            font-weight: 700 !important;
        }
        div.st-key-hsk1_exam2_back_menu button:hover {
            background: #dbeafe !important;
            border-color: #2563eb !important;
            color: #1e3a8a !important;
        }
        div.st-key-hsk1_exam2_saved_back {
            position: absolute !important;
            width: 1px !important;
            height: 1px !important;
            overflow: hidden !important;
            opacity: 0 !important;
            pointer-events: none !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    if st.button(
        "⬅️ Quay lại 📝 Bài Tập Trắc Nghiệm",
        key="hsk1_exam2_back_menu",
        use_container_width=True,
    ):
        _return_to_hsk1_review_menu(saved=False)
        st.rerun()
    if st.button("Đã lưu, quay lại", key="hsk1_exam2_saved_back"):
        _return_to_hsk1_review_menu(saved=True)
        st.rerun()


def _exam2_center_button(label, key):
    _left, mid, _right = st.columns([1, 2, 1])
    with mid:
        return st.button(label, type="primary", key=key, use_container_width=True)


def _exam2_pick(work, qid, value):
    work.setdefault("choices", {})[qid] = value
    st.rerun()


def _render_exam2_mcq(questions, work, attempt_id, stem_fn):
    choices = work.setdefault("choices", {})
    for i, q in enumerate(questions, 1):
        qid = q.get("id")
        with st.container(border=True):
            left, right = st.columns([8, 2])
            with left:
                st.markdown(stem_fn(i, q), unsafe_allow_html=True)
            with right:
                sound = q.get("zh") or q.get("q_zh") or q.get("q") or ""
                if sound:
                    render_play_button(sound, "🔊 Nghe", key=f"e2_audio_{attempt_id}_{qid}", height=42)
            options = q.get("options") or []
            cols = st.columns(2)
            for oi, opt in enumerate(options):
                with cols[oi % 2]:
                    picked = choices.get(qid) == oi
                    if st.button(
                        opt,
                        key=f"e2opt_{attempt_id}_{qid}_{oi}",
                        type="primary" if picked else "secondary",
                        use_container_width=True,
                    ):
                        _exam2_pick(work, qid, oi)


def _render_exam2_tf(questions, work, attempt_id):
    choices = work.setdefault("choices", {})
    for i, q in enumerate(questions, 1):
        qid = q.get("id")
        with st.container(border=True):
            left, right = st.columns([8, 2])
            with left:
                st.markdown(
                    f"<div class='exam2-zh' style='font-size:1.35rem;font-weight:800;'>{i}. {q.get('zh','')}</div>"
                    f"<div style='color:#64748b;margin:4px 0 8px 0;'>{q.get('py','')}</div>"
                    f"<div style='font-size:1.05rem;'>{q.get('vi','')}</div>",
                    unsafe_allow_html=True,
                )
            with right:
                render_play_button(q.get("zh") or "", "🔊 Nghe", key=f"e2_audio_{attempt_id}_{qid}", height=42)
            yes, no = st.columns(2)
            with yes:
                if st.button(
                    "Đúng (Đ)",
                    key=f"e2tf_{attempt_id}_{qid}_D",
                    type="primary" if choices.get(qid) == "D" else "secondary",
                    use_container_width=True,
                ):
                    _exam2_pick(work, qid, "D")
            with no:
                if st.button(
                    "Sai (S)",
                    key=f"e2tf_{attempt_id}_{qid}_S",
                    type="primary" if choices.get(qid) == "S" else "secondary",
                    use_container_width=True,
                ):
                    _exam2_pick(work, qid, "S")


_EXAM2_ORDER_MARKS = "①②③④⑤⑥⑦⑧⑨⑩"


def _render_exam2_order(questions, work, attempt_id):
    banks = work.setdefault("banks", {})
    orders = work.setdefault("orders", {})
    for i, q in enumerate(questions, 1):
        qid = q.get("id")
        bank = banks.get(qid) or list(q.get("tokens") or [])
        banks[qid] = bank
        picked = list(orders.get(qid) or [])
        words = [bank[n] for n in picked if isinstance(n, int) and 0 <= n < len(bank)]
        with st.container(border=True, key=f"e2order_{qid}"):
            head, audio = st.columns([5.2, 1.3])
            with head:
                st.markdown(
                    f"<div class='exam2-order-title'><span>Câu {i}</span>Xếp các từ thành một câu hoàn chỉnh</div>",
                    unsafe_allow_html=True,
                )
            with audio:
                render_play_button(q.get("correct") or "", "🔊 Nghe", key=f"e2_audio_{attempt_id}_{qid}", height=42)
            if words:
                st.markdown(
                    f"<div class='exam2-order-preview exam2-zh'>{'　'.join(words)}</div>"
                    f"<div class='exam2-order-joined exam2-zh'>Câu liền: {''.join(words)}</div>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    "<div class='exam2-order-empty'>Chưa xếp từ nào. Bấm các từ trong kho theo đúng thứ tự.</div>",
                    unsafe_allow_html=True,
                )
            if picked:
                st.markdown("<div class='exam2-order-label'>Đã xếp — bấm để bỏ từ</div>", unsafe_allow_html=True)
                with st.container(key=f"e2slot_{qid}"):
                    cols = st.columns(len(picked))
                    for pos, bank_i in enumerate(picked):
                        mark = _EXAM2_ORDER_MARKS[pos] if pos < len(_EXAM2_ORDER_MARKS) else f"{pos + 1}."
                        with cols[pos]:
                            if st.button(f"{mark} {bank[bank_i]}", key=f"e2rm_{attempt_id}_{qid}_{pos}"):
                                picked.pop(pos)
                                orders[qid] = picked
                                st.rerun()
            remain = [n for n in range(len(bank)) if n not in picked]
            if remain:
                st.markdown("<div class='exam2-order-label'>Kho từ — bấm để thêm vào cuối câu</div>", unsafe_allow_html=True)
                with st.container(key=f"e2bank_{qid}"):
                    cols = st.columns(len(remain))
                    for n, bank_i in enumerate(remain):
                        with cols[n]:
                            if st.button(bank[bank_i], key=f"e2add_{attempt_id}_{qid}_{bank_i}"):
                                picked.append(bank_i)
                                orders[qid] = picked
                                st.rerun()
            if picked and st.button("Xếp lại từ đầu", key=f"e2reset_{attempt_id}_{qid}"):
                orders[qid] = []
                st.rerun()


def _render_exam2_essay(attempt_id):
    st.markdown(
        """
        **Gợi ý dàn ý**
        - Tên, tuổi (我叫..., 今年...岁)
        - Nghề nghiệp hoặc là học sinh, sinh viên
        - Gia đình có mấy người
        - Sở thích
        - Hoạt động hằng ngày hoặc cuối tuần
        """
    )
    essay = st.text_area(
        "Bài viết",
        height=260,
        placeholder="Nhập bài viết bằng chữ Hán tại đây (ví dụ: 你好！我叫王华，今年二十岁...)",
        key=f"hsk1e2_essay_{attempt_id}",
        label_visibility="collapsed",
    )
    compact = "".join((essay or "").split())
    marked = essay or ""
    for sep in "。？！.?!":
        marked = marked.replace(sep, "|")
    sentences = len([part for part in marked.split("|") if part.strip()]) if (essay or "").strip() else 0
    st.caption(f"Số ký tự: {len(compact)} chữ | Ước tính: {sentences} câu")
    with st.expander("Xem đoạn văn mẫu tham khảo"):
        st.markdown(f"<div class='exam2-zh' style='font-size:1.2rem;line-height:1.8;'>{EXAM2_SAMPLE_ESSAY.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)
        st.caption("Xin chào! Tôi tên là Nguyễn Minh, năm nay 21 tuổi, là sinh viên đại học. Tôi rất thích học tiếng Trung, cũng thích xem phim Trung Quốc. Nhà tôi có 4 người: bố, mẹ, anh trai và tôi. Cuối tuần tôi thường cùng bạn đến thư viện đọc sách, thỉnh thoảng cũng đi công viên dạo bộ. Rất vui được làm quen với mọi người!")


def _render_exam2_section(part_key, data, work, attempt_id):
    if part_key == "1":
        _render_exam2_mcq(
            data.get("part1Data") or [],
            work,
            attempt_id,
            lambda i, q: (
                f"<div class='exam2-zh' style='font-size:1.7rem;font-weight:800;'>{i}. {q.get('zh','')}</div>"
                f"<div style='color:#64748b;margin-top:4px;'>{q.get('py','')}</div>"
            ),
        )
    elif part_key == "2":
        _render_exam2_tf(data.get("part2Data") or [], work, attempt_id)
    elif part_key == "3":
        _render_exam2_order(data.get("part3Data") or [], work, attempt_id)
    elif part_key == "4":
        _render_exam2_tf(data.get("part4Data") or [], work, attempt_id)
    elif part_key == "5":
        passage = data.get("passageText") or ""
        st.markdown(
            f"<div style='background:#fff9db;border:1px solid #ffe066;border-left:6px solid #f59f00;border-radius:12px;padding:16px 18px;'>"
            f"<div style='font-weight:800;color:#d9480f;margin-bottom:8px;'>Đoạn văn</div>"
            f"<div class='exam2-zh' style='font-size:1.25rem;line-height:1.9;'>{passage}</div>"
            f"<div style='color:#64748b;margin-top:8px;'>{EXAM2_PASSAGE_PINYIN}</div></div>",
            unsafe_allow_html=True,
        )
        render_play_button(passage, "🔊 Nghe bài đọc", key=f"e2_passage_{attempt_id}", height=42)
        _render_exam2_mcq(
            data.get("part5Data") or [],
            work,
            attempt_id,
            lambda i, q: (
                f"<div class='exam2-zh' style='font-size:1.3rem;font-weight:800;'>{i}. {q.get('q_zh','')}</div>"
                f"<div style='color:#64748b;margin-top:4px;'>{q.get('q_py','')}</div>"
            ),
        )
    elif part_key == "8":
        _render_exam2_mcq(
            data.get("part8Data") or [],
            work,
            attempt_id,
            lambda i, q: f"<div class='exam2-zh' style='font-size:1.45rem;font-weight:800;letter-spacing:1px;'>{i}. {q.get('q','')}</div>",
        )
    elif part_key == "9":
        _render_exam2_essay(attempt_id)


def _show_hsk1_exam2(attempt_id):
    _exam2_full_width()
    _render_exam2_back_button()
    data = _load_exam2_data()
    if not data:
        st.error("Không đọc được dữ liệu Đề 2.")
        return
    work = _exam2_work(data, attempt_id)
    notice = st.session_state.pop("hsk1_exam2_notice", None)
    if notice:
        st.success(notice)

    labels = [label for _key, label, _title, _meta in EXAM2_PARTS]
    pending = st.session_state.pop("hsk1_exam2_pending", None)
    if pending in labels:
        st.session_state.hsk1_exam2_part = pending
    part_label = st.selectbox(
        "Chọn phần của bài test:",
        labels,
        key="hsk1_exam2_part",
    )
    part_key = dict((label, key) for key, label, _title, _meta in EXAM2_PARTS)[part_label]
    title = dict((key, title) for key, _label, title, _meta in EXAM2_PARTS)[part_key]
    meta = dict((key, meta) for key, _label, _title, meta in EXAM2_PARTS)[part_key]

    idx = EXAM2_ORDER.index(part_key)
    if part_key != "full" and idx + 1 < len(EXAM2_ORDER) and EXAM2_ORDER[idx + 1] != "full":
        nxt = EXAM2_ORDER[idx + 1]
        if _exam2_center_button("➡️ Sang phần tiếp theo", f"hsk1_next_{part_key}"):
            st.session_state.hsk1_exam2_pending = EXAM2_LABEL_BY_KEY[nxt]
            st.rerun()
    elif _exam2_center_button("✅ Nộp bài & Chấm điểm", f"hsk1_submit_{part_key}"):
        st.session_state.hsk1_exam2_open_submit = True

    done = len(work.get("choices") or {}) + sum(1 for words in (work.get("orders") or {}).values() if words)
    st.caption(f"Đã làm {done}/55 câu trắc nghiệm")
    if part_key != "full":
        st.markdown(f"### {title}")
        if meta:
            st.caption(meta)
        _render_exam2_section(part_key, data, work, attempt_id)
    else:
        for key, _label, section_title, section_meta in EXAM2_PARTS:
            if key == "full":
                continue
            st.markdown(f"### {section_title}")
            if section_meta:
                st.caption(section_meta)
            _render_exam2_section(key, data, work, attempt_id)

    if st.session_state.get("hsk1_exam2_open_submit"):
        _exam2_submit_dialog()


def _show_scoreboard_quiz(load_all_scores_hsk1_consolidated):
    """Hiển thị bảng điểm tổng hợp cả Đề 1 và Đề 2."""
    st.subheader("🏆 Bảng điểm tổng hợp")
    # --- Đề 2 Supabase ---
    with st.expander("📋 Bài làm đã nộp - Đề 2 (Bài test HSK 1)", expanded=True):
        try:
            sb_client = supabase_client.get_supabase_client()
            if sb_client:
                rows = _load_exam2_submissions()
                if not rows:
                    st.info("Chưa có bài nộp nào (Đề 2).")
                else:
                    overview = [{
                        "Học viên": r.get("student_name", "Ẩn danh"),
                        "Đã làm": len((_as_dict(r.get("answers")).get("choices") or {})) + len(_as_dict(r.get("order_answers"))),
                        "Điểm": f"{r.get('score', 0)}/{r.get('max_score', 55)}",
                        "Phần I": (r.get("part_scores") or {}).get("p1", "-"),
                        "Phần II": (r.get("part_scores") or {}).get("p2", "-"),
                        "Phần III": (r.get("part_scores") or {}).get("p3", "-"),
                        "Phần IV": (r.get("part_scores") or {}).get("p4", "-"),
                        "Phần V": (r.get("part_scores") or {}).get("p5", "-"),
                        "Phần VI": (r.get("part_scores") or {}).get("p8", "-"),
                        "Thời gian": str(r.get("submitted_at", "")).split(".")[0].replace("T", " "),
                    } for r in rows]
                    st.dataframe(overview, use_container_width=True)
                    labels = [f"{r.get('student_name','Ẩn danh')} — {r.get('score',0)}/{r.get('max_score',55)} — {str(r.get('submitted_at','')).split('T')[0]}" for r in rows]
                    pick = st.selectbox("Chọn bài để xem chi tiết:", labels, key="hsk1_exam2_pick_scoreboard")
                    sel = rows[labels.index(pick)]
                    st.markdown("**Bài tự luận (Phần VII):**")
                    st.text_area("Essay", value=sel.get("essay") or "(không có)", height=180, disabled=True, key="hsk1_essay_view_scoreboard")
                    st.markdown("#### Chi tiết đáp án và chấm từng câu")
                    st.html(render_exam2_review(sel))
            else:
                st.warning("Chưa kết nối được Supabase.")
        except Exception as e:
            st.error(f"Lỗi tải bài nộp: {e}")
    # --- Đề 1 CSV ---
    with st.expander("📊 Bảng điểm Đề 1 (50 câu trắc nghiệm)", expanded=False):
        scores_data = []
        if supabase_client.is_supabase_configured():
            scores_data = supabase_client.load_scores_from_supabase()
        if not scores_data:
            raw_csv = load_all_scores_hsk1_consolidated()
            for r in raw_csv:
                scores_data.append({
                    "Thời gian": r.get("thời gian", ""),
                    "Học viên": r.get("học viên", ""),
                    "Điểm": r.get("Kết quả") or r.get("tổng điểm", "")
                })
        if scores_data:
            st.dataframe(scores_data, use_container_width=True)
        else:
            st.info("Chưa có lượt nộp điểm nào (Đề 1).")


def _show_exam2_section():
    """Hiển thị Đề 2 - Bài test HSK 1 (55 câu + tự luận) trực tiếp từ sidebar."""
    _render_exam2_back_button()
    attempt_id = _query_param("hsk1_exam2")
    if not attempt_id:
        attempt_id = uuid.uuid4().hex
        st.query_params["hsk1_exam2"] = attempt_id
        st.rerun()

    part_options = [
        ("I. Từ vựng (10 câu)", "1"),
        ("II. Đúng / Sai (10 câu)", "2"),
        ("III. Sắp xếp câu (10 câu)", "3"),
        ("IV. Đúng / Sai (10 câu)", "4"),
        ("V. Đọc hiểu đoạn văn (5 câu)", "5"),
        ("VI. Ngữ pháp (10 câu)", "8"),
        ("VII. Viết đoạn văn ngắn giới thiệu bản thân (tự luận)", "9"),
        ("🏁 Nộp bài & Xem kết quả (toàn bộ đề)", "full"),
    ]
    part_labels = [p[0] for p in part_options]
    pending_part = st.session_state.pop("hsk1_exam2_pending", None)
    if pending_part in part_labels:
        st.session_state.hsk1_exam2_part = pending_part
    part_choice = st.selectbox(
        "Chọn phần của bài test:",
        part_labels,
        key="hsk1_exam2_part",
    )
    only_part = dict(part_options)[part_choice]

    html_path = Path(__file__).resolve().parent.parent / "bai_test_hsk1.html"
    if html_path.exists():
        html_content = html_path.read_text(encoding="utf-8")
        inject_parts = ["<style>body{padding-bottom:0 !important;}</style>"]
        try:
            sb_cfg = supabase_client.get_supabase_config()
            inject_parts.append(
                f"<script>window.__SUPABASE_URL__='{sb_cfg['url']}';"
                f"window.__SUPABASE_KEY__='{sb_cfg['key']}';"
                f"window.__EXAM2_TABLE__='hsk1_exam2_answers';"
                f"window.__EXAM_ATTEMPT_ID__='{attempt_id}';</script>"
            )
        except Exception:
            pass
        if st.session_state.pop("hsk1_exam2_submit", False):
            inject_parts.append("<script>window.__EXAM_AUTO_SUBMIT__=true;</script>")
        if only_part != "full":
            inject_parts.append(f"<script>window.__EXAM_ONLY_PART__='{only_part}';</script>")
        else:
            inject_parts.append("<style>.bottom-bar{position:static !important;}</style>")
        inject_parts.append("""
<script>
(function(){
  function fit(){
    try{
      var h = document.body ? document.body.scrollHeight : 0;
      if (!h || h < 100) h = document.documentElement.scrollHeight;
      if (window.frameElement && h > 0) window.frameElement.style.height = h + 'px';
    }catch(e){}
  }
  window.addEventListener('load', function(){ setTimeout(fit, 100); });
  window.addEventListener('resize', fit);
  var t = setInterval(fit, 500);
  setTimeout(function(){ clearInterval(t); }, 5000);
})();
</script>""")
        html_content = html_content.replace("</head>", "".join(inject_parts) + "</head>", 1)

        order_keys = ["1", "2", "3", "4", "5", "8", "9", "full"]
        label_by_key = {v: k for k, v in part_options}
        idx = order_keys.index(only_part)

        def render_nav_buttons(suffix):
            if only_part == "full":
                return
            _, mid_col, _ = st.columns([1, 2, 1])
            with mid_col:
                next_key = order_keys[idx + 1]
                if next_key != "full":
                    next_label = label_by_key[next_key]
                    if st.button("➡️ Sang phần tiếp theo", type="primary", key=f"hsk1_next_{only_part}{suffix}", use_container_width=True):
                        st.session_state.hsk1_exam2_pending = next_label
                        st.rerun()
                elif st.button("✅ Nộp bài & Chấm điểm", type="primary", key=f"hsk1_submit_{only_part}{suffix}", use_container_width=True):
                    st.session_state.hsk1_exam2_submit = True
                    st.rerun()

        render_nav_buttons("_top")
        st.markdown("<br/>", unsafe_allow_html=True)
        components.html(html_content, height=900, scrolling=True)
        if only_part == "full":
            st.info("Kiểm tra lại toàn bộ đề, sau đó kéo xuống **cuối khung đề thi** và bấm **✅ Nộp bài & Chấm điểm**.")
    else:
        st.error(f"Không tìm thấy file đề thi: {html_path}")

    if st.session_state.get("hsk1_exam2_open_submit"):
        _exam2_submit_dialog()


def show_hsk1_consolidated_quiz(save_progress, save_score_row_hsk1_consolidated, load_all_scores_hsk1_consolidated, quiz_pick="Đề 1"):
    # CSS Styles cao cấp
    st.markdown("""
    <style>
    /* Card Container */
    .quiz-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 24px;
        padding: 35px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
        margin-bottom: 25px;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Question Number */
    .quiz-q-num {
        font-size: 1.4rem;
        font-weight: 800;
        color: #2563eb;
        margin-bottom: 12px;
        font-family: 'Inter', sans-serif;
    }
    
    /* Question Text */
    .quiz-q-text {
        font-size: 1.25rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 8px;
        line-height: 1.45;
        font-family: 'Inter', sans-serif;
    }
    
    /* Pinyin Text */
    .quiz-q-pinyin {
        font-family: 'Courier New', monospace;
        font-size: 1.15rem;
        font-weight: bold;
        color: #2563eb;
        margin-bottom: 25px;
        background-color: #eff6ff;
        padding: 8px 16px;
        border-radius: 12px;
        display: inline-block;
        border: 1px solid #dbeafe;
    }
    
    /* Option Buttons Container */
    .quiz-option-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-bottom: 20px;
    }
    
    /* Styled Streamlit buttons inside container */
    .quiz-option-container div.stButton > button {
        background-color: #f8fafc !important;
        color: #1f2937 !important;
        border-radius: 20px !important;
        border: 1.5px solid #e2e8f0 !important;
        padding: 18px 24px !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        text-align: left !important;
        align-items: center !important;
        justify-content: flex-start !important;
        width: 100% !important;
        display: flex !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02) !important;
        transition: all 0.2s ease !important;
    }
    
    .quiz-option-container div.stButton > button:hover {
        background-color: #f1f5f9 !important;
        border-color: #cbd5e1 !important;
        color: #0f172a !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 10px rgba(0,0,0,0.06) !important;
    }
    
    /* Static Option Cards (for showing result) */
    .quiz-option-static {
        background-color: #f8fafc;
        color: #1f2937;
        border-radius: 20px;
        padding: 18px 24px;
        font-size: 1.1rem;
        font-weight: 600;
        text-align: left;
        display: flex;
        align-items: center;
        border: 2px solid transparent;
        margin-bottom: 12px;
    }
    
    .quiz-option-static.correct {
        background-color: #f0fdf4;
        color: #14532d;
        border-color: #22c55e;
    }
    
    .quiz-option-static.incorrect {
        background-color: #fef2f2;
        color: #7f1d1d;
        border-color: #ef4444;
    }
    
    .quiz-option-static.normal {
        background-color: #f9fafb;
        color: #9ca3af;
        border-color: #e5e7eb;
        opacity: 0.65;
    }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro("📝 bài tập trắc nghiệm")

    # ================= PHÂN NHÁNH THEO ĐỀ (sidebar radio) =================
    if quiz_pick == "Bảng điểm":
        _show_scoreboard_quiz(load_all_scores_hsk1_consolidated)
        return

    if quiz_pick == "Đề 2":
        _show_exam2_section()
        return

    # Đề 1: quiz 50 câu (mặc định)
    # ================= ĐỀ 1: QUIZ 50 CÂU ÔN TẬP =================

    # Đề thi mặc định cho toàn bộ phần này là quiz_exam_50
    active_key = "quiz_exam_50"

    # --- KHỞI TẠO STATE ---
    if "hsk1_active_quiz_id" not in st.session_state:
        st.session_state.hsk1_active_quiz_id = active_key
    else:
        st.session_state.hsk1_active_quiz_id = active_key

    if "hsk1_quiz_started" not in st.session_state:
        st.session_state.hsk1_quiz_started = False
    if "hsk1_quiz_idx" not in st.session_state:
        st.session_state.hsk1_quiz_idx = 0
    if "hsk1_quiz_answers" not in st.session_state:
        st.session_state.hsk1_quiz_answers = []
    if "hsk1_quiz_score" not in st.session_state:
        st.session_state.hsk1_quiz_score = 0
    if "hsk1_quiz_submitted" not in st.session_state:
        st.session_state.hsk1_quiz_submitted = False
    if "hsk1_quiz_shuffled_options" not in st.session_state:
        st.session_state.hsk1_quiz_shuffled_options = {}

    quiz_info = QUIZZES_DATA.get(active_key)
    if not quiz_info:
        st.error("Không tìm thấy dữ liệu đề ôn tập bài cũ!")
        return

    questions = quiz_info["questions"]

    # Hàm khởi tạo / làm lại bài thi
    def start_new_quiz():
        st.session_state.hsk1_active_quiz_id = active_key
        st.session_state.hsk1_quiz_started = True
        st.session_state.hsk1_quiz_idx = 0
        st.session_state.hsk1_quiz_answers = [None] * len(questions)
        st.session_state.hsk1_quiz_score = 0
        st.session_state.hsk1_quiz_submitted = False
        
        # Xáo trộn đáp án
        shuffled = []
        for i, q in enumerate(questions):
            opts = q["choices"][:]
            random.Random(active_key + str(i)).shuffle(opts)
            shuffled.append(opts)
        st.session_state.hsk1_quiz_shuffled_options[active_key] = shuffled

    # ================= 1. GIAO DIỆN CHƯA BẮT ĐẦU =================
    if not st.session_state.hsk1_quiz_started:
        if st.button("🚀 BẮT ĐẦU LÀM BÀI ÔN TẬP (50 CÂU)", key="btn_start_quiz_50", type="primary", use_container_width=True):
            start_new_quiz()
            save_progress()
            st.rerun()

        # Bảng xếp hạng điểm học viên
        st.markdown("---")
        st.markdown("### 🏆 Bảng xếp hạng nộp bài")
        scores_data = []
        if supabase_client.is_supabase_configured():
            scores_data = supabase_client.load_scores_from_supabase()
        if not scores_data:
            raw_csv = load_all_scores_hsk1_consolidated()
            for r in raw_csv:
                scores_data.append({
                    "Thời gian": r.get("thời gian", ""),
                    "Học viên": r.get("học viên", ""),
                    "Điểm": r.get("Kết quả") or r.get("tổng điểm", "")
                })

        if scores_data:
            st.dataframe(scores_data, use_container_width=True)
        else:
            st.info("Chưa có lượt nộp điểm nào. Hãy bấm bắt đầu để làm bài ôn tập và lưu điểm!")

    # ================= 2. GIAO DIỆN LÀM BÀI =================
    else:
        current_idx = st.session_state.hsk1_quiz_idx

        # Nút sidebar: Làm lại bài từ đầu
        if st.sidebar.button("🔄 Làm lại từ đầu", use_container_width=True):
            start_new_quiz()
            save_progress()
            st.rerun()

        # Khôi phục shuffled options nếu cần
        if active_key not in st.session_state.hsk1_quiz_shuffled_options:
            shuffled = []
            for i, q in enumerate(questions):
                opts = q["choices"][:]
                random.Random(active_key + str(i)).shuffle(opts)
                shuffled.append(opts)
            st.session_state.hsk1_quiz_shuffled_options[active_key] = shuffled

        # Khôi phục answers list nếu bị lệch độ dài
        if not st.session_state.hsk1_quiz_answers or len(st.session_state.hsk1_quiz_answers) != len(questions):
            st.session_state.hsk1_quiz_answers = [None] * len(questions)

        # Nếu đã hoàn thành tất cả câu hỏi
        if current_idx >= len(questions):
            show_quiz_results(questions, save_progress, save_score_row_hsk1_consolidated, load_all_scores_hsk1_consolidated)
            return

        q_data = questions[current_idx]
        shuffled_choices = st.session_state.hsk1_quiz_shuffled_options[active_key][current_idx]
        correct_choice = q_data["answer"]
        user_choice = st.session_state.hsk1_quiz_answers[current_idx]
        is_answered = (user_choice is not None)

        # Thanh tiến độ và số câu hỏi
        percent_done = int((current_idx / len(questions)) * 100)
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; font-weight: bold; color: #475569; margin-bottom: 8px; font-size: 0.95rem;">
            <span>📝 Ôn tập bài cũ (50 câu)</span>
            <span>Câu {current_idx + 1} / {len(questions)} ({percent_done}%)</span>
        </div>
        """, unsafe_allow_html=True)
        st.progress(current_idx / len(questions))

        # Khung thẻ câu hỏi
        st.markdown(f"""
        <div class="quiz-card">
            <div class="quiz-q-num">Câu hỏi {current_idx + 1} / {len(questions)}</div>
            <div class="quiz-q-text">{q_data['question']}</div>
        </div>
        """, unsafe_allow_html=True)

        # Phát âm câu hỏi mẫu
        col_audio, col_empty = st.columns([4, 6])
        with col_audio:
            render_play_button(q_data["sound_txt"], "🔊 Phát âm câu hỏi mẫu", key=f"audio_q_{active_key}_{current_idx}")
        st.markdown("<br/>", unsafe_allow_html=True)

        # Trạng thái: Chưa trả lời
        if not is_answered:
            st.markdown('<div class="quiz-option-container">', unsafe_allow_html=True)
            for i, choice in enumerate(shuffled_choices):
                if st.button(choice, key=f"btn_choice_{active_key}_{i}_{current_idx}", use_container_width=True):
                    st.session_state.hsk1_quiz_answers[current_idx] = choice
                    if choice == correct_choice:
                        st.session_state.hsk1_quiz_score += 1
                    save_progress()
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        # Trạng thái: Đã trả lời
        else:
            static_options_html = '<div class="quiz-option-container">'
            for choice in shuffled_choices:
                if choice == correct_choice:
                    static_options_html += f'<div class="quiz-option-static correct">✅ {choice}</div>'
                elif choice == user_choice:
                    static_options_html += f'<div class="quiz-option-static incorrect">❌ {choice}</div>'
                else:
                    static_options_html += f'<div class="quiz-option-static normal">{choice}</div>'
            static_options_html += '</div>'
            st.markdown(static_options_html, unsafe_allow_html=True)

            # Giải thích kết quả
            if user_choice == correct_choice:
                st.success(f"🎉 **Chính xác!**\n\n**Giải thích:** {q_data['explain']}")
            else:
                st.error(f"😢 **Chưa chính xác!** (Bạn đã chọn: {user_choice})\n\n👉 Đáp án đúng là: **{correct_choice}**\n\n**Giải thích:** {q_data['explain']}")

            # Điều hướng câu hỏi
            st.markdown("<br/>", unsafe_allow_html=True)
            col_nav_1, col_nav_2 = st.columns([1, 1])
            with col_nav_1:
                if current_idx > 0:
                    if st.button("⬅️ Câu trước đó", use_container_width=True):
                        st.session_state.hsk1_quiz_idx -= 1
                        st.rerun()
            with col_nav_2:
                btn_label = "Xem kết quả tổng kết 📊" if current_idx == len(questions) - 1 else "Câu tiếp theo ➡️"
                if st.button(btn_label, type="primary", use_container_width=True):
                    st.session_state.hsk1_quiz_idx += 1
                    st.rerun()


def show_quiz_results(questions, save_progress, save_score_row_hsk1_consolidated, load_all_scores_hsk1_consolidated):
    score = st.session_state.hsk1_quiz_score
    total = len(questions)
    score_display = f"{score}/{total}"

    # Bật popup cho học viên điền tên nếu chưa nộp
    if not st.session_state.hsk1_quiz_submitted:
        popup_submit_score(score_display, questions, save_progress, save_score_row_hsk1_consolidated)

    st.balloons()

    # Màn hình kết quả tinh gọn, không hiện quá nhiều thông tin
    saved_name = st.session_state.get("submitted_student_name", "")
    if st.session_state.hsk1_quiz_submitted and saved_name:
        st.markdown(f"""
        <div style="background-color: #fff; border: 2px solid #22c55e; border-radius: 18px; padding: 25px; text-align: center; max-width: 550px; margin: 20px auto; box-shadow: 0 4px 15px rgba(0,0,0,0.03);">
            <div style="font-size: 2.2rem; margin-bottom: 5px;">🏆</div>
            <h3 style="color: #1e3a8a; margin: 5px 0; font-weight: 800;">Đã lưu điểm thành công!</h3>
            <p style="color: #475569; font-size: 1.1rem; margin-bottom: 5px;">Học viên: <b>{saved_name}</b></p>
            <p style="color: #15803d; font-size: 1.8rem; font-weight: 900; margin: 5px 0;">Điểm số: {score_display}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="background-color: #fff; border: 2px solid #3b82f6; border-radius: 18px; padding: 25px; text-align: center; max-width: 550px; margin: 20px auto; box-shadow: 0 4px 15px rgba(0,0,0,0.03);">
            <div style="font-size: 2.2rem; margin-bottom: 5px;">📝</div>
            <h3 style="color: #1e3a8a; margin: 5px 0; font-weight: 800;">Kết quả: {score_display}</h3>
            <p style="color: #64748b; font-size: 0.95rem; margin-bottom: 15px;">Vui lòng điền tên trong popup để lưu điểm</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("✍️ Mở popup điền tên", use_container_width=True, type="primary"):
            popup_submit_score(score_display, questions, save_progress, save_score_row_hsk1_consolidated)

    # Nút làm lại bài
    if st.button("🔄 Làm lại bài ôn tập", use_container_width=True, type="secondary"):
        st.session_state.hsk1_quiz_idx = 0
        st.session_state.hsk1_quiz_answers = [None] * len(questions)
        st.session_state.hsk1_quiz_score = 0
        st.session_state.hsk1_quiz_submitted = False
        save_progress()
        st.rerun()

    # Bảng xếp hạng nộp bài
    st.markdown("---")
    st.markdown("### 🏆 Bảng xếp hạng nộp bài")
    scores_data = []
    if supabase_client.is_supabase_configured():
        scores_data = supabase_client.load_scores_from_supabase()
    if not scores_data:
        raw_csv = load_all_scores_hsk1_consolidated()
        for r in raw_csv:
            scores_data.append({
                "Thời gian": r.get("thời gian", ""),
                "Học viên": r.get("học viên", ""),
                "Điểm": r.get("Kết quả") or r.get("tổng điểm", "")
            })

    if scores_data:
        st.dataframe(scores_data, use_container_width=True)
    else:
        st.info("Chưa có lượt nộp điểm nào.")
