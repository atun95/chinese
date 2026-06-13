import streamlit as st
from datetime import datetime, timezone, timedelta
from lessons_data import *
from ui_utils import *

def show_lesson2_intro(add_tones):
    render_lesson_intro("📚 Bài 2.1: Vận mẫu kép", "Nắm vững 4 vận mẫu kép cơ bản và ví dụ thực tế.")
    
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
    
    B2_BASIC_VAN_KEP_DATA = [
        {
            "chu": "ai",
            "hdsd": "Phát âm /a/ trước rồi trượt sang /i/.",
            "cach_doc_sau": "Bắt đầu với khẩu hình miệng mở rộng phát âm nguyên âm /a/, sau đó thu hẹp dần khoảng cách giữa hai hàm răng và trượt mượt mà sang nguyên âm /i/.",
            "tuong_duong": "Tương đương âm <b>ai</b> trong tiếng Việt (vd: tai, vai).",
            "luu_y": "Khi viết Pinyin, nếu không có thanh mẫu đứng trước, âm này giữ nguyên là <span class='spelling-highlight'>ai</span> (vd: ài - yêu).",
            "vd_han": "来",
            "vd_py": "lái",
            "vietnamese": "đến / lại đây",
            "more_examples": [
                {"han": "爱", "py": "ài", "vi": "yêu"},
                {"han": "买", "py": "mǎi", "vi": "mua"},
                {"han": "白", "py": "bái", "vi": "màu trắng"}
            ],
            "color": "linear-gradient(135deg, #FFF1F2 0%, #FFE4E6 100%)",
            "border_color": "#F43F5E",
            "text_color": "#9F1239"
        },
        {
            "chu": "ei",
            "hdsd": "Phát âm /e/ trước rồi trượt sang /i/.",
            "cach_doc_sau": "Khẩu hình miệng hơi dẹt, phát âm nguyên âm /e/ (gần giống ê) trước rồi nhanh chóng thu hẹp miệng trượt sang nguyên âm /i/.",
            "tuong_duong": "Gần giống âm <b>ây</b> trong tiếng Việt (vd: mây, tây).",
            "luu_y": "Khi không có thanh mẫu đi kèm, âm này giữ nguyên là <span class='spelling-highlight'>ei</span>.",
            "vd_han": "内",
            "vd_py": "nèi",
            "vietnamese": "bên trong / nội",
            "more_examples": [
                {"han": "美", "py": "měi", "vi": "đẹp"},
                {"han": "累", "py": "lèi", "vi": "mệt"},
                {"han": "杯", "py": "bēi", "vi": "cái cốc/ly"}
            ],
            "color": "linear-gradient(135deg, #FDF2F8 0%, #FCE7F3 100%)",
            "border_color": "#EC4899",
            "text_color": "#9D174D"
        },
        {
            "chu": "ao",
            "hdsd": "Phát âm /a/ trước rồi trượt sang /o/ (u).",
            "cach_doc_sau": "Khẩu hình miệng mở rộng phát âm nguyên âm /a/ trước, sau đó nhanh chóng khép bớt môi và thu tròn môi lại chuyển sang âm /o/ hoặc /u/.",
            "tuong_duong": "Tương đương âm <b>ao</b> trong tiếng Việt (vd: cao, sao).",
            "luu_y": "Khi không có thanh mẫu đứng trước, âm này viết giữ nguyên là <span class='spelling-highlight'>ao</span>.",
            "vd_han": "宝贝",
            "vd_py": "bǎobèi",
            "vietnamese": "bảo bối / em bé",
            "more_examples": [
                {"han": "好", "py": "hǎo", "vi": "tốt / khỏe"},
                {"han": "包", "py": "bāo", "vi": "bao/túi xách"},
                {"han": "高", "py": "gāo", "vi": "cao"}
            ],
            "color": "linear-gradient(135deg, #F5F3FF 0%, #EDE9FE 100%)",
            "border_color": "#8B5CF6",
            "text_color": "#5B21B6"
        },
        {
            "chu": "ou",
            "hdsd": "Phát âm /o/ trước rồi trượt sang /u/.",
            "cach_doc_sau": "Khẩu hình miệng mở tròn vừa phải phát âm âm /o/ làm âm chính, sau đó thu nhỏ tròn môi để trượt sang nguyên âm /u/.",
            "tuong_duong": "Gần giống âm <b>âu</b> trong tiếng Việt (vd: trâu, lâu).",
            "luu_y": "Khi đứng độc lập không có thanh mẫu đứng trước, âm này viết giữ nguyên là <span class='spelling-highlight'>ou</span>.",
            "vd_han": "狗",
            "vd_py": "gǒu",
            "vietnamese": "con chó",
            "more_examples": [
                {"han": "口", "py": "kǒu", "vi": "miệng / nhân khẩu"},
                {"han": "头", "py": "tóu", "vi": "đầu"},
                {"han": "肉", "py": "ròu", "vi": "thịt"}
            ],
            "color": "linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%)",
            "border_color": "#3B82F6",
            "text_color": "#1E40AF"
        }
    ]
    
    st.subheader("Chi tiết 4 vận mẫu kép cơ bản")
    for idx, item in enumerate(B2_BASIC_VAN_KEP_DATA):
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
            render_play_button(item["vd_py"], f"🔊 Phát âm từ khóa ({item['vd_py']})", key=f"btn_b2_main_{item['chu']}_{idx}")
            
            st.markdown("<div style='font-size:0.8em; font-weight:bold; color:#64748b; margin-top:12px; margin-bottom:4px;'>LUYỆN TẬP ÂM KHÁC:</div>", unsafe_allow_html=True)
            for s_idx, sub in enumerate(item["more_examples"]):
                sub_key = f"btn_b2_sub_{item['chu']}_{idx}_{s_idx}"
                render_play_button(sub["py"], f"🔊 {sub['han']} ({sub['py']}): {sub['vi']}", key=sub_key)
        st.markdown("<br/>", unsafe_allow_html=True)

def show_lesson2_spelling(add_tones):
    render_lesson_intro("📚 Bài 2.2: Bảng luyện tập ghép âm", "Luyện tập ghép âm các thanh mẫu với vận mẫu kép cơ bản kèm theo 4 thanh điệu.")
    st.subheader("Bảng luyện tập ghép âm")
    h_cols = st.columns([1.5] + [1] * len(B2_LUYEN_TAP_FINALS))
    h_cols[0].markdown("**T/V**")
    for i, f in enumerate(B2_LUYEN_TAP_FINALS): h_cols[i+1].markdown(f"**{f}**")
    for init in B2_LUYEN_TAP_ROWS.keys():
        r_cols = st.columns([1.5] + [1] * len(B2_LUYEN_TAP_FINALS))
        r_cols[0].markdown(f"**{init}**")
        for i, combo in enumerate(B2_LUYEN_TAP_ROWS[init]):
            if combo:
                with r_cols[i+1]:
                    with st.popover(combo, use_container_width=True):
                        for t in add_tones(combo): st.write(f"- {t}")

def show_lesson2_exercises(save_progress, save_score_row_b2, load_all_scores_b2):
    st.header("📝 Bài 2: Bài tập vận mẫu kép")

    # Dùng dict riêng cho phiên hiện tại, tách biệt khỏi dữ liệu cũ load từ file
    if "b2_current" not in st.session_state:
        st.session_state.b2_current = {}

    # 1. Mini quiz từ vựng
    with st.expander("Bài tập 1: Mini quiz từ vựng", expanded=False):
        st.caption("Chọn nghĩa đúng nhất cho từng từ.")
        score_b2_vcb = 0
        for idx, item in enumerate(B2_QUIZ_VOCAB):
            choices = shuffled_options(item["choices"], f"b2_vcb-{idx}")
            if choices[0] == item["answer"] and len(choices) > 1:
                choices[0], choices[1] = choices[1], choices[0]
            key = f"b2_vcb_q_{idx}"
            selected = st.radio(f"Câu {idx+1}: {item['q']}?", choices, index=0, key=key)
            if selected == item["answer"]: score_b2_vcb += 1
        if st.button("Chấm điểm Bài 1", key="btn_b2_vcb"):
            st.session_state.b2_current["b2_vcb"] = (score_b2_vcb, len(B2_QUIZ_VOCAB))
            save_progress()
            st.success(f"Bạn đúng {score_b2_vcb}/{len(B2_QUIZ_VOCAB)} câu.")

    # 2. Luyện nghe
    with st.expander("Bài tập 2: Luyện nghe và chọn Pinyin", expanded=False):
        score_b2_ls = 0
        for i, q in enumerate(B2_QUIZ_LISTENING):
            st.write(f"**Câu {i+1}:** Nghe từ '{q['q']}' và chọn pinyin đúng")
            render_play_button(q["hanzi"], "🔊 Nghe mẫu", key=f"b2_listen_{i}")
            key = f"b2_tone_q_{i}"
            choices = shuffled_options(q["choices"], f"b2_ls-{i}")
            if choices[0] == q["answer"] and len(choices) > 1:
                choices[0], choices[1] = choices[1], choices[0]
            res = st.radio("Chọn đáp án:", choices, index=0, key=key)
            if res == q["answer"]: score_b2_ls += 1
        if st.button("Chấm điểm Bài 2", key="btn_b2_ls"):
            st.session_state.b2_current["b2_ls"] = (score_b2_ls, len(B2_QUIZ_LISTENING))
            save_progress()
            st.success(f"Bạn đúng {score_b2_ls}/{len(B2_QUIZ_LISTENING)} câu.")

    # 3. Điền vận mẫu
    with st.expander("Bài tập 3: Điền vận mẫu & thanh điệu", expanded=False):
        score_b2_fill = 0
        opts = ["...", "ā", "á", "ǎ", "à", "ē", "é", "ě", "è", "ǐ", "ǒ", "ù", "ái", "ǎi", "èi", "ǎo", "ǒu", "áng"]
        for i, q in enumerate(B2_QUIZ_FILL_BLANKS):
            key = f"b2_fill_q_{i}"
            res = st.selectbox(f"Chọn phần còn thiếu cho {q['q']} ({q['meaning']})", opts, index=0, key=key)
            if res == q["ans"]: score_b2_fill += 1
        if st.button("Chấm điểm Bài 3", key="btn_b2_fill"):
            st.session_state.b2_current["b2_fill"] = (score_b2_fill, len(B2_QUIZ_FILL_BLANKS))
            save_progress()
            st.success(f"Bạn đúng {score_b2_fill}/{len(B2_QUIZ_FILL_BLANKS)} câu.")

    # Tổng kết — chỉ hiện khi học viên đã chấm đủ 3 bài trong phiên này
    st.markdown("---")
    with st.expander("📊 Lịch sử & Tổng kết Bài 2", expanded=True):
        cur = st.session_state.b2_current
        labels_b2 = {"b2_vcb": "BT1: Từ vựng", "b2_ls": "BT2: Nghe", "b2_fill": "BT3: Điền âm"}
        missing_b2 = [v for k, v in labels_b2.items() if k not in cur]

        if missing_b2:
            st.warning(f"Chưa chấm điểm: {', '.join(missing_b2)}")
        else:
            b2_earned = sum(cur[k][0] for k in labels_b2.keys())
            b2_total  = sum(cur[k][1] for k in labels_b2.keys())
            b2_score_10 = round((b2_earned / b2_total) * 10, 2)
            st.success(f"📈 Kết quả Bài 2: **{b2_score_10} / 10** điểm")
            for k, lbl in labels_b2.items():
                s = cur[k]
                st.write(f"- {lbl}: {s[0]}/{s[1]}")

            st.markdown("---")
            name = st.text_input("Tên học viên (Bài 2)", key="student_name_b2")
            if st.button("Nộp bài tập Bài 2"):
                if name:
                    def fmt(k):
                        s = cur.get(k)
                        return f"{s[0]}/{s[1]}" if s else ""
                    row = {
                        "thời gian": datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S"), "học viên": name,
                        "tổng điểm": b2_score_10, "BT1: Từ vựng": fmt("b2_vcb"),
                        "BT2: Nghe": fmt("b2_ls"), "BT3: Điền âm": fmt("b2_fill")
                    }
                    if save_score_row_b2(row):
                        st.success("Đã lưu điểm Bài 2 thành công!")
                        st.session_state.b2_current = {}
                        st.rerun()
                else:
                    st.error("Vui lòng nhập tên học viên!")

        all_s2 = load_all_scores_b2()
        if all_s2: st.dataframe(all_s2, use_container_width=True)
