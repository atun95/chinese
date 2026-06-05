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

    st.markdown("#### 2.2. Thanh nhẹ (轻声 - Qīngshēng)")
    st.write("Thanh nhẹ không có dấu trên Pinyin, đọc nhẹ và ngắn hơn các thanh khác.")
    
    st.markdown("""
    <table class="chinese-table">
      <tr style="background-color: #f1f5f9; font-weight: bold;">
        <th style="width: 25%;">Loại từ / Vị trí</th>
        <th style="width: 25%;">Ví dụ chữ Hán</th>
        <th style="width: 25%;">Pinyin & Cách đọc</th>
        <th style="width: 25%;">Ghi chú</th>
      </tr>
      <tr>
        <td><b>Trợ từ ngữ pháp</b></td>
        <td>的、吗、呢、吧、了</td>
        <td>de, ma, ne, ba, le</td>
        <td>Đọc nhẹ, không nhấn</td>
      </tr>
      <tr>
        <td><b>Hậu tố danh từ</b></td>
        <td>子、头</td>
        <td>zi, tou</td>
        <td>Âm cuối nhẹ, lướt nhanh</td>
      </tr>
      <tr>
        <td><b>Hậu tố đại từ</b></td>
        <td>们</td>
        <td>men</td>
        <td>Trong Chúng tôi (wǒ·men), Các bạn (nǐ·men)</td>
      </tr>
      <tr>
        <td><b>Từ chỉ phương vị</b></td>
        <td>上、下、里、边</td>
        <td>shang, xia, li, bian</td>
        <td>Khi làm hậu tố khinh thanh</td>
      </tr>
      <tr>
        <td><b>Từ láy / Thân thuộc</b></td>
        <td>爸爸、妈妈、哥哥</td>
        <td>bà·ba, mā·ma, gē·ge</td>
        <td>Âm thứ hai đọc nhẹ</td>
      </tr>
      <tr>
        <td><b>Động từ lặp</b></td>
        <td>看看、想想、试试</td>
        <td>kàn·kan, xiǎng·xiang, shì·shi</td>
        <td>Âm thứ hai đọc nhẹ</td>
      </tr>
      <tr>
        <td><b>Từ cố định</b></td>
        <td>知道、漂亮、葡萄</td>
        <td>zhī·dao, piào·liang, pú·tao</td>
        <td>Âm thứ hai đọc nhẹ</td>
      </tr>
    </table>
    """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 15px; font-weight: bold;'>🔊 Luyện nghe & đọc theo các ví dụ thanh nhẹ thông dụng:</div>", unsafe_allow_html=True)
    
    neutral_tone_examples = [
        {"word": "妈妈", "pinyin": "mā·ma", "meaning": "mẹ"},
        {"word": "爸爸", "pinyin": "bà·ba", "meaning": "bố"},
        {"word": "哥哥", "pinyin": "gē·ge", "meaning": "anh trai"},
        {"word": "姐姐", "pinyin": "jiě·jie", "meaning": "chị gái"},
        {"word": "弟弟", "pinyin": "dì·di", "meaning": "em trai"},
        {"word": "妹妹", "pinyin": "mèi·mei", "meaning": "em gái"},
        {"word": "爷爷", "pinyin": "yé·ye", "meaning": "ông nội"},
        {"word": "奶奶", "pinyin": "nǎi·nai", "meaning": "bà nội"},
        {"word": "看看", "pinyin": "kàn·kan", "meaning": "xem xem"},
        {"word": "知道", "pinyin": "zhī·dao", "meaning": "biết"},
        {"word": "漂亮", "pinyin": "piào·liang", "meaning": "đẹp"},
        {"word": "葡萄", "pinyin": "pú·tao", "meaning": "nho"},
    ]
    
    cols = st.columns(4)
    for idx, ex in enumerate(neutral_tone_examples):
        with cols[idx % 4]:
            st.markdown(
                f"""
                <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px; margin-bottom: 5px; background-color: #f8fafc; text-align: center;">
                    <div style="font-size: 1.25rem; font-weight: bold; color: #0f172a;">{ex['word']}</div>
                    <div style="color: #475569; font-family: monospace; font-weight: bold; margin: 2px 0;">{ex['pinyin']}</div>
                    <div style="font-size: 0.85rem; color: #64748b; margin-bottom: 4px;">({ex['meaning']})</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            render_play_button(ex['word'], "🔊 Nghe", key=f"btn_neutral_{idx}")

    st.markdown("---")
    st.markdown("#### 2.3. Quy tắc biến điệu thanh 3 (三声变调 - Sānshēng biàndiào)")
    st.write("Khi các âm tiết mang thanh 3 đi liền nhau, cao độ sẽ thay đổi để tạo sự uyển chuyển.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div style="border-left: 4px solid #3b82f6; background-color: #eff6ff; padding: 12px; border-radius: 4px; height: 100%;">
            <h5 style="margin-top:0; color: #1e3a8a;">1. Hai thanh 3 cạnh nhau (3 + 3)</h5>
            <p style="margin-bottom: 8px;"><b>Quy tắc:</b> Thanh 3 thứ nhất biến đổi thành <b>Thanh 2</b> (đọc giống sắc - hỏi).</p>
            <p style="margin-bottom: 4px; font-family: monospace;"><b>Công thức:</b> 3 + 3 ➔ 2 + 3</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("Ví dụ:")
        col_ex_1a, col_ex_1b = st.columns(2)
        with col_ex_1a:
            st.markdown("""
            <div style="padding: 8px; border: 1px dashed #cbd5e1; border-radius: 6px; text-align: center; background-color: #fafafa;">
                <span style="font-size: 1.1rem; font-weight: bold;">你好</span><br/>
                <span style="font-size: 0.85rem; color: #64748b;">nǐ + hǎo ➔ <b>ní hǎo</b></span><br/>
                <span style="font-size: 0.8rem; color: #94a3b8;">(Xin chào)</span>
            </div>
            """, unsafe_allow_html=True)
            render_play_button("你好", "🔊 Nghe ní hǎo", key="btn_bd_1a")
                
        with col_ex_1b:
            st.markdown("""
            <div style="padding: 8px; border: 1px dashed #cbd5e1; border-radius: 6px; text-align: center; background-color: #fafafa;">
                <span style="font-size: 1.1rem; font-weight: bold;">很好</span><br/>
                <span style="font-size: 0.85rem; color: #64748b;">hěn + hǎo ➔ <b>hén hǎo</b></span><br/>
                <span style="font-size: 0.8rem; color: #94a3b8;">(Rất tốt)</span>
            </div>
            """, unsafe_allow_html=True)
            render_play_button("很好", "🔊 Nghe hén hǎo", key="btn_bd_1b")

    with c2:
        st.markdown("""
        <div style="border-left: 4px solid #10b981; background-color: #ecfdf5; padding: 12px; border-radius: 4px; height: 100%;">
            <h5 style="margin-top:0; color: #064e3b;">2. Ba thanh 3 cạnh nhau (3 + 3 + 3)</h5>
            <p style="margin-bottom: 8px;"><b>Quy tắc:</b> Âm ở giữa (hoặc cả 2 âm đầu) biến thành <b>Thanh 2</b>. Phổ biến nhất là âm giữa biến điệu.</p>
            <p style="margin-bottom: 4px; font-family: monospace;"><b>Công thức:</b> 3 + 3 + 3 ➔ 3 + 2 + 3</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("Ví dụ:")
        col_ex_2a, col_ex_2b = st.columns(2)
        with col_ex_2a:
            st.markdown("""
            <div style="padding: 8px; border: 1px dashed #cbd5e1; border-radius: 6px; text-align: center; background-color: #fafafa;">
                <span style="font-size: 1.1rem; font-weight: bold;">好想你</span><br/>
                <span style="font-size: 0.85rem; color: #64748b;">hǎo xiǎng nǐ ➔ <b>háo xiáng nǐ</b></span><br/>
                <span style="font-size: 0.8rem; color: #94a3b8;">(Rất nhớ bạn)</span>
            </div>
            """, unsafe_allow_html=True)
            render_play_button("好想你", "🔊 Nghe háo xiáng nǐ", key="btn_bd_2a")
                
        with col_ex_2b:
            st.markdown("""
            <div style="padding: 8px; border: 1px dashed #cbd5e1; border-radius: 6px; text-align: center; background-color: #fafafa;">
                <span style="font-size: 1.1rem; font-weight: bold;">我很好</span><br/>
                <span style="font-size: 0.85rem; color: #64748b;">wǒ hěn hǎo ➔ <b>wó hén hǎo</b></span><br/>
                <span style="font-size: 0.8rem; color: #94a3b8;">(Tôi rất khỏe)</span>
            </div>
            """, unsafe_allow_html=True)
            render_play_button("我很好", "🔊 Nghe wó hén hǎo", key="btn_bd_2b")

    st.write("")
    st.markdown("""
    <div style="border-left: 4px solid #f59e0b; background-color: #fffbeb; padding: 12px; border-radius: 4px; margin-top: 10px;">
        <h5 style="margin-top:0; color: #78350f; font-size: 1rem;">3. Bốn thanh 3 cạnh nhau (3 + 3 + 3 + 3)</h5>
        <p style="margin-bottom: 6px;"><b>Quy tắc:</b> Ngắt nhịp 2-2 để đọc tự nhiên. Thanh thứ nhất và thứ ba đổi thành <b>Thanh 2</b>.</p>
        <p style="margin-bottom: 4px; font-family: monospace;"><b>Công thức:</b> 3 + 3 + 3 + 3 ➔ 2 + 3 + 2 + 3</p>
    </div>
    """, unsafe_allow_html=True)

    col_ex_3 = st.columns(3)
    with col_ex_3[0]:
        st.write("Ví dụ:")
        st.markdown("""
        <div style="padding: 8px; border: 1px dashed #cbd5e1; border-radius: 6px; text-align: center; background-color: #fafafa;">
            <span style="font-size: 1.1rem; font-weight: bold;">我也很好</span><br/>
            <span style="font-size: 0.85rem; color: #64748b;">wǒ yě hěn hǎo ➔ <b>wó yě hén hǎo</b></span><br/>
            <span style="font-size: 0.8rem; color: #94a3b8;">(Tôi cũng rất khỏe)</span>
        </div>
        """, unsafe_allow_html=True)
        render_play_button("我也很好", "🔊 Nghe wó yě hén hǎo", key="btn_bd_3")

    st.markdown("""
    <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 15px; margin-top: 15px;">
        <span style="font-size: 1.1rem; font-weight: bold; color: #0f172a;">💡 Mẹo ghi nhớ nhanh:</span>
        <ul style="margin-top: 8px; margin-bottom: 0; padding-left: 20px;">
            <li><b>Thanh nhẹ:</b> Coi như một "dấu huyền" rất ngắn và nhẹ trong tiếng Việt.</li>
            <li><b>Biến điệu:</b> Luôn nhớ quy tắc cửa miệng <b>nǐ hǎo ➔ ní hǎo</b>. Đây là quy tắc cốt lõi và phổ biến nhất khi mới bắt đầu.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


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
            render_play_button(q["hanzi"], "🔊 Nghe mẫu", key=f"listen_{i}")
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
