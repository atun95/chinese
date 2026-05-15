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
        const u = new SpeechSynthesisUtterance(text);
        u.lang = "zh-CN";
        u.rate = 0.9;
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(u);
        </script>
        """,
        height=0,
    )

def render_pronunciation_card(item, key_prefix):
    st.markdown(f"### {item['chu']}")
    st.write(item["hdsd"])
    st.write(f"Ví dụ: **{item['vd_han']}** — *{item['vd_py']}*.")
    if st.button("🔊 Nghe ví dụ", key=f"{key_prefix}_{item['chu']}"):
        play_audio(item["nghe"])

def render_lesson_intro(title, objective):
    st.header(title)
    st.markdown(
        f"""
        <div class="lesson-card">
            <b>Mục tiêu</b><br/>
            <span class="lesson-muted">{objective}</span>
        </div>
        """,
        unsafe_allow_html=True,
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
            saved_val = st.session_state.get(key)
            default_idx = 0
            if saved_val in choices:
                default_idx = choices.index(saved_val)
                
            selected = st.radio(
                f"Câu {idx + 1}: {item['q']}?",
                choices,
                index=default_idx,
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
