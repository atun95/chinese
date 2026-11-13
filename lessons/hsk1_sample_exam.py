"""Đề thi thử HSK 1. Đề 1 là mẫu H10000. Đề sau thêm vào danh sách EXAMS."""
from pathlib import Path

import streamlit as st

import supabase_client

_ASSET = Path(__file__).resolve().parent.parent / "assets" / "h10000"
_AUDIO = _ASSET / "H10000.mp3"

ANSWERS = {
    1: "×", 2: "√", 3: "√", 4: "×", 5: "×",
    6: "A", 7: "C", 8: "B", 9: "C", 10: "B",
    11: "D", 12: "E", 13: "B", 14: "A", 15: "F",
    16: "B", 17: "C", 18: "A", 19: "A", 20: "C",
    21: "×", 22: "√", 23: "√", 24: "√", 25: "×",
    26: "F", 27: "C", 28: "D", 29: "B", 30: "A",
    31: "E", 32: "B", 33: "C", 34: "D", 35: "A",
    36: "F", 37: "B", 38: "A", 39: "C", 40: "E",
}

_PARTS = [
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


def _page(name):
    return str(_ASSET / "pages" / name)


def _score(picked, numbers):
    return sum(1 for n in numbers if picked.get(n) == ANSWERS[n])


def _k(name):
    return f"d1_{name}"


def _choice_list(numbers, options):
    st.markdown("**Đáp án**")
    for n in numbers:
        st.radio(
            f"Câu {n}",
            options,
            index=None,
            key=_k(f"q{n}"),
            horizontal=True,
        )


def _render_parts(section, form_key, submit_label):
    with st.form(form_key):
        for kind, title, caption, image, numbers, options in _PARTS:
            if kind != section:
                continue
            st.subheader(title)
            st.caption(caption)
            st.image(_page(image), width="stretch")
            _choice_list(numbers, options)
            st.divider()
        return st.form_submit_button(submit_label, type="primary", width="stretch")


def _result_table(numbers):
    rows = []
    for n in numbers:
        got = st.session_state.get(_k(f"ans_{n}"))
        ok = got == ANSWERS[n]
        rows.append({
            "Câu": n,
            "Bạn chọn": got or "—",
            "Đáp án": ANSWERS[n],
            "Điểm": 1 if ok else 0,
        })
    st.dataframe(rows, width="stretch", hide_index=True)


def _score_card(name, listening, reading, total):
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Đề", "Đề 1")
    c2.metric("Nghe", f"{listening}/20")
    c3.metric("Đọc", f"{reading}/20")
    c4.metric("Tổng điểm", f"{total}/40")
    st.write(f"Tên học viên: **{name}**")


def _save_once(name, listening, reading, total):
    if st.session_state.get(_k("saved")):
        return
    ok, msg = supabase_client.save_hsk_exam_score("Đề 1", name, listening, reading, total)
    st.session_state[_k("saved")] = ok
    st.session_state[_k("save_msg")] = msg


def _show_scoreboard():
    st.subheader("Bảng điểm")
    rows, err = supabase_client.load_hsk_exam_scores()
    if err:
        st.error(err)
        return
    if not rows:
        st.info("Chưa có điểm nào được lưu.")
        return
    st.dataframe(rows, width="stretch", hide_index=True)


def _reset_attempt():
    for key in list(st.session_state.keys()):
        if str(key).startswith("d1_"):
            del st.session_state[key]


def show_exam(exam_label="Đề 1"):
    if exam_label == "Bảng điểm":
        _show_scoreboard()
        return
    if exam_label != "Đề 1":
        st.subheader(exam_label)
        st.info("Đề này chưa có nội dung. Học viên hãy làm Đề 1 trước.")
        return

    st.session_state.setdefault(_k("phase"), "cover")
    phase = st.session_state[_k("phase")]

    if phase == "cover":
        st.subheader("Đề 1")
        st.write(
            "Nghe 20 câu, rồi Đọc 20 câu. File nghe chạy một mạch, mỗi câu đã được đọc hai lần. "
            "Chọn đáp án ngay dưới mỗi trang. Nộp bài xong, điểm Nghe, Đọc và tổng được tính và lưu lại."
        )
        name = st.text_input("Tên học viên", key=_k("name_input"))
        if st.button("Bắt đầu phần Nghe", type="primary"):
            st.session_state[_k("name")] = name.strip() or "Học viên"
            st.session_state[_k("phase")] = "listen"
            st.rerun()
        return

    if phase == "listen":
        st.caption("Đề 1 · Phần Nghe")
        if _AUDIO.exists():
            st.audio(str(_AUDIO), format="audio/mp3")
        else:
            st.error("Không thấy file nghe của Đề 1.")
        if _render_parts("listen", "d1_listen", "Xong phần Nghe, sang phần Đọc"):
            for n in range(1, 21):
                st.session_state[_k(f"ans_{n}")] = st.session_state.get(_k(f"q{n}"))
            st.session_state[_k("phase")] = "read"
            st.rerun()
        return

    if phase == "read":
        listening = _score({n: st.session_state.get(_k(f"ans_{n}")) for n in range(1, 21)}, range(1, 21))
        st.caption(f"Đề 1 · Phần Đọc · Nghe đã khóa {listening}/20")
        if _render_parts("read", "d1_read", "Nộp bài và tính điểm"):
            for n in range(21, 41):
                st.session_state[_k(f"ans_{n}")] = st.session_state.get(_k(f"q{n}"))
            st.session_state[_k("phase")] = "result"
            st.rerun()
        return

    listening = _score({n: st.session_state.get(_k(f"ans_{n}")) for n in range(1, 21)}, range(1, 21))
    reading = _score({n: st.session_state.get(_k(f"ans_{n}")) for n in range(21, 41)}, range(21, 41))
    total = listening + reading
    name = st.session_state.get(_k("name")) or "Học viên"
    _save_once(name, listening, reading, total)

    st.subheader("Đề 1 · Kết quả")
    _score_card(name, listening, reading, total)
    msg = st.session_state.get(_k("save_msg")) or ""
    if st.session_state.get(_k("saved")):
        st.success(msg)
    else:
        st.error(msg or "Chưa lưu được điểm.")
    tab_listen, tab_read = st.tabs(["Đáp án Nghe", "Đáp án Đọc"])
    with tab_listen:
        _result_table(range(1, 21))
    with tab_read:
        _result_table(range(21, 41))
    if st.button("Làm lại Đề 1"):
        _reset_attempt()
        st.rerun()
