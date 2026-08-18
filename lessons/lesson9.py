import streamlit as st
from ui_utils import render_lesson_intro
from lessons_data import (
    B9_1_QUOC_GIA, B9_1_QUOC_TICH, B9_1_TIEN_TE
)

def show_lesson9_1_countries_currency():
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
        "🌍 Bài 9.1: Quốc gia, Quốc tịch và Tiền tệ",
        "Học cách gọi tên các quốc gia, hỏi đáp về quốc tịch và nhận biết tiền tệ của các quốc gia nổi tiếng."
    )

    tab_countries, tab_nationality, tab_currency, tab_sentences = st.tabs([
        "🗺️ Các quốc gia",
        "🧑‍🤝‍🧑 Quốc tịch",
        "💵 Tiền tệ",
        "🗣️ Mẫu câu"
    ])

    with tab_countries:
        st.subheader("1. Tên một số quốc gia trên thế giới")
        cols = st.columns(2)
        for idx, item in enumerate(B9_1_QUOC_GIA):
            col = cols[idx % 2]
            with col:
                card_html = f"""
                <div class="word-card">
                    <div style="display: flex; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 5px;">
                        <span class="word-title">{item['Chữ Hán']}</span>
                        <span class="pinyin-badge">{item['Pinyin']}</span>
                    </div>
                    <div style="margin-top: 10px;">
                        <span class="meaning-badge">{item['Nghĩa tiếng Việt']}</span>
                    </div>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)

    with tab_nationality:
        st.subheader("2. Người các nước (Quốc tịch)")
        st.markdown("""
        <div class="rule-box">
            <h4>💡 Cấu trúc tạo từ chỉ quốc tịch:</h4>
            <p style="font-size: 1.2rem; font-weight: bold; color: #0f172a;">
                Tên quốc gia + 人 (rén)
            </p>
        </div>
        <br/>
        """, unsafe_allow_html=True)

        cols = st.columns(2)
        for idx, item in enumerate(B9_1_QUOC_TICH):
            col = cols[idx % 2]
            with col:
                card_html = f"""
                <div class="word-card">
                    <div style="display: flex; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 5px;">
                        <span class="word-title">{item['Chữ Hán']}</span>
                        <span class="pinyin-badge">{item['Pinyin']}</span>
                    </div>
                    <div style="margin-top: 10px;">
                        <span class="meaning-badge">{item['Nghĩa tiếng Việt']}</span>
                    </div>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)

    with tab_currency:
        st.subheader("3. Tiền tệ của các quốc gia")
        cols = st.columns(2)
        for idx, item in enumerate(B9_1_TIEN_TE):
            col = cols[idx % 2]
            with col:
                card_html = f"""
                <div class="word-card">
                    <div style="display: flex; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 5px;">
                        <span class="word-title">{item['Chữ Hán']}</span>
                        <span class="pinyin-badge">{item['Pinyin']}</span>
                    </div>
                    <div style="margin-top: 10px;">
                        <span class="meaning-badge">{item['Nghĩa tiếng Việt']}</span>
                    </div>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)

    with tab_sentences:
        st.subheader("4. Các mẫu câu giao tiếp cơ bản")
        sentences = [
            {
                "Q_han": "你是哪国人？",
                "Q_py": "Nǐ shì nǎ guórén?",
                "Q_vi": "Bạn là người nước nào?",
                "A_han": "我是越南人。",
                "A_py": "Wǒ shì Yuènán rén.",
                "A_vi": "Tôi là người Việt Nam."
            },
            {
                "Q_han": "这是什么钱？",
                "Q_py": "Zhè shì shénme qián?",
                "Q_vi": "Đây là tiền gì?",
                "A_han": "这是美元。",
                "A_py": "Zhè shì Měiyuán.",
                "A_vi": "Đây là Đô la Mỹ."
            },
            {
                "Q_han": "他是美国人吗？",
                "Q_py": "Tā shì Měiguó rén ma?",
                "Q_vi": "Anh ấy có phải là người Mỹ không?",
                "A_han": "不，他是英国人。",
                "A_py": "Bù, tā shì Yīngguó rén.",
                "A_vi": "Không, anh ấy là người Anh."
            }
        ]
        
        for item in sentences:
            st.markdown(f"""
            <div class="word-card" style="border-left: 5px solid #f59e0b;">
                <div style="margin-bottom: 15px;">
                    <span style="font-weight: bold; color: #d97706; font-size: 1.1rem;">A:</span>
                    <span style="font-size: 1.5rem; font-weight: bold; margin-left: 10px;">{item['Q_han']}</span><br/>
                    <span style="font-family: monospace; color: #475569; margin-left: 30px;">{item['Q_py']}</span><br/>
                    <span style="color: #64748b; font-style: italic; margin-left: 30px;">Dịch: {item['Q_vi']}</span>
                </div>
                <div>
                    <span style="font-weight: bold; color: #059669; font-size: 1.1rem;">B:</span>
                    <span style="font-size: 1.5rem; font-weight: bold; margin-left: 10px;">{item['A_han']}</span><br/>
                    <span style="font-family: monospace; color: #475569; margin-left: 30px;">{item['A_py']}</span><br/>
                    <span style="color: #64748b; font-style: italic; margin-left: 30px;">Dịch: {item['A_vi']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)


from lessons_data import B9_1_PRACTICE_DATA
import random

def show_lesson9_1_classroom_practice():
    st.markdown("""
    <style>
    .practice-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    .grammar-note {
        color: #3b82f6;
        font-weight: 600;
        font-size: 0.95rem;
        margin-bottom: 15px;
    }
    .dialogue-bubble-a {
        background: #f0fdf4;
        border-left: 4px solid #22c55e;
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .dialogue-bubble-b {
        background: #eff6ff;
        border-left: 4px solid #3b82f6;
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 10px;
        margin-left: 20px;
    }
    .speaker-name {
        font-weight: bold;
        font-size: 1.1rem;
        margin-right: 8px;
    }
    .hanzi-text {
        font-size: 1.4rem;
        font-weight: bold;
        color: #0f172a;
    }
    .pinyin-text {
        font-family: monospace;
        color: #475569;
        font-size: 1.05rem;
    }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "🗣️ Bài 9.1: Thực hành Giao tiếp & Phản xạ",
        "Luyện tập phản xạ thông qua các tình huống thực tế và kết hợp điểm ngữ pháp của các bài trước."
    )

    tab_dialogues, tab_activities = st.tabs(["💬 Hội thoại thực hành", "🎮 Hoạt động nhóm"])

    with tab_dialogues:
        st.subheader("Thực hành đóng vai (Role-play)")
        for dlg in B9_1_PRACTICE_DATA['dialogues']:
            st.markdown(f"### {dlg['title']}")
            st.markdown(f"<div class='grammar-note'>💡 Điểm ngữ pháp: {dlg['grammar']}</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='practice-card'>", unsafe_allow_html=True)
            for line in dlg['lines']:
                bubble_class = 'dialogue-bubble-a' if line['speaker'] == 'A' else 'dialogue-bubble-b'
                speaker_color = '#166534' if line['speaker'] == 'A' else '#1e40af'
                st.markdown(f"""
                <div class='{bubble_class}'>
                    <span class='speaker-name' style='color: {speaker_color};'>{line['speaker']}:</span>
                    <span class='hanzi-text'>{line['han']}</span><br/>
                    <span class='pinyin-text' style='margin-left: 25px;'>{line['py']}</span><br/>
                    <span style='color: #64748b; font-style: italic; margin-left: 25px;'>Dịch: {line['vi']}</span>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

    with tab_activities:
        st.subheader("🎮 Hoạt động nhóm: Siêu thị Quốc tế (国际超市)")

        st.markdown("""
        <div class='practice-card' style='border-top: 5px solid #f59e0b; border-left: 5px solid #8b5cf6;'>
            <h4 style='color: #d97706;'>🌍💱 Hoạt động: Vòng quay Quốc tịch &amp; Quầy Thu ngân</h4>
            <p><b>Luật chơi kết hợp:</b> Nhấn nút để random ra 1 <b>quốc gia</b> và 1 <b>mức giá tiền tệ</b>.
            Học viên A đóng vai <b>nhân viên thu ngân</b>, Học viên B đóng vai <b>khách hàng nước ngoài</b> theo quốc gia được chọn.
            Hai bạn cùng tạo đoạn hội thoại tự nhiên dựa trên thẻ bài!</p>
            <p style='color: #6b7280; font-size: 0.9rem;'>💡 <i>Dùng các câu gợi ý bên dưới để phong phú hội thoại hơn nhé!</i></p>
        </div>
        """, unsafe_allow_html=True)

        btn_col, result_col = st.columns([1, 2])
        with btn_col:
            if st.button("🎲 Random Bài", use_container_width=True):
                countries = [
                    ("中国", "Trung Quốc", "中国人", "Người Trung Quốc", "人民币", "NDT"),
                    ("越南", "Việt Nam", "越南人", "Người Việt Nam", "越南盾", "VND"),
                    ("美国", "Mỹ", "美国人", "Người Mỹ", "美元", "Đô la Mỹ"),
                    ("英国", "Anh", "英国人", "Người Anh", "英镑", "Bảng Anh"),
                    ("法国", "Pháp", "法国人", "Người Pháp", "欧元", "Euro"),
                    ("日本", "Nhật Bản", "日本人", "Người Nhật", "日元", "Yên Nhật"),
                    ("韩国", "Hàn Quốc", "韩国人", "Người Hàn Quốc", "韩元", "Won Hàn"),
                    ("德国", "Đức", "德国人", "Người Đức", "欧元", "Euro"),
                    ("泰国", "Thái Lan", "泰国人", "Người Thái Lan", "泰铢", "Baht"),
                    ("澳大利亚", "Úc", "澳大利亚人", "Người Úc", "澳元", "Đô la Úc"),
                ]
                amounts = ["20", "50", "80", "100", "200", "300", "500", "1000"]
                c = random.choice(countries)
                amt = random.choice(amounts)
                st.session_state["act_country"] = c
                st.session_state["act_amount"] = amt

        with result_col:
            if "act_country" in st.session_state:
                c = st.session_state["act_country"]
                amt = st.session_state["act_amount"]
                st.markdown(f"""
                <div style='display: flex; gap: 15px; flex-wrap: wrap;'>
                    <div style='flex: 1; min-width: 130px; text-align: center;
                                background: linear-gradient(135deg,#eff6ff,#dbeafe);
                                border-radius: 12px; padding: 16px; border: 1px solid #bfdbfe;'>
                        <div style='font-size: 0.8rem; color: #6b7280; margin-bottom: 6px;'>🌍 Vai khách hàng</div>
                        <div style='font-size: 2rem; font-weight: 900; color: #1e3a8a;'>{c[2]}</div>
                        <div style='font-size: 0.85rem; color: #3b82f6; font-weight: 600;'>{c[3]}</div>
                    </div>
                    <div style='flex: 1; min-width: 130px; text-align: center;
                                background: linear-gradient(135deg,#fef3c7,#fde68a);
                                border-radius: 12px; padding: 16px; border: 1px solid #fcd34d;'>
                        <div style='font-size: 0.8rem; color: #6b7280; margin-bottom: 6px;'>💰 Giá sản phẩm</div>
                        <div style='font-size: 2rem; font-weight: 900; color: #92400e;'>{amt} {c[4]}</div>
                        <div style='font-size: 0.85rem; color: #b45309; font-weight: 600;'>{amt} {c[5]}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<br/>", unsafe_allow_html=True)

        # --- Câu hỏi gợi ý ---
        hint_col1, hint_col2 = st.columns(2)

        with hint_col1:
            st.html("""
            <div class='practice-card' style='background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:20px;margin-bottom:20px;border-top:4px solid #3b82f6;'>
                <h5 style='color:#1d4ed8;margin-bottom:10px;'>🟡 Hỏi & xác nhận quốc tịch</h5>
                <ul style='padding-left:18px;font-size:0.9rem;color:#374151;line-height:2;'>
                    <li><b>你是哪国人？</b><br/><span style='color:#6b7280;font-style:italic;'>Nǐ shì nǎ guórén? — Bạn là người nước nào?</span></li>
                    <li><b>你来自哪里？</b><br/><span style='color:#6b7280;font-style:italic;'>Nǐ láizì nǎlǐ? — Bạn đến từ đâu?</span></li>
                    <li><b>你的国籍是什么？</b><br/><span style='color:#6b7280;font-style:italic;'>Nǐ de guójí shì shénme? — Quốc tịch của bạn là gì?</span></li>
                    <li><b>他是美国人吗？</b><br/><span style='color:#6b7280;font-style:italic;'>Tā shì Měiguórén ma? — Anh ấy là người Mỹ à?</span></li>
                    <li><b>你们班有几个国家的同学？</b><br/><span style='color:#6b7280;font-style:italic;'>Lớp có bao nhiêu quốc tịch?</span></li>
                    <li><b>你第一次来这里吗？</b><br/><span style='color:#6b7280;font-style:italic;'>Nǐ dì yī cì lái zhèlǐ ma? — Bạn lần đầu đến đây à?</span></li>
                </ul>
                <h5 style='color:#059669;margin:14px 0 10px;'>🟢 Trả lời quốc tịch</h5>
                <ul style='padding-left:18px;font-size:0.9rem;color:#374151;line-height:2;'>
                    <li><b>我是＿＿人。</b><br/><span style='color:#6b7280;font-style:italic;'>Wǒ shì ___rén. — Tôi là người ...</span></li>
                    <li><b>我来自＿＿。</b><br/><span style='color:#6b7280;font-style:italic;'>Wǒ láizì ___ — Tôi đến từ ...</span></li>
                    <li><b>不，他是＿＿人。</b><br/><span style='color:#6b7280;font-style:italic;'>Bù, tā shì ___rén. — Không, anh ấy là người ...</span></li>
                    <li><b>对，我是第一次来。</b><br/><span style='color:#6b7280;font-style:italic;'>Duì, wǒ shì dì yī cì lái. — Đúng, lần đầu tôi đến.</span></li>
                    <li><b>我在＿＿住了三年。</b><br/><span style='color:#6b7280;font-style:italic;'>Wǒ zài ___ zhùle sān nián. — Tôi đã sống ở ... 3 năm rồi.</span></li>
                    <li><b>我很喜欢中国！</b><br/><span style='color:#6b7280;font-style:italic;'>Wǒ hěn xǐhuān Zhōngguó! — Tôi rất thích Trung Quốc!</span></li>
                </ul>
            </div>
            """)

        with hint_col2:
            st.html("""
            <div class='practice-card' style='background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:20px;margin-bottom:20px;border-top:4px solid #8b5cf6;'>
                <h5 style='color:#7c3aed;margin-bottom:10px;'>🟣 Hỏi về tiền tệ & thanh toán</h5>
                <ul style='padding-left:18px;font-size:0.9rem;color:#374151;line-height:2;'>
                    <li><b>这是什么钱？</b><br/><span style='color:#6b7280;font-style:italic;'>Zhè shì shénme qián? — Đây là tiền gì?</span></li>
                    <li><b>这个多少钱？</b><br/><span style='color:#6b7280;font-style:italic;'>Zhège duōshao qián? — Cái này bao nhiêu tiền?</span></li>
                    <li><b>你们收哪种货币？</b><br/><span style='color:#6b7280;font-style:italic;'>Nǐmen shōu nǎ zhǒng huòbì? — Nhận loại tiền nào?</span></li>
                    <li><b>可以用＿＿付钱吗？</b><br/><span style='color:#6b7280;font-style:italic;'>Kěyǐ yòng ___ fùqián ma? — Có thể dùng ... để trả không?</span></li>
                    <li><b>能换成人民币吗？</b><br/><span style='color:#6b7280;font-style:italic;'>Néng huàn chéng Rénmínbì ma? — Đổi sang NDT được không?</span></li>
                    <li><b>有没有打折？</b><br/><span style='color:#6b7280;font-style:italic;'>Yǒu méiyǒu dǎzhé? — Có giảm giá không?</span></li>
                    <li><b>可以刷卡吗？</b><br/><span style='color:#6b7280;font-style:italic;'>Kěyǐ shuākǎ ma? — Có thể quẹt thẻ không?</span></li>
                    <li><b>有没有更便宜的？</b><br/><span style='color:#6b7280;font-style:italic;'>Yǒu méiyǒu gèng piányí de? — Có loại rẻ hơn không?</span></li>
                </ul>
                <h5 style='color:#dc2626;margin:14px 0 10px;'>🔴 Trả lời thanh toán</h5>
                <ul style='padding-left:18px;font-size:0.9rem;color:#374151;line-height:2;'>
                    <li><b>这是＿＿（loại tiền）。</b><br/><span style='color:#6b7280;font-style:italic;'>Zhè shì ___ — Đây là ...</span></li>
                    <li><b>一共＿＿块。</b><br/><span style='color:#6b7280;font-style:italic;'>Yīgòng ___ kuài. — Tổng cộng ... tệ.</span></li>
                    <li><b>我们收人民币和美元。</b><br/><span style='color:#6b7280;font-style:italic;'>Chúng tôi nhận NDT và Đô la Mỹ.</span></li>
                    <li><b>不好意思，只收人民币。</b><br/><span style='color:#6b7280;font-style:italic;'>Xin lỗi, chỉ nhận NDT thôi.</span></li>
                    <li><b>可以，这里有收据。</b><br/><span style='color:#6b7280;font-style:italic;'>Kěyǐ, zhèlǐ yǒu shōujù. — Được, đây là biên lai ạ.</span></li>
                    <li><b>打九折，优惠价＿＿块。</b><br/><span style='color:#6b7280;font-style:italic;'>Dǎ jiǔ zhé, yōuhuì jià ___ kuài. — Giảm 10%, giá ưu đãi ... tệ.</span></li>
                    <li><b>找您＿＿块钱。</b><br/><span style='color:#6b7280;font-style:italic;'>Zhǎo nín ___ kuài qián. — Tiền thối lại ... tệ ạ.</span></li>
                </ul>
            </div>
            """)

# Force reload
