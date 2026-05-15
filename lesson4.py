import streamlit as st
from lessons_data import *
from ui_utils import *

def show_lesson4_finals():
    render_lesson_intro("📚 Bài 4: Vận mẫu kép mở rộng", "Học các vận mẫu kép mở rộng và quy tắc ghép âm nâng cao.")
    for g in B2_VAN_MAU_KEP_DATA:
        st.markdown(f"#### {g['nhom']}")
        cols = st.columns(4)
        for i, item in enumerate(g["items"]):
            with cols[i%4]: render_pronunciation_card(item, "b4_vk")

def show_lesson4_exercises(save_progress):
    st.header("📝 Bài 4: Bài tập vận mẫu kép mở rộng")
    st.info("Phần bài tập đang được soạn thảo...")
