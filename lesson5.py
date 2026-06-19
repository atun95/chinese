import streamlit as st
import random
import base64
import os
from datetime import datetime, timezone, timedelta
from ui_utils import render_lesson_intro, render_play_button, shuffled_options
from lessons_data import B5_NASAL_FINALS_DATA, B5_QUIZ_VOCAB, B5_QUIZ_LISTENING, B5_QUIZ_FILL_BLANKS

def get_nasal_audio(syllable):
    if syllable == "ēng":
        try:
            current_file = os.path.abspath(__file__)
            with open(current_file, "r", encoding="utf-8") as f:
                content = f.read()
                import re
                m = re.search(r'"play_p2":\s*"(data:audio/mp3;base64,[^"]+)"', content)
                if m:
                    return m.group(1)
        except Exception:
            pass
    return syllable

try:
    from lessons_data import B5_3_ADVERBS_DATA, B5_3_QUIZ
except ImportError:
    B5_3_ADVERBS_DATA = [
        {
            "adv": "很",
            "pinyin": "hěn",
            "level": "Rất (Mức độ thông thường, mang tính liên kết ngữ pháp)",
            "formula": "S + 很 + Adj",
            "example_han": "我很忙",
            "example_py": "Wǒ hěn máng",
            "meaning": "Tôi rất bận",
            "desc": "Trong câu khẳng định với tính từ làm vị ngữ (S + Adj), '很' đóng vai trò liên kết ngữ pháp bắt buộc. Nếu thiếu '很', câu sẽ mang nghĩa so sánh ngầm (ví dụ: 'Tôi bận, người khác rảnh') hoặc nghe không tự nhiên, lửng lơ."
        },
        {
            "adv": "非常",
            "pinyin": "fēicháng",
            "level": "Vô cùng, cực kỳ (Mức độ cao hơn 'hěn/很')",
            "formula": "S + 非常 + Adj",
            "example_han": "她非常漂亮",
            "example_py": "Tā fēicháng piàoliang",
            "meaning": "Cô ấy vô cùng xinh đẹp",
            "desc": "Dùng để nhấn mạnh mức độ vượt trội của tính từ."
        },
        {
            "adv": "太 ... 了",
            "pinyin": "tài ... le",
            "level": "Quá, lắm (Mức độ cao, biểu thị cảm thán)",
            "formula": "S + 太 + Adj + 了",
            "example_han": "今天太热了",
            "example_py": "Jīntiān tài rè le",
            "meaning": "Hôm nay nóng quá rồi",
            "desc": "Thường dùng trong câu cảm thán. Có thể dùng cho cả nghĩa tích cực (tốt quá) và tiêu cực (nóng quá)."
        },
        {
            "adv": "特别",
            "pinyin": "tèbié",
            "level": "Đặc biệt (Nhấn mạnh sự khác biệt so với bình thường)",
            "formula": "S + 特別 + Adj",
            "example_han": "汉语特别有趣",
            "example_py": "Hànyǔ tèbié yǒuqù",
            "meaning": "Tiếng Trung đặc biệt thú vị",
            "desc": "Diễn tả mức độ nổi bật, có nét riêng biệt."
        },
        {
            "adv": "挺 ... 的",
            "pinyin": "tǐng ... de",
            "level": "Khá là, tương đối (Khẩu ngữ sinh động)",
            "formula": "S + 挺 + Adj + 的",
            "example_han": "他挺好的",
            "example_py": "Tā tǐng hǎo de",
            "meaning": "Anh ấy khá là tốt",
            "desc": "Cấu trúc phổ biến trong văn nói, mang sắc thái nhẹ nhàng, thân thiện."
        },
        {
            "adv": "比较",
            "pinyin": "bǐjiào",
            "level": "Tương đối, khá (Mang tính so sánh ngầm)",
            "formula": "S + 比较 + Adj",
            "example_han": "汉语比较难",
            "example_py": "Hànyǔ bǐjiào nán",
            "meaning": "Tiếng Trung tương đối khó",
            "desc": "Dùng khi so sánh tương đối giữa các đối tượng."
        },
        {
            "adv": "极了",
            "pinyin": "jí le",
            "level": "Cực kỳ (Mức độ cực độ, đứng SAU tính từ)",
            "formula": "S + Adj + 极了",
            "example_han": "累极了",
            "example_py": "Lèi jíle",
            "meaning": "Mệt cực kỳ",
            "desc": "Khác với các phó từ khác, '极lự/极了' bắt buộc đứng sau tính từ mà nó bổ nghĩa."
        }
    ]

    B5_3_QUIZ = [
        {
            "q": "Câu nào sau đây diễn đạt đúng ngữ pháp và tự nhiên nhất cho câu 'Tôi bận'?",
            "choices": ["我忙 (Wǒ máng)", "我很忙 (Wǒ hěn máng)", "我不很忙 (Wǒ bù hěn máng)", "我太忙 (Wǒ tài máng)"],
            "answer": "我很忙 (Wǒ hěn máng)"
        },
        {
            "q": "Điền phó từ phù hợp vào chỗ trống để tạo câu cảm thán: '今天___热了！' (Hôm nay nóng quá rồi!)",
            "choices": ["hěn/很", "非常 (fēicháng)", "太 (tài)", "比较 (bǐjiào)"],
            "answer": "太 (tài)"
        },
        {
            "q": "Dịch câu 'Tôi mệt cực kỳ!' sang tiếng Trung sử dụng bổ ngữ mức độ '极了' (jíle):",
            "choices": ["我 cực mệt 了", "我 mệt 极lự 了", "我累极了 (Wǒ lèi jíle)", "我极了累 (Wǒ jíle lèi)"],
            "answer": "我累极了 (Wǒ lèi jíle)"
        },
        {
            "q": "Chọn câu phủ định đúng của '他很好' (Anh ấy rất tốt):",
            "choices": ["他狠不好 (Tā hěn bù hǎo)", "他不好 (Tā bù hǎo)", "他很不好 (Tā hěn bù hǎo)", "他太不好 (Tā tài bù hǎo)"],
            "answer": "他不好 (Tā bù hǎo)"
        },
        {
            "q": "Cấu trúc '挺 + Adj + 的' mang nghĩa là gì?",
            "choices": ["Không bận lắm", "Khá là, tương đối", "Quá, lắm", "Vô cùng, cực kỳ"],
            "answer": "Khá là, tương đối"
        }
    ]

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
                    
    # --- PHÂN BIỆT 二 (èr) VÀ 两 (liǎng) ---
    st.markdown("""
    <div style="background-color: #f0fdf4; border-left: 5px solid #10b981; padding: 20px; border-radius: 8px; margin-top: 25px; margin-bottom: 25px; border: 1px solid #d1fae5;">
        <h4 style="color: #065f46; margin-top: 0; margin-bottom: 12px; display: flex; align-items: center; gap: 8px; font-size: 1.15rem; font-weight: bold;">
            ⚖️ Phân biệt cách dùng số 2: 二 (èr) và 两 (liǎng)
        </h4>
        <p style="font-size: 0.95em; line-height: 1.6; color: #047857; margin-bottom: 15px;">
            Trong tiếng Trung, số <b>2</b> có hai cách biểu đạt là <b>二 (èr)</b> và <b>两 (liǎng)</b>. Việc lựa chọn từ nào phụ thuộc vào ngữ cảnh sử dụng:
        </p>
        <table style="width: 100%; border-collapse: collapse; font-size: 0.95em; text-align: left;">
            <thead>
                <tr style="background-color: #e6fbf1; border-bottom: 2px solid #a7f3d0;">
                    <th style="padding: 10px; color: #065f46; font-weight: bold; width: 25%;">Từ vựng</th>
                    <th style="padding: 10px; color: #065f46; font-weight: bold; width: 45%;">Quy tắc áp dụng</th>
                    <th style="padding: 10px; color: #065f46; font-weight: bold; width: 30%;">Ví dụ minh họa</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                    <td style="padding: 10px; font-weight: bold; color: #047857; font-size: 1.1em;">
                        二 (èr)
                    </td>
                    <td style="padding: 10px; color: #1e293b;">
                        • Đọc số đếm thuần túy (1, 2, 3...).<br>
                        • Số thứ tự, số phòng, số xe, số điện thoại.<br>
                        • Đứng ở hàng chục, hàng đơn vị.
                    </td>
                    <td style="padding: 10px; font-family: monospace; color: #047857;">
                        <b>一，二，三</b> (yī, èr, sān)<br>
                        <b>第二</b> (dì-èr: thứ hai)<br>
                        <b>十二</b> (shí'èr: 12)
                    </td>
                </tr>
                <tr>
                    <td style="padding: 10px; font-weight: bold; color: #b45309; font-size: 1.1em;">
                        两 (liǎng)
                    </td>
                    <td style="padding: 10px; color: #1e293b;">
                        • Đứng trước <b>lượng từ</b> để chỉ số lượng người/vật.<br>
                        • Đứng trước các đơn vị số lớn từ hàng trăm trở lên (trăm, nghìn, vạn, tỷ...).
                    </td>
                    <td style="padding: 10px; font-family: monospace; color: #b45309;">
                        <b>两个人</b> (liǎng gè rén: 2 người)<br>
                        <b>两个粽子</b> (liǎng gè zòngzi: 2 bánh ú)<br>
                        <b>两百</b> (liǎngbǎi: 200)
                    </td>
                </tr>
            </tbody>
        </table>
        <div style="background-color: #fffbeb; border: 1px solid #fef3c7; color: #92400e; padding: 10px; border-radius: 6px; margin-top: 15px; font-size: 0.9em; font-weight: 500;">
            ⚠️ <b>Cực kỳ quan trọng:</b> Tuyệt đối không nói <del>二个人 (èr gè rén)</del> mà bắt buộc phải dùng <b>两个人 (liǎng gè rén)</b>!
        </div>
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

def check_nasal_spelling_rule(initial, final, tone_idx):
    valid_combos = {
        "b": ["an", "ang", "en", "eng", "in", "ing"],
        "p": ["an", "ang", "en", "eng", "in", "ing"],
        "m": ["an", "ang", "en", "eng", "in", "ing"],
        "f": ["an", "ang", "en", "eng"],
        "d": ["an", "ang", "eng", "ing", "ong"],
        "t": ["an", "ang", "eng", "ing", "ong"],
        "n": ["an", "ang", "en", "eng", "in", "ing", "ong"],
        "l": ["an", "ang", "eng", "in", "ing", "ong"],
        "g": ["an", "ang", "en", "eng", "ong"],
        "k": ["an", "ang", "en", "eng", "ong"],
        "h": ["an", "ang", "en", "eng", "ong"],
        "j": ["in", "ing"],
        "q": ["in", "ing"],
        "x": ["in", "ing"],
        "zh": ["an", "ang", "en", "eng", "ong"],
        "ch": ["an", "ang", "en", "eng", "ong"],
        "sh": ["an", "ang", "en", "eng"],
        "r": ["an", "ang", "en", "eng", "ong"],
        "z": ["an", "ang", "en", "eng", "ong"],
        "c": ["an", "ang", "en", "eng", "ong"],
        "s": ["an", "ang", "en", "eng", "ong"],
        "(Không có)": ["an", "ang", "en", "eng", "in", "ing"]
    }
    
    init_key = initial if initial != "(Không có)" else "(Không có)"
    
    if final not in valid_combos.get(init_key, []):
        if initial == "(Không có)":
            if final == "ong":
                return None, "❌ Vận mẫu <b>ong</b> không đứng độc lập mà sẽ biến đổi thành <b>weng</b>!"
            return None, f"❌ Vận mẫu <b>{final}</b> không đứng độc lập trong tiếng Trung tiêu chuẩn!"
        return None, f"❌ Lỗi ghép âm: Thanh mẫu <b>{initial}</b> không thể đi cùng vận mẫu <b>{final}</b>!"
        
    spelled = ""
    if initial == "(Không có)":
        if final == "in":
            spelled = "yin"
        elif final == "ing":
            spelled = "ying"
        else:
            spelled = final
    else:
        spelled = f"{initial}{final}"
        
    if tone_idx == 0:
        return spelled, None
        
    tone_vowels = {
        'a': ['ā', 'á', 'ǎ', 'à'],
        'e': ['ē', 'é', 'ě', 'è'],
        'i': ['ī', 'í', 'ǐ', 'ì'],
        'o': ['ō', 'ó', 'ǒ', 'ò']
    }
    
    res = spelled
    if 'a' in res:
        res = res.replace('a', tone_vowels['a'][tone_idx - 1])
    elif 'o' in res:
        res = res.replace('o', tone_vowels['o'][tone_idx - 1])
    elif 'e' in res:
        res = res.replace('e', tone_vowels['e'][tone_idx - 1])
    elif 'i' in res:
        res = res.replace('i', tone_vowels['i'][tone_idx - 1])
        
    return res, None

def show_lesson5_nasal_finals(add_tones, save_progress, save_score_row_b5, load_all_scores_b5):
    render_lesson_intro("📚 Bài 5.2: Vận mẫu mũi (Nasal Finals)", "Học phát âm, phân biệt và thực hành ghép âm 7 vận mẫu mũi: an, ang, ong, en, eng, in, ing.")
    
    st.markdown(
        """
        <style>
        .final-card {
            border-radius: 12px; 
            padding: 22px; 
            margin-bottom: 20px; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.05); 
            border: 1px solid #e2e8f0; 
            transition: all 0.3s ease;
        }
        .final-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        }
        .rule-badge {
            background-color: #fffbeb;
            color: #451a03;
            border-radius: 8px;
            padding: 10px 14px;
            font-size: 0.9em;
            font-weight: 500;
            margin-top: 12px;
            margin-bottom: 5px;
            border: 1px solid #fef3c7;
            box-shadow: 0 2px 5px rgba(245, 158, 11, 0.05);
        }
        .spelling-highlight {
            background-color: #fef08a;
            color: #854d0e;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: bold;
            font-family: 'Courier New', monospace;
            border: 1px solid #fde047;
            margin: 0 2px;
            display: inline-block;
        }
        .final-letter {
            font-size: 2.2em;
            font-weight: bold;
            font-family: 'Courier New', monospace;
            line-height: 1;
        }
        .comparison-container {
            background-color: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    tab_theory, tab_diff, tab_arena, tab_exercises = st.tabs([
        "📚 Lý thuyết",
        "⚖️ Phân biệt",
        "🎲 Classroom",
        "📝 Bài tập"
    ])
    
    # --- TAB 1: THEORY ---
    with tab_theory:
        st.subheader("1. Chi tiết các vận mẫu mũi trong tiếng Trung")
        st.write("Vận mẫu mũi được chia làm 2 nhóm chính dựa vào phụ âm kết thúc: **Vận mẫu mũi trước (-n)** và **Vận mẫu mũi sau (-ng)**.")
        
        for group in B5_NASAL_FINALS_DATA:
            st.markdown(f"### 📌 {group['nhom']}")
            for idx, item in enumerate(group["items"]):
                cols = st.columns([3.5, 1.5])
                with cols[0]:
                    card_html = f"""
                    <div class="final-card" style="background: {item['color']}; border-left: 6px solid {item['border_color']};">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                            <span class="final-letter" style="color: {item['text_color']};">{item['chu']}</span>
                            <span style="background: white; border: 1px solid {item['border_color']}; color: {item['text_color']}; padding: 3px 10px; border-radius: 20px; font-size: 0.9em; font-weight: bold; font-family: 'Courier New', monospace;">/{item['chu']}/</span>
                        </div>
                        <div style="font-size: 1.05em; font-weight: bold; margin-bottom: 8px; color: #0f172a;">👉 Phát âm: {item['hdsd']}</div>
                        <p style="color: #334155; font-size: 0.95em; line-height: 1.5; margin-bottom: 8px;"><b>Cách đọc chi tiết:</b> {item['cach_doc_sau']}</p>
                        <div style="font-size: 0.92em; color: #475569; margin-bottom: 10px;">📣 <b>Âm tương đương:</b> {item['tuong_duong']}</div>
                        <div class="rule-badge" style="border-left: 5px solid {item['border_color']};">
                            ⚠️ <b>Quy tắc chính tả:</b> {item['luu_y']}
                        </div>
                        <div style="background: rgba(255,255,255,0.85); border-radius: 8px; padding: 12px; border: 1px solid #e2e8f0; margin-top: 12px;">
                            <span style="font-size: 0.8em; color: #64748b; font-weight: bold; text-transform: uppercase;">Ví dụ từ khóa chính:</span>
                            <div style="display: flex; align-items: baseline; gap: 8px; margin-top: 4px;">
                                <span style="font-size: 1.6em; font-weight: bold; color: #0f172a;">{item['vd_han']}</span>
                                <span style="font-family: 'Courier New', monospace; font-weight: bold; color: #2563eb; font-size: 1.1em;">{item['vd_py']}</span>
                                <span style="color: #475569; font-style: italic; font-size: 0.95em;">({item['vietnamese']})</span>
                            </div>
                        </div>
                    </div>
                    """
                    st.markdown(card_html, unsafe_allow_html=True)
                with cols[1]:
                    st.markdown("<br/>", unsafe_allow_html=True)
                    render_play_button(item["vd_py"], f"🔊 Phát âm từ khóa ({item['vd_py']})", key=f"btn_main_nasal_{item['chu']}_{idx}")
                    
                    st.markdown("<div style='font-size:0.8em; font-weight:bold; color:#64748b; margin-top:12px; margin-bottom:4px;'>LUYỆN TẬP ÂM KHÁC:</div>", unsafe_allow_html=True)
                    for s_idx, sub in enumerate(item["more_examples"]):
                        sub_key = f"btn_sub_nasal_{item['chu']}_{idx}_{s_idx}"
                        render_play_button(sub["py"], f"🔊 {sub['han']} ({sub['py']}): {sub['vi']}", key=sub_key)
                st.markdown("<br/>", unsafe_allow_html=True)

        # Quy tắc đặc biệt cho vận mẫu ong khi đứng một mình
        st.markdown("""
        <div style="background-color: #fffbeb; border-left: 6px solid #f59e0b; padding: 18px; border-radius: 12px; margin-top: 10px; margin-bottom: 25px;">
            <h4 style="color: #7c2d12; margin-top: 0; font-weight: bold; display: flex; align-items: center; gap: 8px;">💡 Quy tắc đặc biệt: Khi vận mẫu "ong" đứng một mình</h4>
            <p style="color: #7c2d12; font-size: 0.95em; line-height: 1.5; margin-bottom: 0;">
                Trong hệ thống Bính âm (Pinyin) tiêu chuẩn, vận mẫu <b>ong</b> không bao giờ đứng độc lập làm một âm tiết riêng biệt. 
                Khi một chữ Hán có phát âm này mà không có thanh mẫu đi kèm phía trước, nó sẽ được viết biến đổi thành <b>weng</b> (ví dụ: chữ <b>翁</b> - wēng - nghĩa là 'ông lão'). 
                <br/><i>*Lưu ý cho học viên: Khi viết độc lập, hãy nhớ đổi cách viết từ <b>ong</b> thành <b>weng</b> nhé!</i>
            </p>
        </div>
        """, unsafe_allow_html=True)
                
    # --- TAB 2: DIFFERENCE ---
    with tab_diff:
        st.subheader("2. So sánh và Phân biệt Âm Mũi Trước / Sau")
        st.write("Điểm khác biệt cốt lõi nằm ở vị trí đặt đầu lưỡi và luồng hơi thoát ra khi kết thúc âm:")
        
        st.markdown(
            """
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 25px;">
                <div style="background-color: #eff6ff; border: 1px solid #bfdbfe; padding: 18px; border-radius: 12px;">
                    <h4 style="color: #1e40af; margin-top: 0;">👄 Nhóm Mũi Trước (-n): an, en, in</h4>
                    <p style="font-size: 0.95em; line-height: 1.6; color: #1e3a8a;">
                        • <b>Đầu lưỡi chạm ngạc trên</b>: Khi kết thúc âm, đầu lưỡi của bạn bắt buộc phải nâng lên và chạm nhẹ vào phần nướu răng cửa hàm trên (khép âm lại bằng âm /n/).
                        <br/>• <b>Luồng khí</b>: Đi nhẹ nhàng qua cả miệng và mũi, miệng hơi khép lại vào cuối âm.
                        <br/>• <b>Mẹo cảm nhận</b>: Giống như bạn đang phát âm chữ 'n' trong tiếng Việt nhưng lưỡi giữ nguyên tư thế chạm hàm trên.
                    </p>
                </div>
                <div style="background-color: #ecfdf5; border: 1px solid #a7f3d0; padding: 18px; border-radius: 12px;">
                    <h4 style="color: #065f46; margin-top: 0;">👄 Nhóm Mũi Sau (-ng): ang, eng, ing, ong</h4>
                    <p style="font-size: 0.95em; line-height: 1.6; color: #064e3b;">
                        • <b>Gốc lưỡi thụt về sau</b>: Khi kết thúc âm, khoang miệng mở rộng, đầu lưỡi hạ thấp tự do (không chạm răng), gốc lưỡi nâng lên chạm ngạc mềm phía sau để chặn hơi.
                        <br/>• <b>Luồng khí</b>: Đi mạnh ra hốc mũi, tạo cảm giác âm vang ở phía sau hốc mũi và vòm họng.
                        <br/>• <b>Mẹo cảm nhận</b>: Miệng giữ nguyên tư thế mở vào lúc kết thúc âm, không khép môi hay nâng đầu lưỡi.
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("### 🔊 Luyện tập các cặp âm tương phản")
        st.write("Hãy nghe và lặp lại theo từng cặp để nhận biết rõ sự khác biệt của âm mũi trước và sau:")
        
        pairs = [
            {"label": "Cặp an / ang", "p1": "ān", "play_p1": "安", "example1": "fàn (饭 - cơm)", "sound1": "饭", "p2": "āng", "play_p2": "肮", "example2": "máng (忙 - bận)", "sound2": "忙"},
            {"label": "Cặp en / eng", "p1": "ēn", "play_p1": "恩", "example1": "hěn (很 - rất)", "sound1": "很", "p2": "ēng", "play_p2": "鞥", "example2": "péng (朋 - bạn bè)", "sound2": "朋"},
            {"label": "Cặp in / ing", "p1": "īn", "play_p1": "音", "example1": "nín (您 - ngài)", "sound1": "您", "p2": "īng", "play_p2": "英", "example2": "tīng (听 - nghe)", "sound2": "听"}
        ]
        
        for idx, pair in enumerate(pairs):
            st.markdown(f"#### ⚖️ {pair['label']}")
            col_l, col_r = st.columns(2)
            with col_l:
                st.info(f"👉 **Âm mũi trước (-n)**: /{pair['p1']}/")
                render_play_button(pair['play_p1'], f"🔊 Nghe âm /{pair['p1']}/", key=f"pair_v_l_{idx}")
                render_play_button(pair['sound1'], f"🔊 Từ ví dụ: {pair['example1']}", key=f"pair_ex_l_{idx}")
            with col_r:
                st.success(f"👉 **Âm mũi sau (-ng)**: /{pair['p2']}/")
                render_play_button(pair['play_p2'], f"🔊 Nghe âm /{pair['p2']}/", key=f"pair_v_r_{idx}")
                render_play_button(pair['sound2'], f"🔊 Từ ví dụ: {pair['example2']}", key=f"pair_ex_r_{idx}")
            st.markdown("<br/>", unsafe_allow_html=True)


    # --- TAB 4: ARENA ---
    with tab_arena:
        st.subheader("4. Hoạt động Lớp học (Classroom Arena)")
        tab_game1, tab_game2 = st.tabs(["🎲 Game 1: Phản xạ Âm Mũi", "🕵️ Game 2: Tìm lỗi chính tả"])
        
        with tab_game1:
            st.markdown("### 🎲 Thử thách Phản xạ Âm tiết chứa Vận mẫu mũi")
            st.write("Giáo viên hoặc học viên nhấn nút để tạo ngẫu nhiên một âm tiết mũi. Học viên được chọn cần đọc to và dịch nghĩa (nếu có).")
            
            student_list_raw = st.text_input("Danh sách học viên (cách nhau bằng dấu phẩy):", "Tiên, Vy, Trân, Thanh", key="nasal_students_input")
            students = [s.strip() for s in student_list_raw.split(",") if s.strip()]
            
            NASAL_REFLEX_POOL = [
                {"pinyin": "fàn", "hanzi": "饭", "meaning": "cơm"},
                {"pinyin": "hěn", "hanzi": "很", "meaning": "rất"},
                {"pinyin": "máng", "hanzi": "忙", "meaning": "bận"},
                {"pinyin": "nín", "hanzi": "您", "meaning": "ngài/ông/bà (kính trọng)"},
                {"pinyin": "péngyou", "hanzi": "朋", "meaning": "bạn bè"},
                {"pinyin": "tīng", "hanzi": "听", "meaning": "nghe"},
                {"pinyin": "hóng", "hanzi": "红", "meaning": "màu đỏ"},
                {"pinyin": "shān", "hanzi": "山", "meaning": "núi"},
                {"pinyin": "sān", "hanzi": "三", "meaning": "số ba"},
                {"pinyin": "kàn", "hanzi": "看", "meaning": "nhìn / xem"},
                {"pinyin": "rén", "hanzi": "人", "meaning": "người"},
                {"pinyin": "mén", "hanzi": "门", "meaning": "cánh cửa"},
                {"pinyin": "lěng", "hanzi": "冷", "meaning": "lạnh"},
                {"pinyin": "fēng", "hanzi": "风", "meaning": "gió"},
                {"pinyin": "píngguǒ", "hanzi": "苹果", "meaning": "quả táo"},
                {"pinyin": "dōng", "hanzi": "东", "meaning": "phía đông"}
            ]
            
            if "nasal_arena_item" not in st.session_state:
                st.session_state.nasal_arena_item = NASAL_REFLEX_POOL[0]
            if "nasal_arena_student" not in st.session_state:
                st.session_state.nasal_arena_student = "Học viên"
                
            if st.button("🎲 QUAY NGẪU NHIÊN", type="primary", use_container_width=True, key="btn_nasal_rand"):
                st.session_state.nasal_arena_item = random.choice(NASAL_REFLEX_POOL)
                if students:
                    st.session_state.nasal_arena_student = random.choice(students)
                else:
                    st.session_state.nasal_arena_student = "Học viên"
                st.rerun()
                
            item = st.session_state.nasal_arena_item
            
            st.markdown(
                f"""<div style="background: linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%); border: 2px solid #FCD34D; border-radius: 16px; padding: 30px; margin-top: 15px; text-align: center;">
                    <div style="font-size: 1.1em; color: #92400E; font-weight: bold; text-transform: uppercase;">🌟 Học viên được gọi:</div>
                    <div style="font-size: 2.8em; font-weight: 800; color: #D97706; margin: 10px 0;">👉 {st.session_state.nasal_arena_student} 👈</div>
                    <hr style="border: 0; border-top: 1px solid #FCD34D; margin: 20px 0;"/>
                    <div style="background: white; border-radius: 12px; padding: 18px; border: 1px solid #FCD34D; display: inline-block; min-width: 250px;">
                        <span style="font-size: 0.95em; font-weight: bold; color: #b45309; text-transform: uppercase;">Âm tiết cần phản xạ:</span>
                        <div style="font-size: 3.2em; font-weight: bold; color: #1e293b; font-family: 'Courier New', monospace; margin: 8px 0;">
                            {item['pinyin']}
                        </div>
                        <span style="color: #475569; font-size: 1em;">Chữ Hán: <b>{item['hanzi']}</b> &nbsp;|&nbsp; Nghĩa: <b>{item['meaning']}</b></span>
                    </div>
                </div>""",
                unsafe_allow_html=True
            )
            
            st.markdown("<br/>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                render_play_button(item['pinyin'], "🔊 Phát âm mẫu", key="nasal_arena_play")
            with col2:
                if st.button("🎉 Đọc chính xác! Thưởng điểm", use_container_width=True, key="nasal_arena_reward"):
                    st.balloons()
                    st.success(f"Cộng điểm thưởng cho bạn **{st.session_state.nasal_arena_student}**! 🏆")
                    
        with tab_game2:
            st.markdown("### 🕵️ Tìm lỗi chính tả Bính âm")
            
            imposter_questions = [
                {"title": "Thử thách 1: Vận mẫu 'in' đứng một mình không có thanh mẫu", "options": ["1. in", "2. yin", "3. ien"], "correct_idx": 1, "explain": "Quy tắc Pinyin: Vận mẫu 'in' khi đứng độc lập không có thanh mẫu phải được viết thêm chữ 'y' ở phía trước thành 'yin'."},
                {"title": "Thử thách 2: Vận mẫu 'ing' đứng một mình không có thanh mẫu", "options": ["1. ing", "2. ying", "3. ieng"], "correct_idx": 1, "explain": "Quy tắc Pinyin: Vận mẫu 'ing' khi đứng độc lập không có thanh mẫu phải được viết thêm chữ 'y' ở phía trước thành 'ying'."},
                {"title": "Thử thách 3: Vận mẫu 'ong' đứng độc lập không có thanh mẫu", "options": ["1. ong", "2. wong", "3. weng"], "correct_idx": 2, "explain": "Quy tắc Pinyin: Trong tiếng Trung tiêu chuẩn, không có âm tiết nào viết là 'ong' hay 'wong'. Khi đứng độc lập âm này được biểu diễn bằng dạng 'weng'."},
                {"title": "Thử thách 4: Thanh mẫu j kết hợp với vận mẫu 'in' mang thanh điệu 1", "options": ["1. jīin", "2. jyin", "3. jīn"], "correct_idx": 2, "explain": "Khi kết hợp với thanh mẫu, ta viết trực tiếp thanh mẫu đứng trước vận mẫu. j + in -> jin, thêm thanh 1 thành jīn."}
            ]
            
            if "nasal_imp_idx" not in st.session_state:
                st.session_state.nasal_imp_idx = 0
            if "nasal_imp_revealed" not in st.session_state:
                st.session_state.nasal_imp_revealed = False
            if "nasal_imp_selected" not in st.session_state:
                st.session_state.nasal_imp_selected = None
                
            q_idx = st.session_state.nasal_imp_idx
            q_data = imposter_questions[q_idx]
            
            st.markdown(f"#### {q_data['title']}")
            st.write("👇 Chọn đáp án viết **ĐÚNG CHÍNH TẢ**:")
            
            cols_imp = st.columns(3)
            for idx, opt in enumerate(q_data["options"]):
                word_text = opt.split('. ')[1]
                with cols_imp[idx]:
                    if st.session_state.nasal_imp_selected is None:
                        st.markdown(
                            f"""<div style="border: 2px solid #cbd5e1; background-color: #f8fafc; border-radius: 12px; padding: 20px; text-align: center; margin-bottom: 8px;">
                                <div style="font-size: 1.5em; font-weight: bold; color: #1e293b; font-family: 'Courier New', monospace;">{word_text}</div>
                            </div>""",
                            unsafe_allow_html=True
                        )
                        if st.button(f"Chọn {word_text}", use_container_width=True, key=f"nasal_imp_btn_{q_idx}_{idx}"):
                            st.session_state.nasal_imp_selected = idx
                            st.session_state.nasal_imp_revealed = True
                            st.rerun()
                    else:
                        if idx == q_data["correct_idx"]:
                            border_color = "#10B981"
                            bg_color = "#ECFDF5"
                            label = "✅ ĐÚNG"
                        elif idx == st.session_state.nasal_imp_selected:
                            border_color = "#EF4444"
                            bg_color = "#FEF2F2"
                            label = "❌ CHỌN SAI"
                        else:
                            border_color = "#cbd5e1"
                            bg_color = "#f8fafc"
                            label = "⚪ MẠO DANH"
                            
                        st.markdown(
                            f"""<div style="border: 2px solid {border_color}; background-color: {bg_color}; border-radius: 12px; padding: 20px; text-align: center; min-height: 100px;">
                                <span style="font-weight: bold; color: {border_color}; font-size: 0.8em; text-transform: uppercase;">{label}</span>
                                <div style="font-size: 1.5em; font-weight: bold; color: #1e293b; font-family: 'Courier New', monospace; margin-top: 5px;">{word_text}</div>
                            </div>""",
                            unsafe_allow_html=True
                        )
            
            st.markdown("<br/>", unsafe_allow_html=True)
            col_imp_act = st.columns(2)
            with col_imp_act[0]:
                if st.button("⏭️ Thử thách tiếp theo", use_container_width=True, key="nasal_next_imp"):
                    st.session_state.nasal_imp_idx = (q_idx + 1) % len(imposter_questions)
                    st.session_state.nasal_imp_selected = None
                    st.session_state.nasal_imp_revealed = False
                    st.rerun()
            with col_imp_act[1]:
                if st.button("🔄 Khởi động lại", use_container_width=True, key="nasal_reset_imp"):
                    st.session_state.nasal_imp_idx = 0
                    st.session_state.nasal_imp_selected = None
                    st.session_state.nasal_imp_revealed = False
                    st.rerun()
                    
            if st.session_state.nasal_imp_revealed:
                st.markdown(
                    f"""
                    <div style="background-color: #EFF6FF; border-left: 6px solid #3B82F6; border-radius: 10px; padding: 15px; margin-top: 15px;">
                        <b style="color: #1E40AF;">💡 Giải thích chính tả:</b><br/>
                        <span style="color: #1E3A8A; font-size: 0.95em;">{q_data['explain']}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # --- TAB 5: EXERCISES ---
    with tab_exercises:
        st.subheader("📝 5. Bài tập Luyện tập & Đánh giá")
        st.write("Hoàn thành các bài tập trắc nghiệm, nghe và điền từ dưới đây để tự kiểm tra kiến thức về vận mẫu mũi.")
        
        if "b5_current" not in st.session_state:
            st.session_state.b5_current = {}
            
        # 1. Vocab Quiz
        with st.expander("Bài tập 1: Trắc nghiệm Từ vựng", expanded=False):
            st.caption("Chọn nghĩa tiếng Việt chính xác của các phiên âm dưới đây:")
            score_b5_vcb = 0
            for idx, item in enumerate(B5_QUIZ_VOCAB):
                choices = shuffled_options(item["choices"], f"b5_vcb-{idx}")
                if choices[0] == item["answer"] and len(choices) > 1:
                    choices[0], choices[1] = choices[1], choices[0]
                selected = st.radio(f"Câu {idx+1}: Từ '{item['q']}' nghĩa là gì?", choices, index=0, key=f"b5_vcb_q_{idx}")
                if selected == item["answer"]:
                    score_b5_vcb += 1
            if st.button("Chấm điểm Bài tập 1", key="btn_b5_vcb"):
                st.session_state.b5_current["b5_vcb"] = (score_b5_vcb, len(B5_QUIZ_VOCAB))
                save_progress()
                st.success(f"Bạn đúng {score_b5_vcb}/{len(B5_QUIZ_VOCAB)} câu.")
                
        # 2. Listening Quiz
        with st.expander("Bài tập 2: Luyện nghe và Chọn Pinyin đúng", expanded=False):
            st.caption("Nghe phát âm từ hệ thống và chọn cách viết Pinyin đúng:")
            score_b5_ls = 0
            for idx, item in enumerate(B5_QUIZ_LISTENING):
                st.write(f"**Câu {idx+1}:** Nghe từ mẫu:")
                render_play_button(item['hanzi'], "🔊 Nghe phát âm mẫu", key=f"b5_listen_{idx}")
                choices = shuffled_options(item["choices"], f"b5_ls-{idx}")
                if choices[0] == item["answer"] and len(choices) > 1:
                    choices[0], choices[1] = choices[1], choices[0]
                selected = st.radio("Chọn phiên âm chính xác:", choices, index=0, key=f"b5_ls_q_{idx}")
                if selected == item["answer"]:
                    score_b5_ls += 1
            if st.button("Chấm điểm Bài tập 2", key="btn_b5_ls"):
                st.session_state.b5_current["b5_ls"] = (score_b5_ls, len(B5_QUIZ_LISTENING))
                save_progress()
                st.success(f"Bạn đúng {score_b5_ls}/{len(B5_QUIZ_LISTENING)} câu.")
                
        # 3. Fill Blanks Quiz
        with st.expander("Bài tập 3: Điền vận mẫu còn thiếu", expanded=False):
            st.caption("Điền phần vận mẫu mũi và thanh điệu thích hợp vào chỗ trống để tạo thành từ đúng:")
            score_b5_fill = 0
            opts = ["...", "àn", "án", "ǎn", "àn", "én", "én", "ěn", "èn", "ín", "ín", "ǐn", "ìn", "án", "áng", "ǎng", "àng", "éng", "ěng", "èng", "īng", "ǐng", "ìng", "óng", "ǒng", "òng"]
            opts = list(dict.fromkeys(opts))
            for idx, item in enumerate(B5_QUIZ_FILL_BLANKS):
                selected = st.selectbox(f"Câu {idx+1}: Điền vào '{item['q']}' nghĩa là '{item['meaning']}'", opts, index=0, key=f"b5_fill_q_{idx}")
                if selected == item["ans"]:
                    score_b5_fill += 1
            if st.button("Chấm điểm Bài tập 3", key="btn_b5_fill"):
                st.session_state.b5_current["b5_fill"] = (score_b5_fill, len(B5_QUIZ_FILL_BLANKS))
                save_progress()
                st.success(f"Bạn đúng {score_b5_fill}/{len(B5_QUIZ_FILL_BLANKS)} câu.")
                
        # --- TOTAL SUMMARY & SUBMISSION ---
        st.markdown("---")
        with st.expander("📊 Bảng điểm & Nộp bài tập Bài 5.2", expanded=True):
            cur = st.session_state.b5_current
            labels = {"b5_vcb": "BT1: Từ vựng", "b5_ls": "BT2: Luyện nghe", "b5_fill": "BT3: Điền âm"}
            missing = [labels[k] for k in labels.keys() if k not in cur]
            
            if missing:
                st.warning(f"Vui lòng hoàn thành và bấm chấm điểm các bài tập: {', '.join(missing)}")
            else:
                earned = sum(cur[k][0] for k in labels.keys())
                total = sum(cur[k][1] for k in labels.keys())
                score_10 = round((earned / total) * 10, 2)
                st.success(f"📈 Điểm tổng kết Bài 5.2: **{score_10} / 10**")
                for k, lbl in labels.items():
                    st.write(f"- {lbl}: {cur[k][0]} / {cur[k][1]}")
                    
                st.markdown("---")
                name = st.text_input("Tên học viên (Bài 5.2)", key="student_name_b5")
                if st.button("Nộp bài tập Bài 5.2", type="primary", use_container_width=True):
                    if name:
                        def fmt(k):
                            s = cur.get(k)
                            return f"{s[0]}/{s[1]}" if s else ""
                        row = {
                            "thời gian": datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S"),
                            "học viên": name,
                            "tổng điểm": score_10,
                            "BT1: Từ vựng": fmt("b5_vcb"),
                            "BT2: Nghe": fmt("b5_ls"),
                            "BT3: Điền âm": fmt("b5_fill")
                        }
                        if save_score_row_b5(row):
                            st.success("Đã lưu kết quả bài tập Bài 5.2 thành công!")
                            st.session_state.b5_current = {}
                            st.rerun()
                    else:
                        st.error("Vui lòng nhập tên học viên để nộp bài!")
                        
            all_scores = load_all_scores_b5()
            if all_scores:
                st.write("### 📜 Lịch sử nộp bài lớp học:")
                st.dataframe(all_scores, use_container_width=True)

def show_lesson5_nasal_spelling(add_tones):
    render_lesson_intro("📚 Bài 5: Luyện tập ghép âm Vận mẫu mũi", "Luyện tập ghép âm các thanh mẫu với 7 vận mẫu mũi (an, ang, en, eng, in, ing, ong).")
    
    B5_LUYEN_TAP_FINALS = ["an", "ang", "en", "eng", "in", "ing", "ong"]
    B5_LUYEN_TAP_ROWS = {
        "(Không có)": ["an", "ang", "en", "eng", "yin", "ying", "weng"],
        "b": ["ban", "bang", "ben", "beng", "bin", "bing", ""],
        "p": ["pan", "pang", "pen", "peng", "pin", "ping", ""],
        "m": ["man", "mang", "men", "meng", "min", "ming", ""],
        "f": ["fan", "fang", "fen", "feng", "", "", ""],
        "d": ["dan", "dang", "", "deng", "", "ding", "dong"],
        "t": ["tan", "tang", "", "teng", "", "ting", "tong"],
        "n": ["nan", "nang", "nen", "neng", "nin", "ning", "nong"],
        "l": ["lan", "lang", "", "leng", "lin", "ling", "long"],
        "g": ["gan", "gang", "gen", "geng", "", "", "gong"],
        "k": ["kan", "kang", "ken", "keng", "", "", "kong"],
        "h": ["han", "hang", "hen", "heng", "", "", "hong"],
        "j": ["", "", "", "", "jin", "jing", ""],
        "q": ["", "", "", "", "qin", "qing", ""],
        "x": ["", "", "", "", "xin", "xing", ""],
        "zh": ["zhan", "zhang", "zhen", "zheng", "", "", "zhong"],
        "ch": ["chan", "chang", "chen", "cheng", "", "", "chong"],
        "sh": ["shan", "shang", "shen", "sheng", "", "", ""],
        "r": ["ran", "rang", "ren", "reng", "", "", "rong"],
        "z": ["zan", "zang", "zen", "zeng", "", "", "zong"],
        "c": ["can", "cang", "cen", "ceng", "", "", "cong"],
        "s": ["san", "sang", "sen", "seng", "", "", "song"]
    }
    
    st.subheader("Bảng luyện tập ghép âm vận mẫu mũi (Bài 5)")
    h_cols = st.columns([1.5] + [1] * len(B5_LUYEN_TAP_FINALS))
    h_cols[0].markdown("**T/V**")
    for i, f in enumerate(B5_LUYEN_TAP_FINALS): h_cols[i+1].markdown(f"**{f}**")
    for init in B5_LUYEN_TAP_ROWS.keys():
        r_cols = st.columns([1.5] + [1] * len(B5_LUYEN_TAP_FINALS))
        r_cols[0].markdown(f"**{init}**")
        for i, combo in enumerate(B5_LUYEN_TAP_ROWS[init]):
            if combo:
                with r_cols[i+1]:
                    with st.popover(combo, use_container_width=True):
                        for t in add_tones(combo):
                            col_t, col_btn = st.columns([2, 1])
                            col_t.write(f"- {t}")
                            with col_btn:
                                render_play_button(get_nasal_audio(t), "🔊", key=f"btn_p_b5_{init}_{combo}_{t}", height=45)
            else:
                r_cols[i+1].write("")

def show_lesson5_nasal_exercises(save_progress, save_score_row_b5, load_all_scores_b5):
    st.subheader("📝 Bài tập Luyện tập & Đánh giá (Vận mẫu mũi)")
    st.write("Hoàn thành các bài tập trắc nghiệm, nghe và điền từ dưới đây để tự kiểm tra kiến thức về vận mẫu mũi.")
    
    if "b5_current" not in st.session_state:
        st.session_state.b5_current = {}
        
    # 1. Vocab Quiz
    with st.expander("Bài tập 1: Trắc nghiệm Từ vựng", expanded=False):
        st.caption("Chọn nghĩa tiếng Việt chính xác của các phiên âm dưới đây:")
        score_b5_vcb = 0
        for idx, item in enumerate(B5_QUIZ_VOCAB):
            choices = shuffled_options(item["choices"], f"b5_vcb_standalone-{idx}")
            if choices[0] == item["answer"] and len(choices) > 1:
                choices[0], choices[1] = choices[1], choices[0]
            selected = st.radio(f"Câu {idx+1}: Từ '{item['q']}' nghĩa là gì?", choices, index=0, key=f"b5_vcb_q_standalone_{idx}")
            if selected == item["answer"]:
                score_b5_vcb += 1
        if st.button("Chấm điểm Bài tập 1", key="btn_b5_vcb_standalone"):
            st.session_state.b5_current["b5_vcb"] = (score_b5_vcb, len(B5_QUIZ_VOCAB))
            save_progress()
            st.success(f"Bạn đúng {score_b5_vcb}/{len(B5_QUIZ_VOCAB)} câu.")
            
    # 2. Listening Quiz
    with st.expander("Bài tập 2: Luyện nghe và Chọn Pinyin đúng", expanded=False):
        st.caption("Nghe phát âm từ hệ thống và chọn cách viết Pinyin đúng:")
        score_b5_ls = 0
        for idx, item in enumerate(B5_QUIZ_LISTENING):
            st.write(f"**Câu {idx+1}:** Nghe từ mẫu:")
            render_play_button(item['hanzi'], "🔊 Nghe phát âm mẫu", key=f"b5_listen_standalone_{idx}")
            choices = shuffled_options(item["choices"], f"b5_ls_standalone-{idx}")
            if choices[0] == item["answer"] and len(choices) > 1:
                choices[0], choices[1] = choices[1], choices[0]
            selected = st.radio("Chọn phiên âm chính xác:", choices, index=0, key=f"b5_ls_q_standalone_{idx}")
            if selected == item["answer"]:
                score_b5_ls += 1
        if st.button("Chấm điểm Bài tập 2", key="btn_b5_ls_standalone"):
            st.session_state.b5_current["b5_ls"] = (score_b5_ls, len(B5_QUIZ_LISTENING))
            save_progress()
            st.success(f"Bạn đúng {score_b5_ls}/{len(B5_QUIZ_LISTENING)} câu.")
            
    # 3. Fill Blanks Quiz
    with st.expander("Bài tập 3: Điền vận mẫu còn thiếu", expanded=False):
        st.caption("Điền phần vận mẫu mũi và thanh điệu thích hợp vào chỗ trống để tạo thành từ đúng:")
        score_b5_fill = 0
        opts = ["...", "àn", "án", "ǎn", "àn", "én", "én", "ěn", "èn", "ín", "ín", "ǐn", "ìn", "án", "áng", "ǎng", "àng", "éng", "ěng", "èng", "īng", "ǐng", "ìng", "óng", "ǒng", "òng"]
        opts = list(dict.fromkeys(opts))
        for idx, item in enumerate(B5_QUIZ_FILL_BLANKS):
            selected = st.selectbox(f"Câu {idx+1}: Điền vào '{item['q']}' nghĩa là '{item['meaning']}'", opts, index=0, key=f"b5_fill_q_standalone_{idx}")
            if selected == item["ans"]:
                score_b5_fill += 1
        if st.button("Chấm điểm Bài tập 3", key="btn_b5_fill_standalone"):
            st.session_state.b5_current["b5_fill"] = (score_b5_fill, len(B5_QUIZ_FILL_BLANKS))
            save_progress()
            st.success(f"Bạn đúng {score_b5_fill}/{len(B5_QUIZ_FILL_BLANKS)} câu.")
            
    # --- TOTAL SUMMARY & SUBMISSION ---
    st.markdown("---")
    with st.expander("📊 Bảng điểm & Nộp bài tập Bài 5.2", expanded=True):
        cur = st.session_state.b5_current
        labels = {"b5_vcb": "BT1: Từ vựng", "b5_ls": "BT2: Luyện nghe", "b5_fill": "BT3: Điền âm"}
        missing = [labels[k] for k in labels.keys() if k not in cur]
        
        if missing:
            st.warning(f"Vui lòng hoàn thành và bấm chấm điểm các bài tập: {', '.join(missing)}")
        else:
            earned = sum(cur[k][0] for k in labels.keys())
            total = sum(cur[k][1] for k in labels.keys())
            score_10 = round((earned / total) * 10, 2)
            st.success(f"📈 Điểm tổng kết Bài 5.2: **{score_10} / 10**")
            for k, lbl in labels.items():
                st.write(f"- {lbl}: {cur[k][0]} / {cur[k][1]}")
                
            st.markdown("---")
            name = st.text_input("Tên học viên (Bài 5.2)", key="student_name_b5_standalone")
            if st.button("Nộp bài tập Bài 5.2", type="primary", use_container_width=True, key="btn_submit_b5_standalone"):
                if name:
                    def fmt(k):
                        s = cur.get(k)
                        return f"{s[0]}/{s[1]}" if s else ""
                    row = {
                        "thời gian": datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S"),
                        "học viên": name,
                        "tổng điểm": score_10,
                        "BT1: Từ vựng": fmt("b5_vcb"),
                        "BT2: Nghe": fmt("b5_ls"),
                        "BT3: Điền âm": fmt("b5_fill")
                    }
                    if save_score_row_b5(row):
                        st.success("Đã lưu kết quả bài tập Bài 5.2 thành công!")
                        st.session_state.b5_current = {}
                        st.rerun()
                else:
                    st.error("Vui lòng nhập tên học viên để nộp bài!")
                    
        all_scores = load_all_scores_b5()
        if all_scores:
            st.write("### 📜 Lịch sử nộp bài lớp học:")
            st.dataframe(all_scores, use_container_width=True)


def show_lesson5_degree_adverbs(save_progress, save_score_row_b5_3, load_all_scores_b5_3):
    st.markdown("""
    <style>
    .adv-card {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border-radius: 16px;
        border-left: 5px solid #0ea5e9;
        padding: 16px;
        margin-bottom: 14px;
    }
    .adv-hanzi { font-size: 2.6em; font-weight: 900; color: #0c4a6e; line-height: 1.1; }
    .adv-pinyin { font-size: 1em; color: #0369a1; font-weight: 600; margin-bottom: 4px; }
    .adv-level { font-size: 0.82em; color: #475569; font-style: italic; margin-bottom: 6px; }
    .adv-formula {
        display: inline-block; background: #0ea5e9; color: white;
        border-radius: 8px; padding: 3px 10px; font-size: 0.85em;
        font-weight: 700; margin-bottom: 8px; font-family: monospace;
    }
    .adv-example { background: white; border-radius: 10px; padding: 10px 14px; margin-top: 6px; }
    .adv-example-han { font-size: 1.5em; font-weight: 800; color: #1e3a8a; }
    .adv-example-py { font-size: 0.9em; color: #2563eb; font-family: monospace; font-weight: 600; }
    .adv-example-vi { font-size: 0.88em; color: #059669; font-style: italic; }
    .adv-desc { font-size: 0.82em; color: #64748b; margin-top: 6px; line-height: 1.5; }
    .sb-result-box {
        background: linear-gradient(135deg, #fefce8 0%, #fef9c3 100%);
        border: 2px solid #fbbf24; border-radius: 16px;
        padding: 20px; text-align: center; margin: 16px 0;
    }
    .sb-hanzi { font-size: 2.8em; font-weight: 900; color: #1e3a8a; }
    .sb-py { font-size: 1.1em; font-family: monospace; font-weight: 700; color: #2563eb; margin: 4px 0; }
    .sb-vi { font-size: 1em; color: #059669; font-style: italic; }
    @media (max-width: 640px) {
        .adv-hanzi { font-size: 2em; }
        .sb-hanzi { font-size: 2.2em; }
    }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        title="Bài 5.3 - Cách dùng 很 (hěn) & Phó từ chỉ mức độ",
        objective="Nắm vững cách dùng phó từ 很 (hěn) trong câu vị ngữ tính từ và mở rộng các phó từ chỉ mức độ: 非常, 太...了, 特别, 挺...的, 比较, 极了"
    )

    tab_theory, tab_builder, tab_quiz = st.tabs(["📖 1. Lý thuyết", "🔨 2. Ghép câu", "📝 3. Bài tập"])

    # --- TAB 1: LÝ THUYẾT ---
    with tab_theory:
        st.markdown("""
<div style="background-color: #f0fdf4; border-left: 6px solid #10b981; padding: 22px; border-radius: 12px; margin-bottom: 25px; border: 1px solid #bbf7d0; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.08);">
<h3 style="color: #14532d; margin-top: 0; margin-bottom: 12px; font-weight: 800; display: flex; align-items: center; gap: 8px; font-size: 1.3em;">
💡Cách dùng phó từ "很" (hěn) & trợ từ "了" (le)
</h3>
<p style="font-size: 0.98em; line-height: 1.7; color: #166534; margin-bottom: 15px;">
Trong tiếng Trung, câu khẳng định đơn giản có <b>tính từ làm vị ngữ</b> (như <i>"Tôi bận", "Cậu ấy khỏe"</i>) có cấu trúc đặc thù. Hãy đối chiếu với tiếng Việt và tiếng Anh để thấy rõ sự khác biệt:
</p>

<!-- Bảng so sánh 3 ngôn ngữ -->
<div style="overflow-x: auto; margin-bottom: 20px;">
<table style="width: 100%; border-collapse: collapse; background-color: white; border: 1px solid #e2e8f0; border-radius: 8px; font-size: 0.9em; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
<thead>
<tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1; color: #334155; font-weight: 700;">
<th style="padding: 10px; text-align: left; border-right: 1px solid #e2e8f0;">Ngôn ngữ</th>
<th style="padding: 10px; text-align: left; border-right: 1px solid #e2e8f0;">Ví dụ câu</th>
<th style="padding: 10px; text-align: left; border-right: 1px solid #e2e8f0;">Thành phần ngữ pháp</th>
<th style="padding: 10px; text-align: left;">Đặc điểm nổi bật</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid #e2e8f0;">
<td style="padding: 10px; font-weight: bold; border-right: 1px solid #e2e8f0; color: #0f172a;">Tiếng Việt</td>
<td style="padding: 10px; border-right: 1px solid #e2e8f0; color: #334155;">Tôi đói. / Tôi bận.</td>
<td style="padding: 10px; border-right: 1px solid #e2e8f0; color: #475569; font-style: italic;">Không cần từ đệm</td>
<td style="padding: 10px; color: #475569;">Tính từ trực tiếp làm vị ngữ một cách độc lập và tự do.</td>
</tr>
<tr style="border-bottom: 1px solid #e2e8f0;">
<td style="padding: 10px; font-weight: bold; border-right: 1px solid #e2e8f0; color: #0f172a;">Tiếng Anh</td>
<td style="padding: 10px; border-right: 1px solid #e2e8f0; color: #334155;">I <b>am</b> hungry. / I <b>am</b> busy.</td>
<td style="padding: 10px; border-right: 1px solid #e2e8f0; color: #b91c1c; font-family: monospace; font-weight: 700;">Động từ liên kết "to be"</td>
<td style="padding: 10px; color: #475569;">Tính từ không thể làm vị ngữ trực tiếp, phải có "to be" liên kết.</td>
</tr>
<tr>
<td style="padding: 10px; font-weight: bold; border-right: 1px solid #e2e8f0; color: #0f172a;">Tiếng Trung</td>
<td style="padding: 10px; border-right: 1px solid #e2e8f0; color: #1e40af; font-weight: 700;">我<b>很</b>饿。/ 我<b>很</b>忙。</td>
<td style="padding: 10px; border-right: 1px solid #e2e8f0; color: #15803d; font-family: monospace; font-weight: 700;">Phó từ chỉ mức độ "很"</td>
<td style="padding: 10px; color: #475569;">Bắt buộc phải có "很" làm cầu nối ngữ pháp để câu được trọn vẹn.</td>
</tr>
</tbody>
</table>
</div>

<p style="font-size: 0.98em; line-height: 1.6; color: #1f2937; font-weight: bold; margin-bottom: 8px;">
📌 Tại sao câu vị ngữ tính từ tiếng Trung lại bắt buộc phải có "很" (hěn)?
</p>
<ol style="font-size: 0.95em; line-height: 1.7; color: #374151; padding-left: 20px; margin-bottom: 18px;">
<li style="margin-bottom: 8px;">
<b>Tránh nghĩa so sánh ngầm (Implicit Comparison):</b> 
Nếu chỉ nói <span style="font-family: monospace; font-weight: bold; color: #b91c1c; background: #fee2e2; padding: 2px 6px; border-radius: 4px;">"我忙" (Wǒ máng)</span>, câu sẽ rất cụt và lửng lơ. Người nghe sẽ tự hiểu là bạn đang so sánh ngầm: <i>"Tôi bận (còn người khác rảnh / còn bạn thì không)"</i>. Thêm <b>"很"</b> giúp câu trở thành một câu khẳng định khách quan, độc lập: <span style="font-family: monospace; font-weight: bold; color: #15803d; background: #dcfce7; padding: 2px 6px; border-radius: 4px;">"我很忙" (Wǒ hěn máng)</span>.
</li>
<li style="margin-bottom: 8px;">
<b>Làm chất keo liên kết ngữ pháp:</b> 
Trong tiếng Trung, tính từ làm vị ngữ trực tiếp mà <b>không đi kèm động từ "是" (shì - là)</b> (Tuyệt đối không nói ❌ <i>"我是忙"</i>). Từ <b>"很"</b> ở đây đóng vai trò như một liên từ ngữ pháp giúp kết nối và làm cân bằng cấu trúc câu.
</li>
<li style="margin-bottom: 8px;">
<b>Hiện tượng mờ nhạt ý nghĩa (Semantic Bleaching):</b> 
Trong câu khẳng định bình thường, chữ <b>"很"</b> không mang nghĩa nhấn mạnh là "rất" nữa. Khi nói <i>"我很忙"</i>, ta chỉ dịch là <i>"Tôi bận"</i>. Muốn thực sự nhấn mạnh <b>"rất"</b>, ta phải nhấn trọng âm vào chữ <b>"很"</b> khi nói hoặc dùng từ mạnh hơn như <i>非常 (fēicháng)</i>.
</li>
</ol>

<hr style="border: 0; border-top: 1px dashed #cbd5e1; margin: 20px 0;"/>

<h4 style="color: #0c4a6e; margin-top: 0; margin-bottom: 10px; font-weight: bold;">
🙋 Phân biệt cấu trúc với "很" (hěn) và "了" (le)
</h4>
<div style="background-color: white; border-radius: 8px; padding: 15px; border: 1px solid #e2e8f0; font-size: 0.95em; line-height: 1.6; color: #334155;">
<p style="margin-top: 0; margin-bottom: 10px;">
<b>1. Từ loại của "饱" (bǎo) trong "我饱了" là gì?</b><br/>
👉 Bản chất <b>饱 (bǎo)</b> vẫn là một <b>TÍNH TỪ</b> (形容词 - Adjective) chỉ trạng thái no bụng. Khi đi với trợ từ ngữ khí <b>"了" (le)</b>, nó diễn tả <b>sự chuyển biến sang một trạng thái mới</b> (từ chưa no chuyển sang đã no).
</p>
<p style="margin-bottom: 10px;">
<b>2. Tại sao câu "我饱了" lại không cần dùng "hěn"?</b><br/>
👉 Trợ từ ngữ khí <b>"了" (le)</b> đứng cuối câu biểu thị sự thay đổi trạng thái đã làm trọn vẹn ngữ âm và ngữ nghĩa của câu. Ta <b>không cần</b> dùng phó từ ngữ pháp "很" để làm cầu nối.
</p>
<p style="margin-bottom: 0;">
<b>3. Phân biệt sắc thái của "我饱了" vs "我很饱" vs "我很饱了":</b><br/>
• <span style="font-family: monospace; font-weight: bold; color: #1e40af;">我饱了 (Wǒ bǎo le):</span> <i>"Tôi no rồi."</i> (Thông báo sự thay đổi trạng thái khách quan).<br/>
• <span style="font-family: monospace; font-weight: bold; color: #1e40af;">我很饱 (Wǒ hěn bǎo):</span> <i>"Tôi no."</i> (Miêu tả trạng thái tĩnh, "很" chỉ làm nhiệm vụ cầu nối ngữ pháp, không mang nghĩa nhấn mạnh "rất").<br/>
• <span style="font-family: monospace; font-weight: bold; color: #1e40af;">我很饱了 (Wǒ hěn bǎo le):</span> <i>"Tôi <b>rất</b> no rồi / no căng bụng rồi."</i> (Khi "了" đã hoàn thành cấu trúc câu, "很" được giải phóng khỏi vai trò ngữ pháp và lấy lại nghĩa gốc là <b>RẤT</b> để nhấn mạnh mức độ).
</p>
</div>

<p style="font-size: 0.95em; line-height: 1.6; color: #1f2937; font-weight: bold; margin-top: 15px; margin-bottom: 5px;">
⚠️ Quy tắc khi phủ định:
</p>
<p style="font-size: 0.95em; line-height: 1.6; color: #4b5563; margin-bottom: 0;">
Khi phủ định bằng phó từ <b>"不" (bù - không)</b>, chính "不" đã đóng vai trò làm cầu nối ngữ pháp thay cho "很", do đó ta <b>bỏ "很" đi</b>. Ví dụ: <span style="font-family: monospace; font-weight: bold; color: #b91c1c; background: #fee2e2; padding: 2px 6px; border-radius: 4px;">"我不忙" (Wǒ bù máng)</span> - <i>"Tôi không bận"</i>.
</p>
</div>
        """, unsafe_allow_html=True)

        st.subheader("Bảng các Phó từ Chỉ Mức độ (Phân chia theo cấp độ)")

        categories = [
            {
                "title": "🟢 1. Mức độ tương đối (Khá, tương đối)",
                "advs": ["比较", "挺 ... 的"]
            },
            {
                "title": "🟡 2. Mức độ cơ bản (Rất)",
                "advs": ["很"]
            },
            {
                "title": "🟠 3. Mức độ mạnh (Đặc biệt, vô cùng)",
                "advs": ["特别", "非常"]
            },
            {
                "title": "🔴 4. Mức độ cực hạn / Cảm thán (Quá, cực kỳ)",
                "advs": ["太 ... 了", "极了"]
            }
        ]

        for cat in categories:
            st.markdown(f"### {cat['title']}")
            cat_items = [item for item in B5_3_ADVERBS_DATA if item['adv'] in cat['advs']]
            for item in cat_items:
                st.markdown(f"""
                <div class="adv-card">
                  <div class="adv-hanzi">{item['adv']}</div>
                  <div class="adv-pinyin">{item['pinyin']}</div>
                  <div class="adv-level">🎯 {item['level']}</div>
                  <div class="adv-formula">{item['formula']}</div>
                  <div class="adv-example">
                    <div class="adv-example-han">{item['example_han']}</div>
                    <div class="adv-example-py">{item['example_py']}</div>
                    <div class="adv-example-vi">👉 {item['meaning']}</div>
                  </div>
                  <div class="adv-desc">📌 {item['desc']}</div>
                </div>
                """, unsafe_allow_html=True)
                render_play_button(item['example_han'], f"🔊 Nghe: {item['example_han']}", key=f"adv_play_{item['adv']}")
                st.markdown("<br/>", unsafe_allow_html=True)

    # --- TAB 2: SENTENCE BUILDER ---
    with tab_builder:
        st.subheader("🔨 Ghép câu với Phó từ Chỉ Mức độ")
        st.write("Chọn các thành phần để tạo câu hoàn chỉnh và nghe phát âm:")

        SUBJECTS = {
            "我": {"py": "Wǒ", "vi": "Tôi"},
            "你": {"py": "Nǐ", "vi": "Bạn"},
            "他": {"py": "Tā", "vi": "Anh ấy"},
            "她": {"py": "Tā", "vi": "Cô ấy"},
            "汉语": {"py": "Hànyǔ", "vi": "Tiếng Trung"},
            "今天": {"py": "Jīntiān", "vi": "Hôm nay"},
        }
        ADVERBS = {
            "(Không dùng)": {"py": "", "vi": "", "pos": "none"},
            "很": {"py": "hěn", "vi": "rất", "pos": "pre"},
            "非常": {"py": "fēicháng", "vi": "vô cùng", "pos": "pre"},
            "太": {"py": "tài", "vi": "quá", "pos": "special_tai"},
            "特别": {"py": "tèbié", "vi": "đặc biệt", "pos": "pre"},
            "挺": {"py": "tǐng", "vi": "khá là", "pos": "special_ting"},
            "比较": {"py": "bǐjiào", "vi": "tương đối", "pos": "pre"},
            "极了": {"py": "jíle", "vi": "cực kỳ", "pos": "post"},
        }
        ADJECTIVES = {
            "忙": {"py": "máng", "vi": "bận"},
            "好": {"py": "hǎo", "vi": "tốt"},
            "累": {"py": "lèi", "vi": "mệt"},
            "热": {"py": "rè", "vi": "nóng"},
            "难": {"py": "nán", "vi": "khó"},
            "漂亮": {"py": "piàoliang", "vi": "xinh đẹp"},
            "有趣": {"py": "yǒuqù", "vi": "thú vị"},
        }

        sel_s = st.selectbox("Chủ ngữ", list(SUBJECTS.keys()), key="sb53_sub")
        sel_adv = st.selectbox("Phó từ", list(ADVERBS.keys()), index=1, key="sb53_adv")
        sel_adj = st.selectbox("Tính từ", list(ADJECTIVES.keys()), key="sb53_adj")

        s_data = SUBJECTS[sel_s]
        adv_data = ADVERBS[sel_adv]
        adj_data = ADJECTIVES[sel_adj]

        if adv_data["pos"] == "special_tai":
            built_han = f"{sel_s}太{sel_adj}了"
            built_py = f"{s_data['py']} tài {adj_data['py']} le"
            built_vi = f"{s_data['vi']} {adj_data['vi']} quá rồi"
        elif adv_data["pos"] == "special_ting":
            built_han = f"{sel_s}挺{sel_adj}的"
            built_py = f"{s_data['py']} tǐng {adj_data['py']} de"
            built_vi = f"{s_data['vi']} khá là {adj_data['vi']}"
        elif adv_data["pos"] == "post":
            built_han = f"{sel_s}{sel_adj}极了"
            built_py = f"{s_data['py']} {adj_data['py']} jíle"
            built_vi = f"{s_data['vi']} {adj_data['vi']} cực kỳ"
        elif adv_data["pos"] == "none":
            built_han = f"{sel_s}{sel_adj}"
            built_py = f"{s_data['py']} {adj_data['py']}"
            built_vi = f"{s_data['vi']} {adj_data['vi']} (⚠️ thiếu tự nhiên — thường cần phó từ)"
        else:
            built_han = f"{sel_s}{sel_adv}{sel_adj}"
            built_py = f"{s_data['py']} {adv_data['py']} {adj_data['py']}"
            built_vi = f"{s_data['vi']} {adv_data['vi']} {adj_data['vi']}"

        st.markdown(f"""
        <div class="sb-result-box">
            <div class="sb-hanzi">{built_han}</div>
            <div class="sb-py">{built_py}</div>
            <div class="sb-vi">👉 {built_vi}</div>
        </div>
        """, unsafe_allow_html=True)
        render_play_button(built_han, "🔊 Phát âm câu vừa ghép", key="sb53_play", type="primary")

    # --- TAB 3: BÀI TẬP ---
    with tab_quiz:
        st.subheader("📝 Bài tập Luyện tập & Đánh giá (Bài 5.3)")
        st.write("Hoàn thành các câu trắc nghiệm dưới đây rồi bấm Chấm điểm:")

        if "b5_3_current" not in st.session_state:
            st.session_state.b5_3_current = {}

        score_b5_3 = 0
        for idx, item in enumerate(B5_3_QUIZ):
            choices = shuffled_options(item["choices"], f"b5_3_quiz-{idx}")
            selected = st.radio(f"**Câu {idx+1}:** {item['q']}", choices, index=None, key=f"b5_3_q_{idx}")
            if selected == item["answer"]:
                score_b5_3 += 1
            st.markdown("<br/>", unsafe_allow_html=True)

        if st.button("✅ Chấm điểm Bài 5.3", key="btn_b5_3_score", use_container_width=True):
            st.session_state.b5_3_current["score"] = (score_b5_3, len(B5_3_QUIZ))
            save_progress()
            st.success(f"Bạn đúng {score_b5_3}/{len(B5_3_QUIZ)} câu!")

        st.markdown("---")
        with st.expander("📊 Bảng điểm & Nộp bài Bài 5.3", expanded=True):
            cur = st.session_state.b5_3_current
            if "score" not in cur:
                st.warning("Vui lòng hoàn thành và bấm chấm điểm để nộp bài.")
            else:
                earned, total = cur["score"]
                score_10 = round((earned / total) * 10, 2)
                st.success(f"📈 Điểm Bài 5.3: **{score_10} / 10**")
                name = st.text_input("Tên học viên", key="student_name_b5_3", placeholder="Nhập tên...")
                if st.button("📤 Nộp bài Bài 5.3", type="primary", use_container_width=True, key="btn_submit_b5_3"):
                    if name:
                        row = {
                            "thời gian": datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S"),
                            "học viên": name,
                            "tổng điểm": score_10,
                            "BT: Trắc nghiệm": f"{earned}/{total}"
                        }
                        if save_score_row_b5_3(row):
                            st.success("✅ Đã lưu kết quả thành công!")
                            st.session_state.b5_3_current = {}
                            st.rerun()
                    else:
                        st.error("Vui lòng nhập tên học viên!")

            all_scores = load_all_scores_b5_3()
            if all_scores:
                st.write("### 📜 Lịch sử nộp bài:")
                st.dataframe(all_scores, use_container_width=True)


def show_lesson5_vocab():
    render_lesson_intro("📚 Bài 5: Từ vựng", "Học các từ vựng mới trong Bài 5 dưới dạng thẻ từ tương tác (Flashcards) có phát âm bản xứ.")

    B5_VOCAB = [
        {"emoji": "🌅", "word": "早餐", "pinyin": "zǎocān", "vietnamese": "Bữa sáng", "key_prefix": "b5_zaocan", "example_han": "你吃早餐了吗？", "example_py": "Nǐ chī zǎocān le ma?", "example_vi": "Bạn ăn sáng chưa?"},
        {"emoji": "👥", "word": "大家", "pinyin": "dàjiā", "vietnamese": "Mọi người, cả nhà", "key_prefix": "b5_dajia", "example_han": "大家好！", "example_py": "Dàjiā hǎo!", "example_vi": "Chào mọi người!"},
        {"emoji": "📏", "word": "大", "pinyin": "dà", "vietnamese": "To, lớn", "key_prefix": "b5_da", "example_han": "他的家很大。", "example_py": "Tā de jiā hěn dà.", "example_vi": "Nhà của anh ấy rất lớn.", "note": "Trái nghĩa: <b>小 xiǎo</b> (nhỏ)."},
        {"emoji": "🤏", "word": "小", "pinyin": "xiǎo", "vietnamese": "Nhỏ, bé", "key_prefix": "b5_xiao", "example_han": "这个杯子很小。", "example_py": "Zhège bēizi hěn xiǎo.", "example_vi": "Cái cốc này rất nhỏ.", "note": "Trái nghĩa: <b>大 dà</b> (lớn)."},
        {"emoji": "😋", "word": "饱", "pinyin": "bǎo", "vietnamese": "No, no bụng", "key_prefix": "b5_bao", "example_han": "我饱了。", "example_py": "Wǒ bǎo le.", "example_vi": "Tôi no rồi.", "note": "Trái nghĩa: <b>饿 è</b> (đói)."},
        {"emoji": "🍽️", "word": "饿", "pinyin": "è", "vietnamese": "Đói, đói bụng", "key_prefix": "b5_e", "example_han": "你饿吗？", "example_py": "Nǐ è ma?", "example_vi": "Bạn đói không?", "note": "Trái nghĩa: <b>饱 bǎo</b> (no)."},
        {"emoji": "🙏", "word": "您", "pinyin": "nín", "vietnamese": "Ngài / Ông / Bà (kính trọng)", "key_prefix": "b5_nin", "example_han": "您好！您贵姓？", "example_py": "Nín hǎo! Nín guìxìng?", "example_vi": "Chào Ngài! Ngài quý danh?", "note": "Viết thêm bộ <b>心 (tâm)</b> dưới chữ <b>你</b> để thể hiện sự tôn kính."},
        {"emoji": "🎂", "word": "岁", "pinyin": "suì", "vietnamese": "Tuổi", "key_prefix": "b5_sui", "example_han": "你今年几岁？", "example_py": "Nǐ jīnnián jǐ suì?", "example_vi": "Năm nay bạn bao nhiêu tuổi?"},
        {"emoji": "✅", "word": "已经", "pinyin": "yǐjīng", "vietnamese": "Đã / Đã... rồi", "key_prefix": "b5_yijing", "example_han": "我已经饱了。", "example_py": "Wǒ yǐjīng bǎo le.", "example_vi": "Tôi đã no rồi.", "note": "Phó từ chỉ thời gian. Cấu trúc: <b>已经 + V/Adj + 了</b>."},
    ]

    # --- CSS giống Bài 4 ---
    st.markdown("""
    <style>
    .flashcard-container-b5 {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05), 0 8px 10px -6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        display: flex;
        gap: 30px;
        align-items: center;
    }
    .flashcard-image-b5 {
        flex-shrink: 0;
        width: 200px;
        height: 200px;
        border-radius: 16px;
        overflow: hidden;
        border: 3px solid #f1f5f9;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        background: white;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .flashcard-image-b5 img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .fc-word-b5 {
        font-size: 3.5rem;
        font-weight: 800;
        color: #0f172a;
        line-height: 1.1;
        margin-bottom: 5px;
    }
    .fc-pinyin-b5 {
        font-family: 'Courier New', monospace;
        font-size: 1.5rem;
        font-weight: 700;
        color: #2563eb;
        background: #eff6ff;
        padding: 4px 16px;
        border-radius: 30px;
        border: 1px solid #dbeafe;
        display: inline-block;
        margin-bottom: 12px;
    }
    .fc-viet-b5 {
        font-size: 1.4rem;
        font-weight: 700;
        color: #334155;
        margin-bottom: 15px;
    }
    .fc-ex-box-b5 {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 15px;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.01);
    }
    .fc-ex-title-b5 {
        font-size: 0.8rem;
        color: #64748b;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 6px;
        letter-spacing: 0.05em;
    }
    .fc-ex-han-b5 { font-size: 1.4rem; font-weight: 700; color: #0f172a; margin-bottom: 2px; }
    .fc-ex-py-b5 { font-family: 'Courier New', monospace; font-weight: 700; color: #059669; font-size: 1.05rem; margin-bottom: 4px; }
    .fc-ex-vi-b5 { color: #475569; font-style: italic; font-size: 0.95rem; border-left: 2px solid #cbd5e1; padding-left: 8px; }
    @media (max-width: 768px) {
        .flashcard-container-b5 { flex-direction: column; padding: 20px; text-align: center; gap: 20px; }
        .flashcard-image-b5 { width: 160px; height: 160px; }
    }
    </style>
    """, unsafe_allow_html=True)

    slide_key = "b5_vocab_slide_idx"
    if slide_key not in st.session_state:
        st.session_state[slide_key] = 0

    cur_idx = st.session_state[slide_key]
    if cur_idx >= len(B5_VOCAB):
        cur_idx = 0
        st.session_state[slide_key] = 0

    w = B5_VOCAB[cur_idx]

    # --- Image lookup ---
    img_name = w["key_prefix"].replace("b5_", "")
    img_base64 = ""
    for ext in [".png", ".jpg", ".jpeg", ".gif"]:
        p = os.path.join("assets", "lesson5", img_name + ext)
        if os.path.exists(p):
            with open(p, "rb") as f:
                data = f.read()
                mime = "image/png"
                if data.startswith(b'\xff\xd8'): mime = "image/jpeg"
                elif data.startswith(b'GIF8'): mime = "image/gif"
                img_base64 = f"data:{mime};base64,{base64.b64encode(data).decode('utf-8')}"
            break

    if img_base64:
        img_tag = f'<img src="{img_base64}" />'
    else:
        img_tag = f'<div style="font-size: 4rem;">{w["emoji"]}</div>'

    note_html = ""
    if "note" in w:
        note_html = f'<div style="margin-top: 10px; background-color: #F0F9FF; border-left: 3px solid #0EA5E9; border-radius: 6px; padding: 10px 14px; font-size: 0.88em; color: #334155; line-height: 1.55;">💡 {w["note"]}</div>'

    card_html = f"""<div class="flashcard-container-b5">
<div class="flashcard-image-b5">{img_tag}</div>
<div style="flex-grow: 1;">
<div class="fc-word-b5">{w['word']}</div>
<div><span class="fc-pinyin-b5">{w['pinyin']}</span></div>
<div class="fc-viet-b5">Nghĩa: {w['vietnamese']}</div>
<div class="fc-ex-box-b5">
<div class="fc-ex-title-b5">Ví dụ mẫu:</div>
<div class="fc-ex-han-b5">{w['example_han']}</div>
<div class="fc-ex-py-b5">{w['example_py']}</div>
<div class="fc-ex-vi-b5">{w['example_vi']}</div>
{note_html}
</div>
</div>
</div>"""

    col_card, col_ctrl = st.columns([4.2, 1.8])
    with col_card:
        st.markdown(card_html, unsafe_allow_html=True)
    with col_ctrl:
        st.markdown("<h4 style='color:#1e293b; margin-top:0;'>🔊 Phát âm</h4>", unsafe_allow_html=True)
        render_play_button(w['word'], "🔊 Phát âm từ", key=f"slide_{w['key_prefix']}_word")
        st.write("")
        render_play_button(w['example_han'], "🔊 Nghe cả câu", key=f"slide_{w['key_prefix']}_ex")

        st.markdown("<hr style='margin:15px 0;'/>", unsafe_allow_html=True)
        st.markdown("<h4 style='color:#1e293b;'>🎮 Điều khiển</h4>", unsafe_allow_html=True)

        col_prev, col_next = st.columns(2)
        with col_prev:
            if st.button("⬅️ Từ trước", use_container_width=True, key="b5v_prev"):
                st.session_state[slide_key] = (cur_idx - 1) % len(B5_VOCAB)
                st.rerun()
        with col_next:
            if st.button("Từ sau ➡️", use_container_width=True, key="b5v_next"):
                st.session_state[slide_key] = (cur_idx + 1) % len(B5_VOCAB)
                st.rerun()

        st.markdown(f"<div style='text-align: center; font-size: 1.25em; font-weight: bold; margin-top: 10px; color:#475569;'>Từ {cur_idx + 1} / {len(B5_VOCAB)}</div>", unsafe_allow_html=True)
        st.progress((cur_idx + 1) / len(B5_VOCAB))

    # --- Phần ngữ pháp 已经 (chỉ hiện khi đang xem từ 已经) ---
    if w["key_prefix"] == "b5_yijing":
        st.markdown("---")
        st.subheader("📖 Ngữ pháp mở rộng: 已经 (yǐjīng) — Đã... rồi")

        st.markdown("""
<div style="background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); border-left: 6px solid #3b82f6; border-radius: 12px; padding: 22px; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
<h4 style="color: #1e3a8a; margin-top: 0; margin-bottom: 12px; font-weight: bold;">
💡 Cấu trúc: 已经 + Động từ / Tính từ + 了 (yǐjīng ... le)
</h4>
<p style="color: #334155; line-height: 1.6; margin-bottom: 15px; font-size: 1.02rem;">
Dùng để diễn tả một hành động đã hoàn thành, hoặc một trạng thái đã có sự thay đổi. Trợ từ ngữ khí <b>了 (le)</b> thường đứng cuối câu để biểu thị sự thay đổi đã xảy ra.
</p>
<div style="background-color: white; border-radius: 8px; padding: 15px; border: 1px solid #bfdbfe; color: #1e293b;">
<div style="font-weight: bold; color: #0f172a; margin-bottom: 10px; border-bottom: 1px dashed #cbd5e1; padding-bottom: 6px;">Ví dụ áp dụng:</div>
<ul style="margin: 0; padding-left: 20px; line-height: 1.8;">
<li><b>我已经饱了。</b> (Wǒ yǐjīng bǎo le.) — <i>Tôi đã no rồi.</i></li>
<li><b>他已经来了。</b> (Tā yǐjīng lái le.) — <i>Anh ấy đã đến rồi.</i></li>
<li><b>我们已经十八岁了。</b> (Wǒmen yǐjīng shíbā suì le.) — <i>Chúng tôi đã 18 tuổi rồi.</i></li>
<li><b>爸爸已经回家了。</b> (Bàba yǐjīng huíjiā le.) — <i>Bố đã về nhà rồi.</i></li>
</ul>
</div>
<div style="margin-top: 15px; font-size: 0.95em; color: #b91c1c; font-weight: bold; background-color: #fef2f2; padding: 10px 15px; border-radius: 6px; border: 1px solid #fee2e2;">
⚠️ Lưu ý phủ định: KHÔNG dùng <s>我不已经...</s>. Thay vào đó dùng <b>"还没(有)..." (hái méi yǒu)</b>.<br/>
<i>Ví dụ:</i> <b>我还没饱。</b> (Wǒ hái méi bǎo.) — <i>Tôi vẫn chưa no.</i>
</div>
</div>
        """, unsafe_allow_html=True)

        col_ex1, col_ex2 = st.columns(2)
        with col_ex1:
            render_play_button("我已经饱了", "🔊 我已经饱了 (Tôi đã no rồi)", key="play_ex_yijing_1")
        with col_ex2:
            render_play_button("我们已经十八岁了", "🔊 我们已经十八岁了 (Chúng tôi đã 18 tuổi rồi.)", key="play_ex_yijing_2")


def show_lesson5_duanwu():
    render_lesson_intro(
        title="Bài 5.4 - Tết Đoan Ngọ (端午节)",
        objective="Tìm hiểu nguồn gốc, truyền thuyết về nhà thơ Khuất Nguyên, học từ vựng cốt lõi và các phong tục độc đáo ngày Tết Đoan Ngọ."
    )

    tab_story, tab_vocab, tab_customs, tab_phrases, tab_quiz = st.tabs([
        "📖 1. Truyền thuyết",
        "📚 2. Từ vựng",
        "🎋 3. Phong tục & Hoạt động",
        "💬 4. Câu chúc & Giao tiếp",
        "📝 5. Trắc nghiệm vui"
    ])

    # --- TAB 1: TRUYỀN THUYẾT ---
    with tab_story:
        st.markdown("### ❓ Truyền thuyết Tết Đoan Ngọ :")

        
        # Checkbox để giáo viên bật mở câu chuyện
        show_story = st.checkbox("🔓 Hiển thị câu chuyện truyền thuyết (Khuất Nguyên)", value=False, key="dw_show_story")
        
        if show_story:
            st.markdown("""
<div style="background-color: #f0fdf4; border-left: 6px solid #10b981; padding: 20px; border-radius: 12px; margin-bottom: 20px; margin-top: 15px;">
<h3 style="color: #14532d; margin-top: 0; font-weight: 800;">🐉 Truyền thuyết Khuất Nguyên (屈原)</h3>
<p style="line-height: 1.6; color: #166534; font-size: 1.05em;">
<b>Khuất Nguyên</b> (khoảng 340–278 TCN) là vị trung thần tài hoa và nhà thơ yêu nước vĩ đại của nước Sở thời Chiến Quốc. Khi đất nước bị quân Tần xâm chiếm, ông vô cùng đau xót, đã ôm đá gieo mình xuống sông <b>Mịch La (汨罗江)</b> tự vẫn vào ngày <b>mùng 5 tháng 5 Âm lịch</b> để thể hiện khí tiết.
</p>
<p style="line-height: 1.6; color: #166534; font-size: 1.05em;">
Thương tiếc ông, người dân hối hả chèo thuyền ra cứu (nguồn gốc của <b>đua thuyền rồng</b>), đồng thời ném cơm nếp bọc lá tre xuống sông để cá không ăn thân xác ông (nguồn gốc của <b>bánh tro - bánh ú</b>). Từ đó, ngày 5/5 âm lịch trở thành ngày Tết Đoan Ngọ để tưởng nhớ ông.
</p>
</div>
            """, unsafe_allow_html=True)

            col_audio1, col_audio2 = st.columns(2)
            with col_audio1:
                render_play_button("屈原", "🔊 Nghe phát âm: 屈原 (Khuất Nguyên)", key="dw_play_quyuan_name")
            with col_audio2:
                render_play_button("端午节", "🔊 Nghe phát âm: 端午节 (Tết Đoan Ngọ)", key="dw_play_duanwujie_name")

    # --- TAB 2: TỪ VỰNG FLASHCARD ---
    with tab_vocab:
        DW_VOCAB = [
            {
                "emoji": "🐉", "word": "端午节", "pinyin": "Duānwǔ Jié", "vietnamese": "Tết Đoan Ngọ", "key_prefix": "b5_dw_duanwu",
                "example_han": "端午节是中国的传统节日。", "example_py": "Duānwǔ Jié shì Zhōngguó de chuántǒng jiérì.", "example_vi": "Tết Đoan Ngọ là ngày lễ truyền thống của Trung Quốc.",
                "story": "Ý nghĩa là 'ngày khởi đầu của tháng Ngọ' (tháng 5 âm lịch), một lễ hội quan trọng kéo dài hơn 2000 năm."
            },
            {
                "emoji": "🍙", "word": "粽子", "pinyin": "zòngzi", "vietnamese": "Bánh tro / Bánh ú", "key_prefix": "b5_dw_zongzi",
                "example_han": "我很喜欢吃粽子。", "example_py": "Wǒ hěn xǐhuān chī zòngzi.", "example_vi": "Tôi rất thích ăn bánh tro.",
                "story": "Bánh làm từ gạo nếp gói lá tre hình tam giác, tượng trưng cho những gói cơm người dân ném xuống sông để bảo vệ thân xác Khuất Nguyên."
            },
            {
                "emoji": "⛵", "word": "龙舟", "pinyin": "lóngzhōu", "vietnamese": "Thuyền rồng", "key_prefix": "b5_dw_longzhou",
                "example_han": "这条龙舟非常大。", "example_py": "Zhège lóngzhōu fēicháng dà.", "example_vi": "Chiếc thuyền rồng này vô cùng lớn.",
                "story": "Thuyền dài chạm khắc hình đầu và đuôi rồng, đại diện cho linh vật sông nước bảo vệ và xua đuổi tà khí."
            },
            {
                "emoji": "🚣", "word": "赛龙舟", "pinyin": "sài lóngzhōu", "vietnamese": "Đua thuyền rồng", "key_prefix": "b5_dw_sailongzhou",
                "example_han": "端午节要赛龙舟。", "example_py": "Duānwǔ Jié yào sài lóngzhōu.", "example_vi": "Tết Đoan Ngọ phải đua thuyền rồng.",
                "story": "Bắt nguồn từ việc người dân hối hả chèo thuyền ra cứu Khuất Nguyên, nay là môn thể thao quốc tế sôi nổi."
            },
            {
                "emoji": "👨‍💼", "word": "屈原", "pinyin": "Qū Yuán", "vietnamese": "Khuất Nguyên", "key_prefix": "b5_dw_quyuan",
                "example_han": "屈原是一位伟大的诗人。", "example_py": "Qū Yuán shì yī wèi wěidà de shīrén.", "example_vi": "Khuất Nguyên là một nhà thơ vĩ đại.",
                "story": "Nhà thơ yêu nước lớn thời Chiến Quốc, biểu tượng của sự trung trinh và lòng ái quốc trong văn hóa Trung Hoa."
            },
            {
                "emoji": "🌿", "word": "艾草", "pinyin": "àicǎo", "vietnamese": "Cây ngải cứu", "key_prefix": "b5_dw_aicao",
                "example_han": "门口挂着艾草。", "example_py": "Ménkǒu guàzhe àicǎo.", "example_vi": "Trước cửa có treo ngải cứu.",
                "story": "Lá ngải cứu có mùi thơm nồng, được treo trước cửa nhà vào dịp Đoan Ngọ để trừ dịch bệnh và xua đuổi côn trùng."
            },
            {
                "emoji": "👝", "word": "香包", "pinyin": "xiāngbāo", "vietnamese": "Túi thơm", "key_prefix": "b5_dw_xiangbao",
                "example_han": "孩子戴着香包。", "example_py": "Háizi dàizhe xiāngbāo.", "example_vi": "Trẻ em đeo túi thơm.",
                "story": "Túi thêu đựng nhiều thảo dược thơm tự nhiên đeo bên người để phòng bệnh và cầu bình an."
            },
            {
                "emoji": "❤️", "word": "爱国", "pinyin": "àiguó", "vietnamese": "Yêu nước", "key_prefix": "b5_dw_aiguo",
                "example_han": "他非常爱国。", "example_py": "Tā fēicháng àiguó.", "example_vi": "Anh ấy rất yêu nước.",
                "story": "Tinh thần trung thành vô điều kiện với tổ quốc của Khuất Nguyên, cốt lõi văn hóa của ngày lễ này."
            },
            {
                "emoji": "✍️", "word": "诗人", "pinyin": "shīrén", "vietnamese": "Nhà thơ", "key_prefix": "b5_dw_shiren",
                "example_han": "他是一个诗人。", "example_py": "Tā shì yī ge shīrén.", "example_vi": "Ông ấy là một nhà thơ.",
                "story": "Nhà văn sáng tác thơ ca. Khuất Nguyên là ông tổ của thể thơ lãng mạn phương Nam."
            }
        ]

        st.markdown("""
<style>
.flashcard-container-dw {
    background: linear-gradient(135deg, #ffffff 0%, #f0fdf4 100%);
    border: 1px solid #bbf7d0;
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 10px 25px -5px rgba(16,185,129,0.05);
    margin-bottom: 20px;
    display: flex;
    gap: 30px;
    align-items: center;
}
.flashcard-image-dw {
    flex-shrink: 0;
    width: 180px;
    height: 180px;
    border-radius: 16px;
    background: white;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid #e2e8f0;
}
.fc-word-dw { font-size: 3.2rem; font-weight: 800; color: #14532d; line-height: 1.1; margin-bottom: 5px; }
.fc-pinyin-dw {
    font-family: 'Courier New', monospace;
    font-size: 1.4rem;
    font-weight: 700;
    color: #059669;
    background: #dcfce7;
    padding: 4px 16px;
    border-radius: 30px;
    display: inline-block;
    margin-bottom: 12px;
}
.fc-viet-dw { font-size: 1.3rem; font-weight: 700; color: #1e293b; margin-bottom: 10px; }
.fc-story-dw {
    background: #f8fafc;
    border-left: 4px solid #10b981;
    padding: 10px 14px;
    font-size: 0.92em;
    color: #475569;
    line-height: 1.5;
    border-radius: 6px;
    margin-top: 10px;
}
.fc-ex-box-dw { background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 12px; margin-top: 10px; }
.fc-ex-han-dw { font-size: 1.3rem; font-weight: 700; color: #0f172a; }
.fc-ex-py-dw { font-family: 'Courier New', monospace; font-weight: 700; color: #2563eb; }
.fc-ex-vi-dw { color: #475569; font-style: italic; }
@media (max-width: 768px) {
    .flashcard-container-dw { flex-direction: column; padding: 20px; text-align: center; gap: 20px; }
    .flashcard-image-dw { width: 140px; height: 140px; }
}
</style>
        """, unsafe_allow_html=True)

        slide_key = "b5_dw_slide_idx"
        if slide_key not in st.session_state:
            st.session_state[slide_key] = 0

        cur_idx = st.session_state[slide_key]
        if cur_idx >= len(DW_VOCAB):
            cur_idx = 0
            st.session_state[slide_key] = 0

        w = DW_VOCAB[cur_idx]

        img_name = w["key_prefix"].replace("b5_dw_", "")
        img_base64 = ""
        for ext in [".png", ".jpg", ".jpeg", ".gif"]:
            p = os.path.join("assets", "lesson5", img_name + ext)
            if os.path.exists(p):
                with open(p, "rb") as f:
                    data = f.read()
                    mime = "image/png"
                    if data.startswith(b'\xff\xd8'): mime = "image/jpeg"
                    elif data.startswith(b'GIF8'): mime = "image/gif"
                    img_base64 = f"data:{mime};base64,{base64.b64encode(data).decode('utf-8')}"
                break

        if img_base64:
            img_tag = f'<img src="{img_base64}" style="width:100%; height:100%; object-fit:cover; border-radius:14px;" />'
        else:
            img_tag = f'<div style="font-size: 4.5rem;">{w["emoji"]}</div>'

        card_html = f"""<div class="flashcard-container-dw">
<div class="flashcard-image-dw">{img_tag}</div>
<div style="flex-grow: 1;">
<div class="fc-word-dw">{w['word']}</div>
<div><span class="fc-pinyin-dw">{w['pinyin']}</span></div>
<div class="fc-viet-dw">Nghĩa: {w['vietnamese']}</div>
<div class="fc-story-dw">📖 <b>Tóm tắt sự tích:</b> {w['story']}</div>
<div class="fc-ex-box-dw">
<div style="font-size:0.8em; color:#64748b; font-weight:700;">VÍ DỤ:</div>
<div class="fc-ex-han-dw">{w['example_han']}</div>
<div class="fc-ex-py-dw">{w['example_py']}</div>
<div class="fc-ex-vi-dw">{w['example_vi']}</div>
</div>
</div>
</div>"""

        col_card, col_ctrl = st.columns([4.2, 1.8])
        with col_card:
            st.markdown(card_html, unsafe_allow_html=True)
        with col_ctrl:
            st.markdown("<h4 style='color:#1e293b; margin-top:0;'>🔊 Phát âm</h4>", unsafe_allow_html=True)
            render_play_button(w['word'], "🔊 Phát âm từ", key=f"slide_dw_{w['key_prefix']}_word")
            st.write("")
            render_play_button(w['example_han'], "🔊 Nghe cả câu", key=f"slide_dw_{w['key_prefix']}_ex")

            st.markdown("<hr style='margin:15px 0;'/>", unsafe_allow_html=True)
            st.markdown("<h4 style='color:#1e293b;'>🎮 Điều khiển</h4>", unsafe_allow_html=True)

            col_prev, col_next = st.columns(2)
            with col_prev:
                if st.button("⬅️ Từ trước", use_container_width=True, key="b5dw_prev"):
                    st.session_state[slide_key] = (cur_idx - 1) % len(DW_VOCAB)
                    st.rerun()
            with col_next:
                if st.button("Từ sau ➡️", use_container_width=True, key="b5dw_next"):
                    st.session_state[slide_key] = (cur_idx + 1) % len(DW_VOCAB)
                    st.rerun()

            st.markdown(f"<div style='text-align: center; font-size: 1.25em; font-weight: bold; margin-top: 10px; color:#475569;'>Từ {cur_idx + 1} / {len(DW_VOCAB)}</div>", unsafe_allow_html=True)
            st.progress((cur_idx + 1) / len(DW_VOCAB))

    # --- TAB 3: PHONG TỤC & HOẠT ĐỘNG ---
    with tab_customs:
        st.markdown("""
<h3 style="color: #0f172a;">🎋 Phong tục & Hoạt động tiêu biểu</h3>
<p style="color: #475569;">Bên cạnh ý nghĩa tưởng nhớ Khuất Nguyên, Tết Đoan Ngọ rơi vào dịp nắng nóng cực điểm nên các phong tục cũng mang tính chất xua đuổi côn trùng, phòng trừ dịch bệnh.</p>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
<div style="background-color: #f8fafc; border-left: 4px solid #059669; padding: 15px; border-radius: 8px; margin-bottom: 12px;">
<b>🍙 Gói và ăn bánh tro (吃粽子)</b><br/>
Bánh tro có hình góc nhọn như mũi tên, bọc lá tre. Người miền Bắc chuộng bánh ngọt (nhân chà là), miền Nam thích mặn (thịt ba chỉ, trứng muối).
</div>
<div style="background-color: #f8fafc; border-left: 4px solid #059669; padding: 15px; border-radius: 8px; margin-bottom: 12px;">
<b>🚣 Đua thuyền rồng (赛龙舟)</b><br/>
Hoạt động tập thể sôi nổi nhất. Thuyền đua dài trang trí đầu rồng, chèo theo nhịp trống dồn dập nhằm khơi gợi tinh thần đoàn kết dũng cảm.
</div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
<div style="background-color: #f8fafc; border-left: 4px solid #059669; padding: 15px; border-radius: 8px; margin-bottom: 12px;">
<b>🌿 Treo ngải cứu trước cửa (挂艾草)</b><br/>
Người dân treo ngải cứu trước cửa phòng tránh muỗi rừng và độc trùng mang mầm mống ôn dịch mùa hè.
</div>
<div style="background-color: #f8fafc; border-left: 4px solid #059669; padding: 15px; border-radius: 8px; margin-bottom: 12px;">
<b>👝 Đeo túi thơm thảo dược (佩香包)</b><br/>
Trẻ con đeo túi vải thêu sặc sỡ đựng các vị thảo mộc khô để bảo vệ cơ thể, tránh cảm gió và các côn trùng cắn.
</div>
            """, unsafe_allow_html=True)

        st.markdown("""
<h3 style="color: #0f172a; margin-top: 25px;">🇻🇳 Đối chiếu Văn hóa: Trung Quốc vs Việt Nam</h3>
<div style="overflow-x: auto; margin-bottom: 20px;">
<table style="width: 100%; border-collapse: collapse; background-color: white; border: 1px solid #e2e8f0; border-radius: 8px; font-size: 0.92em;">
<thead>
<tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1; color: #334155; font-weight: bold;">
<th style="padding: 12px; text-align: left; border-right: 1px solid #e2e8f0;">Nội dung</th>
<th style="padding: 12px; text-align: left; border-right: 1px solid #e2e8f0;">🇨🇳 Trung Quốc (端午节)</th>
<th style="padding: 12px; text-align: left;">🇻🇳 Việt Nam (Tết Đoan Ngọ)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid #e2e8f0;">
<td style="padding: 12px; font-weight: bold; border-right: 1px solid #e2e8f0;">Thời gian</td>
<td style="padding: 12px; border-right: 1px solid #e2e8f0;">Mùng 5 tháng 5 Âm lịch</td>
<td style="padding: 12px;">Mùng 5 tháng 5 Âm lịch</td>
</tr>
<tr style="border-bottom: 1px solid #e2e8f0;">
<td style="padding: 12px; font-weight: bold; border-right: 1px solid #e2e8f0;">Nguồn gốc</td>
<td style="padding: 12px; border-right: 1px solid #e2e8f0;">Tưởng nhớ trung thần, nhà thơ Khuất Nguyên</td>
<td style="padding: 12px;">Ngày xua đuổi sâu bọ hại mùa màng & dịch bệnh</td>
</tr>
<tr style="border-bottom: 1px solid #e2e8f0;">
<td style="padding: 12px; font-weight: bold; border-right: 1px solid #e2e8f0;">Món ăn chính</td>
<td style="padding: 12px; border-right: 1px solid #e2e8f0;">Bánh tro hình tam giác (粽子) nhân ngọt/mặn</td>
<td style="padding: 12px;">Cơm rượu nếp, bánh tro (bánh gio) hình thuôn dài, vải, mận</td>
</tr>
<tr style="border-bottom: 1px solid #e2e8f0;">
<td style="padding: 12px; font-weight: bold; border-right: 1px solid #e2e8f0;">Hoạt động tiêu biểu</td>
<td style="padding: 12px; border-right: 1px solid #e2e8f0;">Đua thuyền rồng, treo ngải cứu, bôi rượu hùng hoàng</td>
<td style="padding: 12px;">Khảo cây, ăn quả chua, rượu nếp sáng sớm diệt côn trùng</td>
</tr>
</tbody>
</table>
</div>
        """, unsafe_allow_html=True)

    # --- TAB 4: CÂU CHÚC & GIAO TIẾP ---
    with tab_phrases:
        # Nhúng CSS phong cách cho Card
        st.markdown("""
        <style>
        .dw-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-left: 5px solid #10b981;
            border-radius: 12px;
            padding: 18px;
            margin-bottom: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03), 0 2px 4px -1px rgba(0, 0, 0, 0.02);
            transition: all 0.25s ease;
        }
        .dw-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 20px -3px rgba(16, 185, 129, 0.08);
            border-color: #a7f3d0;
        }
        .dw-card.grammar {
            border-left-color: #f59e0b;
        }
        .dw-card.grammar:hover {
            box-shadow: 0 12px 20px -3px rgba(245, 158, 11, 0.08);
            border-color: #fde68a;
        }
        .dw-card-tag {
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #059669;
            font-weight: 800;
            margin-bottom: 6px;
        }
        .dw-card-tag.grammar-tag {
            color: #d97706;
        }
        .dw-card-han {
            font-size: 1.45rem;
            font-weight: 800;
            color: #0f172a;
            margin-bottom: 4px;
            line-height: 1.3;
        }
        .dw-card-py {
            font-family: 'Courier New', monospace;
            font-size: 1.02rem;
            color: #2563eb;
            font-weight: 700;
            margin-bottom: 4px;
        }
        .dw-card-vi {
            font-size: 0.92rem;
            color: #475569;
            font-style: italic;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("""
<div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border-left: 6px solid #10b981; border-radius: 12px; padding: 20px; margin-bottom: 25px;">
<h4 style="color: #14532d; margin-top: 0; font-weight: bold; display: flex; align-items: center; gap: 8px;">💡 Góc Văn Hóa: Tại sao chúc "Đoan Ngọ An Khang" (端午安康)?</h4>
<p style="color: #166534; line-height: 1.6; margin-bottom: 0; font-size: 0.98em;">
Nhiều người quan niệm ngày này gắn liền với cái chết thương tâm của Khuất Nguyên và sự bùng phát ôn dịch mùa hè. Do đó chúc <b>快乐 (kuàilè - Vui vẻ)</b> đôi khi bị cho là chưa phù hợp. Thay vào đó, lời chúc ý nghĩa nhất là <b>安康 (ānkāng - Bình an và Khỏe mạnh)</b> để cầu mong sự an lành, tai qua nạn khỏi.
</p>
</div>
        """, unsafe_allow_html=True)

        st.markdown("### 💬 Lời chúc & Khẩu ngữ Giao tiếp ngày Tết")
        
        # Câu 1
        col_c1, col_a1 = st.columns([8.2, 1.8])
        with col_c1:
            st.markdown("""
            <div class="dw-card">
                <div class="dw-card-tag">💬 Lời chúc ý nghĩa nhất</div>
                <div class="dw-card-han">端午安康！</div>
                <div class="dw-card-py">Duānwǔ ānkāng!</div>
                <div class="dw-card-vi">Chúc Đoan Ngọ an khang! (Cầu bình an, sức khỏe)</div>
            </div>
            """, unsafe_allow_html=True)
        with col_a1:
            st.write("<br><div style='height: 8px;'></div>", unsafe_allow_html=True)
            render_play_button("端午安康", "🔊 Nghe chúc", key="dw_p1_new")

        # Câu 2
        col_c2, col_a2 = st.columns([8.2, 1.8])
        with col_c2:
            st.markdown("""
            <div class="dw-card">
                <div class="dw-card-tag">💬 Lời chúc phổ biến</div>
                <div class="dw-card-han">端午节快乐！</div>
                <div class="dw-card-py">Duānwǔ Jié kuàilè!</div>
                <div class="dw-card-vi">Tết Đoan Ngọ vui vẻ!</div>
            </div>
            """, unsafe_allow_html=True)
        with col_a2:
            st.write("<br><div style='height: 8px;'></div>", unsafe_allow_html=True)
            render_play_button("端午节快乐", "🔊 Nghe chúc", key="dw_p2_new")

        # Câu 3
        col_c3, col_a3 = st.columns([8.2, 1.8])
        with col_c3:
            st.markdown("""
            <div class="dw-card">
                <div class="dw-card-tag">🗣️ Câu hỏi thăm</div>
                <div class="dw-card-han">你吃粽子了吗？</div>
                <div class="dw-card-py">Nǐ chī zòngzi le ma?</div>
                <div class="dw-card-vi">Bạn ăn bánh tro/bánh ú chưa?</div>
            </div>
            """, unsafe_allow_html=True)
        with col_a3:
            st.write("<br><div style='height: 8px;'></div>", unsafe_allow_html=True)
            render_play_button("你吃粽子了吗？", "🔊 Nghe mẫu", key="dw_p3_new")

        # Câu 4
        col_c4, col_a4 = st.columns([8.2, 1.8])
        with col_c4:
            st.markdown("""
            <div class="dw-card">
                <div class="dw-card-tag">🗣️ Bày tỏ sở thích</div>
                <div class="dw-card-han">我很喜欢吃粽子。</div>
                <div class="dw-card-py">Wǒ hěn xǐhuān chī zòngzi.</div>
                <div class="dw-card-vi">Tôi rất thích ăn bánh tro/bánh ú.</div>
            </div>
            """, unsafe_allow_html=True)
        with col_a4:
            st.write("<br><div style='height: 8px;'></div>", unsafe_allow_html=True)
            render_play_button("我很喜欢吃粽子。", "🔊 Nghe mẫu", key="dw_p4_new")

        st.markdown("<br><hr style='border-color: #cbd5e1;'/><br>", unsafe_allow_html=True)
        st.markdown("### 🎯 Các mẫu câu ngữ pháp HSK 1 ngày Tết Đoan Ngọ")

        # Cấu trúc 1
        col_g1_card, col_g1_btn = st.columns([8.2, 1.8])
        with col_g1_card:
            st.markdown("""
            <div class="dw-card grammar">
                <div class="dw-card-tag grammar-tag">1. Giới thiệu ngày lễ (Ngày tháng + 是 + Tên ngày lễ)</div>
                <div class="dw-card-han">今天是五月五号，端午节。</div>
                <div class="dw-card-py">Jīntiān shì wǔ yuè wǔ hào, Duānwǔ jié.</div>
                <div class="dw-card-vi">Hôm nay là ngày 5 tháng 5, Tết Đoan Ngọ.</div>
            </div>
            """, unsafe_allow_html=True)
        with col_g1_btn:
            st.write("<br><div style='height: 8px;'></div>", unsafe_allow_html=True)
            render_play_button("今天是五月五号，端午节。", "🔊 Nghe câu", key="dw_grammar_p1_new")

        # Cấu trúc 2
        col_g2_card, col_g2_btn = st.columns([8.2, 1.8])
        with col_g2_card:
            st.markdown("""
            <div class="dw-card grammar">
                <div class="dw-card-tag grammar-tag">2. Nói về hoạt động ăn uống (Ai + 吃 + Cái gì)</div>
                <div class="dw-card-han">中国人吃粽子。/ 越南人也吃粽子。</div>
                <div class="dw-card-py">Zhōngguó rén chī zòngzi. / Yuènán rén yě chī zòngzi.</div>
                <div class="dw-card-vi">Người Trung Quốc ăn bánh ú. / Người Việt Nam cũng ăn bánh ú.</div>
            </div>
            """, unsafe_allow_html=True)
        with col_g2_btn:
            st.write("<br><div style='height: 8px;'></div>", unsafe_allow_html=True)
            render_play_button("中国人吃粽子。越南人也吃粽子。", "🔊 Nghe cả hai", key="dw_grammar_p2_new")

        # Cấu trúc 3
        col_g3_card, col_g3_btn = st.columns([8.2, 1.8])
        with col_g3_card:
            st.markdown("""
            <div class="dw-card grammar">
                <div class="dw-card-tag grammar-tag">3. Nói về sở thích (Ai + 喜欢吃 + Trái cây)</div>
                <div class="dw-card-han">我喜欢吃水果。</div>
                <div class="dw-card-py">Wǒ xǐhuan chī shuǐguǒ.</div>
                <div class="dw-card-vi">Tôi thích ăn hoa quả (vải, mận...).</div>
            </div>
            """, unsafe_allow_html=True)
        with col_g3_btn:
            st.write("<br><div style='height: 8px;'></div>", unsafe_allow_html=True)
            render_play_button("我喜欢吃水果。", "🔊 Nghe câu", key="dw_grammar_p3_new")

        # Cấu trúc 4
        col_g4_card, col_g4_btn = st.columns([8.2, 1.8])
        with col_g4_card:
            st.markdown("""
            <div class="dw-card grammar">
                <div class="dw-card-tag grammar-tag">4. Thể hiện cảm xúc (太 + Tính từ + 了)</div>
                <div class="dw-card-han">今天我太高兴了！</div>
                <div class="dw-card-py">Jīntiān wǒ tài gāoxìng le!</div>
                <div class="dw-card-vi">Hôm nay tôi vui quá rồi!</div>
            </div>
            """, unsafe_allow_html=True)
        with col_g4_btn:
            st.write("<br><div style='height: 8px;'></div>", unsafe_allow_html=True)
            render_play_button("今天我太高兴了！", "🔊 Nghe câu", key="dw_grammar_p4_new")

    # --- TAB 5: TRẮC NGHIỆM VUI ---
    with tab_quiz:
        st.markdown("### 📝 Trắc nghiệm kiểm tra kiến thức nhanh")
        st.write("Chọn đáp án đúng nhất để kiểm tra khả năng nhớ bài của bạn!")

        q1 = st.radio(
            "**Câu 1: 端午节是几月几号？(Tết Đoan Ngọ là ngày tháng mấy?)**",
            ["A. 一月一号 (Mùng 1 tháng 1)", "B. 五月初五 (Mùng 5 tháng 5 Âm lịch)", "C. 八月十五 (Mười lăm tháng 8 Âm lịch)", "D. 九月九号 (Mùng 9 tháng 9)"],
            key="dw_q1_radio"
        )
        q2 = st.radio(
            "**Câu 2: 端午节吃什么？(Tết Đoan Ngọ ăn gì?)**",
            ["A. 月饼 (Bánh trung thu)", "B. 饺子 (Sủi cảo)", "C. 粽子 (Bánh tro / bánh ú)", "D. 汤圆 (Bánh trôi nước)"],
            key="dw_q2_radio"
        )
        q3 = st.radio(
            "**Câu 3: 端午节纪念哪位伟大的爱国诗人？(Tết Đoan Ngọ tưởng nhớ nhà thơ yêu nước vĩ đại nào?)**",
            ["A. 孔子 (Khổng Tử)", "B. 屈原 (Khuất Nguyên)", "C. 李白 (Lý Bạch)", "D. 杜甫 (Đỗ Phủ)"],
            key="dw_q3_radio"
        )
        q4 = st.radio(
            "**Câu 4: Hoạt động thể thao sôi động nhất trong ngày Tết Đoan Ngọ (赛龙舟) là gì?**",
            ["A. Đua thuyền rồng", "B. Đua ngựa", "C. Thả diều", "D. Chèo thuyền buồm"],
            key="dw_q4_radio"
        )
        q5 = st.radio(
            "**Câu 5: Người xưa treo gì ở cổng nhà dịp Đoan Ngọ để đuổi độc trùng, phòng tà dịch?**",
            ["A. 春联 (Câu đối đỏ)", "B. 艾草 (Ngải cứu)", "C. 灯笼 (Đèn lồng)", "D. 菊花 (Hoa cúc)"],
            key="dw_q5_radio"
        )
        q6 = st.radio(
            "**Câu 6: Lời chúc Tết Đoan Ngọ truyền thống trang trọng và tinh tế nhất là gì?**",
            ["A. 新年快乐 (Chúc mừng năm mới)", "B. 生日快乐 (Sinh nhật vui vẻ)", "C. 端午安康 (Đoan Ngọ an khang)", "D. 万事如意 (Vạn sự như ý)"],
            key="dw_q6_radio"
        )

        if st.button("📊 Nộp bài & Kiểm tra kết quả", use_container_width=True, key="dw_submit_btn"):
            score = 0
            correct_answers = {
                "q1": "B. 五月初五 (Mùng 5 tháng 5 Âm lịch)",
                "q2": "C. 粽子 (Bánh tro / bánh ú)",
                "q3": "B. 屈原 (Khuất Nguyên)",
                "q4": "A. Đua thuyền rồng",
                "q5": "B. 艾草 (Ngải cứu)",
                "q6": "C. 端午安康 (Đoan Ngọ an khang)"
            }

            user_answers = {
                "q1": q1,
                "q2": q2,
                "q3": q3,
                "q4": q4,
                "q5": q5,
                "q6": q6
            }

            # Check answers
            is_q1_correct = user_answers["q1"] == correct_answers["q1"]
            is_q2_correct = user_answers["q2"] == correct_answers["q2"]
            is_q3_correct = user_answers["q3"] == correct_answers["q3"]
            is_q4_correct = user_answers["q4"] == correct_answers["q4"]
            is_q5_correct = user_answers["q5"] == correct_answers["q5"]
            is_q6_correct = user_answers["q6"] == correct_answers["q6"]

            if is_q1_correct: score += 1
            if is_q2_correct: score += 1
            if is_q3_correct: score += 1
            if is_q4_correct: score += 1
            if is_q5_correct: score += 1
            if is_q6_correct: score += 1

            st.markdown("---")
            if score == 6:
                st.balloons()
                st.success(f"🎉 Xuất sắc! Bạn trả lời đúng 6/6 câu hỏi. Bạn đã hoàn toàn làm chủ kiến thức văn hóa về Tết Đoan Ngọ!")
            else:
                st.info(f"📊 Kết quả của bạn: {score}/6 câu đúng. Hãy xem chi tiết giải đáp bên dưới để ghi nhớ tốt hơn:")

            # Render feedback details
            def render_quiz_feedback(q_num, is_correct, user_val, correct_val):
                if is_correct:
                    st.markdown(f"✅ **Câu {q_num}**: Đúng! Bạn đã chọn `{user_val}`.")
                else:
                    st.markdown(f"❌ **Câu {q_num}**: Chưa đúng. Bạn chọn `{user_val}`. Đáp án đúng là: `{correct_val}`.")

            render_quiz_feedback(1, is_q1_correct, q1, correct_answers["q1"])
            render_quiz_feedback(2, is_q2_correct, q2, correct_answers["q2"])
            render_quiz_feedback(3, is_q3_correct, q3, correct_answers["q3"])
            render_quiz_feedback(4, is_q4_correct, q4, correct_answers["q4"])
            render_quiz_feedback(5, is_q5_correct, q5, correct_answers["q5"])
            render_quiz_feedback(6, is_q6_correct, q6, correct_answers["q6"])


def show_lesson5_classroom_practice():
    import random
    render_lesson_intro(
        title="🗣️ Bài 5.1 - Thực hành Giao tiếp & Phản xạ trên lớp",
        objective="Tích hợp kiến thức của cả Bài 5 (Vận mẫu mũi, số đếm từ 0-10 và cách dùng phó từ 很/非常/太) vào các hoạt động thực hành khẩu ngữ tương tác trực tiếp trên lớp."
    )

    tab_reflex, tab_builder, tab_roleplay, tab_music = st.tabs([
        "🎲 1. Phản xạ Siêu tốc",
        "✍️ 2. Máy ghép câu Tích hợp",
        "🎭 3. Kịch bản Đóng vai",
        "🎵 4. Góc Âm Nhạc (手指歌)"
    ])

    # --- TAB 1: PHẢN XẠ SIÊU TỐC ---
    with tab_reflex:
        st.markdown("""
        <div style="background-color: #eff6ff; border-left: 6px solid #3b82f6; padding: 18px; border-radius: 12px; margin-bottom: 20px;">
            <h4 style="color: #1e3a8a; margin-top: 0; font-weight: bold;">🎲 Thử thách phản xạ Số đếm + Mức độ + Âm mũi</h4>
         
        </div>
        """, unsafe_allow_html=True)

        # Trạng thái session_state cho game phản xạ
        if "reflex_num" not in st.session_state:
            st.session_state.reflex_num = "五 (5)"
            st.session_state.reflex_adv = "非常 (vô cùng)"
            st.session_state.reflex_adj = "忙 (bận - chứa âm mũi /ang/)"
            st.session_state.reflex_target = "Ví dụ: 五个人非常忙。 (5 người vô cùng bận.)"
            st.session_state.reflex_audio = "五个人非常忙。"

        numbers_pool = [
            {"zh": "一 (1)", "val": "1"},
            {"zh": "二 (2)", "val": "2"},
            {"zh": "三 (3)", "val": "3"},
            {"zh": "四 (4)", "val": "4"},
            {"zh": "五 (5)", "val": "5"},
            {"zh": "六 (6)", "val": "6"},
            {"zh": "七 (7)", "val": "7"},
            {"zh": "八 (8)", "val": "8"},
            {"zh": "九 (9)", "val": "9"},
            {"zh": "十 (10)", "val": "10"}
        ]
        adv_pool = [
            {"zh": "很 (rất)", "val": "很"},
            {"zh": "非常 (vô cùng)", "val": "非常"},
            {"zh": "太...了 (quá... rồi)", "val": "太"}
        ]
        adj_pool = [
            {"zh": "忙 (bận - âm mũi /ang/)", "val": "忙", "eg": "个人hěn忙 / người rất bận"},
            {"zh": "累 (mệt)", "val": "累", "eg": "个人非常累 / người vô cùng mệt"},
            {"zh": "高兴 (vui vẻ - âm mũi /ing/)", "val": "高兴", "eg": "个人太高兴了 / người vui quá rồi"},
            {"zh": "红 (đỏ - âm mũi /ong/)", "val": "红", "eg": "个苹果很hóng / quả táo rất đỏ"},
            {"zh": "吃粽子 (ăn bánh ú - âm mũi /ing/)", "val": "吃粽子", "eg": "个人喜欢吃粽子 / người thích ăn bánh ú"}
        ]

        if st.button("🎰 Tạo thử thách ngẫu nhiên!", use_container_width=True, key="btn_rand_reflex"):
            r_num = random.choice(numbers_pool)
            r_adv = random.choice(adv_pool)
            r_adj = random.choice(adj_pool)
            
            st.session_state.reflex_num = r_num["zh"]
            st.session_state.reflex_adv = r_adv["zh"]
            st.session_state.reflex_adj = r_adj["zh"]
            
            # Xây dựng câu ví dụ
            num_val = r_num["val"]
            adv_val = r_adv["val"]
            adj_val = r_adj["val"]
            
            if adj_val == "红":
                if adv_val == "太":
                    st.session_state.reflex_target = f"Ví dụ: {num_val}个苹果太红了！ ({num_val} quả táo đỏ quá rồi!)"
                    st.session_state.reflex_audio = f"{num_val}个苹果太红了"
                else:
                    st.session_state.reflex_target = f"Ví dụ: {num_val}个苹果{adv_val}红。 ({num_val} quả táo {adv_val.replace('很', 'rất').replace('非常', 'vô cùng')} đỏ.)"
                    st.session_state.reflex_audio = f"{num_val}个苹果{adv_val}红"
            elif adj_val == "吃粽子":
                st.session_state.reflex_target = f"Ví dụ: {num_val}个人{adv_val.replace('太', '很')}喜欢吃粽子。 ({num_val} người {adv_val.replace('太', 'rất').replace('很', 'rất').replace('非常', 'vô cùng')} thích ăn bánh ú.)"
                st.session_state.reflex_audio = f"{num_val}个人很喜欢吃粽子"
            else:
                if adv_val == "太":
                    st.session_state.reflex_target = f"Ví dụ: {num_val}个人太{adj_val}了！ ({num_val} người {adj_val.replace('忙', 'bận').replace('累', 'mệt').replace('高兴', 'vui')} quá rồi!)"
                    st.session_state.reflex_audio = f"{num_val}个人太{adj_val}了"
                else:
                    st.session_state.reflex_target = f"Ví dụ: {num_val}个人{adv_val}{adj_val}。 ({num_val} người {adv_val.replace('很', 'rất').replace('非常', 'vô cùng')} {adj_val.replace('忙', 'bận').replace('累', 'mệt').replace('高兴', 'vui')}.)"
                    st.session_state.reflex_audio = f"{num_val}个人{adv_val}{adj_val}"
            st.rerun()

        # Hiển thị thử thách dạng thẻ lớn
        st.markdown(f"""
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin-top: 10px; margin-bottom: 20px;">
            <div style="background: #fffbeb; border: 2px solid #fde68a; border-radius: 12px; padding: 20px; text-align: center;">
                <span style="font-size: 0.85em; color: #b45309; font-weight: bold; text-transform: uppercase;">🔢 Số lượng:</span>
                <div style="font-size: 1.8rem; font-weight: 800; color: #d97706; margin-top: 8px;">{st.session_state.reflex_num}</div>
            </div>
            <div style="background: #fdf2f8; border: 2px solid #fbcfe8; border-radius: 12px; padding: 20px; text-align: center;">
                <span style="font-size: 0.85em; color: #be185d; font-weight: bold; text-transform: uppercase;">⚡ Mức độ:</span>
                <div style="font-size: 1.8rem; font-weight: 800; color: #db2777; margin-top: 8px;">{st.session_state.reflex_adv}</div>
            </div>
            <div style="background: #f0fdf4; border: 2px solid #bbf7d0; border-radius: 12px; padding: 20px; text-align: center;">
                <span style="font-size: 0.85em; color: #15803d; font-weight: bold; text-transform: uppercase;">👄 Từ khóa (Âm mũi):</span>
                <div style="font-size: 1.6rem; font-weight: 800; color: #16a34a; margin-top: 8px;">{st.session_state.reflex_adj}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.info(f"💡 {st.session_state.reflex_target}")
        render_play_button(st.session_state.reflex_audio, "🔊 Nghe phát âm gợi ý", key="reflex_audio_btn")

    # --- TAB 2: MÁY GHÉP CÂU TÍCH HỢP ---
    with tab_builder:
        st.markdown("""
        <div style="background-color: #fdf6f0; border-left: 6px solid #d97706; padding: 18px; border-radius: 12px; margin-bottom: 20px;">
            <h4 style="color: #b45309; margin-top: 0; font-weight: bold;">✍️ Luyện viết và ghép câu tích hợp</h4>
            <p style="color: #b45309; font-size: 0.95em; line-height: 1.5; margin-bottom: 0;">
                Học viên tự chọn các thành phần ngữ pháp trong bảng để ghép thành câu. Máy sẽ tự động dịch nghĩa, hiển thị bính âm và phát âm chuẩn để luyện đọc.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_sub, col_num, col_deg, col_act = st.columns(4)
        
        with col_sub:
            sub_opt = st.selectbox("1. Chủ ngữ (Âm mũi):", [
                "我 (tôi)", "您 (ngài)", "朋友 (bạn)", "中国人 (người Trung Quốc)", "越南人 (người Việt Nam)"
            ], key="b51_sub")
        with col_num:
            num_opt = st.selectbox("2. Số lượng (Số đếm):", [
                "(Không chọn)", "一个 (1 người/cái)", "三个 (3 người/cái)", "五个 (5 người/cái)", "八个 (8 người/cái)", "十个 (10 người/cái)"
            ], key="b51_num")
        with col_deg:
            deg_opt = st.selectbox("3. Phó từ mức độ:", [
                "很 (rất)", "非常 (vô cùng)", "太 (quá... rồi)", "(Không chọn)"
            ], key="b51_deg")
        with col_act:
            act_opt = st.selectbox("4. Tính từ / Hoạt động:", [
                "忙 (bận)", "累 (mệt)", "高兴 (vui vẻ)", "吃粽子 (ăn bánh tro)"
            ], key="b51_act")

        # Xử lý ghép câu
        sub_zh = sub_opt.split(" ")[0]
        act_zh = act_opt.split(" ")[0]
        
        num_zh = "" if "Không" in num_opt else num_opt.split(" ")[0]
        deg_zh = "" if "Không" in deg_opt else deg_opt.split(" ")[0]

        # Xây dựng câu hoàn chỉnh
        full_zh = ""
        translation = ""
        pinyin_text = ""

        # Dịch các thành phần để hiển thị nghĩa tiếng Việt
        sub_vi = "Tôi" if sub_zh == "我" else "Ngài" if sub_zh == "您" else "Bạn bè" if sub_zh == "朋友" else "Người Trung Quốc" if sub_zh == "中国人" else "Người Việt Nam"
        num_vi = "" if not num_zh else "1 người/cái" if "一" in num_zh else "3 người/cái" if "三" in num_zh else "5 người/cái" if "五" in num_zh else "8 người/cái" if "八" in num_zh else "10 người/cái"
        deg_vi = "rất" if deg_zh == "很" else "vô cùng" if deg_zh == "非常" else "quá" if deg_zh == "太" else ""
        act_vi = "bận" if act_zh == "忙" else "mệt" if act_zh == "累" else "vui vẻ" if act_zh == "高兴" else "ăn bánh tro"

        # Cấu trúc câu
        if num_zh:
            classifier = "个"
            num_clean = num_zh.replace("个", "")
            
            if act_zh == "吃粽子":
                full_zh = f"{num_clean}个人"
                pinyin_text = f"{num_clean.replace('一','yī').replace('三','sān').replace('五','wǔ').replace('八','bā').replace('十','shí')} gè rén "
                
                if deg_zh == "太":
                    full_zh += "太喜欢吃粽子了"
                    pinyin_text += "tài xǐhuān chī zòngzi le"
                    translation = f"{num_vi.replace('người/cái', 'người')} thích ăn bánh tro quá rồi"
                else:
                    d_z = "很" if not deg_zh else deg_zh
                    full_zh += f"{d_z}喜欢吃粽子"
                    pinyin_text += f"{'hěn' if d_z=='很' else 'fēicháng'} xǐhuān chī zòngzi"
                    translation = f"{num_vi.replace('người/cái', 'người')} {deg_vi or 'rất'} thích ăn bánh tro"
            else:
                if deg_zh == "太":
                    full_zh = f"{num_clean}个人太{act_zh}了"
                    pinyin_text = f"{num_clean.replace('一','yī').replace('三','sān').replace('五','wǔ').replace('八','bā').replace('十','shí')} gè rén tài { 'máng' if act_zh=='忙' else 'lèi' if act_zh=='累' else 'gāoxìng' } le"
                    translation = f"{num_vi.replace('người/cái', 'người')} {act_vi} quá rồi"
                else:
                    d_z = "很" if not deg_zh else deg_zh
                    full_zh = f"{num_clean}个人{d_z}{act_zh}"
                    pinyin_text = f"{num_clean.replace('一','yī').replace('三','sān').replace('五','wǔ').replace('八','bā').replace('十','shí')} gè rén {'hěn' if d_z=='很' else 'fēicháng'} {'máng' if act_zh=='忙' else 'lèi' if act_zh=='累' else 'gāoxìng'}"
                    translation = f"{num_vi.replace('người/cái', 'người')} {deg_vi or 'rất'} {act_vi}"
        else:
            if act_zh == "吃粽子":
                if deg_zh == "太":
                    full_zh = f"{sub_zh}太喜欢吃粽子了"
                    pinyin_text = f"{'wǒ' if sub_zh=='我' else 'nín' if sub_zh=='您' else 'péngyou' if sub_zh=='朋友' else 'Zhōngguórén' if sub_zh=='中国人' else 'Yuènánrén'} tài xǐhuān chī zòngzi le"
                    translation = f"{sub_vi} thích ăn bánh tro quá rồi"
                else:
                    d_z = "很" if not deg_zh else deg_zh
                    full_zh = f"{sub_zh}{d_z}喜欢吃粽子"
                    pinyin_text = f"{'wǒ' if sub_zh=='我' else 'nín' if sub_zh=='您' else 'péngyou' if sub_zh=='朋友' else 'Zhōngguórén' if sub_zh=='中国人' else 'Yuènánrén'} {'hěn' if d_z=='很' else 'fēicháng'} xǐhuān chī zòngzi"
                    translation = f"{sub_vi} {deg_vi or 'rất'} thích ăn bánh tro"
            else:
                if deg_zh == "太":
                    full_zh = f"{sub_zh}太{act_zh}了"
                    pinyin_text = f"{'wǒ' if sub_zh=='我' else 'nín' if sub_zh=='您' else 'péngyou' if sub_zh=='朋友' else 'Zhōngguórén' if sub_zh=='中国人' else 'Yuènánrén'} tài {'máng' if act_zh=='忙' else 'lèi' if act_zh=='累' else 'gāoxìng'} le"
                    translation = f"{sub_vi} {act_vi} quá rồi"
                else:
                    d_z = "很" if not deg_zh else deg_zh
                    full_zh = f"{sub_zh}{d_z}{act_zh}"
                    pinyin_text = f"{'wǒ' if sub_zh=='wǒ' or sub_zh=='我' else 'nín' if sub_zh=='您' else 'péngyou' if sub_zh=='朋友' else 'Zhōngguórén' if sub_zh=='中国人' else 'Yuènánrén'} {'hěn' if d_z=='很' else 'fēicháng'} {'máng' if act_zh=='忙' else 'lèi' if act_zh=='累' else 'gāoxìng'}"
                    translation = f"{sub_vi} {deg_vi or 'rất'} {act_vi}"

        # Sửa pinyin chuẩn
        pinyin_text = pinyin_text.strip().capitalize()
        pinyin_text = pinyin_text.replace("wǒ", "Wǒ").replace("nín", "Nín").replace("péngyou", "Péngyou")

        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #fdf6f0 0%, #ffedd5 100%); border: 2px solid #fed7aa; border-radius: 16px; padding: 25px; margin-top: 15px; margin-bottom: 15px; text-align: center;">
            <span style="font-size: 0.85em; color: #ea580c; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em;">CÂU HOÀN CHỈNH VỪA GHÉP:</span>
            <div style="font-size: 2.2rem; font-weight: 800; color: #7c2d12; margin: 10px 0;">{full_zh}</div>
            <div style="font-family: 'Courier New', monospace; font-size: 1.25rem; font-weight: bold; color: #2563eb; margin-bottom: 8px;">{pinyin_text}</div>
            <div style="font-size: 1.1rem; color: #475569; font-style: italic;">Nghĩa: {translation}.</div>
        </div>
        """, unsafe_allow_html=True)

        render_play_button(full_zh, "🔊 Phát âm câu vừa ghép", key="builder_play_integrated_btn")

    # --- TAB 3: KỊCH BẢN ĐỒNG VAI ---
    with tab_roleplay:
        st.markdown("""
        <div style="background-color: #f0fdf4; border-left: 6px solid #10b981; padding: 18px; border-radius: 12px; margin-bottom: 20px;">
            <h4 style="color: #14532d; margin-top: 0; font-weight: bold;">🎭 Kịch bản Đóng vai: Giao dịch ngày Tết Đoan Ngọ</h4>
            <p style="color: #14532d; font-size: 0.95em; line-height: 1.5; margin-bottom: 0;">
                Tình huống: Học viên đóng vai Khách mua (A) và Chủ quán (B) để thực hiện giao dịch mua bán bánh ú/hoa quả ngày Tết Đoan Ngọ, sử dụng số đếm và từ chỉ mức độ.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_rp1, col_rp2 = st.columns(2)
        with col_rp1:
            item_type = st.selectbox("Chọn loại hàng mua:", [
                "粽子 (Bánh ú / Bánh tro - âm mũi /ing/)",
                "水果 (Hoa quả / Trái cây - HSK 1)"
            ], key="rp_item")
        with col_rp2:
            qty_val = st.slider("Số lượng mua (Số đếm):", 1, 10, 5, key="rp_qty")

        # Chuẩn bị dữ liệu cho kịch bản
        item_zh = "粽子" if "粽子" in item_type else "水果"
        item_vi = "bánh ú" if item_zh == "粽子" else "hoa quả"
        
        qty_zh = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"][qty_val]
        qty_py = ["líng", "yī", "èr", "sān", "sì", "wǔ", "liù", "qī", "bā", "jiǔ", "shí"][qty_val]

        st.markdown("### 🗣️ Kịch bản Giao tiếp A vs B:")

        # Cặp thoại 1: Khách hỏi mua
        st.markdown(f"""
        <div style="background:#f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 12px; margin-bottom: 8px;">
            <b style="color: #2563eb;">👤 Nhân vật A (Khách mua):</b><br/>
            <span style="font-size: 1.15em; font-weight: 700; color: #0f172a;">你好！我要买{qty_zh}个{item_zh}。</span><br/>
            <span style="font-family: monospace; color: #2563eb; font-size: 0.9em;">Nǐ hǎo! Wǒ yào mǎi {qty_py} gè {item_zh == '粽子' and 'zòngzi' or 'shuǐguǒ'}.</span><br/>
            <span style="color: #475569; font-style: italic; font-size: 0.9em;">(Xin chào! Tôi muốn mua {qty_val} cái/quả {item_vi}.)</span>
        </div>
        """, unsafe_allow_html=True)
        render_play_button(f"你好！我要买{qty_zh}个{item_zh}。", "🔊 Phát âm A1", key="rp_play_a1")

        # Cặp thoại 2: Chủ quán báo giá
        price_num = qty_val * 2
        price_zh = ["零", "二", "四", "六", "八", "十", "十二", "十四", "十六", "十八", "二十"][qty_val]
        price_py = ["líng", "èr", "sì", "liù", "bā", "shí", "shí'èr", "shísì", "shíliù", "shíbā", "èrshí"][qty_val]
        
        st.markdown(f"""
        <div style="background:#f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 12px; margin-bottom: 8px; margin-top: 15px;">
            <b style="color: #16a34a;">👤 Nhân vật B (Chủ quán):</b><br/>
            <span style="font-size: 1.15em; font-weight: 700; color: #0f172a;">好的。{qty_zh}个{item_zh}，一共{price_zh}块钱。</span><br/>
            <span style="font-family: monospace; color: #2563eb; font-size: 0.9em;">Hǎo de. {qty_py} gè {item_zh == '粽子' and 'zòngzi' or 'shuǐguǒ'}, yīgòng {price_py} kuài qián.</span><br/>
            <span style="color: #475569; font-style: italic; font-size: 0.9em;">(Dạ được. {qty_val} {item_vi}, tổng cộng là {price_num} đồng.)</span>
        </div>
        """, unsafe_allow_html=True)
        render_play_button(f"好的。{qty_zh}个{item_zh}，一共{price_zh}块钱。", "🔊 Phát âm B1", key="rp_play_b1")

        # Cặp thoại 3: Khách nhận xét và cảm xúc
        st.markdown(f"""
        <div style="background:#f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 12px; margin-bottom: 8px; margin-top: 15px;">
            <b style="color: #2563eb;">👤 Nhân vật A (Khách mua):</b><br/>
            <span style="font-size: 1.15em; font-weight: 700; color: #0f172a;">这个{item_zh}非常红，非常好吃！今天我太高兴了！</span><br/>
            <span style="font-family: monospace; color: #2563eb; font-size: 0.9em;">Zhège {item_zh == '粽子' and 'zòngzi' or 'shuǐguǒ'} fēicháng hóng, fēicháng hǎochī! Jīntiān wǒ tài gāoxìng le!</span><br/>
            <span style="color: #475569; font-style: italic; font-size: 0.9em;">({item_zh == '粽子' and 'Bánh ú' or 'Hoa quả'} này vô cùng đỏ, vô cùng ngon! Hôm nay tôi vui quá rồi!)</span>
        </div>
        """, unsafe_allow_html=True)
        render_play_button(f"这个{item_zh}非常红，非常好吃！今天我太高兴了！", "🔊 Phát âm A2", key="rp_play_a2")

    # --- TAB 4: GÓC ÂM NHẠC (手指歌) ---
    with tab_music:
        st.markdown("""
        <div style="background-color: #fdf2f8; border-left: 6px solid #db2777; padding: 18px; border-radius: 12px; margin-bottom: 20px;">
            <h4 style="color: #9d174d; margin-top: 0; font-weight: bold; display: flex; align-items: center; gap: 8px;">🎵 Góc Âm Nhạc: Bài hát "Đếm ngón tay" (手指歌 - Shǒuzhǐ Gē)</h4>
            <p style="color: #9d174d; font-size: 0.95em; line-height: 1.5; margin-bottom: 0;">
                Học đếm số từ 1 đến 10 cực kỳ vui nhộn qua bài hát đồng dao và kết hợp làm các động tác ngón tay. Nhấn nút để nghe từng câu hát chậm hoặc xem clip nhạc sinh động ở bên dưới nhé!
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Nhúng clip Youtube bài hát 手指歌
        st.markdown("### 📺 Video Clip Nhạc Đồng Dao:")
        st.video("https://www.youtube.com/watch?v=R3nN42qWf4M")

        st.markdown("### 📝 Lời bài hát & Phát âm từng câu:")

        song_lyrics = [
            {"num": "1", "zh": "一一只小鸡叽叽叽", "py": "Yī yī zhī xiǎojī jījījī", "vi": "Một, một chú gà con kêu chi chíp"},
            {"num": "2", "zh": "二二只小鸭嘎嘎嘎", "py": "Èr èr zhī xiǎoyā gāgāgā", "vi": "Hai, hai chú vịt con kêu cạp cạp"},
            {"num": "3", "zh": "三三只小鱼游游游", "py": "Sān sān zhī xiǎoyú yóu yóu yóu", "vi": "Ba, ba chú cá nhỏ bơi lội"},
            {"num": "4", "zh": "四四只小猫喵喵喵", "py": "Sì sì zhī xiǎomāo miāo miāo miāo", "vi": "Bốn, bốn chú mèo con kêu meo meo"},
            {"num": "5", "zh": "五五只小兔跳跳跳", "py": "Wǔ wǔ zhī xiǎotù tiào tiào tiào", "vi": "Năm, năm chú thỏ con nhảy nhảy nhảy"},
            {"num": "6", "zh": "六六只小孔雀开屏了", "py": "Liù liù zhī xiǎokǒngquè kāipíng le", "vi": "Sáu, sáu chú công nhỏ xòe đuôi hoa"},
            {"num": "7", "zh": "七七只小蜜蜂采蜜忙", "py": "Qī qī zhī xiǎomìfēng cǎimì máng", "vi": "Bảy, bảy chú ong nhỏ bận rộn hút mật"},
            {"num": "8", "zh": "八八只小螃蟹爬爬爬", "py": "Bā bā zhī xiǎopángxiè pá pá pá", "vi": "Tám, tám chú cua nhỏ bò bò bò"},
            {"num": "9", "zh": "九九只小松鼠上大树", "py": "Jiǔ jiǔ zhī xiǎosōngshǔ shàng dàshù", "vi": "Chín, chín chú sóc nhỏ leo cây lớn"},
            {"num": "10", "zh": "十十个小朋友哈哈笑", "py": "Shí shí gè xiǎopéngyǒu hāhā xiào", "vi": "Mười, mười bạn nhỏ cười ha ha ha"}
        ]

        for idx, item in enumerate(song_lyrics):
            col_l, col_r = st.columns([7.5, 2.5])
            with col_l:
                st.markdown(f"""
                <div style="background: white; border: 1px solid #fbcfe8; border-radius: 10px; padding: 12px; margin-bottom: 8px; border-left: 5px solid #db2777;">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="background: #db2777; color: white; border-radius: 50%; width: 25px; height: 25px; display: inline-flex; justify-content: center; align-items: center; font-weight: bold; font-size: 0.85em;">{item['num']}</span>
                        <span style="font-size: 1.25rem; font-weight: bold; color: #1e293b;">{item['zh']}</span>
                    </div>
                    <div style="font-family: monospace; color: #db2777; margin-left: 35px; font-weight: bold; font-size: 0.95em;">{item['py']}</div>
                    <div style="color: #4b5563; font-style: italic; margin-left: 35px; font-size: 0.9em;">({item['vi']})</div>
                </div>
                """, unsafe_allow_html=True)
            with col_r:
                st.markdown("<br/>", unsafe_allow_html=True)
                render_play_button(item['zh'], f"🔊 Hát câu {item['num']}", key=f"sing_line_{idx}")





