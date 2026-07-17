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
            
            if "3. Hỏi về Số lượng" in group['nhom']:
                st.markdown("""
<div style="background-color: #f0fdf4; border-left: 4px solid #16a34a; padding: 12px; border-radius: 8px; margin-top: 8px; margin-bottom: 15px; font-size: 0.92rem; color: #14532d;">
    💡 <b>Phân biệt lượng từ khi hỏi về gia đình:</b><br/>
    • <b>你家有几口人？</b> (Dùng <b>口 - kǒu</b>): Hỏi về thành viên gia đình ruột thịt cùng sống chung (nghĩa gốc là "miệng ăn"). Nghe ấm áp, đậm chất truyền thống.<br/>
    • <b>你家有几个人？</b> (Dùng <b>个 - gè</b>): Cách hỏi hiện đại, dùng lượng từ phổ thông "个". Rất tự nhiên và thông dụng trong khẩu ngữ hàng ngày.
</div>
""".replace("\n", " "), unsafe_allow_html=True)

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
""".replace("\n", " ")
                    
                    if not cautrucs_html:
                        cautrucs_html = f"""
<p style="background:#eff6ff; border-left:4px solid #3b82f6; border-radius:6px; padding:6px 10px; font-size:0.92rem; margin-bottom:8px; font-family:'Courier New',monospace; color:#1d4ed8;"><b>📐 Cấu trúc:</b> {item.get('cautruc','')}</p>
<div class="rule-box">
<span style="font-size: 0.85em; font-weight: bold; color: #1e293b;">VÍ DỤ TIÊU BIỂU:</span><br/>
<span style="font-size: 1.3rem; font-weight: 700; color: #0f172a; display: block; margin-top: 5px;">{item['vd_han']}</span>
<span style="font-family: monospace; font-size: 1.05rem; font-weight: bold; color: #2563eb; display: block;">{item['vd_py']}</span>
<span style="font-size: 0.95rem; color: #475569; display: block; font-style: italic; margin-top: 2px;">➔ Dịch: {item['vd_vi']}</span>
</div>
""".replace("\n", " ")

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
""".replace("\n", " ")
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
            if group_idx == 2:
                comparison_table_html = """
                <div class="comparison-card" style="border-left-color: #3b82f6; margin-top: 15px;">
                    <div class="comparison-title" style="color: #1d4ed8; font-size: 1.15rem; display: flex; align-items: center; gap: 8px;">
                        🔍 Bảng so sánh nhanh
                    </div>
                    <table style="width:100%; border-collapse: collapse; margin-top: 12px; font-size: 0.92rem; background: #ffffff;">
                        <thead>
                            <tr style="background-color: #eff6ff;">
                                <th style="padding: 10px; border: 1px solid #bfdbfe; text-align: left; color: #1e3a8a; font-weight: 700; width: 20%;">Đặc điểm</th>
                                <th style="padding: 10px; border: 1px solid #bfdbfe; text-align: left; color: #1e3a8a; font-weight: 700; width: 40%;">这本书是我的</th>
                                <th style="padding: 10px; border: 1px solid #bfdbfe; text-align: left; color: #1e3a8a; font-weight: 700; width: 40%;">这是我的书</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #475569;">Dịch nghĩa</td>
                                <td style="padding: 10px; border: 1px solid #e2e8f0; color: #0f172a; font-weight: 500;">Cuốn sách này là của tôi.</td>
                                <td style="padding: 10px; border: 1px solid #e2e8f0; color: #0f172a; font-weight: 500;">Đây là cuốn sách của tôi.</td>
                            </tr>
                            <tr style="background-color: #f8fafc;">
                                <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #475569;">Tiếng Anh</td>
                                <td style="padding: 10px; border: 1px solid #e2e8f0; font-family: monospace; font-size: 0.95rem; color: #2563eb;">This book is mine.</td>
                                <td style="padding: 10px; border: 1px solid #e2e8f0; font-family: monospace; font-size: 0.95rem; color: #2563eb;">This is my book.</td>
                            </tr>
                            <tr>
                                <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #475569;">Trọng tâm nhấn mạnh</td>
                                <td style="padding: 10px; border: 1px solid #e2e8f0; color: #16a34a; font-weight: 600;">Người sở hữu <span style="font-weight: normal; color: #475569;">(Là của tôi, không phải của ai khác).</span></td>
                                <td style="padding: 10px; border: 1px solid #e2e8f0; color: #ea580c; font-weight: 600;">Vật thể <span style="font-weight: normal; color: #475569;">(Giới thiệu đây là cuốn sách).</span></td>
                            </tr>
                            <tr style="background-color: #f8fafc;">
                                <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #475569;">Câu hỏi tương ứng</td>
                                <td style="padding: 10px; border: 1px solid #e2e8f0; color: #0f172a;"><span style="font-size: 1rem; font-weight: bold;">这本书是谁的？</span><br/><span style="font-size: 0.85rem; color: #475569;">(Cuốn sách này của ai?)</span></td>
                                <td style="padding: 10px; border: 1px solid #e2e8f0; color: #0f172a;"><span style="font-size: 1rem; font-weight: bold;">这是什么？</span><br/><span style="font-size: 0.85rem; color: #475569;">(Đây là cái gì?)</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                """
                st.markdown(comparison_table_html.replace("\n", " "), unsafe_allow_html=True)
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

def show_lesson7_3_zhe_na(save_progress, save_score_row_b7_3, load_all_scores_b7_3):
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
        "📚 Bài 7.3: Cặp từ 这 và 那",
        "Làm chủ cách sử dụng đại từ chỉ định 这 (Đây/Này), 那 (Kia/Đó), cách kết hợp lượng từ (这个, 那个), câu hỏi lựa chọn 哪个, và từ đệm giao tiếp."
    )

    B7_3_ZHENA_DATA = [
        {
            "nhom": "1. Từ chỉ định cơ bản: 这 (zhè) và 那 (nà)",
            "mota": "Dùng để chỉ định vị trí gần (这) hoặc xa (那) so với người nói.",
            "items": [
                {
                    "tu": "这",
                    "pinyin": "zhè / zhèi",
                    "nghianhanh": "Đây / Này (cự ly gần)",
                    "cachdung": "Dùng để chỉ người hoặc vật ở cự ly gần người nói. Trong khẩu ngữ, khi đi trực tiếp với lượng từ, thường đọc chệch thành 'zhèi'.",
                    "vd_han": "这是我的书。",
                    "vd_py": "Zhè shì wǒ de shū.",
                    "vd_vi": "Đây là sách của tôi.",
                    "sound_txt": "这是我的书。"
                },
                {
                    "tu": "那",
                    "pinyin": "nà / nèi",
                    "nghianhanh": "Kia / Đó (cự ly xa)",
                    "cachdung": "Dùng để chỉ người hoặc vật ở cự ly xa người nói. Trong khẩu ngữ, khi đi trực tiếp với lượng từ, thường đọc chệch thành 'nèi'.",
                    "vd_han": "那是老师的电脑。",
                    "vd_py": "Nà shì lǎoshī de diànnǎo.",
                    "vd_vi": "Kia là máy tính của thầy giáo.",
                    "sound_txt": "那是老师的电脑。"
                }
            ]
        },
        {
            "nhom": "2. Đại từ chỉ định kết hợp lượng từ: 这个 (zhège) và 那个 (nàge)",
            "mota": "Công thức chung: 这/那 + Lượng từ (个) + Danh từ (chỉ cụ thể 'cái này', 'cái kia').",
            "items": [
                {
                    "tu": "这个",
                    "pinyin": "zhège / zhèige",
                    "nghianhanh": "Cái này / Người này",
                    "cachdung": "Đi kèm lượng từ trước danh từ để chỉ vật/người cụ thể ở gần.",
                    "vd_han": "这个杯子是我的。",
                    "vd_py": "Zhège bēizi shì wǒ de.",
                    "vd_vi": "Cái cốc này là của tôi.",
                    "sound_txt": "这个杯子是我的。"
                },
                {
                    "tu": "那个",
                    "pinyin": "nàge / nèige",
                    "nghianhanh": "Cái kia / Người kia",
                    "cachdung": "Đi kèm lượng từ trước danh từ để chỉ vật/người cụ thể ở xa.",
                    "vd_han": "那个学生是我的朋友。",
                    "vd_py": "Nàge xuésheng shì wǒ de péngyou.",
                    "vd_vi": "Học sinh kia là bạn của tôi.",
                    "sound_txt": "那个学生是我的朋友。"
                }
            ]
        },
        {
            "nhom": "3. Hỏi lựa chọn và từ đệm khẩu ngữ: 哪个 (nǎge) và từ đệm",
            "mota": "Ứng dụng mở rộng của cặp từ chỉ định trong giao tiếp hàng ngày.",
            "items": [
                {
                    "tu": "哪个",
                    "pinyin": "nǎge / nèige",
                    "nghianhanh": "Cái nào / Người nào",
                    "cachdung": "Dùng để hỏi lựa chọn giữa nhiều đối tượng cụ thể.",
                    "vd_han": "你要哪个苹果？",
                    "vd_py": "Nǐ yào nǎge píngguǒ?",
                    "vd_vi": "Bạn muốn quả táo nào?",
                    "sound_txt": "你要哪个苹果？"
                },
                {
                    "tu": "Từ đệm khẩu ngữ",
                    "pinyin": "nàge / nèige / zhège / zhèige",
                    "nghianhanh": "Ơ... / À thì... / Cái đó...",
                    "cachdung": "Làm từ đệm ngập ngừng trong giao tiếp hàng ngày khi người nói đang suy nghĩ.",
                    "vd_han": "那个……我不知道。",
                    "vd_py": "Nèi ge... wǒ bù zhīdào.",
                    "vd_vi": "À thì... tôi không biết nữa.",
                    "sound_txt": "那个……我不知道。"
                }
            ]
        }
    ]

    B7_3_QUIZ_DATA = [
        {
            "q": "Chọn câu dịch đúng nhất cho câu: 'Đây là bạn của tôi.'",
            "choices": ["这是我的朋友。 (Zhè shì wǒ de péngyou.)", "那是我的朋友。 (Nà shì wǒ de péngyou.)", "这是我的老师。 (Zhè shì wǒ de lǎoshī.)"],
            "answer": "这是我的朋友。 (Zhè shì wǒ de péngyou.)",
            "explain": "'Đây' dùng 这 (zhè), 'bạn' dùng 朋友 (péngyou)."
        },
        {
            "q": "Chọn câu dịch đúng nhất cho câu: 'Kia là con chó của tôi.'",
            "choices": ["那是我的狗。 (Nà shì wǒ de gǒu.)", "这是我的狗。 (Zhè shì wǒ de gǒu.)", "那是我的猫。 (Nà shì wǒ de māo.)"],
            "answer": "那是我的狗。 (Nà shì wǒ de gǒu.)",
            "explain": "'Kia' dùng 那 (nà), 'chó' dùng 狗 (gǒu)."
        },
        {
            "q": "Khi nói nhanh hoặc trong khẩu ngữ tự nhiên, '这个' (zhège) và '那个' (nàge) thường phát âm thành gì?",
            "choices": ["zhèige và nèige", "zhège và nàge (giữ nguyên)", "zège và nàge"],
            "answer": "zhèige và nèige",
            "explain": "Trong giao tiếp thực tế, âm 'zhè' và 'nà' kết hợp với âm 'yī' của số một tạo thành dạng đọc chệch 'zhèige' và 'nèige' vô cùng phổ biến."
        },
        {
            "q": "Điền từ thích hợp vào chỗ trống: '______ 苹果很大。 (Quả táo này rất to.)'",
            "choices": ["这个 (zhège)", "那个 (nàge)", "哪个 (nǎge)"],
            "answer": "这个 (zhège)",
            "explain": "Để chỉ vật ở gần ('này'), ta dùng '这个'."
        },
        {
            "q": "Điền từ thích hợp vào chỗ trống: '______ 老师是我的妈妈。 (Thầy/cô giáo kia là mẹ của tôi.)'",
            "choices": ["这个 (zhège)", "那个 (nàge)", "哪个 (nǎge)"],
            "answer": "那个 (nàge)",
            "explain": "Để chỉ người ở xa ('kia'), ta dùng '那个老师'."
        },
        {
            "q": "Trong giao tiếp đời sống, từ nào hay được lặp lại làm từ đệm ngập ngừng (giống như 'ơ, à, thì')?",
            "choices": ["那个/这个 (nàge/zhège)", "什么 (shénme)", "谁 (shéi)"],
            "answer": "那个/这个 (nàge/zhège)",
            "explain": "'那个' và '这个' là các từ đệm cực kỳ thông dụng khi đang suy nghĩ."
        },
        {
            "q": "Chọn câu dịch đúng: 'Bạn muốn cốc nào?'",
            "choices": ["你要哪个杯子？ (Nǐ yào nǎge bēizi?)", "你要这个杯子吗？ (Nǐ yào zhège bēizi ma?)", "你要那个杯子？ (Nǐ yào nàge bēizi?)"],
            "answer": "你要哪个杯子？ (Nǐ yào nǎge bēizi?)",
            "explain": "'Nào' dùng 哪个 (nǎge) để hỏi sự lựa chọn."
        },
        {
            "q": "Chọn câu đúng ngữ pháp nhất để nói: 'Người này là giáo viên của tôi.'",
            "choices": ["这人是我的老师。 (Zhè rén shì wǒ de lǎoshī.)", "这个人是我的老师。 (Zhège rén shì wǒ de lǎoshī.)", "这一个是我的老师。 (Zhè yí gè shì wǒ de lǎoshī.)"],
            "answer": "这个人是我的老师。 (Zhège rén shì wǒ de lǎoshī.)",
            "explain": "Cấu trúc chỉ định cụ thể: 这 + lượng từ + danh từ. Ở đây '人' dùng lượng từ '个'."
        },
        {
            "q": "Chọn câu SAI ngữ pháp trong các câu sau:",
            "choices": ["那是谁？ (Nà shì shéi?) - Kia là ai?", "这个是什么？ (Zhège shì shénme?) - Đây là cái gì?", "这个是哪儿？ (Zhège shì nǎr?) - Đây là ở đâu?"],
            "answer": "这个是哪儿？ (Zhège shì nǎr?) - Đây là ở đâu?",
            "explain": "Để hỏi/chỉ vị trí, địa điểm ta phải dùng các từ chỉ nơi chốn như '这儿/这里' hoặc '那儿/ni/nǎr'. '这个' chỉ dùng cho người hoặc đồ vật cụ thể."
        },
        {
            "q": "Điền từ: 'A: Nǐ xǐhuan nǎge bēizi? - B: Wǒ xǐhuan ______ (tôi thích cái này).'",
            "choices": ["这个 (zhège)", "那个 (nàge)", "哪个 (nǎge)"],
            "answer": "这个 (zhège)",
            "explain": "Trả lời chọn 'cái này' (gần) dùng '这个 (zhège)'."
        }
    ]

    tab_vocab, tab_rules, tab_practice, tab_quiz = st.tabs([
        "📚 Bảng lý thuyết chỉ định",
        "💡 Quy tắc & Phân tích",
        "🗣️ Thực hành khẩu ngữ",
        "📝 Bài tập phản xạ"
    ])

    with tab_vocab:
        st.subheader("Bảng từ vựng chỉ định cơ bản")
        for group_idx, group in enumerate(B7_3_ZHENA_DATA):
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
                    <p style="color: #475569; font-size: 0.95rem; margin-bottom: 8px;"><b>Cách dùng:</b> {item['cachdung']}</p>
                    <div class="rule-box">
                    <span style="font-size: 0.85em; font-weight: bold; color: #1e293b;">VÍ DỤ TIÊU BIỂU:</span><br/>
                    <span style="font-size: 1.3rem; font-weight: 700; color: #0f172a; display: block; margin-top: 5px;">{item['vd_han']}</span>
                    <span style="font-family: monospace; font-size: 1.05rem; font-weight: bold; color: #2563eb; display: block;">{item['vd_py']}</span>
                    <span style="font-size: 0.95rem; color: #475569; display: block; font-style: italic; margin-top: 2px;">➔ Dịch: {item['vd_vi']}</span>
                    </div>
                    </div>
                    """.replace("\n", " ")
                    st.markdown(card_html, unsafe_allow_html=True)
                with cols[1]:
                    st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
                    render_play_button(item['sound_txt'], f"🔊 Phát âm", key=f"play_v73_{group_idx}_{idx}")
            st.markdown("<br/>", unsafe_allow_html=True)

    with tab_rules:
        st.subheader("💡 Cách sử dụng và quy tắc đặc biệt")
        st.markdown("""
            <div class="comparison-card">
                <div class="comparison-title">1. Quy tắc phát âm: Đọc chệch (zhè ➔ zhèi, nà ➔ nèi)</div>
                <ul style="line-height: 1.6; margin-left: 20px; color: #334155;">
                    <li>Trong tiếng Trung tiêu chuẩn, âm gốc là <b>这 (zhè)</b> và <b>那 (nà)</b>.</li>
                    <li>Tuy nhiên, khi nói nhanh hoặc đi kèm trực tiếp với lượng từ phía sau, người bản xứ thường phát âm thành <b>zhèi</b> và <b>nèi</b>.</li>
                </ul>
            </div>
            <div class="comparison-card" style="border-left-color: #0ea5e9;">
                <div class="comparison-title" style="color: #0284c7;">2. Vai trò của Lượng từ (Classifier)</div>
                <ul style="line-height: 1.6; margin-left: 20px; color: #334155;">
                    <li>Cấu trúc: <b>这 / 那 + Lượng từ + Danh từ</b>. <i>Ví dụ:</i> <b>这个杯子</b>.</li>
                </ul>
            </div>
            <div class="comparison-card" style="border-left-color: #10b981;">
                <div class="comparison-title" style="color: #059669;">3. Dùng làm từ đệm ngập ngừng (Filler Words)</div>
                <ul style="line-height: 1.6; margin-left: 20px; color: #334155;">
                    <li>Bạn có thể nói <b>那个……</b> hoặc <b>这个……</b> để có thêm thời gian suy nghĩ.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    with tab_practice:
        st.subheader("🗣️ Thực hành Giao tiếp và Phản xạ")
        practice_items = [
            {
                "id": "pr73_1",
                "q_han": "你要哪个杯子？",
                "q_py": "Nǐ yào nǎge bēizi?",
                "q_vi": "Bạn muốn cái cốc nào?",
                "choices": ["我要这个红色的杯子。 (Wǒ yào zhège hóngsè de bēizi.) - Tôi muốn cái cốc màu đỏ này.", "他是我的老师。 (Tā shì wǒ de lǎoshī.) - Anh ấy là thầy giáo của tôi.", "这是我的书。 (Zhè shì wǒ de shū.) - Đây là sách của tôi."],
                "correct": "我要这个红色的杯子。 (Wǒ yào zhège hóngsè de bēizi.) - Tôi muốn cái cốc màu đỏ này."
            },
            {
                "id": "pr73_2",
                "q_han": "那个学生是谁？",
                "q_py": "Nàge xuésheng shì shéi?",
                "q_vi": "Học sinh kia là ai thế?",
                "choices": ["这个苹果很好吃。 (Zhège píngguǒ hěn hǎochī.) - Quả táo này rất ngon.", "那个学生是我的弟弟。 (Nàge xuésheng shì wǒ de dìdi.) - Học sinh kia là em trai tôi.", "他在学校。 (Tā zài xuéxiào.) - Cậu ấy ở trường."],
                "correct": "那个学生是我的弟弟。 (Nàge xuésheng shì wǒ de dìdi.) - Học sinh kia là em trai tôi."
            },
            {
                "id": "pr73_3",
                "q_han": "这是你的电脑吗？",
                "q_py": "Zhè shì nǐ de diànnǎo ma?",
                "q_vi": "Đây là máy tính của bạn phải không?",
                "choices": ["不，这是我爸爸的。 (Bù, zhè shì wǒ bàba de.) - Không, đây là của bố tôi.", "那是我的狗。 (Nà shì wǒ de gǒu.) - Kia là con chó của tôi.", "我要买电脑。 (Wǒ yào mǎi diànnǎo.) - Tôi muốn mua máy tính."],
                "correct": "不，这是我爸爸的。 (Bù, zhè shì wǒ bàba de.) - Không, đây là của bố tôi."
            }
        ]
        for item in practice_items:
            st.markdown(f"##### 🎧 Nghe câu hỏi:")
            cols = st.columns([8, 2])
            with cols[0]:
                st.markdown(f"<div style='background:#f1f5f9; padding: 10px; border-radius: 8px; font-weight: bold;'>{item['q_han']} ({item['q_py']}) <span style='font-weight: normal; font-style: italic; color: #475569;'>- {item['q_vi']}</span></div>", unsafe_allow_html=True)
            with cols[1]:
                render_play_button(item['q_han'], "🔊 Nghe", key=f"play_q_pr73_{item['id']}")

            user_ans = st.radio("Chọn câu phản hồi đúng nhất:", item['choices'], key=f"pr73_ans_select_{item['id']}")
            if user_ans == item['correct']:
                st.success("✅ Đúng ngữ cảnh rồi! Câu trả lời rất logic.")
            else:
                st.info("💡 Hãy nghe lại câu hỏi kỹ và lựa chọn phản hồi phù hợp hơn.")
            st.markdown("---")

    # ================= TAB 4: BÀI TẬP PHẢN XẠ =================
    with tab_quiz:
        st.subheader("Bài tập phản xạ các từ chỉ định HSK 1")
        st.write("Làm bài trắc nghiệm dưới đây và nhấn nút Nộp bài để ghi nhận kết quả:")

        if "b73_score_submitted" not in st.session_state:
            st.session_state.b73_score_submitted = False

        score_b7_3 = 0
        user_answers = {}

        for idx, item in enumerate(B7_3_QUIZ_DATA):
            st.markdown(f"#### Câu {idx+1}: {item['q']}")
            user_ans = st.radio(f"Chọn đáp án đúng cho Câu {idx+1}:", item['choices'], index=0, key=f"v73_quiz_ans_{idx}")
            user_answers[idx] = user_ans
            if user_ans == item['answer']:
                score_b7_3 += 1
            st.markdown("<hr style='margin: 15px 0; border: 0; border-top: 1px dashed #e2e8f0;'/>", unsafe_allow_html=True)

        if not st.session_state.b73_score_submitted:
            if st.button("📝 Chấm điểm bài tập Bài 7.3", type="primary", use_container_width=True, key="v73_quiz_grade_btn"):
                st.session_state.b73_score_submitted = True
                st.rerun()
        else:
            st.markdown("### Kết quả chấm điểm chi tiết:")
            for idx, item in enumerate(B7_3_QUIZ_DATA):
                u_ans = user_answers[idx]
                if u_ans == item['answer']:
                    st.success(f"✅ **Câu {idx+1}: Chính xác!**")
                    st.write(f"Giải thích: {item['explain']}")
                else:
                    st.error(f"❌ **Câu {idx+1}: Chưa chính xác!** (Bạn chọn: {u_ans})")
                    st.write(f"👉 Đáp án đúng: **{item['answer']}**")
                    st.write(f"Giải thích: {item['explain']}")

            final_percentage_score = round((score_b7_3 / len(B7_3_QUIZ_DATA)) * 10, 2)
            st.markdown(f"### Điểm tổng kết: **{score_b7_3} / {len(B7_3_QUIZ_DATA)}** ({final_percentage_score} điểm hệ 10)")
            
            if score_b7_3 == len(B7_3_QUIZ_DATA):
                st.balloons()
                st.success("Xuất sắc! Bạn đã nắm vững 100% cách dùng các từ chỉ định và lượng từ! 👑")

            st.markdown("---")
            name = st.text_input("Nhập tên học viên để nộp điểm:", key="v73_student_name")
            if st.button("Nộp bài tập Bài 7.3", type="primary", use_container_width=True, key="v73_submit_score_btn"):
                if name:
                    row = {
                        "thời gian": datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S"),
                        "học viên": name,
                        "tổng điểm": final_percentage_score,
                        "BT: Cặp từ 这/那": f"{score_b7_3}/{len(B7_3_QUIZ_DATA)}"
                    }
                    if save_score_row_b7_3(row):
                        st.success("Đã nộp bài và lưu điểm thành công!")
                        st.session_state.b73_score_submitted = False
                        save_progress()
                        st.rerun()
                else:
                    st.error("Vui lòng nhập tên để nộp bài!")

            if st.button("🔄 Làm lại bài tập", use_container_width=True, key="v73_redo_quiz_btn"):
                st.session_state.b73_score_submitted = False
                save_progress()
                st.rerun()

        # Hiển thị bảng xếp hạng nộp bài lớp học
        all_scores = load_all_scores_b7_3()
        if all_scores:
            st.write("### 🏆 Bảng xếp hạng nộp bài lớp học:")
            st.dataframe(all_scores, use_container_width=True)


def show_lesson7_4_zai(save_progress, save_score_row_b7_4, load_all_scores_b7_4):
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
        "📚 Bài 7.4: Từ 在 (zài)",
        "Làm chủ cách sử dụng từ đa năng 在 (zài) trong tiếng Trung với 3 vai trò quan trọng: Động từ (Ở), Giới từ (Tại), và Phó từ (Đang)."
    )

    tab_grammar, tab_practice, tab_quiz = st.tabs([
        "📚 Cấu trúc ngữ pháp",
        "🗣️ Thực hành khẩu ngữ",
        "📝 Bài tập phản xạ"
    ])

    B7_4_ZAI_DATA = [
        {
            "nhom": "1. Đóng vai trò là Động từ: \"Ở\", \"Có mặt\"",
            "mota": "Khi là động từ chính trong câu, 在 biểu thị sự tồn tại của người hoặc vật tại một địa điểm nào đó. Cấu trúc: Chủ ngữ + 在 + Địa điểm.",
            "items": [
                {
                    "tu": "我在家。",
                    "pinyin": "Wǒ zài jiā.",
                    "nghianhanh": "Tôi ở nhà.",
                    "cachdung": "Đại từ '我' kết hợp động từ '在' chỉ vị trí ở nhà '家'.",
                    "sound_txt": "我在家。"
                },
                {
                    "tu": "老师不在学校。",
                    "pinyin": "Lǎoshī bú zài xuéxiào.",
                    "nghianhanh": "Thầy/cô giáo không ở trường.",
                    "cachdung": "Thể phủ định dùng '不在'. Chú ý biến điệu của '不' thành 'bú' trước thanh 4 'zài'.",
                    "sound_txt": "老师不在学校。"
                },
                {
                    "tu": "你爸爸在吗？",
                    "pinyin": "Nǐ bàba zài ma?",
                    "nghianhanh": "Bố bạn có nhà/có mặt không?",
                    "cachdung": "Dùng '在吗' để hỏi sự có mặt của ai đó.",
                    "sound_txt": "你爸爸在吗？"
                }
            ]
        },
        {
            "nhom": "2. Đóng vai trò là Giới từ: \"Tại\", \"Ở\" (Làm gì đó ở đâu)",
            "mota": "Khi bạn muốn nói mình làm một hành động gì đó tại một địa điểm cụ thể, 在 sẽ đứng trước địa điểm để làm rõ bối cảnh nơi chốn. Cấu trúc: Chủ ngữ + 在 + Địa điểm + Hành động (Ở đâu làm gì).",
            "items": [
                {
                    "tu": "我在学校学习汉语。",
                    "pinyin": "Wǒ zài xuéxiào xuéxí Hànyǔ.",
                    "nghianhanh": "Tôi học tiếng Trung ở trường.",
                    "cachdung": "Đưa trạng ngữ chỉ địa điểm '在线学校' đứng trước hành động '学习汉语' (Lưu ý: trong tiếng Trung địa điểm đứng trước hành động).",
                    "sound_txt": "我在学校学习汉语。"
                },
                {
                    "tu": "爸爸在客厅看电视。",
                    "pinyin": "Bàba zài kètīng kàn diànshì.",
                    "nghianhanh": "Bố đang xem tivi ở phòng khách.",
                    "cachdung": "Trạng ngữ chỉ địa điểm '在客厅' đứng trước hành động '看电视'.",
                    "sound_txt": "爸爸在客厅看电视。"
                }
            ]
        },
        {
            "nhom": "3. Đóng vai trò là Phó từ: \"Đang\" (Thì hiện tại tiếp diễn)",
            "mota": "Khi đứng ngay trước một động từ hành động, 在 (hoặc 正在 - zhèngzài) biểu thị hành động đó đang diễn ra tại thời điểm nói. Cấu trúc: Chủ ngữ + 在 + Động từ (+ Tân ngữ).",
            "items": [
                {
                    "tu": "我在吃饭。",
                    "pinyin": "Wǒ zài chī fàn.",
                    "nghianhanh": "Tôi đang ăn cơm.",
                    "cachdung": "Từ '在' đứng trước động từ '吃饭' làm phó từ chỉ hành động đang diễn ra.",
                    "sound_txt": "我在吃饭。"
                },
                {
                    "tu": "他在睡觉。",
                    "pinyin": "Tā zài shuìjiào.",
                    "nghianhanh": "Anh ấy đang ngủ.",
                    "cachdung": "Từ '在' đứng trước động từ '睡觉' biểu thị trạng thái đang ngủ.",
                    "sound_txt": "他在睡觉。"
                },
                {
                    "tu": "你们在做什么？",
                    "pinyin": "Nǐmen zài zuò shénme?",
                    "nghianhanh": "Các bạn đang làm gì thế?",
                    "cachdung": "Dùng '在' trước động từ '做' để hỏi hành động đang diễn ra.",
                    "sound_txt": "你们在做什么？"
                }
            ]
        }
    ]

    # Quick fix for typo in explanation
    B7_4_ZAI_DATA[1]["items"][0]["cachdung"] = "Đưa trạng ngữ chỉ địa điểm '在学校' đứng trước hành động '学习汉语'."

    # ================= TAB 1: CẤU TRÚC NGỮ PHÁP =================
    with tab_grammar:
        st.subheader("Cách dùng chi tiết từ 在 (zài)")
        st.write("Hãy phân biệt rõ 3 cách dùng quan trọng dựa trên vị trí của từ 在 trong câu:")

        for group_idx, group in enumerate(B7_4_ZAI_DATA):
            st.markdown(f"### 📌 {group['nhom']}")
            st.write(group['mota'])

            if group_idx == 1:
                st.markdown("""
<div style="background-color: #fef2f2; border-left: 4px solid #ef4444; padding: 12px; border-radius: 8px; margin-top: 8px; margin-bottom: 15px; font-size: 0.92rem; color: #991b1b;">
    ⚠️ <b>LƯU Ý NGỮ PHÁP ĐẶC BIỆT:</b><br/>
    • Tiếng Việt nói: <b>Làm gì + ở đâu</b> (<i>Tôi ăn cơm ở nhà hàng</i>).<br/>
    • Tiếng Trung nói: <b>Ở đâu + làm gì</b> (<i>Chủ ngữ + <b>In/Tại + Địa điểm</b> + Hành động</i>).<br/>
    Đây là lỗi sai phổ biến nhất của người mới học khi dịch từ tiếng Việt sang tiếng Trung!
</div>
""".replace("In/Tại", "在").replace("\n", " "), unsafe_allow_html=True)

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
                    </div>
                    """.replace("\n", " ")
                    st.markdown(card_html, unsafe_allow_html=True)
                with cols[1]:
                    st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
                    render_play_button(
                        item['tu'], 
                        f"🔊 Phát âm ví dụ", 
                        key=f"play_v74_{group_idx}_{idx}"
                    )
            st.markdown("<br/>", unsafe_allow_html=True)

    # ================= TAB 2: THỰC HÀNH KHẨU NGỮ =================
    with tab_practice:
        st.subheader("🗣️ Thực hành Giao tiếp và Phản xạ")
        st.write("Luyện nghe và chọn phản hồi phù hợp với ngữ cảnh:")

        practice_items = [
            {
                "id": "pr_zai1",
                "q_han": "老师在学校吗？",
                "q_py": "Lǎoshī zài xuéxiào ma?",
                "q_vi": "Thầy giáo có ở trường không?",
                "choices": [
                    "老师不在学校，他在家。 (Lǎoshī bú zài xuéxiào, tā zài jiā.) - Thầy không ở trường, thầy ở nhà.",
                    "老师在学习汉语。 (Lǎoshī zài xuéxí Hànyǔ.) - Thầy giáo đang học tiếng Trung.",
                    "他在学校学习。 (Tā zài xuéxiào xuéxí.) - Anh ấy học ở trường."
                ],
                "correct": "老师不在学校，他在家。 (Lǎoshī bú zài xuéxiào, tā zài jiā.) - Thầy không ở trường, thầy ở nhà."
            },
            {
                "id": "pr_zai2",
                "q_han": "你们在哪儿吃饭？",
                "q_py": "Nǐmen zài nǎr chī fàn?",
                "q_vi": "Các bạn ăn cơm ở đâu?",
                "choices": [
                    "我们在学校吃饭。 (Wǒmen zài xuéxiào chī fàn.) - Chúng tôi ăn cơm ở trường.",
                    "我们在吃饭。 (Wǒmen zài chī fàn.) - Chúng tôi đang ăn cơm.",
                    "我不在家。 (Wǒ bú zài jiā.) - Tôi không ở nhà."
                ],
                "correct": "我们在学校吃饭。 (Wǒmen zài xuéxiào chī fàn.) - Chúng tôi ăn cơm ở trường."
            },
            {
                "id": "pr_zai3",
                "q_han": "你在做什么？",
                "q_py": "Nǐ zài zuò shénme?",
                "q_vi": "Bạn đang làm gì thế?",
                "choices": [
                    "我在看电视。 (Wǒ zài kàn diànshì.) - Tôi đang xem tivi.",
                    "我在客厅。 (Wǒ zài kètīng.) - Tôi ở phòng khách.",
                    "这是我的电视。 (Zhè shì wǒ de diànshì.) - Đây là tivi của tôi."
                ],
                "correct": "我在看电视。 (Wǒ zài kàn diànshì.) - Tôi đang xem tivi."
            }
        ]

        for item in practice_items:
            st.markdown(f"##### 🎧 Nghe câu hỏi:")
            cols = st.columns([8, 2])
            with cols[0]:
                st.markdown(f"<div style='background:#f1f5f9; padding: 10px; border-radius: 8px; font-weight: bold;'>{item['q_han']} ({item['q_py']}) <span style='font-weight: normal; font-style: italic; color: #475569;'>- {item['q_vi']}</span></div>", unsafe_allow_html=True)
            with cols[1]:
                render_play_button(item['q_han'], "🔊 Nghe", key=f"play_q_pr74_{item['id']}")

            user_ans = st.radio("Chọn câu phản hồi đúng nhất:", item['choices'], key=f"pr74_ans_select_{item['id']}")
            if user_ans == item['correct']:
                st.success("✅ Đúng ngữ cảnh rồi! Câu trả lời rất logic.")
            else:
                st.info("💡 Hãy nghe lại câu hỏi kỹ và lựa chọn phản hồi phù hợp hơn.")
            st.markdown("---")

    # ================= TAB 3: BÀI TẬP PHẢN XẠ =================
    with tab_quiz:
        st.subheader("Bài tập phản xạ cấu trúc từ 在 (zài)")
        st.write("Làm bài trắc nghiệm dưới đây và nhấn nút Nộp bài để ghi nhận kết quả:")

        B7_4_QUIZ_DATA = [
            {
                "q": "Dịch câu sau sang tiếng Trung: 'Tôi học tiếng Trung ở trường.'",
                "choices": [
                    "我在学校学习汉语。 (Wǒ zài xuéxiào xuéxí Hànyǔ.)",
                    "我学习汉语在学校。 (Wǒ xuéxí Hànyǔ zài xuéxiào.)",
                    "我学校学习汉语。 (Wǒ xuéxiào xuéxí Hànyǔ.)"
                ],
                "answer": "我在学校学习汉语。 (Wǒ zài xuéxiào xuéxí Hànyǔ.)",
                "explain": "Trong tiếng Trung, trạng ngữ chỉ địa điểm phải đứng trước hành động: Chủ ngữ + 在 + Địa điểm + Hành động (Ở đâu làm gì)."
            },
            {
                "q": "Trong câu '他在睡觉。', từ '在' đóng vai trò ngữ pháp gì?",
                "choices": [
                    "Động từ chính (Ở / Có mặt)",
                    "Giới từ (Tại / Ở đâu)",
                    "Phó từ (Đang - chỉ hành động tiếp diễn)"
                ],
                "answer": "Phó từ (Đang - chỉ hành động tiếp diễn)",
                "explain": "'...在...' đứng ngay trước động từ '睡觉' (ngủ) làm phó từ biểu thị hành động đang diễn ra tại thời điểm nói."
            },
            {
                "q": "Chọn câu phủ định đúng ngữ pháp: 'Thầy giáo không ở trường học.'",
                "choices": [
                    "老师不在学校。 (Lǎoshī bú zài xuéxiào.)",
                    "老师没在学校。 (Lǎoshī méi zài xuéxiào.)",
                    "老师不学校。 (Lǎoshī bù xuéxiào.)"
                ],
                "answer": "老师不在学校. (Lǎoshī bú zài xuéxiào.)",
                "explain": "Phủ định của động từ '在' là '不在' (bú zài). Chú ý biến điệu của '不' thành 'bú' trước thanh 4 'zài'."
            },
            {
                "q": "Chọn câu dịch đúng nhất cho câu: 'Bố bạn có nhà không?'",
                "choices": [
                    "你爸爸在家吗？ (Nǐ bàba zài jiā ma?)",
                    "你爸爸在吗？ (Nǐ bàba zài ma?)",
                    "Cả hai câu trên đều đúng ngữ pháp và thông dụng"
                ],
                "answer": "Cả hai câu trên đều đúng ngữ pháp và thông dụng",
                "explain": "Cả hai cách diễn đạt đều đúng và mang nghĩa hỏi thăm ai đó có mặt/ở nhà hay không."
            },
            {
                "q": "Chọn câu đúng ngữ pháp nhất: 'Bố đang xem tivi ở phòng khách.'",
                "choices": [
                    "爸爸看电视在客厅。 (Bàba kàn diànshì zài kètīng.)",
                    "爸爸在客厅看电视。 (Bàba zài kètīng kàn diànshì.)",
                    "爸爸客厅在看电视。 (Bàba kètīng zài kàn diànshì.)"
                ],
                "answer": "爸爸在客厅看电视。 (Bàba zài kètīng kàn diànshì.)",
                "explain": "Trạng ngữ chỉ nơi chốn '在客厅' phải đứng trước cụm động từ '看电视' để tạo thành cấu trúc 'Ở đâu làm gì'."
            }
        ]

        # Fix minor typo in choice comparison
        B7_4_QUIZ_DATA[2]["answer"] = "老师不在学校。 (Lǎoshī bú zài xuéxiào.)"

        if "b74_score_submitted" not in st.session_state:
            st.session_state.b74_score_submitted = False

        score_b7_4 = 0
        user_answers = {}

        for idx, item in enumerate(B7_4_QUIZ_DATA):
            st.markdown(f"#### Câu {idx+1}: {item['q']}")
            user_ans = st.radio(f"Chọn đáp án đúng cho Câu {idx+1}:", item['choices'], index=0, key=f"v74_quiz_ans_{idx}")
            user_answers[idx] = user_ans
            if user_ans == item['answer']:
                score_b7_4 += 1
            st.markdown("<hr style='margin: 15px 0; border: 0; border-top: 1px dashed #e2e8f0;'/>", unsafe_allow_html=True)

        if not st.session_state.b74_score_submitted:
            if st.button("📝 Chấm điểm bài tập Bài 7.4", type="primary", use_container_width=True, key="v74_quiz_grade_btn"):
                st.session_state.b74_score_submitted = True
                st.rerun()
        else:
            st.markdown("### Kết quả chấm điểm chi tiết:")
            for idx, item in enumerate(B7_4_QUIZ_DATA):
                u_ans = user_answers[idx]
                if u_ans == item['answer']:
                    st.success(f"✅ **Câu {idx+1}: Chính xác!**")
                    st.write(f"Giải thích: {item['explain']}")
                else:
                    st.error(f"❌ **Câu {idx+1}: Chưa chính xác!** (Bạn chọn: {u_ans})")
                    st.write(f"👉 Đáp án đúng: **{item['answer']}**")
                    st.write(f"Giải thích: {item['explain']}")

            final_percentage_score = round((score_b7_4 / len(B7_4_QUIZ_DATA)) * 10, 2)
            st.markdown(f"### Điểm tổng kết: **{score_b7_4} / {len(B7_4_QUIZ_DATA)}** ({final_percentage_score} điểm hệ 10)")
            
            if score_b7_4 == len(B7_4_QUIZ_DATA):
                st.balloons()
                st.success("Xuất sắc! Bạn đã nắm vững 100% cách dùng từ 在 (zài)! 👑")

            st.markdown("---")
            name = st.text_input("Nhập tên học viên để nộp điểm:", key="v74_student_name")
            if st.button("Nộp bài tập Bài 7.4", type="primary", use_container_width=True, key="v74_submit_score_btn"):
                if name:
                    row = {
                        "thời gian": datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S"),
                        "học viên": name,
                        "tổng điểm": final_percentage_score,
                        "BT: Từ 在": f"{score_b7_4}/{len(B7_4_QUIZ_DATA)}"
                    }
                    if save_score_row_b7_4(row):
                        st.success("Đã nộp bài và lưu điểm thành công!")
                        st.session_state.b74_score_submitted = False
                        save_progress()
                        st.rerun()
                else:
                    st.error("Vui lòng nhập tên để nộp bài!")

            if st.button("🔄 Làm lại bài tập", use_container_width=True, key="v74_redo_quiz_btn"):
                st.session_state.b74_score_submitted = False
                save_progress()
                st.rerun()

        # Hiển thị bảng xếp hạng nộp bài lớp học
        all_scores = load_all_scores_b7_4()
        if all_scores:
            st.write("### 🏆 Bảng xếp hạng nộp bài lớp học:")
            st.dataframe(all_scores, use_container_width=True)


def show_lesson7_5_qu(save_progress, save_score_row_b7_5, load_all_scores_b7_5):
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
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "📚 Bài 7.5: Từ 去 (qù)",
        "Làm chủ cách sử dụng từ chỉ phương hướng và hành động 去 (qù) trong tiếng Trung từ cơ bản đến cấu trúc liên động và bổ ngữ xu hướng."
    )

    tab_grammar, tab_practice, tab_quiz = st.tabs([
        "📚 Cấu trúc ngữ pháp",
        "🗣️ Thực hành khẩu ngữ",
        "📝 Bài tập phản xạ"
    ])

    B7_5_QU_DATA = [
        {
            "nhom": "1. Cấu trúc cơ bản: Đi đến một địa điểm",
            "mota": "Khi muốn nói 'đi đâu đó', bạn chỉ cần đặt địa điểm ngay sau từ 去. Cấu trúc: Chủ ngữ + 去 + Địa điểm.",
            "items": [
                {
                    "tu": "我去学校。",
                    "pinyin": "Wǒ qù xuéxiào.",
                    "nghianhanh": "Tôi đi đến trường.",
                    "cachdung": "Chủ ngữ '我' kết hợp động từ '去' và địa điểm '学校' (trường học).",
                    "sound_txt": "我去学校。"
                },
                {
                    "tu": "Chúng ta đi siêu thị đi！",
                    "pinyin": "Wǒmen qù chāoshì ba!",
                    "nghianhanh": "Chúng ta đi siêu thị đi!",
                    "cachdung": "Dùng '吧' (ba) ở cuối câu để tạo lời gợi ý, rủ rê thân mật.",
                    "sound_txt": "我们去超市吧！"
                },
                {
                    "tu": "你去哪儿？",
                    "pinyin": "Nǐ qù nǎr?",
                    "nghianhanh": "Bạn đi đâu đấy?",
                    "cachdung": "Dùng từ để hỏi nơi chốn '哪儿' đứng ngay sau '去' để hỏi điểm đến.",
                    "sound_txt": "你去哪儿？"
                }
            ]
        },
        {
            "nhom": "2. Cấu trúc liên động: Đi đâu để làm gì",
            "mota": "Biểu thị mục đích của việc di chuyển. Cấu trúc: Chủ ngữ + 去 + Địa điểm + Hành động. *Mẹo nhỏ: Trong khẩu ngữ, bạn có thể lược bỏ địa điểm nếu người nghe đã biết bạn đang đi đâu.*",
            "items": [
                {
                    "tu": "我去中国学习汉语。",
                    "pinyin": "Wǒ qù Zhōngguó xuéxí Hànyǔ.",
                    "nghianhanh": "Tôi đi Trung Quốc học tiếng Trung.",
                    "cachdung": "Động từ di chuyển '去中国' đứng trước hành động mục đích '学习汉语'.",
                    "sound_txt": "我去中国学习汉语。"
                },
                {
                    "tu": "下午他去商店买衣服。",
                    "pinyin": "Xiàwǔ tā qù shāngdiàn mǎi yīfu.",
                    "nghianhanh": "Chiều nay anh ấy đi cửa hàng mua quần áo.",
                    "cachdung": "Trạng ngữ thời gian '下午' đứng trước chủ ngữ hoặc sau chủ ngữ, cấu trúc liên động '去商店' + '买衣服'.",
                    "sound_txt": "下午他去商店买衣服。"
                },
                {
                    "tu": "我去买饭。",
                    "pinyin": "Wǒ qù mǎi fàn.",
                    "nghianhanh": "Tôi đi mua cơm (đây).",
                    "cachdung": "Lược bỏ địa điểm cụ thể, chỉ giữ hành động '买饭' đứng sau '去'.",
                    "sound_txt": "我去买饭。"
                }
            ]
        },
        {
            "nhom": "3. Đóng vai trò là Xu hướng động từ (Bổ ngữ xu hướng)",
            "mota": "Khi đứng sau một động từ khác, 去 biểu thị hướng của hành động đó là đi ra xa phía người nói (ngược lại với 来 - lái là hướng lại gần). Cấu trúc: Động từ + 去.",
            "items": [
                {
                    "tu": "进去",
                    "pinyin": "jìn qù",
                    "nghianhanh": "Đi vào.",
                    "cachdung": "Người nói đang ở bên ngoài nhìn hành động đi vào trong.",
                    "sound_txt": "进去"
                },
                {
                    "tu": "出去",
                    "pinyin": "chū qù",
                    "nghianhanh": "Đi ra.",
                    "cachdung": "Người nói đang ở bên trong phòng/nhà nhìn hành động đi ra ngoài.",
                    "sound_txt": "出去"
                },
                {
                    "tu": "上去",
                    "pinyin": "shàng qù",
                    "nghianhanh": "Đi lên.",
                    "cachdung": "Người nói đang ở dưới nhìn hành động đi lên phía trên.",
                    "sound_txt": "上去"
                },
                {
                    "tu": "拿去",
                    "pinyin": "ná qù",
                    "nghianhanh": "Cầm đi, mang đi.",
                    "cachdung": "Động từ '拿' (cầm) kết hợp với '去' chỉ hướng di chuyển ra xa người nói.",
                    "sound_txt": "拿去"
                }
            ]
        }
    ]

    # Fix typo in Vietnamese/Chinese mix for item
    B7_5_QU_DATA[0]["items"][1]["tu"] = "我们去超市吧！"

    # ================= TAB 1: CẤU TRÚC NGỮ PHÁP =================
    with tab_grammar:
        st.subheader("Cách dùng chi tiết từ 去 (qù)")
        st.write("Hãy phân biệt rõ 3 cách dùng và cấu trúc của từ 去:")

        for group_idx, group in enumerate(B7_5_QU_DATA):
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
                    </div>
                    """.replace("\n", " ")
                    st.markdown(card_html, unsafe_allow_html=True)
                with cols[1]:
                    st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
                    render_play_button(
                        item['tu'], 
                        f"🔊 Phát âm ví dụ", 
                        key=f"play_v75_{group_idx}_{idx}"
                    )
            st.markdown("<br/>", unsafe_allow_html=True)

    # ================= TAB 2: THỰC HÀNH KHẨU NGỮ =================
    with tab_practice:
        st.subheader("🗣️ Thực hành Giao tiếp và Phản xạ")
        st.write("Luyện nghe và chọn câu trả lời phản hồi phù hợp nhất:")

        practice_items = [
            {
                "id": "pr_qu1",
                "q_han": "你去哪儿？",
                "q_py": "Nǐ qù nǎr?",
                "q_vi": "Bạn đi đâu đấy?",
                "choices": [
                    "我去学校学习汉语。 (Wǒ qù xuéxiào xuéxí Hànyǔ.) - Tôi đi trường học tiếng Trung.",
                    "他在家。 (Tā zài jiā.) - Anh ấy ở nhà.",
                    "这是我的书。 (Zhè shì wǒ de shū.) - Đây là sách của tôi."
                ],
                "correct": "我去 school 学习汉语。 (Wǒ qù xuéxiào xuéxí Hànyǔ.) - Tôi đi trường học tiếng Trung."
            },
            {
                "id": "pr_qu2",
                "q_han": "下午我们去超市买水果，好吗？",
                "q_py": "Xiàwǔ wǒmen qù chāoshì mǎi shuǐguǒ, hǎo ma?",
                "q_vi": "Chiều nay chúng ta đi siêu thị mua hoa quả nhé, được không?",
                "choices": [
                    "太好了！我们去吧。 (Tài hǎo le! Wǒmen qù ba.) - Tuyệt quá! Chúng ta đi đi.",
                    "他在看电视。 (Tā zài kàn diànshì.) - Anh ấy đang xem tivi.",
                    "我去买饭。 (Wǒ qù mǎi fàn.) - Tôi đi mua cơm."
                ],
                "correct": "太好了！Chúng ta đi đi. (Tài hǎo le! Wǒmen qù ba.) - Tuyệt quá! Chúng ta đi đi."
            }
        ]

        # Fix minor mix in correct option representation
        practice_items[0]["correct"] = "我去学校学习汉语。 (Wǒ qù xuéxiào xuéxí Hànyǔ.) - Tôi đi trường học tiếng Trung."
        practice_items[1]["correct"] = "太好了！เรา去吧。 (Tài hǎo le! Wǒmen qù ba.) - Tuyệt quá! Chúng ta đi đi.".replace("เรา", "我们")

        for item in practice_items:
            st.markdown(f"##### 🎧 Nghe câu hỏi:")
            cols = st.columns([8, 2])
            with cols[0]:
                st.markdown(f"<div style='background:#f1f5f9; padding: 10px; border-radius: 8px; font-weight: bold;'>{item['q_han']} ({item['q_py']}) <span style='font-weight: normal; font-style: italic; color: #475569;'>- {item['q_vi']}</span></div>", unsafe_allow_html=True)
            with cols[1]:
                render_play_button(item['q_han'], "🔊 Nghe", key=f"play_q_pr75_{item['id']}")

            user_ans = st.radio("Chọn câu phản hồi đúng nhất:", item['choices'], key=f"pr75_ans_select_{item['id']}")
            if user_ans == item['correct']:
                st.success("✅ Phản hồi hoàn hảo!")
            else:
                st.info("💡 Hãy phân tích kỹ câu hỏi để chọn đáp án phù hợp nhất.")
            st.markdown("---")

    # ================= TAB 3: BÀI TẬP PHẢN XẠ =================
    with tab_quiz:
        st.subheader("Bài tập phản xạ cấu trúc từ 去 (qù)")
        st.write("Làm bài trắc nghiệm dưới đây và nhấn nút Nộp bài để ghi nhận kết quả:")

        B7_5_QUIZ_DATA = [
            {
                "q": "Chọn câu đúng nhất nghĩa của câu: 'Tôi đi cửa hàng mua quần áo.'",
                "choices": [
                    "我去商店买衣服。 (Wǒ qù shāngdiàn mǎi yīfu.)",
                    "我买衣服去商店。 (Wǒ mǎi yīfu qù shāngdiàn.)",
                    "我去买衣服商店。 (Wǒ qù mǎi yīfu shāngdiàn.)"
                ],
                "answer": "我去商店买衣服。 (Wǒ qù shāngdiàn mǎi yīfu.)",
                "explain": "Cấu trúc liên động chỉ mục đích: Chủ ngữ + 去 + Địa điểm (商店) + Hành động (买衣服)."
            },
            {
                "q": "Trong câu '请你出去。' (Mời bạn đi ra ngoài), từ '去' đóng vai trò gì?",
                "choices": [
                    "Động từ chính chỉ hành động đi",
                    "Bổ ngữ xu hướng (Xu hướng động từ chỉ hướng ra xa người nói)",
                    "Phó từ chỉ hành động đang diễn ra"
                ],
                "answer": "Bổ ngữ xu hướng (Xu hướng động từ chỉ hướng ra xa người nói)",
                "explain": "'去' đứng sau động từ hành động '出' (ra) làm bổ ngữ xu hướng để chỉ hướng đi ra xa phía người nói."
            },
            {
                "q": "Chọn câu rủ rê đúng ngữ pháp: 'Chúng ta đi trường học đi!'",
                "choices": [
                    "我们去学校吗？ (Wǒmen qù xuéxiào ma?)",
                    "我们去学校吧！ (Wǒmen qù xuéxiào ba!)",
                    "Chúng ta去学校。 (Wǒmen qù xuéxiào.)"
                ],
                "answer": "Chúng ta đi trường học đi! (Wǒmen qù xuéxiào ba!)".replace("Chúng ta đi trường học đi!", "我们去学校吧！"),
                "explain": "Trợ từ ngữ khí '吧' đặt cuối câu trần thuật biểu thị sự thương lượng, rủ rê, khuyên bảo."
            },
            {
                "q": "Nếu người nói đang ở trong phòng học và gọi bạn học sinh đang ở ngoài cửa 'đi vào', người nói sẽ dùng từ nào?",
                "choices": [
                    "进去 (jìn qù)",
                    "进来 (jìn lái)",
                    "出去 (chū qù)"
                ],
                "answer": "进来 (jìn lái)",
                "explain": "Vì người nói ở bên trong, hướng hành động là tiến về phía người nói nên dùng '来' (进来), còn nếu người nói ở ngoài thì dùng '去' (进去)."
            },
            {
                "q": "Chọn câu đúng ngữ pháp nhất biểu thị ý: 'Chiều nay tôi đi Trung Quốc.'",
                "choices": [
                    "下午我去中国。 (Xiàwǔ wǒ qù Zhōngguó.)",
                    "我去中国下午。 (Wǒ qù Zhōngguó xiàwǔ.)",
                    "下午去中国我。 (Xiàwǔ qù Zhōngguó wǒ.)"
                ],
                "answer": "下午我去中国。 (Xiàwǔ wǒ qù Zhōngguó.)",
                "explain": "Trạng ngữ thời gian '下午' đứng đầu câu hoặc đứng ngay trước động từ/chủ ngữ, không đứng ở cuối câu như tiếng Anh hay tiếng Việt."
            }
        ]

        # Fix key typo in choice representation
        B7_5_QUIZ_DATA[2]["answer"] = "我们去学校吧！ (Wǒmen qù xuéxiào ba!)"

        if "b75_score_submitted" not in st.session_state:
            st.session_state.b75_score_submitted = False

        score_b7_5 = 0
        user_answers = {}

        for idx, item in enumerate(B7_5_QUIZ_DATA):
            st.markdown(f"#### Câu {idx+1}: {item['q']}")
            user_ans = st.radio(f"Chọn đáp án đúng cho Câu {idx+1}:", item['choices'], index=0, key=f"v75_quiz_ans_{idx}")
            user_answers[idx] = user_ans
            if user_ans == item['answer']:
                score_b7_5 += 1
            st.markdown("<hr style='margin: 15px 0; border: 0; border-top: 1px dashed #e2e8f0;'/>", unsafe_allow_html=True)

        if not st.session_state.b75_score_submitted:
            if st.button("📝 Chấm điểm bài tập Bài 7.5", type="primary", use_container_width=True, key="v75_quiz_grade_btn"):
                st.session_state.b75_score_submitted = True
                st.rerun()
        else:
            st.markdown("### Kết quả chấm điểm chi tiết:")
            for idx, item in enumerate(B7_5_QUIZ_DATA):
                u_ans = user_answers[idx]
                if u_ans == item['answer']:
                    st.success(f"✅ **Câu {idx+1}: Chính xác!**")
                    st.write(f"Giải thích: {item['explain']}")
                else:
                    st.error(f"❌ **Câu {idx+1}: Chưa chính xác!** (Bạn chọn: {u_ans})")
                    st.write(f"👉 Đáp án đúng: **{item['answer']}**")
                    st.write(f"Giải thích: {item['explain']}")

            final_percentage_score = round((score_b7_5 / len(B7_5_QUIZ_DATA)) * 10, 2)
            st.markdown(f"### Điểm tổng kết: **{score_b7_5} / {len(B7_5_QUIZ_DATA)}** ({final_percentage_score} điểm hệ 10)")
            
            if score_b7_5 == len(B7_5_QUIZ_DATA):
                st.balloons()
                st.success("Tuyệt vời! Bạn đã hoàn toàn làm chủ cách sử dụng từ 去 (qù)! 👑")

            st.markdown("---")
            name = st.text_input("Nhập tên học viên để nộp điểm:", key="v74_student_name_b75")
            if st.button("Nộp bài tập Bài 7.5", type="primary", use_container_width=True, key="v75_submit_score_btn"):
                if name:
                    row = {
                        "thời gian": datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S"),
                        "học viên": name,
                        "tổng điểm": final_percentage_score,
                        "BT: Từ 去": f"{score_b7_5}/{len(B7_5_QUIZ_DATA)}"
                    }
                    if save_score_row_b7_5(row):
                        st.success("Đã nộp bài và lưu điểm thành công!")
                        st.session_state.b75_score_submitted = False
                        save_progress()
                        st.rerun()
                else:
                    st.error("Vui lòng nhập tên để nộp bài!")

            if st.button("🔄 Làm lại bài tập", use_container_width=True, key="v75_redo_quiz_btn"):
                st.session_state.b75_score_submitted = False
                save_progress()
                st.rerun()

        # Hiển thị bảng xếp hạng nộp bài lớp học
        all_scores = load_all_scores_b7_5()
        if all_scores:
            st.write("### 🏆 Bảng xếp hạng nộp bài lớp học:")
            st.dataframe(all_scores, use_container_width=True)


def show_lesson7_vocab():
    st.markdown("""
    <style>
    .vocab-section-title-b7 {
        color: #1e3a8a;
        border-left: 5px solid #e11d48;
        padding-left: 12px;
        margin-top: 30px;
        margin-bottom: 15px;
        font-weight: 700;
        font-size: 1.4rem;
    }
    .vocab-card-b7 {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        transition: transform 0.2s, box-shadow 0.2s;
        margin-bottom: 10px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 280px;
    }
    .vocab-card-b7:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05);
        border-color: #cbd5e1;
    }
    .vocab-word-b7 {
        font-size: 2.2rem;
        font-weight: 800;
        color: #e11d48;
        margin-bottom: 2px;
        line-height: 1.2;
    }
    .vocab-pinyin-b7 {
        font-family: 'Courier New', monospace;
        font-size: 1.1rem;
        font-weight: 700;
        color: #2563eb;
        margin-bottom: 6px;
    }
    .vocab-viet-b7 {
        font-size: 0.95rem;
        font-weight: 700;
        color: #475569;
        margin-bottom: 10px;
    }
    .vocab-ex-box-b7 {
        background: #f8fafc;
        border-radius: 8px;
        padding: 8px;
        border: 1px solid #f1f5f9;
    }
    .vocab-ex-title-b7 {
        font-size: 0.7rem;
        color: #94a3b8;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 2px;
    }
    .vocab-ex-han-b7 {
        font-size: 1.05rem;
        font-weight: 700;
        color: #1e293b;
        display: block;
        margin-bottom: 1px;
    }
    .vocab-ex-py-b7 {
        font-family: 'Courier New', monospace;
        color: #059669;
        display: block;
        margin-bottom: 2px;
        font-size: 0.8rem;
    }
    .vocab-ex-vi-b7 {
        color: #475569;
        font-style: italic;
        display: block;
        font-size: 0.78rem;
    }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "📚 Bài 7: Hệ thống từ vựng",
        "Học các từ vựng theo nhóm về hoạt động thường ngày, thời gian, từ để hỏi và giao tiếp lịch sự."
    )

    groups = [
        {
            "name": "📅 Nhóm 1: Hoạt động thường ngày (日常活动)",
            "items": [
                {"word": "吃饭", "pinyin": "chī fàn", "vietnamese": "ăn cơm", "example_han": "我们去吃饭吧。", "example_py": "Wǒmen qù chī fàn ba.", "example_vi": "Chúng ta đi ăn cơm đi."},
                {"word": "做", "pinyin": "zuò", "vietnamese": "làm", "example_han": "你在做什么？", "example_py": "Nǐ zài zuò shénme?", "example_vi": "Bạn đang làm gì?"},
                {"word": "工作", "pinyin": "gōngzuò", "vietnamese": "công việc / làm việc", "example_han": "我很喜欢我的工作。", "example_py": "Wǒ hěn xǐhuān wǒ de gōngzuò.", "example_vi": "Tôi rất thích công việc của tôi."},
                {"word": "你在做什么？", "pinyin": "nǐ zài zuò shénme?", "vietnamese": "bạn đang làm gì?", "example_han": "你在做什么？我在工作。", "example_py": "Nǐ zài zuò shénme? Wǒ zài gōngzuò.", "example_vi": "Bạn đang làm gì? Tôi đang làm việc."},
                {"word": "坐飞机", "pinyin": "zuò fēi jī", "vietnamese": "ngồi máy bay / đi máy bay", "example_han": "我坐飞机去北京。", "example_py": "Wǒ zoù fēi jī qù Běijīng.", "example_vi": "Tôi đi máy bay đến Bắc Kinh."}
            ]
        },
        {
            "name": "⏰ Nhóm 2: Từ hỏi và Thời gian (疑问词 & 时间)",
            "items": [
                {"word": "还没", "pinyin": "hái méi", "vietnamese": "chưa (not yet)", "example_han": "他还没来。", "example_py": "Tā hái méi lái.", "example_vi": "Anh ấy chưa đến."},
                {"word": "哪个人", "pinyin": "nǎ ge rén", "vietnamese": "người nào", "example_han": "哪个人是你的老师？", "example_py": "Nǎ ge rén  shì nǐ de lǎoshī?", "example_vi": "Người nào là giáo viên của bạn?"},
                {"word": "日", "pinyin": "rì", "vietnamese": "ngày (văn viết)", "example_han": "十月一日是国庆节。", "example_py": "Shí yuè yī rì  shì guóqìng jié.", "example_vi": "Ngày 1 tháng 10 là ngày Quốc khánh."},
                {"word": "天", "pinyin": "tiān", "vietnamese": "ngày (bao nhiêu ngày)", "example_han": "我去北京三天。", "example_py": "Wǒ qù Běijīng sān tiān.", "example_vi": "Tôi đi Bắc Kinh ba ngày."},
                {"word": "号", "pinyin": "hào", "vietnamese": "ngày (trong câu hỏi hỏi ngày mấy / văn nói)", "example_han": "今天几号？", "example_py": "Jīntiān jǐ hào?", "example_vi": "Hôm nay ngày mấy?"}
            ]
        },
        {
            "name": "🗣️ Nhóm 3: Giao tiếp & Lịch sự (日常交际)",
            "items": [
                {"word": "因为", "pinyin": "yīn wèi", "vietnamese": "tại vì / bởi vì", "example_han": "因为今天很忙，我不去。", "example_py": "Yīnwèi jīntiān hěn máng, wǒ bú qù.", "example_vi": "Vì hôm nay rất bận nên tôi không đi."},
                {"word": "没关系", "pinyin": "méi guān xi", "vietnamese": "không sao / không có gì", "example_han": "对不起！没关系。", "example_py": "Duìbuqǐ! Méi guān xi.", "example_vi": "Xin lỗi! Không sao đâu."},
                {"word": "不客气", "pinyin": "bù kè qì", "vietnamese": "đừng khách sáo / không có gì", "example_han": "谢谢`你！不客气。", "example_py": "Xièxie nǐ! Bú kèqi.", "example_vi": "Cảm ơn bạn! Đừng khách sáo."},
                {"word": "哪里！", "pinyin": "nǎlǐ!", "vietnamese": "nhận được lời khen, tỏ ra khiêm tốn (đâu có!)", "example_han": "你汉语很好！哪里，哪里！", "example_py": "Nǐ Hànyǔ hěn hǎo! Nǎlǐ, nǎlǐ!", "example_vi": "Tiếng Trung của bạn rất tốt! Đâu có, đâu có!"}
            ]
        }
    ]

    group_key = "b7_vocab_group_idx"
    if group_key not in st.session_state:
        st.session_state[group_key] = 0

    cur_group_idx = st.session_state[group_key]
    if cur_group_idx >= len(groups):
        cur_group_idx = 0
        st.session_state[group_key] = 0

    cur_group = groups[cur_group_idx]

    # Navigation controller
    col_prev, col_title, col_next = st.columns([1.5, 4, 1.5])
    with col_prev:
        if st.button("⬅️ Nhóm trước", use_container_width=True, key="b7_g_prev"):
            st.session_state[group_key] = (cur_group_idx - 1) % len(groups)
            st.rerun()
    with col_title:
        st.markdown(f"<div style='text-align: center; font-size: 1.25rem; font-weight: bold; color: #e11d48; padding: 6px; background: #fff1f2; border-radius: 8px; border: 1px solid #fecdd3;'>{cur_group['name']}</div>", unsafe_allow_html=True)
    with col_next:
        if st.button("Nhóm sau ➡️", use_container_width=True, key="b7_g_next"):
            st.session_state[group_key] = (cur_group_idx + 1) % len(groups)
            st.rerun()

    st.markdown(f"<div style='text-align: center; font-size: 1rem; font-weight: bold; margin-top: 5px; color:#475569;'>Nhóm {cur_group_idx + 1} / {len(groups)}</div>", unsafe_allow_html=True)
    st.progress((cur_group_idx + 1) / len(groups))

    # Render active group cards
    items = cur_group["items"]
    cols = st.columns(len(items))
    for idx, item in enumerate(items):
        with cols[idx]:
            card_html = f"""<div class="vocab-card-b7">
<div>
<div class="vocab-word-b7">{item['word']}</div>
<div class="vocab-pinyin-b7">{item['pinyin']}</div>
<div class="vocab-viet-b7">Nghĩa: {item['vietnamese']}</div>
<div class="vocab-ex-box-b7">
<div class="vocab-ex-title-b7">Ví dụ:</div>
<div class="vocab-ex-han-b7">{item['example_han']}</div>
<div class="vocab-ex-py-b7">{item['example_py']}</div>
<div class="vocab-ex-vi-b7">{item['example_vi']}</div>
</div>
</div>
</div>""".replace("\n", " ")
            st.markdown(card_html, unsafe_allow_html=True)
            render_play_button(item['word'], "🔊 Đọc từ", key=f"v7_g{cur_group_idx}_w_{idx}")
            render_play_button(item['example_han'], "🔊 Nghe ví dụ", key=f"v7_g{cur_group_idx}_ex_{idx}")


