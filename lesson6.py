import streamlit as st
import random
from datetime import datetime, timezone, timedelta
from ui_utils import render_lesson_intro, render_play_button

def show_lesson6_1_duanwu(save_progress, save_score_row_b6_1, load_all_scores_b6_1):
    # CSS Styles sang trọng cho Tết Đoan Ngọ (Màu đỏ đô kết hợp vàng cam ấm cúng và xanh lá của bánh ú)
    st.markdown("""
    <style>
    /* Card từ vựng */
    .vocab-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 16px;
        margin-top: 15px;
    }
    .vocab-card {
        background: #ffffff;
        border: 1px solid #f3f4f6;
        border-left: 6px solid #e11d48; /* Màu đỏ lễ hội */
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .vocab-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        border-color: #fecdd3;
    }
    .vocab-hanzi {
        font-size: 2.2rem;
        font-weight: 800;
        color: #9f1239;
        margin-bottom: 2px;
    }
    .vocab-pinyin {
        font-family: 'Courier New', monospace;
        font-size: 1.1rem;
        color: #2563eb;
        font-weight: bold;
        margin-bottom: 6px;
    }
    .vocab-meaning {
        font-size: 0.95rem;
        color: #374151;
        font-weight: 500;
    }
    .vocab-note {
        font-size: 0.82rem;
        color: #6b7280;
        margin-top: 6px;
        font-style: italic;
    }
    
    /* Bong bóng chat hội thoại */
    .chat-container {
        background-color: #fcf8f2;
        border: 1px solid #f5ebe0;
        border-radius: 16px;
        padding: 20px;
        margin: 15px 0;
        max-width: 800px;
    }
    .chat-bubble {
        display: flex;
        flex-direction: column;
        margin-bottom: 16px;
        max-width: 80%;
    }
    .chat-bubble.left {
        align-self: flex-start;
        margin-right: auto;
    }
    .chat-bubble.right {
        align-self: flex-end;
        margin-left: auto;
        align-items: flex-end;
    }
    .chat-avatar {
        font-size: 1.3rem;
        margin-bottom: 4px;
        font-weight: bold;
        color: #4b5563;
    }
    .chat-content {
        padding: 12px 16px;
        border-radius: 16px;
        font-size: 1.15rem;
        line-height: 1.4;
        box-shadow: 0 2px 4px rgba(0,0,0,0.03);
    }
    .chat-bubble.left .chat-content {
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        color: #1f2937;
        border-top-left-radius: 4px;
    }
    .chat-bubble.right .chat-content {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: #ffffff;
        border-top-right-radius: 4px;
    }
    .chat-translation {
        font-size: 0.9rem;
        color: #6b7280;
        margin-top: 4px;
        font-style: italic;
    }
    .chat-bubble.right .chat-translation {
        color: #9ca3af;
        text-align: right;
    }
    
    /* Khối cấu trúc mẫu câu */
    .pattern-card {
        background: #fdf6f0;
        border-left: 5px solid #d97706;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 12px;
    }
    .pattern-title {
        font-weight: bold;
        color: #b45309;
        font-size: 1.05rem;
        margin-bottom: 6px;
    }
    
    /* Interactive Word Builder */
    .word-badge {
        display: inline-block;
        background-color: #f3f4f6;
        border: 1px solid #d1d5db;
        border-radius: 20px;
        padding: 6px 14px;
        margin: 5px;
        font-size: 1.1rem;
        font-weight: 500;
        cursor: pointer;
        user-select: none;
        transition: all 0.15s ease;
    }
    .word-badge:hover {
        background-color: #dbeafe;
        border-color: #3b82f6;
        color: #1d4ed8;
    }
    .word-badge:active {
        transform: scale(0.95);
    }
    .builder-result-box {
        background-color: #ffffff;
        border: 2px dashed #93c5fd;
        border-radius: 12px;
        padding: 15px;
        min-height: 56px;
        margin: 15px 0;
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 8px;
    }
    .builder-word {
        background-color: #eff6ff;
        color: #1e40af;
        border: 1px solid #bfdbfe;
        border-radius: 15px;
        padding: 4px 12px;
        font-size: 1.1rem;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "🎏 Bài 6.1: Tết Đoan Ngọ cùng HSK 1",
        "Chủ đề khóa học: 今天是端午节! (Hôm nay là Tết Đoan Ngọ!) - Học từ vựng, mẫu câu, đóng vai hội thoại và luyện tập HSK 1 thực tế."
    )

    tab_vocab, tab_patterns, tab_dialogue, tab_practice = st.tabs([
        "📚 生词 - Từ vựng",
        "🎯 句子 - Mẫu câu",
        "🗣️ 对话 - Hội thoại",
        "📝 练习 - Luyện tập"
    ])

    # ================= TAB 1: TỪ VỰNG =================
    with tab_vocab:
        st.subheader("PHẦN 1: TỪ VỰNG MỚI (生词 - Shēngcí)")
        st.write("💡 *Gợi ý cho giáo viên: Cho học viên nhìn tranh ảnh về ngày Tết Đoan Ngọ (bánh tro/bánh ú, quả vải, quả mận) và đọc to các từ sau:*")

        vocab_data = [
            {"hanzi": "今天", "pinyin": "jīntiān", "meaning": "Hôm nay", "note": "Từ vựng HSK 1"},
            {"hanzi": "五月五号", "pinyin": "wǔ yuè wǔ hào", "meaning": "Ngày 5 tháng 5", "note": "Số đếm + Ngày tháng HSK 1"},
            {"hanzi": "端午节", "pinyin": "Duānwǔ jié", "meaning": "Tết Đoan Ngọ", "note": "Từ mới theo chủ đề"},
            {"hanzi": "吃", "pinyin": "chī", "meaning": "Ăn", "note": "Động từ HSK 1"},
            {"hanzi": "粽子", "pinyin": "zòngzi", "meaning": "Bánh chưng Tàu / Bánh ú / Bánh tro", "note": "Từ mới theo chủ đề"},
            {"hanzi": "水果", "pinyin": "shuǐguǒ", "meaning": "Hoa quả / Trái cây", "note": "Từ vựng HSK 1"},
            {"hanzi": "高兴", "pinyin": "gāoxìng", "meaning": "Vui vẻ", "note": "Tính từ HSK 1"}
        ]

        # Hiển thị grid từ vựng
        st.markdown('<div class="vocab-grid">', unsafe_allow_html=True)
        cols = st.columns(3)
        for idx, item in enumerate(vocab_data):
            col_idx = idx % 3
            with cols[col_idx]:
                st.markdown(f"""
                <div class="vocab-card">
                    <div class="vocab-hanzi">{item['hanzi']}</div>
                    <div class="vocab-pinyin">{item['pinyin']}</div>
                    <div class="vocab-meaning">👉 {item['meaning']}</div>
                    <div class="vocab-note">📌 {item['note']}</div>
                </div>
                """, unsafe_allow_html=True)
                render_play_button(item['hanzi'], f"🔊 Phát âm: {item['hanzi']}", key=f"play_v61_{idx}")
                st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ================= TAB 2: MẪU CÂU =================
    with tab_patterns:
        st.subheader("PHẦN 2: MẪU CÂU CƠ BẢN (句子 - Jùzi)")
        st.write("Giáo viên giảng giải cấu trúc ngữ pháp HSK 1 thông qua các câu thực tế ngày Tết Đoan Ngọ:")

        # Mẫu câu 1
        st.markdown("""
        <div class="pattern-card">
            <div class="pattern-title">1. Giới thiệu ngày lễ (Cấu trúc: Ngày tháng + 是 + Tên ngày lễ)</div>
            <div style="font-size: 1.3rem; font-weight: bold; color: #1e3a8a;">今天是五月五号，端午节。</div>
            <div style="font-family: monospace; font-size: 1rem; color: #2563eb; margin: 4px 0;">Jīntiān shì wǔ yuè wǔ hào, Duānwǔ jié.</div>
            <div style="color: #059669; font-style: italic; font-size: 0.95rem;">Dịch nghĩa: Hôm nay là ngày 5 tháng 5, Tết Đoan Ngọ.</div>
            <div style="font-size: 0.85rem; color: #475569; margin-top: 6px;"><b>Ngữ pháp HSK 1:</b> Cách nói ngày tháng trong tiếng Trung (Tháng trước - 月, ngày sau - 号).</div>
        </div>
        """, unsafe_allow_html=True)
        render_play_button("今天是五月五号，端午节。", "🔊 Nghe phát âm mẫu câu 1", key="play_pattern_1")
        st.markdown("<br>", unsafe_allow_html=True)

        # Mẫu câu 2
        st.markdown("""
        <div class="pattern-card">
            <div class="pattern-title">2. Nói về hoạt động ăn uống (Cấu trúc: Ai + 吃 + Cái gì)</div>
            <div style="font-size: 1.3rem; font-weight: bold; color: #1e3a8a;">🇨🇳 中国人吃粽子。 / 🇻🇳 越南人也吃粽子。</div>
            <div style="font-family: monospace; font-size: 1rem; color: #2563eb; margin: 4px 0;">Zhōngguó rén chī zòngzi. / Yuènán rén yě chī zòngzi.</div>
            <div style="color: #059669; font-style: italic; font-size: 0.95rem;">Dịch nghĩa: Người Trung Quốc ăn bánh ú. / Người Việt Nam cũng ăn bánh ú.</div>
            <div style="font-size: 0.85rem; color: #475569; margin-top: 6px;"><b>Ngữ pháp HSK 1:</b> Phó từ <b>也 (yě - cũng)</b> đứng trước động từ hành động <b>吃 (chī - ăn)</b>.</div>
        </div>
        """, unsafe_allow_html=True)
        col_p2_1, col_p2_2 = st.columns(2)
        with col_p2_1:
            render_play_button("中国人吃粽子。", "🔊 Trung Quốc ăn bánh ú", key="play_pattern_2_cn")
        with col_p2_2:
            render_play_button("越南人也吃粽子。", "🔊 Việt Nam cũng ăn bánh ú", key="play_pattern_2_vn")
        st.markdown("<br>", unsafe_allow_html=True)

        # Mẫu câu 3
        st.markdown("""
        <div class="pattern-card">
            <div class="pattern-title">3. Nói về sở thích & Trái cây mùa hè (Cấu trúc: Ai + 喜欢吃 + Trái cây)</div>
            <div style="font-size: 1.3rem; font-weight: bold; color: #1e3a8a;">我喜欢吃水果。</div>
            <div style="font-family: monospace; font-size: 1rem; color: #2563eb; margin: 4px 0;">Wǒ xǐhuan chī shuǐguǒ.</div>
            <div style="color: #059669; font-style: italic; font-size: 0.95rem;">Dịch nghĩa: Tôi thích ăn hoa quả (vải, mận...).</div>
            <div style="font-size: 0.85rem; color: #475569; margin-top: 6px;"><b>Ngữ pháp HSK 1:</b> Động từ tâm lý <b>喜欢 (xǐhuan - thích)</b> kết hợp trực tiếp trước động từ hành động <b>吃 (chī - ăn)</b>.</div>
        </div>
        """, unsafe_allow_html=True)
        render_play_button("我喜欢吃水果。", "🔊 Nghe phát âm mẫu câu 3", key="play_pattern_3")
        st.markdown("<br>", unsafe_allow_html=True)

        # Mẫu câu 4
        st.markdown("""
        <div class="pattern-card">
            <div class="pattern-title">4. Thể hiện cảm xúc (Cấu trúc: 太 + Tính từ + 了)</div>
            <div style="font-size: 1.3rem; font-weight: bold; color: #1e3a8a;">今天我太高兴了！</div>
            <div style="font-family: monospace; font-size: 1rem; color: #2563eb; margin: 4px 0;">Jīntiān wǒ tài gāoxìng le!</div>
            <div style="color: #059669; font-style: italic; font-size: 0.95rem;">Dịch nghĩa: Hôm nay tôi vui quá rồi!</div>
            <div style="font-size: 0.85rem; color: #475569; margin-top: 6px;"><b>Ngữ pháp HSK 1:</b> Cấu trúc cảm thán <b>太......了 (tài...le - quá...rồi)</b> dùng để nhấn mạnh mức độ cảm xúc.</div>
        </div>
        """, unsafe_allow_html=True)
        render_play_button("今天我太高兴了！", "🔊 Nghe phát âm mẫu câu 4", key="play_pattern_4")

    # ================= TAB 3: HỘI THOẠI =================
    with tab_dialogue:
        st.subheader("PHẦN 3: ĐOẠN HỘI THOẠI NGẮN (对话 - Duìhuà)")
        st.write("🗣️ *Giáo viên chia cặp cho học viên thực hành đóng vai nhân vật A và B:*")

        st.markdown("""
        <div class="chat-container">
            <!-- Nhân vật A -->
            <div class="chat-bubble left">
                <div class="chat-avatar">🙋‍♂️ Nhân vật A</div>
                <div class="chat-content">
                    喂，今天是端午节，你做什么？
                </div>
                <div style="font-family: monospace; font-size: 0.9rem; color: #2563eb; margin-top: 4px;">
                    Wèi, jīntiān shì Duānwǔ jié, nǐ zuò shénme?
                </div>
                <div class="chat-translation">
                    Dịch: Alo, hôm nay là Tết Đoan Ngọ, bạn làm gì thế?
                </div>
            </div>
        """, unsafe_allow_html=True)
        render_play_button("喂，今天是端午节，你做什么？", "🔊 Nghe phát âm nhân vật A (Câu 1)", key="play_chat_a1")
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
            <!-- Nhân vật B -->
            <div class="chat-bubble right">
                <div class="chat-avatar">🙋‍♀️ Nhân vật B</div>
                <div class="chat-content">
                    我家吃粽子，吃水果。你呢？
                </div>
                <div style="font-family: monospace; font-size: 0.9rem; color: #dbeafe; margin-top: 4px; text-align: right;">
                    Wǒ jiā chī zòngzi, chī shuǐguǒ. Nǐ ne?
                </div>
                <div class="chat-translation">
                    Dịch: Nhà tôi ăn bánh ú, ăn hoa quả. Còn bạn thì sao?
                </div>
            </div>
        """, unsafe_allow_html=True)
        render_play_button("我家吃粽子，吃水果。你呢？", "🔊 Nghe phát âm nhân vật B (Câu 2)", key="play_chat_b1")
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
            <!-- Nhân vật A -->
            <div class="chat-bubble left">
                <div class="chat-avatar">🙋‍♂️ Nhân vật A</div>
                <div class="chat-content">
                    我去商店买东西。今天我太高兴了！
                </div>
                <div style="font-family: monospace; font-size: 0.9rem; color: #2563eb; margin-top: 4px;">
                    Wǒ qù shāngdiàn mǎi dōngxi. Jīntiān wǒ tài gāoxìng le!
                </div>
                <div class="chat-translation">
                    Dịch: Tôi đi cửa hàng mua đồ. Hôm nay tôi vui quá đi mất!
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        render_play_button("我去商店买东西。今天我太高兴了！", "🔊 Nghe phát âm nhân vật A (Câu 3)", key="play_chat_a2")

    # ================= TAB 4: LUYỆN TẬP =================
    with tab_practice:
        st.subheader("PHẦN 4: BÀI TẬP LUYỆN TẬP TẠI LỚP (练习 - Liànxí)")
        st.write("Sắp xếp các từ sau thành câu hoàn chỉnh (Chuẩn form đề thi Đọc hiểu HSK 1):")

        # Initialize session state for practice
        if "b61_score_submitted" not in st.session_state:
            st.session_state.b61_score_submitted = False
        
        # Word Builder 1: "吃 / 我 / 粽子 / 喜欢 / 。"
        st.markdown("#### 🧩 Câu 1: Sắp xếp các từ sau:")
        st.markdown("**`吃` &nbsp;&nbsp;/&nbsp;&nbsp; `我` &nbsp;&nbsp;/&nbsp;&nbsp; `粽子` &nbsp;&nbsp;/&nbsp;&nbsp; `喜欢` &nbsp;&nbsp;/&nbsp;&nbsp; `。`**")
        
        if "builder_1" not in st.session_state:
            st.session_state.builder_1 = []
            
        words_1 = ["我", "喜欢", "吃", "粽子", "。"]
        # Xáo trộn các từ để học viên click
        random_words_1 = ["吃", "粽子", "喜欢", "我", "。"]
        
        # Hiển thị các nút từ khóa để chọn
        st.write("Chọn từ để ghép câu:")
        cols_b1 = st.columns(len(random_words_1))
        for i, word in enumerate(random_words_1):
            with cols_b1[i]:
                if st.button(word, key=f"btn_word1_{word}_{i}"):
                    st.session_state.builder_1.append(word)
                    st.rerun()
                    
        # Hiển thị kết quả ghép hiện tại
        st.markdown('<div class="builder-result-box">', unsafe_allow_html=True)
        if st.session_state.builder_1:
            for word in st.session_state.builder_1:
                st.markdown(f'<span class="builder-word">{word}</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span style="color:#9ca3af; font-style:italic;">Câu trả lời của bạn sẽ hiển thị ở đây...</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        col_clear_1, col_back_1 = st.columns(2)
        with col_clear_1:
            if st.button("🔄 Làm sạch câu 1", use_container_width=True, key="clear_b1"):
                st.session_state.builder_1 = []
                st.rerun()
        with col_back_1:
            if st.button("⬅️ Xóa từ cuối", use_container_width=True, key="back_b1"):
                if st.session_state.builder_1:
                    st.session_state.builder_1.pop()
                    st.rerun()

        # Word Builder 2: "端午节 / 是 / 今天 / 了 / 太好 / ！"
        st.markdown("---")
        st.markdown("#### 🧩 Câu 2: Sắp xếp các từ sau:")
        st.markdown("**`端午节` &nbsp;&nbsp;/&nbsp;&nbsp; `是` &nbsp;&nbsp;/&nbsp;&nbsp; `今天` &nbsp;&nbsp;/&nbsp;&nbsp; `了` &nbsp;&nbsp;/&nbsp;&nbsp; `太好` &nbsp;&nbsp;/&nbsp;&nbsp; `！`**")
        
        if "builder_2" not in st.session_state:
            st.session_state.builder_2 = []
            
        words_2 = ["今天", "是", "端午节", "，", "太好", "了", "！"]
        random_words_2 = ["端午节", "是", "今天", "了", "太好", "！"]
        
        st.write("Chọn từ để ghép câu:")
        cols_b2 = st.columns(len(random_words_2))
        for i, word in enumerate(random_words_2):
            with cols_b2[i]:
                if st.button(word, key=f"btn_word2_{word}_{i}"):
                    # Chèn thêm dấu phẩy ngầm nếu học viên ghép để giống đáp án mẫu
                    if word == "太好" and st.session_state.builder_2 and st.session_state.builder_2[-1] == "端午节":
                        st.session_state.builder_2.append("，")
                    st.session_state.builder_2.append(word)
                    st.rerun()
                    
        # Hiển thị kết quả ghép hiện tại
        st.markdown('<div class="builder-result-box">', unsafe_allow_html=True)
        if st.session_state.builder_2:
            for word in st.session_state.builder_2:
                st.markdown(f'<span class="builder-word">{word}</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span style="color:#9ca3af; font-style:italic;">Câu trả lời của bạn sẽ hiển thị ở đây...</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        col_clear_2, col_back_2 = st.columns(2)
        with col_clear_2:
            if st.button("🔄 Làm sạch câu 2", use_container_width=True, key="clear_b2"):
                st.session_state.builder_2 = []
                st.rerun()
        with col_back_2:
            if st.button("⬅️ Xóa từ cuối", use_container_width=True, key="back_b2"):
                if st.session_state.builder_2:
                    last = st.session_state.builder_2.pop()
                    if last == "太好" and st.session_state.builder_2 and st.session_state.builder_2[-1] == "，":
                        st.session_state.builder_2.pop()
                    st.rerun()

        st.markdown("---")
        
        # Tính toán kết quả chấm điểm
        user_ans_1 = "".join(st.session_state.builder_1)
        user_ans_2 = "".join(st.session_state.builder_2)
        
        # Đáp án chuẩn hóa: không tính dấu hoặc so khớp chính xác
        correct_ans_1 = "我喜欢吃粽子。"
        # Đáp án 2 linh hoạt: "今天是端午节，太好了！" hoặc "今天是端午节太好了！"
        correct_ans_2_a = "今天是端午节，太好了！"
        correct_ans_2_b = "今天是端午节太好了！"
        
        score_6_1 = 0
        ans1_is_correct = (user_ans_1 == correct_ans_1)
        ans2_is_correct = (user_ans_2 == correct_ans_2_a or user_ans_2 == correct_ans_2_b)
        
        if ans1_is_correct:
            score_6_1 += 1
        if ans2_is_correct:
            score_6_1 += 1

        if not st.session_state.b61_score_submitted:
            if st.button("📝 Chấm điểm bài tập Bài 6.1", type="primary", use_container_width=True):
                st.session_state.b61_score_submitted = True
                st.session_state.scores["b61_practice"] = (score_6_1, 2)
                save_progress()
                st.rerun()
        else:
            # Hiện feedback cho từng câu
            st.markdown("### Kết quả chi tiết:")
            
            if ans1_is_correct:
                st.success("✅ **Câu 1: Chính xác!**")
                st.markdown(f"Đọc: **{correct_ans_1}** (Tôi thích ăn bánh ú.)")
            else:
                st.error("❌ **Câu 1: Chưa chính xác!**")
                st.markdown(f"Đáp án đúng: **{correct_ans_1}**")
                
            if ans2_is_correct:
                st.success("✅ **Câu 2: Chính xác!**")
                st.markdown(f"Đọc: **{correct_ans_2_a}** (Hôm nay là Tết Đoan Ngọ, tốt quá rồi!)")
            else:
                st.error("❌ **Câu 2: Chưa chính xác!**")
                st.markdown(f"Đáp án đúng: **{correct_ans_2_a}**")
                
            st.markdown(f"### Điểm tổng kết: **{score_6_1} / 2**")
            
            if score_6_1 == 2:
                st.balloons()
                st.success("Chúc mừng! Bạn đã trả lời xuất sắc cả 2 câu hỏi! 🎉")
                
            st.markdown("---")
            name = st.text_input("Tên học viên (Bài 6.1)", key="student_name_b61")
            if st.button("Nộp bài tập Bài 6.1", type="primary", use_container_width=True):
                if name:
                    row = {
                        "thời gian": datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S"),
                        "học viên": name,
                        "tổng điểm": round((score_6_1 / 2) * 10, 2),
                        "BT: Ghép câu": f"{score_6_1}/2"
                    }
                    if save_score_row_b6_1(row):
                        st.success("Đã lưu kết quả bài tập Bài 6.1 thành công!")
                        st.session_state.builder_1 = []
                        st.session_state.builder_2 = []
                        st.session_state.b61_score_submitted = False
                        if "b61_practice" in st.session_state.scores:
                            del st.session_state.scores["b61_practice"]
                        save_progress()
                        st.rerun()
                else:
                    st.error("Vui lòng nhập tên học viên để nộp bài!")
                    
            if st.button("🔄 Làm lại bài tập", use_container_width=True):
                st.session_state.builder_1 = []
                st.session_state.builder_2 = []
                st.session_state.b61_score_submitted = False
                if "b61_practice" in st.session_state.scores:
                    del st.session_state.scores["b61_practice"]
                save_progress()
                st.rerun()

        # Hiển thị lịch sử nộp bài lớp học
        all_scores = load_all_scores_b6_1()
        if all_scores:
            st.write("### 📜 Lịch sử nộp bài lớp học:")
            st.dataframe(all_scores, use_container_width=True)
