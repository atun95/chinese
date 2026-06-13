import streamlit as st
import random
import base64
import os
from datetime import datetime, timezone, timedelta
from ui_utils import render_lesson_intro, render_play_button, shuffled_options
from lessons_data import B5_NASAL_FINALS_DATA, B5_QUIZ_VOCAB, B5_QUIZ_LISTENING, B5_QUIZ_FILL_BLANKS

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
    
    tab_theory, tab_diff, tab_spelling, tab_arena, tab_exercises = st.tabs([
        "📚 1. Chi tiết 7 Vận mẫu Mũi",
        "⚖️ 2. Phân biệt Âm Mũi Trước / Sau",
        "🎮 3. Công cụ Ghép âm Tương tác",
        "🎲 4. Hoạt động lớp học (Classroom Arena)",
        "📝 5. Luyện tập & Bài tập"
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
            {"label": "Cặp an / ang", "p1": "ān", "example1": "fàn (饭 - cơm)", "sound1": "fàn", "p2": "āng", "example2": "máng (忙 - bận)", "sound2": "máng"},
            {"label": "Cặp en / eng", "p1": "ēn", "example1": "hěn (很 - rất)", "sound1": "hěn", "p2": "ēng", "example2": "péng (朋 - bạn bè)", "sound2": "péng"},
            {"label": "Cặp in / ing", "p1": "īn", "example1": "nín (您 - ngài)", "sound1": "nín", "p2": "īng", "example2": "tīng (听 - nghe)", "sound2": "tīng"}
        ]
        
        for idx, pair in enumerate(pairs):
            st.markdown(f"#### ⚖️ {pair['label']}")
            col_l, col_r = st.columns(2)
            with col_l:
                st.info(f"👉 **Âm mũi trước (-n)**: /{pair['p1']}/")
                render_play_button(pair['p1'], f"🔊 Nghe âm /{pair['p1']}/", key=f"pair_v_l_{idx}")
                render_play_button(pair['sound1'], f"🔊 Từ ví dụ: {pair['example1']}", key=f"pair_ex_l_{idx}")
            with col_r:
                st.success(f"👉 **Âm mũi sau (-ng)**: /{pair['p2']}/")
                render_play_button(pair['p2'], f"🔊 Nghe âm /{pair['p2']}/", key=f"pair_v_r_{idx}")
                render_play_button(pair['sound2'], f"🔊 Từ ví dụ: {pair['example2']}", key=f"pair_ex_r_{idx}")
            st.markdown("<br/>", unsafe_allow_html=True)
            
    # --- TAB 3: SANDBOX ---
    with tab_spelling:
        st.subheader("3. Công cụ Ghép âm Tương tác (Nasal Finals)")
        st.write("Chọn thanh mẫu, vận mẫu mũi và thanh điệu để ghép âm và nghe phát âm chính xác:")
        
        cols_sel = st.columns(3)
        with cols_sel[0]:
            initials = ["(Không có)", "b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "j", "q", "x", "zh", "ch", "sh", "r", "z", "c", "s"]
            sel_initial = st.selectbox("Chọn Thanh mẫu:", initials, index=0, key="nasal_sandbox_initial")
        with cols_sel[1]:
            finals = ["an", "ang", "en", "eng", "in", "ing", "ong"]
            sel_final = st.selectbox("Chọn Vận mẫu mũi:", finals, index=0, key="nasal_sandbox_final")
        with cols_sel[2]:
            tones = ["Thanh nhẹ", "Thanh 1", "Thanh 2", "Thanh 3", "Thanh 4"]
            sel_tone = st.selectbox("Chọn Thanh điệu:", tones, index=1, key="nasal_sandbox_tone")
            
        tone_idx = tones.index(sel_tone)
        spelled_res, err = check_nasal_spelling_rule(sel_initial, sel_final, tone_idx)
        
        st.markdown("<br/>", unsafe_allow_html=True)
        if err:
            st.markdown(
                f"""
                <div style="background-color: #FEF2F2; border: 1px solid #FCA5A5; border-radius: 12px; padding: 18px; text-align: center;">
                    <span style="font-size: 1.1em; color: #DC2626; font-weight: bold;">{err}</span>
                    <p style="color: #991B1B; font-size: 0.9em; margin-top: 6px; margin-bottom: 0;">
                        Vui lòng chọn tổ hợp ghép âm khác. Nhóm thanh mẫu mặt lưỡi j, q, x chỉ có thể kết hợp với in, ing trong nhóm vận mẫu mũi này.
                    </p>
                </div>
                """, 
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style="background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%); border: 1px solid #A7F3D0; border-radius: 12px; padding: 22px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.04);">
                    <div style="font-size: 0.85em; color: #065F46; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;">KẾT QUẢ GHÉP ÂM CHUẨN XÁC:</div>
                    <div style="font-size: 3.5em; font-weight: bold; color: #047857; font-family: 'Courier New', monospace; margin: 10px 0;">{spelled_res}</div>
                    <div style="font-size: 0.95em; color: #065F46; font-style: italic;">
                        Ghép từ: <b>{sel_initial if sel_initial != '(Không có)' else ''}</b> + <b>{sel_final}</b> + <b>{sel_tone}</b>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown("<br/>", unsafe_allow_html=True)
            render_play_button(spelled_res, "🔊 Phát âm Âm tiết vừa ghép", key="nasal_sandbox_play_btn", type="primary")

    # --- TAB 4: ARENA ---
    with tab_arena:
        st.subheader("4. Hoạt động Lớp học (Classroom Arena)")
        tab_game1, tab_game2 = st.tabs(["🎲 Game 1: Vòng quay Phản xạ Âm Mũi", "🕵️ Game 2: Tìm lỗi chính tả (Spot the Imposter)"])
        
        with tab_game1:
            st.markdown("### 🎲 Thử thách Phản xạ Âm tiết chứa Vận mẫu mũi")
            st.write("Giáo viên hoặc học viên nhấn nút để tạo ngẫu nhiên một âm tiết mũi. Học viên được chọn cần đọc to và dịch nghĩa (nếu có).")
            
            student_list_raw = st.text_input("Danh sách học viên (cách nhau bằng dấu phẩy):", "Tiên, Vy, Trân, Thanh", key="nasal_students_input")
            students = [s.strip() for s in student_list_raw.split(",") if s.strip()]
            
            NASAL_REFLEX_POOL = [
                {"pinyin": "fàn", "hanzi": "饭", "meaning": "cơm / ăn cơm"},
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
    st.subheader("Công cụ Ghép âm Tương tác (Nasal Finals)")
    st.write("Chọn thanh mẫu, vận mẫu mũi và thanh điệu để ghép âm và nghe phát âm chính xác:")
    
    cols_sel = st.columns(3)
    with cols_sel[0]:
        initials = ["(Không có)", "b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "j", "q", "x", "zh", "ch", "sh", "r", "z", "c", "s"]
        sel_initial = st.selectbox("Chọn Thanh mẫu:", initials, index=0, key="nasal_sandbox_initial_standalone")
    with cols_sel[1]:
        finals = ["an", "ang", "en", "eng", "in", "ing", "ong"]
        sel_final = st.selectbox("Chọn Vận mẫu mũi:", finals, index=0, key="nasal_sandbox_final_standalone")
    with cols_sel[2]:
        tones = ["Thanh nhẹ", "Thanh 1", "Thanh 2", "Thanh 3", "Thanh 4"]
        sel_tone = st.selectbox("Chọn Thanh điệu:", tones, index=1, key="nasal_sandbox_tone_standalone")
        
    tone_idx = tones.index(sel_tone)
    spelled_res, err = check_nasal_spelling_rule(sel_initial, sel_final, tone_idx)
    
    st.markdown("<br/>", unsafe_allow_html=True)
    if err:
        st.markdown(
            f"""
            <div style="background-color: #FEF2F2; border: 1px solid #FCA5A5; border-radius: 12px; padding: 18px; text-align: center;">
                <span style="font-size: 1.1em; color: #DC2626; font-weight: bold;">{err}</span>
                <p style="color: #991B1B; font-size: 0.9em; margin-top: 6px; margin-bottom: 0;">
                    Vui lòng chọn tổ hợp ghép âm khác. Nhóm thanh mẫu mặt lưỡi j, q, x chỉ có thể kết hợp với in, ing trong nhóm vận mẫu mũi này.
                </p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%); border: 1px solid #A7F3D0; border-radius: 12px; padding: 22px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.04);">
                <div style="font-size: 0.85em; color: #065F46; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;">KẾT QUẢ GHÉP ÂM CHUẨN XÁC:</div>
                <div style="font-size: 3.5em; font-weight: bold; color: #047857; font-family: 'Courier New', monospace; margin: 10px 0;">{spelled_res}</div>
                <div style="font-size: 0.95em; color: #065F46; font-style: italic;">
                    Ghép từ: <b>{sel_initial if sel_initial != '(Không có)' else ''}</b> + <b>{sel_final}</b> + <b>{sel_tone}</b>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<br/>", unsafe_allow_html=True)
        render_play_button(spelled_res, "🔊 Phát âm Âm tiết vừa ghép", key="nasal_sandbox_play_btn_standalone", type="primary")

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


