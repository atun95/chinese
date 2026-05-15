import streamlit as st
from datetime import datetime
from lessons_data import *
from ui_utils import *

def show_lesson2_intro(add_tones):
    render_lesson_intro("📚 Bài 2: Vận mẫu kép & Luyện tập ghép âm", "Nắm vững 4 vận mẫu kép cơ bản và luyện tập ghép âm.")
    st.subheader("1. Vận mẫu kép cơ bản")
    cols = st.columns(4)
    for i, item in enumerate(B2_VAN_KEP_SLIDES):
        with cols[i]: render_pronunciation_card({"chu": item["vận"], "hdsd": item["hướng_dẫn"], "vd_han": item["ví_dụ_hán"], "vd_py": item["ví_dụ_py"], "nghe": item["nghe"]}, "b2_vk")
    
    st.markdown("---")
    st.subheader("2. Bảng luyện tập ghép âm")
    h_cols = st.columns([1.5] + [1] * len(B2_LUYEN_TAP_FINALS))
    h_cols[0].markdown("**T/V**")
    for i, f in enumerate(B2_LUYEN_TAP_FINALS): h_cols[i+1].markdown(f"**{f}**")
    for init in B2_LUYEN_TAP_ROWS.keys():
        r_cols = st.columns([1.5] + [1] * len(B2_LUYEN_TAP_FINALS))
        r_cols[0].markdown(f"**{init}**")
        for i, combo in enumerate(B2_LUYEN_TAP_ROWS[init]):
            if combo:
                with r_cols[i+1]:
                    with st.popover(combo, use_container_width=True):
                        for t in add_tones(combo): st.write(f"- {t}")

def show_lesson2_exercises(save_progress, save_score_row_b2, load_all_scores_b2):
    st.header("📝 Bài 2: Bài tập vận mẫu kép")
    
    # 1. Mini quiz từ vựng
    render_quiz_section(B2_QUIZ_VOCAB, "b2_vcb", "Bài tập 1: Mini quiz từ vựng", "Chọn nghĩa đúng nhất cho từng từ.", save_progress)

    # 2. Luyện nghe
    with st.expander("Bài tập 2: Luyện nghe và chọn Pinyin", expanded=False):
        score_b2_ls = 0
        for i, q in enumerate(B2_QUIZ_LISTENING):
            st.write(f"**Câu {i+1}:** Nghe từ '{q['q']}' và chọn pinyin đúng")
            if st.button(f"🔊 Nghe mẫu", key=f"b2_listen_{i}"): play_audio(q["hanzi"])
            key = f"b2_tone_q_{i}"
            choices = shuffled_options(q["choices"], f"b2_ls-{i}")
            if choices[0] == q["answer"] and len(choices) > 1:
                choices[0], choices[1] = choices[1], choices[0]
            res = st.radio("Chọn đáp án:", choices, index=0, key=key)
            if res == q["answer"]: score_b2_ls += 1
        if st.button("Chấm điểm bài 2", key="btn_b2_ls"): 
            st.session_state.scores["b2_ls"] = (score_b2_ls, len(B2_QUIZ_LISTENING))
            save_progress()
            st.success(f"Bạn đúng {score_b2_ls}/{len(B2_QUIZ_LISTENING)} câu.")

    # 3. Điền vận mẫu
    with st.expander("Bài tập 3: Điền vận mẫu & thanh điệu", expanded=False):
        score_b2_fill = 0
        opts = ["...", "ā", "á", "ǎ", "à", "ē", "é", "ě", "è", "ǐ", "ǒ", "ù", "ái", "ǎi", "èi", "ǎo", "ǒu", "áng"]
        for i, q in enumerate(B2_QUIZ_FILL_BLANKS):
            key = f"b2_fill_q_{i}"
            res = st.selectbox(f"Chọn phần còn thiếu cho {q['q']} ({q['meaning']})", opts, index=0, key=key)
            if res == q["ans"]: score_b2_fill += 1
        if st.button("Chấm điểm bài 3", key="btn_b2_fill"):
            st.session_state.scores["b2_fill"] = (score_b2_fill, len(B2_QUIZ_FILL_BLANKS))
            save_progress()
            st.success(f"Bạn đúng {score_b2_fill}/{len(B2_QUIZ_FILL_BLANKS)} câu.")

    with st.expander("📊 Lịch sử & Tổng kết Bài 2", expanded=True):
        labels_b2 = {"b2_vcb": "BT1: Từ vựng", "b2_ls": "BT2: Nghe", "b2_fill": "BT3: Điền âm"}
        missing_b2 = [v for k, v in labels_b2.items() if k not in st.session_state.scores]
        if missing_b2:
            st.warning(f"Chưa xong: {', '.join(missing_b2)}")
        else:
            if st.button("📊 Xem kết quả & Nộp bài", key="btn_b2_summary"):
                st.session_state["b2_show_result"] = True

            if st.session_state.get("b2_show_result"):
                b2_earned = sum(st.session_state.scores[k][0] for k in labels_b2.keys() if k in st.session_state.scores)
                b2_total = sum(st.session_state.scores[k][1] for k in labels_b2.keys() if k in st.session_state.scores)
                b2_score_10 = round((b2_earned / b2_total) * 10, 2)
                st.success(f"📈 Kết quả Bài 2: **{b2_score_10} / 10** điểm")
                
                name = st.text_input("Tên học viên (Bài 2)", key="student_name_b2")
                if st.button("Nộp bài tập Bài 2"):
                    if name:
                        def fmt(key):
                            s = st.session_state.scores.get(key)
                            return f"{s[0]}/{s[1]}" if s else ""
                        row = {
                            "thời gian": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "học viên": name, 
                            "tổng điểm": b2_score_10, "BT1: Từ vựng": fmt("b2_vcb"), 
                            "BT2: Nghe": fmt("b2_ls"), "BT3: Điền âm": fmt("b2_fill")
                        }
                        if save_score_row_b2(row):
                            st.success("Đã lưu điểm Bài 2 thành công!")
                            st.session_state["b2_show_result"] = False
                            st.session_state.scores = {}
                            st.rerun()
                    else: st.error("Vui lòng nhập tên học viên!")
        
        all_s2 = load_all_scores_b2()
        if all_s2: st.dataframe(all_s2, use_container_width=True)
