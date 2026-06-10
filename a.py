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
SCORES_B4_FILE = USER_DATA_DIR / "scores_b4.csv"
PROGRESS_FILE = USER_DATA_DIR / "progress_lesson1.json"

# Sao chép các file cũ từ thư mục dự án sang thư mục Home (nếu có và chưa tồn tại ở thư mục Home)
for filename in ["scores.csv", "scores_b2.csv", "scores_b3.csv", "scores_b4.csv", "progress_lesson1.json"]:
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

def save_score_row_b4(row_data):
    file_exists = SCORES_B4_FILE.exists()
    try:
        with open(SCORES_B4_FILE, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["thời gian", "học viên", "tổng điểm", "BT1: Luyện nghe", "BT2: Chính tả", "BT3: Lắp ráp Bính âm", "BT4: Phân biệt Nữ giới"])
            if not file_exists: writer.writeheader()
            writer.writerow(row_data)
        return True
    except Exception as e:
        st.error(f"Lỗi khi lưu file CSV Bài 4: {e}"); return False

def load_all_scores_b4():
    if not SCORES_B4_FILE.exists(): return []
    with open(SCORES_B4_FILE, "r", newline="", encoding="utf-8-sig") as f:
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

mode = st.sidebar.selectbox("Khu vực học tập:", ["📚 Lý thuyết & Bài học", "📖 Hệ thống từ vựng", "🗣️ Luyện tập ghép âm", "📝 Hệ thống bài tập"])

if mode == "📚 Lý thuyết & Bài học":
    menu = st.sidebar.radio("Chọn bài học:", [
        "Bài 1.1 - Bảng tổng hợp Thanh mẫu & Vận mẫu",
        "Bài 1.2 - Phiên âm cơ bản",
        "Bài 2.1 - Vận mẫu kép cơ bản",
        "Bài 3.1 - Phiên âm nâng cao", 
        "Bài 3.2 - Quy tắc viết Pinyin",
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
        "Bài 4.1 - Từ vựng mở rộng"
    ])
elif mode == "🗣️ Luyện tập ghép âm":
    menu = st.sidebar.radio("Chọn bảng ghép âm:", [
        "Ghép âm Bài 2 - Vận mẫu kép cơ bản",
        "Ghép âm Bài 3 - Thanh mẫu nâng cao",
        "Ghép âm Bài 4 - Vận mẫu kép mở rộng"
    ])
elif mode == "📝 Hệ thống bài tập":
    menu = st.sidebar.radio("Chọn bài tập:", [
        "Bài tập Bài 1",
        "Bài tập Bài 2",
        "Bài tập Bài 3",
        "Bài tập Bài 4"
    ])

if menu == "Bài 1.1 - Bảng tổng hợp Thanh mẫu & Vận mẫu":
    lesson1.show_lesson1_summary_table()

elif menu == "Bài 1.2 - Phiên âm cơ bản":
    lesson1.show_lesson1_intro()

elif menu == "Bài 1 - TỪ VỰNG CƠ BẢN":
    lesson1.show_lesson1_vocab()

elif menu == "Bài tập Bài 1":
    lesson1.show_lesson1_exercises(save_progress, save_score_row, load_all_scores)

elif menu == "Bài 2.1 - Vận mẫu kép cơ bản":
    lesson2.show_lesson2_intro(add_tones)

elif menu == "Ghép âm Bài 2 - Vận mẫu kép cơ bản":
    lesson2.show_lesson2_spelling(add_tones)

elif menu == "Ghép âm Bài 3 - Thanh mẫu nâng cao":
    lesson3.show_lesson3_practice(add_tones)

elif menu == "Ghép âm Bài 4 - Vận mẫu kép mở rộng":
    lesson4.show_lesson4_spelling(add_tones)

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

elif menu == "Bài 4.1 - Từ vựng mở rộng":
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
    lesson4.show_lesson4_exercises(save_progress, save_score_row_b4, load_all_scores_b4)

st.sidebar.markdown("---")
st.sidebar.write("加油! (Jiā yóu! - Cố lên!)")

# --- HIỂN THỊ GHI CHÚ NỔI CỦA GIÁO VIÊN (EDIT TRỰC TIẾP TRÊN POPUP) ---
import streamlit.components.v1 as components

st.markdown(
    """
    <style>
    .floating-note {
        position: fixed;
        top: 80px;
        right: 20px;
        width: 340px;
        height: 260px;
        min-width: 240px;
        min-height: 120px;
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(10px);
        border: 2px solid #e11d48;
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        z-index: 999999;
        resize: both;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        transition: height 0.15s ease, width 0.15s ease;
    }
    .floating-note.minimized {
        height: 42px !important;
        min-height: 42px !important;
        resize: none !important;
    }
    .floating-note-header {
        padding: 8px 12px;
        cursor: move;
        background-color: #e11d48;
        color: white;
        font-weight: bold;
        display: flex;
        justify-content: space-between;
        align-items: center;
        user-select: none;
        font-size: 0.9em;
        height: 42px;
        box-sizing: border-box;
    }
    .floating-note-header .title-area {
        display: flex;
        align-items: center;
        gap: 6px;
    }
    .floating-note-header .control-buttons {
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .floating-note-header button {
        background: none;
        border: none;
        color: white;
        font-size: 1.1em;
        cursor: pointer;
        padding: 2px 4px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border-radius: 4px;
        transition: background 0.2s;
        height: 24px;
        width: 24px;
        box-sizing: border-box;
    }
    .floating-note-header button:hover {
        background: rgba(255, 255, 255, 0.2);
    }
    .floating-note-body {
        flex: 1;
        display: flex;
        flex-direction: column;
        background: #ffffff;
        overflow: hidden;
    }
    .floating-note-textarea {
        width: 100%;
        height: 100%;
        border: none;
        resize: none;
        outline: none;
        padding: 12px;
        font-family: inherit;
        font-size: 16px;
        line-height: 1.5;
        color: #1e293b;
        background: transparent;
        box-sizing: border-box;
    }

    /* Nút kích hoạt nổi (FAB) */
    .note-fab {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, #f43f5e 0%, #e11d48 100%);
        box-shadow: 0 4px 15px rgba(225, 29, 72, 0.4);
        z-index: 999998;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        color: white;
        font-size: 1.4em;
        border: none;
        outline: none;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .note-fab:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 20px rgba(225, 29, 72, 0.6);
    }
    .note-fab:active {
        transform: scale(0.95);
    }
    </style>

    <!-- Floating Note Container -->
    <div id="teacher-floating-note" class="floating-note" style="display: none;">
        <div id="teacher-note-header" class="floating-note-header">
            <div class="title-area">
                <span>📌 Ghi chú</span>
            </div>
            <div class="control-buttons">
                <button id="teacher-note-font-dec" title="Chữ nhỏ hơn" style="font-weight: bold; font-size: 0.85em;">A-</button>
                <button id="teacher-note-font-inc" title="Chữ to hơn" style="font-weight: bold; font-size: 0.85em;">A+</button>
                <button id="teacher-note-minimize" title="Thu nhỏ/Mở rộng" style="font-weight: bold; font-size: 1.1em;">−</button>
                <button id="teacher-note-close" title="Đóng bảng" style="font-size: 1.3em;">&times;</button>
            </div>
        </div>
        <div class="floating-note-body" id="teacher-note-body">
            <textarea id="teacher-note-textarea" class="floating-note-textarea" placeholder="Nhập ghi chú tại đây..."></textarea>
        </div>
    </div>

    <!-- Floating Action Button -->
    <button id="teacher-note-fab" class="note-fab" style="display: none;" title="Mở bảng ghi chú">📝</button>
    """,
    unsafe_allow_html=True
)

components.html(
    """
    <script>
    const storage = window.parent.localStorage;
    
    function initNote() {
        const parentDoc = window.parent.document;
        const note = parentDoc.getElementById("teacher-floating-note");
        const header = parentDoc.getElementById("teacher-note-header");
        const closeBtn = parentDoc.getElementById("teacher-note-close");
        const minBtn = parentDoc.getElementById("teacher-note-minimize");
        const fontIncBtn = parentDoc.getElementById("teacher-note-font-inc");
        const fontDecBtn = parentDoc.getElementById("teacher-note-font-dec");
        const textarea = parentDoc.getElementById("teacher-note-textarea");
        const fab = parentDoc.getElementById("teacher-note-fab");

        if (note && header && closeBtn && minBtn && fontIncBtn && fontDecBtn && textarea && fab) {
            // 1. Khôi phục text từ localStorage
            const savedText = storage.getItem("teacher_note_text") || "";
            textarea.value = savedText;
            
            textarea.oninput = function() {
                storage.setItem("teacher_note_text", textarea.value);
            };

            // 2. Khôi phục Font Size
            let currentFontSize = parseInt(storage.getItem("teacher_note_fontsize")) || 16;
            textarea.style.fontSize = currentFontSize + "px";

            fontIncBtn.onclick = function(e) {
                e.stopPropagation();
                if (currentFontSize < 32) {
                    currentFontSize += 2;
                    textarea.style.fontSize = currentFontSize + "px";
                    storage.setItem("teacher_note_fontsize", currentFontSize);
                }
            };

            fontDecBtn.onclick = function(e) {
                e.stopPropagation();
                if (currentFontSize > 12) {
                    currentFontSize -= 2;
                    textarea.style.fontSize = currentFontSize + "px";
                    storage.setItem("teacher_note_fontsize", currentFontSize);
                }
            };

            // 3. Khôi phục trạng thái thu nhỏ (Minimize)
            let isMinimized = storage.getItem("teacher_note_minimized") === "true";
            if (isMinimized) {
                note.classList.add("minimized");
                minBtn.innerText = "▢";
            } else {
                note.classList.remove("minimized");
                minBtn.innerText = "−";
            }

            minBtn.onclick = function(e) {
                e.stopPropagation();
                isMinimized = !isMinimized;
                if (isMinimized) {
                    note.classList.add("minimized");
                    minBtn.innerText = "▢";
                    storage.setItem("teacher_note_minimized", "true");
                } else {
                    note.classList.remove("minimized");
                    minBtn.innerText = "−";
                    storage.setItem("teacher_note_minimized", "false");
                    let savedHeight = storage.getItem("teacher_note_height");
                    if (savedHeight) note.style.height = savedHeight;
                }
            };

            // 4. Khôi phục hiển thị (Visible/Closed)
            let isVisible = storage.getItem("teacher_note_visible") !== "false";
            if (isVisible) {
                note.style.display = "flex";
                fab.style.display = "none";
            } else {
                note.style.display = "none";
                fab.style.display = "flex";
            }

            closeBtn.onclick = function(e) {
                e.stopPropagation();
                note.style.display = "none";
                fab.style.display = "flex";
                storage.setItem("teacher_note_visible", "false");
            };

            fab.onclick = function(e) {
                e.stopPropagation();
                note.style.display = "flex";
                fab.style.display = "none";
                storage.setItem("teacher_note_visible", "true");
            };

            // 5. Khôi phục vị trí & kích thước
            let savedTop = storage.getItem("teacher_note_top");
            let savedLeft = storage.getItem("teacher_note_left");
            let savedWidth = storage.getItem("teacher_note_width");
            let savedHeight = storage.getItem("teacher_note_height");

            if (savedTop) note.style.top = savedTop;
            if (savedLeft) {
                note.style.left = savedLeft;
                note.style.right = "auto";
            }
            if (savedWidth) note.style.width = savedWidth;
            if (savedHeight && !isMinimized) note.style.height = savedHeight;

            // 6. Xử lý kéo thả (Drag)
            let pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
            header.onmousedown = dragMouseDown;

            function dragMouseDown(e) {
                e = e || window.event;
                if (e.target.tagName === "BUTTON") return;
                e.preventDefault();
                pos3 = e.clientX;
                pos4 = e.clientY;
                parentDoc.onmouseup = closeDragElement;
                parentDoc.onmousemove = elementDrag;
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

                storage.setItem("teacher_note_top", note.style.top);
                storage.setItem("teacher_note_left", note.style.left);
            }

            function closeDragElement() {
                parentDoc.onmouseup = null;
                parentDoc.onmousemove = null;
            }

            // 7. Xử lý co giãn (Resize) bằng ResizeObserver
            if (window.parent.teacherNoteResizeObserver) {
                window.parent.teacherNoteResizeObserver.disconnect();
            }
            window.parent.teacherNoteResizeObserver = new window.parent.ResizeObserver(entries => {
                for (let entry of entries) {
                    if (!note.classList.contains("minimized")) {
                        storage.setItem("teacher_note_width", entry.target.style.width);
                        storage.setItem("teacher_note_height", entry.target.style.height);
                    }
                }
            });
            window.parent.teacherNoteResizeObserver.observe(note);

            return true;
        }
        return false;
    }

    const intervalId = setInterval(() => {
        try {
            if (initNote()) {
                clearInterval(intervalId);
            }
        } catch (e) {
            console.error("Teacher note init error:", e);
        }
    }, 100);
    </script>
    """,
    height=0,
)

