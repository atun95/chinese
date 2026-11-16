"""Đề thi thử HSK 1. Hỗ trợ Đề 1 (mẫu H10000) và Đề 2 (mẫu H11334)."""
from pathlib import Path

import streamlit as st

import supabase_client
from ui_utils import render_lesson_intro

_ASSET_BASE = Path(__file__).resolve().parent.parent / "assets"

EXAMS = {
    "Đề 1": {
        "code": "H10000",
        "title": "Đề 1 (H10000)",
        "asset_dir": _ASSET_BASE / "h10000",
        "audio": _ASSET_BASE / "h10000" / "H10000.mp3",
        "prefix": "d1",
        "answers": {
            1: "×", 2: "√", 3: "√", 4: "×", 5: "×",
            6: "A", 7: "C", 8: "B", 9: "C", 10: "B",
            11: "D", 12: "E", 13: "B", 14: "A", 15: "F",
            16: "B", 17: "C", 18: "A", 19: "A", 20: "C",
            21: "×", 22: "√", 23: "√", 24: "√", 25: "×",
            26: "F", 27: "C", 28: "D", 29: "B", 30: "A",
            31: "E", 32: "B", 33: "C", 34: "D", 35: "A",
            36: "F", 37: "B", 38: "A", 39: "C", 40: "E",
        },
        "parts": [
            ("listen", "Nghe · Phần 1", "Câu 1–5. Nghe và nhìn tranh, chọn đúng hoặc sai.", "page_03.png", range(1, 6), ["√", "×"]),
            ("listen", "Nghe · Phần 2", "Câu 6–10. Nghe và chọn tranh A, B hoặc C.", "page_04.png", range(6, 9), ["A", "B", "C"]),
            ("listen", "Nghe · Phần 2 (tiếp)", "Câu 9–10.", "page_05.png", range(9, 11), ["A", "B", "C"]),
            ("listen", "Nghe · Phần 3", "Câu 11–15. Nghe hội thoại, chọn tranh A–F. Một tranh không dùng.", "page_06.png", range(11, 16), list("ABCDEF")),
            ("listen", "Nghe · Phần 4", "Câu 16–20. Nghe đoạn và câu hỏi, chọn A, B hoặc C.", "page_07.png", range(16, 21), ["A", "B", "C"]),
            ("read", "Đọc · Phần 1", "Câu 21–25. Nhìn tranh và chữ, chọn đúng hoặc sai.", "page_08.png", range(21, 26), ["√", "×"]),
            ("read", "Đọc · Phần 2", "Câu 26–30. Đọc câu, chọn tranh A–F.", "page_09.png", range(26, 31), list("ABCDEF")),
            ("read", "Đọc · Phần 3", "Câu 31–35. Ghép câu hỏi với câu trả lời A–F.", "page_10.png", range(31, 36), list("ABCDEF")),
            ("read", "Đọc · Phần 4", "Câu 36–40. Chọn từ A–F điền vào chỗ trống.", "page_11.png", range(36, 41), list("ABCDEF")),
        ]
    },
    "Đề 2": {
        "code": "H11334",
        "title": "Đề 2 (H11334)",
        "asset_dir": _ASSET_BASE / "h11334",
        "audio": _ASSET_BASE / "h11334" / "H11334.mp3",
        "prefix": "d2",
        "answers": {
            1: "√", 2: "√", 3: "×", 4: "×", 5: "×",
            6: "B", 7: "C", 8: "A", 9: "C", 10: "C",
            11: "D", 12: "F", 13: "B", 14: "E", 15: "A",
            16: "A", 17: "A", 18: "C", 19: "B", 20: "B",
            21: "×", 22: "√", 23: "√", 24: "√", 25: "×",
            26: "C", 27: "D", 28: "A", 29: "F", 30: "B",
            31: "D", 32: "E", 33: "C", 34: "B", 35: "A",
            36: "E", 37: "B", 38: "F", 39: "C", 40: "A",
        },
        "parts": [
            ("listen", "Nghe · Phần 1", "Câu 1–5. Nghe và nhìn tranh, chọn đúng hoặc sai.", "page_02.png", range(1, 6), ["√", "×"]),
            ("listen", "Nghe · Phần 2", "Câu 6–10. Nghe và chọn tranh A, B hoặc C.", "page_03.png", range(6, 9), ["A", "B", "C"]),
            ("listen", "Nghe · Phần 2 (tiếp)", "Câu 9–10.", "page_04.png", range(9, 11), ["A", "B", "C"]),
            ("listen", "Nghe · Phần 3", "Câu 11–15. Nghe hội thoại, chọn tranh A–F. Một tranh không dùng.", "page_05.png", range(11, 16), list("ABCDEF")),
            ("listen", "Nghe · Phần 4", "Câu 16–20. Nghe đoạn và câu hỏi, chọn A, B hoặc C.", "page_06.png", range(16, 21), ["A", "B", "C"]),
            ("read", "Đọc · Phần 1", "Câu 21–25. Nhìn tranh và chữ, chọn đúng hoặc sai.", "page_07.png", range(21, 26), ["√", "×"]),
            ("read", "Đọc · Phần 2", "Câu 26–30. Đọc câu, chọn tranh A–F.", "page_08.png", range(26, 31), list("ABCDEF")),
            ("read", "Đọc · Phần 3", "Câu 31–35. Ghép câu hỏi với câu trả lời A–F.", "page_09.png", range(31, 36), list("ABCDEF")),
            ("read", "Đọc · Phần 4", "Câu 36–40. Chọn từ A–F điền vào chỗ trống.", "page_10.png", range(36, 41), list("ABCDEF")),
        ]
    }
}


def _page(exam_cfg, name):
    return str(exam_cfg["asset_dir"] / "pages" / name)


def _score(exam_cfg, picked, numbers):
    ans = exam_cfg["answers"]
    return sum(1 for n in numbers if picked.get(n) == ans[n])


def _k(exam_cfg, name):
    return f"{exam_cfg['prefix']}_{name}"


def _choice_list(exam_cfg, numbers, options):
    st.markdown("**Đáp án**")
    for n in numbers:
        st.radio(
            f"Câu {n}",
            options,
            index=None,
            key=_k(exam_cfg, f"q{n}"),
            horizontal=True,
        )


def _render_parts(exam_cfg, section, form_key, submit_label):
    with st.form(form_key):
        for kind, title, caption, image, numbers, options in exam_cfg["parts"]:
            if kind != section:
                continue
            st.subheader(title)
            st.caption(caption)
            st.image(_page(exam_cfg, image), width="stretch")
            _choice_list(exam_cfg, numbers, options)
            st.divider()
        return st.form_submit_button(submit_label, type="primary", width="stretch")


def _result_table(exam_cfg, numbers):
    ans = exam_cfg["answers"]
    rows = []
    for n in numbers:
        got = st.session_state.get(_k(exam_cfg, f"ans_{n}"))
        ok = got == ans[n]
        rows.append({
            "Câu": n,
            "Bạn chọn": got or "—",
            "Đáp án": ans[n],
            "Điểm": 1 if ok else 0,
        })
    st.dataframe(rows, width="stretch", hide_index=True)


def _score_card(exam_label, name, listening, reading, total):
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Đề", exam_label)
    c2.metric("Nghe", f"{listening}/20")
    c3.metric("Đọc", f"{reading}/20")
    c4.metric("Tổng điểm", f"{total}/40")
    st.write(f"Tên học viên: **{name}**")


def _save_once(exam_label, exam_cfg, name, listening, reading, total):
    saved_key = _k(exam_cfg, "saved")
    msg_key = _k(exam_cfg, "save_msg")
    if st.session_state.get(saved_key):
        return
    ok, msg = supabase_client.save_hsk_exam_score(exam_label, name, listening, reading, total)
    st.session_state[saved_key] = ok
    st.session_state[msg_key] = msg


def _show_scoreboard():
    st.subheader("🏆 Bảng điểm Đề thi thử HSK 1")
    rows, err = supabase_client.load_hsk_exam_scores()
    if err:
        st.error(err)
        return
    if not rows:
        st.info("Chưa có lượt nộp điểm nào cho Đề thi thử HSK 1.")
        return
    st.dataframe(rows, use_container_width=True, hide_index=True)


def _reset_attempt(exam_cfg):
    prefix = exam_cfg["prefix"] + "_"
    for key in list(st.session_state.keys()):
        if str(key).startswith(prefix):
            del st.session_state[key]


def show_exam(exam_label="Đề 1"):
    # Đảm bảo phần đầu trang có khoảng cách đủ, không bị thanh header của Streamlit che khuất
    st.markdown("""
    <style>
    .block-container, [data-testid="stMainBlockContainer"] {
        padding-top: 3.2rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro("📄 Đề thi thử HSK 1")

    if exam_label == "Bảng điểm":
        _show_scoreboard()
        return

    if exam_label not in EXAMS:
        st.subheader(exam_label)
        st.info(f"{exam_label} hiện chưa có nội dung. Học viên hãy làm Đề 1 hoặc Đề 2 trước.")
        return

    exam_cfg = EXAMS[exam_label]
    phase_key = _k(exam_cfg, "phase")
    st.session_state.setdefault(phase_key, "cover")
    phase = st.session_state[phase_key]

    if phase == "cover":
        st.subheader(f"{exam_label} ({exam_cfg['code']})")
        st.write(
            "Nghe 20 câu, rồi Đọc 20 câu. File nghe chạy một mạch, mỗi câu đã được đọc hai lần. "
            "Chọn đáp án ngay dưới mỗi trang. Nộp bài xong, điểm Nghe, Đọc và tổng được tính và lưu lại."
        )
        name = st.text_input("Tên học viên", key=_k(exam_cfg, "name_input"))
        if st.button("Bắt đầu phần Nghe", type="primary"):
            st.session_state[_k(exam_cfg, "name")] = name.strip() or "Học viên"
            st.session_state[phase_key] = "listen"
            st.rerun()
        return

    if phase == "listen":
        st.caption(f"{exam_label} ({exam_cfg['code']}) · Phần Nghe")
        audio_path = exam_cfg["audio"]
        if audio_path.exists():
            st.audio(str(audio_path), format="audio/mp3")
        else:
            st.error(f"Không thấy file nghe của {exam_label}.")
        if _render_parts(exam_cfg, "listen", f"{exam_cfg['prefix']}_listen", "Xong phần Nghe, sang phần Đọc"):
            for n in range(1, 21):
                st.session_state[_k(exam_cfg, f"ans_{n}")] = st.session_state.get(_k(exam_cfg, f"q{n}"))
            st.session_state[phase_key] = "read"
            st.rerun()
        return

    if phase == "read":
        listening = _score(exam_cfg, {n: st.session_state.get(_k(exam_cfg, f"ans_{n}")) for n in range(1, 21)}, range(1, 21))
        st.caption(f"{exam_label} ({exam_cfg['code']}) · Phần Đọc · Nghe đã khóa {listening}/20")
        if _render_parts(exam_cfg, "read", f"{exam_cfg['prefix']}_read", "Nộp bài và tính điểm"):
            for n in range(21, 41):
                st.session_state[_k(exam_cfg, f"ans_{n}")] = st.session_state.get(_k(exam_cfg, f"q{n}"))
            st.session_state[phase_key] = "result"
            st.rerun()
        return

    listening = _score(exam_cfg, {n: st.session_state.get(_k(exam_cfg, f"ans_{n}")) for n in range(1, 21)}, range(1, 21))
    reading = _score(exam_cfg, {n: st.session_state.get(_k(exam_cfg, f"ans_{n}")) for n in range(21, 41)}, range(21, 41))
    total = listening + reading
    name = st.session_state.get(_k(exam_cfg, "name")) or "Học viên"
    _save_once(exam_label, exam_cfg, name, listening, reading, total)

    st.subheader(f"{exam_label} ({exam_cfg['code']}) · Kết quả")
    _score_card(exam_label, name, listening, reading, total)
    msg = st.session_state.get(_k(exam_cfg, "save_msg")) or ""
    if st.session_state.get(_k(exam_cfg, "saved")):
        st.success(msg)
    else:
        st.error(msg or "Chưa lưu được điểm.")
    tab_listen, tab_read = st.tabs(["Đáp án Nghe", "Đáp án Đọc"])
    with tab_listen:
        _result_table(exam_cfg, range(1, 21))
    with tab_read:
        _result_table(exam_cfg, range(21, 41))
    if st.button(f"Làm lại {exam_label}"):
        _reset_attempt(exam_cfg)
        st.rerun()
