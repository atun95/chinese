import streamlit as st
import os
import base64
from lessons_data import *
from ui_utils import *

def check_spelling_rule(initial, final, tone_idx):
    # tone_idx: 0 to 4 (0: None/light, 1: tone 1, 2: tone 2, 3: tone 3, 4: tone 4)
    spelled = ""
    if not initial or initial == "(Không có)":
        if final == "ia": spelled = "ya"
        elif final == "ie": spelled = "ye"
        elif final == "iao": spelled = "yao"
        elif final == "iu": spelled = "you"
        elif final == "ua": spelled = "wa"
        elif final == "uo": spelled = "wo"
        elif final == "uai": spelled = "wai"
        elif final == "ui": spelled = "wei"
        elif final == "üe": spelled = "yue"
    else:
        # j, q, x compatibility
        if initial in ['j', 'q', 'x']:
            if final in ['ua', 'uo', 'uai', 'ui']:
                return None, f"❌ Lỗi ghép âm: Thanh mẫu <b>{initial}</b> không thể đi cùng nhóm vận mẫu bắt đầu bằng <b>u</b> ({final})!"
            if final == "üe":
                spelled = f"{initial}ue"
            else:
                spelled = f"{initial}{final}"
        # b, p, m, f compatibility
        elif initial in ['b', 'p', 'm', 'f']:
            if final in ['ua', 'uai', 'ui']:
                return None, f"❌ Lỗi ghép âm: Âm môi <b>{initial}</b> không thể đi cùng vận mẫu <b>{final}</b>!"
            if final == "üe":
                return None, f"❌ Lỗi ghép âm: Thanh mẫu <b>{initial}</b> không thể đi cùng vận mẫu <b>üe</b>!"
            if final == 'uo':
                spelled = f"{initial}o"
            else:
                spelled = f"{initial}{final}"
        # d, t, g, k, h, zh, ch, sh, r, z, c, s compatibility
        elif initial in ['d', 't', 'g', 'k', 'h', 'zh', 'ch', 'sh', 'r', 'z', 'c', 's']:
            if final == "üe":
                return None, f"❌ Lỗi ghép âm: Thanh mẫu <b>{initial}</b> không thể đi cùng vận mẫu <b>üe</b>!"
            spelled = f"{initial}{final}"
        # n, l compatibility
        elif initial in ['n', 'l']:
            spelled = f"{initial}{final}"
            
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
    render_lesson_intro("📚 Bài 4.3: Luyện tập", "Hoạt động thực hành nhóm và phản xạ nhanh dành cho lớp học online.")
    
    
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
        "🧩 3. Assembler Puzzle"
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

    # ------------------ CHALLENGE 3: ASSEMBLER PUZZLE ------------------
    with tab_challenge3:
        st.markdown(
            """
            <div class="challenge-header">🧩 Thử thách: Lắp ráp Bính âm (Pinyin Assembler)</div>
            <p style='color: #475569;'>Ghép các mảnh ghép để tạo thành Bính âm chính xác biểu thị nghĩa của từ khóa.</p>
            """, 
            unsafe_allow_html=True
        )
        
        ASSEMBLY_TARGETS = [
            {"target": "huā", "meaning": "Đóa hoa / Hoa", "image": "hua.png", "hint": "Gợi ý: Thanh mẫu bắt đầu bằng 'h', vận mẫu kép 'ua', thanh 1"},
            {"target": "shuǐ", "meaning": "Nước", "image": "shui.png", "hint": "Gợi ý: Thanh mẫu uốn lưỡi 'sh', vận mẫu gốc 'uei' (nhớ quy tắc rút gọn), thanh 3"},
            {"target": "liù", "meaning": "Số sáu", "image": "liu.png", "hint": "Gợi ý: Thanh mẫu 'l', vận mẫu gốc 'iou' (nhớ quy tắc rút gọn), thanh 4"},
            {"target": "yuè", "meaning": "Mặt trăng / Tháng", "image": "yue.png", "hint": "Gợi ý: Không có thanh mẫu, vận mẫu tròn môi 'üe' đứng độc lập (nhớ quy tắc biến đổi), thanh 4"}
        ]
        
        if "assembly_idx" not in st.session_state:
            st.session_state.assembly_idx = 0
            
        cur_idx = st.session_state.assembly_idx
        
        if cur_idx >= len(ASSEMBLY_TARGETS):
            st.session_state.scores["b4_assembly"] = (4, 4)
            st.markdown(
                """
                <div style="background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%); border: 1px solid #A7F3D0; border-radius: 12px; padding: 22px; text-align: center;">
                    <span style="font-size: 2em;">🏆</span>
                    <h3 style="color: #065F46; margin-top: 5px;">Chúc mừng bạn đã hoàn thành xuất sắc Thử thách Lắp ráp!</h3>
                    <p style="color: #047857; margin-bottom: 15px;">Bạn đã làm chủ hoàn toàn cách ghép âm và quy luật viết Pinyin mở rộng!</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button("🔄 Chơi lại Thử thách Lắp ráp từ đầu", use_container_width=True):
                st.session_state.assembly_idx = 0
                if "b4_assembly" in st.session_state.scores:
                    del st.session_state.scores["b4_assembly"]
                st.rerun()
        else:
            item = ASSEMBLY_TARGETS[cur_idx]
            
            img_base64 = ""
            if "image" in item:
                img_path = os.path.join("assets", "lesson4", item["image"])
                if os.path.exists(img_path):
                    with open(img_path, "rb") as f:
                        img_base64 = f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

            img_html = f'<div style="margin: 15px 0;"><img src="{img_base64}" style="width: 130px; height: 130px; border-radius: 16px; border: 1px solid #e2e8f0; object-fit: cover; background: white; padding: 5px; box-shadow: 0 4px 12px rgba(0,0,0,0.06);"/></div>' if img_base64 else ""

            st.markdown(
                f"""
                <div class="puzzle-card">
                    <span style="font-size: 0.9em; color: #64748b; font-weight: bold; text-transform: uppercase;">MỤC TIÊU LẮP RÁP ({cur_idx + 1}/{len(ASSEMBLY_TARGETS)}):</span>
                    {img_html}
                    <h2 style="color: #0f172a; margin: 5px 0;">"{item['meaning']}"</h2>
                    <p style="color: #475569; font-style: italic; font-size: 0.9em; margin-bottom: 0;">{item['hint']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            cols_assembly = st.columns(3)
            with cols_assembly[0]:
                a_initials = ["(Không có)", "b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "j", "q", "x", "zh", "ch", "sh", "r", "z", "c", "s"]
                sel_a_initial = st.selectbox("Chọn Thanh mẫu:", a_initials, key=f"assem_init_{cur_idx}")
            with cols_assembly[1]:
                a_finals = ["ia", "ie", "iao", "iou", "ua", "uo", "uai", "uei", "üe"]
                sel_a_final = st.selectbox("Chọn Vận mẫu gốc:", a_finals, key=f"assem_final_{cur_idx}")
            with cols_assembly[2]:
                a_tones = [
                    "Thanh 1",
                    "Thanh 2 ",
                    "Thanh 3 ",
                    "Thanh 4 "
                ]
                sel_a_tone = st.selectbox("Chọn Thanh điệu:", a_tones, key=f"assem_tone_{cur_idx}")
                
            a_tone_idx = a_tones.index(sel_a_tone) + 1
            
            assembled_pinyin, err_msg = check_spelling_rule(sel_a_initial, sel_a_final, a_tone_idx)
            
            if err_msg:
                st.error(err_msg)
            else:
                st.markdown(
                    f"""
                    <div style="text-align: center; margin: 15px 0;">
                        <span>Bính âm lắp ráp hiện tại của bạn:</span><br/>
                        <div class="spelling-box">{assembled_pinyin}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                col_actions = st.columns([1, 1])
                with col_actions[0]:
                    render_play_button(assembled_pinyin, "🔊 Phát âm thử âm tiết", key=f"assem_play_{cur_idx}", type="secondary")
                with col_actions[1]:
                    if st.button("🚀 Kiểm tra & Xác nhận", type="primary", use_container_width=True, key=f"assem_check_{cur_idx}"):
                        if assembled_pinyin == item["target"]:
                            st.success(f"🎉 Tuyệt vời! Bạn đã lắp ráp chính xác từ '{item['meaning']}' thành công là **{assembled_pinyin}**!")
                            st.balloons()
                            st.session_state.assembly_idx = cur_idx + 1
                            st.rerun()
                        else:
                            st.error(f"❌ Chưa chính xác! Âm vừa ghép là '{assembled_pinyin}', nhưng từ '{item['meaning']}' cần cách viết khác. Hãy thử lại theo gợi ý!")


    # Tổng kết — chỉ hiện khi học viên đã chấm đủ các bài tập
    st.markdown("---")
    with st.expander("📊 Lịch sử & Tổng kết Bài 4", expanded=True):
        from datetime import datetime, timezone, timedelta
        cur = st.session_state.scores
        labels_b4 = {
            "b4_listening": "BT1: Luyện nghe", 
            "b4_spelling": "BT2: Chính tả", 
            "b4_assembly": "BT3: Lắp ráp Bính âm", 
            "b4_female_vocab": "BT4: Phân biệt Nữ giới"
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
                        "BT3: Lắp ráp Bính âm": fmt("b4_assembly"),
                        "BT4: Phân biệt Nữ giới": fmt("b4_female_vocab")
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

def show_lesson4_vocab():
    render_lesson_intro("📚 Bài 4: Hệ thống từ vựng Vận mẫu kép")

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
        {"group": "ue (yue)", "emoji": "🌙", "word": "月", "pinyin": "yuè", "vietnamese": "Mặt trăng, tháng", "key_prefix": "ue_yue", "example_han": "月饼很好吃。", "example_py": "Yuèbǐng hěn hǎochī.", "example_vi": "Bánh trung thu rất ngon."},
        {"group": "ue (yue)", "emoji": "📚", "word": "学", "pinyin": "xué", "vietnamese": "Học", "key_prefix": "ue_xue", "example_han": "我学汉语。", "example_py": "Wǒ xué Hànyǔ.", "example_vi": "Tôi học tiếng Trung."}
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

    groups = ["Tất cả (18 từ)"] + sorted(list(set(w["group"] for w in VOCAB_LIST)))
    sel_group = st.selectbox("🔍 Chọn Nhóm Vận mẫu để học:", groups)

    if sel_group.startswith("Tất cả"):
        filtered_vocab = VOCAB_LIST
    else:
        filtered_vocab = [w for w in VOCAB_LIST if w["group"] == sel_group]

    slide_key = f"b4_vocab_slide_idx_{sel_group}"
    if slide_key not in st.session_state:
        st.session_state[slide_key] = 0

    cur_idx = st.session_state[slide_key]

    if cur_idx >= len(filtered_vocab):
        cur_idx = 0
        st.session_state[slide_key] = 0

    w = filtered_vocab[cur_idx]
    img_name = w["key_prefix"].split('_')[-1] + '.png'
    img_path = os.path.join("assets", "lesson4", img_name)
    img_base64 = ""
    if os.path.exists(img_path):
        with open(img_path, "rb") as f:
            img_base64 = f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

    if img_base64:
        img_tag = f'<img src="{img_base64}" class="flashcard-image" />'
    else:
        img_tag = f'<div style="font-size: 4rem;">{w["emoji"]}</div>'

    card_html = f"""
    <div class="flashcard-container">
        <div class="flashcard-image-container">
            {img_tag}
        </div>
        <div class="flashcard-content">
            <div class="flashcard-word">{w['word']}</div>
            <div>
                <span class="flashcard-pinyin">{w['pinyin']}</span>
            </div>
            <div class="flashcard-vietnamese">Nghĩa: {w['vietnamese']}</div>
            <div class="flashcard-example-box">
                <div class="flashcard-example-title">Ví dụ mẫu:</div>
                <div class="flashcard-example-han">{w['example_han']}</div>
                <div class="flashcard-example-py">{w['example_py']}</div>
                <div class="flashcard-example-vi">{w['example_vi']}</div>
            </div>
        </div>
    </div>
    """

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
            if st.button("⬅️ Từ trước", disabled=(cur_idx == 0), use_container_width=True, key=f"btn_prev_{sel_group}"):
                st.session_state[slide_key] -= 1
                st.rerun()
        with col_next:
            if st.button("Từ sau ➡️", disabled=(cur_idx == len(filtered_vocab) - 1), use_container_width=True, key=f"btn_next_{sel_group}"):
                st.session_state[slide_key] += 1
                st.rerun()
                
        st.markdown(f"<div style='text-align: center; font-size: 1.25em; font-weight: bold; margin-top: 10px; color:#475569;'>Từ {cur_idx + 1} / {len(filtered_vocab)}</div>", unsafe_allow_html=True)
        progress_val = (cur_idx + 1) / len(filtered_vocab)
        st.progress(progress_val)
