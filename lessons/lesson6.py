import streamlit as st
import random
from datetime import datetime, timezone, timedelta
from ui_utils import render_lesson_intro, render_play_button
from lessons_data import B6_1_NASAL_FINALS_DATA, B6_1_QUIZ_DATA, B6_2_STANDALONE_FINALS_DATA, B6_2_QUIZ_DATA

def check_nasal_spelling_rule_6_1(initial, final, tone_idx):
    valid_combos = {
        "b": ["ian"],
        "p": ["ian"],
        "m": ["ian"],
        "f": [],
        "d": ["ian", "uan", "un"],
        "t": ["ian", "uan", "un"],
        "n": ["ian", "iang", "uan", "un"],
        "l": ["ian", "iang", "uan", "un"],
        "g": ["uan", "uang", "un"],
        "k": ["uan", "uang", "un"],
        "h": ["uan", "uang", "un"],
        "j": ["ian", "iang", "iong", "üan", "ün"],
        "q": ["ian", "iang", "iong", "üan", "ün"],
        "x": ["ian", "iang", "iong", "üan", "ün"],
        "zh": ["uan", "uang", "un"],
        "ch": ["uan", "uang", "un"],
        "sh": ["uan", "uang", "un"],
        "r": ["uan", "un"],
        "z": ["uan", "un"],
        "c": ["uan", "un"],
        "s": ["uan", "un"],
        "(Không có)": ["ian", "iang", "iong", "uan", "uang", "un", "üan", "ün"]
    }
    
    init_key = initial if initial != "(Không có)" else "(Không có)"
    
    # n và l có đi với üan
    if init_key in ["n", "l"] and final == "üan":
        pass
    elif final not in valid_combos.get(init_key, []) and not (init_key in ["n", "l"] and final == "üan"):
        if initial == "(Không có)":
            return None, f"❌ Vận mẫu <b>{final}</b> không đứng độc lập mà sẽ biến đổi chính tả khi viết!"
        return None, f"❌ Lỗi ghép âm: Thanh mẫu <b>{initial}</b> không đi cùng vận mẫu <b>{final}</b> trong tiếng Trung tiêu chuẩn!"
        
    spelled = ""
    explain_txt = None
    
    if initial == "(Không có)":
        if final == "ian":
            spelled = "yan"
            explain_txt = "💡 Quy tắc: Vận mẫu <b>ian</b> khi đứng độc lập viết biến đổi thành <b>yan</b>."
        elif final == "iang":
            spelled = "yang"
            explain_txt = "💡 Quy tắc: Vận mẫu <b>iang</b> khi đứng độc lập viết biến đổi thành <b>yang</b>."
        elif final == "iong":
            spelled = "yong"
            explain_txt = "💡 Quy tắc: Vận mẫu <b>iong</b> khi đứng độc lập viết biến đổi thành <b>yong</b>."
        elif final == "uan":
            spelled = "wan"
            explain_txt = "💡 Quy tắc: Vận mẫu <b>uan</b> khi đứng độc lập viết biến đổi thành <b>wan</b>."
        elif final == "uang":
            spelled = "wang"
            explain_txt = "💡 Quy tắc: Vận mẫu <b>uang</b> khi đứng độc lập viết biến đổi thành <b>wang</b>."
        elif final == "un":
            spelled = "wen"
            explain_txt = "💡 Quy tắc: Vận mẫu <b>un</b> (uen) khi đứng độc lập viết biến đổi thành <b>wen</b>."
        elif final == "ün":
            spelled = "yun"
            explain_txt = "💡 Quy tắc: Vận mẫu <b>ün</b> khi đứng độc lập viết biến đổi thành <b>yun</b>."
        elif final == "üan":
            spelled = "yuan"
            explain_txt = "💡 Quy tắc: Vận mẫu <b>üan</b> khi đứng độc lập viết biến đổi thành <b>yuan</b>."
    else:
        if initial in ["j", "q", "x"]:
            if final == "üan":
                spelled = f"{initial}uan"
                explain_txt = f"💡 Quy tắc: Vận mẫu <b>üan</b> đi sau <b>{initial}</b> sẽ lược bỏ hai dấu chấm trên đầu, viết là <b>{initial}uan</b> nhưng vẫn giữ nguyên cách đọc tròn môi 'uyên'!"
            elif final == "ün":
                spelled = f"{initial}un"
                explain_txt = f"💡 Quy tắc: Vận mẫu <b>ün</b> đi sau <b>{initial}</b> sẽ lược bỏ hai dấu chấm trên đầu, viết là <b>{initial}un</b> nhưng vẫn giữ nguyên cách đọc tròn môi 'uyn'!"
            else:
                spelled = f"{initial}{final}"
        else:
            spelled = f"{initial}{final}"
            
    if tone_idx == 0:
        return spelled, explain_txt
        
    tone_vowels = {
        'a': ['ā', 'á', 'ǎ', 'à'],
        'e': ['ē', 'é', 'ě', 'è'],
        'i': ['ī', 'í', 'ǐ', 'ì'],
        'o': ['ō', 'ó', 'ǒ', 'ò'],
        'u': ['ū', 'ú', 'ǔ', 'ù'],
        'ü': ['ǖ', 'ǘ', 'ǚ', 'ǜ']
    }
    
    res = spelled
    if 'a' in res:
        res = res.replace('a', tone_vowels['a'][tone_idx - 1])
    elif 'o' in res:
        res = res.replace('o', tone_vowels['o'][tone_idx - 1])
    elif 'e' in res:
        res = res.replace('e', tone_vowels['e'][tone_idx - 1])
    elif 'ü' in res:
        res = res.replace('ü', tone_vowels['ü'][tone_idx - 1])
    elif 'u' in res:
        res = res.replace('u', tone_vowels['u'][tone_idx - 1])
    elif 'i' in res:
        res = res.replace('i', tone_vowels['i'][tone_idx - 1])
        
    return res, explain_txt

def show_lesson6_1_nasal_finals(save_progress, save_score_row_b6_1, load_all_scores_b6_1):
    # CSS Styles sang trọng cho Bài 6.1 (Tông màu Tím pastel kết hợp Xanh dương trẻ trung)
    st.markdown("""
    <style>
    .final-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .final-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
    }
    .final-letter {
        font-size: 2.3em;
        font-weight: 800;
        font-family: 'Courier New', monospace;
        line-height: 1.1;
    }
    .spelling-highlight {
        background-color: #fef08a;
        color: #854d0e;
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: bold;
        font-family: 'Courier New', monospace;
        border: 1px solid #fde047;
    }
    .rule-box {
        background-color: #f8fafc;
        border-left: 5px solid #6366f1;
        border-radius: 8px;
        padding: 15px;
        margin: 15px 0;
    }
    .rule-title {
        font-weight: bold;
        color: #4f46e5;
        font-size: 1.05rem;
        margin-bottom: 6px;
    }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "📚 Bài 6.1: Các vận mẫu mũi còn lại",
        "Học phát âm, phân biệt và thực hành ghép âm 8 vận mẫu mũi phức hợp: ian, iang, iong, uan, uang, un, ün, üan."
    )

    tab_theory, tab_rules, tab_spelling, tab_exercises = st.tabs([
        "📚 Lý thuyết chi tiết",
        "✍️ Quy tắc chính tả",
        "🗣️ Luyện tập ghép âm",
        "📝 Bài tập tự luyện"
    ])

    # ================= TAB 1: LÝ THUYẾT CHI TIẾT =================
    with tab_theory:
        st.subheader("1. Chi tiết các vận mẫu mũi phức hợp")
        st.write("Các vận mẫu mũi này bắt đầu bằng âm đệm nguyên âm hẹp (**i**, **u**, **ü**) và kết thúc bằng phụ âm mũi (**-n** hoặc **-ng**).")

        for group in B6_1_NASAL_FINALS_DATA:
            st.markdown(f"### 📌 {group['nhom']}")
            for idx, item in enumerate(group["items"]):
                cols = st.columns([3.5, 1.5])
                with cols[0]:
                    card_html = f"""
                    <div class="final-card" style="border-left: 6px solid {item['border_color']};">
                        <div style="display: flex; align-items: center;">
                            <span class="final-letter" style="color: {item['text_color']};">{item['chu']}</span>
                        </div>
                        <p style="margin-top: 10px; color: #1e293b; font-weight: 500;">👉 <b>Hướng dẫn phát âm:</b> {item['hdsd']}</p>
                        <p style="color: #475569; font-size: 0.9em; line-height: 1.4;"><i>{item['cach_doc_sau']}</i></p>
                        <div class="rule-box" style="border-left-color: {item['border_color']}; margin-top: 10px; padding: 10px;">
                            <span style="font-size: 0.85em; font-weight: bold; color: {item['text_color']};">⚠️ LƯU Ý VIẾT PINYIN:</span><br/>
                            <span style="font-size: 0.9em; color: #334155;">{item['luu_y']}</span>
                        </div>
                    </div>
                    """
                    st.markdown(card_html, unsafe_allow_html=True)
                with cols[1]:
                    st.markdown(f"<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
                    st.markdown(f"**Ví dụ tiêu biểu:**")
                    st.markdown(f"<span style='font-size: 2.2rem; font-weight: bold; color: #1e293b;'>{item['vd_han']}</span>", unsafe_allow_html=True)
                    st.markdown(f"<span style='font-family: monospace; font-size: 1.15rem; font-weight: bold; color: #2563eb;'>{item['vd_py']}</span>", unsafe_allow_html=True)
                    st.markdown(f"<span style='color: #475569; font-size: 0.95rem; font-style: italic;'>({item['vietnamese']})</span>", unsafe_allow_html=True)
                    render_play_button(item['nghe'], f"🔊 Nghe: {item['vd_py']}", key=f"play_v61_theory_{item['chu']}")
                
                # Hiển thị ví dụ mở rộng dạng bảng nhỏ đẹp mắt
                with st.expander(f"🔍 Xem thêm ví dụ phát âm cho vận mẫu /{item['chu']}/"):
                    ex_cols = st.columns(len(item['more_examples']))
                    for ex_idx, ex in enumerate(item['more_examples']):
                        with ex_cols[ex_idx]:
                            st.markdown(f"""
                            <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px; text-align: center;">
                                <span style="font-size: 1.5rem; font-weight: bold; color: #0f172a;">{ex['han']}</span><br/>
                                <span style="font-family: monospace; font-weight: bold; color: #2563eb;">{ex['py']}</span><br/>
                                <span style="font-size: 0.85em; color: #6b7280; font-style: italic;">({ex['vi']})</span>
                            </div>
                            """, unsafe_allow_html=True)
                            render_play_button(ex['han'], f"🔊 Phát âm", key=f"play_v61_theory_ex_{item['chu']}_{ex_idx}")
                st.markdown("<hr style='margin: 15px 0; border: 0; border-top: 1px dashed #e2e8f0;'/>", unsafe_allow_html=True)

    # ================= TAB 2: QUY TẮC CHÍNH TẢ =================
    with tab_rules:
        st.subheader("2. Hai Quy Tắc Vàng Khi Viết Pinyin (Trọng tâm học thuật)")
        st.write("8 vận mẫu mũi phức hợp này chứa đựng các quy tắc chính tả biến đổi phức tạp nhất trong hệ thống Pinyin. Học viên cần ghi nhớ nằm lòng:")
        
        st.markdown("""
        <div style="background-color: #eff6ff; border-left: 6px solid #3b82f6; padding: 18px; border-radius: 12px; margin-bottom: 20px;">
            <h4 style="color: #1e3a8a; margin-top: 0; font-weight: bold;">🌟 Quy tắc 1: Khi đứng độc lập một mình (Không đi kèm thanh mẫu)</h4>
            <p style="color: #1e3a8a; font-size: 0.95em; line-height: 1.5; margin-bottom: 0;">
                Bán nguyên âm <b>i</b> đứng đầu sẽ chuyển hóa thành phụ âm <b>y</b>.<br/>
                Bán nguyên âm <b>u</b> đứng đầu sẽ chuyển hóa thành phụ âm <b>w</b>.<br/>
                Bán nguyên âm <b>ü</b> đứng đầu sẽ chuyển hóa thành phụ âm <b>yu</b> (bỏ hai dấu chấm).
            </p>
        </div>
        """, unsafe_allow_html=True)

        rule1_data = [
            {"goc": "ian", "bien": "yan", "vd_han": "烟 (khói)", "vd_py": "yān"},
            {"goc": "iang", "bien": "yang", "vd_han": "羊 (con dê)", "vd_py": "yáng"},
            {"goc": "iong", "bien": "yong", "vd_han": "用 (sử dụng)", "vd_py": "yòng"},
            {"goc": "uan", "bien": "wan", "vd_han": "玩 (chơi)", "vd_py": "wán"},
            {"goc": "uang", "bien": "wang", "vd_han": "王 (vua)", "vd_py": "wáng"},
            {"goc": "un (uen)", "bien": "wen", "vd_han": "问 (hỏi)", "vd_py": "wèn"},
            {"goc": "ün", "bien": "yun", "vd_han": "云 (đám mây)", "vd_py": "yún"},
            {"goc": "üan", "bien": "yuan", "vd_han": "元 (đồng tệ)", "vd_py": "yuán"},
        ]

        cols_r1 = st.columns(4)
        for idx, r1 in enumerate(rule1_data):
            col_idx = idx % 4
            with cols_r1[col_idx]:
                st.markdown(f"""
                <div style="background: white; border: 1px solid #bfdbfe; border-radius: 10px; padding: 12px; margin-bottom: 12px; text-align: center; box-shadow: 0 2px 5px rgba(59, 130, 246, 0.05);">
                    <div style="font-family: monospace; font-size: 0.9em; color: #64748b;">Vận mẫu gốc: <b>{r1['goc']}</b></div>
                    <div style="font-size: 1.5em; font-weight: bold; color: #2563eb; margin: 5px 0;">➔ {r1['bien']}</div>
                    <div style="font-weight: 500; color: #0f172a;">{r1['vd_han']}</div>
                    <div style="font-family: 'Courier New', monospace; font-weight: bold; color: #3b82f6;">{r1['vd_py']}</div>
                </div>
                """, unsafe_allow_html=True)
                render_play_button(r1['vd_han'].split(" ")[0], "🔊 Nghe phát âm", key=f"play_v61_rule1_{idx}")
                st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div style="background-color: #fffbeb; border-left: 6px solid #d97706; padding: 18px; border-radius: 12px; margin-top: 10px; margin-bottom: 20px;">
            <h4 style="color: #78350f; margin-top: 0; font-weight: bold;">🌟 Quy tắc 2: Lược bỏ hai dấu chấm của ü sau j, q, x</h4>
            <p style="color: #78350f; font-size: 0.95em; line-height: 1.5; margin-bottom: 0;">
                Khi các vận mẫu tròn môi <b>ün</b> và <b>üan</b> đi sau các thanh mẫu mặt lưỡi <b>j, q, x</b>, chúng ta bắt buộc phải lược bỏ hai dấu chấm trên đầu chữ ü.<br/>
                Ví dụ: viết là <b>jun, qun, xun, juan, quan, xuan</b> nhưng miệng phát âm vẫn bắt buộc khum tròn môi là <b>jün, qün, xün, jüan, qüan, xüan</b>.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_r2_1, col_r2_2 = st.columns(2)
        with col_r2_1:
            st.markdown("""
            <div style="background: white; border: 1px solid #fde047; border-radius: 12px; padding: 16px; height: 100%;">
                <h5 style="color: #a16207; font-weight: bold; margin-top: 0;">Ví dụ với ün (uyn):</h5>
                <ul>
                    <li>j + ün ➔ <b>jun</b> (quân đội) - <span style="font-family: monospace; color:#2563eb; font-weight:bold;">jūn</span></li>
                    <li>q + ün ➔ <b>qun</b> (váy) - <span style="font-family: monospace; color:#2563eb; font-weight:bold;">qún</span></li>
                    <li>x + ün ➔ <b>xun</b> (tìm kiếm) - <span style="font-family: monospace; color:#2563eb; font-weight:bold;">xún</span></li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        with col_r2_2:
            st.markdown("""
            <div style="background: white; border: 1px solid #fde047; border-radius: 12px; padding: 16px; height: 100%;">
                <h5 style="color: #a16207; font-weight: bold; margin-top: 0;">Ví dụ với üan (uyên):</h5>
                <ul>
                    <li>j + üan ➔ <b>juan</b> (cuộn tròn) - <span style="font-family: monospace; color:#2563eb; font-weight:bold;">juǎn</span></li>
                    <li>q + üan ➔ <b>quan</b> (tất cả / toàn bộ) - <span style="font-family: monospace; color:#2563eb; font-weight:bold;">quán</span></li>
                    <li>x + üan ➔ <b>xuan</b> (chọn lựa) - <span style="font-family: monospace; color:#2563eb; font-weight:bold;">xuǎn</span></li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br/>", unsafe_allow_html=True)
        st.warning("💡 **Mẹo phân biệt:** Các thanh mẫu đầu lưỡi `n` và `l` có thể đi cùng cả `u` thường và `ü` tròn môi. Do đó, khi `n` và `l` đi với `üan`, ta **bắt buộc phải giữ nguyên dấu hai chấm** trên đầu để tránh trùng lặp. Ví dụ: `luan` (luân) khác biệt hoàn toàn với `lüan` (luyến).")

    # ================= TAB 3: LUYỆN TẬP GHÉP ÂM =================
    with tab_spelling:
        st.subheader("3. Máy Ghép Âm Mũi Phức Hợp (Spelling Interactive)")
        st.write("Chọn thanh mẫu, vận mẫu và thanh điệu bên dưới để máy tự động ghép chữ và chỉ ra quy tắc chính tả chuẩn xác:")

        col_sp1, col_sp2, col_sp3 = st.columns(3)
        with col_sp1:
            sp_init = st.selectbox("1. Chọn Thanh mẫu (Initials):", [
                "(Không có)", "b", "p", "m", "d", "t", "n", "l", "g", "k", "h", "j", "q", "x", "zh", "ch", "sh", "r", "z", "c", "s"
            ], key="v61_sp_initial")
        with col_sp2:
            sp_final = st.selectbox("2. Chọn Vận mẫu mũi (Finals):", [
                "ian", "iang", "iong", "uan", "uang", "un", "ün", "üan"
            ], key="v61_sp_final")
        with col_sp3:
            sp_tone = st.slider("3. Chọn Thanh điệu (Tones):", 0, 4, 1, format="Thanh %d" if "%d" else None, key="v61_sp_tone")

        spelled_res, explain_txt = check_nasal_spelling_rule_6_1(sp_init, sp_final, sp_tone)

        st.markdown("### Kết quả ghép âm:")
        if spelled_res:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f5f3ff 0%, #edd9ff 100%); border: 2px solid #ddd6fe; border-radius: 16px; padding: 25px; text-align: center; margin-top: 10px; margin-bottom: 10px;">
                <span style="font-size: 0.85em; color: #6d28d9; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em;">BÍNH ÂM CHUẨN XÁC:</span>
                <div style="font-size: 3.5rem; font-weight: 800; color: #4c1d95; margin: 15px 0; font-family: 'Courier New', monospace;">{spelled_res}</div>
            </div>
            """, unsafe_allow_html=True)
            render_play_button(spelled_res, "🔊 Phát âm chuẩn Bính âm vừa ghép", key="v61_sp_play_btn")
            if explain_txt:
                st.markdown(f"<div class='rule-box'><div class='rule-title'>📌 Cảnh báo chính tả:</div><p style='color: #374151; font-size: 0.95em;'>{explain_txt}</p></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="background-color: #fef2f2; border: 2px dashed #fca5a5; border-radius: 16px; padding: 25px; text-align: center; margin-top: 10px; margin-bottom: 10px; color: #991b1b;">
                <div style="font-size: 3rem; margin-bottom: 10px;">⚠️</div>
                <div style="font-weight: bold; font-size: 1.15rem;">Sự kết hợp âm này không tồn tại trong tiếng Trung tiêu chuẩn!</div>
                <p style="font-size: 0.95em; color: #b91c1c; margin-top: 5px;">{explain_txt}</p>
            </div>
            """, unsafe_allow_html=True)

    # ================= TAB 4: BÀI TẬP TỰ LUYỆN =================
    with tab_exercises:
        st.subheader("4. Bài tập thực hành luyện nghe và phản xạ Bính âm")
        st.write("Học viên làm bài trắc nghiệm dưới đây và nhấn nút Nộp bài để lưu kết quả và tính điểm thi đua:")

        if "b61_score_submitted" not in st.session_state:
            st.session_state.b61_score_submitted = False

        score_b6_1 = 0
        user_answers = {}

        for idx, item in enumerate(B6_1_QUIZ_DATA):
            st.markdown(f"#### Câu {idx+1}: {item['q']}")
            if "hanzi" in item:
                st.markdown(f"<span style='font-size: 2rem; font-weight: bold; color: #1e293b;'>Chữ Hán: {item['hanzi']}</span>", unsafe_allow_html=True)
                render_play_button(item['hanzi'], f"🔊 Nghe âm phát mẫu", key=f"v61_quiz_play_{idx}")
                st.markdown("<br/>", unsafe_allow_html=True)
            
            user_ans = st.radio(f"Chọn đáp án đúng cho Câu {idx+1}:", item['choices'], index=0, key=f"v61_quiz_ans_{idx}")
            user_answers[idx] = user_ans
            if user_ans == item['answer']:
                score_b6_1 += 1
            st.markdown("<hr style='margin: 15px 0; border: 0; border-top: 1px dashed #e2e8f0;'/>", unsafe_allow_html=True)

        if not st.session_state.b61_score_submitted:
            if st.button("📝 Chấm điểm bài tập Bài 6.1", type="primary", use_container_width=True, key="v61_quiz_grade_btn"):
                st.session_state.b61_score_submitted = True
                st.rerun()
        else:
            st.markdown("### Kết quả chấm điểm chi tiết:")
            for idx, item in enumerate(B6_1_QUIZ_DATA):
                u_ans = user_answers[idx]
                if u_ans == item['answer']:
                    st.success(f"✅ **Câu {idx+1}: Chính xác!**")
                    st.write(f"Đọc giải thích: {item['explain']}")
                else:
                    st.error(f"❌ **Câu {idx+1}: Chưa chính xác!** (Bạn chọn: {u_ans})")
                    st.write(f"👉 Đáp án đúng: **{item['answer']}**")
                    st.write(f"Đọc giải thích: {item['explain']}")

            final_percentage_score = round((score_b6_1 / len(B6_1_QUIZ_DATA)) * 10, 2)
            st.markdown(f"### Điểm tổng kết: **{score_b6_1} / {len(B6_1_QUIZ_DATA)}** ({final_percentage_score} điểm hệ 10)")
            
            if score_b6_1 == len(B6_1_QUIZ_DATA):
                st.balloons()
                st.success("Tuyệt vời! Bạn đã trả lời đúng tất cả các câu hỏi! 👑")

            st.markdown("---")
            name = st.text_input("Nhập tên học viên để nộp điểm:", key="v61_student_name")
            if st.button("Nộp bài tập Bài 6.1", type="primary", use_container_width=True, key="v61_submit_score_btn"):
                if name:
                    row = {
                        "thời gian": datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S"),
                        "học viên": name,
                        "tổng điểm": final_percentage_score,
                        "BT: Ghép câu": f"{score_b6_1}/{len(B6_1_QUIZ_DATA)}"
                    }
                    if save_score_row_b6_1(row):
                        st.success("Đã nộp bài và lưu điểm thành công!")
                        st.session_state.b61_score_submitted = False
                        save_progress()
                        st.rerun()
                else:
                    st.error("Vui lòng nhập tên để nộp bài!")

            if st.button("🔄 Làm lại bài tập", use_container_width=True, key="v61_redo_quiz_btn"):
                st.session_state.b61_score_submitted = False
                save_progress()
                st.rerun()

        # Hiển thị bảng xếp hạng nộp bài lớp học
        all_scores = load_all_scores_b6_1()
        if all_scores:
            st.write("### 🏆 Bảng xếp hạng nộp bài lớp học:")
            st.dataframe(all_scores, use_container_width=True)


def show_lesson6_2_standalone_finals(save_progress, save_score_row_b6_2, load_all_scores_b6_2):
    # CSS Styles sang trọng cho Bài 6.2 (Tông màu HSL hiện đại, trẻ trung)
    st.markdown("""
    <style>
    .standalone-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 18px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .standalone-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.06);
    }
    .standalone-card-highlighted {
        background: #fffbeb;
        border: 1.5px solid #fde68a;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 18px;
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .standalone-card-highlighted:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(245, 158, 11, 0.08);
    }
    .standalone-letters {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 10px;
    }
    .goc-letter {
        font-size: 1.8em;
        font-weight: 700;
        color: #64748b;
        font-family: 'Courier New', monospace;
    }
    .arrow-icon {
        font-size: 1.5em;
        color: #3b82f6;
    }
    .bien-letter {
        font-size: 2.3em;
        font-weight: 800;
        color: #1e3a8a;
        font-family: 'Courier New', monospace;
        background: #eff6ff;
        padding: 2px 10px;
        border-radius: 8px;
        border: 1px solid #bfdbfe;
    }
    .standalone-desc {
        color: #475569;
        font-size: 0.95em;
        line-height: 1.4;
    }
    .mota-box {
        background-color: #f8fafc;
        border-left: 5px solid #3b82f6;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 20px;
        font-size: 0.95rem;
        line-height: 1.5;
        color: #334155;
    }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "📚 Bài 6.2: Quy tắc biến đổi Vận mẫu khi đứng độc lập",
        "Tổng hợp tất cả các vận mẫu thay đổi cách viết Pinyin khi đứng một mình (không đi kèm thanh mẫu)."
    )

    tab_theory, tab_exercises = st.tabs([
        "📚 Quy tắc biến đổi chi tiết",
        "📝 Bài tập tự luyện"
    ])

    # ================= TAB 1: LÝ THUYẾT CHI TIẾT =================
    with tab_theory:
        st.write("Trong tiếng Trung, một số vận mẫu khi đứng một mình làm thành một âm tiết (không có thanh mẫu đi cùng) thì hình thức viết Pinyin của chúng bắt buộc phải thay đổi để phân tách âm tiết rõ ràng. Dưới đây là bảng tổng hợp đầy đủ theo 3 nhóm:")

        for idx_group, group in enumerate(B6_2_STANDALONE_FINALS_DATA):
            st.markdown(f"### 📌 {group['nhom']}")
            st.markdown(f"<div class='mota-box'>{group['mota']}</div>", unsafe_allow_html=True)
            
            # Hiển thị các vận mẫu dưới dạng Grid layout đẹp mắt
            items = group["items"]
            cols_per_row = 2
            for i in range(0, len(items), cols_per_row):
                cols = st.columns(cols_per_row)
                for col_idx in range(cols_per_row):
                    item_idx = i + col_idx
                    if item_idx < len(items):
                        item = items[item_idx]
                        with cols[col_idx]:
                            st.markdown(f"""
                            <div class="standalone-card">
                                <div class="standalone-letters">
                                    <span class="goc-letter">/{item['goc']}/</span>
                                    <span class="arrow-icon">➔</span>
                                    <span class="bien-letter">{item['bien']}</span>
                                </div>
                                <div style="margin-top: 12px; border-top: 1px dashed #e2e8f0; padding-top: 10px;">
                                    <span style="color: #64748b; font-size: 0.85em; font-weight: bold; text-transform: uppercase;">Ví dụ cụ thể:</span>
                                    <div style="display: flex; align-items: baseline; gap: 10px; margin-top: 5px;">
                                        <span style="font-size: 1.8rem; font-weight: bold; color: #0f172a;">{item['vd_han']}</span>
                                        <span style="font-family: monospace; font-size: 1.1rem; font-weight: bold; color: #2563eb;">{item['vd_py']}</span>
                                        <span style="color: #475569; font-size: 0.9em; font-style: italic;">({item['meaning']})</span>
                                    </div>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                            render_play_button(item['vd_han'], f"🔊 Nghe phát âm: {item['vd_py']}", key=f"play_v62_theory_{idx_group}_{item_idx}")
            st.markdown("<br/>", unsafe_allow_html=True)

    # ================= TAB 2: BÀI TẬP TỰ LUYỆN =================
    with tab_exercises:
        st.subheader("Bài tập thực hành phản xạ Quy tắc đứng độc lập")
        st.write("Làm bài trắc nghiệm dưới đây và nhấn nút Nộp bài để lưu kết quả thi đua:")

        if "b62_score_submitted" not in st.session_state:
            st.session_state.b62_score_submitted = False

        score_b6_2 = 0
        user_answers = {}

        for idx, item in enumerate(B6_2_QUIZ_DATA):
            st.markdown(f"#### Câu {idx+1}: {item['q']}")
            user_ans = st.radio(f"Chọn đáp án đúng cho Câu {idx+1}:", item['choices'], index=0, key=f"v62_quiz_ans_{idx}")
            user_answers[idx] = user_ans
            if user_ans == item['answer']:
                score_b6_2 += 1
            st.markdown("<hr style='margin: 15px 0; border: 0; border-top: 1px dashed #e2e8f0;'/>", unsafe_allow_html=True)

        if not st.session_state.b62_score_submitted:
            if st.button("📝 Chấm điểm bài tập Bài 6.2", type="primary", use_container_width=True, key="v62_quiz_grade_btn"):
                st.session_state.b62_score_submitted = True
                st.rerun()
        else:
            st.markdown("### Kết quả chấm điểm chi tiết:")
            for idx, item in enumerate(B6_2_QUIZ_DATA):
                u_ans = user_answers[idx]
                if u_ans == item['answer']:
                    st.success(f"✅ **Câu {idx+1}: Chính xác!**")
                    st.write(f"Đọc giải thích: {item['explain']}")
                else:
                    st.error(f"❌ **Câu {idx+1}: Chưa chính xác!** (Bạn chọn: {u_ans})")
                    st.write(f"👉 Đáp án đúng: **{item['answer']}**")
                    st.write(f"Đọc giải thích: {item['explain']}")

            final_percentage_score = round((score_b6_2 / len(B6_2_QUIZ_DATA)) * 10, 2)
            st.markdown(f"### Điểm tổng kết: **{score_b6_2} / {len(B6_2_QUIZ_DATA)}** ({final_percentage_score} điểm hệ 10)")
            
            if score_b6_2 == len(B6_2_QUIZ_DATA):
                st.balloons()
                st.success("Tuyệt vời! Bạn đã nắm rất chắc các quy tắc viết chính tả! 👑")

            st.markdown("---")
            name = st.text_input("Nhập tên học viên để nộp điểm:", key="v62_student_name")
            if st.button("Nộp bài tập Bài 6.2", type="primary", use_container_width=True, key="v62_submit_score_btn"):
                if name:
                    row = {
                        "thời gian": datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S"),
                        "học viên": name,
                        "tổng điểm": final_percentage_score,
                        "BT: Đứng độc lập": f"{score_b6_2}/{len(B6_2_QUIZ_DATA)}"
                    }
                    if save_score_row_b6_2(row):
                        st.success("Đã nộp bài và lưu điểm thành công!")
                        st.session_state.b62_score_submitted = False
                        save_progress()
                        st.rerun()
                else:
                    st.error("Vui lòng nhập tên để nộp bài!")

            if st.button("🔄 Làm lại bài tập", use_container_width=True, key="v62_redo_quiz_btn"):
                st.session_state.b62_score_submitted = False
                save_progress()
                st.rerun()

        # Hiển thị bảng xếp hạng nộp bài lớp học
        all_scores = load_all_scores_b6_2()
        if all_scores:
            st.write("### 🏆 Bảng xếp hạng nộp bài lớp học:")
            st.dataframe(all_scores, use_container_width=True)


def show_lesson6_vocab():
    st.markdown("""
    <style>
    .vocab-section-title-b6 {
        color: #1e3a8a;
        border-left: 5px solid #2563eb;
        padding-left: 12px;
        margin-top: 30px;
        margin-bottom: 15px;
        font-weight: 700;
        font-size: 1.4rem;
    }
    .vocab-card-b6 {
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
    .vocab-card-b6:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05);
        border-color: #cbd5e1;
    }
    .vocab-word-b6 {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 2px;
        line-height: 1.2;
    }
    .vocab-pinyin-b6 {
        font-family: 'Courier New', monospace;
        font-size: 1.1rem;
        font-weight: 700;
        color: #2563eb;
        margin-bottom: 6px;
    }
    .vocab-viet-b6 {
        font-size: 0.95rem;
        font-weight: 700;
        color: #475569;
        margin-bottom: 10px;
    }
    .vocab-ex-box-b6 {
        background: #f8fafc;
        border-radius: 8px;
        padding: 8px;
        border: 1px solid #f1f5f9;
    }
    .vocab-ex-title-b6 {
        font-size: 0.7rem;
        color: #94a3b8;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 2px;
    }
    .vocab-ex-han-b6 {
        font-size: 1.05rem;
        font-weight: 700;
        color: #1e293b;
        display: block;
        margin-bottom: 1px;
    }
    .vocab-ex-py-b6 {
        font-family: 'Courier New', monospace;
        color: #059669;
        display: block;
        margin-bottom: 2px;
        font-size: 0.8rem;
    }
    .vocab-ex-vi-b6 {
        color: #475569;
        font-style: italic;
        display: block;
        font-size: 0.78rem;
    }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "📚 Bài 6: Hệ thống từ vựng",
        "Học các từ vựng theo nhóm từ cơ bản đến nâng cao về thời gian, thứ ngày tháng năm, giờ giấc và các mùa."
    )

    groups = [
        {
            "name": "📅 Nhóm 1: Thời gian cơ bản",
            "items": [
                {"word": "昨天", "pinyin": "zuótiān", "vietnamese": "Hôm qua", "example_han": "昨天我去学校了。", "example_py": "Zuótiān wǒ qù xuéxiào le.", "example_vi": "Hôm qua tôi đi học rồi."},
                {"word": "今天", "pinyin": "jīntiān", "vietnamese": "Hôm nay", "example_han": "今天天气很好。", "example_py": "Jīntiān tiānqì hěn hǎo.", "example_vi": "Hôm nay thời tiết rất tốt."},
                {"word": "明天", "pinyin": "míngtiān", "vietnamese": "Ngày mai", "example_han": "明天`nǐ`忙吗？", "example_py": "Míngtiān nǐ máng ma?", "example_vi": "Ngày mai bạn bận không?"}
            ],
            "guide": None
        },
        {
            "name": "🗓️ Nhóm 2: Thứ, Ngày, Tháng, Năm",
            "items": [
                {"word": "星期", "pinyin": "xīngqī", "vietnamese": "Thứ (trong tuần)", "example_han": "今天星期几？", "example_py": "Jīntiān xīngqī jǐ?", "example_vi": "Hôm nay thứ mấy?"},
                {"word": "号", "pinyin": "hào", "vietnamese": "Ngày (văn nói)", "example_han": "今天几号？", "example_py": "Jīntiān jǐ hào?", "example_vi": "Hôm nay ngày mấy?"},
                {"word": "日", "pinyin": "rì", "vietnamese": "Ngày (văn viết)", "example_han": "十月一日是国庆节。", "example_py": "Shíyuè yī rì  shì guóqìng jié.", "example_vi": "Ngày 1 tháng 10 là ngày Quốc khánh."},
                {"word": "月", "pinyin": "yuè", "vietnamese": "Tháng", "example_han": "现在 là 六月。", "example_py": "Xiànzài shì liùyuè.", "example_vi": "Bây giờ là tháng 6."},
                {"word": "年", "pinyin": "nián", "vietnamese": "Năm", "example_han": "今年 là 二零二六年。", "example_py": "Jīnnián  shì èr líng èr liù nián.", "example_vi": "Năm nay là năm 2026."}
            ],
            "guide": "date"
        },
        {
            "name": "⏰ Nhóm 3: Giờ giấc & Cách đọc giờ",
            "items": [
                {"word": "点", "pinyin": "diǎn", "vietnamese": "Giờ", "example_han": "现在八点。", "example_py": "Xiànzài bā diǎn.", "example_vi": "Bây giờ là 8 giờ."},
                {"word": "分", "pinyin": "fēn", "vietnamese": "Phút", "example_han": "现在八点十分。", "example_py": "Xiànzài  bā diǎn shí fēn.", "example_vi": "Bây giờ là 8 giờ 10 phút."},
                {"word": "半", "pinyin": "bàn", "vietnamese": "Rưỡi / Nửa", "example_han": "现在八点半。", "example_py": "Xiànzài bā diǎn bàn.", "example_vi": "Bây giờ là 8 giờ rưỡi."},
                {"word": "刻", "pinyin": "kè", "vietnamese": "Khắc (15 phút)", "example_han": "现在八点一刻。", "example_py": "Xiànzài  bā diǎn yí kè.", "example_vi": "Bây giờ là 8 giờ 15 phút."},
                {"word": "差", "pinyin": "chà", "vietnamese": "Kém", "example_han": "差五分九点。", "example_py": "Chà wǔ fēn jiǔ diǎn.", "example_vi": "9 giờ kém 5 phút."}
            ],
            "guide": "time"
        },
        {
            "name": "🌸 Nhóm 4: Bốn mùa",
            "items": [
                {"word": "春天", "pinyin": "chūntiān", "vietnamese": "Mùa xuân", "example_han": "春天很暖和。", "example_py": "Chūntiān hěn nuǎnhuo.", "example_vi": "Mùa xuân rất ấm áp."},
                {"word": "夏天", "pinyin": "xiàtiān", "vietnamese": "Mùa hạ / hè", "example_han": "夏天很热。", "example_py": "Xiàtiān hěn rè.", "example_vi": "Mùa hè rất nóng."},
                {"word": "秋天", "pinyin": "qiūtiān", "vietnamese": "Mùa thu", "example_han": "秋天很凉快。", "example_py": "Qiūtiān hěn liángkuai.", "example_vi": "Mùa thu rất mát mẻ."},
                {"word": "冬天", "pinyin": "dōngtiān", "vietnamese": "Mùa đông", "example_han": "冬天很冷。", "example_py": "Dōngtiān hěn lěng.", "example_vi": "Mùa đông rất lạnh."}
            ],
            "guide": None
        }
    ]

    groups[0]["items"][2]["example_han"] = "明天你忙吗？"
    groups[1]["items"][3]["example_han"] = "Now six month... -> 现在是六月。"
    groups[1]["items"][3]["example_han"] = "现在是六月。"
    groups[1]["items"][4]["example_han"] = "今年是二零二六年。"

    group_key = "b6_vocab_group_idx"
    if group_key not in st.session_state:
        st.session_state[group_key] = 0

    cur_group_idx = st.session_state[group_key]
    cur_group = groups[cur_group_idx]

    # --- Navigation controller (like flashcards) ---
    col_prev, col_title, col_next = st.columns([1.5, 4, 1.5])
    with col_prev:
        if st.button("⬅️ Nhóm trước", use_container_width=True, key="b6_g_prev"):
            st.session_state[group_key] = (cur_group_idx - 1) % len(groups)
            st.rerun()
    with col_title:
        st.markdown(f"<div style='text-align: center; font-size: 1.25rem; font-weight: bold; color: #1e3a8a; padding: 6px; background: #eff6ff; border-radius: 8px; border: 1px solid #bfdbfe;'>{cur_group['name']}</div>", unsafe_allow_html=True)
    with col_next:
        if st.button("Nhóm sau ➡️", use_container_width=True, key="b6_g_next"):
            st.session_state[group_key] = (cur_group_idx + 1) % len(groups)
            st.rerun()

    st.markdown(f"<div style='text-align: center; font-size: 1rem; font-weight: bold; margin-top: 5px; color:#475569;'>Nhóm {cur_group_idx + 1} / {len(groups)}</div>", unsafe_allow_html=True)
    st.progress((cur_group_idx + 1) / len(groups))

    # --- Render active group cards ---
    items = cur_group["items"]
    cols = st.columns(len(items))
    for idx, item in enumerate(items):
        with cols[idx]:
            card_html = f"""<div class="vocab-card-b6">
<div>
<div class="vocab-word-b6">{item['word']}</div>
<div class="vocab-pinyin-b6">{item['pinyin']}</div>
<div class="vocab-viet-b6">Nghĩa: {item['vietnamese']}</div>
<div class="vocab-ex-box-b6">
<div class="vocab-ex-title-b6">Ví dụ:</div>
<div class="vocab-ex-han-b6">{item['example_han']}</div>
<div class="vocab-ex-py-b6">{item['example_py']}</div>
<div class="vocab-ex-vi-b6">{item['example_vi']}</div>
</div>
</div>
</div>""".replace("\n", " ")
            st.markdown(card_html, unsafe_allow_html=True)
            render_play_button(item['word'], "🔊 Đọc từ", key=f"v6_g{cur_group_idx}_w_{idx}")
            render_play_button(item['example_han'], "🔊 Nghe ví dụ", key=f"v6_g{cur_group_idx}_ex_{idx}")

    # --- Render guides under active group ---
    if cur_group["guide"] == "date":
        st.markdown("""
        <div style="background-color: #eff6ff; border-left: 5px solid #2563eb; padding: 20px; border-radius: 8px; margin-top: 20px; margin-bottom: 10px; border: 1px solid #dbeafe;">
            <h4 style="color: #1e3a8a; margin-top: 0; margin-bottom: 12px; font-weight: bold; font-size: 1.1rem;">
                💡 Cách đọc thứ ngày tháng năm trong tiếng Trung
            </h4>
            <p style="font-size: 0.95em; line-height: 1.6; color: #1e3a8a; margin-bottom: 12px;">
                <b>Quy tắc cốt lõi:</b> Đi từ đơn vị lớn đến đơn vị nhỏ: <b>Năm (年) ➔ Tháng (月) ➔ Ngày (日/号) ➔ Thứ (星期)</b>.
            </p>
            <ul style="font-size: 0.95em; line-height: 1.7; color: #1e3a8a; padding-left: 20px; margin-bottom: 0;">
                <li><b>Cách đọc Năm:</b> Đọc từng chữ số riêng lẻ kèm từ "年" (nián). Ví dụ: 2026年 ➔ 二零二六年 (èr líng èr liù nián).</li>
                <li><b>Cách đọc Tháng:</b> Số thứ tự tháng (1-12) + "月" (yuè). Ví dụ: Tháng 6 ➔ 六月 (liù yuè).</li>
                <li><b>Cách đọc Ngày:</b> Số ngày (1-31) + "号" (hào - văn nói) hoặc "日" (rì - văn viết). Ví dụ: Ngày 25 ➔ 二十五号 (èrshíwǔ hào).</li>
                <li><b>Cách đọc Thứ:</b> "星期" (xīngqī) + Số tương ứng. Đặc biệt: Thứ Hai đến Thứ Bảy là 1-6 (Ví dụ: Thứ Hai ➔ 星期一 xīngqīyī; Thứ Bảy ➔ 星期六 xīngqīliù). Chủ Nhật dùng <b>星期天 (xīngqītiān)</b> hoặc <b>星期日 (xīngqīrì)</b>.</li>
            </ul>
            <div style="margin-top: 15px; background: white; padding: 12px; border-radius: 6px; border: 1px dashed #bfdbfe; font-size: 0.95rem; font-weight: bold; color: #1e3a8a;">
                👉 Ví dụ hoàn chỉnh: Thứ Năm, ngày 25 tháng 6 năm 2026<br/>
                ➔ 2026年6月25日 星期四 (Èr líng èr liù nián liù yuè èrshíwǔ rì xīngqīsì)
            </div>
        </div>
        """.replace("\n", " "), unsafe_allow_html=True)
        render_play_button("二零二六年六月二十五号星期四", "🔊 Nghe phát âm câu ví dụ hoàn chỉnh", key="play_date_full_ex_v6")
        
    elif cur_group["guide"] == "time":
        st.markdown("""
        <div style="background-color: #fef3c7; border-left: 5px solid #d97706; padding: 20px; border-radius: 8px; margin-top: 20px; margin-bottom: 25px; border: 1px solid #fde68a;">
            <h4 style="color: #92400e; margin-top: 0; margin-bottom: 12px; font-weight: bold; font-size: 1.1rem;">
                💡 Các mẫu câu đọc giờ trong tiếng Trung
            </h4>
            <ul style="font-size: 0.95em; line-height: 1.7; color: #92400e; padding-left: 20px; margin-bottom: 0;">
                <li><b>Giờ chẵn:</b> Số giờ + 点 (diǎn). Ví dụ: 10 giờ ➔ 十点 (shí diǎn).</li>
                <li><b>Giờ lẻ phút:</b> Số giờ + 点 + Số phút + 分 (fēn). Ví dụ: 10 giờ 10 phút ➔ 十点十分 (shí diǎn shí fēn).</li>
                <li><b>Giờ rưỡi (30 phút):</b> Số giờ + 点 + 半 (bàn). Ví dụ: 10 giờ rưỡi ➔ 十点半 (shí diǎn bàn).</li>
                <li><b>Giờ khắc (15 hoặc 45 phút):</b> Số giờ + 点 + 一刻 (yí kè - 15 phút) hoặc 三刻 (sān kè - 45 phút). Ví dụ: 10 giờ 15 phút ➔ 十点一刻 (shí diǎn yí kè).</li>
                <li><b>Giờ kém:</b> 差 (chà) + Số phút kém + 分 + Số giờ tiếp theo + 点. Ví dụ: 10 giờ kém 10 phút ➔ 差十分十点 (chà shí fēn shí diǎn).</li>
            </ul>
        </div>
        """.replace("\n", " "), unsafe_allow_html=True)
