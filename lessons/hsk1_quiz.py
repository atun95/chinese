# -*- coding: utf-8 -*-
import streamlit as st
import random
import csv
from datetime import datetime, timezone, timedelta
from ui_utils import render_lesson_intro, render_play_button

# IMPORT ĐỀ QUIZ TỪ FILE DỮ LIỆU RIÊNG BIỆT
try:
    from hsk1_quizzes_data import QUIZZES_DATA
except ImportError:
    from lessons.hsk1_quizzes_data import QUIZZES_DATA


def show_hsk1_consolidated_quiz(save_progress, save_score_row_hsk1_consolidated, load_all_scores_hsk1_consolidated):
    # CSS Styles cao cấp, mô phỏng đúng thiết kế của ảnh người dùng gửi và tăng trải nghiệm premium
    st.markdown("""
    <style>
    /* Card Container */
    .quiz-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 24px;
        padding: 35px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
        margin-bottom: 25px;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Question Number */
    .quiz-q-num {
        font-size: 1.4rem;
        font-weight: 800;
        color: #e11d48;
        margin-bottom: 12px;
        font-family: 'Inter', sans-serif;
    }
    
    /* Question Text */
    .quiz-q-text {
        font-size: 1.25rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 8px;
        line-height: 1.45;
        font-family: 'Inter', sans-serif;
    }
    
    /* Pinyin Text */
    .quiz-q-pinyin {
        font-family: 'Courier New', monospace;
        font-size: 1.15rem;
        font-weight: bold;
        color: #2563eb;
        margin-bottom: 25px;
        background-color: #eff6ff;
        padding: 8px 16px;
        border-radius: 12px;
        display: inline-block;
        border: 1px solid #dbeafe;
    }
    
    /* Option Buttons Container */
    .quiz-option-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-bottom: 20px;
    }
    
    /* Styled Streamlit buttons inside container - EXACTLY like the image */
    .quiz-option-container div.stButton > button {
        background-color: #f3f4f6 !important;
        color: #1f2937 !important;
        border-radius: 24px !important;
        border: 1px solid transparent !important;
        padding: 20px 25px !important;
        font-size: 1.15rem !important;
        font-weight: 600 !important;
        text-align: left !important;
        align-items: center !important;
        justify-content: flex-start !important;
        width: 100% !important;
        display: flex !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.01) !important;
        transition: all 0.2s ease !important;
    }
    
    .quiz-option-container div.stButton > button:hover {
        background-color: #e5e7eb !important;
        border-color: #d1d5db !important;
        color: #000000 !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
    }
    
    /* Static Option Cards (for showing result) */
    .quiz-option-static {
        background-color: #f3f4f6;
        color: #1f2937;
        border-radius: 24px;
        padding: 20px 25px;
        font-size: 1.15rem;
        font-weight: 600;
        text-align: left;
        display: flex;
        align-items: center;
        border: 2px solid transparent;
        margin-bottom: 12px;
    }
    
    .quiz-option-static.correct {
        background-color: #f0fdf4;
        color: #14532d;
        border-color: #22c55e;
    }
    
    .quiz-option-static.incorrect {
        background-color: #fef2f2;
        color: #7f1d1d;
        border-color: #ef4444;
    }
    
    .quiz-option-static.normal {
        background-color: #f9fafb;
        color: #9ca3af;
        border-color: #e5e7eb;
        opacity: 0.65;
    }
    
    /* Selection Cards CSS */
    .quiz-selector-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px -1px rgba(0, 0, 0, 0.006);
        transition: all 0.3s ease;
        margin-bottom: 12px;
        position: relative;
        min-height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .quiz-selector-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 24px -5px rgba(0, 0, 0, 0.08);
        border-color: #cbd5e1;
    }
    .quiz-card-badge {
        position: absolute;
        top: 20px;
        right: 20px;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 700;
    }
    .quiz-card-icon {
        font-size: 2.2rem;
        margin-bottom: 12px;
        text-align: left;
    }
    .quiz-card-title {
        font-size: 1.15rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 8px;
        line-height: 1.35;
        text-align: left;
    }
    .quiz-card-desc {
        font-size: 0.88rem;
        color: #475569;
        line-height: 1.5;
        margin-bottom: 15px;
        text-align: left;
        flex-grow: 1;
    }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "📝 Hệ thống Đề Trắc nghiệm HSK 1"
    )

    # --- KHỞI TẠO STATE CHO QUIZ MỚI ---
    if "hsk1_active_quiz_id" not in st.session_state:
        st.session_state.hsk1_active_quiz_id = None
    if "hsk1_quiz_started" not in st.session_state:
        st.session_state.hsk1_quiz_started = False
    if "hsk1_quiz_idx" not in st.session_state:
        st.session_state.hsk1_quiz_idx = 0
    if "hsk1_quiz_answers" not in st.session_state:
        st.session_state.hsk1_quiz_answers = []
    if "hsk1_quiz_score" not in st.session_state:
        st.session_state.hsk1_quiz_score = 0
    if "hsk1_quiz_submitted" not in st.session_state:
        st.session_state.hsk1_quiz_submitted = False
    if "hsk1_quiz_shuffled_options" not in st.session_state:
        st.session_state.hsk1_quiz_shuffled_options = {}

    # ================= 1. GIAO DIỆN CHỌN ĐỀ (CHƯA BẮT ĐẦU HOẶC CHƯA CHỌN ĐỀ) =================
    if not st.session_state.hsk1_quiz_started or not st.session_state.hsk1_active_quiz_id:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 35px; margin-top: 10px;">
            <h2 style="color: #0f172a; font-weight: 800; font-size: 2.2rem; margin-bottom: 0;">📚 Lựa chọn Đề trắc nghiệm ôn tập</h2>
        </div>
        """, unsafe_allow_html=True)

        # Helper function to start a quiz
        def init_quiz_state(selected_quiz_key):
            questions = QUIZZES_DATA[selected_quiz_key]["questions"]
            st.session_state.hsk1_active_quiz_id = selected_quiz_key
            st.session_state.hsk1_quiz_started = True
            st.session_state.hsk1_quiz_idx = 0
            st.session_state.hsk1_quiz_answers = [None] * len(questions)
            st.session_state.hsk1_quiz_score = 0
            st.session_state.hsk1_quiz_submitted = False
            
            # Xáo trộn đáp án của đề
            shuffled = []
            for i, q in enumerate(questions):
                opts = q["choices"][:]
                random.Random(selected_quiz_key + str(i)).shuffle(opts)
                shuffled.append(opts)
            st.session_state.hsk1_quiz_shuffled_options[selected_quiz_key] = shuffled
            st.rerun()

        # Grid layout (Loop through 8 quizzes in pairs to create a clean responsive grid)
        quiz_metadata = {
            "quiz_1": {"badge": "Bài 1 - Bài 3", "badge_bg": "#dbeafe", "badge_color": "#1e40af", "icon": "🎒", "color": "#3b82f6", "title": "Đề 1: Nhập môn Ngữ âm & Từ vựng"},
            "quiz_2": {"badge": "Bài 4 - Bài 5", "badge_bg": "#f3e8ff", "badge_color": "#6b21a8", "icon": "🌸", "color": "#8b5cf6", "title": "Đề 2: Ngữ âm mở rộng & Số đếm"},
            "quiz_3": {"badge": "Bài 6 - Bài 7", "badge_bg": "#fce7f3", "badge_color": "#9d174d", "icon": "⚡", "color": "#ec4899", "title": "Đề 3: Từ để hỏi & Trợ từ 的"},
            "quiz_4": {"badge": "Bài 8 & Tổng hợp", "badge_bg": "#fef3c7", "badge_color": "#92400e", "icon": "🔥", "color": "#f59e0b", "title": "Đề 4: Chữ Hán & Đàm thoại tổng hợp"},
            "quiz_5": {"badge": "Bài 1 - Bài 3", "badge_bg": "#e0f2fe", "badge_color": "#0369a1", "icon": "📝", "color": "#0ea5e9", "title": "Đề 5: Luyện tập Ngữ âm & Giao tiếp"},
            "quiz_6": {"badge": "Bài 4 - Bài 5", "badge_bg": "#d1fae5", "badge_color": "#065f46", "icon": "📊", "color": "#10b981", "title": "Đề 6: Số đếm & Từ vựng Nữ giới"},
            "quiz_7": {"badge": "Bài 6 - Bài 7", "badge_bg": "#ffedd5", "badge_color": "#9a3412", "icon": "🔍", "color": "#f97316", "title": "Đề 7: Từ để hỏi & Định ngữ"},
            "quiz_8": {"badge": "Bài 8 & Tổng hợp", "badge_bg": "#e2e8f0", "badge_color": "#334155", "icon": "🏆", "color": "#64748b", "title": "Đề 8: Quy tắc bút thuận & Tổng hợp"}
        }

        keys = ["quiz_1", "quiz_2", "quiz_3", "quiz_4", "quiz_5", "quiz_6", "quiz_7", "quiz_8"]
        for row_idx in range(0, len(keys), 2):
            col1, col2 = st.columns(2)
            
            # Left Column Card
            k1 = keys[row_idx]
            meta1 = quiz_metadata[k1]
            with col1:
                st.markdown(f"""
                <div class="quiz-selector-card" style="border-top: 4px solid {meta1['color']};">
                    <div class="quiz-card-badge" style="background-color: {meta1['badge_bg']}; color: {meta1['badge_color']};">{meta1['badge']}</div>
                    <div class="quiz-card-icon">{meta1['icon']}</div>
                    <div class="quiz-card-title">{meta1['title']}</div>
                    <div class="quiz-card-desc">{QUIZZES_DATA[k1]['description']}</div>
                </div>
                """, unsafe_allow_html=True)
                if st.button("🚀 Bắt đầu làm bài", key=f"btn_start_{k1}", type="primary", use_container_width=True):
                    init_quiz_state(k1)
            
            # Right Column Card
            if row_idx + 1 < len(keys):
                k2 = keys[row_idx + 1]
                meta2 = quiz_metadata[k2]
                with col2:
                    st.markdown(f"""
                    <div class="quiz-selector-card" style="border-top: 4px solid {meta2['color']};">
                        <div class="quiz-card-badge" style="background-color: {meta2['badge_bg']}; color: {meta2['badge_color']};">{meta2['badge']}</div>
                        <div class="quiz-card-icon">{meta2['icon']}</div>
                        <div class="quiz-card-title">{meta2['title']}</div>
                        <div class="quiz-card-desc">{QUIZZES_DATA[k2]['description']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button("🚀 Bắt đầu làm bài", key=f"btn_start_{k2}", type="primary", use_container_width=True):
                        init_quiz_state(k2)

    # ================= 2. GIAO DIỆN LÀM BÀI =================
    else:
        active_key = st.session_state.hsk1_active_quiz_id
        quiz_info = QUIZZES_DATA[active_key]
        questions = quiz_info["questions"]
        current_idx = st.session_state.hsk1_quiz_idx

        # Nút Quay lại chọn đề (chỉ khi chưa hoàn thành hoặc muốn đổi)
        if st.sidebar.button("🔙 Chọn đề thi khác", use_container_width=True):
            st.session_state.hsk1_quiz_started = False
            st.session_state.hsk1_active_quiz_id = None
            st.rerun()

        # Khôi phục shuffled options nếu bị mất do hot reload / restart
        if active_key not in st.session_state.hsk1_quiz_shuffled_options:
            shuffled = []
            for i, q in enumerate(questions):
                opts = q["choices"][:]
                random.Random(active_key + str(i)).shuffle(opts)
                shuffled.append(opts)
            st.session_state.hsk1_quiz_shuffled_options[active_key] = shuffled

        # Khôi phục answers list nếu bị trống hoặc lệch độ dài
        if not st.session_state.hsk1_quiz_answers or len(st.session_state.hsk1_quiz_answers) != len(questions):
            st.session_state.hsk1_quiz_answers = [None] * len(questions)

        # Nếu hoàn thành tất cả câu hỏi
        if current_idx >= len(questions):
            show_quiz_results(active_key, questions, save_progress, save_score_row_hsk1_consolidated, load_all_scores_hsk1_consolidated)
            return

        q_data = questions[current_idx]
        shuffled_choices = st.session_state.hsk1_quiz_shuffled_options[active_key][current_idx]
        correct_choice = q_data["answer"]
        user_choice = st.session_state.hsk1_quiz_answers[current_idx]
        is_answered = (user_choice is not None)

        # Thanh tiến độ và số câu hỏi
        percent_done = int((current_idx / len(questions)) * 100)
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; font-weight: bold; color: #475569; margin-bottom: 8px; font-size: 0.95rem;">
            <span>{quiz_info['title']}</span>
            <span>Câu {current_idx + 1} / {len(questions)} ({percent_done}%)</span>
        </div>
        """, unsafe_allow_html=True)
        st.progress(current_idx / len(questions))

        # Khung thẻ câu hỏi chuẩn giao diện
        st.markdown(f"""
        <div class="quiz-card">
            <div class="quiz-q-num">Câu hỏi {current_idx + 1}</div>
            <div class="quiz-q-text">{q_data['question']}</div>
        </div>
        """, unsafe_allow_html=True)

        # Phát âm câu mẫu
        col_audio, col_empty = st.columns([4, 6])
        with col_audio:
            render_play_button(q_data["sound_txt"], "🔊 Phát âm câu hỏi mẫu", key=f"audio_q_{active_key}_{current_idx}")
        st.markdown("<br/>", unsafe_allow_html=True)

        # ================= 2.1 TRẠNG THÁI: CHƯA TRẢ LỜI =================
        if not is_answered:
            st.markdown('<div class="quiz-option-container">', unsafe_allow_html=True)
            for i, choice in enumerate(shuffled_choices):
                if st.button(choice, key=f"btn_choice_{active_key}_{i}_{current_idx}", use_container_width=True):
                    st.session_state.hsk1_quiz_answers[current_idx] = choice
                    if choice == correct_choice:
                        st.session_state.hsk1_quiz_score += 1
                    save_progress()
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        # ================= 2.2 TRẠNG THÁI: ĐÃ TRẢ LỜI =================
        else:
            # Hiển thị các block đáp án tĩnh, tô màu chuẩn
            static_options_html = '<div class="quiz-option-container">'
            for choice in shuffled_choices:
                if choice == correct_choice:
                    static_options_html += f'<div class="quiz-option-static correct">✅ {choice}</div>'
                elif choice == user_choice:
                    static_options_html += f'<div class="quiz-option-static incorrect">❌ {choice}</div>'
                else:
                    static_options_html += f'<div class="quiz-option-static normal">{choice}</div>'
            static_options_html += '</div>'
            st.markdown(static_options_html, unsafe_allow_html=True)

            # Khung thông báo và giải thích kết quả
            if user_choice == correct_choice:
                st.success(f"🎉 **Chính xác!**\n\n**Giải thích:** {q_data['explain']}")
            else:
                st.error(f"😢 **Chưa chính xác!** (Bạn đã chọn: {user_choice})\n\n👉 Đáp án đúng là: **{correct_choice}**\n\n**Giải thích:** {q_data['explain']}")

            # Điều hướng
            st.markdown("<br/>", unsafe_allow_html=True)
            col_nav_1, col_nav_2 = st.columns([1, 1])
            with col_nav_1:
                if current_idx > 0:
                    if st.button("⬅️ Câu trước đó", use_container_width=True):
                        st.session_state.hsk1_quiz_idx -= 1
                        st.rerun()
            with col_nav_2:
                btn_label = "Xem kết quả tổng kết 📊" if current_idx == len(questions) - 1 else "Câu tiếp theo ➡️"
                if st.button(btn_label, type="primary", use_container_width=True):
                    st.session_state.hsk1_quiz_idx += 1
                    st.rerun()


def show_quiz_results(active_key, questions, save_progress, save_score_row_hsk1_consolidated, load_all_scores_hsk1_consolidated):
    score = st.session_state.hsk1_quiz_score
    total = len(questions)
    final_score_10 = round((score / total) * 10, 2)
    quiz_title = QUIZZES_DATA[active_key]["title"]

    st.balloons()
    st.markdown(f"""
    <div style="background-color: #fff; border: 2px solid #22c55e; border-radius: 20px; padding: 40px; text-align: center; max-width: 600px; margin: 30px auto; box-shadow: 0 10px 25px rgba(0,0,0,0.05);">
        <span style="font-size: 4rem;">🏆</span>
        <h2 style="color: #1e3a8a; margin-top: 15px; font-weight: 800;">Hoàn thành bài thi!</h2>
        <p style="font-size: 1.1rem; color: #475569; margin-bottom: 25px;">Bạn đã hoàn thành <b>{quiz_title}</b></p>
        <div style="background-color: #f0fdf4; border-radius: 12px; padding: 20px; display: inline-block; margin-bottom: 10px;">
            <span style="font-size: 1.1rem; color: #166534; font-weight: bold; display: block;">KẾT QUẢ ĐẠT ĐƯỢC:</span>
            <span style="font-size: 3rem; color: #15803d; font-weight: 900;">{score} / {total}</span>
            <span style="font-size: 1.3rem; color: #15803d; font-weight: 700; display: block; margin-top: 5px;">({final_score_10} điểm hệ 10)</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Form nộp bài lên data backend (lưu ở CSV)
    if not st.session_state.hsk1_quiz_submitted:
        name = st.text_input("Nhập họ và tên học viên để nộp điểm lên data backend:", placeholder="Ví dụ: Nguyễn Văn A", key="hsk1_quiz_student_name")
        if st.button("💾 Nộp bài & Lưu điểm lên hệ thống", type="primary", use_container_width=True):
            if name:
                row = {
                    "thời gian": datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S"),
                    "học viên": name,
                    "Đề kiểm tra": quiz_title,
                    "tổng điểm": final_score_10,
                    "Kết quả": f"{score}/{total}"
                }
                if save_score_row_hsk1_consolidated(row):
                    st.session_state.hsk1_quiz_submitted = True
                    st.success("Đã nộp bài và lưu điểm số vào data backend thành công!")
                    save_progress()
                    st.rerun()
            else:
                st.error("Vui lòng điền tên trước khi bấm nộp bài!")
    else:
        st.success("Chúc mừng bạn đã nộp bài thành công lên hệ thống data backend!")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔄 Làm lại đề này", use_container_width=True):
            st.session_state.hsk1_quiz_idx = 0
            st.session_state.hsk1_quiz_answers = [None] * len(questions)
            st.session_state.hsk1_quiz_score = 0
            st.session_state.hsk1_quiz_submitted = False
            save_progress()
            st.rerun()
    with col2:
        if st.button("🔙 Trở về danh sách đề thi", use_container_width=True):
            st.session_state.hsk1_quiz_started = False
            st.session_state.hsk1_active_quiz_id = None
            save_progress()
            st.rerun()

    # Bảng xếp hạng nộp bài
    st.markdown("---")
    st.markdown("### 🏆 Bảng xếp hạng nộp bài trắc nghiệm HSK 1")
    all_scores = load_all_scores_hsk1_consolidated()
    if all_scores:
        st.dataframe(all_scores, use_container_width=True)
    else:
        st.info("Chưa có lượt nộp điểm nào cho các đề. Hãy nộp điểm đầu tiên!")
