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

from lessons_data import *
from ui_utils import *


# Import các bài học đã tách file và reload để tránh cache
import importlib
import lessons_data
import lesson1
import lesson2
import lesson3
import lesson4
import lesson5
import lesson6
import lesson7
import lesson8


try:
    importlib.reload(lessons_data)
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


def show_consolidated_flashcards():
    import os
    import json
    
    # Path to vocabulary JSON
    json_path = os.path.join("assets", "vocabulary.json")
    
    # If the JSON doesn't exist, generate it dynamically
    if not os.path.exists(json_path) or os.path.getsize(json_path) == 0:
        with st.spinner("Đang khởi tạo dữ liệu từ vựng..."):
            try:
                import flashcard_generator
                flashcard_generator.generate_vocabulary()
            except Exception as e:
                st.error(f"Lỗi khi tạo dữ liệu từ vựng: {e}")
                return

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            vocab_data = json.load(f)
    except Exception as e:
        st.error(f"Lỗi khi đọc tệp từ vựng: {e}")
        return

    # Render Header
    render_lesson_intro(
        "🎴 Thẻ từ ghi nhớ (Flashcards) Tổng Hợp",
        "Hệ thống ôn tập từ vựng thông minh tích hợp từ Bài 1 đến Bài 7. Sử dụng flashcards tương tác kèm phát âm giọng bản xứ."
    )
    
    # Sync vocabulary database button
    col_sync, col_status = st.columns([3, 7])
    with col_sync:
        if st.button("🔄 Đồng bộ & Cập nhật từ vựng", use_container_width=True, key="btn_sync_db"):
            with st.spinner("Đang đồng bộ..."):
                try:
                    import flashcard_generator
                    importlib.reload(flashcard_generator)
                    vocab_data = flashcard_generator.generate_vocabulary()
                    st.success("Đồng bộ thành công!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Lỗi khi đồng bộ: {e}")
                    
    # Filter settings UI
    st.markdown("### 🛠️ Bộ lọc từ vựng")
    col_les, col_cat, col_search = st.columns([2, 2, 3])
    
    # Lesson selection
    lessons_list = ["Tất cả"] + sorted(list(set(item["lesson"] for item in vocab_data)), key=lambda x: int(x.split(" ")[1]) if len(x.split(" ")) > 1 and x.split(" ")[1].isdigit() else 99)
    with col_les:
        sel_lesson = st.selectbox("Chọn bài học:", lessons_list, key="fc_sel_lesson")
        
    # Category selection
    cats_for_lesson = [item["category"] for item in vocab_data if sel_lesson == "Tất cả" or item["lesson"] == sel_lesson]
    categories_list = ["Tất cả"] + sorted(list(set(cats_for_lesson)))
    with col_cat:
        sel_cat = st.selectbox("Chọn nhóm từ:", categories_list, key="fc_sel_cat")
        
    # Search input
    with col_search:
        search_query = st.text_input("🔍 Tìm kiếm từ vựng (Hán tự, Pinyin, Tiếng Việt):", "", key="fc_search")
        
    # Filtering the vocab list
    filtered_vocab = [
        item for item in vocab_data
        if (sel_lesson == "Tất cả" or item["lesson"] == sel_lesson) and
           (sel_cat == "Tất cả" or item["category"] == sel_cat) and
           (not search_query or 
            search_query.lower() in item["word"].lower() or 
            search_query.lower() in item["pinyin"].lower() or 
            search_query.lower() in item["vietnamese"].lower())
    ]
    
    if not filtered_vocab:
        st.warning("Không tìm thấy từ vựng nào khớp với bộ lọc hiện tại!")
        return

    # View Mode Selector
    view_mode = st.radio("Chế độ hiển thị:", ["🎴 Thẻ từ (Flashcard)", "📋 Bảng tổng hợp chi tiết"], horizontal=True, key="fc_view_mode")
    
    if view_mode == "📋 Bảng tổng hợp chi tiết":
        st.markdown(f"**Danh sách gồm {len(filtered_vocab)} từ vựng:**")
        # Format table data
        table_data = []
        for idx, item in enumerate(filtered_vocab, 1):
            table_data.append({
                "STT": idx,
                "Bài": item["lesson"],
                "Nhóm": item["category"],
                "Chữ Hán": item["word"],
                "Pinyin": item["pinyin"],
                "Nghĩa tiếng Việt": item["vietnamese"],
                "Ví dụ": item["example_han"] if item["example_han"] else "-"
            })
        st.dataframe(table_data, use_container_width=True)
        
        # Download buttons
        st.write("### 📥 Tải xuống / Xuất file:")
        
        # Offline App (Interactive App)
        app_path = "Flashcard_Offline.html"
        if os.path.exists(app_path):
            with open(app_path, "r", encoding="utf-8") as f:
                app_bytes = f.read()
            st.download_button(
                label="🚀 TẢI APP FLASHCARD OFFLINE (Tương tác lật thẻ + Phát âm + Xem nét chữ động)",
                data=app_bytes,
                file_name="Flashcard_Offline.html",
                mime="text/html",
                use_container_width=True,
                type="primary",
                key="fc_dl_offline_app"
            )
            st.info("💡 Hướng dẫn gửi học viên: Tải file `Flashcard_Offline.html` này gửi qua Zalo/Email. Học viên chỉ cần mở file bằng trình duyệt (Chrome, Safari, Edge...) trên Điện thoại hoặc Máy tính là học được ngay offline, không cần cài đặt gì thêm!")
            st.markdown("---")
            
        col_dl_json, col_dl_csv, col_dl_html = st.columns(3)
        
        # JSON
        with open(json_path, "r", encoding="utf-8") as f:
            json_bytes = f.read()
        with col_dl_json:
            st.download_button("📥 Tải file JSON", json_bytes, file_name="vocabulary.json", mime="application/json", key="fc_dl_json")
            
        # CSV
        csv_path = os.path.join("assets", "vocabulary.csv")
        if os.path.exists(csv_path):
            with open(csv_path, "r", encoding="utf-8") as f:
                csv_bytes = f.read()
            with col_dl_csv:
                st.download_button("📥 Tải file CSV (Excel)", csv_bytes, file_name="vocabulary.csv", mime="text/csv", key="fc_dl_csv")
                
        # HTML Print Format
        html_path = os.path.join("assets", "vocabulary_print.html")
        if os.path.exists(html_path):
            with open(html_path, "r", encoding="utf-8") as f:
                html_bytes = f.read()
            with col_dl_html:
                st.download_button("📥 Tải trang HTML In Ấn", html_bytes, file_name="vocabulary_print.html", mime="text/html", key="fc_dl_html")
        return

    # Shuffle button
    col_ord, col_shuf = st.columns([5, 2])
    with col_ord:
        st.markdown(f"**Đang hiển thị {len(filtered_vocab)} từ vựng.**")
    with col_shuf:
        if st.button("🔀 Trộn ngẫu nhiên", use_container_width=True, key="fc_shuffle"):
            random.shuffle(filtered_vocab)
            st.session_state["fc_shuffled_list"] = filtered_vocab
            st.session_state["fc_index"] = 0
            st.rerun()

    # Get the source list (use shuffled if available)
    vocab_source = st.session_state.get("fc_shuffled_list", filtered_vocab)
    
    # Sync with filtered list size change
    if len(vocab_source) != len(filtered_vocab):
        vocab_source = filtered_vocab
        if "fc_shuffled_list" in st.session_state:
            del st.session_state["fc_shuffled_list"]

    # Current index in session state
    if "fc_index" not in st.session_state:
        st.session_state["fc_index"] = 0
        
    if st.session_state["fc_index"] >= len(vocab_source):
        st.session_state["fc_index"] = 0
        
    cur_idx = st.session_state["fc_index"]
    item = vocab_source[cur_idx]
    
    # Progress indicator
    st.progress((cur_idx + 1) / len(vocab_source))
    st.markdown(f"<div style='text-align: center; color: #64748b; font-weight: bold; margin-bottom: 20px;'>Từ {cur_idx + 1} / {len(vocab_source)} ({item['lesson']} - {item['category']})</div>", unsafe_allow_html=True)
    
    # Card Flipped State
    if "fc_flipped" not in st.session_state:
        st.session_state["fc_flipped"] = False

    # Custom styling for premium card
    st.markdown("""
    <style>
    .fc-box {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 2px solid #e11d48;
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 15px 30px rgba(0,0,0,0.06);
        text-align: center;
        min-height: 280px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin-bottom: 25px;
    }
    .fc-word {
        font-size: 3.8rem;
        font-weight: 800;
        color: #e11d48;
        margin-bottom: 10px;
    }
    .fc-pinyin {
        font-family: 'Courier New', monospace;
        font-size: 1.8rem;
        font-weight: 700;
        color: #2563eb;
        background: #eff6ff;
        padding: 4px 20px;
        border-radius: 30px;
        border: 1px solid #dbeafe;
        display: inline-block;
        margin-bottom: 15px;
    }
    .fc-viet {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 20px;
    }
    .fc-ex-box {
        background: #f8fafc;
        border-radius: 12px;
        padding: 15px;
        border: 1px solid #e2e8f0;
        width: 100%;
        max-width: 600px;
        text-align: left;
        margin-top: 10px;
    }
    .fc-ex-title {
        font-size: 0.8rem;
        color: #94a3b8;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 5px;
    }
    .fc-ex-han {
        font-size: 1.3rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 2px;
    }
    .fc-ex-py {
        font-family: 'Courier New', monospace;
        color: #059669;
        font-size: 0.95rem;
        margin-bottom: 4px;
    }
    .fc-ex-vi {
        color: #475569;
        font-style: italic;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    if not st.session_state["fc_flipped"]:
        # Front Side (Chinese only)
        st.markdown(f"""
        <div class="fc-box">
            <div class="fc-word">{item['word']}</div>
            <div style="color: #94a3b8; font-style: italic; font-size: 0.9rem; margin-top: 15px;">(Click "Lật thẻ" bên dưới để xem phiên âm & nghĩa)</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Back Side (Detailed View)
        ex_html = ""
        if item["example_han"]:
            ex_html = f"""
            <div class="fc-ex-box">
                <div class="fc-ex-title">Ví dụ minh họa:</div>
                <div class="fc-ex-han">{item['example_han']}</div>
                <div class="fc-ex-py">{item['example_py']}</div>
                <div class="fc-ex-vi">{item['example_vi']}</div>
            </div>
            """
            
        st.markdown(f"""
        <div class="fc-box">
            <div class="fc-word" style="font-size: 3rem;">{item['word']}</div>
            <div><span class="fc-pinyin">{item['pinyin']}</span></div>
            <div class="fc-viet">{item['vietnamese']}</div>
            {ex_html}
        </div>
        """, unsafe_allow_html=True)
        
        # Audio Player columns
        col_a1, col_a2 = st.columns(2)
        with col_a1:
            render_play_button(item['word'], "🔊 Phát âm từ", key=f"fc_aud_w_{cur_idx}")
        with col_a2:
            if item["example_han"]:
                render_play_button(item['example_han'], "🔊 Nghe câu ví dụ", key=f"fc_aud_ex_{cur_idx}")

    # Navigation buttons
    col_prev, col_flip, col_next = st.columns([2, 3, 2])
    
    with col_prev:
        if st.button("⬅️ Từ trước", use_container_width=True, key="btn_fc_prev"):
            st.session_state["fc_index"] = (cur_idx - 1) % len(vocab_source)
            st.session_state["fc_flipped"] = False
            st.rerun()
            
    with col_flip:
        btn_label = "👁️ Lật thẻ (Xem nghĩa)" if not st.session_state["fc_flipped"] else "🙈 Lật thẻ (Ẩn nghĩa)"
        if st.button(btn_label, use_container_width=True, type="primary", key="btn_fc_flip"):
            st.session_state["fc_flipped"] = not st.session_state["fc_flipped"]
            st.rerun()
            
    with col_next:
        if st.button("Từ sau ➡️", use_container_width=True, key="btn_fc_next"):
            st.session_state["fc_index"] = (cur_idx + 1) % len(vocab_source)
            st.session_state["fc_flipped"] = False
            st.rerun()


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
PROGRESS_FILE = USER_DATA_DIR / "progress_lesson1.json"

# Sao chép các file cũ từ thư mục dự án sang thư mục Home (nếu có và chưa tồn tại ở thư mục Home)
for filename in ["scores.csv", "scores_b2.csv", "scores_b3.csv", "scores_b4.csv", "scores_b5.csv", "scores_b5_3.csv", "scores_b6_1.csv", "scores_b6_2.csv", "scores_b7_1.csv", "scores_b7_2.csv", "scores_b7_3.csv", "progress_lesson1.json"]:
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

mode = st.sidebar.selectbox("Khu vực học tập:", ["📚 Lý thuyết & Bài học", "📖 Hệ thống từ vựng", "🗣️ Luyện tập ghép âm", "🗣️ Thực hành trên lớp", "📝 Hệ thống bài tập", "🎴 HSK 1 - THẺ TỪ ÔN TẬP TỰ VỰNG", "🖨️ In ấn & Đồng bộ"])

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
        "Bài 8.1 - Tổng quan Chữ Hán",
        "Bài 8.2 - Hệ thống Nét viết",
        "Bài 8.3 - Quy tắc Bút thuận",
        "Bài 8.4 - Hệ thống Bộ thủ",
        "Bài 8.5 - Đơn thể & Hợp thể"
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
        "Bài 6.1 - Thực hành Giao tiếp & Phản xạ"
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
        "Bài tập Bài 7.3"
    ])

if mode == "🎴 HSK 1 - THẺ TỪ ÔN TẬP TỰ VỰNG":
    show_consolidated_flashcards()

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

elif menu == "Bài 5.1 - Số đếm từ 0 đến 10":
    # Hot-reload trigger: 2026-06-12 16:38
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

