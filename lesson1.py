import streamlit as st
from datetime import datetime, timezone, timedelta
from lessons_data import *
from ui_utils import *

def show_lesson1_intro():
    render_lesson_intro("📚 Bài 1: Học phiên âm cơ bản", "Nắm thanh mẫu cơ bản, vận mẫu đơn, 5 thanh điệu và biến điệu thanh 3.")
    with st.expander("📊 Bảng tổng hợp Thanh mẫu & Vận mẫu", expanded=True):
        st.markdown("""<div style='margin-bottom: 10px;'><span style='background-color: #0f172a; color: white; padding: 5px 15px; border-radius: 5px; font-weight: bold;'>1</span><span style='font-size: 1.3rem; font-weight: bold; margin-left: 10px;'>声母 Thanh mẫu (Initials)</span></div><table class="chinese-table"><tr class="tm-header"><th style="width: 30%;">Vị trí phát âm</th><th>Thanh mẫu</th></tr><tr><td class="cat-col">Âm môi</td><td><span class="pinyin-text">b &nbsp; p &nbsp; m</span></td></tr><tr><td class="cat-col">Âm môi răng</td><td><span class="pinyin-text">f</span></td></tr><tr><td class="cat-col">Âm tròn môi</td><td><span class="pinyin-text">w</span></td></tr><tr><td class="cat-col">Âm đầu lưỡi trước</td><td><span class="pinyin-text">z &nbsp; c &nbsp; s</span></td></tr><tr><td class="cat-col">Âm đầu lưỡi giữa</td><td><span class="pinyin-text">d &nbsp; t &nbsp; n &nbsp; l</span></td></tr><tr><td class="cat-col">Âm đầu lưỡi sau</td><td><span class="pinyin-text">zh &nbsp; ch &nbsp; sh &nbsp; r</span></td></tr><tr><td class="cat-col">Âm mặt lưỡi</td><td><span class="pinyin-text">j &nbsp; q &nbsp; x</span></td></tr><tr><td class="cat-col">Âm cuống lưỡi</td><td><span class="pinyin-text">g &nbsp; k &nbsp; h &nbsp; y</span></td></tr></table><div style='margin-bottom: 10px; margin-top: 20px;'><span style='background-color: #fbbf24; color: #0f172a; padding: 5px 15px; border-radius: 5px; font-weight: bold;'>2</span><span style='font-size: 1.3rem; font-weight: bold; margin-left: 10px;'>韵母 Vận mẫu (Finals)</span></div><table class="chinese-table"><tr class="vm-header"><th style="width: 20%;">Loại</th><th style="text-align: center;">a</th><th style="text-align: center;">o</th><th style="text-align: center;">e</th><th style="text-align: center;">i</th><th style="text-align: center;">u</th><th style="text-align: center;">ü</th></tr><tr><td class="cat-col">Đơn</td><td style="text-align: center;"><span class="pinyin-text">a</span></td><td style="text-align: center;"><span class="pinyin-text">o</span></td><td style="text-align: center;"><span class="pinyin-text">e</span></td><td style="text-align: center;"><span class="pinyin-text">i</span></td><td style="text-align: center;"><span class="pinyin-text">u</span></td><td style="text-align: center;"><span class="pinyin-text">ü</span></td></tr><tr><td class="cat-col">Kép</td><td style="text-align: center;"><span class="pinyin-text">ai ao</span></td><td style="text-align: center;"><span class="pinyin-text">ou</span></td><td style="text-align: center;"><span class="pinyin-text">ei</span></td><td style="text-align: center;"><span class="pinyin-text">ia ie<br>iao iu</span></td><td style="text-align: center;"><span class="pinyin-text">ua uo<br>uai ui</span></td><td style="text-align: center;"><span class="pinyin-text">üe</span></td></tr><tr><td class="cat-col">Mũi</td><td style="text-align: center;"><span class="pinyin-text">an ang</span></td><td style="text-align: center;"><span class="pinyin-text">ong</span></td><td style="text-align: center;"><span class="pinyin-text">en eng</span></td><td style="text-align: center;"><span class="pinyin-text">ian in<br>iang ing<br>iong</span></td><td style="text-align: center;"><span class="pinyin-text">uan un<br>uang</span></td><td style="text-align: center;"><span class="pinyin-text">üan ün</span></td></tr></table>""", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("1. Thanh mẫu và vận mẫu cơ bản")
    st.markdown("#### 1.1. Thanh mẫu (Initials)")
    cols_tm = st.columns(4)
    for i, item in enumerate(B1_INITIALS_CARDS):
        with cols_tm[i % 4]: render_pronunciation_card(item, "b1_tm")
    st.markdown("---")
    st.markdown("#### 1.2. Vận mẫu (Finals)")
    cols_vm = st.columns(4)
    for i, item in enumerate(B1_FINALS_CARDS):
        with cols_vm[i % 4]: render_pronunciation_card(item, "b1_vm")
    
    st.markdown("---")
    st.subheader("2. Thanh điệu (Tones)")
    st.markdown("#### 2.1. Bốn thanh điệu cơ bản")
    col_t1, col_t2, col_t3, col_t4 = st.columns(4)
    with col_t1: st.info("**Thanh 1: mā**\n\n(Cao và ngang)")
    with col_t2: st.info("**Thanh 2: má**\n\n(Đi lên)")
    with col_t3: st.info("**Thanh 3: mǎ**\n\n(Hạ xuống rồi lên)")
    with col_t4: st.info("**Thanh 4: mà**\n\n(Đi xuống mạnh)")
    st.write("💡 *Thanh nhẹ: nhẹ, ngắn, không nhấn*")

    st.markdown("#### 2.2. Thanh nhẹ (轻声)")
    st.write("Thanh nhẹ thường xuất hiện ở âm tiết thứ hai trong từ láy hoặc một số từ thông dụng.")
    st.write("Ví dụ:")
    st.write("- **māma** (妈妈): âm tiết **ma** thứ hai là thanh nhẹ")
    st.write("- **bàba** (爸爸): âm tiết **ba** thứ hai là thanh nhẹ")
    st.write("- **gēge** (哥哥), **jiějie** (姐姐), **dìdi** (弟弟)")

    st.markdown("#### 2.3. Quy tắc biến điệu thanh 3")
    st.success("**Quy tắc chuẩn:** Khi hai thanh 3 đi liền nhau (**3 + 3**), âm tiết thứ nhất đổi thành **thanh 2**.")
    col_ex1, col_ex2 = st.columns(2)
    with col_ex1: st.code("nǐ + hǎo → ní hǎo", language="text")
    with col_ex2: st.code("wǒ + hěn → wó hěn", language="text")
    st.warning("⚠️ Với chuỗi **3 + 3 + 3**: Thường đổi 2 âm đầu thành thanh 2 (Ví dụ: nǐ wǒ hǎo → ní wó hǎo).")

def show_lesson1_vocab():
    render_lesson_intro("👨‍👩‍👧‍👦 Bài 1: Học TỪ VỰNG CƠ BẢN", "Học từ xưng hô, đại từ thường dùng và từ mở rộng để ghép câu ngắn.")
    st.subheader("Từ xưng hô dạng từ láy"); st.table(XUNG_HO_TU_LAY)
    st.subheader("Đại từ xưng hô cơ bản"); st.table(DAI_TU_XUNG_HO)
    st.subheader("Từ vựng bổ sung"); st.table(TU_VUNG_BO_SUNG)

def show_lesson1_exercises(save_progress, save_score_row, load_all_scores):
    st.header("📝 Bài 1: Bài tập tổng hợp")
    
    render_quiz_section(B1_QUIZ_VOCAB, "bai1", "Bài tập 1: Mini quiz từ vựng", "Chọn nghĩa đúng nhất cho từng từ.", save_progress)

    with st.expander("Bài tập 2: Âm bật hơi", expanded=False):
        col1, col2, col3 = st.columns(3)
        with col1: b = st.checkbox("B", key="q2_b"); p = st.checkbox("P", key="q2_p")
        with col2: d = st.checkbox("D", key="q2_d"); t = st.checkbox("T", key="q2_t")
        with col3: g = st.checkbox("G", key="q2_g"); k = st.checkbox("K", key="q2_k")
        if st.button("Kiểm tra kết quả"):
            if (p and t and k) and not (b or d or g):
                st.balloons(); st.success("Đúng! P, T, K là âm bật hơi."); st.session_state.scores["bai2"] = (1, 1)
            else: st.error("Sai rồi! Nhớ nhé: P, T, K là các âm bật hơi."); st.session_state.scores["bai2"] = (0, 1)
            save_progress()

    with st.expander("Bài tập 3: Điền vận mẫu", expanded=False):
        opts = ["...", "ā", "á", "ǎ", "à", "ē", "é", "ě", "è", "ǐ", "ǒ", "ù"]
        score = 0
        for i, (q, ans, meaning) in enumerate(B1_QUIZ_FILL_VM):
            key = f"vanmau_q_{i}"
            res = st.selectbox(f"Chọn vận mẫu cho {q} ({meaning})", opts, index=0, key=key)
            if res == ans: score += 1
        if st.button("Chấm điểm bài 3"): st.session_state.scores["bai3"] = (score, len(B1_QUIZ_FILL_VM)); save_progress(); st.success(f"Bạn đúng {score}/{len(B1_QUIZ_FILL_VM)} câu.")

    render_quiz_section(B1_QUIZ_PY, "bai4", "Bài tập 4: Dịch sang Pinyin", "Chọn Pinyin đúng cho nghĩa tiếng Việt tương ứng.", save_progress)

    with st.expander("Bài tập 5: Luyện thanh điệu (nghe)", expanded=False):
        score_5 = 0
        for i, q in enumerate(B1_QUIZ_TONE):
            st.write(f"**Câu {i+1}:** Nghe và chọn pinyin đúng")
            if st.button(f"🔊 Nghe mẫu", key=f"listen_{i}"): play_audio(q["hanzi"])
            key = f"tone_q_{i}"
            choices = q["choices"][:]
            if choices[0] == q["answer"] and len(choices) > 1:
                choices[0], choices[1] = choices[1], choices[0]
            res = st.radio("Chọn đáp án:", choices, index=0, key=key)
            if res == q["answer"]: score_5 += 1
        if st.button("Chấm điểm bài 5"): st.session_state.scores["bai5"] = (score_5, len(B1_QUIZ_TONE)); save_progress(); st.success(f"Bạn đúng {score_5}/{len(B1_QUIZ_TONE)} câu.")

    render_quiz_section(B1_QUIZ_SENTENCE, "bai6", "Bài tập 6: Câu ngắn", "Chọn nghĩa đúng của câu ngắn.", save_progress)

    with st.expander("📊 Lịch sử & Tổng kết", expanded=True):
        labels = {"bai1": "BT1: Từ vựng", "bai2": "BT2: Bật hơi", "bai3": "BT3: Vận mẫu", "bai4": "BT4: Đọc & Viết", "bai5": "BT5: Nghe", "bai6": "BT6: Câu ngắn"}
        missing = [v for k, v in labels.items() if k not in st.session_state.scores]
        if missing: st.warning(f"Chưa xong: {', '.join(missing)}")
        else:
            earned = sum(s[0] for s in st.session_state.scores.values() if isinstance(s, tuple))
            total = sum(s[1] for s in st.session_state.scores.values() if isinstance(s, tuple))
            score_10 = round((earned / total) * 10, 2)
            
            st.success(f"📈 Kết quả tổng quát: **{score_10} / 10** điểm")
            st.info(f"Chi tiết: Đúng {earned} trên tổng số {total} câu hỏi.")
            
            name = st.text_input("Tên học viên", key="student_name")
            if st.button("Nộp bài"):
                if name: 
                    def fmt_b1(key):
                        s = st.session_state.scores.get(key)
                        return f"{s[0]}/{s[1]}" if s else ""
                    row = {
                        "thời gian": datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S"), "học viên": name, 
                        "tổng điểm": score_10, "BT1: Từ vựng": fmt_b1("bai1"), 
                        "BT2: Âm bật hơi": fmt_b1("bai2"), "BT3: Vận mẫu": fmt_b1("bai3"), 
                        "BT4: Pinyin": fmt_b1("bai4"), "BT5: Nghe": fmt_b1("bai5"), 
                        "BT6: Câu ngắn": fmt_b1("bai6")
                    }
                    if save_score_row(row):
                        st.success("Đã lưu điểm Bài 1 thành công!"); st.session_state.scores = {}; st.rerun()
                else: st.error("Vui lòng nhập tên học viên!")
        
        all_s = load_all_scores()
        if all_s: st.dataframe(all_s, use_container_width=True)
