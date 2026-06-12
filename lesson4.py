import streamlit as st
import os
import base64
from lessons_data import *
from ui_utils import *

def check_spelling_rule(initial, final, tone_idx):
    # tone_idx: 0 to 4 (0: None/light, 1: tone 1, 2: tone 2, 3: tone 3, 4: tone 4)
    spelled = ""
    
    # Normalize abbreviations when an initial is present
    f_norm = final
    if initial and initial != "(Không có)":
        if final == "uei":
            f_norm = "ui"
        elif final == "iou":
            f_norm = "iu"
            
    if not initial or initial == "(Không có)":
        if final == "ia": spelled = "ya"
        elif final == "ie": spelled = "ye"
        elif final == "iao": spelled = "yao"
        elif final in ["iu", "iou"]: spelled = "you"
        elif final == "ua": spelled = "wa"
        elif final == "uo": spelled = "wo"
        elif final == "uai": spelled = "wai"
        elif final in ["ui", "uei"]: spelled = "wei"
        elif final == "üe": spelled = "yue"
    else:
        # j, q, x compatibility
        if initial in ['j', 'q', 'x']:
            if f_norm in ['ua', 'uo', 'uai', 'ui']:
                return None, f"❌ Lỗi ghép âm: Thanh mẫu <b>{initial}</b> không thể đi cùng nhóm vận mẫu bắt đầu bằng <b>u</b> ({final})!"
            if f_norm == "üe":
                spelled = f"{initial}ue"
            else:
                spelled = f"{initial}{f_norm}"
        # b, p, m, f compatibility
        elif initial in ['b', 'p', 'm', 'f']:
            if f_norm in ['ua', 'uai', 'ui']:
                return None, f"❌ Lỗi ghép âm: Âm môi <b>{initial}</b> không thể đi cùng vận mẫu <b>{final}</b>!"
            if f_norm == "üe":
                return None, f"❌ Lỗi ghép âm: Thanh mẫu <b>{initial}</b> không thể đi cùng vận mẫu <b>üe</b>!"
            if f_norm == 'uo':
                spelled = f"{initial}o"
            else:
                spelled = f"{initial}{f_norm}"
        # d, t, g, k, h, zh, ch, sh, r, z, c, s compatibility
        elif initial in ['d', 't', 'g', 'k', 'h', 'zh', 'ch', 'sh', 'r', 'z', 'c', 's']:
            if f_norm == "üe":
                return None, f"❌ Lỗi ghép âm: Thanh mẫu <b>{initial}</b> không thể đi cùng vận mẫu <b>üe</b>!"
            spelled = f"{initial}{f_norm}"
        # n, l compatibility
        elif initial in ['n', 'l']:
            spelled = f"{initial}{f_norm}"
            
    # Apply Tone Placement rules in Pinyin:
    if tone_idx == 0:
        return spelled, None
        
    tone_vowels = {
        'a': ['ā', 'á', 'ǎ', 'à'],
        'o': ['ō', 'ó', 'ǒ', 'ò'],
        'e': ['ē', 'é', 'ě', 'è'],
        'i': ['ī', 'í', 'ǐ', 'ì'],
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
    elif 'iu' in res:
        res = res.replace('u', tone_vowels['u'][tone_idx - 1])
    elif 'ui' in res:
        res = res.replace('i', tone_vowels['i'][tone_idx - 1])
    elif 'ü' in res:
        res = res.replace('ü', tone_vowels['ü'][tone_idx - 1])
    elif 'u' in res:
        res = res.replace('u', tone_vowels['u'][tone_idx - 1])
    elif 'i' in res:
        res = res.replace('i', tone_vowels['i'][tone_idx - 1])
        
    return res, None

def show_lesson4_finals():
    render_lesson_intro("📚 Bài 4: Vận mẫu kép mở rộng", "Học các vận mẫu kép mở rộng và quy tắc ghép âm nâng cao.")
    
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
        </style>
        
        """,
        unsafe_allow_html=True
    )

    
    st.subheader("1. Chi tiết 9 vận mẫu kép mở rộng")
    
    for g in B2_VAN_MAU_KEP_DATA:
        st.markdown(f"#### 📌 {g['nhom']}")
        for idx, item in enumerate(g["items"]):
            cols = st.columns([3.5, 1.5])
            with cols[0]:
                card_html = f"""
                <div class="final-card" style="background: {item['color']}; border-left: 6px solid {item['border_color']};">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <span class="final-letter" style="color: {item['text_color']};">{item['chu']}</span>
                        <span style="background: white; border: 1px solid {item['border_color']}; color: {item['text_color']}; padding: 3px 10px; border-radius: 20px; font-size: 0.9em; font-weight: bold; font-family: 'Courier New', monospace;">/{item['chu']}/</span>
                    </div>
                    <div style="font-size: 1.05em; font-weight: bold; margin-bottom: 8px; color: #0f172a;">👉 Đọc nhanh: {item['hdsd']}</div>
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
                render_play_button(item["vd_py"], f"🔊 Phát âm từ khóa ({item['vd_py']})", key=f"btn_main_{item['chu']}_{idx}")
                
                st.markdown("<div style='font-size:0.8em; font-weight:bold; color:#64748b; margin-top:12px; margin-bottom:4px;'>LUYỆN TẬP ÂM KHÁC:</div>", unsafe_allow_html=True)
                for s_idx, sub in enumerate(item["more_examples"]):
                    sub_key = f"btn_sub_{item['chu']}_{idx}_{s_idx}"
                    render_play_button(sub["py"], f"🔊 {sub['han']} ({sub['py']}): {sub['vi']}", key=sub_key)
            st.markdown("<br/>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🔑 2. Chính tả Pinyin")
    st.write(
        "Đối với các vận mẫu kép mở rộng, có **3 quy tắc chính tả cực kỳ quan trọng** mà bất kỳ người học tiếng Trung nào cũng phải nằm lòng để tránh nhầm lẫn khi đọc viết:"
    )
    
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%); border-left: 6px solid #D97706; border-radius: 12px; padding: 18px; border: 1px solid #FDE68A; margin-bottom: 20px;">
            <h4 style="color: #92400E; margin-top: 0; margin-bottom: 12px;">🌟 Quy tắc 1: Viết gọn của -iu và -ui</h4>
            <div style="color: #78350F; font-size: 0.95em; line-height: 1.6; margin-bottom: 0;">
                Bản chất: Vận mẫu <span class="spelling-highlight">iu</span> gốc là <b>iou</b>, còn <span class="spelling-highlight">ui</span> gốc là <b>uei</b>. Cách viết thay đổi tùy theo việc đi kèm thanh mẫu:
                <div style="margin-top: 10px; display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                    <div style="background: rgba(255, 255, 255, 0.6); padding: 12px; border-radius: 8px; border: 1px dashed #FCD34D;">
                        <b style="color: #92400E;">1. Có thanh mẫu đứng trước:</b>
                        <br/><i>(Lược bỏ chữ cái ở giữa 'o' hoặc 'e')</i>
                        <br/>• <span class="spelling-highlight">iou</span> ➔ <span class="spelling-highlight">iu</span> (Ví dụ: l + iou ➔ <b>liù</b>)
                        <br/>• <span class="spelling-highlight">uei</span> ➔ <span class="spelling-highlight">ui</span> (Ví dụ: sh + uei ➔ <b>shuǐ</b>)
                    </div>
                    <div style="background: rgba(255, 255, 255, 0.6); padding: 12px; border-radius: 8px; border: 1px dashed #FCD34D;">
                        <b style="color: #92400E;">2. Đứng độc lập (Không có thanh mẫu):</b>
                        <br/><i>(Viết ở dạng đầy đủ, đổi i ➔ y, u ➔ w)</i>
                        <br/>• <span class="spelling-highlight">iou</span> ➔ <span class="spelling-highlight">you</span>
                        <br/>• <span class="spelling-highlight">uei</span> ➔ <span class="spelling-highlight">wei</span>
                    </div>
                </div>
            </div>
        </div>
        
        <div style="background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%); border-left: 6px solid #3B82F6; border-radius: 12px; padding: 18px; border: 1px solid #BFDBFE; margin-bottom: 20px;">
            <h4 style="color: #1E40AF; margin-top: 0; margin-bottom: 10px;">🌟 Quy tắc 2: Biến đổi âm đệm khi đứng một mình</h4>
            <p style="color: #1E3A8A; font-size: 0.95em; line-height: 1.6; margin-bottom: 0;">
                Khi các vận mẫu này không có thanh mẫu đi kèm (đứng độc lập), ta không được viết trực tiếp chữ cái <span class="spelling-highlight">i</span> hay <span class="spelling-highlight">u</span> ở đầu từ:
                <br/>• Nguyên âm đệm <span class="spelling-highlight">i</span> sẽ chuyển thành âm bán nguyên âm <span class="spelling-highlight">y</span> (Ví dụ: <i>ia ➔ ya</i>, <i>ie ➔ ye</i>, <i>iao ➔ yao</i>).
                <br/>• Nguyên âm đệm <span class="spelling-highlight">u</span> sẽ chuyển thành âm bán nguyên âm <span class="spelling-highlight">w</span> (Ví dụ: <i>ua ➔ wa</i>, <i>uo ➔ wo</i>, <i>uai ➔ wai</i>).
                <br/>• Nguyên âm đệm <span class="spelling-highlight">ü</span> sẽ viết thêm chữ <span class="spelling-highlight">y</span> đằng trước và bỏ dấu 2 chấm (Ví dụ: <i>üe ➔ yue</i>).
            </p>
        </div>
        
        <div style="background: linear-gradient(135deg, #F5F3FF 0%, #EDE9FE 100%); border-left: 6px solid #8B5CF6; border-radius: 12px; padding: 18px; border: 1px solid #DDD6FE; margin-bottom: 25px;">
            <h4 style="color: #5B21B6; margin-top: 0; margin-bottom: 10px;">🌟 Quy tắc 3: Triệt tiêu dấu hai chấm của âm tròn môi ü</h4>
            <p style="color: #4C1D95; font-size: 0.95em; line-height: 1.6; margin-bottom: 0;">
                Vận mẫu tròn môi <span class="spelling-highlight">üe</span> khi đi sau nhóm thanh mẫu mặt lưỡi <span class="spelling-highlight">j, q, x</span> và âm đệm <span class="spelling-highlight">y</span> sẽ được lược bỏ hoàn toàn dấu hai chấm trên đầu, chỉ viết là <span class="spelling-highlight">ue</span> nhưng cách đọc vẫn giữ nguyên âm tròn môi /ü/ (Ví dụ: <i>j + üe ➔ jué</i>, <i>q + üe ➔ què</i>, <i>x + üe ➔ xuě</i>).
                <br/>⚠️ <i>Lưu ý:</i> Đối với hai thanh mẫu uốn lưỡi <span class="spelling-highlight">n, l</span>, dấu hai chấm <b>bắt buộc giữ nguyên</b> (<i>nüe</i>, <i>lüe</i>) .
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.subheader("🎮 3. Công cụ Ghép âm Tương tác ")
    st.write(
        "Hãy thử sức tự mình tạo ra các âm tiết tiếng Trung! Hãy chọn một **Thanh mẫu**, một **Vận mẫu kép mở rộng** và một **Thanh điệu** dưới đây. Hệ thống sẽ tự động ghép âm chuẩn xác theo quy tắc Pinyin và cho bạn nghe phát âm trực tiếp!"
    )
    
    cols_sel = st.columns(3)
    
    with cols_sel[0]:
        initials_list = ["(Không có)", "b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "j", "q", "x", "zh", "ch", "sh", "r", "z", "c", "s"]
        sel_initial = st.selectbox("Chọn Thanh mẫu (Initial):", initials_list, index=0, key="sandbox_initial")
        
    with cols_sel[1]:
        finals_list = ["ia", "ie", "iao", "iu", "ua", "uo", "uai", "ui", "üe"]
        sel_final = st.selectbox("Chọn Vận mẫu kép mở rộng (Final):", finals_list, index=0, key="sandbox_final")
        
    with cols_sel[2]:
        tones_list = [
            "Thanh nhẹ",
            "Thanh 1",
            "Thanh 2",
            "Thanh 3",
            "Thanh 4"
        ]
        sel_tone = st.selectbox("Chọn Thanh điệu (Tone):", tones_list, index=1, key="sandbox_tone")
        
    tone_idx = tones_list.index(sel_tone)
    
    spelled_res, err = check_spelling_rule(sel_initial, sel_final, tone_idx)
    
    st.markdown("<br/>", unsafe_allow_html=True)
    if err:
        st.markdown(
            f"""
            <div style="background-color: #FEF2F2; border: 1px solid #FCA5A5; border-radius: 12px; padding: 18px; text-align: center;">
                <span style="font-size: 1.1em; color: #DC2626; font-weight: bold;">{err}</span>
                <p style="color: #991B1B; font-size: 0.9em; margin-top: 6px; margin-bottom: 0;">
                    Vui lòng chọn tổ hợp ghép âm hợp lệ khác để tiếp tục thực hành.
                </p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%); border: 1px solid #A7F3D0; border-radius: 12px; padding: 22px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.04);">
                <div style="font-size: 0.85em; color: #065F46; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;">KẾT QUẢ PHIÊN ÂM CHUẨN XÁC:</div>
                <div style="font-size: 3.5em; font-weight: bold; color: #047857; font-family: 'Courier New', monospace; margin: 10px 0; text-shadow: 0 1px 2px rgba(0,0,0,0.05);">{spelled_res}</div>
                <div style="font-size: 0.95em; color: #065F46; font-style: italic;">
                    Ghép từ: <b>{sel_initial if sel_initial != '(Không có)' else ''}</b> + <b>{sel_final}</b> + <b>{sel_tone.split(' - ')[0]}</b>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("<br/>", unsafe_allow_html=True)
        col_btn = st.columns([1, 2, 1])
        with col_btn[1]:
            render_play_button(spelled_res, "🔊 Phát âm Âm tiết vừa ghép", key="sandbox_play_btn", type="primary")

def show_lesson4_classroom_arena():
    render_lesson_intro("📚 Bài 4.1: Luyện tập", "Hoạt động thực hành nhóm và phản xạ nhanh dành cho lớp học online.")
    
    
    tab_game1, tab_game2, tab_game3 = st.tabs([
        "🎲 1. Vòng quay May mắn (Random Call)",
        "🕵️ 2. Kẻ mạo danh Chính tả (Spot the Imposter)",
        "🧩 3. Lắp ráp Câu thần tốc (Sentence Builder)"
    ])
    
    # ------------------ GAME 1: RANDOM CALL ------------------
    with tab_game1:
        st.markdown("### 🎲 Thử thách Gọi tên Ngẫu nhiên")
        
        student_list_raw = st.text_input("Nhập tên các học viên (cách nhau bằng dấu phẩy):", "Tiên, Vy, Trân, Thanh", key="classroom_students_input")
        students = [s.strip() for s in student_list_raw.split(",") if s.strip()]
        
        # Danh sách từ vựng & câu thực hành ngữ cảnh dựa trên bài 1 - 4 (không chứa vận mẫu mũi)
        RANDOM_CALL_POOL = [
            {"pinyin": "wǒ", "hanzi": "我", "meaning": "Tôi", "sentence_pinyin": "Wǒ yéye ài zāihuā.", "sentence_hanzi": "我爷爷爱栽花。", "sentence_meaning": "Ông nội tôi yêu thích việc trồng hoa."},
            {"pinyin": "nǐ", "hanzi": "你", "meaning": "Bạn / Anh / Chị", "sentence_pinyin": "Nǐ hǎo ma?", "sentence_hanzi": "你好吗？", "sentence_meaning": "Bạn khỏe không?"},
            {"pinyin": "māma", "hanzi": "妈妈", "meaning": "Mẹ", "sentence_pinyin": "Māma ài wǒ.", "sentence_hanzi": "妈妈爱我。", "sentence_meaning": "Mẹ yêu tôi."},
            {"pinyin": "nǚ'ér", "hanzi": "女儿", "meaning": "Con gái", "sentence_pinyin": "Tā shì wǒ de nǚ'ér.", "sentence_hanzi": "她是我的女儿。", "sentence_meaning": "Cô ấy là con gái của tôi."},
            {"pinyin": "huā", "hanzi": "花", "meaning": "Đóa hoa / Hoa", "sentence_pinyin": "Zhè shì wǒ de huā.", "sentence_hanzi": "这是我的花。", "sentence_meaning": "Đây là hoa của tôi."},
            {"pinyin": "shuǐ", "hanzi": "水", "meaning": "Nước", "sentence_pinyin": "Wǒ hē shuǐ.", "sentence_hanzi": "我喝水。", "sentence_meaning": "Tôi uống nước."},
            {"pinyin": "liù", "hanzi": "六", "meaning": "Số sáu", "sentence_pinyin": "Wǒ yǒu liù ge wáwa.", "sentence_hanzi": "我有六个娃娃。", "sentence_meaning": "Tôi có sáu búp bê."},
            {"pinyin": "jiějie", "hanzi": "姐姐", "meaning": "Chị gái", "sentence_pinyin": "Jiějie ài wáwa.", "sentence_hanzi": "姐姐爱娃娃。", "sentence_meaning": "Chị gái yêu búp bê."},
            {"pinyin": "bàba", "hanzi": "爸爸", "meaning": "Bố / Cha", "sentence_pinyin": "Bàba ài māma.", "sentence_hanzi": "爸爸爱妈妈。", "sentence_meaning": "Bố yêu mẹ."}
        ]
        
        if "arena_item" not in st.session_state:
            st.session_state.arena_item = RANDOM_CALL_POOL[0]
        if "arena_student" not in st.session_state:
            st.session_state.arena_student = "Học viên"
            
        if st.button("🎲 QUAY NGẪU NHIÊN (Chọn Học viên & Từ)", type="primary", use_container_width=True):
            st.session_state.arena_item = random.choice(RANDOM_CALL_POOL)
            if students:
                st.session_state.arena_student = random.choice(students)
            else:
                st.session_state.arena_student = "Học viên"
            st.rerun()
            
        item = st.session_state.arena_item
        
        st.markdown(
            f"""<div style="background: linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%); border: 2px solid #FDE68A; border-radius: 16px; padding: 30px; margin-top: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
<div style="font-size: 1.1em; color: #92400E; font-weight: bold; text-transform: uppercase; text-align: center;">🌟 Lượt đọc của học viên:</div>
<div style="font-size: 2.8em; font-weight: 800; color: #D97706; margin: 10px 0; text-align: center;">👉 {st.session_state.arena_student} 👈</div>
<hr style="border: 0; border-top: 1px solid #FCD34D; margin: 20px 0;"/>
<div style="display: flex; flex-direction: column; gap: 20px;">
<div style="background: white; border-radius: 12px; padding: 18px; border: 1px solid #FCD34D;">
<span style="font-size: 0.95em; font-weight: bold; color: #b45309; text-transform: uppercase;">🔹 Bước 1: Đọc từ khóa</span>
<div style="font-size: 2.5em; font-weight: bold; color: #1e293b; font-family: 'Courier New', monospace; margin: 8px 0;">
{item['pinyin']} <span style="font-size: 0.75em; color: #64748b; font-weight: normal;">({item['hanzi']})</span>
</div>
<span style="color: #475569; font-size: 1em;">Nghĩa: <b>{item['meaning']}</b></span>
</div>
<div style="background: white; border-radius: 12px; padding: 18px; border: 1px solid #FCD34D;">
<span style="font-size: 0.95em; font-weight: bold; color: #b45309; text-transform: uppercase;">🔸 Bước 2: Đọc câu mở rộng (Đầy đủ ngữ cảnh)</span>
<div style="font-size: 1.8em; font-weight: bold; color: #0f172a; margin: 10px 0; font-family: 'Courier New', monospace; line-height: 1.4;">
{item['sentence_pinyin']}<br/>
<span style="font-size: 0.85em; color: #047857; font-weight: normal; font-family: inherit;">{item['sentence_hanzi']}</span>
</div>
<span style="color: #475569; font-size: 1em;">Nghĩa: <b>{item['sentence_meaning']}</b></span>
</div>
</div>
</div>""",
            unsafe_allow_html=True
        )
        
        st.markdown("<br/>", unsafe_allow_html=True)
        col_btns = st.columns([1, 1, 1])
        with col_btns[0]:
            render_play_button(item['pinyin'], "🔊 Phát âm Từ khóa", key="arena_play_word", type="secondary")
        with col_btns[1]:
            render_play_button(item['sentence_hanzi'], "🔊 Phát âm Câu mở rộng", key="arena_play_sentence", type="secondary")
        with col_btns[2]:
            if st.button("🎉 Đọc đúng! Thưởng điểm", use_container_width=True, key="arena_reward_btn"):
                st.balloons()
                st.success(f"Cộng 10 điểm thưởng cho bạn **{st.session_state.arena_student}**! 🏆")

    # ------------------ GAME 2: IMPOSTER ------------------
    with tab_game2:
        st.markdown("### 🕵️ Tìm kiếm Kẻ mạo danh Chính tả")
        
        imposter_questions = [
            {"title": "Thử thách 1: j + üe + thanh 2", "options": ["1. jüé", "2. qué", "3. jué"], "correct_idx": 2, "explain": "Quy tắc 3: Sau thanh mẫu mặt lưỡi 'j, q, x', üe lược bỏ dấu hai chấm viết thành ue (nhưng vẫn giữ nguyên cách đọc tròn môi)."},
            {"title": "Thử thách 2: sh + uei + thanh 3", "options": ["1. shuǐ", "2. shueǐ", "3. shǔi"], "correct_idx": 0, "explain": "Quy tắc 1: 'uei' khi đi sau thanh mẫu viết rút gọn thành 'ui'. Dấu thanh điệu đặt trên chữ cái 'i' đứng sau."},
            {"title": "Thử thách 3: Vận mẫu 'uei' đứng một mình", "options": ["1. uēi", "2. wei", "3. yui"], "correct_idx": 1, "explain": "Quy tắc 1: Khi đứng độc lập không có thanh mẫu đi kèm, 'uei' viết ở dạng đầy đủ là 'wei'."},
            {"title": "Thử thách 4: y + ia + thanh 1  (con vịt)", "options": ["1. yia", "2. ya", "3. iā"], "correct_idx": 1, "explain": "Quy tắc viết Pinyin: Khi vận mẫu bắt đầu bằng 'i' đứng độc lập không có thanh mẫu đi kèm, 'i' được viết thành 'y' (ia viết thành ya)."},
            {"title": "Thử thách 5: w + uo + thanh 3  (tôi)", "options": ["1. uǒ", "2. wǒ", "3. wuǒ"], "correct_idx": 1, "explain": "Quy tắc viết Pinyin: Khi vận mẫu bắt đầu bằng 'u' đứng độc lập không có thanh mẫu đi kèm, 'u' được viết thành 'w' (uo viết thành wo)."}
        ]
        
        if "imposter_q_idx" not in st.session_state:
            st.session_state.imposter_q_idx = 0
        if "imposter_revealed" not in st.session_state:
            st.session_state.imposter_revealed = False
        if "imposter_selected_idx" not in st.session_state:
            st.session_state.imposter_selected_idx = None
            
        q_idx = st.session_state.imposter_q_idx
        q_data = imposter_questions[q_idx]
        
        st.markdown(f"#### {q_data['title']}")
        st.write("👇 Hãy click vào ô đáp án mà bạn tin là viết **ĐÚNG CHÍNH TẢ**:")
        
        cols_imp = st.columns(3)
        for idx, opt in enumerate(q_data["options"]):
            word_text = opt.split('. ')[1]
            with cols_imp[idx]:
                if st.session_state.imposter_selected_idx is None:
                    # Square card before selection
                    st.markdown(
                        f"""<div style="border: 2px solid #cbd5e1; background-color: #f8fafc; border-radius: 12px; padding: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02); transition: all 0.2s; margin-bottom: 8px;">
<span style="font-weight: bold; color: #64748b; font-size: 0.85em; text-transform: uppercase;">❓ ĐANG CHỜ</span>
<div style="font-size: 1.8em; font-weight: bold; color: #1e293b; margin-top: 10px; font-family: 'Courier New', monospace;">{word_text}</div>
</div>""",
                        unsafe_allow_html=True
                    )
                    if st.button(f"Chọn {word_text}", use_container_width=True, key=f"imp_opt_btn_{q_idx}_{idx}"):
                        st.session_state.imposter_selected_idx = idx
                        st.session_state.imposter_revealed = True
                        if idx == q_data["correct_idx"]:
                            st.toast("🎉 Chính xác!", icon="✅")
                        else:
                            st.toast("❌ Sai rồi!", icon="❌")
                        st.rerun()
                else:
                    # Reveal status cards
                    if idx == q_data["correct_idx"]:
                        border_color = "#10B981"
                        bg_color = "#ECFDF5"
                        label_icon = "✅ ĐÚNG (Chuẩn)"
                    elif idx == st.session_state.imposter_selected_idx:
                        border_color = "#EF4444"
                        bg_color = "#FEF2F2"
                        label_icon = "❌ BẠN ĐÃ CHỌN SAI"
                    else:
                        border_color = "#cbd5e1"
                        bg_color = "#f8fafc"
                        label_icon = "⚪ MẠO DANH"
                        
                    st.markdown(
                        f"""<div style="border: 2px solid {border_color}; background-color: {bg_color}; border-radius: 12px; padding: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02); transition: all 0.2s; min-height: 120px;">
<span style="font-weight: bold; color: {border_color}; font-size: 0.85em; text-transform: uppercase;">{label_icon}</span>
<div style="font-size: 1.8em; font-weight: bold; color: #1e293b; margin-top: 10px; font-family: 'Courier New', monospace;">{word_text}</div>
</div>""",
                        unsafe_allow_html=True
                    )
        
        st.markdown("<br/>", unsafe_allow_html=True)
        col_imp_actions = st.columns(2)
        with col_imp_actions[0]:
            if st.button("⏭️ Thử thách tiếp theo", use_container_width=True, key="next_imp_btn"):
                st.session_state.imposter_q_idx = (q_idx + 1) % len(imposter_questions)
                st.session_state.imposter_selected_idx = None
                st.session_state.imposter_revealed = False
                st.rerun()
        with col_imp_actions[1]:
            if st.button("🔄 Khởi động lại", use_container_width=True, key="reset_imp_btn"):
                st.session_state.imposter_q_idx = 0
                st.session_state.imposter_selected_idx = None
                st.session_state.imposter_revealed = False
                st.rerun()
                
        if st.session_state.imposter_revealed:
            st.markdown(
                f"""
                <div style="background-color: #EFF6FF; border-left: 6px solid #3B82F6; border-radius: 10px; padding: 15px; margin-top: 15px;">
                    <b style="color: #1E40AF;">💡 Giải thích chính tả:</b><br/>
                    <span style="color: #1E3A8A; font-size: 0.95em;">{q_data['explain']}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

    # ------------------ GAME 3: SENTENCE BUILDER ------------------
    with tab_game3:
        st.markdown("### 🧩 Sentence Builder")
        st.write("Học viên lắp ráp các mảnh ghép từ vựng rời rạc thành một câu tiếng Trung hoàn chỉnh và chính xác theo nghĩa gợi ý.")
        builder_puzzles = [
            {
                "meaning": "Đây là nhà của tôi.",
                "correct": ["这 (Zhè)", "是 (shì)", "我 (wǒ)", "... (de)", "家 (jiā)"],
                "full_pinyin": "Zhè shì wǒ de jiā.",
                "full_hanzi": "这是我的家。",
                "tip": "Chú ý định ngữ sở hữu '我的' (của tôi) đứng trước danh từ '家' (nhà)."
            },
            {
                "meaning": "Chị gái tôi thích búp bê.",
                "correct": ["我 (wǒ)", "的 (de)", "姐姐 (jiějie)", "喜欢 (xǐhuān)", "我 (wǒ)"],
                "full_pinyin": "Wǒ de jiějie xǐhuān wáwa.",
                "full_hanzi": "我的姐姐喜欢娃娃。",
                "tip": "Định ngữ sở hữu '我的' đứng trước danh từ '姐姐'."
            },
            {
                "meaning": "Bố yêu mẹ.",
                "correct": ["爸爸 (Bàba)", "爱 (ài)", "妈妈 (māma)"],
                "full_pinyin": "Bàba ài māma.",
                "full_hanzi": "爸爸爱妈妈。",
                "tip": "Cấu trúc cơ bản: Chủ ngữ (爸爸) + Động từ (爱) + Tân ngữ (妈妈)."
            },
            {
                "meaning": "Cô ấy là một bé gái ngoan.",
                "correct": ["她 (Tā)", "是 (shì)", "好 (hǎo)", "女孩 (nǚhái)"],
                "full_pinyin": "Tā ...",
                "full_hanzi": "她是好女孩。",
                "tip": "Động từ hệ '是' đi kèm cụm danh từ '好女孩' (tính từ '好' đứng liền trước bổ nghĩa cho danh từ '女孩')."
            },
            {
                "meaning": "Anh trai có bạn gái.",
                "correct": ["哥哥 (Gēge)", "有 (yǒu)", "女朋友 (nǚ péngyǒu)"],
                "full_pinyin": "Gēge yǒu nǚ péngyǒu.",
                "full_hanzi": "哥哥有女朋友。",
                "tip": "Cấu trúc biểu thị quyền sở hữu: Chủ ngữ (哥哥) + Động từ (yǒu - 有) + Tân ngữ (nǚ péngyǒu)."
            },
            {
                "meaning": "Đây là búp bê của chị gái.",
                "correct": ["这 (Zhè)", "是 (shì)", "姐姐 (jiějie)", "的 (de)", "娃娃 (wáwa)"],
                "full_pinyin": "Zhè... (Zhè)",
                "full_hanzi": "这是姐姐的娃娃。",
                "tip": "Định ngữ sở hữu '姐姐的' (của chị gái) đứng trước trung tâm ngữ '娃娃' (búp bê)."
            }
        ]
        
        # Post-correct correct lists and full_hanzi/full_pinyin values to ensure no placeholders
        builder_puzzles[0]["correct"] = ["这 (Zhè)", "是 (shì)", "我 (wǒ)", "的 (de)", "家 (jiā)"]
        builder_puzzles[1]["full_hanzi"] = "我的姐姐爱我。"
        builder_puzzles[3]["full_pinyin"] = "Tā shì hǎo nǚhái."
        builder_puzzles[5]["full_pinyin"] = "Zhè... (Zhè)"
        builder_puzzles[5]["full_pinyin"] = "Zhè shì jiějie de wáwa."
        

        if "builder_q_idx" not in st.session_state:
            st.session_state.builder_q_idx = 0
            
        b_idx = st.session_state.builder_q_idx
        puzzle = builder_puzzles[b_idx]
        
        scramble_key = f"scrambled_words_{b_idx}"
        if scramble_key not in st.session_state:
            words = list(puzzle["correct"])
            random.seed(b_idx + 42)
            random.shuffle(words)
            st.session_state[scramble_key] = words
            
        if "builder_assembled" not in st.session_state:
            st.session_state.builder_assembled = []
            
        if "builder_checked" not in st.session_state:
            st.session_state.builder_checked = False
            
        if "builder_correct" not in st.session_state:
            st.session_state.builder_correct = False

        st.markdown(
            f"""<div style="background: linear-gradient(135deg, #EEF2F6 0%, #E2E8F0 100%); border: 2px solid #CBD5E1; border-radius: 12px; padding: 20px; text-align: center; margin-bottom: 15px;">
<span style="font-size: 0.85em; color: #475569; font-weight: bold; text-transform: uppercase;">DỊCH CÂU SAU SANG TIẾNG TRUNG:</span>
<div style="font-size: 1.8em; font-weight: bold; color: #1E293B; margin-top: 5px;">"{puzzle['meaning']}"</div>
</div>""",
            unsafe_allow_html=True
        )

        st.markdown("#### 📥 Câu của bạn:")
        assembled = st.session_state.builder_assembled
        
        if not assembled:
            st.info("💡 Hãy click vào các mảnh ghép từ vựng phía dưới để lắp ghép câu.")
        else:
            cols_as = st.columns(len(assembled) + 1)
            for a_idx, word in enumerate(assembled):
                with cols_as[a_idx]:
                    if st.button(f"{word} ❌", key=f"as_word_{a_idx}", use_container_width=True):
                        assembled.pop(a_idx)
                        st.session_state.builder_checked = False
                        st.rerun()
            with cols_as[-1]:
                st.caption("👈 Nhấp để xóa")

        st.markdown("#### 🧩 Các mảnh ghép từ vựng:")
        available_words = st.session_state[scramble_key]
        
        cols_av = st.columns(len(available_words))
        for w_idx, word in enumerate(available_words):
            with cols_av[w_idx]:
                is_selected = word in assembled
                if st.button(word, key=f"av_word_{w_idx}", disabled=is_selected, use_container_width=True, type="secondary" if is_selected else "primary"):
                    assembled.append(word)
                    st.session_state.builder_checked = False
                    st.rerun()

        st.markdown("<br/>", unsafe_allow_html=True)
        
        col_actions = st.columns(4)
        with col_actions[0]:
            if st.button("🧹 Xóa hết", use_container_width=True, key="builder_clear_btn", disabled=len(assembled) == 0):
                st.session_state.builder_assembled = []
                st.session_state.builder_checked = False
                st.rerun()
                
        with col_actions[1]:
            if st.button("✅ Kiểm tra", use_container_width=True, key="builder_check_btn", type="primary", disabled=len(assembled) < len(puzzle["correct"])):
                st.session_state.builder_checked = True
                st.session_state.builder_correct = (assembled == puzzle["correct"])
                if st.session_state.builder_correct:
                    st.toast("🎉 Chính xác!", icon="✅")
                else:
                    st.toast("❌ Chưa chính xác!", icon="❌")
                st.rerun()
                
        with col_actions[2]:
            if st.button("⏭️ Câu tiếp theo", use_container_width=True, key="builder_next_btn"):
                st.session_state.builder_q_idx = (b_idx + 1) % len(builder_puzzles)
                st.session_state.builder_assembled = []
                st.session_state.builder_checked = False
                st.session_state.builder_correct = False
                next_key = f"scrambled_words_{(b_idx + 1) % len(builder_puzzles)}"
                if next_key in st.session_state:
                    del st.session_state[next_key]
                st.rerun()
                
        with col_actions[3]:
            if st.button("🔄 Bắt đầu lại", use_container_width=True, key="builder_reset_btn"):
                st.session_state.builder_q_idx = 0
                st.session_state.builder_assembled = []
                st.session_state.builder_checked = False
                st.session_state.builder_correct = False
                for i in range(len(builder_puzzles)):
                    k = f"scrambled_words_{i}"
                    if k in st.session_state:
                        del st.session_state[k]
                st.rerun()

        if st.session_state.builder_checked:
            if st.session_state.builder_correct:
                st.balloons()
                st.markdown(
                    f"""<div style="background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%); border: 2px solid #A7F3D0; border-radius: 12px; padding: 20px; margin-top: 15px;">
<h4 style="color: #065F46; margin-top: 0; margin-bottom: 5px;">🎉 GHÉP CÂU CHUẨN XÁC HOÀN TOÀN!</h4>
<div style="font-size: 2.2em; font-weight: bold; color: #047857; margin-bottom: 2px;">{puzzle['full_hanzi']}</div>
<div style="font-family: 'Courier New', monospace; font-size: 1.3em; font-weight: bold; color: #065F46;">{puzzle['full_pinyin']}</div>
</div>""",
                    unsafe_allow_html=True
                )
                
                st.markdown("<br/>🔊 <b>Nghe đọc phát âm chuẩn cả câu:</b>", unsafe_allow_html=True)
                cols_aud = st.columns([1.5, 4.5])
                with cols_aud[0]:
                    render_play_button(puzzle['full_hanzi'], "🔊 Nghe cả câu", key=f"builder_audio_play_{b_idx}")
            else:
                st.markdown(
                    f"""<div style="background: #FEF2F2; border: 2px solid #FCA5A5; border-radius: 12px; padding: 20px; margin-top: 15px; color: #991B1B;">
<h4 style="margin-top: 0; margin-bottom: 5px; color: #991B1B;">❌ TRẬT TỰ TỪ CHƯA ĐÚNG!</h4>
<p style="font-size: 0.95em; margin-bottom: 0; color: #7F1D1D;">
<b>Gợi ý cú pháp:</b> {puzzle['tip']}
</p>
</div>""",
                    unsafe_allow_html=True
                )

def show_lesson4_qa_and_dialogues():
    import random
    render_lesson_intro("🗣️ Bài 4.2: Phản xạ & Giao tiếp", "Thực hành phản xạ hỏi đáp nhanh và đóng vai giao tiếp theo nhóm/cặp trên lớp học.")
    
    tab_qa, tab_dialogues, tab_game = st.tabs([
        "🗣️ Q&A Reading Challenge",
        "👥 Role-Play Dialogues",
        "🎮 Reflex Game Arena"
    ])
    
    with tab_qa:
        
        QA_CLASSROOM_CHALLENGES = [
            {
                "question_pinyin": "Nǐ jiějie è ma?",
                "question_hanzi": "你姐姐饿吗？",
                "question_meaning": "Chị gái bạn đói không?",
                "choices": [
                    "Wǒ jiějie bù è, tā hěn lèi. (我姐姐不饿，她很累。)",
                    "Wǒ yéye hē shuǐ. (我爷爷喝水。)",
                    "Tā bù xǐhuān wáwa. (他不喜欢娃娃。)"
                ],
                "choices_meaning": [
                    "Chị gái tôi không đói, chị ấy rất mệt.",
                    "Ông nội tôi uống nước.",
                    "Nó không thích búp bê."
                ],
                "answer_idx": 0,
                "hint": "Đáp án đúng phải liên quan đến câu hỏi về 'chị gái' (jiějie - vận mẫu ie) và tình trạng 'đói' (è - vận mẫu e). 'lèi' (mệt) chứa vận mẫu kép 'ei' đã học.",
                "pron_focus": "Vận mẫu kép: ie (jiějie), ei (lèi) và vận mẫu đơn e (è)."
            },
            {
                "question_pinyin": "Zhè gè yuè nǐ máng ma?",
                "question_hanzi": "这个月你忙吗？",
                "question_meaning": "Tháng này bạn bận không?",
                "choices": [
                    "Bàba ài chī yúròu. (爸爸爱吃鱼肉。)",
                    "Zhè gè yuè wǒ bù máng, wǒ xué Hànyǔ. (这个月我不忙，我学汉语。)",
                    "Tā chī niúròu. (他吃牛肉。)"
                ],
                "choices_meaning": [
                    "Bố thích ăn thịt cá.",
                    "Tháng này tôi không bận, tôi học tiếng Trung.",
                    "Cậu ấy ăn thịt bò."
                ],
                "answer_idx": 1,
                "hint": "Trả lời cho câu hỏi thời gian 'Tháng này' (zhè gè yuè - vận mẫu üe trong yuè) và hành động 'học tiếng Trung' (xué Hànyǔ - vận mẫu üe trong xué).",
                "pron_focus": "Vận mẫu kép: üe (yuè, xué) và vận mẫu kép cơ bản đã học."
            },
            {
                "question_pinyin": "Zhè shì nǐ de wáwa ma?",
                "question_hanzi": "这是你的娃娃吗？",
                "question_meaning": "Đây là búp bê của bạn à?",
                "choices": [
                    "Wǒmen qù chī jī. (我们去吃鸡。)",
                    "Tā chī niúròu. (他吃牛肉。)",
                    "Bú shì, zhè shì wǒ nǚpéngyou de wáwa. (不是，这是我女朋友的娃娃。)"
                ],
                "choices_meaning": [
                    "Chúng tôi đi ăn gà.",
                    "Anh ấy ăn thịt bò.",
                    "Không phải, đây là búp bê của bạn gái tôi."
                ],
                "answer_idx": 2,
                "hint": "Câu trả lời xác nhận hoặc phủ định về vật sở hữu 'búp bê' (wáwa - vận mẫu ua) của 'bạn gái' (nǚpéngyou - vận mẫu ü trong nǚ và ou trong péngyou).",
                "pron_focus": "Vận mẫu kép: ua (wáwa), ou (péngyou) và vận mẫu đơn ü (nǚ)."
            },
            {
                "question_pinyin": "Nǐmen qù hē nǎichá ma?",
                "question_hanzi": "你们去喝奶茶吗？",
                "question_meaning": "Các bạn đi uống trà sữa không?",
                "choices": [
                    "Wǒmen bù hē nǎichá, wǒmen hē shuǐ. (我们不喝奶茶，我们喝水。)",
                    "Tā hěn shuài. (他很帅。)",
                    "Māma ài wáwa. (妈妈爱娃娃。)"
                ],
                "choices_meaning": [
                    "Chúng tôi không uống trà sữa, chúng tôi uống nước.",
                    "Anh ấy rất đẹp trai.",
                    "Mẹ yêu búp bê."
                ],
                "answer_idx": 0,
                "hint": "Hỏi về 'các bạn' (nǐmen) và hành động 'uống trà sữa' (hē nǎichá). Trả lời phải dùng ngôi 'chúng tôi' (wǒmen - vận mẫu uo) và từ 'uống nước' (hē shuǐ - vận mẫu ui).",
                "pron_focus": "Vận mẫu kép: uo (wǒmen), ui (shuǐ), ai (nǎichá)."
            },
            {
                "question_pinyin": "Tā gēge shuài ma?",
                "question_hanzi": "他哥哥帅吗？",
                "question_meaning": "Anh trai cậu ấy đẹp trai không?",
                "choices": [
                    "Tā hěn máng. (他很忙。)",
                    "Tā gēge hěn shuài, tā shì shuàigē. (他哥哥很帅，他是帅哥。)",
                    "Wǒ yéye hē nǎichá. (我爷爷喝奶茶。)"
                ],
                "choices_meaning": [
                    "Cô ấy rất bận.",
                    "Anh trai cậu ấy rất đẹp trai, anh ấy là soái ca.",
                    "Ông nội tôi uống trà sữa."
                ],
                "answer_idx": 1,
                "hint": "Hỏi về tính chất 'đẹp trai' (shuài - vận mẫu uai). Câu trả lời lập lại thuộc tính 'shuài' và bổ sung 'shuàigē' (soái ca).",
                "pron_focus": "Vận mẫu kép: uai (shuài, shuàigē) và vận mẫu kép cơ bản."
            },
            {
                "question_pinyin": "Yéye de jiā yǒu gǒu ma?",
                "question_hanzi": "爷爷的家有狗吗？",
                "question_meaning": "Nhà của ông nội có chó không?",
                "choices": [
                    "Tā bù chī niúròu. (他不吃牛肉。)",
                    "Wǒmen hē shuǐ. (我们喝水。)",
                    "Yéye de jiā méiyǒu gǒu, yǒu yā. (爷爷的家没有狗，有鸭。)"
                ],
                "choices_meaning": [
                    "Nó không ăn thịt bò.",
                    "Chúng tôi uống nước.",
                    "Nhà ông nội không có chó, có vịt."
                ],
                "answer_idx": 2,
                "hint": "Hỏi về 'nhà ông nội' (yéye de jiā - vận mẫu ie và ia) có 'chó' không (gǒu - vận mẫu ou). Trả lời phủ định 'không có' (méiyǒu - vận mẫu iu/you) và nhắc đến 'vịt' (yā - vận mẫu ia).",
                "pron_focus": "Vận mẫu kép: ie (yéye), ia (jiā, yā), ou (gǒu, yǒu)."
            }
        ]

        if "qa_class_idx" not in st.session_state:
            st.session_state.qa_class_idx = 0
        if "qa_class_selected" not in st.session_state:
            st.session_state.qa_class_selected = None
        if "qa_class_confirmed" not in st.session_state:
            st.session_state.qa_class_confirmed = False
            
        c_idx = st.session_state.qa_class_idx
        c_data = QA_CLASSROOM_CHALLENGES[c_idx]
        
        cols_q = st.columns([8, 2])
        with cols_q[0]:
            st.markdown(
                f"""<div style="background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%); border: 1px solid #BFDBFE; border-radius: 10px; padding: 12px 18px; margin-bottom: 5px;">
<span style="font-size: 0.8em; color: #1E40AF; font-weight: bold; text-transform: uppercase;">CÂU HỎI {c_idx + 1}/{len(QA_CLASSROOM_CHALLENGES)}:</span>
<div style="font-size: 1.8em; font-weight: bold; color: #1E3A8A; font-family: 'Courier New', monospace; margin-top: 2px;">
{c_data['question_pinyin']} &nbsp;&nbsp;&nbsp;&nbsp; <span style="font-size: 0.9em; color: #2563EB;">{c_data['question_hanzi']}</span>
</div>
<span style="color: #475569; font-size: 0.95em;">Nghĩa: <b>"{c_data['question_meaning']}"</b></span>
</div>""",
                unsafe_allow_html=True
            )
        with cols_q[1]:
            st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)
            render_play_button(c_data['question_hanzi'], "🔊 Nghe câu hỏi", key=f"qa_class_q_play_{c_idx}")
            
        st.write("👉 **Chọn đáp án đúng:**")
        
        confirmed = st.session_state.qa_class_confirmed
        sel_choice = st.session_state.qa_class_selected
        
        for idx, choice in enumerate(c_data["choices"]):
            is_sel = (sel_choice == idx)
            btn_type = "secondary"
            btn_label = choice
            
            if confirmed:
                if idx == c_data["answer_idx"]:
                    btn_label = f"✅ {choice} (Chính xác)"
                    btn_type = "primary"
                elif is_sel:
                    btn_label = f"❌ {choice} (Bạn chọn chưa đúng)"
                    btn_type = "primary"
            else:
                if is_sel:
                    btn_label = f"👉 {choice}"
                    btn_type = "primary"
                    
            if st.button(btn_label, key=f"qa_class_btn_{c_idx}_{idx}", type=btn_type, use_container_width=True, disabled=confirmed):
                st.session_state.qa_class_selected = idx
                st.rerun()
                
        st.markdown("<br/>", unsafe_allow_html=True)
        
        col_qa_acts = st.columns(4)
        with col_qa_acts[0]:
            if st.button("🚀 Xác nhận đáp án", type="primary", use_container_width=True, key=f"qa_class_confirm_{c_idx}", disabled=confirmed or (sel_choice is None)):
                st.session_state.qa_class_confirmed = True
                if sel_choice == c_data["answer_idx"]:
                    st.toast("🎉 Chính xác!", icon="✅")
                else:
                    st.toast("❌ Chưa đúng!", icon="❌")
                st.rerun()
        with col_qa_acts[1]:
            if st.button("⏭️ Câu tiếp theo", use_container_width=True, key=f"qa_class_next_{c_idx}", disabled=not confirmed):
                st.session_state.qa_class_idx = (c_idx + 1) % len(QA_CLASSROOM_CHALLENGES)
                st.session_state.qa_class_selected = None
                st.session_state.qa_class_confirmed = False
                st.rerun()
        with col_qa_acts[2]:
            if st.button("🔄 Khởi động lại", use_container_width=True, key=f"qa_class_reset_{c_idx}"):
                st.session_state.qa_class_idx = 0
                st.session_state.qa_class_selected = None
                st.session_state.qa_class_confirmed = False
                st.rerun()
                
        if confirmed:
            if sel_choice == c_data["answer_idx"]:
                student_list_raw = st.session_state.get("classroom_students_input", "Tiên, Vy, Trân, Thanh")
                students = [s.strip() for s in student_list_raw.split(",") if s.strip()]
                target_reader = random.choice(students) if students else "Học viên"
                
                ans_text = c_data["choices"][c_data["answer_idx"]]
                pinyin_part = ans_text.split(" (")[0]
                hanzi_part = ans_text.split(" (")[1].replace(")", "")
                
                st.markdown(
                    f"""<div style="background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%); border: 2px solid #A7F3D0; border-radius: 12px; padding: 20px; margin-top: 15px;">
<h4 style="color: #065F46; margin-top: 0; margin-bottom: 5px;">🎉 CHÍNH XÁC! LƯỢT ĐỌC TO TRÊN LỚP:</h4>
<div style="font-size: 1.5em; font-weight: bold; color: #047857; margin-bottom: 8px;">👑 Chỉ định học viên đọc: <span style="font-size: 1.25em; color: #065F46; text-decoration: underline;">{target_reader}</span></div>
<hr style="border: 0; border-top: 1px solid #A7F3D0; margin: 10px 0;"/>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 10px;">
    <div style="background: white; border-radius: 8px; padding: 12px; border: 1px solid #A7F3D0;">
        <span style="color:#047857; font-weight:bold; font-size:0.9em; text-transform:uppercase;">🗣️ Học viên A hỏi:</span>
        <div style="font-family: 'Courier New', monospace; font-size: 1.2em; font-weight: bold; color: #1e293b; margin-top: 5px;">{c_data['question_pinyin']}</div>
        <div style="font-size: 1.1em; color: #047857; font-weight: bold; margin-top: 2px;">{c_data['question_hanzi']}</div>
        <div style="color: #64748b; font-size: 0.9em; font-style: italic; margin-top: 2px;">({c_data['question_meaning']})</div>
    </div>
    <div style="background: white; border-radius: 8px; padding: 12px; border: 1px solid #A7F3D0;">
        <span style="color:#047857; font-weight:bold; font-size:0.9em; text-transform:uppercase;">🗣️ Học viên B trả lời:</span>
        <div style="font-family: 'Courier New', monospace; font-size: 1.2em; font-weight: bold; color: #1e293b; margin-top: 5px;">{pinyin_part}</div>
        <div style="font-size: 1.1em; color: #047857; font-weight: bold; margin-top: 2px;">{hanzi_part}</div>
        <div style="color: #64748b; font-size: 0.9em; font-style: italic; margin-top: 2px;">({c_data['choices_meaning'][c_data['answer_idx']]})</div>
    </div>
</div>
<div style="background: rgba(255,255,255,0.7); border-radius: 8px; padding: 10px; margin-top: 10px; border: 1px solid #A7F3D0; font-size: 0.92em; color: #065F46;">
🔍 <b>Trọng tâm phát âm:</b> {c_data['pron_focus']}
</div>
</div>""",
                    unsafe_allow_html=True
                )
                
                st.markdown("<br/>🔊 <b>Hỗ trợ phát âm mẫu cho cặp hội thoại:</b>", unsafe_allow_html=True)
                cols_class_aud = st.columns([1.5, 1.5, 3])
                with cols_class_aud[0]:
                    render_play_button(c_data['question_hanzi'], "🔊 Nghe Câu hỏi", key=f"qa_class_q_play_success_{c_idx}")
                with cols_class_aud[1]:
                    render_play_button(hanzi_part, "🔊 Nghe Câu trả lời", key=f"qa_class_a_play_success_{c_idx}")
                with cols_class_aud[2]:
                    if st.button("🎉 Cộng điểm thưởng cho " + target_reader, key=f"qa_class_reward_{c_idx}"):
                        st.balloons()
                        st.success(f"Cộng 10 điểm thưởng cho bạn **{target_reader}**! 🏆")
            else:
                st.markdown(
                    f"""<div style="background-color: #FEF2F2; border: 2px solid #FCA5A5; border-radius: 12px; padding: 20px; margin-top: 15px; color: #991B1B;">
<h4 style="margin-top: 0; margin-bottom: 5px; color: #991B1B;">❌ CÂU TRẢ LỜI CHƯA CHÍNH XÁC!</h4>
<p style="font-size: 0.95em; margin-bottom: 8px; color: #7F1D1D;">
Học viên hãy xem lại ngữ cảnh câu hỏi hoặc thảo luận nhóm để tìm ra câu trả lời hợp lý.
</p>
<div style="background: white; border-radius: 8px; padding: 12px; border: 1px solid #FCA5A5; font-size: 0.92em; color: #991B1B;">
💡 <b>Gợi ý:</b> {c_data['hint']}
</div>
</div>""",
                    unsafe_allow_html=True
                )

    with tab_dialogues:
        student_list_raw = st.text_input("Danh sách học viên (cách nhau bằng dấu phẩy):", "Tiên, Vy, Trân, Thanh", key="dialogue_students_input")
        students = [s.strip() for s in student_list_raw.split(",") if s.strip()]
        
        st.markdown("---")
        
        st.markdown("#### 💬 Hội thoại 1")
        
        if st.button("🎲 Bốc thăm vai (Hội thoại 1)", key="btn_pick_dlg1"):
            if len(students) >= 3:
                trio = random.sample(students, 3)
                st.success(f"👑 Chỉ định: **{trio[0]}** đóng vai **Học viên A** | **{trio[1]}** đóng vai **Học viên B** | **{trio[2]}** đóng vai **Học viên C**")
            else:
                st.warning("Vui lòng nhập ít nhất 3 học viên để bốc thăm.")
                
        dlg1_lines = [
            ("Học viên A", "#2563eb", "Nǐmen qù hē nǎichá ma?", "你们去喝奶茶吗？", "Các bạn đi uống trà sữa không?"),
            ("Học viên B", "#10b981", "Wǒ bù hē nǎichá, wǒ hē shuǐ. Nǐ qù ma?", "我不喝奶茶，我喝水。你去吗？", "Tớ không uống trà sữa, tớ uống nước. Cậu đi không?"),
            ("Học viên C", "#8b5cf6", "Wǒ qù! Wǒ hěn è. Nǐmen lèi ma?", "我去！我很饿。你们累吗？", "Tớ đi! Tớ rất đói. Các cậu mệt không?"),
            ("Học viên B", "#10b981", "Wǒ bú lèi, wǒ yě è. Wǒmen qù chī jīròu.", "我不累，我也饿。我们去吃鸡肉。", "Tớ không mệt, tớ cũng đói. Chúng ta đi ăn thịt gà."),
            ("Học viên A", "#2563eb", "Nǐmen de péngyou qù ma? Tā ài chī jīròu ma?", "你们的朋友去吗？他爱吃鸡肉吗？", "Bạn của các cậu đi không? Cậu ấy thích ăn thịt gà không?"),
            ("Học viên C", "#8b5cf6", "Tā bú qù, tā hěn lèi. Tā ài chī yúròu, bú ài chī jīròu.", "他不去，他很累。他爱吃鱼肉，不爱吃鸡肉。", "Cậu ấy không đi, cậu ấy rất mệt. Cậu ấy thích ăn thịt cá, không thích ăn thịt gà.")
        ]
        for idx, (speaker, color, pinyin, hanzi, meaning) in enumerate(dlg1_lines):
            col_lbl, col_content, col_audio = st.columns([1.8, 7.2, 1])
            with col_lbl:
                st.markdown(f"<span style='color: {color}; font-weight: bold;'>👤 {speaker}</span>", unsafe_allow_html=True)
            with col_content:
                st.markdown(f"<span style='font-size: 1.1em; font-weight: bold;'>{hanzi}</span> &nbsp;&nbsp; <span style='font-family: monospace; color: #2563eb; font-size: 0.9em; background-color: #eff6ff; padding: 2px 6px; border-radius: 4px;'>{pinyin}</span><br/><span style='color: #64748b; font-style: italic; font-size: 0.9em;'>{meaning}</span>", unsafe_allow_html=True)
            with col_audio:
                render_play_button(hanzi, "🔊", key=f"audio_dlg1_line_{idx}")
                
        st.markdown("---")
        
        # Comparison note between 爱 and 喜欢
        st.markdown(
            """<div style="background-color: #F8FAFC; border-left: 4px solid #3B82F6; padding: 12px 15px; border-radius: 4px; margin-bottom: 15px;">
<b style="color: #1E3A8A;">💡 Phân biệt 爱 (ài) & 喜欢 (xǐhuan):</b>
<table style="width: 100%; border-collapse: collapse; margin-top: 8px; font-size: 0.9em;">
  <tr style="background-color: #EFF6FF; color: #1E3A8A;">
    <th style="border: 1px solid #E2E8F0; padding: 6px; text-align: left;">Từ</th>
    <th style="border: 1px solid #E2E8F0; padding: 6px; text-align: left;">Ý nghĩa</th>
    <th style="border: 1px solid #E2E8F0; padding: 6px; text-align: left;">Mức độ & Cách dùng</th>
  </tr>
  <tr>
    <td style="border: 1px solid #E2E8F0; padding: 6px;"><b>爱 (ài)</b></td>
    <td style="border: 1px solid #E2E8F0; padding: 6px;">Yêu / Rất thích / Hay (làm gì)</td>
    <td style="border: 1px solid #E2E8F0; padding: 6px;">Mức độ tình cảm mạnh mẽ hơn, hoặc chỉ một thói quen/sở thích rất lớn. (Ví dụ: <i>Tā ài wáwa</i> - Cô ấy yêu/rất thích búp bê).</td>
  </tr>
  <tr>
    <td style="border: 1px solid #E2E8F0; padding: 6px;"><b>喜欢 (xǐhuan)</b></td>
    <td style="border: 1px solid #E2E8F0; padding: 6px;">Thích</td>
    <td style="border: 1px solid #E2E8F0; padding: 6px;">Thể hiện sự yêu thích thông thường, nhẹ nhàng hơn. (Ví dụ: <i>Wǒ xǐhuan hē nǎichá</i> - Tôi thích uống trà sữa).</td>
  </tr>
</table>
</div>""",
            unsafe_allow_html=True
        )
        
        st.markdown("#### 💬 Hội thoại 2")
        
        if st.button("🎲 Bốc thăm vai (Hội thoại 2)", key="btn_pick_dlg2"):
            if len(students) >= 3:
                trio = random.sample(students, 3)
                st.success(f"👑 Chỉ định: **{trio[0]}** đóng vai **Học viên A** | **{trio[1]}** đóng vai **Học viên B** | **{trio[2]}** đóng vai **Học viên C**")
            else:
                st.warning("Vui lòng nhập ít nhất 3 học viên để bốc thăm.")
                
        dlg2_lines = [
            ("Học viên A", "#2563eb", "Zhè shì nǐ de wáwa ma?", "这是你的娃娃吗？", "Đây là búp bê của bạn à?"),
            ("Học viên B", "#10b981", "Bú shì, zhè shì wǒ jiějie de wáwa. Tā hěn ài wáwa.", "不是，这是我姐姐的娃娃。她很爱娃娃。", "Không phải, đây là búp bê của chị gái tớ. Chị ấy rất yêu búp bê."),
            ("Học viên C", "#8b5cf6", "Nǐ jiějie shì měinǚ ma?", "你姐姐是美女吗？", "Chị gái cậu là người đẹp phải không?"),
            ("Học viên B", "#10b981", "Shì, tā hěn měi. Tā yě hěn ài zāihuā.", "是，她很美。她也很爱栽花。", "Đúng vậy, chị ấy rất đẹp. Chị ấy cũng rất thích trồng hoa."),
            ("Học viên A", "#2563eb", "Tā ài xué Hànyǔ ma?", "她爱学汉语吗？", "Chị ấy thích học tiếng Trung không?"),
            ("Học viên C", "#8b5cf6", "Tā bù ài xué Hànyǔ, tā ài wáwa.", "她不爱学汉语，她爱娃娃。", "Chị ấy không thích học tiếng Trung, chị ấy thích búp bê."),
            ("Học viên B", "#10b981", "Bú duì, tā ài xué Hànyǔ, yě ài wáwa.", "不对，她爱学汉语，也爱娃娃。", "Không đúng, chị ấy thích học tiếng Trung, cũng thích búp bê.")
        ]
        for idx, (speaker, color, pinyin, hanzi, meaning) in enumerate(dlg2_lines):
            col_lbl, col_content, col_audio = st.columns([1.8, 7.2, 1])
            with col_lbl:
                st.markdown(f"<span style='color: {color}; font-weight: bold;'>👤 {speaker}</span>", unsafe_allow_html=True)
            with col_content:
                st.markdown(f"<span style='font-size: 1.1em; font-weight: bold;'>{hanzi}</span> &nbsp;&nbsp; <span style='font-family: monospace; color: #2563eb; font-size: 0.9em; background-color: #eff6ff; padding: 2px 6px; border-radius: 4px;'>{pinyin}</span><br/><span style='color: #64748b; font-style: italic; font-size: 0.9em;'>{meaning}</span>", unsafe_allow_html=True)
            with col_audio:
                render_play_button(hanzi, "🔊", key=f"audio_dlg2_line_{idx}")
                
        # Comparison note between 美 and 漂亮
        st.markdown(
            """<div style="background-color: #F8FAFC; border-left: 4px solid #10B981; padding: 12px 15px; border-radius: 4px; margin-top: 15px; margin-bottom: 15px;">
<b style="color: #065F46;">💡 Phân biệt 美 (měi) & 漂亮 (piàoliang):</b>
<table style="width: 100%; border-collapse: collapse; margin-top: 8px; font-size: 0.9em;">
  <tr style="background-color: #ECFDF5; color: #065F46;">
    <th style="border: 1px solid #E2E8F0; padding: 6px; text-align: left;">Từ</th>
    <th style="border: 1px solid #E2E8F0; padding: 6px; text-align: left;">Ý nghĩa</th>
    <th style="border: 1px solid #E2E8F0; padding: 6px; text-align: left;">Đặc điểm & Cách dùng</th>
  </tr>
  <tr>
    <td style="border: 1px solid #E2E8F0; padding: 6px;"><b>美 (měi)</b></td>
    <td style="border: 1px solid #E2E8F0; padding: 6px;">Đẹp (trừu tượng/nghệ thuật/vẻ đẹp bên trong)</td>
    <td style="border: 1px solid #E2E8F0; padding: 6px;">Dùng cho cả vẻ đẹp bên trong (tâm hồn, đức hạnh) lẫn phong cảnh, nghệ thuật. Thường mang tính văn chương hơn.</td>
  </tr>
  <tr>
    <td style="border: 1px solid #E2E8F0; padding: 6px;"><b>漂亮 (piàoliang)</b></td>
    <td style="border: 1px solid #E2E8F0; padding: 6px;">Xinh đẹp / Đẹp mắt (bên ngoài)</td>
    <td style="border: 1px solid #E2E8F0; padding: 6px;">Dùng chủ yếu trong khẩu ngữ hàng ngày để tả vẻ đẹp ngoại hình trực quan của người, vật, hay quần áo. Không dùng tả vẻ đẹp tâm hồn. </td>
  </tr>
</table>
</div>""",
            unsafe_allow_html=True
        )
        
        st.markdown("---")
        
        st.markdown("#### 💬 Hội thoại 3")
        
        if st.button("🎲 Bốc thăm vai (Hội thoại 3)", key="btn_pick_dlg3"):
            if len(students) >= 4:
                quad = random.sample(students, 4)
                st.success(f"👑 Chỉ định: **{quad[0]}** đóng vai **Học viên A** | **{quad[1]}** đóng vai **Học viên B** | **{quad[2]}** đóng vai **Học viên C** | **{quad[3]}** đóng vai **Học viên D**")
            else:
                st.warning("Vui lòng nhập ít nhất 4 học viên để bốc thăm.")
                
        dlg3_lines = [
            ("Học viên A", "#2563eb", "Tā gēge shuài ma?", "他哥哥帅吗？", "Anh trai cậu ấy đẹp trai không?"),
            ("Học viên B", "#10b981", "Tā hěn shuài, tā shì shuàigē. Tā ài chī jīròu, yě ài hē nǎichá.", "他很帅，他是帅哥。他爱吃鸡肉，也爱喝奶茶。", "Anh ấy rất đẹp trai, anh ấy là soái ca. Anh ấy thích ăn thịt gà, cũng thích uống trà sữa."),
            ("Học viên C", "#8b5cf6", "Tā ài chī yúròu hé niúròu ma?", "他爱吃鱼肉和牛肉吗？", "Anh ấy thích ăn thịt cá và thịt bò không?"),
            ("Học viên B", "#10b981", "Tā bú ài chī yúròu, tā xǐhuān chī niúròu.", "他不爱吃鱼肉，他喜欢吃牛肉。", "Anh ấy không thích ăn thịt cá, anh ấy thích ăn thịt bò."),
            ("Học viên D", "#f59e0b", "Tā lèi ma? Tā ài xué Hànyǔ ma?", "他累吗？他爱学汉语吗？", "Anh ấy mệt không? Anh ấy thích học tiếng Trung không?"),
            ("Học viên B", "#10b981", "Tā bú lèi, tā hěn ài xué Hànyǔ.", "他不累，他很爱学汉语。", "Anh ấy không mệt, anh ấy rất thích học tiếng Trung."),
            ("Học viên A", "#2563eb", "Wèi, nǐmen è ma?", "喂，你们饿吗？", "Này, các cậu đói không?"),
            ("Học viên B", "#10b981", "Wǒ hěn è, wǒ xiǎng chī jīròu. Wǒmen qù chī ba!", "我很饿，我想吃鸡肉。我们去吃吧！", "Tớ rất đói, tớ muốn ăn thịt gà. Chúng ta đi ăn đi!"),
            ("Học viên C", "#8b5cf6", "Wǒ bù è, wǒ lèi. Wǒ xǐhuān hē nǎichá.", "我不饿，我累。我喜欢喝奶茶。", "Tớ không đói, tớ mệt. Tớ thích uống trà sữa."),
            ("Học viên D", "#f59e0b", "Hǎo! Wǒmen qù hē nǎichá, chī jīròu ba!", "好！我们去喝奶茶，吃鸡肉吧！", "Được! Chúng ta đi uống trà sữa, ăn thịt gà đi!")
        ]
        for idx, (speaker, color, pinyin, hanzi, meaning) in enumerate(dlg3_lines):
            col_lbl, col_content, col_audio = st.columns([1.8, 7.2, 1])
            with col_lbl:
                st.markdown(f"<span style='color: {color}; font-weight: bold;'>👤 {speaker}</span>", unsafe_allow_html=True)
            with col_content:
                st.markdown(f"<span style='font-size: 1.1em; font-weight: bold;'>{hanzi}</span> &nbsp;&nbsp; <span style='font-family: monospace; color: #2563eb; font-size: 0.9em; background-color: #eff6ff; padding: 2px 6px; border-radius: 4px;'>{pinyin}</span><br/><span style='color: #64748b; font-style: italic; font-size: 0.9em;'>{meaning}</span>", unsafe_allow_html=True)
            with col_audio:
                render_play_button(hanzi, "🔊", key=f"audio_dlg3_line_{idx}")
                
        st.markdown("---")
        
    with tab_game:
        # Get student list from the shared input
        students_raw = st.session_state.get("dialogue_students_input", "Tiên, Vy, Trân, Thanh")
        students = [s.strip() for s in students_raw.split(",") if s.strip()]
        
        if not students:
            st.warning("⚠️ Vui lòng nhập danh sách học viên ở tab **Role-Play Dialogues** trước khi chơi.")
        else:
            # Initialize scores in session state
            if "game_scores" not in st.session_state:
                st.session_state.game_scores = {s: 0 for s in students}
            
            # Sync scores with any new students added
            for s in students:
                if s not in st.session_state.game_scores:
                    st.session_state.game_scores[s] = 0
            
            # Leaderboard & Control Panel side-by-side
            col_play, col_scores = st.columns([7, 3])
            
            with col_scores:
                st.markdown("🏆 **BẢNG XẾP HẠNG**")
                # Render beautiful custom scoreboard
                sorted_scores = sorted(st.session_state.game_scores.items(), key=lambda x: x[1], reverse=True)
                for rank, (name, score) in enumerate(sorted_scores, 1):
                    medal = "🥇" if rank == 1 else ("🥈" if rank == 2 else ("🥉" if rank == 3 else "👤"))
                    st.markdown(f"""
                    <div style='background-color: #f1f5f9; border-radius: 8px; padding: 6px 12px; margin-bottom: 6px; display: flex; justify-content: space-between; align-items: center;'>
                        <span style='font-weight: bold; color: #1e293b;'>{medal} {name}</span>
                        <span style='background-color: #3b82f6; color: white; border-radius: 12px; padding: 2px 8px; font-size: 0.85em; font-weight: bold;'>{score}đ</span>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("<br/>", unsafe_allow_html=True)
                if st.button("🔄 Reset điểm số", use_container_width=True, key="reset_game_scores"):
                    st.session_state.game_scores = {s: 0 for s in students}
                    st.toast("Đã đặt lại điểm số!", icon="🔄")
                    st.rerun()
            
            with col_play:
                game_mode = st.radio(
                    "Chọn chế độ chơi:",
                    ["🎯 Vòng xoay Thử thách (Reflex Spin)", "⚔️ Song đấu Phản xạ (Word Duel)"],
                    horizontal=True,
                    key="game_mode_select"
                )
                
                # Game data bank
                GAME_PROMPTS = [
                    {"hanzi": "吃牛肉", "pinyin": "chī niúròu", "vietnamese": "ăn thịt bò"},
                    {"hanzi": "喝奶茶", "pinyin": "hē nǎichá", "vietnamese": "uống trà sữa"},
                    {"hanzi": "不累", "pinyin": "bù lèi", "vietnamese": "không mệt"},
                    {"hanzi": "很饿", "pinyin": "hěn è", "vietnamese": "rất đói"},
                    {"hanzi": "帅哥", "pinyin": "shuàigē", "vietnamese": "soái ca"},
                    {"hanzi": "美女", "pinyin": "měinǚ", "vietnamese": "mỹ nữ"},
                    {"hanzi": "爱吃鱼肉", "pinyin": "ài chī yúròu", "vietnamese": "thích ăn thịt cá"},
                    {"hanzi": "他哥哥", "pinyin": "tā gēge", "vietnamese": "anh trai cậu ấy"},
                    {"hanzi": "去吃鸡肉", "pinyin": "qù chī jīròu", "vietnamese": "đi ăn thịt gà"},
                    {"hanzi": "这个月", "pinyin": "zhè gè yuè", "vietnamese": "tháng này"},
                    {"hanzi": "漂亮", "pinyin": "piàoliang", "vietnamese": "xinh đẹp"},
                    {"hanzi": "爷爷喝水", "pinyin": "yéye hē shuǐ", "vietnamese": "ông nội uống nước"}
                ]
                
                if "Reflex Spin" in game_mode:
                    if "spin_student" not in st.session_state:
                        st.session_state.spin_student = None
                    if "spin_prompt" not in st.session_state:
                        st.session_state.spin_prompt = None
                    if "spin_action" not in st.session_state:
                        st.session_state.spin_action = None
                    
                    if st.button("🎲 QUAY SỐ NGẪU NHIÊN", type="primary", use_container_width=True, key="spin_btn"):
                        st.session_state.spin_student = random.choice(students)
                        st.session_state.spin_prompt = random.choice(GAME_PROMPTS)
                        st.session_state.spin_action = random.choice([
                            "🗣️ Đọc to & Phát âm (Đọc to chữ Hán & Pinyin trên màn hình)",
                            "✍️ Đặt câu nhanh (Đặt 1 câu tiếng Trung có nghĩa chứa từ này)",
                            "🔄 Dịch nhanh (Giáo viên che màn hình, học viên dịch nhanh từ tiếng Việt sang tiếng Trung)"
                        ])
                        st.session_state.reveal_spin_meaning = False
                        st.rerun()
                        
                    if st.session_state.spin_student and st.session_state.spin_prompt:
                        reveal = st.session_state.get("reveal_spin_meaning", False)
                        meaning_text = st.session_state.spin_prompt['vietnamese'] if reveal else "❓ (Bấm nút hiện nghĩa bên dưới để xem)"
                        
                        st.markdown(f"""
                        <div style='background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); color: white; border-radius: 12px; padding: 20px; text-align: center; margin-top: 15px;'>
                            <div style='font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px; opacity: 0.9;'>👤 LƯỢT CHƠI CỦA:</div>
                            <div style='font-size: 2.2em; font-weight: bold; margin-bottom: 15px;'>👑 {st.session_state.spin_student} 👑</div>
                            <hr style='border: 0; border-top: 1px solid rgba(255,255,255,0.2); margin: 10px 0;'/>
                            <div style='font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px; opacity: 0.9;'>📝 TỪ VỰNG THỬ THÁCH:</div>
                            <div style='font-size: 2.5em; font-weight: bold; margin-top: 5px;'>{st.session_state.spin_prompt['hanzi']}</div>
                            <div style='font-family: monospace; font-size: 1.3em; opacity: 0.9;'>{st.session_state.spin_prompt['pinyin']}</div>
                            <div style='font-style: italic; opacity: 0.8;'>Nghĩa: {meaning_text}</div>
                            <hr style='border: 0; border-top: 1px solid rgba(255,255,255,0.2); margin: 15px 0;'/>
                            <div style='font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px; opacity: 0.9;'>⚡ YÊU CẦU:</div>
                            <div style='font-size: 1.25em; font-weight: bold; background: rgba(255,255,255,0.15); border-radius: 8px; padding: 8px 12px; display: inline-block; margin-top: 5px;'>{st.session_state.spin_action}</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.markdown("<br/>", unsafe_allow_html=True)
                        col_btns = st.columns([1.5, 1.5, 1.2])
                        with col_btns[0]:
                            if not reveal:
                                if st.button("👁️ Hiện nghĩa", use_container_width=True, key="spin_reveal"):
                                    st.session_state.reveal_spin_meaning = True
                                    st.rerun()
                            else:
                                if st.button("👁️ Ẩn nghĩa", use_container_width=True, key="spin_hide"):
                                    st.session_state.reveal_spin_meaning = False
                                    st.rerun()
                        with col_btns[1]:
                            if st.button("✅ Đúng (+10đ)", type="primary", use_container_width=True, key="spin_correct"):
                                st.session_state.game_scores[st.session_state.spin_student] += 10
                                st.balloons()
                                st.toast(f"Đã cộng 10 điểm cho {st.session_state.spin_student}!", icon="✅")
                                st.session_state.spin_student = None
                                st.session_state.spin_prompt = None
                                st.session_state.reveal_spin_meaning = False
                                st.rerun()
                        with col_btns[2]:
                            if st.button("❌ Bỏ qua", use_container_width=True, key="spin_incorrect"):
                                st.toast("Lượt chơi đã qua!", icon="ℹ️")
                                st.session_state.spin_student = None
                                st.session_state.spin_prompt = None
                                st.session_state.reveal_spin_meaning = False
                                st.rerun()
                                
                else:
                    if "duel_p1" not in st.session_state:
                        st.session_state.duel_p1 = None
                    if "duel_p2" not in st.session_state:
                        st.session_state.duel_p2 = None
                    if "duel_prompt" not in st.session_state:
                        st.session_state.duel_prompt = None
                    
                    if st.button("⚔️ THIẾT LẬP CẶP ĐẤU", type="primary", use_container_width=True, key="duel_btn"):
                        if len(students) < 2:
                            st.warning("⚠️ Cần ít nhất 2 học viên để tổ chức song đấu.")
                        else:
                            pair = random.sample(students, 2)
                            st.session_state.duel_p1 = pair[0]
                            st.session_state.duel_p2 = pair[1]
                            st.session_state.duel_prompt = random.choice(GAME_PROMPTS)
                            st.rerun()
                            
                    if st.session_state.duel_p1 and st.session_state.duel_p2 and st.session_state.duel_prompt:
                        st.markdown(f"""
                        <div style='background: linear-gradient(135deg, #7f1d1d 0%, #dc2626 100%); color: white; border-radius: 12px; padding: 20px; text-align: center; margin-top: 15px;'>
                            <div style='font-size: 1.8em; font-weight: bold; margin-bottom: 10px;'>⚔️ SONG ĐẤU NẢY LỬA ⚔️</div>
                            <div style='display: flex; justify-content: space-around; align-items: center; margin-bottom: 15px;'>
                                <div style='font-size: 1.5em; font-weight: bold; background: rgba(0,0,0,0.3); padding: 8px 16px; border-radius: 8px;'>🔵 {st.session_state.duel_p1}</div>
                                <div style='font-size: 1.5em; font-weight: bold; font-style: italic; color: #fde047;'>VS</div>
                                <div style='font-size: 1.5em; font-weight: bold; background: rgba(0,0,0,0.3); padding: 8px 16px; border-radius: 8px;'>🔴 {st.session_state.duel_p2}</div>
                            </div>
                            <hr style='border: 0; border-top: 1px solid rgba(255,255,255,0.2); margin: 10px 0;'/>
                            <div style='font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px; opacity: 0.9;'>Nghĩa tiếng Việt cần phản xạ nhanh:</div>
                            <div style='font-size: 2.8em; font-weight: bold; color: #fde047; margin-top: 5px;'>"{st.session_state.duel_prompt['vietnamese']}"</div>
                            <div style='font-size: 0.85em; opacity: 0.7; font-style: italic; margin-top: 5px;'>(Đáp án ẩn: {st.session_state.duel_prompt['hanzi']} - {st.session_state.duel_prompt['pinyin']})</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.markdown("<br/>", unsafe_allow_html=True)
                        col_winners = st.columns(3)
                        with col_winners[0]:
                            if st.button(f"🔵 {st.session_state.duel_p1} thắng (+15đ)", type="primary", use_container_width=True, key="duel_win_p1"):
                                st.session_state.game_scores[st.session_state.duel_p1] += 15
                                st.balloons()
                                st.toast(f"Chúc mừng {st.session_state.duel_p1} thắng!", icon="🏆")
                                st.session_state.duel_p1 = None
                                st.session_state.duel_p2 = None
                                st.session_state.duel_prompt = None
                                st.rerun()
                        with col_winners[1]:
                            if st.button(f"🔴 {st.session_state.duel_p2} thắng (+15đ)", type="primary", use_container_width=True, key="duel_win_p2"):
                                st.session_state.game_scores[st.session_state.duel_p2] += 15
                                st.balloons()
                                st.toast(f"Chúc mừng {st.session_state.duel_p2} thắng!", icon="🏆")
                                st.session_state.duel_p1 = None
                                st.session_state.duel_p2 = None
                                st.session_state.duel_prompt = None
                                st.rerun()
                        with col_winners[2]:
                            if st.button("🤝 Hòa / Đổi lượt đấu", use_container_width=True, key="duel_tie"):
                                st.toast("Lượt đấu hòa!", icon="🤝")
                                st.session_state.duel_p1 = None
                                st.session_state.duel_p2 = None
                                st.session_state.duel_prompt = None
                                st.rerun()
        st.markdown("---")
        
def show_lesson4_exercises(save_progress, save_score_row_b4=None, load_all_scores_b4=None):
    st.header("🎯 Bài 4: Luyện tập Vận mẫu kép mở rộng")
   
    
    st.markdown(
        """
        <style>
        .challenge-container {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 25px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.025);
        }
        .challenge-header {
            font-size: 1.25rem;
            font-weight: 700;
            color: #1e293b;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .puzzle-card {
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            border: 2px dashed #cbd5e1;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            margin-bottom: 20px;
        }
        .spelling-box {
            font-family: 'Courier New', monospace;
            font-size: 2.2rem;
            font-weight: bold;
            color: #2563eb;
            background: white;
            border: 1px solid #e2e8f0;
            padding: 10px 20px;
            border-radius: 8px;
            display: inline-block;
            margin: 10px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    tab_challenge1, tab_challenge2, tab_challenge3 = st.tabs([
        "🎧 1. Listening", 
        "✍️ 2. Spelling", 
        "🧩 3. Pinyin Quiz"
    ])
    
    # ------------------ CHALLENGE 1: LISTENING ------------------
    with tab_challenge1:
        st.markdown(
            """
            <div class="challenge-header">🎧 Thử thách: Đôi tai vàng</div>
            <p style='color: #475569;'>Bấm nút loa để nghe phát âm từ người bản xứ và chọn đáp án Bính âm tương ứng chính xác nhất.</p>
            """, 
            unsafe_allow_html=True
        )
        
        LISTENING_CHALLENGES = [
            {"audio": "huā", "choices": ["huā", "huō", "hāu", "huāi"], "answer": "huā", "tip": "Thanh mẫu 'h' + Vận mẫu kép 'ua' + Thanh 1."},
            {"audio": "liù", "choices": ["lù", "liò", "liù", "loù"], "answer": "liù", "tip": "Thanh mẫu 'l' + Vận mẫu 'iou' viết gọn thành 'iu' + Thanh 4."},
            {"audio": "yuè", "choices": ["yüè", "yuè", "iè", "yě"], "answer": "yuè", "tip": "Vận mẫu 'üe' khi đứng độc lập đổi 'ü' thành 'y' và bỏ dấu hai chấm, thêm thanh 4."},
            {"audio": "shuǐ", "choices": ["shǔi", "shuǐ", "sheǐ", "shueǐ"], "answer": "shuǐ", "tip": "Thanh mẫu 'sh' + Vận mẫu 'uei' viết gọn thành 'ui' + Thanh 3. Dấu thanh điệu đặt trên nguyên âm chính 'i'."},
            {"audio": "wǒ", "choices": ["wǒ", "uǒ", "oǔ", "yǒ"], "answer": "wǒ", "tip": "Vận mẫu 'uo' đứng độc lập đổi 'u' thành 'w' + Thanh 3."}
        ]
        
        listen_submitted_key = "b4_listen_quiz_submitted"
        if listen_submitted_key not in st.session_state:
            st.session_state[listen_submitted_key] = False
            
        listen_score = 0
        total_listen = len(LISTENING_CHALLENGES)
        
        for idx, item in enumerate(LISTENING_CHALLENGES):
            st.markdown(f"**Câu hỏi {idx + 1}:** Nghe và chọn từ đúng")
            cols_listen = st.columns([1.5, 4.5])
            with cols_listen[0]:
                render_play_button(item["audio"], "🔊 Nghe âm thanh", key=f"btn_listen_q_{idx}")
            with cols_listen[1]:
                selected_listen = st.radio(
                    f"Đáp án cho câu hỏi {idx + 1}:",
                    item["choices"],
                    index=0,
                    key=f"b4_listen_q_radio_{idx}",
                    disabled=st.session_state[listen_submitted_key],
                    label_visibility="collapsed"
                )
                
            if selected_listen == item["answer"]:
                listen_score += 1
                
            if st.session_state[listen_submitted_key]:
                if selected_listen == item["answer"]:
                    st.success(f"✅ Chính xác: **{item['answer']}**")
                else:
                    st.error(f"❌ Chưa đúng! Đáp án đúng: **{item['answer']}**")
                st.info(f"💡 **Mẹo:** {item['tip']}")
            st.markdown("---")
            
        if not st.session_state[listen_submitted_key]:
            if st.button("📝 Chấm điểm phần Luyện Nghe", type="primary", use_container_width=True, key="btn_score_listen"):
                st.session_state[listen_submitted_key] = True
                st.session_state.scores["b4_listening"] = (listen_score, total_listen)
                save_progress()
                st.rerun()
        else:
            st.markdown(f"### Kết quả luyện nghe: **{listen_score} / {total_listen}**")
            if listen_score == total_listen:
                st.balloons()
            if st.button("🔄 Làm lại phần Luyện Nghe", use_container_width=True, key="btn_reset_listen"):
                st.session_state[listen_submitted_key] = False
                if "b4_listening" in st.session_state.scores:
                    del st.session_state.scores["b4_listening"]
                save_progress()
                st.rerun()

    # ------------------ CHALLENGE 2: SPELLING ------------------
    with tab_challenge2:
        st.markdown(
            """
            <div class="challenge-header">✍️ Thử thách: Chiến binh Chính tả</div>
            <p style='color: #475569;'>Áp dụng 3 quy tắc chính tả Pinyin viết gọn và biến đổi âm đệm để chọn cách viết chính xác.</p>
            """, 
            unsafe_allow_html=True
        )
        
        SPELLING_CHALLENGES = [
            {
                "q": "Khi không có thanh mẫu đứng trước, vận mẫu 'ui' (gốc là 'uei') được viết đầy đủ chính tả là gì?",
                "choices": ["ui", "wei", "yui", "uei"],
                "answer": "wei",
                "explain": "Quy tắc 1: Khi đứng độc lập không có thanh mẫu, 'uei' viết đầy đủ là 'wei'."
            },
            {
                "q": "Kết quả ghép âm chính tả của thanh mẫu 'q' + vận mẫu 'üe' + thanh 2 (sắc) là gì?",
                "choices": ["qüé", "qué", "qié", "qüé"],
                "answer": "qué",
                "explain": "Quy tắc 3: Nhóm thanh mẫu mặt lưỡi 'j, q, x' khi đi với 'üe' phải lược bỏ dấu hai chấm trên đầu, chỉ viết là 'ue' (đọc vẫn tròn môi)."
            },
            {
                "q": "Kết quả ghép âm chính tả của thanh mẫu 'l' + vận mẫu 'üe' + thanh 4 (nặng) là gì?",
                "choices": ["lùe", "lüè", "luè", "lyuè"],
                "answer": "lüè",
                "explain": "Quy tắc 3 lưu ý: Đối với 'n' và 'l', khi đi với 'üe' BẮT BUỘC phải giữ nguyên dấu 2 chấm để phân biệt (nếu không sẽ bị nhầm với 'u')."
            },
            {
                "q": "Cách viết chính tả bính âm của âm tiết ghép bởi thanh mẫu 'd' + vận mẫu 'iou' + thanh 4 là gì?",
                "choices": ["diou4", "diù", "diò", "doù"],
                "answer": "diù",
                "explain": "Quy tắc 1: 'iou' khi đi sau thanh mẫu viết rút gọn thành 'iu'. Dấu thanh điệu đặt trên chữ cái sau cùng 'u'."
            }
        ]
        
        spell_submitted_key = "b4_spell_quiz_submitted"
        if spell_submitted_key not in st.session_state:
            st.session_state[spell_submitted_key] = False
            
        spell_score = 0
        total_spell = len(SPELLING_CHALLENGES)
        
        for idx, item in enumerate(SPELLING_CHALLENGES):
            st.markdown(f"**Câu hỏi {idx + 1}:** {item['q']}")
            selected_spell = st.radio(
                f"Đáp án cho câu hỏi chính tả {idx + 1}:",
                item["choices"],
                index=0,
                key=f"b4_spell_q_radio_{idx}",
                disabled=st.session_state[spell_submitted_key],
                label_visibility="collapsed"
            )
            
            if selected_spell == item["answer"]:
                spell_score += 1
                
            if st.session_state[spell_submitted_key]:
                if selected_spell == item["answer"]:
                    st.success(f"✅ Chính xác: **{item['answer']}**")
                else:
                    st.error(f"❌ Chưa đúng! Đáp án đúng: **{item['answer']}**")
                st.info(f"💡 **Giải thích:** {item['explain']}")
            st.markdown("---")
            
        if not st.session_state[spell_submitted_key]:
            if st.button("📝 Chấm điểm phần Chính tả", type="primary", use_container_width=True, key="btn_score_spell"):
                st.session_state[spell_submitted_key] = True
                st.session_state.scores["b4_spelling"] = (spell_score, total_spell)
                save_progress()
                st.rerun()
        else:
            st.markdown(f"### Kết quả phần chính tả: **{spell_score} / {total_spell}**")
            if spell_score == total_spell:
                st.balloons()
            if st.button("🔄 Làm lại phần Chính tả", use_container_width=True, key="btn_reset_spell"):
                st.session_state[spell_submitted_key] = False
                if "b4_spelling" in st.session_state.scores:
                    del st.session_state.scores["b4_spelling"]
                save_progress()
                st.rerun()

    # ------------------ CHALLENGE 3: QA PUZZLE (HỎI ĐÁP BÍNH ÂM) ------------------
    with tab_challenge3:
        st.markdown(
            """
            <style>
            .puzzle-goal-card {
                background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
                border: 2px dashed #cbd5e1;
                border-radius: 16px;
                padding: 24px;
                text-align: center;
                margin-bottom: 20px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02);
            }
            </style>
            <div class="challenge-header">🧩 Thử thách: Pinyin Quiz</div>
            <p style='color: #475569;'>Quan sát nghĩa của từ, nghe phát âm và chọn đáp án Bính âm (Pinyin) đúng quy tắc chính tả nhất.</p>
            """, 
            unsafe_allow_html=True
        )
        
        QA_TARGETS = [
            {
                "meaning": "A Trân thích uống trà sữa",
                "audio": "阿珍喜欢喝奶茶",
                "image": "naichá.png",
                "emoji": "🥤",
                "question": "Chọn cách viết Bính âm (Pinyin) chuẩn xác nhất cho câu: \"阿珍喜欢喝奶茶\"",
                "choices": ["A. Āzhēn xǐhuan hē nǎichá", "B. Āzhēn xǐhuān hē nǎicá", "C. Āzhēn xǐhuān hē lǎichá", "D. Āzhēn xǐhuan hē nǎishá"],
                "answer": "A. Āzhēn xǐhuan hē nǎichá",
                "explain": "Chú ý phụ âm đầu n- và l- trong 'nǎi', âm đầu ch- trong 'chá', và thanh điệu chính xác của các từ."
            },
            {
                "meaning": "Thầy giáo không có bạn gái",
                "audio": "老师没有女朋友",
                "image": "nǚpéngyou.png",
                "emoji": "👩‍❤️‍👨",
                "question": "Chọn cách viết Bính âm (Pinyin) chuẩn xác nhất cho câu: \"老师没有女朋友\"",
                "choices": ["A. Lǎoshī méiyǒu nǚpényou", "B. Lǎoshī méiyǒu nǔpéngyou", "C. Lǎoshī méiyǒu nǚpénggǒu", "D. Lǎoshī méiyǒu nǚpéngyou"],
                "answer": "D. Lǎoshī méiyǒu nǚpéngyou",
                "explain": "Chú ý nguyên âm 'ü' trong từ 'nǚ' (phải giữ nguyên dấu hai chấm khi kết hợp với n-), và vận mẫu 'eng' trong 'péng'."
            },
            {
                "meaning": "Chị Vy là một người phụ nữ đẹp",
                "audio": "薇姐是一个漂亮女人",
                "image": "piàoliang.png",
                "emoji": "💃",
                "question": "Chọn cách viết Bính âm (Pinyin) chuẩn xác nhất cho câu: \"薇姐是一个漂亮女人\"",
                "choices": ["A. Wēijiě shì yíge piàolang nǚrén", "B. Wēijiě shì yíge piàoliang nǚrén", "C. Wēijiě shì yíge piàoliang nǔrén", "D. Wēijiě shì yíge piāoliang nǚrén"],
                "answer": "B. Wēijiě shì yíge piàoliang nǚrén",
                "explain": "Chú ý vận mẫu 'iao' trong 'piào' và nguyên âm 'ü' trong 'nǚ' (phải giữ nguyên dấu hai chấm khi kết hợp với n-)."
            },
            {
                "meaning": "A Thanh là một luật sư tập sự",
                "audio": "阿青是一个实习律师",
                "image": "lǜshī.png",
                "emoji": "⚖️",
                "question": "Chọn cách viết Bính âm (Pinyin) chuẩn xác nhất cho câu: \"阿青是一个实习律师\"",
                "choices": ["A. Āqīng shì yíge shíxí lǜshī", "B. Āqīng shì yíge shíxí lùshī", "C. Āqīng shì yíge shíxí lüshī", "D. Āqǐng shì yíge shíxí lǜshī"],
                "answer": "A. Āqīng shì yíge shíxí lǜshī",
                "explain": "Chú ý âm đầu 'q' trong 'qīng' và nguyên âm 'ü' có dấu thanh điệu 'ǜ' trong 'lǜ' (phải giữ nguyên dấu hai chấm khi kết hợp với l-)."
            }
        ]
        
        if "assembly_idx" not in st.session_state:
            st.session_state.assembly_idx = 0
        if "assembly_answers" not in st.session_state or not isinstance(st.session_state.assembly_answers, dict):
            st.session_state.assembly_answers = {}
        if "assembly_checked" not in st.session_state or not isinstance(st.session_state.assembly_checked, dict):
            st.session_state.assembly_checked = {}
            
        cur_idx = st.session_state.assembly_idx
        
        if cur_idx >= len(QA_TARGETS):
            # Calculate and save score
            correct_count = sum(1 for i, q in enumerate(QA_TARGETS) if st.session_state.assembly_answers.get(i) == q["answer"])
            st.session_state.scores["b4_assembly"] = (correct_count, len(QA_TARGETS))
            save_progress()
            
            st.markdown(
                f"""
                <div style="background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%); border: 1px solid #A7F3D0; border-radius: 12px; padding: 22px; text-align: center;">
                    <span style="font-size: 2.5em;">🏆</span>
                    <h3 style="color: #065F46; margin-top: 5px;">Chúc mừng bạn đã hoàn thành Thử thách Pinyin Quiz!</h3>
                    <p style="color: #047857; font-size: 1.1em; margin-bottom: 5px;">Kết quả đạt được: <b>{correct_count} / {len(QA_TARGETS)}</b> câu đúng</p>
                    <p style="color: #047857; margin-bottom: 15px;">Bạn đã làm chủ hoàn toàn các quy luật chính tả Pinyin rút gọn/biến đổi!</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button("🔄 Làm lại phần Hỏi đáp từ đầu", use_container_width=True, key="reset_qa_final_btn"):
                st.session_state.assembly_idx = 0
                st.session_state.assembly_answers = {}
                st.session_state.assembly_checked = {}
                if "b4_assembly" in st.session_state.scores:
                    del st.session_state.scores["b4_assembly"]
                save_progress()
                st.rerun()
        else:
            item = QA_TARGETS[cur_idx]
            
            img_base64 = ""
            if "image" in item:
                img_path = os.path.join("assets", "lesson4", item["image"])
                if os.path.exists(img_path):
                    with open(img_path, "rb") as f:
                        img_base64 = f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

            if img_base64:
                img_html = f'<div style="margin: 10px 0;"><img src="{img_base64}" style="width: 120px; height: 120px; border-radius: 16px; border: 1px solid #e2e8f0; object-fit: cover; background: white; padding: 5px; box-shadow: 0 4px 12px rgba(0,0,0,0.06);"/></div>'
            else:
                img_html = f'<div style="margin: 10px 0; font-size: 3.5rem; background: white; width: 120px; height: 120px; display: inline-flex; align-items: center; justify-content: center; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,0.06);">{item["emoji"]}</div>'

            st.markdown(
                f"""
                <div class="puzzle-goal-card">
                    <span style="font-size: 0.9em; color: #64748b; font-weight: bold; text-transform: uppercase; letter-spacing: 0.5px;">CÂU HỎI ({cur_idx + 1}/{len(QA_TARGETS)}):</span>
                    <br/>
                    {img_html}
                    <h3 style="color: #0f172a; margin: 10px 0 5px 0;">Nghĩa: "{item['meaning']}"</h3>
                    <p style="color: #475569; font-size: 1rem; font-weight: 500; margin-bottom: 0;">{item['question']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Speaker button
            cols_aud = st.columns([1.5, 3, 1.5])
            with cols_aud[1]:
                render_play_button(item["audio"], "🔊 Nghe phát âm từ khóa", key=f"qa_play_target_{cur_idx}", type="secondary")
                
            st.markdown("<hr style='margin: 15px 0; border: 0; border-top: 1px solid #e2e8f0;'/>", unsafe_allow_html=True)
            
            # --- Choices Selector ---
            is_checked = st.session_state.assembly_checked.get(cur_idx, False)
            selected_choice = st.session_state.assembly_answers.get(cur_idx, None)
            
            st.markdown("#### 👇 Chọn đáp án của bạn:")
            cols_choice = st.columns(2)
            for idx, choice in enumerate(item["choices"]):
                col_to_use = cols_choice[idx % 2]
                with col_to_use:
                    is_sel = (selected_choice == choice)
                    btn_label = choice
                    btn_type = "secondary"
                    
                    if is_checked:
                        if choice == item["answer"]:
                            btn_label = f"✅ {choice} (Đúng)"
                            btn_type = "primary"
                        elif is_sel:
                            btn_label = f"❌ {choice} (Bạn chọn)"
                            btn_type = "primary"
                    else:
                        if is_sel:
                            btn_label = f"👉 {choice}"
                            btn_type = "primary"
                            
                    if st.button(
                        btn_label,
                        key=f"qa_btn_{cur_idx}_{idx}",
                        type=btn_type,
                        use_container_width=True,
                        disabled=is_checked
                    ):
                        st.session_state.assembly_answers[cur_idx] = choice
                        st.rerun()

            # --- Feedback messaging ---
            if is_checked:
                is_correct = (selected_choice == item["answer"])
                if is_correct:
                    st.markdown(
                        f"""<div style="background-color: #ECFDF5; border: 2px solid #A7F3D0; border-radius: 10px; padding: 15px; margin-top: 15px; color: #065F46;">
                            <b>🎉 CHÍNH XÁC!</b> Bạn đã chọn đúng đáp án: <b>{selected_choice}</b>
                        </div>""",
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"""<div style="background-color: #FEF2F2; border: 2px solid #FCA5A5; border-radius: 10px; padding: 15px; margin-top: 15px; color: #991B1B;">
                            <b>❌ CHƯA CHÍNH XÁC!</b> Bạn chọn: <i>{selected_choice}</i>. Đáp án đúng là: <b>{item['answer']}</b>
                        </div>""",
                        unsafe_allow_html=True
                    )
                
                st.markdown(
                    f"""<div style="background-color: #EFF6FF; border-left: 6px solid #3B82F6; border-radius: 10px; padding: 15px; margin-top: 10px;">
                        <b style="color: #1E40AF;">💡 Giải thích chính tả:</b><br/>
                        <span style="color: #1E3A8A; font-size: 0.95em;">{item['explain']}</span>
                    </div>""",
                    unsafe_allow_html=True
                )
                
            # --- Action buttons ---
            st.markdown("<br/>", unsafe_allow_html=True)
            col_acts = st.columns(2)
            
            with col_acts[0]:
                check_disabled = is_checked or (selected_choice is None)
                if st.button("🚀 Xác nhận đáp án", type="primary", use_container_width=True, key=f"qa_check_btn_{cur_idx}", disabled=check_disabled):
                    st.session_state.assembly_checked[cur_idx] = True
                    is_correct = (selected_choice == item["answer"])
                    if is_correct:
                        st.toast("🎉 Chính xác!", icon="✅")
                    else:
                        st.toast("❌ Chưa đúng rồi!", icon="❌")
                    st.rerun()
                    
            with col_acts[1]:
                next_disabled = not is_checked
                btn_label = "Xem kết quả chung cuộc 📊" if cur_idx == len(QA_TARGETS) - 1 else "⏭️ Câu tiếp theo"
                if st.button(btn_label, use_container_width=True, key=f"qa_next_btn_{cur_idx}", disabled=next_disabled):
                    st.session_state.assembly_idx = cur_idx + 1
                    st.rerun()


    # Tổng kết — chỉ hiện khi học viên đã chấm đủ các bài tập
    st.markdown("---")
    with st.expander("📊 Lịch sử & Tổng kết Bài 4", expanded=True):
        from datetime import datetime, timezone, timedelta
        cur = st.session_state.scores
        labels_b4 = {
            "b4_listening": "BT1: Luyện nghe", 
            "b4_spelling": "BT2: Chính tả", 
            "b4_assembly": "BT3: Pinyin Quiz"
        }
        missing_b4 = [v for k, v in labels_b4.items() if k not in cur]

        if missing_b4:
            st.warning(f"Chưa chấm điểm đủ bài tập. Các bài còn thiếu: {', '.join(missing_b4)}")
        else:
            b4_earned = sum(cur[k][0] for k in labels_b4.keys())
            b4_total  = sum(cur[k][1] for k in labels_b4.keys())
            b4_score_10 = round((b4_earned / b4_total) * 10, 2)
            st.success(f"📈 Điểm số tổng quát Bài 4: **{b4_score_10} / 10** điểm")
            for k, lbl in labels_b4.items():
                s = cur[k]
                st.write(f"- {lbl}: Đúng **{s[0]}/{s[1]}** câu")

            st.markdown("---")
            name = st.text_input("Tên học viên (Bài 4)", key="student_name_b4")
            if st.button("Nộp bài tập Bài 4"):
                if name:
                    def fmt(k):
                        s = cur.get(k)
                        return f"{s[0]}/{s[1]}" if s else ""
                    
                    row = {
                        "thời gian": datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S"), 
                        "học viên": name,
                        "tổng điểm": b4_score_10, 
                        "BT1: Luyện nghe": fmt("b4_listening"),
                        "BT2: Chính tả": fmt("b4_spelling"),
                        "BT3: Pinyin Quiz": fmt("b4_assembly")
                    }
                    if save_score_row_b4 and save_score_row_b4(row):
                        st.success("Đã lưu điểm Bài 4 thành công!")
                        # Clean up session state scores for Lesson 4
                        for k in labels_b4.keys():
                            if k in st.session_state.scores:
                                del st.session_state.scores[k]
                        if "assembly_idx" in st.session_state:
                            st.session_state.assembly_idx = 0
                        save_progress()
                        st.rerun()
                else:
                    st.error("Vui lòng nhập tên học viên để lưu điểm!")

        st.write("### 🏆 Bảng điểm học viên đã nộp:")
        if load_all_scores_b4:
            all_s4 = load_all_scores_b4()
            if all_s4: 
                st.dataframe(all_s4, use_container_width=True)

def show_lesson4_hanzi():
    render_lesson_intro("📚 Bài 5: Nét chữ Hán cơ bản", "Rèn nét cơ bản và quy tắc thứ tự nét.")
    st.table(NET_CO_BAN)

def show_lesson4_female_comparison(save_progress):
    render_lesson_intro(
        "📚 Bài 4: Phân biệt từ vựng chỉ Nữ giới", 
        "Học cách phân biệt 7 từ vựng chỉ nữ giới phổ biến dựa trên độ tuổi, sắc thái biểu đạt và văn cảnh giao tiếp."
    )
    
    st.markdown(
        """
        <style>
        .custom-card {
            border-radius: 12px; 
            padding: 20px; 
            margin-bottom: 18px; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.05); 
            border: 1px solid #e2e8f0; 
            transition: all 0.3s ease;
        }
        .custom-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.08);
        }
        .star-active { color: #eab308; font-size: 1.1em; }
        .star-inactive { color: #cbd5e1; font-size: 1.1em; }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.write(
        "Trong tiếng Trung, có rất nhiều từ mang ý nghĩa 'phụ nữ, con gái, nữ giới'. Tuy nhiên, mỗi từ lại có một sắc thái biểu cảm, độ trang trọng và phạm vi sử dụng hoàn toàn khác nhau. Hãy cùng khám phá bí quyết phân biệt cực kỳ trực quan và dễ nhớ dưới đây nhé!"
    )
    
    # Sơ đồ trục tuổi tác trực quan
    st.markdown("#### ⏳ Sơ đồ độ tuổi tâm lý sử dụng trong giao tiếp:")
    st.markdown(
        """
        <div style="display: flex; gap: 8px; margin: 15px 0 25px 0; align-items: center; justify-content: center; flex-wrap: wrap; background-color: #f8fafc; padding: 15px; border-radius: 10px; border: 1px dashed #cbd5e1;">
            <span style="background: #EC4899; color: white; padding: 6px 14px; border-radius: 20px; font-weight: bold; font-size: 0.9em; box-shadow: 0 2px 5px rgba(236,72,153,0.2);">女孩 (Dưới 20 tuổi)</span>
            <span style="font-weight: bold; color: #94a3b8;">➔</span>
            <span style="background: #3B82F6; color: white; padding: 6px 14px; border-radius: 20px; font-weight: bold; font-size: 0.9em; box-shadow: 0 2px 5px rgba(59,130,246,0.2);">女生 (12 - 30 tuổi)</span>
            <span style="font-weight: bold; color: #94a3b8;">➔</span>
            <span style="background: #F43F5E; color: white; padding: 6px 14px; border-radius: 20px; font-weight: bold; font-size: 0.9em; box-shadow: 0 2px 5px rgba(244,63,94,0.2);">女人 (Trên 18 tuổi)</span>
            <span style="font-weight: bold; color: #94a3b8;">➔</span>
            <span style="background: #D97706; color: white; padding: 6px 14px; border-radius: 20px; font-weight: bold; font-size: 0.9em; box-shadow: 0 2px 5px rgba(217,119,6,0.2);">妇女 (Trung niên / Có gia đình)</span>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.subheader("1. Chi tiết 7 từ vựng chỉ Nữ giới phổ biến nhất")
    
    # Hiển thị từng thẻ từ vựng kèm theo nút nghe phát âm
    for idx, w in enumerate(FEMALE_VOCAB_COMPARISON_DATA):
        stars_html = "".join([f'<span class="star-active">★</span>' for _ in range(w['formality'])]) + "".join([f'<span class="star-inactive">☆</span>' for _ in range(5 - w['formality'])])
        
        card_html = f"""
        <div class="custom-card" style="background: {w['color']}; border-left: 6px solid {w['border_color']};">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-size: 1.7em; font-weight: bold; color: {w['text_color']};">{w['word']}</span>
                <span style="background: white; border: 1px solid {w['border_color']}; color: {w['text_color']}; padding: 3px 10px; border-radius: 20px; font-size: 0.9em; font-weight: bold; font-family: 'Courier New', monospace;">{w['pinyin']}</span>
            </div>
            <div style="font-size: 1.1em; font-weight: bold; margin-bottom: 12px; color: #0f172a;">Nghĩa: {w['vietnamese']}</div>
            <p style="color: #334155; font-size: 0.95em; line-height: 1.5; margin-bottom: 14px;">{w['explanation']}</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; font-size: 0.88em; border-top: 1px dashed #cbd5e1; padding-top: 12px; margin-bottom: 14px; color: #475569;">
                <div><b>Trái nghĩa:</b> <span style="color:#0f172a; font-weight: 500;">{w['antonym']}</span></div>
                <div><b>Độ tuổi:</b> <span style="color:#0f172a; font-weight: 500;">{w['age']}</span></div>
                <div><b>Văn cảnh:</b> <span style="color:#0f172a; font-weight: 500;">{w['context']}</span></div>
                <div><b>Độ trang trọng:</b> {stars_html}</div>
            </div>
            <div style="background: rgba(255,255,255,0.85); border-radius: 8px; padding: 12px; border: 1px solid #e2e8f0;">
                <div style="font-size: 0.8em; color: #64748b; font-weight: bold; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px;">Ví dụ thực tế:</div>
                <div style="font-size: 1.25em; font-weight: bold; color: #0f172a; margin-bottom: 2px;">{w['example_han']}</div>
                <div style="font-family: 'Courier New', monospace; font-weight: bold; color: #2563eb; font-size: 1em; margin-bottom: 4px;">{w['example_py']}</div>
                <div style="color: #475569; font-style: italic; font-size: 0.92em; border-left: 2px solid #cbd5e1; padding-left: 6px;">{w['example_vi']}</div>
            </div>
        </div>
        """
        
        cols = st.columns([5, 1])
        with cols[0]:
            st.markdown(card_html, unsafe_allow_html=True)
        with cols[1]:
            st.markdown("<br/>", unsafe_allow_html=True)
            render_play_button(w['word'], "🔊 Phát âm từ", key=f"btn_word_{w['word']}_{idx}")
            render_play_button(w['example_han'], "🔊 Nghe ví dụ", key=f"btn_ex_{w['word']}_{idx}")
            st.caption("<div style='text-align: center; color: #94a3b8; font-size:0.8em;'>Bấm để nghe giọng Bắc Kinh chuẩn</div>", unsafe_allow_html=True)
            
    st.markdown("---")
    st.subheader("2. Bảng đối chiếu nhanh (Cheat Sheet)")
    
    st.markdown(
        """
        <table class="chinese-table" style="width:100%;">
            <thead>
                <tr class="tm-header">
                    <th style="padding: 12px; text-align:center;">Từ vựng</th>
                    <th style="text-align:center;">Phiên âm</th>
                    <th>Nghĩa chính</th>
                    <th>Độ tuổi thích hợp</th>
                    <th>Văn cảnh sử dụng</th>
                    <th style="text-align:center;">Độ trang trọng</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="text-align:center; font-size:1.15em;"><b>女人</b></td>
                    <td class="pinyin-text" style="text-align:center; color:#2563eb;">nǚrén</td>
                    <td>Phụ nữ / Đàn bà nói chung</td>
                    <td>Trên 18 tuổi</td>
                    <td>Giao tiếp, đời sống hàng ngày</td>
                    <td style="text-align:center; color:#eab308;">⭐⭐☆☆☆</td>
                </tr>
                <tr>
                    <td style="text-align:center; font-size:1.15em;"><b>女孩</b></td>
                    <td class="pinyin-text" style="text-align:center; color:#2563eb;">nǚhái</td>
                    <td>Cô bé / Con gái / Thiếu nữ</td>
                    <td>Dưới 20 tuổi</td>
                    <td>Khẩu ngữ thân mật, gần gũi</td>
                    <td style="text-align:center; color:#eab308;">⭐⭐☆☆☆</td>
                </tr>
                <tr>
                    <td style="text-align:center; font-size:1.15em;"><b>女儿</b></td>
                    <td class="pinyin-text" style="text-align:center; color:#2563eb;">nǚ'ér</td>
                    <td>Con gái ruột (bố mẹ)</td>
                    <td>Mọi lứa tuổi</td>
                    <td>Trong mối quan hệ gia đình</td>
                    <td style="text-align:center; color:#eab308;">⭐⭐⭐☆☆</td>
                </tr>
                <tr>
                    <td style="text-align:center; font-size:1.15em;"><b>女生</b></td>
                    <td class="pinyin-text" style="text-align:center; color:#2563eb;">nǚshēng</td>
                    <td>Nữ sinh / Bạn nữ trẻ</td>
                    <td>12 - 30 tuổi</td>
                    <td>Học đường, giới trẻ hiện đại</td>
                    <td style="text-align:center; color:#eab308;">⭐⭐☆☆☆</td>
                </tr>
                <tr>
                    <td style="text-align:center; font-size:1.15em;"><b>女性</b></td>
                    <td class="pinyin-text" style="text-align:center; color:#2563eb;">nǚxìng</td>
                    <td>Nữ giới / Phái nữ</td>
                    <td>Mọi lứa tuổi</td>
                    <td>Văn bản chính thức, khoa học, y tế</td>
                    <td style="text-align:center; color:#eab308;">⭐⭐⭐⭐⭐</td>
                </tr>
                <tr>
                    <td style="text-align:center; font-size:1.15em;"><b>女子</b></td>
                    <td class="pinyin-text" style="text-align:center; color:#2563eb;">nǚzǐ</td>
                    <td>Nữ / Nữ tử (trang trọng)</td>
                    <td>Mọi lứa tuổi</td>
                    <td>Thể thao, tiêu đề chính thức, văn viết</td>
                    <td style="text-align:center; color:#eab308;">⭐⭐⭐⭐☆</td>
                </tr>
                <tr>
                    <td style="text-align:center; font-size:1.15em;"><b>妇女</b></td>
                    <td class="pinyin-text" style="text-align:center; color:#2563eb;">fùnǚ</td>
                    <td>Phụ nữ trưởng thành / Có gia đình</td>
                    <td>Trên 25-30 tuổi</td>
                    <td>Pháp luật, chính trị, ngày kỷ niệm</td>
                    <td style="text-align:center; color:#eab308;">⭐⭐⭐⭐☆</td>
                </tr>
            </tbody>
        </table>
        """, 
        unsafe_allow_html=True
    )
    
    st.markdown("<br/>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%); border-left: 6px solid #2563EB; border-radius: 12px; padding: 18px; margin: 15px 0; border: 1px solid #BFDBFE;">
            <h4 style="color: #1E40AF; margin-top: 0; margin-bottom: 10px; font-weight: bold;">💡 Ngữ pháp & Từ loại cần nhớ:</h4>
            <p style="color: #1E3A8A; font-size: 1em; line-height: 1.6; margin-bottom: 12px;">
                Tất cả 7 từ vựng trên đều là <b>Danh từ (名词 - Noun)</b> chỉ người trong tiếng Trung. Không có từ nào là tính từ!
            </p>
            <div style="background: white; border-radius: 8px; padding: 12px; border: 1px solid #BFDBFE;">
                <span style="color: #2563EB; font-weight: bold; font-size: 0.95em;">⚙️ CÁCH DÙNG ĐẶC BIỆT: Danh từ làm Định ngữ</span>
                <p style="color: #334155; font-size: 0.92em; line-height: 1.5; margin-top: 6px; margin-bottom: 10px;">
                    Trong tiếng Trung, các danh từ chỉ nữ giới (đặc biệt là <b>女性</b>, <b>女子</b>, <b>女生</b>) có thể đứng trước một danh từ khác để đóng vai trò làm <b>định ngữ bổ nghĩa</b> (tương tự như cách dùng danh từ bổ nghĩa trong tiếng Anh).
                </p>
                <ul style="color: #334155; font-size: 0.92em; line-height: 1.8; margin: 0; padding-left: 20px;">
                    <li><span class="pinyin-text" style="color:#2563EB; font-size:1.05em; font-weight:bold;">女性朋友</span> (nǚxìng péngyou) = Bạn bè là nữ giới <i>(Danh từ 女性 bổ nghĩa cho 朋友)</i></li>
                    <li><span class="pinyin-text" style="color:#2563EB; font-size:1.05em; font-weight:bold;">女子单打</span> (nǚzǐ dāndǎ) = Đơn nữ (tennis, cầu lông) <i>(Danh từ 女子 bổ nghĩa cho 单打)</i></li>
                    <li><span class="pinyin-text" style="color:#2563EB; font-size:1.05em; font-weight:bold;">女生宿舍</span> (nǚshēng sùshè) = Ký túc xá nữ <i>(Danh từ 女生 bổ nghĩa cho 宿舍)</i></li>
                </ul>
            </div>
            <p style="color: #475569; font-size: 0.88em; font-style: italic; margin-top: 10px; margin-bottom: 0;">
                * Mẹo phân biệt: Chữ đơn <b>女 (nǚ)</b> mới đóng vai trò là tính từ/tiền tố ghép từ chỉ giới tính (ví dụ: 女医生 - bác sĩ nữ). Còn 7 từ trên đều là các danh từ đầy đủ, độc lập.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<br/>", unsafe_allow_html=True)
    st.subheader("3. So sánh ")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "👩‍🦰 女人 vs 妇女 (Phụ nữ)", 
        "👧 女孩 vs 女生 (Cô gái trẻ)", 
        "🏛️ 女性 vs 女子 (Trang trọng)", 
        "🏠 女儿 (Mối quan hệ gia đình)"
    ])
    
    with tab1:
        st.markdown(
            """
            <div style="background-color: #f8fafc; border-left: 4px solid #f43f5e; padding: 15px; border-radius: 8px; margin-bottom: 15px;">
                <h4 style="color: #9f1239; margin-top: 0;">Sự khác biệt lớn nhất nằm ở <b>độ tuổi tâm lý</b> và <b>sắc thái xã hội</b>:</h4>
                <ul style="line-height: 1.6; color: #334155; padding-left: 20px;">
                    <li><b>女人 (nǚrén):</b> Rất phổ thông, dùng trong khẩu ngữ để chỉ bất kỳ người mang giới tính nữ đã trưởng thành nào. Từ trái nghĩa trực tiếp là <b>男人 (nánrén - đàn ông)</b>.</li>
                    <li><b>妇女 (fùnǚ):</b> Mang sắc thái chính trị, xã hội, pháp lý chính thống. Thường chỉ người phụ nữ đã trưởng thành, đặc biệt là đã lập gia đình hoặc trung niên.</li>
                </ul>
                <div style="background: white; border: 1px solid #fed7aa; border-radius: 8px; padding: 12px; margin-top: 10px;">
                    <span style="color: #d97706; font-weight: bold;">🏮 GÓC VĂN HÓA:</span><br/>
                    Trong xã hội hiện đại, phụ nữ rất nhạy cảm với tuổi tác. Từ <b>妇女</b> trong đời sống hàng ngày thường mang lại cảm giác 'hơi già nua, luộm thuộm của người nội trợ'. Do đó, <b>tuyệt đối không được gọi một cô gái trẻ hoặc đồng nghiệp nữ chưa chồng là 妇女</b>. Họ sẽ cảm thấy không vui! Hãy gọi họ là <b>女生 (nǚshēng)</b> hoặc từ lóng tôn vinh là <b>美女 (měinǚ - mỹ nữ/người đẹp)</b>.
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    with tab2:
        st.markdown(
            """
            <div style="background-color: #f8fafc; border-left: 4px solid #3b82f6; padding: 15px; border-radius: 8px; margin-bottom: 15px;">
                <h4 style="color: #1e40af; margin-top: 0;">Sự chuyển biến thời thượng trong cách xưng hô:</h4>
                <ul style="line-height: 1.6; color: #334155; padding-left: 20px;">
                    <li><b>女孩 (nǚhái):</b> Gợi lên hình ảnh một cô bé đáng yêu, ngây thơ, tinh nghịch hoặc một thiếu nữ chưa trưởng thành (teenager).</li>
                    <li><b>女生 (nǚshēng):</b> Gốc từ là "nữ sinh" (học sinh, sinh viên nữ). Nhưng ngày nay, từ này đã biến đổi thành một danh từ cực kỳ thời thượng để chỉ những cô gái trẻ nói chung (từ tuổi teen đến khoảng 30 tuổi).</li>
                </ul>
                <div style="background: white; border: 1px solid #bfdbfe; border-radius: 8px; padding: 12px; margin-top: 10px;">
                    <span style="color: #2563eb; font-weight: bold;">💡 MẸO SỬ DỤNG:</span><br/>
                    Khi làm việc tại văn phòng công sở hoặc đi giao lưu xã hội, nếu bạn muốn gọi chung các đồng nghiệp nữ trẻ tuổi một cách lịch sự, thanh lịch và tôn trọng, hãy dùng từ <b>女生们 (nǚshēngmen)</b> thay vì <b>女人 (nǚrén)</b>. Từ <i>女生</i> vừa mang sắc thái trí thức, hiện đại lại vừa tôn vinh sự trẻ trung của họ.
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    with tab3:
        st.markdown(
            """
            <div style="background-color: #f8fafc; border-left: 4px solid #10b981; padding: 15px; border-radius: 8px; margin-bottom: 15px;">
                <h4 style="color: #065f46; margin-top: 0;">Thuật ngữ mang tính chính quy, học thuật và thể thao:</h4>
                <ul style="line-height: 1.6; color: #334155; padding-left: 20px;">
                    <li><b>女性 (nǚxìng):</b> Tập trung thuần túy vào đặc điểm <b>giới tính</b> (female/nữ giới). Từ này mang tính khách quan, khoa học, y học hoặc thống kê. Thường đi cặp với <b>男性 (nánxìng - nam giới)</b>.</li>
                    <li><b>女子 (nǚzǐ):</b> Mang sắc thái cổ xưa, trang nhã. Trong tiếng Trung hiện đại, từ này được dùng cố định làm <b>tiêu đề trong các cuộc thi thể thao chính quy</b> hoặc tên các tổ chức (Ví dụ: bóng đá nữ - 女子足球, đơn nữ cầu lông - 女子单打). Đi cặp với <b>男子 (nánzǐ - nam tử)</b>.</li>
                </ul>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    with tab4:
        st.markdown(
            """
            <div style="background-color: #f8fafc; border-left: 4px solid #8b5cf6; padding: 15px; border-radius: 8px; margin-bottom: 15px;">
                <h4 style="color: #5b21b6; margin-top: 0;">Từ vựng chỉ quan hệ thân tộc duy nhất:</h4>
                <p style="line-height: 1.6; color: #334155;">
                    <b>女儿 (nǚ'ér)</b> là từ duy nhất mang nghĩa là <b>"con gái" của bố mẹ</b> (con ruột/con nuôi). Trái nghĩa của nó là <b>儿子 (érzi - con trai)</b>.
                </p>
                <div style="background: white; border: 1px solid #f3e8ff; border-radius: 8px; padding: 12px; margin-top: 10px; border-left: 4px solid #a855f7;">
                    <span style="color: #e53e3e; font-weight: bold;">⚠️ CẢNH BÁO LỖI SAI:</span><br/>
                    Bạn không được dùng từ <b>女儿</b> để chỉ những người con gái xa lạ gặp ngoài đường, hoặc giới thiệu bạn gái lớp bên cạnh là <i>女儿</i>, trừ khi bạn muốn nhận cô ấy làm con gái ruột của mình! Ngoài đường, hãy dùng <b>女孩</b> hoặc <b>女生</b>.
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    st.markdown("---")
    st.subheader("4. Quick Quiz")
    st.info("Hãy áp dụng các quy tắc vừa học để giải quyết các tình huống giao tiếp thực tế dưới đây.")
    
    # State quản lý quiz
    quiz_submitted_key = "b4_female_quiz_submitted"
    if quiz_submitted_key not in st.session_state:
        st.session_state[quiz_submitted_key] = False
        
    score = 0
    total = len(FEMALE_VOCAB_QUIZ_DATA)
    
    # Render các câu hỏi trắc nghiệm
    for idx, item in enumerate(FEMALE_VOCAB_QUIZ_DATA):
        st.write("")
        st.markdown(f"**Câu {idx + 1}:** {item['q']}")
        
        # Đảm bảo index radio được khởi tạo và ghi nhớ
        radio_key = f"b4_female_q_radio_{idx}"
        
        selected = st.radio(
            "Chọn đáp án đúng nhất:",
            item["choices"],
            index=0,
            key=radio_key,
            disabled=st.session_state[quiz_submitted_key]
        )
        
        if selected == item["answer"]:
            score += 1
            
        # Hiển thị phản hồi khi đã nộp bài
        if st.session_state[quiz_submitted_key]:
            if selected == item["answer"]:
                st.success(f"✅ Chính xác! Đáp án đúng: **{item['answer']}**")
            else:
                st.error(f"❌ Chưa đúng! Bạn đã chọn: *{selected}*. Đáp án đúng là: **{item['answer']}**")
            st.markdown(f"<div style='background-color:#f1f5f9; padding:10px; border-radius:6px; font-size:0.9em; color:#475569;'><b>Giải thích:</b> {item['explain']}</div>", unsafe_allow_html=True)
            
    st.markdown("<br/>", unsafe_allow_html=True)
    
    # Nút bấm nộp bài
    if not st.session_state[quiz_submitted_key]:
        if st.button("📝 Chấm điểm Bài tập", type="primary", use_container_width=True):
            st.session_state[quiz_submitted_key] = True
            st.session_state.scores["b4_female_vocab"] = (score, total)
            save_progress()
            st.rerun()
    else:
        # Hiển thị điểm số chung cuộc
        st.markdown(
            f"""
            <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border: 1px solid #bbf7d0; padding: 20px; border-radius: 12px; text-align: center; margin-top: 15px;">
                <h3 style="color: #166534; margin-top:0;">🎉 Kết quả của bạn!</h3>
                <span style="font-size: 2.5em; font-weight: bold; color: #15803d;">{score} / {total}</span>
                <p style="color: #166534; margin-bottom: 0; font-size:1.1em; font-weight: 500;">Bạn đã hoàn thành bài tập phân biệt từ vựng chỉ Nữ giới!</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        if score == total:
            st.balloons()
            st.success("Tuyệt vời! Bạn đã trả lời đúng 100% câu hỏi! Cố lên nhé! 💪")
            
        if st.button("🔄 Làm lại bài tập", use_container_width=True):
            st.session_state[quiz_submitted_key] = False
            if "b4_female_vocab" in st.session_state.scores:
                del st.session_state.scores["b4_female_vocab"]
            save_progress()
            st.rerun()

def show_lesson4_vocab(extended_only=False):
    if extended_only:
        render_lesson_intro("📚 Bài 4.1: Từ vựng mở rộng", "Học các từ vựng mở rộng dưới dạng thẻ từ tương tác (Flashcards) có phát âm bản xứ.")
    else:
        render_lesson_intro("📚 Bài 4: từ vựng")

    VOCAB_LIST = [
        {"group": "ia (ya)", "emoji": "🏠", "word": "家", "pinyin": "jiā", "vietnamese": "Nhà", "key_prefix": "ia_jia", "example_han": "这是我的家。", "example_py": "Zhè shì wǒ de jiā.", "example_vi": "Đây là nhà của tôi."},
        {"group": "ia (ya)", "emoji": "🦆", "word": "鸭", "pinyin": "yā", "vietnamese": "Con vịt", "key_prefix": "ia_ya", "example_han": "鸭子很可爱。", "example_py": "Yāzi hěn kě'ài.", "example_vi": "Con vịt rất đáng yêu."},
        {"group": "ie (ye)", "emoji": "👩‍🦰", "word": "姐姐", "pinyin": "jiějie", "vietnamese": "Chị gái", "key_prefix": "ie_jie", "example_han": "我的姐姐很美。", "example_py": "Wǒ de jiějie hěn měi.", "example_vi": "Chị gái tôi rất đẹp."},
        {"group": "ie (ye)", "emoji": "👴", "word": "爷爷", "pinyin": "yéye", "vietnamese": "Ông nội", "key_prefix": "ie_ye", "example_han": "爷爷爱栽花。", "example_py": "Yéye ài zāihuā.", "example_vi": "Ông nội thích trồng hoa."},
        {"group": "iao (yao)", "emoji": "👶", "word": "小", "pinyin": "xiǎo", "vietnamese": "Nhỏ, bé", "key_prefix": "iao_xiao", "example_han": "他很小。", "example_py": "Tā hěn xiǎo.", "example_vi": "Cậu bé ấy rất nhỏ."},
        {"group": "iao (yao)", "emoji": "💊", "word": "药", "pinyin": "yào", "vietnamese": "Thuốc", "key_prefix": "iao_yao", "example_han": "我吃药。", "example_py": "Wǒ chī yào.", "example_vi": "Tôi uống thuốc."},
        {"group": "iu (you)", "emoji": "6️⃣", "word": "六", "pinyin": "liù", "vietnamese": "Số sáu", "key_prefix": "iu_liu", "example_han": "我有六个女朋友。", "example_py": "Wǒ yǒu liù ge nǚ péngyǒu.", "example_vi": "Tôi có 6 người bạn gái."},
        {"group": "iu (you)", "emoji": "🤝", "word": "有", "pinyin": "yǒu", "vietnamese": "Có", "key_prefix": "iu_you", "example_han": "我有一个姐姐。", "example_py": "Wǒ yǒu yī ge jiějie.", "example_vi": "Tôi có một người chị gái."},
        {"group": "ua (wa)", "emoji": "🌸", "word": "花", "pinyin": "huā", "vietnamese": "Bông hoa, hoa", "key_prefix": "ua_hua", "example_han": "花很美。", "example_py": "Huā hěn měi.", "example_vi": "Hoa rất đẹp."},
        {"group": "ua (wa)", "emoji": "🧸", "word": "娃娃", "pinyin": "wáwa", "vietnamese": "Búp bê, em bé", "key_prefix": "ua_wawa", "example_han": "我喜欢娃娃。", "example_py": "Wǒ xǐhuān wáwa.", "example_vi": "Tôi thích búp bê."},
        {"group": "uo (wo)", "emoji": "🙋‍♂️", "word": "我", "pinyin": "wǒ", "vietnamese": "Tôi, tớ, mình", "key_prefix": "uo_wo", "example_han": "我是学生。", "example_py": "Wǒ shì xuéshēng.", "example_vi": "Tôi là học sinh."},
        {"group": "uo (wo)", "emoji": "🇨🇳", "word": "国家", "pinyin": "guójiā", "vietnamese": "Quốc gia, đất nước", "key_prefix": "uo_guojia", "example_han": "我的国家很美。", "example_py": "Wǒ de guójiā hěn měi.", "example_vi": "Đất nước của tôi rất đẹp."},
        {"group": "uai (wai)", "emoji": "🚪", "word": "外", "pinyin": "wài", "vietnamese": "Ngoài, bên ngoài", "key_prefix": "uai_wai", "example_han": "外面很美。", "example_py": "Wài mian hěn měi.", "example_vi": "Bên ngoài rất đẹp."},
        {"group": "uai (wai)", "emoji": "😎", "word": "帅", "pinyin": "shuài", "vietnamese": "Đẹp trai", "key_prefix": "uai_shuai", "example_han": "他很帅。", "example_py": "Tā hěn shuài.", "example_vi": "Anh ấy rất đẹp trai."},
        {"group": "ui (wei)", "emoji": "💧", "word": "水", "pinyin": "shuǐ", "vietnamese": "Nước", "key_prefix": "ui_shui", "example_han": "我喝水。", "example_py": "Wǒ hē shuǐ.", "example_vi": "Tôi uống nước."},
        {"group": "ui (wei)", "emoji": "📞", "word": "喂", "pinyin": "wèi", "vietnamese": "Alo", "key_prefix": "ui_wei", "example_han": "喂，你好吗？", "example_py": "Wèi, nǐ hǎo ma?", "example_vi": "Alo, bạn khỏe không?"},
        {"group": "ue (yue)", "emoji": "🌙", "word": "月", "pinyin": "yuè", "vietnamese": "Mặt trăng, tháng", "key_prefix": "ue_yue", "example_han": "月饼很好吃。", "example_py": "Yuèbǐng hěn hǎochī.", "example_vi": "Bánh trung thu rất ngon.", "note": "<b>1. Ngày hội Đoàn viên:</b> Vào đêm rằm tháng 8 âm lịch, người Trung Hoa sẽ trở về nhà sum họp gia đình, cùng thưởng thức bánh và ngắm trăng tròn trịa tượng trưng cho sự đoàn tụ trọn vẹn.<br/><b>2. Lễ hội Tạ ơn & Mừng mùa màng:</b> Tháng 8 âm lịch là thời điểm gặt hái xong vụ mùa thu. Người nông dân làm lễ cúng trăng, dâng lên các sản vật mới thu hoạch (trái cây, bánh trái) để tạ ơn đất trời đã ban cho một mùa màng bội thu, đồng thời cầu mong cho mùa sau mưa thuận gió hòa."},
        {"group": "ue (yue)", "emoji": "📚", "word": "学", "pinyin": "xué", "vietnamese": "Học", "key_prefix": "ue_xue", "example_han": "我学汉语。", "example_py": "Wǒ xué Hànyǔ.", "example_vi": "Tôi học Hán ngữ."},
        {"group": "Từ vựng mở rộng", "emoji": "😎", "word": "帅哥", "pinyin": "shuàigē", "vietnamese": "Soái ca, trai đẹp", "key_prefix": "ext_shuaige", "example_han": "这里有很多帅哥。", "example_py": "Zhèlǐ yǒu hěn duō shuàigē.", "example_vi": "Ở đây có rất nhiều trai đẹp."},
        {"group": "Từ vựng mở rộng", "emoji": "👸", "word": "美女", "pinyin": "měinǚ", "vietnamese": "Mỹ nữ, gái đẹp", "key_prefix": "ext_meinu", "example_han": "她是我们的美女。", "example_py": "Tā shì wǒmen de měinǚ.", "example_vi": "Cô ấy là mỹ nữ của chúng tôi."},
        {"group": "Từ vựng mở rộng", "emoji": "🥛", "word": "喝", "pinyin": "hē", "vietnamese": "Uống", "key_prefix": "ext_he", "example_han": "我想喝奶茶。", "example_py": "Wǒ xiǎng hē nǎichá.", "example_vi": "Tôi muốn uống trà sữa."},
        {"group": "Từ vựng mở rộng", "emoji": "🍚", "word": "吃", "pinyin": "chī", "vietnamese": "Ăn", "key_prefix": "ext_chi", "example_han": "你吃什么肉？", "example_py": "Nǐ chī shénme ròu?", "example_vi": "Bạn ăn thịt gì?"},
        {"group": "Từ vựng mở rộng", "emoji": "🧋", "word": "奶茶", "pinyin": "nǎichá", "vietnamese": "Trà sữa", "key_prefix": "ext_naicha", "example_han": "我爱喝奶茶。", "example_py": "Wǒ ài hē nǎichá.", "example_vi": "Tôi yêu thích uống trà sữa."},
        {"group": "Từ vựng mở rộng", "emoji": "😋", "word": "饿", "pinyin": "è", "vietnamese": "Đói", "key_prefix": "ext_e", "example_han": "我很饿。", "example_py": "Wǒ hěn è.", "example_vi": "Tôi rất đói."},
        {"group": "Từ vựng mở rộng", "emoji": "😫", "word": "累", "pinyin": "lèi", "vietnamese": "Mệt", "key_prefix": "ext_lei", "example_han": "你累吗？", "example_py": "Nǐ lèi ma?", "example_vi": "Bạn mệt không?"},
        {"group": "Từ vựng mở rộng", "emoji": "🍗", "word": "鸡肉", "pinyin": "jīròu", "vietnamese": "Thịt gà", "key_prefix": "ext_jirou", "example_han": "我喜欢吃鸡肉。", "example_py": "Wǒ xǐhuān chī jīròu.", "example_vi": "Tôi thích ăn thịt gà."},
        {"group": "Từ vựng mở rộng", "emoji": "🐟", "word": "鱼肉", "pinyin": "yúròu", "vietnamese": "Thịt cá", "key_prefix": "ext_yurou", "example_han": "鱼肉很好吃。", "example_py": "Yúròu hěn hǎochī.", "example_vi": "Thịt cá rất ngon."},
        {"group": "Từ vựng mở rộng", "emoji": "🥩", "word": "牛肉", "pinyin": "niúròu", "vietnamese": "Thịt bò", "key_prefix": "ext_niurou", "example_han": "牛肉很贵。", "example_py": "Niúròu hěn guì.", "example_vi": "Thịt bò rất đắt."}
    ]

    st.markdown(
        """
        <style>
        .flashcard-container {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
            border: 1px solid #e2e8f0;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.05);
            margin-bottom: 20px;
            display: flex;
            gap: 30px;
            align-items: center;
        }
        .flashcard-image-container {
            flex-shrink: 0;
            width: 200px;
            height: 200px;
            border-radius: 16px;
            overflow: hidden;
            border: 3px solid #f1f5f9;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            background: white;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .flashcard-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .flashcard-content {
            flex-grow: 1;
        }
        .flashcard-word {
            font-size: 3.5rem;
            font-weight: 800;
            color: #0f172a;
            line-height: 1.1;
            margin-bottom: 5px;
        }
        .flashcard-pinyin {
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
        .flashcard-vietnamese {
            font-size: 1.4rem;
            font-weight: 700;
            color: #334155;
            margin-bottom: 15px;
        }
        .flashcard-example-box {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 15px;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.01);
        }
        .flashcard-example-title {
            font-size: 0.8rem;
            color: #64748b;
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 6px;
            letter-spacing: 0.05em;
        }
        .flashcard-example-han {
            font-size: 1.4rem;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 2px;
        }
        .flashcard-example-py {
            font-family: 'Courier New', monospace;
            font-weight: 700;
            color: #059669;
            font-size: 1.05rem;
            margin-bottom: 4px;
        }
        .flashcard-example-vi {
            color: #475569;
            font-style: italic;
            font-size: 0.95rem;
            border-left: 2px solid #cbd5e1;
            padding-left: 8px;
        }
        
        @media (max-width: 768px) {
            .flashcard-container {
                flex-direction: column;
                padding: 20px;
                text-align: center;
                gap: 20px;
            }
            .flashcard-image-container {
                width: 160px;
                height: 160px;
            }
            .flashcard-example-vi {
                border-left: none;
                padding-left: 0;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if extended_only:
        vocab_pool = [w for w in VOCAB_LIST if w["group"] == "Từ vựng mở rộng"]
    else:
        vocab_pool = [w for w in VOCAB_LIST if w["group"] != "Từ vựng mở rộng"]

    groups = [f"Tất cả ({len(vocab_pool)} từ)"] + sorted(list(set(w["group"] for w in vocab_pool)))
    
    if len(groups) > 1:
        sel_group = st.selectbox("🔍 Chọn Nhóm Vận mẫu để học:", groups, key=f"sel_group_{extended_only}")
    else:
        sel_group = groups[0]

    if sel_group.startswith("Tất cả"):
        filtered_vocab = vocab_pool
    else:
        filtered_vocab = [w for w in vocab_pool if w["group"] == sel_group]

    slide_key = f"b4_vocab_slide_idx_{sel_group}"
    if slide_key not in st.session_state:
        st.session_state[slide_key] = 0

    cur_idx = st.session_state[slide_key]

    if cur_idx >= len(filtered_vocab):
        cur_idx = 0
        st.session_state[slide_key] = 0

    w = filtered_vocab[cur_idx]
    img_name_prefix = w["key_prefix"].split('_')[-1]
    img_path = ""
    for ext in [".png", ".jpg", ".jpeg", ".gif"]:
        p = os.path.join("assets", "lesson4", img_name_prefix + ext)
        if os.path.exists(p):
            img_path = p
            break

    img_base64 = ""
    if img_path and os.path.exists(img_path):
        with open(img_path, "rb") as f:
            data = f.read()
            mime = "image/png"
            if data.startswith(b'\xff\xd8'):
                mime = "image/jpeg"
            elif data.startswith(b'\x89PNG'):
                mime = "image/png"
            elif data.startswith(b'GIF8'):
                mime = "image/gif"
            img_base64 = f"data:{mime};base64,{base64.b64encode(data).decode('utf-8')}"

    if img_base64:
        img_tag = f'<img src="{img_base64}" class="flashcard-image" />'
    else:
        img_tag = f'<div style="font-size: 4rem;">{w["emoji"]}</div>'

    note_html = ""
    if "note" in w:
        note_html = f'<details style="margin-top: 10px; background-color: #F0F9FF; border-left: 3px solid #0EA5E9; border-radius: 6px; padding: 10px 14px; cursor: pointer;"><summary style="font-size: 0.88em; color: #0369A1; font-weight: bold; outline: none; list-style: none; display: flex; align-items: center; gap: 6px;">💡 <b>Xem giải thích nguồn gốc từ "月饼"</b></summary><div style="font-size: 0.85em; color: #334155; margin-top: 10px; line-height: 1.55; border-top: 1px dashed #BAE6FD; padding-top: 8px;">{w["note"]}</div></details>'

    card_html = f"""<div class="flashcard-container">
<div class="flashcard-image-container">{img_tag}</div>
<div class="flashcard-content">
<div class="flashcard-word">{w['word']}</div>
<div><span class="flashcard-pinyin">{w['pinyin']}</span></div>
<div class="flashcard-vietnamese">Nghĩa: {w['vietnamese']}</div>
<div class="flashcard-example-box">
<div class="flashcard-example-title">Ví dụ mẫu:</div>
<div class="flashcard-example-han">{w['example_han']}</div>
<div class="flashcard-example-py">{w['example_py']}</div>
<div class="flashcard-example-vi">{w['example_vi']}</div>
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
            if st.button("⬅️ Từ trước", use_container_width=True, key=f"btn_prev_{sel_group}"):
                st.session_state[slide_key] = (cur_idx - 1) % len(filtered_vocab)
                st.rerun()
        with col_next:
            if st.button("Từ sau ➡️", use_container_width=True, key=f"btn_next_{sel_group}"):
                st.session_state[slide_key] = (cur_idx + 1) % len(filtered_vocab)
                st.rerun()
                
        st.markdown(f"<div style='text-align: center; font-size: 1.25em; font-weight: bold; margin-top: 10px; color:#475569;'>Từ {cur_idx + 1} / {len(filtered_vocab)}</div>", unsafe_allow_html=True)
        progress_val = (cur_idx + 1) / len(filtered_vocab)
        st.progress(progress_val)

def show_lesson4_spelling(add_tones):
    render_lesson_intro("📚 Bài 4: Luyện tập ghép âm mở rộng", "Luyện tập ghép âm các thanh mẫu với 9 vận mẫu kép mở rộng (ia, ie, iao, iu, ua, uo, uai, ui, üe).")
    
    B4_LUYEN_TAP_FINALS = ["ia", "ie", "iao", "iu", "ua", "uo", "uai", "ui", "üe"]
    B4_LUYEN_TAP_ROWS = {
        "b": ["", "bie", "biao", "", "", "bo", "", "", ""],
        "p": ["", "pie", "piao", "", "", "po", "", "", ""],
        "m": ["", "mie", "miao", "miu", "", "mo", "", "", ""],
        "f": ["", "", "", "", "", "fo", "", "", ""],
        "d": ["", "die", "diao", "diu", "", "duo", "", "dui", ""],
        "t": ["", "tie", "tiao", "", "", "tuo", "", "tui", ""],
        "n": ["", "nie", "niao", "niu", "", "nuo", "", "", "nüe"],
        "l": ["", "lie", "liao", "liu", "", "luo", "", "", "lüe"],
        "g": ["", "", "", "", "gua", "guo", "guai", "gui", ""],
        "k": ["", "", "", "", "kua", "kuo", "kuai", "kui", ""],
        "h": ["", "", "", "", "hua", "huo", "huai", "hui", ""],
        "j": ["jia", "jie", "jiao", "jiu", "", "", "", "", "jue"],
        "q": ["qia", "qie", "qiao", "qiu", "", "", "", "", "que"],
        "x": ["xia", "xie", "xiao", "xiu", "", "", "", "", "xue"],
        "zh": ["", "", "", "", "zhua", "zhuo", "zhuai", "zhui", ""],
        "ch": ["", "", "", "", "chua", "chuo", "chuai", "chui", ""],
        "sh": ["", "", "", "", "shua", "shuo", "shuai", "shui", ""],
        "r": ["", "", "", "", "", "ruo", "", "rui", ""],
        "z": ["", "", "", "", "", "zuo", "", "zui", ""],
        "c": ["", "", "", "", "", "cuo", "", "cui", ""],
        "s": ["", "", "", "", "", "suo", "", "sui", ""]
    }
    
    st.subheader("Bảng luyện tập ghép âm mở rộng (Bài 4)")
    h_cols = st.columns([1.5] + [1] * len(B4_LUYEN_TAP_FINALS))
    h_cols[0].markdown("**T/V**")
    for i, f in enumerate(B4_LUYEN_TAP_FINALS): h_cols[i+1].markdown(f"**{f}**")
    for init in B4_LUYEN_TAP_ROWS.keys():
        r_cols = st.columns([1.5] + [1] * len(B4_LUYEN_TAP_FINALS))
        r_cols[0].markdown(f"**{init}**")
        for i, combo in enumerate(B4_LUYEN_TAP_ROWS[init]):
            if combo:
                with r_cols[i+1]:
                    with st.popover(combo, use_container_width=True):
                        for t in add_tones(combo):
                            col_t, col_btn = st.columns([2, 1])
                            col_t.write(f"- {t}")
                            with col_btn:
                                render_play_button(t, "🔊", key=f"btn_p_b4_{init}_{combo}_{t}", height=45)
            else:
                r_cols[i+1].write("")
