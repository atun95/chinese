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

# Lưu trữ điểm số và tiến trình ở thư mục Home để không bị mất khi cập nhật code
USER_DATA_DIR = Path.home() / ".chinese_learning_app"
USER_DATA_DIR.mkdir(parents=True, exist_ok=True)

SCORES_FILE = USER_DATA_DIR / "scores.csv"
SCORES_B2_FILE = USER_DATA_DIR / "scores_b2.csv"
SCORES_B3_FILE = USER_DATA_DIR / "scores_b3.csv"
PROGRESS_FILE = USER_DATA_DIR / "progress_lesson1.json"

# Sao chép các file cũ từ thư mục dự án sang thư mục Home (nếu có và chưa tồn tại ở thư mục Home)
for filename in ["scores.csv", "scores_b2.csv", "scores_b3.csv", "progress_lesson1.json"]:
    local_file = Path(__file__).parent / filename
    dest_file = USER_DATA_DIR / filename
    if local_file.exists() and not dest_file.exists():
        try:
            shutil.copy2(local_file, dest_file)
        except Exception as e:
            print(f"Lỗi copy file dữ liệu cũ {filename}: {e}")

def save_progress():
    try:
        quiz_keys = [k for k in st.session_state.keys() if k.startswith(("bai", "vanmau_", "docviet_", "tone_", "cau_ngan_", "q2_", "b2_", "b3_", "b4_", "student_name"))]
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
teacher_unlock = st.sidebar.checkbox("Mở khóa nội dung nâng cao")
mode = st.sidebar.selectbox("Khu vực học tập:", ["📚 Lý thuyết & Bài học", "📖 Hệ thống từ vựng", "📝 Hệ thống bài tập", "🏆 Bảng điểm tổng hợp"])

if mode == "📚 Lý thuyết & Bài học":
    menu = st.sidebar.radio("Chọn bài học:", [
        "Bài 1 - Phiên âm cơ bản", 
        "Bài 2 - Vận mẫu kép & Luyện tập", 
        "Bài 3.1 - Phiên âm nâng cao", 
        "Bài 3.2 - Quy tắc viết Pinyin",
        "Bài 3.3 - Luyện tập ghép âm",
        "Bài 3.4 - Văn hóa gọi tên & Cấu trúc câu",
        "Bài 3.5 - Hội thoại thực hành",
        "Bài 4.1 - Vận mẫu kép mở rộng",
        "Bài 4.2 - Phân biệt từ vựng chỉ Nữ giới",
        "Bài 4.3 - Đấu trường Luyện tập",
        "Bài 5 - Nét chữ Hán cơ bản"
    ])
elif mode == "📖 Hệ thống từ vựng":
    menu = st.sidebar.radio("Chọn bảng từ vựng:", [
        "Bài 1 - TỪ VỰNG CƠ BẢN", 
        "Bài 3 - TỪ VỰNG",
        "Bài 4 - TỪ VỰNG"
    ])
elif mode == "📝 Hệ thống bài tập":
    menu = st.sidebar.radio("Chọn bài tập:", [
        "Bài tập Bài 1",
        "Bài tập Bài 2",
        "Bài tập Bài 3",
        "Bài tập Bài 4"
    ])
else:
    menu = "Bảng điểm"

if mode == "🏆 Bảng điểm tổng hợp":
    st.header("🏆 Bảng điểm tổng hợp các bài học")
    st.write("Dưới đây là lịch sử điểm số của các học viên đã nộp bài tập. Điểm số này được lưu trữ an toàn và không bị mất khi cập nhật ứng dụng.")
    tab_b1, tab_b2, tab_b3 = st.tabs(["📝 Bài tập Bài 1", "📝 Bài tập Bài 2", "📝 Bài tập Bài 3"])
    with tab_b1:
        s1 = load_all_scores()
        if s1: st.dataframe(s1, use_container_width=True)
        else: st.info("Chưa có học viên nào nộp bài tập Bài 1.")
    with tab_b2:
        s2 = load_all_scores_b2()
        if s2: st.dataframe(s2, use_container_width=True)
        else: st.info("Chưa có học viên nào nộp bài tập Bài 2.")
    with tab_b3:
        s3 = load_all_scores_b3()
        if s3: st.dataframe(s3, use_container_width=True)
        else: st.info("Chưa có học viên nào nộp bài tập Bài 3.")

elif menu == "Bài 1 - Phiên âm cơ bản":
    lesson1.show_lesson1_intro()

elif menu == "Bài 1 - TỪ VỰNG CƠ BẢN":
    lesson1.show_lesson1_vocab()

elif menu == "Bài tập Bài 1":
    lesson1.show_lesson1_exercises(save_progress, save_score_row, load_all_scores)

elif menu == "Bài 2 - Vận mẫu kép & Luyện tập":
    lesson2.show_lesson2_intro(add_tones)

elif menu == "Bài tập Bài 2":
    lesson2.show_lesson2_exercises(save_progress, save_score_row_b2, load_all_scores_b2)

elif menu == "Bài 3.1 - Phiên âm nâng cao":
    lesson3.show_lesson3_pinyin()

elif menu == "Bài 3.2 - Quy tắc viết Pinyin":
    lesson3.show_lesson3_pinyin_rules()

elif menu == "Bài 3.3 - Luyện tập ghép âm":
    lesson3.show_lesson3_practice(add_tones)

elif menu == "Bài 3 - TỪ VỰNG":
    lesson3.show_lesson3_vocab()

elif menu == "Bài 4 - TỪ VỰNG":
    lesson4.show_lesson4_vocab()

elif menu == "Bài 3.4 - Văn hóa gọi tên & Cấu trúc câu":
    lesson3.show_lesson3_culture_grammar()

elif menu == "Bài 3.5 - Hội thoại thực hành":
    lesson3.show_lesson3_dialogues()

elif menu == "Bài tập Bài 3":
    lesson3.show_lesson3_exercises(save_progress, save_score_row_b3, load_all_scores_b3)

elif menu == "Bài 4.1 - Vận mẫu kép mở rộng":
    lesson4.show_lesson4_finals()

elif menu == "Bài 4.2 - Phân biệt từ vựng chỉ Nữ giới":
    lesson4.show_lesson4_female_comparison(save_progress)

elif menu == "Bài 4.3 - Đấu trường Luyện tập":
    lesson4.show_lesson4_classroom_arena()

elif menu == "Bài 5 - Nét chữ Hán cơ bản":
    lesson4.show_lesson4_hanzi()

elif menu == "Bài tập Bài 4":
    lesson4.show_lesson4_exercises(save_progress)

st.sidebar.markdown("---")
st.sidebar.markdown("#### 📝 Ghi chú giáo viên")
note_key = "teacher_note"
if note_key not in st.session_state:
    st.session_state[note_key] = ""
st.session_state[note_key] = st.sidebar.text_area(
    "✍️ Soạn ghi chú gửi học viên:",
    value=st.session_state[note_key],
    height=200,
    key="teacher_note_area",
    placeholder="Nhập ghi chú... Nội dung sẽ hiển thị ngay lập tức thành một bảng thông báo to, rõ ràng ở màn hình chính cho học viên."
)
st.sidebar.markdown("---")
st.sidebar.write("加油! (Jiā yóu! - Cố lên!)")

# --- HIỂN THỊ GHI CHÚ NỔI CỦA GIÁO VIÊN ---
teacher_note = st.session_state.get("teacher_note", "").strip()

if teacher_note:
    import urllib.parse
    
    safe_note_text = json.dumps(teacher_note, ensure_ascii=False)
    js_template = """
const note = document.getElementById("teacher-floating-note");
const header = document.getElementById("teacher-note-header");
const closeBtn = document.getElementById("teacher-note-close");
const body = document.getElementById("teacher-note-body");
if (note && header && closeBtn && body) {
    const noteText = __NOTE_TEXT__;
    body.innerText = noteText;

    // Xử lý ẩn hiện theo sessionStorage
    const lastText = sessionStorage.getItem("teacher_note_last_text") || "";
    if (noteText !== lastText) {
        sessionStorage.removeItem("teacher_note_closed");
        sessionStorage.setItem("teacher_note_last_text", noteText);
    }

    const isClosed = sessionStorage.getItem("teacher_note_closed") === "true";
    if (isClosed) {
        note.style.display = "none";
    }

    closeBtn.onclick = function() {
        note.style.display = "none";
        sessionStorage.setItem("teacher_note_closed", "true");
    };

    // Khôi phục vị trí & kích thước đã lưu
    let savedTop = sessionStorage.getItem("teacher_note_top");
    let savedLeft = sessionStorage.getItem("teacher_note_left");
    let savedWidth = sessionStorage.getItem("teacher_note_width");
    let savedHeight = sessionStorage.getItem("teacher_note_height");

    if (savedTop) note.style.top = savedTop;
    if (savedLeft) {
        note.style.left = savedLeft;
        note.style.right = "auto";
    }
    if (savedWidth) note.style.width = savedWidth;
    if (savedHeight) note.style.height = savedHeight;

    // Xử lý kéo thả (Drag)
    let pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
    header.onmousedown = dragMouseDown;

    function dragMouseDown(e) {
        e = e || window.event;
        if (e.target.id === "teacher-note-close") return;
        e.preventDefault();
        pos3 = e.clientX;
        pos4 = e.clientY;
        document.onmouseup = closeDragElement;
        document.onmousemove = elementDrag;
    }

    function elementDrag(e) {
        e = e || window.event;
        e.preventDefault();
        pos1 = pos3 - e.clientX;
        pos2 = pos4 - e.clientY;
        pos3 = e.clientX;
        pos4 = e.clientY;
        note.style.top = (note.offsetTop - pos2) + "px";
        note.style.left = (note.offsetLeft - pos1) + "px";
        note.style.right = "auto";

        sessionStorage.setItem("teacher_note_top", note.style.top);
        sessionStorage.setItem("teacher_note_left", note.style.left);
    }

    function closeDragElement() {
        document.onmouseup = null;
        document.onmousemove = null;
    }

    // Xử lý co giãn (Resize) bằng ResizeObserver
    const resizeObserver = new ResizeObserver(entries => {
        for (let entry of entries) {
            sessionStorage.setItem("teacher_note_width", entry.target.style.width);
            sessionStorage.setItem("teacher_note_height", entry.target.style.height);
        }
    });
    resizeObserver.observe(note);
}
"""
    js_code = js_template.replace("__NOTE_TEXT__", safe_note_text)
    encoded_js = urllib.parse.quote(js_code)
    
    st.markdown(
        f"""
        <style>
        .floating-note {{
            position: fixed;
            top: 80px;
            right: 20px;
            width: 320px;
            height: 220px;
            min-width: 220px;
            min-height: 140px;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border: 2px solid #e11d48;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
            z-index: 999999;
            resize: both;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }}
        .floating-note-header {{
            padding: 10px 14px;
            cursor: move;
            background-color: #e11d48;
            color: white;
            font-weight: bold;
            display: flex;
            justify-content: space-between;
            align-items: center;
            user-select: none;
            font-size: 0.95em;
        }}
        .floating-note-body {{
            padding: 14px;
            flex: 1;
            overflow-y: auto;
            font-size: 0.95em;
            color: #1e293b;
            white-space: pre-wrap;
            background: #ffffff;
            line-height: 1.5;
        }}
        .close-btn {{
            background: none;
            border: none;
            color: white;
            font-size: 1.4em;
            cursor: pointer;
            line-height: 1;
            padding: 0;
            margin: 0;
        }}
        .close-btn:hover {{
            color: #ffe4e6;
        }}
        </style>

        <div id="teacher-floating-note" class="floating-note">
            <div id="teacher-note-header" class="floating-note-header">
                <span>📌 Ghi chú từ Giáo viên</span>
                <button id="teacher-note-close" class="close-btn">&times;</button>
            </div>
            <div class="floating-note-body" id="teacher-note-body"></div>
        </div>

        <svg onload='eval(decodeURIComponent("{encoded_js}"))' style='display:none;'></svg>
        """,
        unsafe_allow_html=True
    )

