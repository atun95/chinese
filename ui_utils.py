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
        const hasChinese = /[\u4e00-\u9fa5]/.test(text);
        
        const toneVowels = {{
            'ā': 'a1', 'á': 'a2', 'ǎ': 'a3', 'à': 'a4',
            'ē': 'e1', 'é': 'e2', 'ě': 'e3', 'è': 'e4',
            'ī': 'i1', 'í': 'i2', 'ǐ': 'i3', 'ì': 'i4',
            'ō': 'o1', 'ó': 'o2', 'ǒ': 'o3', 'ò': 'o4',
            'ū': 'u1', 'ú': 'u2', 'ǔ': 'u3', 'ù': 'u4',
            'ǖ': 'v1', 'ǘ': 'v2', 'ǚ': 'v3', 'ǜ': 'v4',
            'ü': 'v'
        }};
        
        function speakSpeechSynthesis() {{
            const u = new SpeechSynthesisUtterance(text);
            u.lang = "zh-CN";
            u.rate = 0.9;
            u.volume = 1.0;
            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(u);
        }}
        
        if (hasChinese) {{
            const url = "https://translate.google.com/translate_tts?ie=UTF-8&tl=zh-CN&client=tw-ob&q=" + encodeURIComponent(text);
            const audio = new Audio(url);
            audio.volume = 1.0;
            audio.play().catch(err => {{
                speakSpeechSynthesis();
            }});
        }} else {{
            const cleanText = text.trim();
            const isSingle = !/\\s/.test(cleanText) && cleanText.length <= 7;
            if (isSingle) {{
                let tone = 5;
                let base = cleanText.toLowerCase();
                for (const [marked, replacement] of Object.entries(toneVowels)) {{
                    if (base.includes(marked)) {{
                        base = base.replace(marked, replacement.slice(0, -1));
                        tone = parseInt(replacement.slice(-1));
                        break;
                    }}
                }}
                base = base.replace(/ü/g, 'v');
                const numbered = base + tone;
                let url = "https://dictionary.writtenchinese.com/sounds/" + encodeURIComponent(numbered) + ".mp3";
                let pinyinAudio = new Audio(url);
                pinyinAudio.volume = 1.0;
                let fallbackTriggered = false;
                
                const triggerFallback = () => {{
                    if (!fallbackTriggered) {{
                        if (tone === 5 && url.endsWith("5.mp3")) {{
                            url = url.replace(/5\\.mp3$/, ".mp3");
                            pinyinAudio = new Audio(url);
                            pinyinAudio.volume = 1.0;
                            pinyinAudio.onerror = () => {{
                                fallbackTriggered = true;
                                speakSpeechSynthesis();
                            }};
                            pinyinAudio.play().catch(err => {{
                                fallbackTriggered = true;
                                speakSpeechSynthesis();
                            }});
                        }} else {{
                            fallbackTriggered = true;
                            speakSpeechSynthesis();
                        }}
                    }}
                }};
                
                pinyinAudio.onerror = triggerFallback;
                pinyinAudio.play().catch(err => {{
                    triggerFallback();
                }});
            }} else {{
                speakSpeechSynthesis();
            }}
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
        let audio = null;
        const toneVowels = {{
            'ā': 'a1', 'á': 'a2', 'ǎ': 'a3', 'à': 'a4',
            'ē': 'e1', 'é': 'e2', 'ě': 'e3', 'è': 'e4',
            'ī': 'i1', 'í': 'i2', 'ǐ': 'i3', 'ì': 'i4',
            'ō': 'o1', 'ó': 'o2', 'ǒ': 'o3', 'ò': 'o4',
            'ū': 'u1', 'ú': 'u2', 'ǔ': 'u3', 'ù': 'u4',
            'ǖ': 'v1', 'ǘ': 'v2', 'ǚ': 'v3', 'ǜ': 'v4',
            'ü': 'v'
        }};
        
        function speakSpeechSynthesis(txt) {{
            const u = new SpeechSynthesisUtterance(txt);
            u.lang = "zh-CN";
            u.rate = 0.9;
            u.volume = 1.0;
            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(u);
        }}
        
        function playTTS() {{
            const text = {safe_text};
            const hasChinese = /[\u4e00-\u9fa5]/.test(text);
            
            if (audio) {{
                audio.pause();
                audio.currentTime = 0;
            }}
            
            if (hasChinese) {{
                const url = "https://translate.google.com/translate_tts?ie=UTF-8&tl=zh-CN&client=tw-ob&q=" + encodeURIComponent(text);
                audio = new Audio(url);
                audio.volume = 1.0;
                audio.play().catch(err => {{
                    speakSpeechSynthesis(text);
                }});
            }} else {{
                const cleanText = text.trim();
                const isSingle = !/\\s/.test(cleanText) && cleanText.length <= 7;
                if (isSingle) {{
                    let tone = 5;
                    let base = cleanText.toLowerCase();
                    for (const [marked, replacement] of Object.entries(toneVowels)) {{
                        if (base.includes(marked)) {{
                            base = base.replace(marked, replacement.slice(0, -1));
                            tone = parseInt(replacement.slice(-1));
                            break;
                        }}
                    }}
                    base = base.replace(/ü/g, 'v');
                    const numbered = base + tone;
                    let url = "https://dictionary.writtenchinese.com/sounds/" + encodeURIComponent(numbered) + ".mp3";
                    audio = new Audio(url);
                    audio.volume = 1.0;
                    let fallbackTriggered = false;
                    
                    const triggerFallback = () => {{
                        if (!fallbackTriggered) {{
                            if (tone === 5 && url.endsWith("5.mp3")) {{
                                url = url.replace(/5\\.mp3$/, ".mp3");
                                audio = new Audio(url);
                                audio.volume = 1.0;
                                audio.onerror = () => {{
                                    fallbackTriggered = true;
                                    speakSpeechSynthesis(text);
                                }};
                                audio.play().catch(err => {{
                                    fallbackTriggered = true;
                                    speakSpeechSynthesis(text);
                                }});
                            }} else {{
                                fallbackTriggered = true;
                                speakSpeechSynthesis(text);
                            }}
                        }}
                    }};
                    
                    audio.onerror = triggerFallback;
                    audio.play().catch(err => {{
                        triggerFallback();
                    }});
                }} else {{
                    speakSpeechSynthesis(text);
                }}
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
        .lesson-title {{
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            font-size: calc(1.3rem + 0.8vw);
            font-weight: 800;
            margin-top: 0;
            margin-bottom: 20px;
            color: #0f172a;
            border-bottom: 2px solid #f1f5f9;
            padding-bottom: 10px;
        }}
        @media (max-width: 768px) {{
            .lesson-title {{
                font-size: 1.25rem;
            }}
        }}
        </style>
        <h1 class="lesson-title">{title}</h1>
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
