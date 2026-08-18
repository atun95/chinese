with open('c:/Users/lyquo/OneDrive/Desktop/chinese/lessons/lesson9.py', 'a', encoding='utf-8') as f:
    f.write('''
from lessons_data import B9_1_PRACTICE_DATA
import random

def show_lesson9_1_classroom_practice():
    st.markdown(\"\"\"
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
    \"\"\", unsafe_allow_html=True)

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
                st.markdown(f\"\"\"
                <div class='{bubble_class}'>
                    <span class='speaker-name' style='color: {speaker_color};'>{line['speaker']}:</span>
                    <span class='hanzi-text'>{line['han']}</span><br/>
                    <span class='pinyin-text' style='margin-left: 25px;'>{line['py']}</span><br/>
                    <span style='color: #64748b; font-style: italic; margin-left: 25px;'>Dịch: {line['vi']}</span>
                </div>
                \"\"\", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

    with tab_activities:
        st.subheader("Hoạt động tương tác (Interactive Games)")
        
        act1_col, act2_col = st.columns(2)
        with act1_col:
            st.markdown(\"\"\"
            <div class='practice-card' style='border-top: 5px solid #f59e0b;'>
                <h4 style='color: #d97706;'>🎲 Hoạt động 1: Vòng quay Quốc tịch</h4>
                <p><b>Luật chơi:</b> Random ra 1 quốc gia. Học viên A hỏi quốc tịch, Học viên B đóng vai người nước đó để trả lời.</p>
                <p>A: 你是哪国人？<br/>B: 我是...</p>
            </div>
            \"\"\", unsafe_allow_html=True)
            
            if st.button("🎲 Random Quốc gia"):
                countries = ["中国 (Trung Quốc)", "越南 (Việt Nam)", "美国 (Mỹ)", "英国 (Anh)", "法国 (Pháp)", "日本 (Nhật Bản)", "韩国 (Hàn Quốc)"]
                selected = random.choice(countries)
                st.success(f"🎯 Đóng vai người nước: **{selected}**")

        with act2_col:
            st.markdown(\"\"\"
            <div class='practice-card' style='border-top: 5px solid #8b5cf6;'>
                <h4 style='color: #7c3aed;'>💱 Hoạt động 2: Quầy Thu ngân</h4>
                <p><b>Luật chơi:</b> Random ra mức giá và loại tiền tệ. Học viên A báo giá, Học viên B trả giá/hỏi thăm.</p>
                <p>A: 这个... (giá tiền)<br/>B: 那个是... 吗？</p>
            </div>
            \"\"\", unsafe_allow_html=True)
            
            if st.button("💱 Random Giá Tiền"):
                currencies = ["100 人民币 (100 NDT)", "50 美元 (50 Đô la)", "20 欧元 (20 Euro)", "1000 日元 (1000 Yên)", "10 英镑 (10 Bảng Anh)"]
                selected = random.choice(currencies)
                st.info(f"🏷️ Mức giá: **{selected}**")
''')
