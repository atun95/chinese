import streamlit as st
import random
import json
import csv
from datetime import datetime
from pathlib import Path
from lessons_data import *
from ui_utils import *

# Import các bài học đã tách file
import lesson1
import lesson2
import lesson3
import lesson4

# Cấu hình trang
st.set_page_config(page_title="Học Tiếng Trung", page_icon="🇨🇳", layout="wide")
st.markdown(
    """
    <style>
    .block-container { padding-top: 1.1rem; }
    .lesson-card {
        border: 1px solid #e5e7eb; border-radius: 12px;
        padding: 12px 14px; margin-bottom: 10px; background-color: #fafafa;
    }
    .lesson-card b { font-size: 1.02rem; }
    .lesson-muted { color: #6b7280; }
    .chinese-table { width: 100%; border-collapse: collapse; margin-top: 10px; background-color: white; }
    .chinese-table th, .chinese-table td { border: 1px solid #ddd; padding: 8px; text-align: left; }
    .tm-header { background-color: #0f172a; color: white; }
    .vm-header { background-color: #fbbf24; color: #0f172a; }
    .cat-col { font-weight: bold; background-color: #f8fafc; }
    .pinyin-text { font-family: 'Courier New', monospace; font-weight: bold; }
    section[data-testid="stSidebar"] textarea {
        resize: both !important;
        min-height: 300px !important;
        min-width: 100% !important;
        font-size: 1rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- KHỞI TẠO & BIẾN TOÀN CỤC ---
if "scores" not in st.session_state:
    st.session_state.scores = {}

SCORES_FILE = Path(__file__).with_name("scores.csv")
SCORES_B2_FILE = Path(__file__).with_name("scores_b2.csv")
SCORES_B3_FILE = Path(__file__).with_name("scores_b3.csv")
PROGRESS_FILE = Path(__file__).with_name("progress_lesson1.json")

def save_progress():
    try:
        quiz_keys = [k for k in st.session_state.keys() if k.startswith(("bai", "vanmau_", "docviet_", "tone_", "cau_ngan_", "q2_", "b2_", "b3_", "student_name"))]
        data = {"scores": st.session_state.scores, "values": {k: st.session_state[k] for k in quiz_keys}}
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e: print(f"Lỗi lưu tiến độ: {e}")

def load_progress():
    if PROGRESS_FILE.exists():
        try:
            with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if "scores" in data: st.session_state.scores = data["scores"]
                if "values" in data:
                    for k, v in data["values"].items(): st.session_state[k] = v
        except Exception as e: print(f"Lỗi tải tiến độ: {e}")

def save_score_row(row_data):
    file_exists = SCORES_FILE.exists()
    try:
        with open(SCORES_FILE, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["thời gian", "học viên", "tổng điểm", "BT1: Từ vựng", "BT2: Âm bật hơi", "BT3: Vận mẫu", "BT4: Pinyin", "BT5: Nghe", "BT6: Câu ngắn"])
            if not file_exists: writer.writeheader()
            writer.writerow(row_data)
        return True
    except Exception as e:
        st.error(f"Lỗi khi lưu file CSV: {e}"); return False

def load_all_scores():
    if not SCORES_FILE.exists(): return []
    with open(SCORES_FILE, "r", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def save_score_row_b2(row_data):
    file_exists = SCORES_B2_FILE.exists()
    try:
        with open(SCORES_B2_FILE, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["thời gian", "học viên", "tổng điểm", "BT1: Từ vựng", "BT2: Nghe", "BT3: Điền âm"])
            if not file_exists: writer.writeheader()
            writer.writerow(row_data)
        return True
    except Exception as e:
        st.error(f"Lỗi khi lưu file CSV Bài 2: {e}"); return False

def load_all_scores_b2():
    if not SCORES_B2_FILE.exists(): return []
    with open(SCORES_B2_FILE, "r", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def save_score_row_b3(row_data):
    file_exists = SCORES_B3_FILE.exists()
    try:
        with open(SCORES_B3_FILE, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["thời gian", "học viên", "tổng điểm", "BT1: Từ vựng", "BT2: Chính tả", "BT3: Điền âm", "BT4: Luyện nghe", "BT5: Hội thoại"])
            if not file_exists: writer.writeheader()
            writer.writerow(row_data)
        return True
    except Exception as e:
        st.error(f"Lỗi khi lưu file CSV Bài 3: {e}"); return False

def load_all_scores_b3():
    if not SCORES_B3_FILE.exists(): return []
    with open(SCORES_B3_FILE, "r", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def add_tones(base):
    vowels = {'a':['ā','á','ǎ','à'], 'o':['ō','ó','ǒ','ò'], 'e':['ē','é','ě','è'], 'i':['ī','í','ǐ','ì'], 'u':['ū','ú','ǔ','ù'], 'ü':['ǖ','ǘ','ǚ','ǜ']}
    tones = []
    for i in range(4):
        res = base
        for v, syms in vowels.items():
            if v in res:
                if (v=='u' and 'iu' in res) or (v=='i' and 'ui' in res): continue
                res = res.replace(v, syms[i]); break
        tones.append(res)
    return tones

# Chỉ tải tiến độ một lần khi khởi tạo session
if "initialized" not in st.session_state:
    load_progress()
    st.session_state.initialized = True

# --- GIAO DIỆN CHÍNH ---
st.title("Học Pinyin Cơ Bản")
st.sidebar.header("Danh mục giáo án")
teacher_unlock = st.sidebar.checkbox("Nội dung Bài học")
menu = st.sidebar.radio("Chọn mục:", [
    "Bài 1 - Phiên âm cơ bản", 
    "Bài 1 - TỪ VỰNG CƠ BẢN", 
    "Bài 1 - Bài tập", 
    "Bài 2 - Vận mẫu kép & Luyện tập", 
    "Bài 2 - Bài tập", 
    "Bài 3 - Phiên âm nâng cao", 
    "Bài 3 - Quy tắc viết Pinyin",
    "Bài 3 - Luyện tập ghép âm",
    "Bài 3 - Văn hóa gọi tên & Cấu trúc câu",
    "Bài 3 - TỪ VỰNG",
    "Bài 3 - Hội thoại thực hành",
    "Bài 3 - Bài tập",
    "Bài 4 - Vận mẫu kép mở rộng",
    "Bài 4 - Phân biệt từ vựng chỉ Nữ giới (đang khóa)",
    "Bài 4 - Nét chữ Hán cơ bản (đang khóa)",
    "Bài 4 - Bài tập (đang khóa)"
])

if menu == "Bài 1 - Phiên âm cơ bản":
    lesson1.show_lesson1_intro()

elif menu == "Bài 1 - TỪ VỰNG CƠ BẢN":
    lesson1.show_lesson1_vocab()

elif menu == "Bài 1 - Bài tập":
    lesson1.show_lesson1_exercises(save_progress, save_score_row, load_all_scores)

elif menu == "Bài 2 - Vận mẫu kép & Luyện tập":
    lesson2.show_lesson2_intro(add_tones)

elif menu == "Bài 2 - Bài tập":
    lesson2.show_lesson2_exercises(save_progress, save_score_row_b2, load_all_scores_b2)

elif menu == "Bài 3 - Phiên âm nâng cao":
    lesson3.show_lesson3_pinyin()

elif menu == "Bài 3 - Quy tắc viết Pinyin":
    lesson3.show_lesson3_pinyin_rules()

elif menu == "Bài 3 - Luyện tập ghép âm":
    lesson3.show_lesson3_practice(add_tones)

elif menu == "Bài 3 - TỪ VỰNG":
    lesson3.show_lesson3_vocab()

elif menu == "Bài 3 - Văn hóa gọi tên & Cấu trúc câu":
    lesson3.show_lesson3_culture_grammar()

elif menu == "Bài 3 - Hội thoại thực hành":
    lesson3.show_lesson3_dialogues()

elif menu == "Bài 3 - Bài tập":
    lesson3.show_lesson3_exercises(save_progress, save_score_row_b3, load_all_scores_b3)

elif menu == "Bài 4 - Vận mẫu kép mở rộng":
    lesson4.show_lesson4_finals()

elif menu == "Bài 4 - Phân biệt từ vựng chỉ Nữ giới (đang khóa)":
    if not teacher_unlock: st.warning("Đang khóa.")
    else: lesson4.show_lesson4_female_comparison()

elif menu == "Bài 4 - Nét chữ Hán cơ bản (đang khóa)":
    if not teacher_unlock: st.warning("Đang khóa.")
    else: lesson4.show_lesson4_hanzi()

elif menu == "Bài 4 - Bài tập (đang khóa)":
    if not teacher_unlock: st.warning("Đang khóa.")
    else: lesson4.show_lesson4_exercises(save_progress)

st.sidebar.markdown("---")
st.sidebar.markdown("#### 📝 Ghi chú giáo viên")
note_key = "teacher_note"
if note_key not in st.session_state:
    st.session_state[note_key] = ""
st.session_state[note_key] = st.sidebar.text_area(
    "Nhập ghi chú:",
    value=st.session_state[note_key],
    height=300,
    key="teacher_note_area",
    placeholder="Nhập nội dung muốn hiển thị cho học viên..."
)
st.sidebar.markdown("---")
st.sidebar.write("加油! (Jiā yóu! - Cố lên!)")
