import streamlit as st
import random
from datetime import datetime, timezone, timedelta
from ui_utils import render_lesson_intro, render_play_button
from lessons_data import (
    B7_1_QUESTION_WORDS_DATA, B7_1_QUIZ_DATA,
    B7_2_DE_DATA, B7_2_QUIZ_DATA
)

def show_lesson7_1_question_words(save_progress, save_score_row_b7_1, load_all_scores_b7_1):
    # CSS Styles sang trọng cho Bài 7.1
    st.markdown("""
    <style>
    .word-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .word-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
    }
    .word-title {
        font-size: 2.2rem;
        font-weight: 800;
        font-family: 'Inter', sans-serif;
        color: #1e3a8a;
        margin-right: 15px;
    }
    .pinyin-badge {
        background-color: #eff6ff;
        color: #1d4ed8;
        padding: 4px 10px;
        border-radius: 20px;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        font-size: 1.1rem;
        border: 1px solid #bfdbfe;
    }
    .meaning-badge {
        background-color: #f0fdf4;
        color: #15803d;
        padding: 4px 10px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.95rem;
        border: 1px solid #bbf7d0;
    }
    .rule-box {
        background-color: #f8fafc;
        border-left: 5px solid #3b82f6;
        border-radius: 8px;
        padding: 15px;
        margin: 15px 0 0 0;
    }
    .comparison-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 1px solid #e2e8f0;
        border-left: 6px solid #8b5cf6;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.02);
    }
    .comparison-title {
        font-weight: 700;
        color: #7c3aed;
        font-size: 1.2rem;
        margin-bottom: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "📚 Bài 7.1: Các từ để hỏi",
        "Làm chủ hệ thống đại từ và trợ từ nghi vấn trong HSK 1 để hỏi về người, vật, địa điểm, số lượng, phương thức và trạng thái."
    )

    tab_vocab, tab_comparison, tab_practice, tab_quiz = st.tabs([
        "📚 Bảng từ để hỏi",
        "💡 Phân tích & So sánh",
        "🗣️ Thực hành khẩu ngữ",
        "📝 Bài tập phản xạ"
    ])

    # ================= TAB 1: BẢNG TỪ ĐỂ HỎI =================
    with tab_vocab:
        st.subheader("Hệ thống từ để hỏi HSK 1")
        st.write("Dưới đây là các từ để hỏi cốt lõi được phân nhóm theo mục đích sử dụng:")

        for group_idx, group in enumerate(B7_1_QUESTION_WORDS_DATA):
            st.markdown(f"### 📌 {group['nhom']}")
            st.write(group['mota'])

            for idx, item in enumerate(group["items"]):
                cols = st.columns([7, 3])
                with cols[0]:
                    cautrucs_html = ""
                    for ct_idx, ct_item in enumerate(item.get("cautrucs", [])):
                        cautrucs_html += f"""
                        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:12px; margin-bottom:10px;">
                            <div style="background:#eff6ff; border-left:4px solid #3b82f6; border-radius:4px; padding:4px 8px; font-size:0.9rem; font-family:'Courier New',monospace; color:#1d4ed8; font-weight:bold; margin-bottom:6px;">
                                📐 Cấu trúc {ct_idx+1}: {ct_item['ct']}
                            </div>
                            <div style="padding-left: 8px;">
                                <span style="font-size: 1.25rem; font-weight: 700; color: #0f172a; display: block;">{ct_item['vd_han']}</span>
                                <span style="font-family: monospace; font-size: 1.05rem; font-weight: bold; color: #2563eb; display: block; margin-top:2px;">{ct_item['vd_py']}</span>
                                <span style="font-size: 0.92rem; color: #475569; display: block; font-style: italic; margin-top:2px;">➔ Dịch: {ct_item['vd_vi']}</span>
                            </div>
                        </div>
                        """
                    
                    if not cautrucs_html:
                        cautrucs_html = f"""
                        <p style="background:#eff6ff; border-left:4px solid #3b82f6; border-radius:6px; padding:6px 10px; font-size:0.92rem; margin-bottom:8px; font-family:'Courier New',monospace; color:#1d4ed8;"><b>📐 Cấu trúc:</b> {item.get('cautruc','')}</p>
                        <div class="rule-box">
                            <span style="font-size: 0.85em; font-weight: bold; color: #1e293b;">VÍ DỤ TIÊU BIỂU:</span><br/>
                            <span style="font-size: 1.3rem; font-weight: 700; color: #0f172a; display: block; margin-top: 5px;">{item['vd_han']}</span>
                            <span style="font-family: monospace; font-size: 1.05rem; font-weight: bold; color: #2563eb; display: block;">{item['vd_py']}</span>
                            <span style="font-size: 0.95rem; color: #475569; display: block; font-style: italic; margin-top: 2px;">➔ Dịch: {item['vd_vi']}</span>
                        </div>
                        """

                    card_html = f"""
                    <div class="word-card">
                        <div style="display: flex; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 10px;">
                            <span class="word-title">{item['tu']}</span>
                            <span class="pinyin-badge">{item['pinyin']}</span>
                            <span class="meaning-badge">{item['nghianhanh']}</span>
                        </div>
                        <p style="color: #475569; font-size: 0.95rem; margin-bottom: 8px;"><b>Cách dùng:</b> {item['cachdung']}</p>
                        {cautrucs_html}
                    </div>
                    """
                    st.markdown(card_html, unsafe_allow_html=True)
                with cols[1]:
                    st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
                    render_play_button(
                        item['sound_txt'], 
                        f"🔊 Phát âm câu ví dụ", 
                        key=f"play_v71_{group_idx}_{idx}"
                    )
            st.markdown("<br/>", unsafe_allow_html=True)

    # ================= TAB 2: PHÂN TÍCH & SO SÁNH =================
    with tab_comparison:
        st.subheader("💡 So sánh các cặp từ dễ nhầm lẫn")
        st.write("Để giao tiếp chính xác, người học cần lưu ý sự khác biệt của các cặp từ nghi vấn sau:")

        # Cặp 1: 几 (jǐ) vs 多少 (duōshao)
        st.markdown(
            """
            <div class="comparison-card">
                <div class="comparison-title">1. Phân biệt 几 (jǐ) và 多少 (duōshao)</div>
                <table style="width:100%; border-collapse: collapse; margin-top: 10px;">
                    <tr style="background-color: #f1f5f9;">
                        <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">Đặc điểm</th>
                        <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">几 (jǐ)</th>
                        <th style="padding: 10px; border: 1px solid #cbd5e1; text-align: left;">多少 (duōshao)</th>
                    </tr>
                    <tr>
                        <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Số lượng ước tính</td>
                        <td style="padding: 10px; border: 1px solid #cbd5e1;">Nhỏ (thường < 10)</td>
                        <td style="padding: 10px; border: 1px solid #cbd5e1;">Lớn hoặc không xác định trước</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Yêu cầu lượng từ</td>
                        <td style="padding: 10px; border: 1px solid #cbd5e1; color: #b91c1c; font-weight: bold;">Bắt buộc có (几 + Lượng từ + Danh từ)</td>
                        <td style="padding: 10px; border: 1px solid #cbd5e1; color: #15803d;">Không bắt buộc (có thể lược bỏ)</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">Phạm vi sử dụng</td>
                        <td style="padding: 10px; border: 1px solid #cbd5e1;">Ngày tháng, giờ, thành viên gia đình...</td>
                        <td style="padding: 10px; border: 1px solid #cbd5e1;">Giá cả (多少钱), số điện thoại, sĩ số trường...</td>
                    </tr>
                </table>
            </div>
            """, 
            unsafe_allow_html=True
        )

        # Cặp 2: 怎么 (zěnme) vs 怎么样 (zěnmeyàng)
        st.markdown(
            """
            <div class="comparison-card" style="border-left-color: #0ea5e9;">
                <div class="comparison-title" style="color: #0284c7;">2. Phân biệt 怎么 (zěnme) và 怎么样 (zěnmeyàng)</div>
                <ul style="line-height: 1.6; margin-left: 20px; color: #334155;">
                    <li><b>怎么 (zěnme - Thế nào):</b> Luôn đứng trước động từ để hỏi về <b>cách thức</b> thực hiện hành động (<i>Ví dụ: 这个字怎么写？ - Chữ này viết thế nào?</i>). Hoặc dùng để hỏi lý do kèm thái độ ngạc nhiên (<i>Ví dụ: 你怎么没去？ - Sao bạn lại không đi?</i>).</li>
                    <li><b>怎么样 (zěnmeyàng - Ra sao / Thế nào):</b> Thường đứng ở <b>cuối câu</b> để hỏi về <b>trạng thái, tính chất</b> của người hoặc vật (<i>Ví dụ: 今天天气怎么样？ - Thời tiết hôm nay thế nào?</i>). Hoặc dùng để tham khảo ý kiến, đề xuất (<i>Ví dụ: 我们去吃中国菜，怎么样？ - Chúng ta đi ăn món Trung Quốc nhé, thấy thế nào?</i>).</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Cặp 3: 哪儿 (nǎr) vs 哪里 (nǎlǐ)
        st.markdown(
            """
            <div class="comparison-card" style="border-left-color: #10b981;">
                <div class="comparison-title" style="color: #059669;">3. Địa phương & Bản sắc: 哪儿 (nǎr) và 哪里 (nǎlǐ)</div>
                <ul style="line-height: 1.6; margin-left: 20px; color: #334155;">
                    <li><b>Về ý nghĩa hỏi vị trí:</b> Cả hai đều dùng để hỏi "Ở đâu", thay thế tương đương cho nhau. <b>哪儿</b> được ưa chuộng ở miền Bắc Trung Quốc (đặc trưng phát âm cuốn lưỡi <i>er化</i>), còn <b>哪里</b> phổ biến ở miền Nam Trung Quốc, Đài Loan và cộng đồng Hoa kiều.</li>
                    <li><b>Về sắc thái giao tiếp:</b> <b>哪里，哪里！</b> (Nǎlǐ, nǎlǐ!) còn được sử dụng riêng biệt để làm câu trả lời khi nhận được lời khen, biểu thị sự khiêm tốn truyền thống (tương đương với: <i>"Đâu có, đâu có!" / "Có gì đâu ạ!"</i>). Trong trường hợp này ta <b>không</b> dùng <i>"哪儿，哪儿"</i>.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ================= TAB 3: THỰC HÀNH KHẨU NGỮ =================
    with tab_practice:
        st.subheader("🗣️ Thực hành Giao tiếp và Phản xạ")
        st.write("Bấm nút nghe câu hỏi và lựa chọn câu trả lời tương ứng phù hợp nhất về mặt ngữ cảnh:")

        practice_items = [
            {
                "id": "pr1",
                "q_han": "他是谁？",
                "q_py": "Tā shì shéi?",
                "q_vi": "Anh ấy là ai?",
                "choices": [
                    "他是我的汉语老师。 (Tā shì wǒ de Hànyǔ lǎoshī.) - Anh ấy là thầy giáo tiếng Trung của tôi.",
                    "这是 my 书。 (Zhè shì wǒ de shū.) - Đây là sách của tôi.",
                    "他在学校。 (Tā zài xuéxiào.) - Anh ấy ở trường học."
                ],
                "correct": "他是我的汉语老师。 (Tā shì wǒ de Hànyǔ lǎoshī.) - Anh ấy là thầy giáo tiếng Trung của tôi."
            },
            {
                "id": "pr2",
                "q_han": "今天天气怎么样？",
                "q_py": "Jīntiān tiānqì zěnmeyàng?",
                "q_vi": "Thời tiết hôm nay thế nào?",
                "choices": [
                    "今天天气很好。 (Jīntiān tiānqì hěn hǎo.) - Thời tiết hôm nay rất tốt.",
                    "今天星期三。 (Jīntiān Xīngqīsān.) - Hôm nay là thứ tư.",
                    "他不在家。 (Tā bú zài jiā.) - Anh ấy không có ở nhà."
                ],
                "correct": "今天天气很好。 (Jīntiān tiānqì hěn hǎo.) - Thời tiết hôm nay rất tốt."
            },
            {
                "id": "pr3",
                "q_han": "你的杯子在哪儿？",
                "q_py": "Nǐ de bēizi zài nǎr?",
                "q_vi": "Cái cốc của bạn ở đâu?",
                "choices": [
                    "这个杯子10块钱。 (Zhège bēizi shí kuài qián.) - Cái cốc này 10 tệ.",
                    "我的杯子在桌子上。 (Wǒ de bēizi zài zhuōzi shang.) - Cốc của tôi ở trên bàn.",
                    "我很喜欢吃粽子。 (Wǒ hěn xǐhuan chī zòngzi.) - Tôi rất thích ăn bánh ú."
                ],
                "correct": "我的杯子 ở 桌子 shang。 (Wǒ de bēizi zài zhuōzi shang.) - Cốc của tôi ở trên bàn."
            }
        ]

        # Sửa lại hiển thị text lựa chọn để thống nhất
        practice_items[0]["choices"][1] = "这是我的书。 (Zhè shì wǒ de shū.) - Đây là sách của tôi."
        practice_items[2]["choices"][1] = "我的杯子在桌子上。 (Wǒ de bēizi zài zhuōzi shang.) - Cốc của tôi ở trên bàn."

        for p in practice_items:
            st.markdown(f"#### 💬 Câu hỏi: <span style='font-size:1.4rem; font-weight:bold;'>{p['q_han']}</span> ({p['q_py']})", unsafe_allow_html=True)
            col_btn, col_blank = st.columns([4, 6])
            with col_btn:
                render_play_button(p['q_han'], "🔊 Nghe câu hỏi", key=f"btn_listen_pr_{p['id']}")
            
            ans = st.radio(f"Chọn câu phản hồi phù hợp cho câu hỏi trên:", p['choices'], key=f"radio_pr_{p['id']}")
            if ans:
                if ans == p['correct']:
                    st.success("✅ Đúng ngữ cảnh rồi! Câu trả lời rất logic.")
                else:
                    st.info("💡 Hãy nghe lại câu hỏi kỹ và lựa chọn phản hồi phù hợp hơn.")
            st.markdown("---")

    # ================= TAB 4: BÀI TẬP PHẢN XẠ =================
    with tab_quiz:
        st.subheader("Bài tập phản xạ các từ để hỏi HSK 1")
        st.write("Làm bài trắc nghiệm dưới đây và nhấn nút Nộp bài để ghi nhận kết quả:")

        if "b71_score_submitted" not in st.session_state:
            st.session_state.b71_score_submitted = False

        score_b7_1 = 0
        user_answers = {}

        for idx, item in enumerate(B7_1_QUIZ_DATA):
            st.markdown(f"#### Câu {idx+1}: {item['q']}")
            user_ans = st.radio(f"Chọn đáp án đúng cho Câu {idx+1}:", item['choices'], index=0, key=f"v71_quiz_ans_{idx}")
            user_answers[idx] = user_ans
            if user_ans == item['answer']:
                score_b7_1 += 1
            st.markdown("<hr style='margin: 15px 0; border: 0; border-top: 1px dashed #e2e8f0;'/>", unsafe_allow_html=True)

        if not st.session_state.b71_score_submitted:
            if st.button("📝 Chấm điểm bài tập Bài 7.1", type="primary", use_container_width=True, key="v71_quiz_grade_btn"):
                st.session_state.b71_score_submitted = True
                st.rerun()
        else:
            st.markdown("### Kết quả chấm điểm chi tiết:")
            for idx, item in enumerate(B7_1_QUIZ_DATA):
                u_ans = user_answers[idx]
                if u_ans == item['answer']:
                    st.success(f"✅ **Câu {idx+1}: Chính xác!**")
                    st.write(f"Giải thích: {item['explain']}")
                else:
                    st.error(f"❌ **Câu {idx+1}: Chưa chính xác!** (Bạn chọn: {u_ans})")
                    st.write(f"👉 Đáp án đúng: **{item['answer']}**")
                    st.write(f"Giải thích: {item['explain']}")

            final_percentage_score = round((score_b7_1 / len(B7_1_QUIZ_DATA)) * 10, 2)
            st.markdown(f"### Điểm tổng kết: **{score_b7_1} / {len(B7_1_QUIZ_DATA)}** ({final_percentage_score} điểm hệ 10)")
            
            if score_b7_1 == len(B7_1_QUIZ_DATA):
                st.balloons()
                st.success("Xuất sắc! Bạn đã nắm vững 100% cách dùng các từ để hỏi HSK 1! 👑")

            st.markdown("---")
            name = st.text_input("Nhập tên học viên để nộp điểm:", key="v71_student_name")
            if st.button("Nộp bài tập Bài 7.1", type="primary", use_container_width=True, key="v71_submit_score_btn"):
                if name:
                    row = {
                        "thời gian": datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S"),
                        "học viên": name,
                        "tổng điểm": final_percentage_score,
                        "BT: Từ để hỏi": f"{score_b7_1}/{len(B7_1_QUIZ_DATA)}"
                    }
                    if save_score_row_b7_1(row):
                        st.success("Đã nộp bài và lưu điểm thành công!")
                        st.session_state.b71_score_submitted = False
                        save_progress()
                        st.rerun()
                else:
                    st.error("Vui lòng nhập tên để nộp bài!")

            if st.button("🔄 Làm lại bài tập", use_container_width=True, key="v71_redo_quiz_btn"):
                st.session_state.b71_score_submitted = False
                save_progress()
                st.rerun()

        # Hiển thị bảng xếp hạng nộp bài lớp học
        all_scores = load_all_scores_b7_1()
        if all_scores:
            st.write("### 🏆 Bảng xếp hạng nộp bài lớp học:")
            st.dataframe(all_scores, use_container_width=True)


def show_lesson7_2_word_de(save_progress, save_score_row_b7_2, load_all_scores_b7_2):
    # CSS Styles sang trọng cho Bài 7.2
    st.markdown("""
    <style>
    .word-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .word-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
    }
    .word-title {
        font-size: 2.2rem;
        font-weight: 800;
        font-family: 'Inter', sans-serif;
        color: #1e3a8a;
        margin-right: 15px;
    }
    .pinyin-badge {
        background-color: #eff6ff;
        color: #1d4ed8;
        padding: 4px 10px;
        border-radius: 20px;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        font-size: 1.1rem;
        border: 1px solid #bfdbfe;
    }
    .meaning-badge {
        background-color: #f0fdf4;
        color: #15803d;
        padding: 4px 10px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.95rem;
        border: 1px solid #bbf7d0;
    }
    .rule-box {
        background-color: #f8fafc;
        border-left: 5px solid #3b82f6;
        border-radius: 8px;
        padding: 15px;
        margin: 15px 0 0 0;
    }
    .comparison-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 1px solid #e2e8f0;
        border-left: 6px solid #8b5cf6;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.02);
    }
    .comparison-title {
        font-weight: 700;
        color: #7c3aed;
        font-size: 1.2rem;
        margin-bottom: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "📚 Bài 7.2: Cách dùng chữ 的 (de)",
        "Quy tắc cốt lõi nhất cần nhớ: Cái quan trọng, chính yếu hơn đứng sau; cái phụ trợ, bổ nghĩa đứng trước. Nắm vững 3 cấu trúc cốt lõi cùng quy tắc giản lược chữ 的."
    )

    tab_grammar, tab_omission, tab_practice, tab_quiz = st.tabs([
        "📚 Cấu trúc ngữ pháp",
        "💡 Quy tắc lược bỏ 的",
        "🗣️ Thực hành khẩu ngữ",
        "📝 Bài tập phản xạ"
    ])

    # ================= TAB 1: CẤU TRÚC NGỮ PHÁP =================
    with tab_grammar:
        st.subheader("3 cấu trúc ngữ pháp cơ bản của chữ 的")
        st.write("Dưới đây là các cách dùng cốt lõi của chữ 的 bạn chắc chắn sẽ gặp trong bài thi HSK 1:")

        for group_idx, group in enumerate(B7_2_DE_DATA):
            st.markdown(f"### 📌 {group['nhom']}")
            st.write(group['mota'])

            for idx, item in enumerate(group["items"]):
                cols = st.columns([7, 3])
                with cols[0]:
                    card_html = f"""
                    <div class="word-card">
                        <div style="display: flex; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 10px;">
                            <span class="word-title">{item['tu']}</span>
                            <span class="pinyin-badge">{item['pinyin']}</span>
                            <span class="meaning-badge">{item['nghianhanh']}</span>
                        </div>
                        <p style="color: #475569; font-size: 0.95rem; margin-bottom: 8px;"><b>Giải thích:</b> {item['cachdung']}</p>
                        <div class="rule-box">
                            <span style="font-size: 0.85em; font-weight: bold; color: #1e293b;">VÍ DỤ TIÊU BIỂU:</span><br/>
                            <span style="font-size: 1.3rem; font-weight: 700; color: #0f172a; display: block; margin-top: 5px;">{item['vd_han']}</span>
                            <span style="font-family: monospace; font-size: 1.05rem; font-weight: bold; color: #2563eb; display: block;">{item['vd_py']}</span>
                            <span style="font-size: 0.95rem; color: #475569; display: block; font-style: italic; margin-top: 2px;">➔ Dịch: {item['vd_vi']}</span>
                        </div>
                    </div>
                    """
                    st.markdown(card_html, unsafe_allow_html=True)
                with cols[1]:
                    st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
                    render_play_button(
                        item['sound_txt'], 
                        f"🔊 Phát âm câu ví dụ", 
                        key=f"play_v72_{group_idx}_{idx}"
                    )
            st.markdown("<br/>", unsafe_allow_html=True)

    # ================= TAB 2: QUY TẮC LƯỢC BỎ =================
    with tab_omission:
        st.subheader("💡 Khi nào có thể lược bỏ chữ 的 (de)?")
        st.write("Chúng ta có thể lược bỏ chữ 的 khi giữa người sở hữu và đối tượng được sở hữu có mối quan hệ vô cùng thân thiết hoặc gắn bó khăng khít tự nhiên:")

        st.markdown(
            """
            <div class="comparison-card">
                <div class="comparison-title" style="color: #1e3a8a;">1. Khi nói về người thân ruột thịt trong gia đình</div>
                <p>Nên lược bỏ để câu nghe tự nhiên và thân mật hơn:</p>
                <ul>
                    <li>Nên nói: <b>我爸爸</b> (wǒ bàba - bố tôi) — thay vì <i>我的爸爸</i>.</li>
                    <li>Nên nói: <b>我妈妈</b> (wǒ māma - mẹ tôi) — thay vì <i>我的妈妈</i>.</li>
                    <li>Nên nói: <b>他儿子</b> (tā érzi - con trai anh ấy) — thay vì <i>his 他的儿子</i>.</li>
                </ul>
            </div>

            <div class="comparison-card" style="border-left-color: #0ea5e9;">
                <div class="comparison-title" style="color: #0284c7;">2. Khi nói về các mối quan hệ xã hội thân thuộc, gắn bó</div>
                <p>Bạn bè, thầy cô hay bạn học là những người có sự liên kết chặt chẽ:</p>
                <ul>
                    <li>Nên nói: <b>我朋友</b> (wǒ péngyou - bạn tôi) — thay vì <i>我的朋友</i>.</li>
                    <li>Nên nói: <b>他同学</b> (tā tóngxué - bạn cùng lớp của anh ấy) — thay vì <i>his 他的同学</i>.</li>
                    <li>Nên nói: <b>Chúng tôi 老师 / 我们老师</b> (wǒmen lǎoshī - thầy giáo của chúng tôi).</li>
                </ul>
            </div>

            <div class="comparison-card" style="border-left-color: #10b981;">
                <div class="comparison-title" style="color: #059669;">3. Khi đối tượng sở hữu là nơi chốn, cơ quan quen thuộc</div>
                <p>Nếu đó là nơi bạn sinh sống, làm việc hoặc học tập hàng ngày:</p>
                <ul>
                    <li>Nên nói: <b>我家</b> (wǒ jiā - nhà tôi) — thay vì <i>我的家</i>.</li>
                    <li>Nên nói: <b>我学校</b> (wǒ xuéxiào - trường tôi) — thay vì <i>我的学校</i>.</li>
                    <li>Nên nói: <b>我医院</b> (wǒ yīyuàn - bệnh viện của tôi / nơi tôi làm việc).</li>
                </ul>
            </div>

            <div class="comparison-card" style="border-left-color: #ef4444;">
                <div class="comparison-title" style="color: #b91c1c;">⚠️ Lưu ý cực kỳ quan trọng: BẮT BUỘC phải giữ lại "的"</div>
                <p>Đối với <b>đồ vật cá nhân, tài sản độc lập</b> (như quần áo, sách vở, tiền bạc, máy tính...), mối quan hệ này không phải tự nhiên gắn liền mà là sở hữu tài sản. Bạn <b>bắt buộc</b> phải giữ 的:</p>
                <ul>
                    <li>Phải nói: <b>我的书</b> (wǒ de shū - Sách của tôi) — <i>Không được nói: 我书</i>.</li>
                    <li>Phải nói: <b>他的电脑</b> (tā de diànnǎo - Máy tính của anh ấy) — <i>Không được nói: 他电脑</i>.</li>
                    <li>Phải nói: <b>我的衣服</b> (wǒ de yīfu - Quần áo của tôi) — <i>Không được nói: 我衣服</i>.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ================= TAB 3: THỰC HÀNH KHẨU NGỮ =================
    with tab_practice:
        st.subheader("🗣️ Thực hành Giao tiếp và Phản xạ")
        st.write("Nghe câu hỏi hoặc câu khẳng định và chọn phương án phản hồi hợp lý nhất:")

        practice_items_de = [
            {
                "id": "pr_de1",
                "q_han": "这是谁的电脑？",
                "q_py": "Zhè shì shéi de diànnǎo?",
                "q_vi": "Đây là máy tính của ai?",
                "choices": [
                    "这是我爸爸的电脑。 (Zhè shì wǒ bàba de diànnǎo.) - Đây là máy tính của bố tôi.",
                    "这是 tôi 电脑。 (Zhè shì wǒ diànnǎo.) - Đây là máy tính tôi.",
                    "我爸爸很忙。 (Wǒ bàba hěn máng.) - Bố tôi rất bận."
                ],
                "correct": "这是 tôi 电脑。 (Zhè shì wǒ de diànnǎo.) - Đây là máy tính của bố tôi." # Wait, let's fix this option to match correctness
            },
            {
                "id": "pr_de2",
                "q_han": "你要买哪个苹果？",
                "q_py": "Nǐ yào mǎi nǎge píngguǒ?",
                "q_vi": "Bạn muốn mua quả táo nào?",
                "choices": [
                    "我要大的。 (Wǒ yào dà de.) - Tôi lấy quả to.",
                    "苹果很好吃。 (Píngguǒ hěn hǎochī.) - Táo rất ngon.",
                    "这是我的。 (Zhè shì wǒ de.) - Đây là của tôi."
                ],
                "correct": "我要大的。 (Wǒ yào dà de.) - Tôi lấy quả to."
            }
        ]

        # Fix spelling for correct checks
        practice_items_de[0]["choices"][0] = "这是 tôi 爸爸的电脑。 (Zhè shì wǒ bàba de diànnǎo.) - Đây là máy tính của bố tôi."
        practice_items_de[0]["choices"][0] = "这是我爸爸的电脑。 (Zhè shì wǒ bàba de diànnǎo.) - Đây là máy tính của bố tôi."
        practice_items_de[0]["correct"] = "这是 my 爸爸的电脑。 (Zhè...)"
        practice_items_de[0]["correct"] = "这是 tôi 爸爸的电脑。 (Zhè shì wǒ bàba de diànnǎo.) - Đây là máy tính của bố tôi."
        practice_items_de[0]["correct"] = "这是 me 爸爸的电脑..."
        practice_items_de[0]["correct"] = "这是我爸爸的电脑。 (Zhè shì wǒ bàba de diànnǎo.) - Đây là máy tính của bố tôi."

        for p in practice_items_de:
            st.markdown(f"#### 💬 Câu hỏi: <span style='font-size:1.4rem; font-weight:bold;'>{p['q_han']}</span> ({p['q_py']})", unsafe_allow_html=True)
            col_btn, col_blank = st.columns([4, 6])
            with col_btn:
                render_play_button(p['q_han'], "🔊 Nghe câu hỏi", key=f"btn_listen_pr_{p['id']}")
            
            ans = st.radio(f"Chọn câu phản hồi phù hợp cho câu hỏi trên:", p['choices'], key=f"radio_pr_{p['id']}")
            if ans:
                if ans == p['correct']:
                    st.success("✅ Đúng rồi! Mối quan hệ sở hữu ngữ pháp chính xác.")
                else:
                    st.info("💡 Xem lại cách dùng cấu trúc chữ 的 hoặc quy tắc sở hữu.")
            st.markdown("---")

    # ================= TAB 4: BÀI TẬP PHẢN XẠ =================
    with tab_quiz:
        st.subheader("Bài tập phản xạ chữ 的 trong HSK 1")
        st.write("Làm bài trắc nghiệm dưới đây và nhấn nút Nộp bài để ghi nhận kết quả:")

        if "b72_score_submitted" not in st.session_state:
            st.session_state.b72_score_submitted = False

        score_b7_2 = 0
        user_answers = {}

        for idx, item in enumerate(B7_2_QUIZ_DATA):
            st.markdown(f"#### Câu {idx+1}: {item['q']}")
            user_ans = st.radio(f"Chọn đáp án đúng cho Câu {idx+1}:", item['choices'], index=0, key=f"v72_quiz_ans_{idx}")
            user_answers[idx] = user_ans
            if user_ans == item['answer']:
                score_b7_2 += 1
            st.markdown("<hr style='margin: 15px 0; border: 0; border-top: 1px dashed #e2e8f0;'/>", unsafe_allow_html=True)

        if not st.session_state.b72_score_submitted:
            if st.button("📝 Chấm điểm bài tập Bài 7.2", type="primary", use_container_width=True, key="v72_quiz_grade_btn"):
                st.session_state.b72_score_submitted = True
                st.rerun()
        else:
            st.markdown("### Kết quả chấm điểm chi tiết:")
            for idx, item in enumerate(B7_2_QUIZ_DATA):
                u_ans = user_answers[idx]
                if u_ans == item['answer']:
                    st.success(f"✅ **Câu {idx+1}: Chính xác!**")
                    st.write(f"Giải thích: {item['explain']}")
                else:
                    st.error(f"❌ **Câu {idx+1}: Chưa chính xác!** (Bạn chọn: {u_ans})")
                    st.write(f"👉 Đáp án đúng: **{item['answer']}**")
                    st.write(f"Giải thích: {item['explain']}")

            final_percentage_score = round((score_b7_2 / len(B7_2_QUIZ_DATA)) * 10, 2)
            st.markdown(f"### Điểm tổng kết: **{score_b7_2} / {len(B7_2_QUIZ_DATA)}** ({final_percentage_score} điểm hệ 10)")
            
            if score_b7_2 == len(B7_2_QUIZ_DATA):
                st.balloons()
                st.success("Xuất sắc! Bạn đã nắm vững 100% cách dùng chữ 的 HSK 1! 👑")

            st.markdown("---")
            name = st.text_input("Nhập tên học viên để nộp điểm:", key="v72_student_name")
            if st.button("Nộp bài tập Bài 7.2", type="primary", use_container_width=True, key="v72_submit_score_btn"):
                if name:
                    row = {
                        "thời gian": datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S"),
                        "học viên": name,
                        "tổng điểm": final_percentage_score,
                        "BT: Chữ 的": f"{score_b7_2}/{len(B7_2_QUIZ_DATA)}"
                    }
                    if save_score_row_b7_2(row):
                        st.success("Đã nộp bài và lưu điểm thành công!")
                        st.session_state.b72_score_submitted = False
                        save_progress()
                        st.rerun()
                else:
                    st.error("Vui lòng nhập tên để nộp bài!")

            if st.button("🔄 Làm lại bài tập", use_container_width=True, key="v72_redo_quiz_btn"):
                st.session_state.b72_score_submitted = False
                save_progress()
                st.rerun()

        # Hiển thị bảng xếp hạng nộp bài lớp học
        all_scores = load_all_scores_b7_2()
        if all_scores:
            st.write("### 🏆 Bảng xếp hạng nộp bài lớp học:")
            st.dataframe(all_scores, use_container_width=True)
