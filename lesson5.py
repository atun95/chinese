import streamlit as st
import random
from ui_utils import render_lesson_intro, render_play_button

NUMBERS_DATA = [
    {
        "digit": "0",
        "hanzi": "零",
        "pinyin": "líng",
        "vietnamese": "Không",
        "read_guide": "Linh",
        "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/0_in_Chinese_charactar.svg/320px-0_in_Chinese_charactar.svg.png",
        "desc": "Thường được viết tắt là 〇 trong các tài liệu hoặc số điện thoại."
    },
    {
        "digit": "1",
        "hanzi": "一",
        "pinyin": "yī",
        "vietnamese": "Một",
        "read_guide": "Y / I",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Eins.jpg",
        "desc": "Cử chỉ tay: Chỉ duy nhất ngón trỏ lên."
    },
    {
        "digit": "2",
        "hanzi": "二",
        "pinyin": "èr",
        "vietnamese": "Hai",
        "read_guide": "Ơ-r (uốn lưỡi)",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Zwei.jpg",
        "desc": "Cử chỉ tay: Giơ ngón trỏ và ngón giữa (như hình chữ V)."
    },
    {
        "digit": "3",
        "hanzi": "三",
        "pinyin": "sān",
        "vietnamese": "Ba",
        "read_guide": "San",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Drei.jpg",
        "desc": "Cử chỉ tay: Giơ ngón trỏ, ngón giữa và ngón áp út."
    },
    {
        "digit": "4",
        "hanzi": "四",
        "pinyin": "sì",
        "vietnamese": "Bốn",
        "read_guide": "Sư (thanh 4, dứt khoát)",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Vier.jpg",
        "desc": "Cử chỉ tay: Giơ 4 ngón tay từ ngón trỏ đến ngón út."
    },
    {
        "digit": "5",
        "hanzi": "五",
        "pinyin": "wǔ",
        "vietnamese": "Năm",
        "read_guide": "Ủ (xuống giọng và lên giọng)",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Fuenf.jpg",
        "desc": "Cử chỉ tay: Xòe cả 5 ngón tay."
    },
    {
        "digit": "6",
        "hanzi": "六",
        "pinyin": "liù",
        "vietnamese": "Sáu",
        "read_guide": "Liêu (thanh 4)",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Sechs.jpg",
        "desc": "Cử chỉ tay: Giơ ngón cái và ngón út (giống biểu tượng điện thoại)."
    },
    {
        "digit": "7",
        "hanzi": "七",
        "pinyin": "qī",
        "vietnamese": "Bảy",
        "read_guide": "Chi (âm gió bật hơi nhẹ)",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Sieben.jpg",
        "desc": "Cử chỉ tay: Chụm ngón cái, ngón trỏ và ngón giữa lại với nhau."
    },
    {
        "digit": "8",
        "hanzi": "八",
        "pinyin": "bā",
        "vietnamese": "Tám",
        "read_guide": "Pa (không bật hơi)",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Acht.jpg",
        "desc": "Cử chỉ tay: Giơ ngón cái và ngón trỏ (giống hình khẩu súng chĩa xuống)."
    },
    {
        "digit": "9",
        "hanzi": "九",
        "pinyin": "jiǔ",
        "vietnamese": "Chín",
        "read_guide": "Chiểu (thanh 3)",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Neun.jpg",
        "desc": "Cử chỉ tay: Cong ngón trỏ thành hình cái móc, các ngón khác nắm lại."
    },
    {
        "digit": "10",
        "hanzi": "十",
        "pinyin": "shí",
        "vietnamese": "Mười",
        "read_guide": "Sứ (uốn lưỡi)",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Zehn.jpg",
        "desc": "Cử chỉ tay: Đan chéo ngón trỏ của hai tay thành hình chữ thập 十 (hoặc nắm tay lại)."
    }
]

def show_lesson5_numbers():
    render_lesson_intro("🔢 Bài 5.1: Số đếm từ 0 đến 10", "Học phát âm, chữ Hán và cử chỉ ngón tay đếm số của người Trung Quốc.")
    
    st.markdown("""
    <style>
    .number-card {
        background: white;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        border: 1px solid #e2e8f0;
        text-align: center;
        margin-bottom: 20px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .number-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
        border-color: #3b82f6;
    }
    .number-digit {
        font-size: 2.2rem;
        font-weight: bold;
        color: #2563eb;
    }
    .number-hanzi {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1e293b;
        margin: 5px 0;
    }
    .number-pinyin {
        font-family: monospace;
        font-size: 1.15rem;
        color: #4b5563;
        font-weight: bold;
    }
    .number-vietnamese {
        font-size: 0.95rem;
        color: #6b7280;
        font-style: italic;
    }
    .number-desc {
        font-size: 0.82rem;
        color: #4b5563;
        margin-top: 10px;
        min-height: 48px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Grid of numbers (2 rows of 6 columns to fit 0 to 10 beautifully)
    for row_idx in range(2):
        cols = st.columns(6)
        for col_idx in range(6):
            idx = row_idx * 6 + col_idx
            if idx < len(NUMBERS_DATA):
                item = NUMBERS_DATA[idx]
                with cols[col_idx]:
                    st.markdown(f"""
                    <div class="number-card">
                        <div class="number-digit">{item['digit']}</div>
                        <div class="number-hanzi">{item['hanzi']}</div>
                        <div class="number-pinyin">{item['pinyin']}</div>
                        <div class="number-vietnamese">{item['vietnamese']} ({item['read_guide']})</div>
                        <div style="margin: 12px 0; display: flex; justify-content: center; align-items: center; height: 110px;">
                            <img src="{item['img_url']}" style="max-width: 100%; max-height: 110px; object-fit: contain; border-radius: 8px; border: 1px solid #f1f5f9;"/>
                        </div>
                        <div class="number-desc">{item['desc']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    render_play_button(item['hanzi'], "🔊 Phát âm", key=f"play_num_{item['digit']}")
                    
    st.markdown("---")
    st.subheader("🎯 Thử thách Phản xạ Số đếm")
    st.write("Giáo viên nhấn nút **Tạo số ngẫu nhiên** để yêu cầu học viên phản xạ nhanh cách phát âm, chữ Hán hoặc làm ký hiệu tay tương ứng.")
    
    if st.button("🎲 TẠO SỐ NGẪU NHIÊN", type="primary", use_container_width=True, key="btn_rand_number"):
        st.session_state.rand_num = random.choice(NUMBERS_DATA)
        st.rerun()
            
    if "rand_num" in st.session_state and st.session_state.rand_num:
        num = st.session_state.rand_num
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: white; border-radius: 12px; padding: 25px; text-align: center; margin-top: 15px;'>
            <div style='font-size: 1.1em; text-transform: uppercase; letter-spacing: 1px; opacity: 0.8;'>Số cần phản xạ:</div>
            <div style='font-size: 5.5em; font-weight: bold; color: #fbbf24; margin: 10px 0;'>{num['digit']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("👁️ Xem đáp án Chữ Hán & Ký hiệu tay"):
            st.markdown(f"""
            <div style='text-align: center; margin-top: 10px; margin-bottom: 20px;'>
                <h3 style='margin: 0; color: #0f172a;'>Chữ Hán: <span style='font-size: 1.6em; font-weight: bold;'>{num['hanzi']}</span></h3>
                <p style='font-size: 1.25em; font-family: monospace; font-weight: bold; color: #2563eb; margin: 5px 0;'>Bính âm: {num['pinyin']}</p>
                <p style='font-size: 1.15em; font-style: italic; color: #4b5563; margin: 0;'>Nghĩa: {num['vietnamese']} ({num['read_guide']})</p>
            </div>
            """, unsafe_allow_html=True)
            
            col_img_left, col_img_center, col_img_right = st.columns([1, 2, 1])
            with col_img_center:
                st.image(num['img_url'], caption=f"Ký hiệu tay cho số {num['digit']}", use_container_width=True)
            render_play_button(num['hanzi'], "🔊 Phát âm", key="play_rand_num_challenge_inside")
