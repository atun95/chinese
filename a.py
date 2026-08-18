import streamlit as st
import random
import streamlit.components.v1 as components
import json
import csv
import shutil
import sys
from datetime import datetime
from pathlib import Path

# Thêm thư mục lessons vào sys.path để import các bài học
sys.path.append(str(Path(__file__).parent / "lessons"))

from lessons.lessons_data import *
from ui_utils import *


# Import các bài học đã tách file và reload để tránh cache
import importlib
import lessons.lessons_data as lessons_data
import lessons.lesson1 as lesson1
import lessons.lesson2 as lesson2
import lessons.lesson3 as lesson3
import lessons.lesson4 as lesson4
import lessons.lesson5 as lesson5
import lessons.lesson6 as lesson6
import lessons.lesson7 as lesson7
import lessons.lesson8 as lesson8
import sys
if 'lessons.lesson9' in sys.modules:
    del sys.modules['lessons.lesson9']
if 'lesson9' in sys.modules:
    del sys.modules['lesson9']
import lessons.lesson9 as lesson9
import lessons.hsk1_quiz as hsk1_quiz


try:
    importlib.reload(lessons_data)
except Exception as e:
    pass

try:
    importlib.reload(hsk1_quiz)
except Exception as e:
    pass

try:
    importlib.reload(lesson1)
except Exception as e:
    pass

try:
    importlib.reload(lesson2)
except Exception as e:
    pass

try:
    importlib.reload(lesson3)
except Exception as e:
    pass

try:
    importlib.reload(lesson4)
except Exception as e:
    pass

try:
    importlib.reload(lesson5)
except Exception as e:
    pass

try:
    importlib.reload(lesson6)
except Exception as e:
    pass

try:
    importlib.reload(lesson7)
except Exception as e:
    pass

try:
    importlib.reload(lesson8)
except Exception as e:
    pass

try:
    importlib.reload(lesson9)
except Exception as e:
    st.error(f'Error reloading lesson9: {e}')


def show_consolidated_flashcards():
    import os
    import streamlit.components.v1 as components
    
    # Path to the standalone HTML app
    app_path = "Flashcard_Offline.html"
    
    # If the app doesn't exist, generate it dynamically first
    if not os.path.exists(app_path) or os.path.getsize(app_path) == 0:
        with st.spinner("Đang tạo ứng dụng thẻ từ ôn tập..."):
            try:
                import flashcard_generator
                flashcard_generator.generate_vocabulary()
            except Exception as e:
                st.error(f"Lỗi khi khởi tạo thẻ từ: {e}")
                return

    # Render Header without description
    render_lesson_intro("🎴 HSK 1 - THẺ TỪ ÔN TẬP TỰ VỰNG")

    # Embed Flashcard_Offline.html using Streamlit components
    try:
        with open(app_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        components.html(html_content, height=850, scrolling=True)
    except Exception as e:
        st.error(f"Lỗi khi hiển thị ứng dụng: {e}")


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

# Lưu trữ điểm số và tiến trình ở thư mục Home để không bị mất khi cập nhật code
USER_DATA_DIR = Path.home() / ".chinese_learning_app"
USER_DATA_DIR.mkdir(parents=True, exist_ok=True)

SCORES_FILE = USER_DATA_DIR / "scores.csv"
SCORES_B2_FILE = USER_DATA_DIR / "scores_b2.csv"
SCORES_B3_FILE = USER_DATA_DIR / "scores_b3.csv"
SCORES_B4_FILE = USER_DATA_DIR / "scores_b4.csv"
SCORES_B5_FILE = USER_DATA_DIR / "scores_b5.csv"
SCORES_B5_3_FILE = USER_DATA_DIR / "scores_b5_3.csv"
SCORES_B6_1_FILE = USER_DATA_DIR / "scores_b6_1.csv"
SCORES_B6_2_FILE = USER_DATA_DIR / "scores_b6_2.csv"
SCORES_B7_1_FILE = USER_DATA_DIR / "scores_b7_1.csv"
SCORES_B7_2_FILE = USER_DATA_DIR / "scores_b7_2.csv"
SCORES_B7_3_FILE = USER_DATA_DIR / "scores_b7_3.csv"
SCORES_B7_4_FILE = USER_DATA_DIR / "scores_b7_4.csv"
SCORES_B7_5_FILE = USER_DATA_DIR / "scores_b7_5.csv"
SCORES_B7_6_FILE = USER_DATA_DIR / "scores_b7_6.csv"
SCORES_HSK1_CONSOLIDATED_FILE = USER_DATA_DIR / "scores_hsk1_consolidated.csv"
PROGRESS_FILE = USER_DATA_DIR / "progress_lesson1.json"

# Sao chép các file cũ từ thư mục dự án sang thư mục Home (nếu có và chưa tồn tại ở thư mục Home)
for filename in ["scores.csv", "scores_b2.csv", "scores_b3.csv", "scores_b4.csv", "scores_b5.csv", "scores_b5_3.csv", "scores_b6_1.csv", "scores_b6_2.csv", "scores_b7_1.csv", "scores_b7_2.csv", "scores_b7_3.csv", "scores_b7_4.csv", "scores_b7_5.csv", "scores_b7_6.csv", "scores_hsk1_consolidated.csv", "progress_lesson1.json"]:
    local_file = Path(__file__).parent / filename
    dest_file = USER_DATA_DIR / filename
    if local_file.exists() and not dest_file.exists():
        try:
            shutil.copy2(local_file, dest_file)
        except Exception as e:
            print(f"Lỗi copy file dữ liệu cũ {filename}: {e}")

def save_progress():
    try:
        quiz_keys = [k for k in st.session_state.keys() if k.startswith(("bai", "vanmau_", "docviet_", "tone_", "cau_ngan_", "q2_", "b2_", "b3_", "b4_", "b5_", "b6", "b7", "v6", "v7", "radio_pr_", "student_name"))]
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

def save_score_row_b4(row_data):
    file_exists = SCORES_B4_FILE.exists()
    new_fields = ["thời gian", "học viên", "tổng điểm", "BT1: Luyện nghe", "BT2: Chính tả", "BT3: Pinyin Quiz"]
    
    if file_exists:
        try:
            with open(SCORES_B4_FILE, "r", newline="", encoding="utf-8-sig") as f:
                reader = csv.DictReader(f)
                headers = reader.fieldnames
            
            if headers and ("BT3: Lắp ráp Bính âm" in headers or "BT4: Phân biệt Nữ giới" in headers):
                rows = []
                with open(SCORES_B4_FILE, "r", newline="", encoding="utf-8-sig") as f:
                    reader = csv.DictReader(f)
                    for r in reader:
                        new_row = {
                            "thời gian": r.get("thời gian", ""),
                            "học viên": r.get("học viên", ""),
                            "tổng điểm": r.get("tổng điểm", ""),
                            "BT1: Luyện nghe": r.get("BT1: Luyện nghe", ""),
                            "BT2: Chính tả": r.get("BT2: Chính tả", ""),
                            "BT3: Pinyin Quiz": r.get("BT3: Lắp ráp Bính âm", "") or r.get("BT3: Pinyin Quiz", "")
                        }
                        rows.append(new_row)
                
                with open(SCORES_B4_FILE, "w", newline="", encoding="utf-8-sig") as f:
                    writer = csv.DictWriter(f, fieldnames=new_fields)
                    writer.writeheader()
                    writer.writerows(rows)
        except Exception as e:
            print(f"Lỗi di trú file CSV Bài 4: {e}")

    try:
        with open(SCORES_B4_FILE, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=new_fields)
            if not SCORES_B4_FILE.exists() or SCORES_B4_FILE.stat().st_size == 0:
                writer.writeheader()
            writer.writerow(row_data)
        return True
    except Exception as e:
        st.error(f"Lỗi khi lưu file CSV Bài 4: {e}"); return False

def load_all_scores_b4():
    if not SCORES_B4_FILE.exists(): return []
    with open(SCORES_B4_FILE, "r", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def save_score_row_b5(row_data):
    file_exists = SCORES_B5_FILE.exists()
    try:
        with open(SCORES_B5_FILE, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["thời gian", "học viên", "tổng điểm", "BT1: Từ vựng", "BT2: Nghe", "BT3: Điền âm"])
            if not file_exists: writer.writeheader()
            writer.writerow(row_data)
        return True
    except Exception as e:
        st.error(f"Lỗi khi lưu file CSV Bài 5.2: {e}"); return False

def load_all_scores_b5():
    if not SCORES_B5_FILE.exists(): return []
    with open(SCORES_B5_FILE, "r", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def save_score_row_b5_3(row_data):
    file_exists = SCORES_B5_3_FILE.exists()
    try:
        with open(SCORES_B5_3_FILE, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["thời gian", "học viên", "tổng điểm", "BT: Trắc nghiệm"])
            if not file_exists: writer.writeheader()
            writer.writerow(row_data)
        return True
    except Exception as e:
        st.error(f"Lỗi khi lưu file CSV Bài 5.3: {e}"); return False

def load_all_scores_b5_3():
    if not SCORES_B5_3_FILE.exists(): return []
    with open(SCORES_B5_3_FILE, "r", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def save_score_row_b6_1(row_data):
    file_exists = SCORES_B6_1_FILE.exists()
    try:
        with open(SCORES_B6_1_FILE, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["thời gian", "học viên", "tổng điểm", "BT: Ghép câu"])
            if not file_exists: writer.writeheader()
            writer.writerow(row_data)
        return True
    except Exception as e:
        st.error(f"Lỗi khi lưu file CSV Bài 6.1: {e}"); return False

def load_all_scores_b6_1():
    if not SCORES_B6_1_FILE.exists(): return []
    with open(SCORES_B6_1_FILE, "r", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def save_score_row_b6_2(row_data):
    file_exists = SCORES_B6_2_FILE.exists()
    try:
        with open(SCORES_B6_2_FILE, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["thời gian", "học viên", "tổng điểm", "BT: Đứng độc lập"])
            if not file_exists: writer.writeheader()
            writer.writerow(row_data)
        return True
    except Exception as e:
        st.error(f"Lỗi khi lưu file CSV Bài 6.2: {e}"); return False

def load_all_scores_b6_2():
    if not SCORES_B6_2_FILE.exists(): return []
    with open(SCORES_B6_2_FILE, "r", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def save_score_row_b7_1(row_data):
    file_exists = SCORES_B7_1_FILE.exists()
    try:
        with open(SCORES_B7_1_FILE, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["thời gian", "học viên", "tổng điểm", "BT: Từ để hỏi"])
            if not file_exists: writer.writeheader()
            writer.writerow(row_data)
        return True
    except Exception as e:
        st.error(f"Lỗi khi lưu file CSV Bài 7.1: {e}"); return False

def load_all_scores_b7_1():
    if not SCORES_B7_1_FILE.exists(): return []
    with open(SCORES_B7_1_FILE, "r", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def save_score_row_b7_2(row_data):
    file_exists = SCORES_B7_2_FILE.exists()
    try:
        with open(SCORES_B7_2_FILE, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["thời gian", "học viên", "tổng điểm", "BT: Chữ 的"])
            if not file_exists: writer.writeheader()
            writer.writerow(row_data)
        return True
    except Exception as e:
        st.error(f"Lỗi khi lưu file CSV Bài 7.2: {e}"); return False

def load_all_scores_b7_2():
    if not SCORES_B7_2_FILE.exists(): return []
    with open(SCORES_B7_2_FILE, "r", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def save_score_row_b7_3(row_data):
    file_exists = SCORES_B7_3_FILE.exists()
    try:
        with open(SCORES_B7_3_FILE, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["thời gian", "học viên", "tổng điểm", "BT: Cặp từ 这/那"])
            if not file_exists: writer.writeheader()
            writer.writerow(row_data)
        return True
    except Exception as e:
        st.error(f"Lỗi khi lưu file CSV Bài 7.3: {e}"); return False

def load_all_scores_b7_3():
    if not SCORES_B7_3_FILE.exists(): return []
    with open(SCORES_B7_3_FILE, "r", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def save_score_row_b7_4(row_data):
    file_exists = SCORES_B7_4_FILE.exists()
    try:
        with open(SCORES_B7_4_FILE, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["thời gian", "học viên", "tổng điểm", "BT: Từ 在"])
            if not file_exists: writer.writeheader()
            writer.writerow(row_data)
        return True
    except Exception as e:
        st.error(f"Lỗi khi lưu file CSV Bài 7.4: {e}"); return False

def load_all_scores_b7_4():
    if not SCORES_B7_4_FILE.exists(): return []
    with open(SCORES_B7_4_FILE, "r", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def save_score_row_b7_5(row_data):
    file_exists = SCORES_B7_5_FILE.exists()
    try:
        with open(SCORES_B7_5_FILE, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["thời gian", "học viên", "tổng điểm", "BT: Từ 去"])
            if not file_exists: writer.writeheader()
            writer.writerow(row_data)
        return True
    except Exception as e:
        st.error(f"Lỗi khi lưu file CSV Bài 7.5: {e}"); return False

def load_all_scores_b7_5():
    if not SCORES_B7_5_FILE.exists(): return []
    with open(SCORES_B7_5_FILE, "r", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def save_score_row_b7_6(row_data):
    file_exists = SCORES_B7_6_FILE.exists()
    try:
        with open(SCORES_B7_6_FILE, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["thời gian", "học viên", "tổng điểm", "BT: Cặp từ 些/点"])
            if not file_exists: writer.writeheader()
            writer.writerow(row_data)
        return True
    except Exception as e:
        st.error(f"Lỗi khi lưu file CSV Bài 7.6: {e}"); return False

def load_all_scores_b7_6():
    if not SCORES_B7_6_FILE.exists(): return []
    with open(SCORES_B7_6_FILE, "r", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def save_score_row_hsk1_consolidated(row_data):
    file_exists = SCORES_HSK1_CONSOLIDATED_FILE.exists()
    try:
        with open(SCORES_HSK1_CONSOLIDATED_FILE, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["thời gian", "học viên", "Đề kiểm tra", "tổng điểm", "Kết quả"])
            if not file_exists: writer.writeheader()
            writer.writerow(row_data)
        return True
    except Exception as e:
        st.error(f"Lỗi khi lưu file CSV Trắc nghiệm HSK 1: {e}"); return False

def load_all_scores_hsk1_consolidated():
    if not SCORES_HSK1_CONSOLIDATED_FILE.exists(): return []
    with open(SCORES_HSK1_CONSOLIDATED_FILE, "r", newline="", encoding="utf-8-sig") as f:
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

# Tích hợp CSS in ấn
st.markdown(
    """
    <style>
    @media print {
        section[data-testid="stSidebar"] {
            display: none !important;
        }
        header, footer, [data-testid="stHeader"], [data-testid="stFooter"] {
            display: none !important;
        }
        [data-testid="column"]:has(button[key="btn_print_lesson"]), .stButton, button, iframe, .note-fab, #teacher-floating-note {
            display: none !important;
        }
        .block-container {
            padding-top: 0 !important;
            padding-bottom: 0 !important;
            padding-left: 20px !important;
            padding-right: 20px !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.header("Danh mục giáo án")

mode = st.sidebar.selectbox("Khu vực học tập:", ["📚 Lý thuyết & Bài học", "📖 Hệ thống từ vựng", "🗣️ Luyện tập ghép âm", "🗣️ Thực hành trên lớp", "📝 Hệ thống bài tập", "📝 Trắc nghiệm Tổng hợp HSK 1", "🎴 HSK 1 - THẺ TỪ ÔN TẬP TỰ VỰNG", "🖨️ In ấn & Đồng bộ"])

menu = None
if mode == "📚 Lý thuyết & Bài học":
    menu = st.sidebar.radio("Chọn bài học:", [
        "Bài 1.1 - Bảng tổng hợp Thanh mẫu & Vận mẫu",
        "Bài 1.2 - Thanh mẫu và vận mẫu đơn",
        "Bài 2.1 - Vận mẫu kép",
        "Bài 3.1 - Thanh mẫu", 
        "Bài 3.2 - Quy tắc viết Pinyin",
        "Bài 3.3 - Văn hóa gọi tên & Cấu trúc câu",
        "Bài 4.1 - Vận mẫu kép",
        "Bài 4.2 - Phân biệt từ vựng chỉ Nữ giới",
        "Bài 5.1 - Số đếm từ 0 đến 10",
        "Bài 5.2 - Vận mẫu mũi",
        "Bài 5.3 - Cách dùng 很 (hěn) & Phó từ chỉ mức độ",
        "Bài 5.4 - Tết Đoan Ngọ (端午节)",
        "Bài 6.1 - Các vận mẫu mũi còn lại",
        "Bài 6.2 - Vận mẫu đứng một mình",
        "Bài 7.1 - Các từ để hỏi",
        "Bài 7.2 - Cách dùng chữ 的 (de)",
        "Bài 7.3 - Cặp từ 这 và 那",
        "Bài 7.4 - Từ 在 (zài)",
        "Bài 7.5 - Từ 去 (qù)",
        "Bài 7.6 - Cặp từ 些 và 点",
        "Bài 8.1 - Tổng quan Chữ Hán",
        "Bài 8.2 - Hệ thống Nét viết",
        "Bài 8.3 - Quy tắc Bút thuận",
        "Bài 8.4 - Hệ thống Bộ thủ",
        "Bài 8.5 - Đơn thể & Hợp thể",
        "Bài 9.1 - Quốc gia, Quốc tịch và Tiền tệ"
    ])
elif mode == "📖 Hệ thống từ vựng":
    menu = st.sidebar.radio("Chọn bảng từ vựng:", [
        "Bài 1 - TỪ VỰNG CƠ BẢN", 
        "Bài 3 - TỪ VỰNG",
        "Bài 4 - TỪ VỰNG",
        "Bài 4.1 - Từ vựng mở rộng",
        "Bài 5 - TỪ VỰNG",
        "Bài 6 - TỪ VỰNG",
        "Bài 7 - TỪ VỰNG"
    ])
elif mode == "🗣️ Luyện tập ghép âm":
    menu = st.sidebar.radio("Chọn bảng ghép âm:", [
        "Ghép âm Bài 2 - Vận mẫu kép cơ bản",
        "Ghép âm Bài 3 - Thanh mẫu nâng cao",
        "Ghép âm Bài 4 - Vận mẫu kép mở rộng",
        "Ghép âm Bài 5 - Vận mẫu mũi",
        "Ghép âm Bài 6 - Vận mẫu mũi phức hợp"
    ])
elif mode == "🗣️ Thực hành trên lớp":
    menu = st.sidebar.radio("Chọn hoạt động:", [
        "Bài 3.1 - Hội thoại thực hành",
        "Bài 4.1 - Đấu trường Luyện tập",
        "Bài 4.2 - Phản xạ & Giao tiếp",
        "Bài 5.1 - Thực hành Giao tiếp & Phản xạ",
        "Bài 6.1 - Thực hành Giao tiếp & Phản xạ",
        "Bài 9.1 - Thực hành Giao tiếp & Phản xạ"
    ])
elif mode == "📝 Hệ thống bài tập":
    menu = st.sidebar.radio("Chọn bài tập:", [
        "Bài tập Bài 1",
        "Bài tập Bài 2",
        "Bài tập Bài 3",
        "Bài tập Bài 4",
        "Bài tập Bài 5",
        "Bài tập Bài 6.1",
        "Bài tập Bài 6.2",
        "Bài tập Bài 7.1",
        "Bài tập Bài 7.2",
        "Bài tập Bài 7.3",
        "Bài tập Bài 7.4",
        "Bài tập Bài 7.5",
        "Bài tập Bài 7.6"
    ])

if mode == "🎴 HSK 1 - THẺ TỪ ÔN TẬP TỰ VỰNG":
    show_consolidated_flashcards()

elif mode == "📝 Trắc nghiệm Tổng hợp HSK 1":
    hsk1_quiz.show_hsk1_consolidated_quiz(save_progress, save_score_row_hsk1_consolidated, load_all_scores_hsk1_consolidated)

elif mode == "🖨️ In ấn & Đồng bộ":
    
    if st.button("🔄 Đồng bộ & Cập nhật giáo trình", type="primary", use_container_width=True):
        try:
            import build_giao_trinh
            importlib.reload(build_giao_trinh)
            build_giao_trinh.build_individual_lessons()
            
            # Also regenerate vocabulary JSON, CSV and print HTML
            import flashcard_generator
            importlib.reload(flashcard_generator)
            flashcard_generator.generate_vocabulary()
            
            st.success("Đồng bộ thành công! Các bài học và danh sách từ vựng đã được cập nhật và sẵn sàng tải xuống.")
        except Exception as e:
            st.error(f"Có lỗi xảy ra khi đồng bộ: {e}")
            
    st.subheader("📁 Danh sách tài liệu học tập:")
    
    import os
    import re
    output_dir = "giao_trinh_in_an"
    if os.path.exists(output_dir):
        files = sorted(os.listdir(output_dir))
        if files:
            # Combined file option
            combined_path = "giao_trinh_in_an.html"
            if os.path.exists(combined_path):
                try:
                    with open(combined_path, "r", encoding="utf-8") as f_data:
                        combined_bytes = f_data.read()
                except Exception as e:
                    combined_bytes = f"Error reading combined file: {e}"
                
                col_file, col_dl = st.columns([7, 3])
                with col_file:
                    st.markdown("**🎴 In toàn bộ giáo trình (File gộp)** (`giao_trinh_in_an.html`)")
                with col_dl:
                    st.download_button(
                        label="📥 Tải file gộp",
                        data=combined_bytes,
                        file_name="giao_trinh_in_an.html",
                        mime="text/html",
                        key="dl_combined_giao_trinh"
                    )
                st.markdown("---")
            
            # Vocabulary Print file option
            vocab_print_path = os.path.join("assets", "vocabulary_print.html")
            if not os.path.exists(vocab_print_path):
                try:
                    import flashcard_generator
                    flashcard_generator.generate_vocabulary()
                except Exception as e:
                    pass
            
            if os.path.exists(vocab_print_path):
                try:
                    with open(vocab_print_path, "r", encoding="utf-8") as f_data:
                        vocab_bytes = f_data.read()
                except Exception as e:
                    vocab_bytes = f"Error reading vocabulary print file: {e}"
                
                col_file, col_dl = st.columns([7, 3])
                with col_file:
                    st.markdown("**🎴 In toàn bộ Từ vựng (Flashcard HTML)** (`vocabulary_print.html`)")
                with col_dl:
                    st.download_button(
                        label="📥 Tải bảng từ vựng",
                        data=vocab_bytes,
                        file_name="vocabulary_print.html",
                        mime="text/html",
                        key="dl_vocab_print_html"
                    )
                st.markdown("---")
            
            for f_name in files:
                filepath = os.path.join(output_dir, f_name)
                try:
                    with open(filepath, "r", encoding="utf-8") as f_data:
                        html_bytes = f_data.read()
                except Exception as e:
                    html_bytes = f"Error reading file: {e}"
                
                if "trang_bia" in f_name:
                    display_name = "🎴 Trang bìa và Mục lục"
                else:
                    num_match = re.search(r"bai_(\d+)", f_name)
                    if num_match:
                        display_name = f"📖 Giáo án Bài {num_match.group(1)}"
                    else:
                        display_name = f"📄 {f_name.replace('.html', '')}"
                
                col_file, col_dl = st.columns([7, 3])
                with col_file:
                    st.markdown(f"**{display_name}** (`{f_name}`)")
                with col_dl:
                    st.download_button(
                        label="📥 Tải file để in",
                        data=html_bytes,
                        file_name=f_name,
                        mime="text/html",
                        key=f"dl_{f_name}"
                    )
        else:
            st.info("Chưa có file nào được tạo. Nhấp vào nút đồng bộ ở trên để tạo file.")
    else:
        st.info("Thư mục in ấn chưa tồn tại. Nhấp vào nút đồng bộ ở trên để tạo.")

elif menu == "Bài 1.1 - Bảng tổng hợp Thanh mẫu & Vận mẫu":
    lesson1.show_lesson1_summary_table()

elif menu == "Bài 1.2 - Thanh mẫu và vận mẫu đơn":
    lesson1.show_lesson1_intro()

elif menu == "Bài 1 - TỪ VỰNG CƠ BẢN":
    lesson1.show_lesson1_vocab()

elif menu == "Bài tập Bài 1":
    lesson1.show_lesson1_exercises(save_progress, save_score_row, load_all_scores)

elif menu == "Bài 2.1 - Vận mẫu kép":
    lesson2.show_lesson2_intro(add_tones)

elif menu == "Ghép âm Bài 2 - Vận mẫu kép cơ bản":
    lesson2.show_lesson2_spelling(add_tones)

elif menu == "Ghép âm Bài 3 - Thanh mẫu nâng cao":
    lesson3.show_lesson3_practice(add_tones)

elif menu == "Ghép âm Bài 4 - Vận mẫu kép mở rộng":
    lesson4.show_lesson4_spelling(add_tones)

elif menu == "Bài tập Bài 2":
    lesson2.show_lesson2_exercises(save_progress, save_score_row_b2, load_all_scores_b2)

elif menu == "Bài 3.1 - Thanh mẫu":
    lesson3.show_lesson3_pinyin()

elif menu == "Bài 3.2 - Quy tắc viết Pinyin":
    lesson3.show_lesson3_pinyin_rules()

elif menu == "Bài 3.3 - Luyện tập ghép âm":
    lesson3.show_lesson3_practice(add_tones)

elif menu == "Bài 3 - TỪ VỰNG":
    lesson3.show_lesson3_vocab()

elif menu == "Bài 4 - TỪ VỰNG":
    lesson4.show_lesson4_vocab(extended_only=False)

elif menu == "Bài 4.1 - Từ vựng mở rộng":
    lesson4.show_lesson4_vocab(extended_only=True)

elif menu == "Bài 5 - TỪ VỰNG":
    lesson5.show_lesson5_vocab()

elif menu == "Bài 6 - TỪ VỰNG":
    lesson6.show_lesson6_vocab()

elif menu == "Bài 7 - TỪ VỰNG":
    lesson7.show_lesson7_vocab()



elif menu == "Bài 3.3 - Văn hóa gọi tên & Cấu trúc câu":
    lesson3.show_lesson3_culture_grammar()

elif menu == "Bài 3.1 - Hội thoại thực hành":
    lesson3.show_lesson3_dialogues()

elif menu == "Bài tập Bài 3":
    lesson3.show_lesson3_exercises(save_progress, save_score_row_b3, load_all_scores_b3)

elif menu == "Bài 4.1 - Vận mẫu kép":
    lesson4.show_lesson4_finals()

elif menu == "Bài 4.2 - Phân biệt từ vựng chỉ Nữ giới":
    lesson4.show_lesson4_female_comparison(save_progress)

elif menu == "Bài 4.1 - Đấu trường Luyện tập":
    lesson4.show_lesson4_classroom_arena()

elif menu == "Bài 4.2 - Phản xạ & Giao tiếp":
    # Hot-reload trigger: 2026-06-12 12:19
    lesson4.show_lesson4_qa_and_dialogues()

elif menu == "Bài 5.1 - Thực hành Giao tiếp & Phản xạ":
    lesson5.show_lesson5_classroom_practice()

elif menu == "Bài 6.1 - Thực hành Giao tiếp & Phản xạ":
    lesson6.show_lesson6_1_classroom_practice()
    
elif menu == "Bài 9.1 - Thực hành Giao tiếp & Phản xạ":
    lesson9.show_lesson9_1_classroom_practice()

elif menu == "Bài 6.2 - Vận mẫu đứng một mình" or menu == "Bài tập Bài 6.2":
    lesson6.show_lesson6_2_standalone_finals(save_progress, save_score_row_b6_2, load_all_scores_b6_2)

elif menu == "Bài 6.1 - Các vận mẫu mũi còn lại" or menu == "Bài tập Bài 6.1":
    lesson6.show_lesson6_1_nasal_finals(save_progress, save_score_row_b6_1, load_all_scores_b6_1)

elif menu == "Bài 7.1 - Các từ để hỏi" or menu == "Bài tập Bài 7.1":
    lesson7.show_lesson7_1_question_words(save_progress, save_score_row_b7_1, load_all_scores_b7_1)

elif menu == "Bài 7.2 - Cách dùng chữ 的 (de)" or menu == "Bài tập Bài 7.2":
    lesson7.show_lesson7_2_word_de(save_progress, save_score_row_b7_2, load_all_scores_b7_2)

elif menu == "Bài 7.3 - Cặp từ 这 và 那" or menu == "Bài tập Bài 7.3":
    lesson7.show_lesson7_3_zhe_na(save_progress, save_score_row_b7_3, load_all_scores_b7_3)

elif menu == "Bài 7.4 - Từ 在 (zài)" or menu == "Bài tập Bài 7.4":
    lesson7.show_lesson7_4_zai(save_progress, save_score_row_b7_4, load_all_scores_b7_4)

elif menu == "Bài 7.5 - Từ 去 (qù)" or menu == "Bài tập Bài 7.5":
    lesson7.show_lesson7_5_qu(save_progress, save_score_row_b7_5, load_all_scores_b7_5)

elif menu == "Bài 7.6 - Cặp từ 些 và 点" or menu == "Bài tập Bài 7.6":
    lesson7.show_lesson7_6_xie_dian(save_progress, save_score_row_b7_6, load_all_scores_b7_6)

elif menu == "Bài 8.1 - Tổng quan Chữ Hán":
    lesson8.show_lesson8_1_overview()

elif menu == "Bài 8.2 - Hệ thống Nét viết":
    lesson8.show_lesson8_2_strokes()

elif menu == "Bài 8.3 - Quy tắc Bút thuận":
    lesson8.show_lesson8_3_rules()

elif menu == "Bài 8.4 - Hệ thống Bộ thủ":
    lesson8.show_lesson8_4_radicals()

elif menu == "Bài 8.5 - Đơn thể & Hợp thể":
    lesson8.show_lesson8_5_structures()
    
elif menu == "Bài 9.1 - Quốc gia, Quốc tịch và Tiền tệ":
    lesson9.show_lesson9_1_countries_currency()

elif menu == "Bài 5.1 - Số đếm từ 0 đến 10":
    lesson5.show_lesson5_numbers()

elif menu == "Bài 5.2 - Vận mẫu mũi":
    lesson5.show_lesson5_nasal_finals(add_tones, save_progress, save_score_row_b5, load_all_scores_b5)

elif menu == "Bài 5.3 - Cách dùng 很 (hěn) & Phó từ chỉ mức độ":
    lesson5.show_lesson5_degree_adverbs(save_progress, save_score_row_b5_3, load_all_scores_b5_3)

elif menu == "Bài 5.4 - Tết Đoan Ngọ (端午节)":
    lesson5.show_lesson5_duanwu()

elif menu == "Ghép âm Bài 5 - Vận mẫu mũi":
    lesson5.show_lesson5_nasal_spelling(add_tones)

elif menu == "Ghép âm Bài 6 - Vận mẫu mũi phức hợp":
    lesson6.show_lesson6_spelling(add_tones)

elif menu == "Bài tập Bài 5":
    lesson5.show_lesson5_nasal_exercises(save_progress, save_score_row_b5, load_all_scores_b5)

elif menu == "Bài tập Bài 4":
    lesson4.show_lesson4_exercises(save_progress, save_score_row_b4, load_all_scores_b4)

st.sidebar.markdown("---")
st.sidebar.write("加油! (Jiā yóu! - Cố lên!)")

# --- HIỂN THỊ 2 POPUP NỔI ĐỘC LẬP: (1) GHI CHÚ GIÁO VIÊN & (2) TRA PINYIN TỪ VỰNG ---
components.html("""
<script>
(function(){
    var P = window.parent;
    var PD = P.document;

    // Remove old elements for hot-reloading
    var oldWrap = PD.getElementById('pg-popup-container');
    if(oldWrap) oldWrap.remove();
    var oldCss = PD.getElementById('pg-popup-css');
    if(oldCss) oldCss.remove();

    /* ---- INJECT CSS ---- */
    var st = PD.createElement('style');
    st.id = 'pg-popup-css';
    st.innerHTML = [
        "#pg-fab-note,#pg-fab-pinyin{position:fixed!important;width:52px;height:52px;border-radius:50%;border:none;outline:none;cursor:pointer;color:#fff;font-size:22px;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 20px rgba(0,0,0,.3);z-index:2147483647!important;pointer-events:auto!important;transition:transform .2s;}",
        "#pg-fab-note{bottom:24px;right:24px;background:linear-gradient(135deg,#f43f5e,#e11d48);}",
        "#pg-fab-pinyin{bottom:84px;right:24px;background:linear-gradient(135deg,#0284c7,#0369a1);}",
        "#pg-fab-note:hover,#pg-fab-pinyin:hover{transform:scale(1.12);}",
        "#pg-popup-note,#pg-popup-pinyin{position:fixed!important;border-radius:14px;box-shadow:0 12px 40px rgba(0,0,0,.22);display:flex;flex-direction:column;overflow:hidden;z-index:2147483646!important;pointer-events:auto!important;resize:both;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;}",
        "#pg-popup-note{top:80px;right:24px;width:340px;height:260px;min-width:240px;min-height:44px;border:2px solid #e11d48;background:#fff;}",
        "#pg-popup-pinyin{bottom:148px;right:24px;width:340px;height:280px;min-width:260px;min-height:44px;border:2px solid #0284c7;background:#fff;}",
        "#pg-popup-note.pg-min,#pg-popup-pinyin.pg-min{height:44px!important;resize:none!important;}",
        ".pg-hdr{display:flex;align-items:center;justify-content:space-between;padding:0 10px;height:44px;min-height:44px;cursor:move;user-select:none;flex-shrink:0;color:#fff;font-weight:700;font-size:13px;}",
        "#pg-popup-note .pg-hdr{background:#e11d48;}",
        "#pg-popup-pinyin .pg-hdr{background:linear-gradient(135deg,#0284c7,#0369a1);}",
        ".pg-btns{display:flex;gap:4px;}",
        ".pg-hdr button{background:rgba(255,255,255,.18);border:none;color:#fff;width:28px;height:28px;border-radius:6px;cursor:pointer;font-size:13px;font-weight:700;display:flex;align-items:center;justify-content:center;transition:background .15s;pointer-events:auto!important;}",
        ".pg-hdr button:hover{background:rgba(255,255,255,.38);}",
        ".pg-body{flex:1;display:flex;flex-direction:column;overflow:hidden;}",
        "#pg-note-ta{flex:1;width:100%;height:100%;border:none;outline:none;resize:none;padding:10px 12px;font-size:15px;line-height:1.6;color:#1e293b;font-family:inherit;background:#fff;}",
        ".pg-py-body{flex:1;display:flex;flex-direction:column;padding:8px;gap:6px;overflow:hidden;}",
        "#pg-py-inp{flex:1;width:100%;min-height:60px;border:1.5px solid #cbd5e1;border-radius:7px;padding:7px 10px;font-size:14px;font-family:inherit;outline:none;resize:none;box-sizing:border-box;transition:border-color .15s;}",
        "#pg-py-inp:focus{border-color:#0284c7;box-shadow:0 0 0 3px rgba(2,132,199,.12);}",
        "#pg-py-out{flex:1;overflow-y:auto;background:#f8fafc;border:1.5px solid #e2e8f0;border-radius:7px;padding:6px 10px;line-height:1.6;word-break:break-word;}",
        "#pg-py-copy-row{display:flex;justify-content:flex-end;flex-shrink:0;margin-top:6px;}",
        "#pg-py-copy{background:#0284c7;border:none;color:#fff;border-radius:7px;padding:5px 14px;font-size:12px;font-weight:700;cursor:pointer;pointer-events:auto!important;transition:background .15s;display:flex;align-items:center;gap:5px;}",
        "#pg-py-copy:hover{background:#0369a1;}",
        "#pg-py-copy.copied{background:#16a34a;}"
        ].join('');
        PD.head.appendChild(st);

    /* ---- INJECT HTML ---- */
    var html = [
        '<button id="pg-fab-note" title="Mở ghi chú">📝</button>',
        '<button id="pg-fab-pinyin" title="Mở tra Pinyin">🔤</button>',
        '<div id="pg-popup-note">',
        '  <div class="pg-hdr" id="pg-hdr-note">',
        '    <span>📌 Ghi chú giáo viên</span>',
        '    <div class="pg-btns">',
        '      <button id="pg-n-dec">A-</button>',
        '      <button id="pg-n-inc">A+</button>',
        '      <button id="pg-n-min">−</button>',
        '      <button id="pg-n-cls">✕</button>',
        '    </div>',
        '  </div>',
        '  <div class="pg-body"><textarea id="pg-note-ta" placeholder="Nhập ghi chú tại đây..."></textarea></div>',
        '</div>',
        '<div id="pg-popup-pinyin">',
        '  <div class="pg-hdr" id="pg-hdr-pinyin">',
        '    <span>🔤 Tra Pinyin Từ Vựng</span>',
        '    <div class="pg-btns">',
        '      <button id="pg-py-dec">A-</button>',
        '      <button id="pg-py-inc">A+</button>',
        '      <button id="pg-py-min">−</button>',
        '      <button id="pg-py-cls">✕</button>',
        '    </div>',
        '  </div>',
        '  <div class="pg-body">',
        '    <div class="pg-py-body">',
        '      <textarea id="pg-py-inp" placeholder="Nhập chữ Hán"></textarea>',
        '      <div id="pg-py-out"><span style="color:#94a3b8;font-style:italic;font-size:12px;">Pinyin </span></div>',
        '      <div id="pg-py-copy-row"><button id="pg-py-copy">📋 Copy Pinyin</button></div>',
        '    </div>',
        '  </div>',
        '</div>'
    ].join('\\n');

    var wrap = PD.createElement('div');
    wrap.id = 'pg-popup-container';
    wrap.innerHTML = html;
    PD.body.appendChild(wrap);

    /* ---- HELPERS ---- */
    function ls(k,d){ try{var v=localStorage.getItem(k);return v===null?d:v;}catch(e){return d;} }
    function ss(k,v){ try{localStorage.setItem(k,v);}catch(e){} }
    function el(id){ return PD.getElementById(id); }

    /* ---- LOAD PINYIN-PRO ---- */
    var pyLoaded = false;
    var pyDict = {'我':'wǒ','你':'nǐ','他':'tā','她':'tā','它':'tā','们':'men','好':'hǎo','是':'shì','在':'zài','不':'bù','有':'yǒu','这':'zhè','那':'nà','个':'gè','上':'shàng','下':'xià','人':'rén','大':'dà','小':'xiǎo','中':'zhōng','国':'guó','年':'nián','月':'yuè','日':'rì','老':'lǎo','师':'shī','学':'xué','校':'xiào','生':'shēng','同':'tóng','朋':'péng','友':'yǒu','家':'jiā','爸':'bà','妈':'mā','哥':'gē','姐':'jiě','弟':'dì','妹':'mèi','吃':'chī','喝':'hē','茶':'chá','水':'shuǐ','菜':'cài','饭':'fàn','果':'guǒ','苹':'píng','猫':'māo','狗':'gǒu','爱':'ài','喜':'xǐ','欢':'huān','想':'xiǎng','要':'yào','去':'qù','来':'lái','买':'mǎi','卖':'mài','看':'kàn','听':'tīng','说':'shuō','读':'dú','写':'xiě','字':'zì','汉':'hàn','语':'yǔ','英':'yīng','书':'shū','电':'diàn','脑':'nǎo','视':'shì','话':'huà','车':'chē','钱':'qián','块':'kuài','百':'bǎi','千':'qiān','一':'yī','二':'èr','三':'sān','四':'sì','五':'wǔ','六':'liù','七':'qī','八':'bā','九':'jiǔ','十':'shí','谢':'xiè','再':'zài','见':'jiàn','对':'duì','起':'qǐ','没':'méi','关':'guān','系':'xì','多':'duō','少':'shǎo','冷':'lěng','热':'rè','雨':'yǔ','高':'gāo','兴':'xìng','坐':'zuò','请':'qǐng','作':'zuò','业':'yè','桌':'zhuō','椅':'yǐ','衣':'yī','服':'fu','号':'hào','时':'shí','分':'fēn','点':'diǎn','天':'tiān','什':'shén','么':'me','哪':'nǎ','呢':'ne','吗':'ma','的':'de','了':'le','和':'hé','也':'yě','都':'dōu','很':'hěn','知':'zhī','道':'dào','名':'míng','岁':'suì'};

    var ps = PD.createElement('script');
    ps.src = 'https://cdn.jsdelivr.net/npm/pinyin-pro@3.19.6/dist/index.js';
    ps.onload = function(){ pyLoaded = true; renderPy(); };
    PD.head.appendChild(ps);

    function getpy(c){
        if(pyLoaded && P.pinyinPro && P.pinyinPro.pinyin){
            try{ var r=P.pinyinPro.pinyin(c,{toneType:'symbol',type:'array'}); if(r&&r[0]) return r[0]; }catch(e){}
        }
        return pyDict[c]||'';
    }

    function renderPy(){
        var inp=el('pg-py-inp'), out=el('pg-py-out'); if(!inp||!out) return;
        var txt=inp.value; ss('pg_py_txt',txt);
        if(!txt.trim()){out.innerHTML='<span style="color:#94a3b8;font-style:italic;font-size:12px;">Pinyin</span>'; out._pyText=''; return;}
        var p='';
        for(var i=0;i<txt.length;i++){
            var c=txt[i];
            if(c>='\\u4e00'&&c<='\\u9fa5') {
                var py = getpy(c);
                p += (py ? py + ' ' : c);
            } else {
                p += c;
            }
        }
        var result = p.replace(/ +\\n/g, '\\n').trim();
        out._pyText = result;
        out.innerHTML = result.replace(/\\n/g,'<br>').replace(/ /g,'&nbsp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
    }

    /* ---- DRAG ---- */
    function makeDrag(hdr, popup){
        var on=false, ox=0, oy=0;
        hdr.addEventListener('mousedown', function(e){
            if(e.target.tagName==='BUTTON') return;
            on=true;
            var r=popup.getBoundingClientRect();
            ox=e.clientX-r.left; oy=e.clientY-r.top;
            e.preventDefault();
        });
        PD.addEventListener('mousemove', function(e){
            if(!on) return;
            var x=Math.max(0,Math.min(P.innerWidth-popup.offsetWidth, e.clientX-ox));
            var y=Math.max(0,Math.min(P.innerHeight-popup.offsetHeight, e.clientY-oy));
            popup.style.left=x+'px'; popup.style.top=y+'px';
            popup.style.right='auto'; popup.style.bottom='auto';
            ss(popup.id+'_pos', JSON.stringify({x:x,y:y}));
        });
        PD.addEventListener('mouseup', function(){ on=false; });
    }

    /* ---- SETUP POPUP ---- */
    function setup(pId, fId, mId, cId){
        var p=el(pId), f=el(fId), m=el(mId), c=el(cId);
        if(!p||!f) return;
        // restore position
        try{
            var pos=ls(pId+'_pos',null);
            if(pos){var j=JSON.parse(pos);p.style.left=j.x+'px';p.style.top=j.y+'px';p.style.right='auto';p.style.bottom='auto';}
        }catch(e){}
        // restore visibility
        if(ls(pId+'_vis','1')==='0'){p.style.display='none';f.style.display='flex';}
        else{p.style.display='flex';f.style.display='none';}
        // restore minimized
        if(ls(pId+'_min','0')==='1'){p.classList.add('pg-min');if(m)m.textContent='▢';}
        // bind events
        f.addEventListener('click', function(){p.style.display='flex';f.style.display='none';ss(pId+'_vis','1');});
        if(c) c.addEventListener('click', function(){p.style.display='none';f.style.display='flex';ss(pId+'_vis','0');});
        if(m) m.addEventListener('click', function(){var mn=p.classList.toggle('pg-min');m.textContent=mn?'▢':'−';ss(pId+'_min',mn?'1':'0');});
    }

    setup('pg-popup-note',   'pg-fab-note',   'pg-n-min', 'pg-n-cls');
    setup('pg-popup-pinyin', 'pg-fab-pinyin', 'pg-py-min','pg-py-cls');
    makeDrag(el('pg-hdr-note'),   el('pg-popup-note'));
    makeDrag(el('pg-hdr-pinyin'), el('pg-popup-pinyin'));

    /* ---- NOTE TEXTAREA ---- */
    var ta=el('pg-note-ta');
    if(ta){
        ta.value=ls('pg_note_txt','');
        var fs=parseInt(ls('pg_note_fs','15'));
        ta.style.fontSize=fs+'px';
        ta.addEventListener('input', function(){ss('pg_note_txt',ta.value);});
    }
    el('pg-n-inc').addEventListener('click', function(){if(!ta)return;var f=Math.min(32,(parseInt(ta.style.fontSize)||15)+2);ta.style.fontSize=f+'px';ss('pg_note_fs',f);});
    el('pg-n-dec').addEventListener('click', function(){if(!ta)return;var f=Math.max(10,(parseInt(ta.style.fontSize)||15)-2);ta.style.fontSize=f+'px';ss('pg_note_fs',f);});

    /* ---- PINYIN INPUT & ZOOM ---- */
    var pi=el('pg-py-inp'), po=el('pg-py-out');
    if(pi && po){
        var pyfs = parseInt(ls('pg_py_fs', '14')) || 14;
        pi.style.fontSize = pyfs + 'px';
        po.style.fontSize = pyfs + 'px';
        pi.value=ls('pg_py_txt',''); 
        pi.addEventListener('input',renderPy); 
        renderPy(); 
    }
    el('pg-py-inc').addEventListener('click', function(){
        if(!pi || !po) return;
        var f = Math.min(48, (parseInt(pi.style.fontSize) || 14) + 2);
        pi.style.fontSize = f + 'px';
        po.style.fontSize = f + 'px';
        ss('pg_py_fs', f);
    });
    el('pg-py-dec').addEventListener('click', function(){
        if(!pi || !po) return;
        var f = Math.max(10, (parseInt(pi.style.fontSize) || 14) - 2);
        pi.style.fontSize = f + 'px';
        po.style.fontSize = f + 'px';
        ss('pg_py_fs', f);
    });

    /* ---- COPY BUTTON ---- */
    var cpBtn=el('pg-py-copy');
    if(cpBtn){
        cpBtn.addEventListener('click', function(){
            var o=el('pg-py-out');
            var txt = o && o._pyText ? o._pyText : '';
            if(!txt || !txt.trim()) return;
            function fallbackCopy(){
                try{
                    var ta2=PD.createElement('textarea');
                    ta2.value=txt; ta2.style.position='fixed'; ta2.style.opacity='0';
                    PD.body.appendChild(ta2); ta2.select(); PD.execCommand('copy'); PD.body.removeChild(ta2);
                }catch(e){}
                cpBtn.textContent='✅ Đã copy!'; cpBtn.classList.add('copied');
                setTimeout(function(){ cpBtn.textContent='📋 Copy Pinyin'; cpBtn.classList.remove('copied'); }, 1500);
            }
            if(P.navigator && P.navigator.clipboard && P.navigator.clipboard.writeText){
                P.navigator.clipboard.writeText(txt).then(function(){
                    cpBtn.textContent='✅ Đã copy!'; cpBtn.classList.add('copied');
                    setTimeout(function(){ cpBtn.textContent='📋 Copy Pinyin'; cpBtn.classList.remove('copied'); }, 1500);
                }).catch(fallbackCopy);
            } else {
                fallbackCopy();
            }
        });
    }
})();
</script>
""", height=0, scrolling=False)

 

