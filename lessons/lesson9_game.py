import streamlit as st
import random
import json
import textwrap
from ui_utils import render_play_button

try:
    from lessons.lessons_data import B9_1_QUOC_GIA, B9_1_QUOC_TICH, B9_1_TIEN_TE
except ImportError:
    from lessons_data import B9_1_QUOC_GIA, B9_1_QUOC_TICH, B9_1_TIEN_TE

# Currency to Country mapping for rich questions
CURRENCY_DETAILS = [
    {
        "hanzi": "人民币", "pinyin": "Rénmínbì", "meaning": "Nhân dân tệ",
        "country": "Trung Quốc", "country_hanzi": "中国", "flag": "cn",
        "note": "Đơn vị tiền tệ chính thức của Cộng hòa Nhân dân Trung Hoa."
    },
    {
        "hanzi": "元", "pinyin": "yuán", "meaning": "Đồng/Nguyên (văn viết)",
        "country": "Trung Quốc", "country_hanzi": "中国", "flag": "cn",
        "note": "Dùng trong văn viết, báo chí, hóa đơn hoặc niêm yết giá chính thức."
    },
    {
        "hanzi": "块", "pinyin": "kuài", "meaning": "Tệ/Đồng (khẩu ngữ)",
        "country": "Trung Quốc", "country_hanzi": "中国", "flag": "cn",
        "note": "Rất phổ biến trong khẩu ngữ giao tiếp hàng ngày khi mua bán."
    },
    {
        "hanzi": "越南盾", "pinyin": "Yuènán dùn", "meaning": "Đồng Việt Nam",
        "country": "Việt Nam", "country_hanzi": "越南", "flag": "vn",
        "note": "Đơn vị tiền tệ chính thức của Việt Nam."
    },
    {
        "hanzi": "美元", "pinyin": "Měiyuán", "meaning": "Đô la Mỹ (USD)",
        "country": "Mỹ", "country_hanzi": "美国", "flag": "us",
        "note": "Đồng tiền quốc tế thông dụng của Hoa Kỳ."
    },
    {
        "hanzi": "欧元", "pinyin": "Ōuyuán", "meaning": "Euro (EUR)",
        "country": "Châu Âu (Pháp, Đức, Ý...)", "country_hanzi": "欧洲", "flag": "eu",
        "note": "Đồng tiền chung của nhiều quốc gia thuộc Liên minh Châu Âu."
    },
    {
        "hanzi": "日元", "pinyin": "Rìyuán", "meaning": "Yên Nhật (JPY)",
        "country": "Nhật Bản", "country_hanzi": "日本", "flag": "jp",
        "note": "Đơn vị tiền tệ chính thức của Nhật Bản."
    },
    {
        "hanzi": "英镑", "pinyin": "Yīngbàng", "meaning": "Bảng Anh (GBP)",
        "country": "Anh", "country_hanzi": "英国", "flag": "gb",
        "note": "Đơn vị tiền tệ của Vương quốc Anh."
    },
    {
        "hanzi": "韩元", "pinyin": "Hányuán", "meaning": "Won Hàn Quốc (KRW)",
        "country": "Hàn Quốc", "country_hanzi": "韩国", "flag": "kr",
        "note": "Đơn vị tiền tệ của Hàn Quốc."
    }
]

def generate_questions(mode="mix", num_q=10):
    """Tạo bộ câu hỏi ngẫu nhiên và đa dạng theo chế độ chơi"""
    questions = []
    
    # --- Dạng 1: Flag -> Country Name ---
    def create_flag_q(country):
        flag_code = country.get("FlagCode", "un")
        other_countries = [c for c in B9_1_QUOC_GIA if c["Chữ Hán"] != country["Chữ Hán"]]
        distractors = random.sample(other_countries, 3)
        options = [country] + distractors
        random.shuffle(options)
        correct_idx = options.index(country)
        
        return {
            "type": "flag",
            "title": "🚩 Nhìn quốc kỳ - Chọn tên quốc gia",
            "prompt": "Lá cờ dưới đây là của quốc gia nào trong tiếng Trung?",
            "flag_code": flag_code,
            "audio_text": country["Chữ Hán"],
            "options": [f"{opt['Chữ Hán']} ({opt['Pinyin']}) — {opt['Nghĩa tiếng Việt']}" for opt in options],
            "correct_idx": correct_idx,
            "correct_item": country,
            "explanation": f"Quốc kỳ: <b>{country['Nghĩa tiếng Việt']}</b>. Tên tiếng Trung là <b>{country['Chữ Hán']}</b> ({country['Pinyin']}).",
            "example": f"Mẫu câu: 我来自{country['Chữ Hán']}。(Wǒ láizì {country['Pinyin']}. — Tôi đến từ {country['Nghĩa tiếng Việt']}.)"
        }

    # --- Dạng 2: Country -> Nationality ---
    def create_nationality_q(nat):
        flag_code = nat.get("FlagCode", "un")
        other_nats = [n for n in B9_1_QUOC_TICH if n["Chữ Hán"] != nat["Chữ Hán"]]
        distractors = random.sample(other_nats, 3)
        options = [nat] + distractors
        random.shuffle(options)
        correct_idx = options.index(nat)
        country_vn = nat["Nghĩa tiếng Việt"].replace("Người ", "")
        
        return {
            "type": "nationality",
            "title": "🧑‍🤝‍🧑 Phản xạ Quốc tịch (国籍)",
            "prompt": f"Người mang quốc tịch <b>{country_vn}</b> trong tiếng Trung gọi là gì?",
            "flag_code": flag_code,
            "audio_text": nat["Chữ Hán"],
            "options": [f"{opt['Chữ Hán']} ({opt['Pinyin']}) — {opt['Nghĩa tiếng Việt']}" for opt in options],
            "correct_idx": correct_idx,
            "correct_item": nat,
            "explanation": f"Công thức tạo quốc tịch: <b>Tên quốc gia + 人 (rén)</b>. Do đó: <b>{nat['Chữ Hán']}</b> ({nat['Pinyin']}) = {nat['Nghĩa tiếng Việt']}.",
            "example": f"Mẫu câu: 他是{nat['Chữ Hán']}。(Tā shì {nat['Pinyin']}. — Anh ấy là {nat['Nghĩa tiếng Việt']}.)"
        }

    # --- Dạng 3: Currency Match ---
    def create_currency_q(curr):
        other_currs = [c for c in CURRENCY_DETAILS if c["hanzi"] != curr["hanzi"]]
        distractors = random.sample(other_currs, 3)
        options = [curr] + distractors
        random.shuffle(options)
        
        q_type = random.choice(["curr_to_country", "name_to_curr"])
        if q_type == "curr_to_country":
            prompt = f"Loại tiền tệ <b>{curr['hanzi']}</b> ({curr['pinyin']} - {curr['meaning']}) được sử dụng chủ yếu tại đâu?"
            opts = [f"{opt['country']} ({opt['country_hanzi']})" for opt in options]
            correct_text = f"{curr['country']} ({curr['country_hanzi']})"
            correct_idx = opts.index(correct_text)
            audio_text = curr['hanzi']
        else:
            prompt = f"Tiền tệ của <b>{curr['country']}</b> ({curr['meaning']}) trong tiếng Trung gọi là gì?"
            opts = [f"{opt['hanzi']} ({opt['pinyin']}) — {opt['meaning']}" for opt in options]
            correct_idx = options.index(curr)
            audio_text = curr['hanzi']

        return {
            "type": "currency",
            "title": "💵 Thử tài Tiền tệ (货币)",
            "prompt": prompt,
            "flag_code": curr.get("flag", "un"),
            "audio_text": audio_text,
            "options": opts,
            "correct_idx": correct_idx,
            "correct_item": curr,
            "explanation": f"<b>{curr['hanzi']}</b> ({curr['pinyin']}): {curr['meaning']}. {curr['note']}",
            "example": f"Mẫu câu: 这是{curr['hanzi']}。(Zhè shì {curr['pinyin']}. — Đây là {curr['meaning']}.)"
        }

    # --- Dạng 4: Dialogue / Sentence Reflex ---
    def create_dialogue_q():
        sample_countries = random.sample(B9_1_QUOC_TICH, 4)
        target = sample_countries[0]
        options = [
            f"我是{opt['Chữ Hán']}。(Wǒ shì {opt['Pinyin']}.)"
            for opt in sample_countries
        ]
        combined = list(enumerate(options))
        random.shuffle(combined)
        shuffled_opts = [item[1] for item in combined]
        correct_idx = [i for i, item in enumerate(combined) if item[0] == 0][0]

        return {
            "type": "sentence",
            "title": "🗣️ Giao tiếp phản xạ: Hỏi quốc tịch",
            "prompt": f"Khi người khác hỏi: <b>“你是哪国人？”</b> (Nǐ shì nǎ guórén? — Bạn là người nước nào?), nếu bạn là <b>{target['Nghĩa tiếng Việt']}</b>, bạn sẽ trả lời câu nào?",
            "flag_code": target.get("FlagCode", "un"),
            "audio_text": f"我是{target['Chữ Hán']}",
            "options": shuffled_opts,
            "correct_idx": correct_idx,
            "correct_item": target,
            "explanation": f"Trả lời đầy đủ: <b>我是{target['Chữ Hán']}。</b> (Wǒ shì {target['Pinyin']}. — Tôi là {target['Nghĩa tiếng Việt']}.)",
            "example": "Cấu trúc: 我是 + [Tên quốc gia] + 人。"
        }

    # Collect questions according to mode
    if mode == "flag":
        sampled = random.sample(B9_1_QUOC_GIA, min(num_q, len(B9_1_QUOC_GIA)))
        questions = [create_flag_q(c) for c in sampled]
    elif mode == "nationality":
        sampled = random.sample(B9_1_QUOC_TICH, min(num_q, len(B9_1_QUOC_TICH)))
        questions = [create_nationality_q(n) for n in sampled]
    elif mode == "currency":
        sampled = random.choices(CURRENCY_DETAILS, k=num_q)
        questions = [create_currency_q(c) for c in sampled]
    else:  # mix mode
        flag_samples = random.sample(B9_1_QUOC_GIA, k=max(2, num_q // 3))
        nat_samples = random.sample(B9_1_QUOC_TICH, k=max(2, num_q // 3))
        curr_samples = random.sample(CURRENCY_DETAILS, k=max(2, num_q // 4))
        
        q_pool = [create_flag_q(c) for c in flag_samples]
        q_pool += [create_nationality_q(n) for n in nat_samples]
        q_pool += [create_currency_q(c) for c in curr_samples]
        q_pool.append(create_dialogue_q())
        q_pool.append(create_dialogue_q())
        
        random.shuffle(q_pool)
        questions = q_pool[:num_q]

    return questions

def render_lesson9_1_game():
    """Giao diện chính của Trò chơi Ôn tập Bài 9.1"""
    
    st.html("""
    <style>
    .game-hero {
        background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 50%, #4f46e5 100%);
        border-radius: 18px;
        padding: 24px 28px;
        color: white;
        margin-bottom: 22px;
        box-shadow: 0 10px 30px rgba(37, 99, 235, 0.2);
    }
    .stat-pill {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.25);
        border-radius: 12px;
        padding: 8px 16px;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-weight: 700;
        font-size: 0.95rem;
    }
    .q-card {
        background: #ffffff;
        border: 2px solid #e2e8f0;
        border-radius: 18px;
        padding: 24px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.06);
        margin-bottom: 20px;
    }
    .flag-display {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 16px;
        background: #f8fafc;
        border-radius: 14px;
        border: 1px dashed #cbd5e1;
        margin-bottom: 18px;
    }
    .flag-img-lg {
        width: 120px;
        height: auto;
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.18);
        border: 1px solid #e2e8f0;
        transition: transform 0.2s ease;
    }
    .flag-img-lg:hover {
        transform: scale(1.05);
    }
    .streak-badge {
        background: linear-gradient(135deg, #f97316, #ef4444);
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 800;
        font-size: 0.85rem;
        display: inline-block;
        box-shadow: 0 2px 8px rgba(239, 68, 68, 0.3);
    }
    .feedback-box-correct {
        background: #f0fdf4;
        border: 2px solid #22c55e;
        border-radius: 14px;
        padding: 16px 20px;
        margin-top: 18px;
    }
    .feedback-box-wrong {
        background: #fef2f2;
        border: 2px solid #ef4444;
        border-radius: 14px;
        padding: 16px 20px;
        margin-top: 18px;
    }
    .mini-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 14px 10px;
        text-align: center;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
        margin-bottom: 8px;
    }
    .mini-card:hover {
        border-color: #3b82f6;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.12);
    }
    </style>
    """)

    # Khởi tạo session state
    if "b91_mode" not in st.session_state:
        st.session_state.b91_mode = "mix"
    if "b91_num_q" not in st.session_state:
        st.session_state.b91_num_q = 10
    if "b91_questions" not in st.session_state:
        st.session_state.b91_questions = generate_questions(st.session_state.b91_mode, st.session_state.b91_num_q)
    if "b91_idx" not in st.session_state:
        st.session_state.b91_idx = 0
    if "b91_score" not in st.session_state:
        st.session_state.b91_score = 0
    if "b91_streak" not in st.session_state:
        st.session_state.b91_streak = 0
    if "b91_max_streak" not in st.session_state:
        st.session_state.b91_max_streak = 0
    if "b91_answered" not in st.session_state:
        st.session_state.b91_answered = False
    if "b91_selected" not in st.session_state:
        st.session_state.b91_selected = None
    if "b91_history" not in st.session_state:
        st.session_state.b91_history = []
    if "b91_game_over" not in st.session_state:
        st.session_state.b91_game_over = False

    # Tabs trong khu vực Game
    subtab_arena, subtab_flashcards, subtab_wheel = st.tabs([
        "🏆 Đấu Trường Phản Xạ (Quiz Arena)",
        "🎴 Thẻ Lật Ôn Nhanh (Flashcards)",
        "🎲 Vòng Quay Gọi Tên (Classroom Call)"
    ])

    # =========================================================================
    # TAB 1: ĐẤU TRƯỜNG PHẢN XẠ (QUIZ ARENA)
    # =========================================================================
    with subtab_arena:
        # Thanh cài đặt ván chơi
        ctrl_col1, ctrl_col2, ctrl_col3 = st.columns([2, 1, 1])
        with ctrl_col1:
            mode_options = {
                "mix": "⚡ Đấu trường Tổng hợp (All-in-one)",
                "flag": "🚩 Đoán Quốc kỳ (Flags Only)",
                "nationality": "🧑‍🤝‍🧑 Phản xạ Quốc tịch (Nationalities)",
                "currency": "💵 Thử tài Tiền tệ (Currencies)"
            }
            chosen_mode = st.selectbox(
                "🎯 Chọn chế độ chơi:",
                list(mode_options.keys()),
                format_func=lambda k: mode_options[k],
                index=list(mode_options.keys()).index(st.session_state.b91_mode),
                key="b91_mode_selector"
            )
        with ctrl_col2:
            num_q = st.selectbox(
                "🔢 Số câu hỏi:",
                [5, 10, 15, 20],
                index=[5, 10, 15, 20].index(st.session_state.b91_num_q) if st.session_state.b91_num_q in [5, 10, 15, 20] else 1,
                key="b91_num_selector"
            )
        with ctrl_col3:
            st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
            if st.button("🔄 Bắt đầu ván mới", key="b91_btn_start_new", use_container_width=True, type="primary"):
                st.session_state.b91_mode = chosen_mode
                st.session_state.b91_num_q = num_q
                st.session_state.b91_questions = generate_questions(chosen_mode, num_q)
                st.session_state.b91_idx = 0
                st.session_state.b91_score = 0
                st.session_state.b91_streak = 0
                st.session_state.b91_max_streak = 0
                st.session_state.b91_answered = False
                st.session_state.b91_selected = None
                st.session_state.b91_history = []
                st.session_state.b91_game_over = False
                st.rerun()

        # Kiểm tra nếu user thay đổi chế độ trên selectbox nhưng chưa ấn nút bắt đầu
        if chosen_mode != st.session_state.b91_mode or num_q != st.session_state.b91_num_q:
            st.info("💡 Bạn đã đổi cấu hình. Bấm **'🔄 Bắt đầu ván mới'** để áp dụng bộ câu hỏi mới nhé!")

        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

        # MÀN HÌNH TỔNG KẾT KHI HOÀN THÀNH
        if st.session_state.b91_game_over or st.session_state.b91_idx >= len(st.session_state.b91_questions):
            st.session_state.b91_game_over = True
            total_q = len(st.session_state.b91_questions)
            correct_count = sum(1 for h in st.session_state.b91_history if h["is_correct"])
            pct = int((correct_count / total_q) * 100) if total_q > 0 else 0

            if pct >= 70:
                st.balloons()

            if pct == 100:
                rank_title = "🥇 ĐẠI SỨ NGOẠI GIAO XUẤT SẮC"
                rank_msg = "Tuyệt đỉnh! Bạn ghi nhớ trọn vẹn 100% tất cả quốc gia, quốc tịch và tiền tệ!"
                rank_color = "#eab308"
            elif pct >= 80:
                rank_title = "🥈 CHUYÊN GIA ĐỊA LÝ & TIỀN TỆ"
                rank_msg = "Rất ấn tượng! Phản xạ từ vựng tiếng Trung của bạn vô cùng chuẩn xác!"
                rank_color = "#3b82f6"
            elif pct >= 60:
                rank_title = "🥉 NHÀ LỮ HÀNH NĂNG ĐỘNG"
                rank_msg = "Khá tốt! Luyện tập thêm một vài lần nữa bạn sẽ đạt điểm tuyệt đối!"
                rank_color = "#10b981"
            else:
                rank_title = "🌱 CHIẾN BINH ĐANG TIẾN BỘ"
                rank_msg = "Hãy ôn lại các thẻ từ vựng ở bên dưới và thử sức lại một ván nữa nhé!"
                rank_color = "#f97316"

            st.html(f"""
            <div style="background: white; border: 2px solid {rank_color}; border-radius: 18px; padding: 30px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.08); margin-bottom: 25px;">
                <div style="font-size: 3rem; margin-bottom: 8px;">🏆</div>
                <h2 style="color: {rank_color}; margin: 0 0 10px 0; font-weight: 900;">{rank_title}</h2>
                <p style="font-size: 1.1rem; color: #475569; max-width: 600px; margin: 0 auto 20px auto;">{rank_msg}</p>
                <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-bottom: 25px;">
                    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 12px 24px;">
                        <div style="font-size: 0.85rem; color: #64748b;">Điểm tổng kết</div>
                        <div style="font-size: 2rem; font-weight: 900; color: #1e3a8a;">{st.session_state.b91_score}</div>
                    </div>
                    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 12px 24px;">
                        <div style="font-size: 0.85rem; color: #64748b;">Số câu đúng</div>
                        <div style="font-size: 2rem; font-weight: 900; color: #16a34a;">{correct_count}/{total_q} ({pct}%)</div>
                    </div>
                    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 12px 24px;">
                        <div style="font-size: 0.85rem; color: #64748b;">Combo dài nhất</div>
                        <div style="font-size: 2rem; font-weight: 900; color: #ea580c;">🔥 {st.session_state.b91_max_streak}</div>
                    </div>
                </div>
            </div>
            """)

            # Review Expanders
            with st.expander("📝 Xem lại chi tiết từng câu đã làm", expanded=True):
                for idx, h in enumerate(st.session_state.b91_history):
                    icon = "✅" if h["is_correct"] else "❌"
                    color = "#16a34a" if h["is_correct"] else "#dc2626"
                    q_data = h["question"]
                    
                    st.html(f"""
                    <div style="border-left: 4px solid {color}; background: #f8fafc; padding: 12px 16px; border-radius: 6px; margin-bottom: 12px;">
                        <div style="font-weight: 700; color: #1e293b;">{icon} Câu {idx + 1}: {q_data['prompt']}</div>
                        <div style="margin: 6px 0; font-size: 0.95rem;">
                            Bạn chọn: <b style="color: {color};">{h['user_choice']}</b>
                        </div>
                        <div style="font-size: 0.9rem; color: #475569;">
                            💡 {q_data['explanation']}
                        </div>
                    </div>
                    """)

            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                if st.button("🔁 Chơi lại ván mới cùng chế độ", key="b91_btn_replay", use_container_width=True, type="primary"):
                    st.session_state.b91_questions = generate_questions(st.session_state.b91_mode, st.session_state.b91_num_q)
                    st.session_state.b91_idx = 0
                    st.session_state.b91_score = 0
                    st.session_state.b91_streak = 0
                    st.session_state.b91_max_streak = 0
                    st.session_state.b91_answered = False
                    st.session_state.b91_selected = None
                    st.session_state.b91_history = []
                    st.session_state.b91_game_over = False
                    st.rerun()
            with col_btn2:
                if st.button("🔀 Đổi sang Đấu trường Tổng hợp", key="b91_btn_switch_mix", use_container_width=True):
                    st.session_state.b91_mode = "mix"
                    st.session_state.b91_questions = generate_questions("mix", st.session_state.b91_num_q)
                    st.session_state.b91_idx = 0
                    st.session_state.b91_score = 0
                    st.session_state.b91_streak = 0
                    st.session_state.b91_max_streak = 0
                    st.session_state.b91_answered = False
                    st.session_state.b91_selected = None
                    st.session_state.b91_history = []
                    st.session_state.b91_game_over = False
                    st.rerun()

        else:
            # GIAO DIỆN CÂU HỎI ĐANG CHƠI
            curr_q = st.session_state.b91_questions[st.session_state.b91_idx]
            total_q = len(st.session_state.b91_questions)
            curr_num = st.session_state.b91_idx + 1

            # Progress bar
            progress_pct = (curr_num - 1) / total_q
            st.progress(progress_pct, text=f"Tiến độ: Câu {curr_num}/{total_q}")

            # Khung câu hỏi
            streak_html = f'<span class="streak-badge">🔥 COMBO x{st.session_state.b91_streak}</span>' if st.session_state.b91_streak >= 2 else ''
            st.html(f"""
            <div class="q-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <span style="font-weight: 800; font-size: 0.9rem; color: #2563eb; text-transform: uppercase; letter-spacing: 0.05em;">
                        {curr_q['title']} • CÂU {curr_num}/{total_q}
                    </span>
                    {streak_html}
                </div>
                <div style="font-size: 1.25rem; font-weight: 700; color: #0f172a; margin-bottom: 14px; line-height: 1.5;">
                    {curr_q['prompt']}
                </div>
            </div>
            """)

            # Cột hiển thị hình ảnh / cờ nếu có
            if curr_q.get("flag_code") and curr_q["flag_code"] != "un":
                flag_cols = st.columns([1, 2, 1])
                with flag_cols[1]:
                    st.html(f"""
                    <div class="flag-display">
                        <img class="flag-img-lg" src="https://flagcdn.com/w160/{curr_q['flag_code']}.png" alt="{curr_q['flag_code']}">
                    </div>
                    """)

            # Audio phát âm nếu đã trả lời xong
            if st.session_state.b91_answered:
                audio_cols = st.columns([1, 2, 1])
                with audio_cols[1]:
                    render_play_button(curr_q["audio_text"], f"🔊 Nghe phát âm: {curr_q['audio_text']}", key=f"audio_q_{curr_num}")

            # Danh sách lựa chọn
            st.markdown("<div style='font-size: 0.95rem; font-weight: 600; color: #475569; margin-bottom: 10px;'>👉 Chọn một đáp án đúng:</div>", unsafe_allow_html=True)

            opt_cols = st.columns(2)
            for opt_idx, opt_text in enumerate(curr_q["options"]):
                col = opt_cols[opt_idx % 2]
                with col:
                    btn_type = "secondary"
                    btn_label = opt_text
                    
                    if st.session_state.b91_answered:
                        if opt_idx == curr_q["correct_idx"]:
                            btn_label = f"✅ {opt_text}"
                            btn_type = "primary"
                        elif opt_idx == st.session_state.b91_selected:
                            btn_label = f"❌ {opt_text}"
                            btn_type = "primary"
                        
                        st.button(
                            btn_label,
                            key=f"opt_btn_{curr_num}_{opt_idx}",
                            type=btn_type,
                            use_container_width=True,
                            disabled=True
                        )
                    else:
                        if st.button(
                            btn_label,
                            key=f"opt_btn_{curr_num}_{opt_idx}",
                            type=btn_type,
                            use_container_width=True
                        ):
                            st.session_state.b91_selected = opt_idx
                            st.session_state.b91_answered = True
                            is_correct = (opt_idx == curr_q["correct_idx"])
                            
                            if is_correct:
                                st.session_state.b91_streak += 1
                                if st.session_state.b91_streak > st.session_state.b91_max_streak:
                                    st.session_state.b91_max_streak = st.session_state.b91_streak
                                
                                streak_bonus = min(st.session_state.b91_streak * 2, 10)
                                earned = 10 + streak_bonus
                                st.session_state.b91_score += earned
                                st.toast(f"🎉 Xuất sắc! +{earned} điểm!", icon="🔥")
                            else:
                                st.session_state.b91_streak = 0
                                st.toast("❌ Chưa chính xác rồi!", icon="😢")

                            st.session_state.b91_history.append({
                                "question": curr_q,
                                "user_choice": opt_text,
                                "is_correct": is_correct
                            })
                            st.rerun()

            # Hiển thị giải thích & nút Tiếp theo khi đã trả lời
            if st.session_state.b91_answered:
                is_win = (st.session_state.b91_selected == curr_q["correct_idx"])
                box_class = "feedback-box-correct" if is_win else "feedback-box-wrong"
                header_icon = "🎉 CHÍNH XÁC!" if is_win else "💡 GIẢI THÍCH CHI TIẾT"
                header_color = "#15803d" if is_win else "#b91c1c"

                st.html(f"""
                <div class="{box_class}">
                    <div style="font-weight: 800; font-size: 1.1rem; color: {header_color}; margin-bottom: 6px;">
                        {header_icon}
                    </div>
                    <div style="color: #1e293b; font-size: 1rem; line-height: 1.6;">
                        {curr_q['explanation']}
                    </div>
                    <div style="margin-top: 8px; font-size: 0.95rem; color: #475569; font-style: italic;">
                        {curr_q['example']}
                    </div>
                </div>
                """)

                st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
                act_cols = st.columns([3, 1])
                with act_cols[1]:
                    next_label = "Xem kết quả 🏆" if (curr_num >= total_q) else "Câu tiếp theo ➡️"
                    if st.button(next_label, type="primary", use_container_width=True, key=f"btn_next_{curr_num}"):
                        if curr_num >= total_q:
                            st.session_state.b91_game_over = True
                        else:
                            st.session_state.b91_idx += 1
                            st.session_state.b91_answered = False
                            st.session_state.b91_selected = None
                        st.rerun()

    # =========================================================================
    # TAB 2: THẺ LẬT ÔN NHANH (FLASHCARDS GRID)
    # =========================================================================
    with subtab_flashcards:
        st.subheader("🎴 Thẻ Lật Nhớ Nhanh Từ Vựng")
        st.caption("Xem nhanh và nghe phát âm chuẩn của tất cả quốc gia, quốc tịch và tiền tệ.")
        
        filter_type = st.radio(
            "Lọc danh mục thẻ:",
            ["🗺️ Tất cả quốc gia (36)", "🧑‍🤝‍🧑 Quốc tịch (18)", "💵 Tiền tệ (9)"],
            horizontal=True,
            key="b91_flash_filter"
        )

        if "quốc gia" in filter_type.lower():
            items = B9_1_QUOC_GIA
            cols = st.columns(3)
            for idx, c in enumerate(items):
                col = cols[idx % 3]
                with col:
                    code = c.get("FlagCode", "un")
                    st.html(f"""
                    <div class="mini-card">
                        <img src="https://flagcdn.com/w40/{code}.png" width="40" height="26" style="border-radius:3px;box-shadow:0 1px 3px rgba(0,0,0,0.2);margin-bottom:6px;">
                        <div style="font-size: 1.3rem; font-weight: 800; color: #1e3a8a;">{c['Chữ Hán']}</div>
                        <div style="font-family: monospace; color: #2563eb; font-weight: 600; font-size: 0.9rem;">{c['Pinyin']}</div>
                        <div style="font-size: 0.85rem; color: #16a34a; font-weight: 600;">{c['Nghĩa tiếng Việt']}</div>
                    </div>
                    """)
                    render_play_button(c['Chữ Hán'], "🔊 Nghe", key=f"flash_cg_{idx}", height=38)

        elif "quốc tịch" in filter_type.lower():
            items = B9_1_QUOC_TICH
            cols = st.columns(3)
            for idx, c in enumerate(items):
                col = cols[idx % 3]
                with col:
                    code = c.get("FlagCode", "un")
                    st.html(f"""
                    <div class="mini-card">
                        <img src="https://flagcdn.com/w40/{code}.png" width="40" height="26" style="border-radius:3px;box-shadow:0 1px 3px rgba(0,0,0,0.2);margin-bottom:6px;">
                        <div style="font-size: 1.3rem; font-weight: 800; color: #1e3a8a;">{c['Chữ Hán']}</div>
                        <div style="font-family: monospace; color: #2563eb; font-weight: 600; font-size: 0.9rem;">{c['Pinyin']}</div>
                        <div style="font-size: 0.85rem; color: #16a34a; font-weight: 600;">{c['Nghĩa tiếng Việt']}</div>
                    </div>
                    """)
                    render_play_button(c['Chữ Hán'], "🔊 Nghe", key=f"flash_nat_{idx}", height=38)

        else:
            cols = st.columns(3)
            for idx, c in enumerate(CURRENCY_DETAILS):
                col = cols[idx % 3]
                with col:
                    flag = c.get("flag", "cn")
                    st.html(f"""
                    <div class="mini-card">
                        <img src="https://flagcdn.com/w40/{flag}.png" width="40" height="26" style="border-radius:3px;box-shadow:0 1px 3px rgba(0,0,0,0.2);margin-bottom:6px;">
                        <div style="font-size: 1.3rem; font-weight: 800; color: #1e3a8a;">{c['hanzi']}</div>
                        <div style="font-family: monospace; color: #2563eb; font-weight: 600; font-size: 0.9rem;">{c['pinyin']}</div>
                        <div style="font-size: 0.85rem; color: #d97706; font-weight: 600;">{c['meaning']}</div>
                        <div style="font-size: 0.75rem; color: #64748b;">({c['country']})</div>
                    </div>
                    """)
                    render_play_button(c['hanzi'], "🔊 Nghe", key=f"flash_curr_{idx}", height=38)

    # =========================================================================
    # TAB 3: VÒNG QUAY GỌI TÊN THỬ THÁCH (CLASSROOM CALLER)
    # =========================================================================
    with subtab_wheel:
        st.subheader("🎲 Vòng Quay May Mắn & Thử Thách Lớp Học")
        st.caption("Dành cho giáo viên hoặc người học tự luyện: Bốc thăm ngẫu nhiên học viên và câu hỏi thử thách phản xạ!")

        wheel_col1, wheel_col2 = st.columns([1, 1])
        with wheel_col1:
            students_input = st.text_area(
                "Danh sách học viên (phân cách bởi dấu phẩy):",
                "Tiên, Vy, Trân, Thanh, Nam, Hùng, Linh, Mai",
                height=80,
                key="b91_students_wheel_input"
            )
            challenge_types = st.multiselect(
                "Các dạng thử thách bốc thăm:",
                ["🚩 Đọc tên quốc kỳ", "🧑‍🤝‍🧑 Đóng vai người nước đó", "💵 Trả giá bằng tiền tệ đó"],
                default=["🚩 Đọc tên quốc kỳ", "🧑‍🤝‍🧑 Đóng vai người nước đó"],
                key="b91_challenges_select"
            )
            spin_btn = st.button("🎰 QUAY THỬ THÁCH NGAY!", key="b91_btn_spin", type="primary", use_container_width=True)

        with wheel_col2:
            if spin_btn:
                students = [s.strip() for s in students_input.split(",") if s.strip()]
                chosen_student = random.choice(students) if students else "Bạn học viên"
                chosen_country = random.choice(B9_1_QUOC_GIA)
                chosen_currency = random.choice(CURRENCY_DETAILS)
                chosen_task = random.choice(challenge_types) if challenge_types else "🚩 Đọc tên quốc kỳ"

                code = chosen_country.get("FlagCode", "un")
                st.session_state["wheel_result"] = {
                    "student": chosen_student,
                    "country": chosen_country,
                    "currency": chosen_currency,
                    "task": chosen_task
                }

            if "wheel_result" in st.session_state:
                res = st.session_state["wheel_result"]
                c = res["country"]
                curr = res["currency"]
                code = c.get("FlagCode", "un")

                st.html(f"""
                <div style="background: linear-gradient(135deg, #fef3c7, #fde68a); border: 2px solid #f59e0b; border-radius: 16px; padding: 20px; text-align: center;">
                    <div style="font-size: 0.9rem; font-weight: 800; color: #b45309; text-transform: uppercase;">🎯 Người được gọi tên:</div>
                    <div style="font-size: 2.2rem; font-weight: 900; color: #92400e; margin: 4px 0 12px 0;">👉 {res['student']} 👈</div>
                    
                    <div style="background: white; border-radius: 12px; padding: 14px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
                        <img src="https://flagcdn.com/w80/{code}.png" width="70" height="45" style="border-radius:4px;box-shadow:0 2px 6px rgba(0,0,0,0.15);margin-bottom:8px;">
                        <div style="font-size: 1.1rem; color: #1e3a8a; font-weight: bold;">Nhiệm vụ: {res['task']}</div>
                        <div style="margin-top: 8px; font-size: 0.95rem; color: #475569;">
                            Quốc gia: <b>{c['Nghĩa tiếng Việt']}</b> | Tiền tệ: <b>{curr['meaning']}</b>
                        </div>
                    </div>
                    
                    <div style="font-size: 0.85rem; color: #6b7280; font-style: italic;">
                        Học viên hãy phát âm chuẩn câu tiếng Trung trước cả lớp!
                    </div>
                </div>
                """)
                
                render_play_button(f"我是{c['Chữ Hán']}人", f"🔊 Nghe câu mẫu: 我是{c['Chữ Hán']}人", key="wheel_play_btn")

def show_lesson9_1_review_game():
    """Hàm wrapper cho phép gọi độc lập từ sidebar a.py"""
    render_lesson9_1_game()
