import streamlit as st
import random
import json
import streamlit.components.v1 as components

# ─── SHARED TTS JavaScript (chuẩn phát âm tiếng Trung phổ thông) ──────────
_TTS_JS_CORE = """
<script>
(function() {
    const TONE_VOWELS = {
        'ā': 'a1', 'á': 'a2', 'ǎ': 'a3', 'à': 'a4',
        'ō': 'o1', 'ó': 'o2', 'ǒ': 'o3', 'ò': 'o4',
        'ē': 'e1', 'é': 'e2', 'ě': 'e3', 'è': 'e4',
        'ī': 'i1', 'í': 'i2', 'ǐ': 'i3', 'ì': 'i4',
        'ū': 'u1', 'ú': 'u2', 'ǔ': 'u3', 'ù': 'u4',
        'ǖ': 'v1', 'ǘ': 'v2', 'ǚ': 'v3', 'ǜ': 'v4',
        'ü': 'v'
    };

    function buildAudioUrls(text) {
        text = (text || '').toString().trim();
        const urls = [];
        if (!text) return urls;

        const hasChinese = /[\\u4e00-\\u9fa5]/.test(text);

        if (hasChinese) {
            // Chữ Hán, từ vựng, câu hội thoại
            urls.push("https://dict.youdao.com/dictvoice?audio=" + encodeURIComponent(text) + "&le=zh");
            urls.push("https://translate.google.com/translate_tts?ie=UTF-8&tl=zh-CN&client=tw-ob&q=" + encodeURIComponent(text));
        } else {
            // Pinyin hoặc chữ cái đơn lẻ
            const clean = text.toLowerCase().trim();
            if (!/\\s/.test(clean)) {
                let tone = '';
                let base = clean;
                for (const [marked, repl] of Object.entries(TONE_VOWELS)) {
                    if (base.includes(marked)) {
                        base = base.replace(marked, repl.slice(0, -1));
                        tone = repl.slice(-1);
                        break;
                    }
                }
                base = base.replace(/ü/g, 'v');
                const m = base.match(/^([a-z]+)([1-5])$/);
                let numbered = '';
                if (m) {
                    numbered = m[1] + m[2];
                } else if (tone) {
                    numbered = base + tone;
                } else {
                    numbered = base;
                }

                if (numbered) {
                    // Audio chuẩn người bản xứ đọc từng âm tiết pinyin theo thanh điệu
                    urls.push("https://dictionary.writtenchinese.com/sounds/" + encodeURIComponent(numbered) + ".mp3");
                    if (numbered.endsWith('5')) {
                        urls.push("https://dictionary.writtenchinese.com/sounds/" + encodeURIComponent(numbered.slice(0, -1)) + ".mp3");
                    }
                }
            }

            // Fallback sang Youdao engine tiếng Trung và Google Translate tiếng Trung
            urls.push("https://dict.youdao.com/dictvoice?audio=" + encodeURIComponent(text) + "&le=zh");
            urls.push("https://translate.google.com/translate_tts?ie=UTF-8&tl=zh-CN&client=tw-ob&q=" + encodeURIComponent(text));
        }
        return urls;
    }

    let _activeAudio = null;

    function playAudioUrls(urls, onDone, onFail) {
        if (_activeAudio) {
            try {
                _activeAudio.pause();
                _activeAudio.currentTime = 0;
            } catch(e) {}
            _activeAudio = null;
        }

        let idx = 0;
        function tryNext() {
            if (idx >= urls.length) {
                if (onFail) onFail();
                return;
            }
            const url = urls[idx++];
            const audio = new Audio();
            _activeAudio = audio;
            let finished = false;

            const next = () => {
                if (finished) return;
                finished = true;
                tryNext();
            };

            audio.onerror = next;

            const timer = setTimeout(() => {
                if (!finished && audio.readyState < 2) {
                    next();
                }
            }, 3500);

            audio.oncanplay = () => {
                clearTimeout(timer);
            };

            audio.onended = () => {
                finished = true;
                clearTimeout(timer);
                if (onDone) onDone();
            };

            audio.play().then(() => {
                clearTimeout(timer);
            }).catch(() => {
                clearTimeout(timer);
                next();
            });
        }

        tryNext();
    }

    function speakWSAIfChinese(txt) {
        try {
            if (!window.speechSynthesis) return;
            const voices = window.speechSynthesis.getVoices();
            // TUYỆT ĐỐI CHỈ DÙNG NẾU CÓ GIỌNG TIẾNG TRUNG, KHÔNG DÙNG GIỌNG TIẾNG ANH MẶC ĐỊNH
            const zhVoice = voices.find(v => (v.lang && (v.lang === 'zh-CN' || v.lang === 'zh_CN' || v.lang.startsWith('zh'))) || (v.name && v.name.toLowerCase().includes('chinese')));
            if (!zhVoice) return;
            const u = new SpeechSynthesisUtterance(txt);
            u.voice = zhVoice;
            u.lang = 'zh-CN';
            u.rate = 0.85;
            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(u);
        } catch(e) {}
    }

    window.chineseTTS = function(txt) {
        if (!txt) return;
        txt = txt.toString().trim();
        if (!txt) return;

        if (txt.startsWith('data:audio/')) {
            if (_activeAudio) {
                try { _activeAudio.pause(); } catch(e) {}
            }
            const a = new Audio(txt);
            _activeAudio = a;
            a.play().catch(() => {});
            return;
        }

        const urls = buildAudioUrls(txt);
        playAudioUrls(urls, null, () => {
            speakWSAIfChinese(txt);
        });
    };
})();
</script>
"""

def _tts_js_once():
    """Nhúng TTS core JS vào page."""
    components.html(_TTS_JS_CORE, height=0)


def play_audio(text):
    """Phát âm tự động (không cần button) — chuẩn âm thanh tiếng Trung."""
    safe_txt = json.dumps(text, ensure_ascii=False)
    components.html(
        f"""
        {_TTS_JS_CORE}
        <script>
        (function() {{
            const txt = {safe_txt};
            if (window.chineseTTS) {{
                window.chineseTTS(txt);
            }}
        }})();
        </script>
        """,
        height=0,
    )


def render_play_button(text, label, key=None, height=45, type="secondary"):
    safe_text = json.dumps(text, ensure_ascii=False)
    bg      = "#2563eb" if type == "primary" else "#ffffff"
    color   = "#ffffff" if type == "primary" else "#31333F"
    border  = "#2563eb" if type == "primary" else "#e2e8f0"
    bg_hov  = "#1d4ed8" if type == "primary" else "#eff6ff"
    brd_hov = "#1d4ed8" if type == "primary" else "#2563eb"
    clr_hov = "#ffffff" if type == "primary" else "#2563eb"

    components.html(
        f"""
        {_TTS_JS_CORE}
        <style>
        body {{ margin:0; padding:0; background:transparent; overflow:hidden; }}
        .play-btn {{
            display:inline-flex; align-items:center; justify-content:center;
            width:100%; height:38px;
            background-color:{bg}; color:{color};
            border:1px solid {border}; border-radius:8px;
            font-size:0.88rem; font-weight:500; cursor:pointer;
            transition:all 0.2s ease;
            box-shadow:0 1px 2px rgba(0,0,0,0.05);
            font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
            box-sizing:border-box; user-select:none;
        }}
        .play-btn:hover {{
            background-color:{bg_hov}; border-color:{brd_hov}; color:{clr_hov};
        }}
        .play-btn:active {{ transform:scale(0.98); }}
        </style>
        <button class="play-btn" onclick="handlePlay()">{label}</button>
        <script>
        function handlePlay() {{
            const txt = {safe_text};
            if (window.chineseTTS) {{
                window.chineseTTS(txt);
            }}
        }}
        </script>
        """,
        height=height,
    )

def render_pronunciation_card(item, key_prefix):
    st.markdown(f"### {item['chu']}")
    st.write(item["hdsd"])
    st.write(f"Ví dụ: **{item['vd_han']}** — *{item['vd_py']}*.")
    render_play_button(item["nghe"], "🔊 Nghe ví dụ", key=f"{key_prefix}_{item['chu']}")

def render_lesson_intro(title, objective=None):
    st.markdown(
        f"""
        <style>
        /* ===== GLOBAL MOBILE FIXES ===== */
        .lesson-title {{
            white-space: normal;
            word-break: break-word;
            font-size: calc(1.1rem + 0.6vw);
            font-weight: 800;
            margin-top: 0;
            margin-bottom: 16px;
            color: #0f172a;
            border-bottom: 2px solid #f1f5f9;
            padding-bottom: 10px;
            line-height: 1.3;
        }}
        /* Tabs: allow horizontal scroll on mobile instead of clipping */
        [data-testid="stTabs"] [role="tablist"] {{
            overflow-x: auto;
            flex-wrap: nowrap;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
        }}
        [data-testid="stTabs"] [role="tablist"]::-webkit-scrollbar {{ display: none; }}
        [data-testid="stTabs"] button[role="tab"] {{
            white-space: nowrap;
            flex-shrink: 0;
            font-size: 0.82rem;
            padding: 8px 12px;
        }}
        /* Radio buttons: bigger tap targets on mobile */
        @media (max-width: 640px) {{
            .lesson-title {{
                font-size: 1.15rem;
            }}
            [data-testid="stRadio"] label {{
                font-size: 0.9rem;
                padding: 6px 0;
            }}
            /* Columns on mobile: stack vertically */
            [data-testid="column"] {{
                min-width: 100% !important;
            }}
            /* Buttons full width */
            [data-testid="stButton"] > button {{
                width: 100%;
                font-size: 0.9rem;
            }}
            /* Cards: reduce padding */
            .adv-card, .nasal-card {{
                padding: 12px;
            }}
        }}
        </style>
        <h1 class="lesson-title">{title}</h1>
        {f'<p style="color:#475569;font-size:0.95rem;margin-top:-8px;margin-bottom:16px;">{objective}</p>' if objective else ''}
        """,
        unsafe_allow_html=True
    )

def shuffled_options(options, seed_text):
    opts = options[:]
    rnd = random.Random(seed_text)
    rnd.shuffle(opts)
    return opts

def render_quiz_section(questions, key_prefix, title, caption, save_func):
    with st.expander(title, expanded=False):
        st.caption(caption)
        score = 0
        for idx, item in enumerate(questions):
            raw_choices = item["choices"]
            choices = shuffled_options(raw_choices, f"{key_prefix}-{idx}")
            
            # Đảm bảo câu đầu tiên không phải đáp án đúng để học viên phải chọn
            if choices[0] == item["answer"] and len(choices) > 1:
                choices[0], choices[1] = choices[1], choices[0]
                
            key = f"{key_prefix}_q_{idx}"
            selected = st.radio(
                f"Câu {idx + 1}: {item['q']}?",
                choices,
                index=0,
                key=key,
            )
            if selected == item["answer"]:
                score += 1
        
        if st.button(f"Chấm điểm {title}", key=f"btn_{key_prefix}"):
            total = len(questions)
            st.session_state.scores[key_prefix] = (score, total)
            save_func()
            st.success(f"Bạn đúng {score}/{total} câu.")
            return score, total
    return None


# ─── Bảng luyện tập ghép âm – layout chung cho tất cả bài ──────────────────
_TONE_LABELS = ["Thanh 1", "Thanh 2", "Thanh 3", "Thanh 4"]
_TONE_COLORS = ["#2563eb", "#16a34a", "#d97706", "#dc2626"]
_TONE_BG     = ["#eff6ff", "#f0fdf4", "#fefce8", "#fff1f2"]

def render_spelling_table(finals, rows, key_prefix, add_tones, group_colors=None):
    """
    Bảng luyện tập ghép âm cải tiến.
      - finals      : list cột vận mẫu
      - rows        : dict {thanh_mẫu: [tổ_hợp_hoặc_rỗng, ...]}
      - key_prefix  : tiền tố duy nhất cho widget key
      - add_tones   : hàm(base) → [t1, t2, t3, t4]
      - group_colors: dict {thanh_mẫu: màu_nền} để phân nhóm màu
    """
    if group_colors is None:
        group_colors = {}

    # ── CSS: ép pinyin không xuống dòng trong nút popover ────────────────────
    st.markdown(
        f"""
        <style>
        /* Tất cả button trong cột của bảng ghép âm: không wrap */
        [data-testid="stPopoverButton"] > div,
        [data-testid="stPopoverButton"] p,
        [data-testid="stPopoverButton"] {{
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
            font-family: monospace !important;
            font-size: 0.78rem !important;
        }}
        [data-testid="stPopoverButton"] {{
            padding: 4px 2px !important;
            min-height: 30px !important;
            max-height: 36px !important;
            width: 100% !important;
        }}
        </style>
        """,
        unsafe_allow_html=True)

    ratio = [1.8] + [1] * len(finals)

    # ── Header ────────────────────────────────────────────────────────────────
    h_cols = st.columns(ratio)
    h_cols[0].markdown(
        "<div style='background:linear-gradient(135deg,#1e40af,#3b82f6);"
        "color:#fff;border-radius:8px;padding:8px 6px;font-weight:800;"
        "text-align:center;font-size:0.88rem;letter-spacing:1px;'>T / V</div>",
        unsafe_allow_html=True)
    for j, f in enumerate(finals):
        h_cols[j + 1].markdown(
            f"<div style='background:linear-gradient(135deg,#1e40af,#3b82f6);"
            f"color:#fff;border-radius:8px;padding:8px 2px;font-weight:700;"
            f"text-align:center;font-size:0.82rem;font-family:monospace;'>{f}</div>",
            unsafe_allow_html=True)

    # ── Hàng dữ liệu ─────────────────────────────────────────────────────────
    for row_idx, (init, combos) in enumerate(rows.items()):
        bg     = group_colors.get(init, "#f8fafc")
        border = group_colors.get(f"{init}__border", "#e2e8f0")
        r_cols = st.columns(ratio)

        # Ô thanh mẫu (cột đầu)
        r_cols[0].markdown(
            f"<div style='background:{bg};border:1.5px solid {border};"
            f"border-radius:8px;padding:8px 6px;font-weight:800;"
            f"text-align:center;color:#1e3a8a;font-size:0.92rem;"
            f"font-family:monospace;min-height:38px;display:flex;"
            f"align-items:center;justify-content:center;'>{init}</div>",
            unsafe_allow_html=True)

        # Ô ghép âm
        for col_idx, combo in enumerate(combos):
            with r_cols[col_idx + 1]:
                if combo:
                    with st.popover(combo, use_container_width=True):
                        st.markdown(
                            f"<div style='text-align:center;margin-bottom:10px;'>"
                            f"<span style='font-size:0.78rem;color:#64748b;'>4 thanh điệu của </span>"
                            f"<span style='font-size:1rem;font-weight:800;color:#1e3a8a;"
                            f"font-family:monospace;'>{combo}</span></div>",
                            unsafe_allow_html=True)

                        tones = add_tones(combo)
                        # Lưới 2×2: hàng 1 (T1, T2) — hàng 2 (T3, T4)
                        ca, cb = st.columns(2)
                        cc, cd = st.columns(2)
                        for grid_col, t_idx in [(ca, 0), (cb, 1), (cc, 2), (cd, 3)]:
                            if t_idx < len(tones):
                                t_val = tones[t_idx]
                                with grid_col:
                                    st.markdown(
                                        f"<div style='text-align:center;"
                                        f"background:{_TONE_BG[t_idx]};border:1px solid {_TONE_COLORS[t_idx]}40;"
                                        f"border-radius:8px;padding:5px 2px;margin-bottom:4px;'>"
                                        f"<div style='font-size:0.67rem;color:{_TONE_COLORS[t_idx]};"
                                        f"font-weight:700;'>{_TONE_LABELS[t_idx]}</div>"
                                        f"<div style='font-size:1.4rem;font-weight:800;color:#0f172a;"
                                        f"font-family:Georgia,serif;line-height:1.3;'>{t_val}</div>"
                                        f"</div>",
                                        unsafe_allow_html=True)
                                    render_play_button(
                                        t_val, "🔊",
                                        key=f"{key_prefix}_{row_idx}_{col_idx}_{t_idx}",
                                        height=32)
