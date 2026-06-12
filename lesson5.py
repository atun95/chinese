import streamlit as st
import random
import base64
import os
from ui_utils import render_lesson_intro, render_play_button

def get_image_src(img_path_or_url):
    if img_path_or_url.startswith("http"):
        return img_path_or_url
    try:
        if os.path.exists(img_path_or_url):
            ext = os.path.splitext(img_path_or_url)[1].lower()
            mime = "image/jpeg"
            if ext == ".png":
                mime = "image/png"
            elif ext == ".webp":
                mime = "image/webp"
            with open(img_path_or_url, "rb") as f:
                encoded = base64.b64encode(f.read()).decode("utf-8")
                return f"data:{mime};base64,{encoded}"
    except Exception:
        pass
    return img_path_or_url

NUMBERS_DATA = [
    {
        "digit": "0",
        "hanzi": "零",
        "pinyin": "líng",
        "img_url": "assets/0.jpg",
    },
    {
        "digit": "1",
        "hanzi": "一",
        "pinyin": "yī",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Eins.jpg",
    },
    {
        "digit": "2",
        "hanzi": "二",
        "pinyin": "èr",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Zwei.jpg",
    },
    {
        "digit": "3",
        "hanzi": "三",
        "pinyin": "sān",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Drei.jpg",
    },
    {
        "digit": "4",
        "hanzi": "四",
        "pinyin": "sì",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Vier.jpg",
    },
    {
        "digit": "5",
        "hanzi": "五",
        "pinyin": "wǔ",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Fuenf.jpg",
    },
    {
        "digit": "6",
        "hanzi": "六",
        "pinyin": "liù",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Sechs.jpg",
    },
    {
        "digit": "7",
        "hanzi": "七",
        "pinyin": "qī",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Sieben.jpg",
    },
    {
        "digit": "8",
        "hanzi": "八",
        "pinyin": "bā",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Acht.jpg",
    },
    {
        "digit": "9",
        "hanzi": "九",
        "pinyin": "jiǔ",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Neun.jpg",
    },
    {
        "digit": "10",
        "hanzi": "十",
        "pinyin": "shí",
        "img_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinesische.Zahl.Zehn.jpg",
    }
]

LARGE_NUMBERS_DATA = [
    {"digit": "100", "hanzi": "一百", "pinyin": "yī bǎi", "meaning": "Một trăm"},
    {"digit": "1.000", "hanzi": "一千", "pinyin": "yī qiān", "meaning": "Một nghìn"},
    {"digit": "10.000", "hanzi": "一万", "pinyin": "yī wàn", "meaning": "Mười nghìn (1 vạn)"},
    {"digit": "100.000", "hanzi": "十万", "pinyin": "shí wàn", "meaning": "Một trăm nghìn (10 vạn)"},
    {"digit": "1.000.000", "hanzi": "一百万", "pinyin": "yī bǎi wàn", "meaning": "Một triệu"},
    {"digit": "10.000.000", "hanzi": "一千万", "pinyin": "yī qiān wàn", "meaning": "Mười triệu"},
    {"digit": "100.000.000", "hanzi": "一亿", "pinyin": "yī yì", "meaning": "Một trăm triệu"},
    {"digit": "1.000.000.000", "hanzi": "十亿", "pinyin": "shí yì", "meaning": "Một tỷ"}
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
                        <div style="margin: 12px 0; display: flex; justify-content: center; align-items: center; height: 110px;">
                            <img src="{get_image_src(item['img_url'])}" style="max-width: 100%; max-height: 110px; object-fit: contain; border-radius: 8px; border: 1px solid #f1f5f9;"/>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    render_play_button(item['hanzi'], "🔊 Phát âm", key=f"play_num_{item['digit']}")
                    
    # --- LARGE NUMBERS EXTENSION ---
    st.markdown("---")
    st.subheader("📊 Mở rộng: Các đơn vị số lớn")
    st.write("Cách đọc và đơn vị đếm các số hàng trăm, hàng nghìn, hàng triệu, hàng tỷ:")
    
    for row_idx in range(2):
        cols_large = st.columns(4)
        for col_idx in range(4):
            idx = row_idx * 4 + col_idx
            if idx < len(LARGE_NUMBERS_DATA):
                item = LARGE_NUMBERS_DATA[idx]
                with cols_large[col_idx]:
                    st.markdown(f"""
                    <div class="number-card" style="min-height: 180px; display: flex; flex-direction: column; justify-content: space-between; padding: 12px; margin-bottom: 15px;">
                        <div>
                            <div class="number-digit" style="font-size: 1.3rem; color: #0284c7;">{item['digit']}</div>
                            <div class="number-hanzi" style="font-size: 2.0rem; margin: 5px 0;">{item['hanzi']}</div>
                            <div class="number-pinyin" style="font-size: 1.05rem; color: #4b5563; font-weight: bold;">{item['pinyin']}</div>
                        </div>
                        <div style="font-size: 0.9rem; font-weight: bold; color: #059669; margin-top: 8px; font-style: italic;">{item['meaning']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    render_play_button(item['hanzi'], "🔊 Phát âm", key=f"play_large_{idx}")

    # --- TONE SANDHI OF YI COMPARISON TABLE ---
    st.markdown("""
    <div style="background-color: #f8fafc; border-left: 5px solid #2563eb; padding: 20px; border-radius: 8px; margin-top: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0;">
        <h4 style="color: #1e3a8a; margin-top: 0; margin-bottom: 12px; display: flex; align-items: center; gap: 8px; font-size: 1.15rem; font-weight: bold;">
            💡 Quy tắc Biến điệu của chữ "一" (yī)
        </h4>
        <p style="font-size: 0.95em; line-height: 1.6; color: #334155; margin-bottom: 15px;">
            Chữ <b>一 (yī)</b> có phiên âm gốc là thanh 1 (yī) khi đứng một mình hoặc đếm số thứ tự. Tuy nhiên, khi đi kèm với các từ chỉ đơn vị (lượng từ) phía sau, âm điệu của nó sẽ thay đổi tùy thuộc vào thanh điệu của từ tiếp theo:
        </p>
        <table style="width: 100%; border-collapse: collapse; font-size: 0.95em; text-align: left;">
            <thead>
                <tr style="background-color: #eff6ff; border-bottom: 2px solid #bfdbfe;">
                    <th style="padding: 10px; color: #1e40af; font-weight: bold;">Quy tắc biến điệu</th>
                    <th style="padding: 10px; color: #1e40af; font-weight: bold;">Cách đọc thực tế</th>
                    <th style="padding: 10px; color: #1e40af; font-weight: bold;">Ví dụ minh họa</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                    <td style="padding: 10px; font-weight: bold; color: #0f172a;">
                        Giữ nguyên <span style="color: #2563eb;">yī</span> (Thanh 1)
                    </td>
                    <td style="padding: 10px;">Khi đứng một mình, ở cuối từ, hoặc khi đọc số thứ tự từng số.</td>
                    <td style="padding: 10px; font-family: monospace;"><b>十一</b> (shíyī)<br><b>第一</b> (dì-yī)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                    <td style="padding: 10px; font-weight: bold; color: #b45309;">
                        Đổi thành <span style="color: #d97706;">yì</span> (Thanh 4)
                    </td>
                    <td style="padding: 10px;">Khi đứng trước âm tiết mang <b>Thanh 1, Thanh 2, Thanh 3</b>.</td>
                    <td style="padding: 10px; font-family: monospace;">
                        <b>一百</b> (yī + bǎi [thanh 3] &rarr; <span style="color: #d97706; font-weight:bold;">yì</span>bǎi)<br>
                        <b>一千</b> (yī + qiān [thanh 1] &rarr; <span style="color: #d97706; font-weight:bold;">yì</span>qiān)<br>
                        <b>一百万</b> (yī + bǎi &rarr; <span style="color: #d97706; font-weight:bold;">yì</span>bǎiwàn)
                    </td>
                </tr>
                <tr>
                    <td style="padding: 10px; font-weight: bold; color: #047857;">
                        Đổi thành <span style="color: #059669;">yí</span> (Thanh 2)
                    </td>
                    <td style="padding: 10px;">Khi đứng trước âm tiết mang <b>Thanh 4</b>.</td>
                    <td style="padding: 10px; font-family: monospace;">
                        <b>一万</b> (yī + wàn [thanh 4] &rarr; <span style="color: #059669; font-weight:bold;">yí</span>wàn)<br>
                        <b>一亿</b> (yī + yì [thanh 4] &rarr; <span style="color: #059669; font-weight:bold;">yí</span>yì)
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)
                    
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
            </div>
            """, unsafe_allow_html=True)
            
            col_img_left, col_img_center, col_img_right = st.columns([1, 2, 1])
            with col_img_center:
                st.image(num['img_url'], caption=f"Ký hiệu tay cho số {num['digit']}", use_container_width=True)
            render_play_button(num['hanzi'], "🔊 Phát âm", key=f"play_rand_num_{num['digit']}")
