import streamlit as st
from lessons_data import *
from ui_utils import *

def show_lesson3_pinyin():
    render_lesson_intro("🔒 Bài 3: Thanh mẫu nâng cao & Biến điệu", "Học các thanh mẫu khó (Âm mặt lưỡi, đầu lưỡi) và quy tắc biến điệu của 不.")
    for g in B2_THANH_MAU_DATA:
        st.markdown(f"#### {g['ten']}")
        cols = st.columns(4)
        for i, item in enumerate(g["items"]):
            with cols[i%4]: render_pronunciation_card(item, "b3_tm")
    
    st.markdown("---")
    st.subheader("3. Biến điệu của '不' (bù)")
    st.info("""
    **Quy tắc:**
    - **Giữ nguyên thanh 4 (bù):** Khi đứng một mình hoặc đứng trước âm tiết mang **thanh 1, thanh 2, thanh 3**.
    - **Biến thành thanh 2 (bú):** Khi đứng trước âm tiết mang **thanh 4**.
    """)
    
    col_ex1, col_ex2 = st.columns(2)
    with col_ex1:
        st.success("**Ví dụ biến thành thanh 2 (bú):**")
        st.write("- bù qù → **bú qù** (不去: không đi)")
        st.write("- bù shì → **bú shì** (不是: không phải)")
    with col_ex2:
        st.warning("**Ví dụ giữ nguyên thanh 4 (bù):**")
        st.write("- bù nán (不难: không khó) - *Thanh 2*")
        st.write("- bù hē (不喝: không uống) - *Thanh 1*")
        st.write("- bù hǎo (不好: không tốt) - *Thanh 3*")
    
    st.markdown("#### Luyện tập thêm:")
    col_ex3, col_ex4 = st.columns(2)
    with col_ex3:
        st.write("- bù gāo (不高: không cao)")
        st.write("- bù lái (不来: không đến)")
    with col_ex4:
        st.write("- bù xiǎo (不小: không nhỏ)")
        st.write("- bù mang (不忙: không bận)")

def show_lesson3_hanzi():
    render_lesson_intro("🔒 Bài 3: Nét chữ Hán cơ bản", "Rèn nét cơ bản và quy tắc thứ tự nét.")
    st.table(NET_CO_BAN)
