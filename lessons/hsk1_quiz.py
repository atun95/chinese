# -*- coding: utf-8 -*-
import streamlit as st
import streamlit.components.v1 as components
import random
import csv
import json
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


def render_exam2_review(sel):
    """Render bài làm của học viên (từ Supabase) dạng chấm điểm, không phải JSON."""
    data = _load_exam2_data()
    answers = sel.get("answers") or {}
    order_ans = sel.get("order_answers") or {}
    out = []

    def qcard(inner):
        return f"""
        <div style="background:#fff;border:1px solid #e2e8f0;border-radius:14px;padding:14px 18px;margin-bottom:10px;">
            {inner}
        </div>"""

    def mcq_html(q, stem_html, note=""):
        user = answers.get(q["id"])
        opts = ""
        for oi, opt in enumerate(q.get("options", [])):
            if oi == q.get("ans"):
                mark, bg, bd, color = "✅", "#f0fdf4", "#22c55e", "#14532d"
            elif user == oi:
                mark, bg, bd, color = "❌", "#fef2f2", "#ef4444", "#7f1d1d"
            else:
                mark, bg, bd, color = "", "#f8fafc", "#e2e8f0", "#374151"
            opts += f'<div style="display:flex;gap:8px;align-items:center;background:{bg};border:1.5px solid {bd};border-radius:10px;padding:8px 12px;margin:5px 0;color:{color};font-weight:600;font-size:0.95rem;"><span style="min-width:20px;">{mark}</span><span>{opt}</span></div>'
        exp = q.get("exp", "")
        return qcard(f"""
            <div style="font-weight:800;color:#0f172a;margin-bottom:6px;">{stem_html}</div>
            {opts}
            <div style="margin-top:8px;font-size:0.85rem;color:#475569;background:#f8fafc;border-left:3px solid #94a3b8;padding:6px 10px;border-radius:6px;">{exp}</div>
            {note}
        """)

    def tf_html(q, idx):
        user = answers.get(q["id"])
        correct = "Đúng (Đ)" if q.get("ans") == "D" else "Sai (S)"
        user_txt = "Đúng (Đ)" if user == "D" else ("Sai (S)" if user == "S" else "(bỏ trống)")
        ok = user == q.get("ans")
        return qcard(f"""
            <div style="font-weight:800;color:#0f172a;">{idx}. <span class="zh" style="font-size:1.1rem;">{q.get('zh','')}</span>
            <span style="color:#64748b;font-weight:600;"> ({q.get('py','')})</span></div>
            <div style="color:#475569;font-size:0.9rem;margin:4px 0 8px 0;">{q.get('vi','')}</div>
            <div style="font-size:0.9rem;">Học viên chọn: <b style="color:{'#15803d' if ok else '#b91c1c'};">{user_txt}</b>
            &nbsp;|&nbsp; Đáp án: <b>{correct}</b></div>
            <div style="margin-top:6px;font-size:0.85rem;color:#475569;background:#f8fafc;border-left:3px solid #94a3b8;padding:6px 10px;border-radius:6px;">{q.get('exp','')}</div>
        """)

    # ---------- PHẦN I: Từ vựng ----------
    qs = data.get("part1Data", [])
    if qs:
        out.append("<h4 style='color:#1d4ed8;margin:18px 0 8px 0;'>Phần I. Chọn nghĩa đúng của từ vựng</h4>")
        for i, q in enumerate(qs, 1):
            stem = f"<span style='color:#2563eb;font-weight:800;'>{i}.</span> <span style='font-size:1.2rem;font-weight:800;'>{q.get('zh','')}</span> <span style='color:#64748b;'>({q.get('py','')})</span>"
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
            user_words = order_ans.get(q["id"]) or []
            user_sent = "".join(user_words).replace(" ", "")
            target = (q.get("correct") or "").replace(" ", "")
            ok = user_sent == target and bool(user_sent)
            user_disp = " ".join(user_words) if user_words else "(bỏ trống)"
            out.append(qcard(f"""
                <div style="font-weight:800;color:#0f172a;margin-bottom:6px;">{i}. Sắp xếp các từ: <span style="color:#64748b;font-weight:600;">{' '.join(q.get('tokens',[]))}</span></div>
                <div style="font-size:0.95rem;">Học viên xếp: <b style="color:{'#15803d' if ok else '#b91c1c'};">{user_disp}</b></div>
                <div style="font-size:0.95rem;margin-top:4px;">Câu đúng: <b style="color:#15803d;">{q.get('correct','')}</b></div>
                <div style="margin-top:6px;font-size:0.85rem;color:#475569;background:#f8fafc;border-left:3px solid #94a3b8;padding:6px 10px;border-radius:6px;">{q.get('exp','')}</div>
            """))

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
            out.append(f"""
            <div style="background:#fff9db;border:1px solid #ffe066;border-left:5px solid #f59f00;border-radius:10px;padding:14px 18px;margin-bottom:10px;">
                <div style="font-weight:800;color:#d9480f;margin-bottom:6px;">📖 Đoạn văn</div>
                <div style="font-size:1.05rem;line-height:1.9;">{passage}</div>
            </div>""")
        for i, q in enumerate(qs, 1):
            stem = f"<span style='color:#2563eb;font-weight:800;'>{i}.</span> <span style='font-size:1.1rem;font-weight:800;'>{q.get('q_zh','')}</span> <span style='color:#64748b;'>({q.get('q_py','')})</span>"
            out.append(mcq_html(q, stem))

    # ---------- PHẦN VIII: Ngữ pháp ----------
    qs = data.get("part8Data", [])
    if qs:
        out.append("<h4 style='color:#1d4ed8;margin:18px 0 8px 0;'>Phần VI. Ngữ pháp điền từ</h4>")
        for i, q in enumerate(qs, 1):
            stem = f"<span style='color:#2563eb;font-weight:800;'>{i}.</span> <span style='font-size:1.15rem;font-weight:800;letter-spacing:1px;'>{q.get('q','')}</span>"
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


def show_hsk1_consolidated_quiz(save_progress, save_score_row_hsk1_consolidated, load_all_scores_hsk1_consolidated):
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

    render_lesson_intro("📝 Trắc nghiệm Tổng hợp HSK 1 - Ôn tập bài cũ")

    # ================= TRANG DANH SÁCH ĐỀ (2 BÀI KIỂM TRA HSK 1) =================
    exam_view = st.session_state.get("hsk1_exam_view", "menu")

    if exam_view == "menu":
        exams = [
            (
                "exam1",
                "📝",
                "Đề 1: Ôn tập bài cũ (50 câu trắc nghiệm)",
                "50 câu trắc nghiệm ôn tập toàn diện: ngữ âm, chữ Hán, từ vựng, ngữ pháp, lượng từ, tìm lỗi sai, sắp xếp câu và đối thoại.",
                "#3b82f6"
            ),
            (
                "exam2",
                "🎓",
                "Đề 2: Bài test HSK 1 (55 câu + tự luận)",
                "Bài kiểm tra tổng hợp 6 phần: từ vựng, đúng/sai, sắp xếp câu, đọc hiểu, ngữ pháp và viết đoạn văn. Có nghe phát âm tiếng Trung và đồng hồ 45 phút.",
                "#c92a2a"
            ),
        ]
        for key, icon, title, desc, color in exams:
            st.markdown(f"""
            <div style="background: white; border: 2px solid #e2e8f0; border-left: 6px solid {color}; border-radius: 18px; padding: 24px 28px; margin-bottom: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.04);">
                <div style="font-size: 2rem; margin-bottom: 6px;">{icon}</div>
                <div style="font-size: 1.3rem; font-weight: 800; color: #0f172a; margin-bottom: 6px;">{title}</div>
                <div style="color: #475569; font-size: 0.95rem; line-height: 1.6;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"🚀 Bắt đầu làm bài", key=f"hsk1_open_{key}", type="primary", use_container_width=True):
                st.session_state.hsk1_exam_view = key
                st.session_state.hsk1_exam_choice = key
                st.rerun()
            st.markdown("<br/>", unsafe_allow_html=True)

        # ================= XEM LẠI BÀI ĐÃ NỘP (SUPABASE) =================
        with st.expander("📋 Xem bài làm học viên đã nộp (Đề 2 - Bài test HSK 1)"):
            try:
                sb_client = supabase_client.get_supabase_client()
                if sb_client:
                    res = sb_client.table("hsk1_exam2_answers").select(
                        "id,student_name,score,max_score,part_scores,answers,order_answers,essay,submitted_at"
                    ).order("submitted_at", desc=True).limit(50).execute()
                    rows = res.data or []
                    if not rows:
                        st.info("Chưa có bài nộp nào trong database.")
                    else:
                        overview = [{
                            "Học viên": r.get("student_name", "Ẩn danh"),
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
                        pick = st.selectbox("Chọn bài để xem chi tiết:", labels, key="hsk1_exam2_pick_menu")
                        sel = rows[labels.index(pick)]
                        st.markdown("**Bài tự luận (Phần VII):**")
                        st.text_area("Essay", value=sel.get("essay") or "(không có)", height=180, disabled=True, key="hsk1_essay_view_menu")
                        st.markdown("#### 📝 Chi tiết đáp án & chấm từng câu")
                        frag = render_exam2_review(sel)
                        review_page = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
body {{ font-family: -apple-system, 'Segoe UI', Roboto, sans-serif; background: #f8fafc; padding: 18px; margin: 0; color: #1f2937; }}
.zh {{ font-family: 'PingFang SC','Microsoft YaHei','Noto Sans SC',sans-serif; }}
h4 {{ margin: 22px 0 10px 0; }}
</style></head><body>{frag}
<script>
(function(){{
  function fit(){{
    try{{
      var h = document.body ? document.body.scrollHeight : 0;
      if (window.frameElement && h > 0) window.frameElement.style.height = h + 'px';
    }}catch(e){{}}
  }}
  window.addEventListener('load', function(){{ setTimeout(fit, 100); }});
  var t = setInterval(fit, 500);
  setTimeout(function(){{ clearInterval(t); }}, 5000);
}})();
</script>
</body></html>"""
                        components.html(review_page, height=1200, scrolling=True)
                else:
                    st.warning("Chưa kết nối được Supabase.")
            except Exception as e:
                st.error(f"Lỗi tải bài nộp: {e}")
        return

    # ================= NÚT QUAY LẠI DANH SÁCH ĐỀ =================
    if st.button("⬅️ Quay lại danh sách đề", key="hsk1_back_to_menu", use_container_width=False):
        st.session_state.hsk1_exam_view = "menu"
        st.rerun()
    st.markdown("---")

    # ================= ĐỀ 2: BÀI TEST HSK 1 (HTML) =================
    if exam_view == "exam2":
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
        # Áp dụng điều hướng từ nút Trước/Sau (phải set TRƯỚC khi selectbox render)
        pending_part = st.session_state.pop("hsk1_exam2_pending", None)
        if pending_part in part_labels:
            st.session_state.hsk1_exam2_part = pending_part
        part_choice = st.selectbox(
            "Chọn phần của bài test:",
            part_labels,
            key="hsk1_exam2_part",
            help="Đáp án đã chọn được tự động lưu — bạn có thể chuyển qua lại giữa các phần mà không mất bài."
        )
        only_part = dict(part_options)[part_choice]

        html_path = Path(__file__).resolve().parent.parent / "bai_test_hsk1.html"
        if html_path.exists():
            html_content = html_path.read_text(encoding="utf-8")
            inject_parts = ["<style>body{padding-bottom:0 !important;}</style>"]
            # Inject cấu hình Supabase để đề thi tự lưu đáp án
            try:
                sb_cfg = supabase_client.get_supabase_config()
                inject_parts.append(
                    f"<script>window.__SUPABASE_URL__='{sb_cfg['url']}';"
                    f"window.__SUPABASE_KEY__='{sb_cfg['key']}';"
                    f"window.__EXAM2_TABLE__='hsk1_exam2_answers';</script>"
                )
            except Exception:
                pass
            if only_part != "full":
                inject_parts.append(f"<script>window.__EXAM_ONLY_PART__='{only_part}';</script>")
            else:
                # Bản full không cuộn trong khung -> đưa thanh nộp bài về cuối tài liệu
                inject_parts.append("<style>.bottom-bar{position:static !important;}</style>")
            # Script tự chỉnh chiều cao iframe sát nội dung (hết khoảng trắng thừa)
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

            # ================= NÚT ĐIỀU HƯỚNG (đặt trên đầu đề) =================
            order_keys = ["1", "2", "3", "4", "5", "8", "9", "full"]
            label_by_key = {v: k for k, v in part_options}
            idx = order_keys.index(only_part)

            def render_nav_buttons(suffix):
                if only_part == "full":
                    return
                prev_col, next_col = st.columns([1, 2])
                with prev_col:
                    if idx > 0:
                        prev_label = label_by_key[order_keys[idx - 1]]
                        if st.button("⬅️ Phần trước", key=f"hsk1_prev_{only_part}{suffix}", use_container_width=True):
                            st.session_state.hsk1_exam2_pending = prev_label
                            st.rerun()
                with next_col:
                    next_key = order_keys[idx + 1]
                    if next_key != "full":
                        next_label = label_by_key[next_key]
                        if st.button("➡️ Sang phần tiếp theo", type="primary", key=f"hsk1_next_{only_part}{suffix}", use_container_width=True):
                            st.session_state.hsk1_exam2_pending = next_label
                            st.rerun()

            render_nav_buttons("_top")
            st.markdown("<br/>", unsafe_allow_html=True)

            components.html(html_content, height=900, scrolling=True)

            if only_part == "full":
                st.info("Kiểm tra lại toàn bộ đề, sau đó kéo xuống **cuối khung đề thi** và bấm **✅ Nộp bài & Chấm điểm**.")
        else:
            st.error(f"Không tìm thấy file đề thi: {html_path}")
        return

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
