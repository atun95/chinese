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



def show_lesson9_2_bu_mei():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');

    .b92-hero {
        background: linear-gradient(135deg, #1e3a8a 0%, #3730a3 50%, #6d28d9 100%);
        border-radius: 20px;
        padding: 32px 36px;
        color: white;
        margin-bottom: 28px;
        box-shadow: 0 12px 40px rgba(109,40,217,0.25);
    }
    .b92-hero h1 { margin: 0 0 8px 0; font-size: 2rem; font-weight: 900; font-family: 'Inter', sans-serif; }
    .b92-hero p { margin: 0; opacity: 0.88; font-size: 1rem; }

    .b92-char-card {
        border-radius: 18px;
        padding: 28px 24px;
        text-align: center;
        height: 100%;
        box-shadow: 0 8px 28px rgba(0,0,0,0.08);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .b92-char-card:hover { transform: translateY(-4px); box-shadow: 0 14px 40px rgba(0,0,0,0.13); }
    .b92-char-card.bu  { background: linear-gradient(145deg, #fff1f2, #ffe4e6); border: 2px solid #fda4af; }
    .b92-char-card.mei { background: linear-gradient(145deg, #eff6ff, #dbeafe); border: 2px solid #93c5fd; }

    .b92-char-main { font-size: 5.5rem; font-weight: 900; line-height: 1; margin-bottom: 6px; }
    .b92-char-main.bu  { color: #e11d48; }
    .b92-char-main.mei { color: #1d4ed8; }

    .b92-pinyin { font-size: 1.3rem; font-family: monospace; font-weight: 700; margin-bottom: 10px; }
    .b92-pinyin.bu  { color: #be123c; }
    .b92-pinyin.mei { color: #1e40af; }

    .b92-tag {
        display: inline-block;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 700;
        margin-bottom: 14px;
    }
    .b92-tag.bu  { background: #fda4af; color: #9f1239; }
    .b92-tag.mei { background: #93c5fd; color: #1e3a8a; }

    .b92-rule-row {
        display: flex;
        align-items: flex-start;
        gap: 14px;
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 16px 18px;
        margin-bottom: 10px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.03);
        transition: box-shadow 0.2s;
    }
    .b92-rule-row:hover { box-shadow: 0 6px 18px rgba(0,0,0,0.07); }
    .b92-rule-icon { font-size: 1.6rem; flex-shrink: 0; margin-top: 2px; }
    .b92-rule-title { font-weight: 700; font-size: 1rem; color: #1e293b; margin-bottom: 3px; }
    .b92-rule-desc { font-size: 0.9rem; color: #475569; margin-bottom: 6px; }
    .b92-example {
        background: #f8fafc;
        border-radius: 8px;
        padding: 8px 12px;
        font-size: 0.88rem;
        color: #334155;
    }
    .b92-example .han { font-size: 1.1rem; font-weight: 700; }
    .b92-example .py  { font-family: monospace; color: #64748b; }
    .b92-example .vi  { font-style: italic; color: #64748b; }

    .b92-compare-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0 6px;
        margin-top: 10px;
    }
    .b92-compare-table th {
        padding: 10px 16px;
        font-size: 0.95rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .b92-compare-table th.hdr-criterion { background: #f1f5f9; color: #475569; border-radius: 8px 0 0 8px; }
    .b92-compare-table th.hdr-bu  { background: #fda4af; color: #9f1239; }
    .b92-compare-table th.hdr-mei { background: #93c5fd; color: #1e3a8a; border-radius: 0 8px 8px 0; }
    .b92-compare-table td {
        padding: 10px 16px;
        vertical-align: top;
        font-size: 0.93rem;
    }
    .b92-compare-table tr:nth-child(even) td { background: #fafafa; }
    .b92-compare-table td:first-child { font-weight: 600; color: #1e293b; border-radius: 8px 0 0 8px; }
    .b92-compare-table td.cell-bu  { color: #be123c; }
    .b92-compare-table td.cell-mei { color: #1d4ed8; border-radius: 0 8px 8px 0; }

    .b92-pair-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 20px 22px;
        margin-bottom: 18px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }
    .b92-pair-title {
        font-weight: 800;
        font-size: 1.05rem;
        color: #0f172a;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .b92-pair-row {
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 10px 14px;
        border-radius: 10px;
        margin-bottom: 8px;
    }
    .b92-pair-row.row-bu  { background: #fff1f2; border-left: 4px solid #e11d48; }
    .b92-pair-row.row-mei { background: #eff6ff; border-left: 4px solid #1d4ed8; }
    .b92-pair-char { font-size: 1.4rem; font-weight: 900; min-width: 36px; }
    .b92-pair-char.bu  { color: #e11d48; }
    .b92-pair-char.mei { color: #1d4ed8; }
    .b92-pair-han { font-size: 1.25rem; font-weight: 700; color: #0f172a; }
    .b92-pair-explain {
        margin-left: auto;
        background: #f8fafc;
        border-radius: 8px;
        padding: 4px 12px;
        font-size: 0.82rem;
        color: #475569;
        white-space: nowrap;
    }

    .b92-warn-card {
        border-radius: 14px;
        padding: 18px 20px;
        margin-bottom: 16px;
    }
    .b92-warn-card.wrong { background: #fff1f2; border: 2px solid #fda4af; }
    .b92-warn-card.right { background: #f0fdf4; border: 2px solid #86efac; }
    .b92-warn-title { font-weight: 800; font-size: 1rem; margin-bottom: 10px; }
    .b92-warn-title.wrong { color: #be123c; }
    .b92-warn-title.right { color: #166534; }
    .b92-warn-item { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; font-size: 0.93rem; }
    .b92-warn-item .icon { font-size: 1.1rem; flex-shrink: 0; }
    .b92-warn-item .txt-strike { text-decoration: line-through; color: #94a3b8; }
    .b92-warn-item .txt-ok { color: #0f172a; font-weight: 600; }

    .b92-tip-box {
        background: linear-gradient(135deg, #fefce8, #fef9c3);
        border: 2px solid #fde047;
        border-radius: 16px;
        padding: 22px 24px;
        margin-top: 8px;
    }
    .b92-tip-title { font-weight: 800; font-size: 1.1rem; color: #713f12; margin-bottom: 14px; }
    .b92-tip-row { display: flex; align-items: flex-start; gap: 16px; margin-bottom: 12px; }
    .b92-tip-char { font-size: 3rem; font-weight: 900; line-height: 1; min-width: 60px; text-align: center; }
    .b92-tip-char.bu  { color: #e11d48; }
    .b92-tip-char.mei { color: #1d4ed8; }
    .b92-tip-text { font-size: 0.95rem; color: #3f3f46; line-height: 1.6; }
    .b92-tip-keyword { font-weight: 700; }

    .b92-quiz-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 20px 22px;
        margin-bottom: 14px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.04);
    }
    .b92-quiz-q { font-size: 1.4rem; font-weight: 700; color: #0f172a; margin-bottom: 4px; }
    .b92-quiz-py { font-family: monospace; color: #64748b; font-size: 0.95rem; margin-bottom: 4px; }
    .b92-quiz-vi { font-style: italic; color: #94a3b8; font-size: 0.9rem; }
    .b92-score-box {
        background: linear-gradient(135deg, #1e3a8a, #3730a3);
        color: white;
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        margin-top: 20px;
    }
    .b92-score-num { font-size: 3.5rem; font-weight: 900; }
    .b92-score-label { font-size: 1rem; opacity: 0.85; }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "⚖️ Bài 9.2 - So sánh 不 (bù) và 没 (méi)",
        "Hai từ phủ định quan trọng nhất tiếng Trung — dùng sai là câu sai nghĩa hoàn toàn!"
    )

    tab_theory, tab_compare, tab_examples, tab_tips, tab_quiz = st.tabs([
        "📚 Lý thuyết",
        "🔄 So sánh",
        "📝 Ví dụ song song",
        "⚠️ Lưu ý & Mẹo nhớ",
        "🎮 Luyện tập"
    ])

    # ─────────────────────────────────────────────────────────────
    # TAB 1: LÝ THUYẾT
    # ─────────────────────────────────────────────────────────────
    with tab_theory:
        col_bu, col_mei = st.columns(2, gap="large")

        with col_bu:
            st.markdown("""
            <div class="b92-char-card bu">
                <div class="b92-char-main bu">不</div>
                <div class="b92-pinyin bu">bù</div>
                <div class="b92-tag bu">Phủ định ý chí / Tính chất</div>
            </div>
            """, unsafe_allow_html=True)

        with col_mei:
            st.markdown("""
            <div class="b92-char-card mei">
                <div class="b92-char-main mei">没</div>
                <div class="b92-pinyin mei">méi</div>
                <div class="b92-tag mei">Phủ định hành động đã/chưa xảy ra</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br/>", unsafe_allow_html=True)

        # 不 rules
        st.markdown("### 🔴 Khi nào dùng 不 (bù)?")

        rules_bu = [
            ("💬", "Từ chối / Ý chí chủ động",
             "Người nói <em>tự quyết định</em> không làm — không phải vì hoàn cảnh.",
             "我<b>不</b>去。", "Wǒ bù qù.", "Tôi <b>không đi</b> (tôi không muốn đi)."),
            ("🔄", "Thói quen / Tính chất thường xuyên",
             "Điều không bao giờ xảy ra theo <em>thói quen</em> của chủ thể.",
             "他<b>不</b>吃辣。", "Tā bù chī là.", "Anh ấy <b>không ăn</b> cay (thói quen lâu dài)."),
            ("🎨", "Phủ định tính từ / Trạng thái",
             "Dùng trước tính từ hoặc từ chỉ trạng thái.",
             "这个<b>不</b>好。", "Zhège bù hǎo.", "Cái này <b>không tốt</b>."),
            ("🏷️", "Phủ định 是 và động từ ý chí",
             "Trước 是, 想, 喜欢, 知道... — những từ thể hiện suy nghĩ, danh tính.",
             "我<b>不</b>是老师。", "Wǒ bú shì lǎoshī.", "Tôi <b>không phải</b> giáo viên."),
            ("🔮", "Phủ định tương lai",
             "Sự việc <em>chưa xảy ra</em>, mang ý định / kế hoạch.",
             "明天我<b>不</b>来。", "Míngtiān wǒ bù lái.", "Ngày mai tôi <b>sẽ không</b> đến."),
        ]

        for icon, title, desc, han, py, vi in rules_bu:
            st.markdown(f"""
            <div class="b92-rule-row">
                <div class="b92-rule-icon">{icon}</div>
                <div style="flex:1">
                    <div class="b92-rule-title">{title}</div>
                    <div class="b92-rule-desc">{desc}</div>
                    <div class="b92-example">
                        <span class="han">{han}</span><br/>
                        <span class="py">{py}</span><br/>
                        <span class="vi">→ {vi}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br/>", unsafe_allow_html=True)
        st.markdown("### 🔵 Khi nào dùng 没 (méi)?")

        rules_mei = [
            ("⏪", "Phủ định hành động đã/chưa xảy ra trong quá khứ",
             "Hành động <em>đã không / chưa</em> xảy ra — là sự thật khách quan.",
             "我<b>没</b>去。", "Wǒ méi qù.", "Tôi <b>đã không đi</b> (hành động không xảy ra)."),
            ("📦", "Phủ định sự tồn tại / sở hữu",
             "Luôn đứng trước 有 (yǒu) — không có, không tồn tại.",
             "我<b>没</b>有钱。", "Wǒ méiyǒu qián.", "Tôi <b>không có</b> tiền."),
            ("📏", "So sánh (chưa đến mức)",
             "Đứng trước tính từ để so sánh: A 没 B + tính từ = A không bằng B về...",
             "他<b>没</b>你高。", "Tā méi nǐ gāo.", "Anh ấy <b>không cao bằng</b> bạn."),
        ]

        for icon, title, desc, han, py, vi in rules_mei:
            st.markdown(f"""
            <div class="b92-rule-row">
                <div class="b92-rule-icon">{icon}</div>
                <div style="flex:1">
                    <div class="b92-rule-title">{title}</div>
                    <div class="b92-rule-desc">{desc}</div>
                    <div class="b92-example">
                        <span class="han">{han}</span><br/>
                        <span class="py">{py}</span><br/>
                        <span class="vi">→ {vi}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ─────────────────────────────────────────────────────────────
    # TAB 2: BẢNG SO SÁNH
    # ─────────────────────────────────────────────────────────────
    with tab_compare:
        st.markdown("### 🔄 Bảng so sánh trực quan")
        st.markdown("""
        <table class="b92-compare-table">
            <thead>
                <tr>
                    <th class="hdr-criterion">Tiêu chí</th>
                    <th class="hdr-bu">不 (bù)</th>
                    <th class="hdr-mei">没 (méi)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Ý nghĩa cốt lõi</td>
                    <td class="cell-bu">Phủ định ý chí, tính chất, thói quen</td>
                    <td class="cell-mei">Phủ định hành động đã/chưa xảy ra</td>
                </tr>
                <tr>
                    <td>Thì thường gặp</td>
                    <td class="cell-bu">Hiện tại · Tương lai · Thói quen</td>
                    <td class="cell-mei">Quá khứ · Thực tế đã xảy ra</td>
                </tr>
                <tr>
                    <td>Đứng trước</td>
                    <td class="cell-bu">Động từ ý chí + Tính từ + 是</td>
                    <td class="cell-mei">Động từ hành động + 有</td>
                </tr>
                <tr>
                    <td>Dùng với tính từ</td>
                    <td class="cell-bu">✅ Trực tiếp: 不好, 不大</td>
                    <td class="cell-mei">⚠️ Chỉ khi so sánh: 没你高</td>
                </tr>
                <tr>
                    <td>Dùng với 有</td>
                    <td class="cell-bu">❌ Không dùng: ~~不有~~</td>
                    <td class="cell-mei">✅ Bắt buộc: 没有</td>
                </tr>
                <tr>
                    <td>So sánh ngang bằng</td>
                    <td class="cell-bu">❌ Không dùng</td>
                    <td class="cell-mei">✅ Dùng được: 他没你高</td>
                </tr>
                <tr>
                    <td>Câu hỏi 吗 tương ứng</td>
                    <td class="cell-bu">他不去吗？ → 对，他不去。</td>
                    <td class="cell-mei">他没去吗？ → 对，他没去。</td>
                </tr>
                <tr>
                    <td>Ví dụ điển hình</td>
                    <td class="cell-bu">我不去。(Tôi không muốn đi.)</td>
                    <td class="cell-mei">我没去。(Tôi đã không đi.)</td>
                </tr>
            </tbody>
        </table>
        """, unsafe_allow_html=True)

        st.markdown("<br/>", unsafe_allow_html=True)
        st.info("💡 **Tóm gọn nhất:** 不 = *chủ quan, ý chí* | 没 = *khách quan, thực tế*")

    # ─────────────────────────────────────────────────────────────
    # TAB 3: VÍ DỤ SONG SONG
    # ─────────────────────────────────────────────────────────────
    with tab_examples:
        st.markdown("### 📝 Các cặp câu song song — cùng động từ, khác nghĩa")
        st.caption("Để thấy rõ sự khác biệt, hãy đọc từng cặp câu và chú ý sự thay đổi ý nghĩa.")

        pairs = [
            {
                "title": "Cặp 1 — Đi (去 qù)",
                "emoji": "🚶",
                "bu":  ("我不去。",      "Wǒ bù qù.",        "Tôi không đi.",        "Ý chí: tôi không muốn / không có kế hoạch đi"),
                "mei": ("我没去。",      "Wǒ méi qù.",       "Tôi đã không đi.",     "Sự thật: hành động đó đã không xảy ra"),
            },
            {
                "title": "Cặp 2 — Ăn cơm (吃饭 chī fàn)",
                "emoji": "🍚",
                "bu":  ("他不吃饭。",   "Tā bù chī fàn.",   "Anh ấy không ăn cơm.", "Thói quen: anh ấy thường kiêng / không thích"),
                "mei": ("他没吃饭。",   "Tā méi chī fàn.",  "Anh ấy chưa ăn cơm.", "Thực tế lần này: anh ấy chưa ăn"),
            },
            {
                "title": "Cặp 3 — Có (有 yǒu)",
                "emoji": "💰",
                "bu":  ("我不要钱。",   "Wǒ bù yào qián.",  "Tôi không lấy tiền.",  "Ý chí: tôi từ chối, không cần"),
                "mei": ("我没有钱。",   "Wǒ méiyǒu qián.",  "Tôi không có tiền.",   "Thực tế: tôi không có"),
            },
            {
                "title": "Cặp 4 — Ngủ (睡觉 shuìjiào)",
                "emoji": "😴",
                "bu":  ("我不睡觉。",   "Wǒ bù shuìjiào.",  "Tôi không ngủ.",       "Quyết định: tôi chọn không ngủ"),
                "mei": ("我没睡觉。",   "Wǒ méi shuìjiào.", "Tôi đã không ngủ.",    "Thực tế: tôi không ngủ đêm qua"),
            },
            {
                "title": "Cặp 5 — Xem phim (看电影 kàn diànyǐng)",
                "emoji": "🎬",
                "bu":  ("她不看电影。", "Tā bù kàn diànyǐng.", "Cô ấy không xem phim.", "Thói quen: cô ấy không thích xem phim"),
                "mei": ("她没看电影。", "Tā méi kàn diànyǐng.", "Cô ấy đã không xem phim.", "Hôm qua cô ấy không xem"),
            },
        ]

        for p in pairs:
            bu_han, bu_py, bu_vi, bu_exp = p["bu"]
            mei_han, mei_py, mei_vi, mei_exp = p["mei"]
            st.markdown(f"""
            <div class="b92-pair-card">
                <div class="b92-pair-title">{p['emoji']} {p['title']}</div>
                <div class="b92-pair-row row-bu">
                    <div class="b92-pair-char bu">不</div>
                    <div>
                        <div class="b92-pair-han">{bu_han}</div>
                        <div style="font-family:monospace;color:#64748b;font-size:0.88rem;">{bu_py}</div>
                        <div style="font-style:italic;color:#64748b;font-size:0.88rem;">→ {bu_vi}</div>
                    </div>
                    <div class="b92-pair-explain">{bu_exp}</div>
                </div>
                <div class="b92-pair-row row-mei">
                    <div class="b92-pair-char mei">没</div>
                    <div>
                        <div class="b92-pair-han">{mei_han}</div>
                        <div style="font-family:monospace;color:#64748b;font-size:0.88rem;">{mei_py}</div>
                        <div style="font-style:italic;color:#64748b;font-size:0.88rem;">→ {mei_vi}</div>
                    </div>
                    <div class="b92-pair-explain">{mei_exp}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ─────────────────────────────────────────────────────────────
    # TAB 4: LƯU Ý & MẸO NHỚ
    # ─────────────────────────────────────────────────────────────
    with tab_tips:
        st.markdown("### ⚠️ Lỗi hay gặp")

        col_w1, col_w2 = st.columns(2)
        with col_w1:
            st.markdown("""
            <div class="b92-warn-card wrong">
                <div class="b92-warn-title wrong">❌ Lỗi #1: Dùng 没 với tính từ</div>
                <div class="b92-warn-item">
                    <span class="icon">🚫</span>
                    <span class="txt-strike">他没高</span>&nbsp;→ Sai hoàn toàn!
                </div>
                <div class="b92-warn-item">
                    <span class="icon">✅</span>
                    <span class="txt-ok">他<b>不</b>高。(Anh ấy không cao.)</span>
                </div>
                <div class="b92-warn-item">
                    <span class="icon">💡</span>
                    <span>Ngoại lệ so sánh: 他<b>没</b>你高。(Không cao <em>bằng</em> bạn.)</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col_w2:
            st.markdown("""
            <div class="b92-warn-card wrong">
                <div class="b92-warn-title wrong">❌ Lỗi #2: Dùng 不 với 有</div>
                <div class="b92-warn-item">
                    <span class="icon">🚫</span>
                    <span class="txt-strike">我不有钱</span>&nbsp;→ Sai hoàn toàn!
                </div>
                <div class="b92-warn-item">
                    <span class="icon">✅</span>
                    <span class="txt-ok">我<b>没</b>有钱。(Tôi không có tiền.)</span>
                </div>
                <div class="b92-warn-item">
                    <span class="icon">⚠️</span>
                    <span>Trước 有 luôn dùng 没, không bao giờ dùng 不!</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br/>", unsafe_allow_html=True)
        st.markdown("### 💛 Mẹo nhớ siêu nhanh")
        st.markdown("""
        <div class="b92-tip-box">
            <div class="b92-tip-title">🧠 Hai câu thần chú để không bao giờ nhầm:</div>
            <div class="b92-tip-row">
                <div class="b92-tip-char bu">不</div>
                <div class="b92-tip-text">
                    <span class="b92-tip-keyword">= "Không muốn / Không thích / Không phải"</span><br/>
                    Dùng khi bạn <b>lắc đầu vì ý chí</b>: "Tôi quyết định không", "Thường thì không", "Không phải vậy".<br/>
                    → Mang màu sắc <b>chủ quan</b> của người nói.
                </div>
            </div>
            <div class="b92-tip-row">
                <div class="b92-tip-char mei">没</div>
                <div class="b92-tip-text">
                    <span class="b92-tip-keyword">= "Chưa làm / Không có / Đã không xảy ra"</span><br/>
                    Dùng khi nói về <b>sự thật đã/chưa xảy ra</b>: "Hôm qua không làm", "Hiện không có".<br/>
                    → Mang màu sắc <b>khách quan</b>, tường thuật thực tế.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br/>", unsafe_allow_html=True)
        st.markdown("### 📌 Bổ sung: Câu hỏi phủ định dạng 有没有")
        st.markdown("""
        Trong tiếng Trung, dạng câu hỏi **有没有...？** (yǒu méiyǒu) rất phổ biến — tương đương "Có ... không?":
        """)
        special_cases = [
            ("有没有问题？", "Yǒu méiyǒu wèntí?", "Có vấn đề gì không?"),
            ("有没有时间？", "Yǒu méiyǒu shíjiān?", "Có thời gian không?"),
            ("你去没去？",  "Nǐ qù méi qù?",      "Bạn có đi không? (hỏi về quá khứ)"),
        ]
        for han, py, vi in special_cases:
            st.markdown(f"""
            <div class="b92-example" style="margin-bottom:8px; border-radius:10px; padding:12px 16px;">
                <span class="han" style="font-size:1.2rem; font-weight:700;">{han}</span><br/>
                <span class="py">{py}</span><br/>
                <span class="vi">→ {vi}</span>
            </div>
            """, unsafe_allow_html=True)

    # ─────────────────────────────────────────────────────────────
    # TAB 5: QUIZ TƯƠNG TÁC
    # ─────────────────────────────────────────────────────────────
    with tab_quiz:
        st.markdown("### 🎮 Luyện tập: Chọn 不 hay 没?")
        st.caption("Điền vào chỗ trống: mỗi câu chọn 不 (bù) hoặc 没 (méi) cho đúng.")

        quiz_data = [
            {
                "q":       "我___是学生。",
                "py":      "Wǒ ___ shì xuésheng.",
                "vi":      "Tôi không phải là học sinh.",
                "options": ["不", "没"],
                "answer":  "不",
                "explain": "Phủ định 是 — dùng 不. (不是 = không phải)"
            },
            {
                "q":       "他昨天___来学校。",
                "py":      "Tā zuótiān ___ lái xuéxiào.",
                "vi":      "Anh ấy hôm qua không đến trường.",
                "options": ["不", "没"],
                "answer":  "没",
                "explain": "Hành động quá khứ không xảy ra — dùng 没."
            },
            {
                "q":       "她___有手机。",
                "py":      "Tā ___ yǒu shǒujī.",
                "vi":      "Cô ấy không có điện thoại.",
                "options": ["不", "没"],
                "answer":  "没",
                "explain": "Trước 有 luôn dùng 没."
            },
            {
                "q":       "这个菜___好吃。",
                "py":      "Zhège cài ___ hǎochī.",
                "vi":      "Món ăn này không ngon.",
                "options": ["不", "没"],
                "answer":  "不",
                "explain": "Phủ định tính từ 好吃 — dùng 不."
            },
            {
                "q":       "我___喜欢喝咖啡。",
                "py":      "Wǒ ___ xǐhuān hē kāfēi.",
                "vi":      "Tôi không thích uống cà phê.",
                "options": ["不", "没"],
                "answer":  "不",
                "explain": "Phủ định 喜欢 (cảm xúc, thói quen) — dùng 不."
            },
            {
                "q":       "他们___吃早饭。",
                "py":      "Tāmen ___ chī zǎofàn.",
                "vi":      "Họ chưa ăn sáng (sáng nay).",
                "options": ["不", "没"],
                "answer":  "没",
                "explain": "Hành động chưa xảy ra lần này — dùng 没."
            },
            {
                "q":       "我___看这部电影。",
                "py":      "Wǒ ___ kàn zhè bù diànyǐng.",
                "vi":      "Tôi chưa xem bộ phim này.",
                "options": ["不", "没"],
                "answer":  "没",
                "explain": "Hành động chưa từng xảy ra — dùng 没."
            },
            {
                "q":       "她___想去。",
                "py":      "Tā ___ xiǎng qù.",
                "vi":      "Cô ấy không muốn đi.",
                "options": ["不", "没"],
                "answer":  "不",
                "explain": "Phủ định ý chí 想 — dùng 不."
            },
            {
                "q":       "这里___有椅子。",
                "py":      "Zhèlǐ ___ yǒu yǐzi.",
                "vi":      "Ở đây không có ghế.",
                "options": ["不", "没"],
                "answer":  "没",
                "explain": "Phủ định sự tồn tại 有 — dùng 没."
            },
            {
                "q":       "明天我___上班。",
                "py":      "Míngtiān wǒ ___ shàngbān.",
                "vi":      "Ngày mai tôi không đi làm.",
                "options": ["不", "没"],
                "answer":  "不",
                "explain": "Tương lai, ý định không làm — dùng 不."
            },
        ]

        if "b92_answers" not in st.session_state:
            st.session_state.b92_answers = {}
        if "b92_submitted" not in st.session_state:
            st.session_state.b92_submitted = False

        for i, q in enumerate(quiz_data):
            key = f"b92_q{i}"
            ans_key = f"b92_a{i}"

            result_html = ""
            if st.session_state.b92_submitted and ans_key in st.session_state.b92_answers:
                user_ans = st.session_state.b92_answers[ans_key]
                if user_ans == q["answer"]:
                    result_html = f'<span style="color:#16a34a;font-weight:700;font-size:0.9rem;">✅ Đúng! — {q["explain"]}</span>'
                else:
                    result_html = f'<span style="color:#dc2626;font-weight:700;font-size:0.9rem;">❌ Sai — Đáp án đúng: <b>{q["answer"]}</b>. {q["explain"]}</span>'

            st.markdown(f"""
            <div class="b92-quiz-card">
                <div class="b92-quiz-q">Câu {i+1}: {q['q']}</div>
                <div class="b92-quiz-py">{q['py']}</div>
                <div class="b92-quiz-vi">→ {q['vi']}</div>
            </div>
            """, unsafe_allow_html=True)

            chosen = st.radio(
                f"Câu {i+1}:",
                options=q["options"],
                key=key,
                horizontal=True,
                label_visibility="collapsed"
            )
            st.session_state.b92_answers[ans_key] = chosen

            if result_html:
                st.markdown(result_html, unsafe_allow_html=True)
            st.markdown("---")

        col_btn, col_reset = st.columns([2, 1])
        with col_btn:
            if st.button("✅ Nộp bài & Xem kết quả", use_container_width=True, type="primary"):
                st.session_state.b92_submitted = True
                st.rerun()
        with col_reset:
            if st.button("🔄 Làm lại", use_container_width=True):
                st.session_state.b92_submitted = False
                st.session_state.b92_answers = {}
                for i in range(len(quiz_data)):
                    key = f"b92_q{i}"
                    if key in st.session_state:
                        del st.session_state[key]
                st.rerun()

        if st.session_state.b92_submitted:
            correct = sum(
                1 for i, q in enumerate(quiz_data)
                if st.session_state.b92_answers.get(f"b92_a{i}") == q["answer"]
            )
            total = len(quiz_data)
            pct = int(correct / total * 100)
            if pct == 100:
                msg = "🏆 Xuất sắc! Bạn đã nắm vững 不 và 没!"
                color = "#166534"
            elif pct >= 70:
                msg = "👍 Khá tốt! Ôn lại các câu sai nhé."
                color = "#1e40af"
            else:
                msg = "📖 Hãy xem lại phần Lý thuyết và thử lại!"
                color = "#9f1239"

            st.markdown(f"""
            <div class="b92-score-box">
                <div class="b92-score-num">{correct}/{total}</div>
                <div class="b92-score-label">{pct}% chính xác</div>
                <div style="margin-top:10px; font-size:1.1rem; font-weight:700; color:{color if pct<100 else '#fbbf24'};">
                    {msg}
                </div>
            </div>
            """, unsafe_allow_html=True)


# Force reload
