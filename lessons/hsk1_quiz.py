# -*- coding: utf-8 -*-
import streamlit as st
import random
import csv
from datetime import datetime, timezone, timedelta
from ui_utils import render_lesson_intro, render_play_button

# IMPORT SUPABASE CLIENT
try:
    import supabase_client
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parent.parent))
    import supabase_client

# IMPORT ĐỀ QUIZ TỪ FILE DỮ LIỆU RIÊNG BIỆT
try:
    from hsk1_quizzes_data import QUIZZES_DATA
except ImportError:
    from lessons.hsk1_quizzes_data import QUIZZES_DATA


def show_hsk1_consolidated_quiz(save_progress, save_score_row_hsk1_consolidated, load_all_scores_hsk1_consolidated):
    # CSS Styles cao cấp
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
        color: #2563eb;
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
    
    /* Styled Streamlit buttons inside container */
    .quiz-option-container div.stButton > button {
        background-color: #f8fafc !important;
        color: #1f2937 !important;
        border-radius: 20px !important;
        border: 1.5px solid #e2e8f0 !important;
        padding: 18px 24px !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        text-align: left !important;
        align-items: center !important;
        justify-content: flex-start !important;
        width: 100% !important;
        display: flex !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02) !important;
        transition: all 0.2s ease !important;
    }
    
    .quiz-option-container div.stButton > button:hover {
        background-color: #f1f5f9 !important;
        border-color: #cbd5e1 !important;
        color: #0f172a !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 10px rgba(0,0,0,0.06) !important;
    }
    
    /* Static Option Cards (for showing result) */
    .quiz-option-static {
        background-color: #f8fafc;
        color: #1f2937;
        border-radius: 20px;
        padding: 18px 24px;
        font-size: 1.1rem;
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
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro("📝 Trắc nghiệm Tổng hợp HSK 1 - Ôn tập bài cũ")

    # Đề thi mặc định cho toàn bộ phần này là quiz_exam_50
    active_key = "quiz_exam_50"

    # --- KHỞI TẠO STATE ---
    if "hsk1_active_quiz_id" not in st.session_state:
        st.session_state.hsk1_active_quiz_id = active_key
    else:
        st.session_state.hsk1_active_quiz_id = active_key

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

    quiz_info = QUIZZES_DATA.get(active_key)
    if not quiz_info:
        st.error("Không tìm thấy dữ liệu đề ôn tập bài cũ!")
        return

    questions = quiz_info["questions"]

    # Hàm khởi tạo / làm lại bài thi
    def start_new_quiz():
        st.session_state.hsk1_active_quiz_id = active_key
        st.session_state.hsk1_quiz_started = True
        st.session_state.hsk1_quiz_idx = 0
        st.session_state.hsk1_quiz_answers = [None] * len(questions)
        st.session_state.hsk1_quiz_score = 0
        st.session_state.hsk1_quiz_submitted = False
        
        # Xáo trộn đáp án
        shuffled = []
        for i, q in enumerate(questions):
            opts = q["choices"][:]
            random.Random(active_key + str(i)).shuffle(opts)
            shuffled.append(opts)
        st.session_state.hsk1_quiz_shuffled_options[active_key] = shuffled

    # ================= 1. GIAO DIỆN CHƯA BẮT ĐẦU =================
    if not st.session_state.hsk1_quiz_started:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border-radius: 24px; padding: 32px 36px; color: white; margin-bottom: 25px; box-shadow: 0 10px 25px rgba(15, 23, 42, 0.2); border: 2px solid #3b82f6;">
            <div style="font-size: 2.4rem; margin-bottom: 10px;">📝</div>
            <h2 style="color: #60a5fa; font-size: 1.65rem; font-weight: 800; margin-bottom: 10px;">ÔN TẬP BÀI CŨ (50 CÂU)</h2>
            <p style="color: #cbd5e1; font-size: 1rem; line-height: 1.65; margin-bottom: 0;">
                Bài ôn tập trắc nghiệm toàn diện gồm <b>50 câu hỏi</b> bao quát 7 dạng bài cốt lõi: Ngữ âm & Biến điệu, Chữ Hán & Bộ thủ, Từ vựng cơ bản, Ngữ pháp (的, 在, 去, 不/没, 有点儿/一点儿), Lượng từ & Số từ, Tìm lỗi sai, Sắp xếp câu hoàn chỉnh, và Đối thoại giao tiếp phản xạ.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🚀 BẮT ĐẦU LÀM BÀI ÔN TẬP (50 CÂU)", key="btn_start_quiz_50", type="primary", use_container_width=True):
            start_new_quiz()
            save_progress()
            st.rerun()

        # Bảng xếp hạng điểm học viên
        st.markdown("---")
        st.markdown("### 🏆 Bảng xếp hạng nộp bài")
        scores_data = []
        if supabase_client.is_supabase_configured():
            scores_data = supabase_client.load_scores_from_supabase()
        if not scores_data:
            raw_csv = load_all_scores_hsk1_consolidated()
            for r in raw_csv:
                scores_data.append({
                    "Thời gian": r.get("thời gian", ""),
                    "Học viên": r.get("học viên", ""),
                    "Điểm": r.get("Kết quả") or r.get("tổng điểm", "")
                })

        if scores_data:
            st.dataframe(scores_data, use_container_width=True)
        else:
            st.info("Chưa có lượt nộp điểm nào. Hãy bấm bắt đầu để làm bài ôn tập và lưu điểm!")

    # ================= 2. GIAO DIỆN LÀM BÀI =================
    else:
        current_idx = st.session_state.hsk1_quiz_idx

        # Nút sidebar: Làm lại bài từ đầu
        if st.sidebar.button("🔄 Làm lại từ đầu", use_container_width=True):
            start_new_quiz()
            save_progress()
            st.rerun()

        # Khôi phục shuffled options nếu cần
        if active_key not in st.session_state.hsk1_quiz_shuffled_options:
            shuffled = []
            for i, q in enumerate(questions):
                opts = q["choices"][:]
                random.Random(active_key + str(i)).shuffle(opts)
                shuffled.append(opts)
            st.session_state.hsk1_quiz_shuffled_options[active_key] = shuffled

        # Khôi phục answers list nếu bị lệch độ dài
        if not st.session_state.hsk1_quiz_answers or len(st.session_state.hsk1_quiz_answers) != len(questions):
            st.session_state.hsk1_quiz_answers = [None] * len(questions)

        # Nếu đã hoàn thành tất cả câu hỏi
        if current_idx >= len(questions):
            show_quiz_results(questions, save_progress, save_score_row_hsk1_consolidated, load_all_scores_hsk1_consolidated)
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
            <span>📝 Ôn tập bài cũ (50 câu)</span>
            <span>Câu {current_idx + 1} / {len(questions)} ({percent_done}%)</span>
        </div>
        """, unsafe_allow_html=True)
        st.progress(current_idx / len(questions))

        # Khung thẻ câu hỏi
        st.markdown(f"""
        <div class="quiz-card">
            <div class="quiz-q-num">Câu hỏi {current_idx + 1} / {len(questions)}</div>
            <div class="quiz-q-text">{q_data['question']}</div>
        </div>
        """, unsafe_allow_html=True)

        # Phát âm câu hỏi mẫu
        col_audio, col_empty = st.columns([4, 6])
        with col_audio:
            render_play_button(q_data["sound_txt"], "🔊 Phát âm câu hỏi mẫu", key=f"audio_q_{active_key}_{current_idx}")
        st.markdown("<br/>", unsafe_allow_html=True)

        # Trạng thái: Chưa trả lời
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

        # Trạng thái: Đã trả lời
        else:
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

            # Giải thích kết quả
            if user_choice == correct_choice:
                st.success(f"🎉 **Chính xác!**\n\n**Giải thích:** {q_data['explain']}")
            else:
                st.error(f"😢 **Chưa chính xác!** (Bạn đã chọn: {user_choice})\n\n👉 Đáp án đúng là: **{correct_choice}**\n\n**Giải thích:** {q_data['explain']}")

            # Điều hướng câu hỏi
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


def show_quiz_results(questions, save_progress, save_score_row_hsk1_consolidated, load_all_scores_hsk1_consolidated):
    score = st.session_state.hsk1_quiz_score
    total = len(questions)
    score_display = f"{score}/{total}"
    quiz_title = "Ôn tập bài cũ (50 câu)"

    st.balloons()
    st.markdown(f"""
    <div style="background-color: #fff; border: 2px solid #22c55e; border-radius: 20px; padding: 35px; text-align: center; max-width: 650px; margin: 25px auto; box-shadow: 0 10px 25px rgba(0,0,0,0.05);">
        <span style="font-size: 3.5rem;">🏆</span>
        <h2 style="color: #1e3a8a; margin-top: 10px; font-weight: 800; font-size: 1.8rem;">Hoàn thành bài ôn tập!</h2>
        <p style="font-size: 1.05rem; color: #475569; margin-bottom: 20px;">Bạn đã hoàn thành <b>{quiz_title}</b></p>
        <div style="background-color: #f0fdf4; border-radius: 16px; padding: 20px 35px; display: inline-block; margin-bottom: 10px; border: 1.5px solid #86efac;">
            <span style="font-size: 1.05rem; color: #166534; font-weight: bold; display: block;">KẾT QUẢ ĐẠT ĐƯỢC:</span>
            <span style="font-size: 3.5rem; color: #15803d; font-weight: 900; letter-spacing: 1px;">{score_display}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Mục BẮT BUỘC nhập tên học viên để lưu điểm
    if not st.session_state.hsk1_quiz_submitted:
        st.markdown(f"""
        <div style="background-color: #eff6ff; border: 2px dashed #3b82f6; border-radius: 18px; padding: 22px 26px; margin: 20px auto; max-width: 650px;">
            <h4 style="color: #1e40af; margin-top: 0; font-size: 1.2rem; font-weight: 800;">✍️ Bắt buộc nhập tên học viên để lưu điểm</h4>
            <p style="color: #475569; margin-bottom: 5px; font-size: 0.95rem;">Hệ thống sẽ ghi nhận <b>Họ tên học viên</b> và kết quả <b>{score_display}</b> trực tiếp lên cơ sở dữ liệu Supabase.</p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("form_submit_student_score"):
            name = st.text_input("Nhập họ và tên học viên * :", placeholder="Ví dụ: Nguyễn Văn A", key="hsk1_quiz_student_name")
            submitted = st.form_submit_button("💾 Nộp bài & Lưu điểm lên Supabase", type="primary", use_container_width=True)

            if submitted:
                clean_name = name.strip() if name else ""
                if clean_name:
                    now_str = datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S")

                    # 1. Lưu lên Supabase: Chỉ lưu tên và điểm (câu đúng/50)
                    saved_sb, msg_sb = supabase_client.save_score_to_supabase(
                        student_name=clean_name,
                        score_str=score_display
                    )

                    # 2. Lưu dự phòng vào CSV cục bộ
                    row_csv = {
                        "thời gian": now_str,
                        "học viên": clean_name,
                        "Đề kiểm tra": quiz_title,
                        "tổng điểm": score_display,
                        "Kết quả": score_display
                    }
                    save_score_row_hsk1_consolidated(row_csv)

                    st.session_state.hsk1_quiz_submitted = True
                    st.session_state.submitted_student_name = clean_name
                    save_progress()

                    if saved_sb:
                        st.success(f"🎉 Đã lưu điểm thành công! Học viên: **{clean_name}** — Điểm: **{score_display}**")
                    else:
                        st.warning(f"Đã lưu điểm vào CSV cục bộ. (Thông báo Supabase: {msg_sb})")
                    st.rerun()
                else:
                    st.error("⚠️ Bạn bắt buộc phải nhập họ và tên học viên trước khi bấm nộp bài!")
    else:
        saved_name = st.session_state.get("submitted_student_name", "")
        st.success(f"✅ Đã lưu điểm thành công cho học viên: **{saved_name}** — Điểm số: **{score_display}**")

    # Nút làm lại bài
    if st.button("🔄 Làm lại bài ôn tập", use_container_width=True, type="secondary"):
        st.session_state.hsk1_quiz_idx = 0
        st.session_state.hsk1_quiz_answers = [None] * len(questions)
        st.session_state.hsk1_quiz_score = 0
        st.session_state.hsk1_quiz_submitted = False
        save_progress()
        st.rerun()

    # Bảng xếp hạng nộp bài
    st.markdown("---")
    st.markdown("### 🏆 Bảng xếp hạng nộp bài")
    scores_data = []
    if supabase_client.is_supabase_configured():
        scores_data = supabase_client.load_scores_from_supabase()
    if not scores_data:
        raw_csv = load_all_scores_hsk1_consolidated()
        for r in raw_csv:
            scores_data.append({
                "Thời gian": r.get("thời gian", ""),
                "Học viên": r.get("học viên", ""),
                "Điểm": r.get("Kết quả") or r.get("tổng điểm", "")
            })

    if scores_data:
        st.dataframe(scores_data, use_container_width=True)
    else:
        st.info("Chưa có lượt nộp điểm nào. Hãy nộp điểm đầu tiên!")
