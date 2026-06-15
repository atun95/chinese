import streamlit as st
import random
import json
import streamlit.components.v1 as components

def play_audio(text):
    safe_txt = json.dumps(text, ensure_ascii=False)
    components.html(
        f"""
        <script>
        const text = {safe_txt};
        
        let audioCtx = null;
        function playAmplified(audioNode, fallbackFunc, volumeBoost = 3.0) {{
            try {{
                if (!audioCtx) {{
                    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                }}
                if (audioCtx.state === 'suspended') {{
                    audioCtx.resume();
                }}
                if (!audioNode._amplified) {{
                    const source = audioCtx.createMediaElementSource(audioNode);
                    const gainNode = audioCtx.createGain();
                    gainNode.gain.value = volumeBoost;
                    source.connect(gainNode);
                    gainNode.connect(audioCtx.destination);
                    audioNode._amplified = true;
                }}
                audioNode.play().catch(err => {{
                    if (fallbackFunc) fallbackFunc();
                }});
            }} catch(err) {{
                audioNode.play().catch(err => {{
                    if (fallbackFunc) fallbackFunc();
                }});
            }}
        }}

        function loadAndPlay(url, fallbackFunc, volumeBoost = 3.0) {{
            let audioNode = new Audio();
            audioNode.src = url;
            audioNode.onerror = () => {{
                if (fallbackFunc) fallbackFunc();
            }};
            if (url.startsWith("data:")) {{
                playAmplified(audioNode, fallbackFunc, volumeBoost);
            }} else {{
                audioNode.play().catch(err => {{
                    if (fallbackFunc) fallbackFunc();
                }});
            }}
        }}

        function speakSpeechSynthesis(txt, onFallback) {{
            try {{
                if (!window.speechSynthesis) {{
                    if (onFallback) onFallback();
                    return;
                }}
                const u = new SpeechSynthesisUtterance(txt);
                u.lang = "zh-CN";
                u.rate = 0.9;
                u.volume = 1.0;
                u.onerror = (e) => {{
                    if (onFallback) onFallback();
                }};
                window.speechSynthesis.cancel();
                window.speechSynthesis.speak(u);
            }} catch (err) {{
                if (onFallback) onFallback();
            }}
        }}
        
        if (text.startsWith("data:audio/")) {{
            loadAndPlay(text, null, 3.0);
        }} else {{
            const url = "https://translate.google.com/translate_tts?ie=UTF-8&tl=zh-CN&client=tw-ob&q=" + encodeURIComponent(text);
            loadAndPlay(url, () => speakSpeechSynthesis(text, null), 3.0);
        }}
        </script>
        """,
        height=0,
    )

def render_play_button(text, label, key=None, height=45, type="secondary"):
    safe_text = json.dumps(text, ensure_ascii=False)
    components.html(
        f"""
        <style>
        body {{
            margin: 0;
            padding: 0;
            background-color: transparent;
            overflow: hidden;
        }}
        .play-btn {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            height: 38px;
            background-color: {"#2563eb" if type == "primary" else "#ffffff"};
            color: {"#ffffff" if type == "primary" else "#31333F"};
            border: {"1px solid #2563eb" if type == "primary" else "1px solid #e2e8f0"};
            border-radius: 8px;
            font-size: 0.88rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            box-sizing: border-box;
            user-select: none;
        }}
        .play-btn:hover {{
            background-color: {"#1d4ed8" if type == "primary" else "#eff6ff"};
            border-color: {"#1d4ed8" if type == "primary" else "#2563eb"};
            color: {"#ffffff" if type == "primary" else "#2563eb"};
        }}
        .play-btn:active {{
            transform: scale(0.98);
        }}
        </style>
        <button class="play-btn" onclick="playTTS()">{label}</button>
        <script>
        let audioCtx = null;
        let audio = null;
        
        function speakSpeechSynthesis(txt, onFallback) {{
            try {{
                if (!window.speechSynthesis) {{
                    if (onFallback) onFallback();
                    return;
                }}
                const u = new SpeechSynthesisUtterance(txt);
                u.lang = "zh-CN";
                u.rate = 0.9;
                u.volume = 1.0;
                u.onerror = (e) => {{
                    if (onFallback) onFallback();
                }};
                window.speechSynthesis.cancel();
                window.speechSynthesis.speak(u);
            }} catch (err) {{
                if (onFallback) onFallback();
            }}
        }}

        function playAmplified(audioNode, fallbackFunc, volumeBoost = 3.0) {{
            try {{
                if (!audioCtx) {{
                    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                }}
                if (audioCtx.state === 'suspended') {{
                    audioCtx.resume();
                }}
                if (!audioNode._amplified) {{
                    const source = audioCtx.createMediaElementSource(audioNode);
                    const gainNode = audioCtx.createGain();
                    gainNode.gain.value = volumeBoost;
                    source.connect(gainNode);
                    gainNode.connect(audioCtx.destination);
                    audioNode._amplified = true;
                }}
                audioNode.play().catch(err => {{
                    // Do not trigger fallback immediately here because onerror will handle the retry
                }});
            }} catch(err) {{
                audioNode.play().catch(err => {{
                    if (fallbackFunc) fallbackFunc();
                }});
            }}
        }}

        function loadAndPlay(url, fallbackFunc, volumeBoost = 3.0) {{
            if (audio) {{
                audio.pause();
            }}
            let fallbackTriggered = false;
            const triggerFallback = () => {{
                if (!fallbackTriggered) {{
                    fallbackTriggered = true;
                    if (fallbackFunc) fallbackFunc();
                }}
            }};
            audio = new Audio();
            audio.src = url;
            audio.onerror = () => {{
                triggerFallback();
            }};
            if (url.startsWith("data:")) {{
                playAmplified(audio, triggerFallback, volumeBoost);
            }} else {{
                audio.play().catch(err => {{
                    triggerFallback();
                }});
            }}
        }}
        
        function playTTS() {{
            const text = {safe_text};
            if (text.startsWith("data:audio/")) {{
                loadAndPlay(text, null, 3.0);
                return;
            }}
            const url = "https://translate.google.com/translate_tts?ie=UTF-8&tl=zh-CN&client=tw-ob&q=" + encodeURIComponent(text);
            loadAndPlay(url, () => speakSpeechSynthesis(text, null), 3.0);
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
