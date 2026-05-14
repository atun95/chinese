import streamlit as st
import random
import json
import csv
from datetime import datetime
from pathlib import Path
from lessons_data import *
from ui_utils import *

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
    </style>
    """,
    unsafe_allow_html=True,
)

# --- KHỞI TẠO & BIẾN TOÀN CỤC ---
if "scores" not in st.session_state:
    st.session_state.scores = {}

SCORES_FILE = Path(__file__).with_name("scores.csv")
PROGRESS_FILE = Path(__file__).with_name("progress_lesson1.json")

def save_progress():
    try:
        quiz_keys = [k for k in st.session_state.keys() if k.startswith(("bai", "vanmau_", "docviet_", "tone_", "cau_ngan_", "q2_", "student_name"))]
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
            writer = csv.DictWriter(f, fieldnames=["thời gian","học viên","tổng điểm","tổng câu","phần trăm","bài 1","bài 2","bài 3","bài 4","bài 5","bài 6"])
            if not file_exists: writer.writeheader()
            writer.writerow(row_data)
        return True
    except Exception as e:
        st.error(f"Lỗi khi lưu file CSV: {e}"); return False

def load_all_scores():
    if not SCORES_FILE.exists(): return []
    with open(SCORES_FILE, "r", newline="", encoding="utf-8-sig") as f:
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
teacher_unlock = st.sidebar.checkbox("Mở khóa nội dung Bài 2 (GV)")
menu = st.sidebar.radio("Chọn mục:", ["Bài 1 - Phiên âm cơ bản", "Bài 1 - TỪ VỰNG CƠ BẢN", "Bài 1 - Bài tập", "Bài 2 - Vận mẫu kép & Luyện tập", "Bài 3 - Phiên âm nâng cao (đang khóa)", "Bài 3 - Nét chữ Hán cơ bản (đang khóa)"])

if menu == "Bài 1 - Phiên âm cơ bản":
    render_lesson_intro("📚 Bài 1: Học phiên âm cơ bản", "Nắm thanh mẫu cơ bản, vận mẫu đơn, 5 thanh điệu và biến điệu thanh 3.")
    with st.expander("📊 Bảng tổng hợp Thanh mẫu & Vận mẫu", expanded=True):
        st.markdown("""<div style='margin-bottom: 10px;'><span style='background-color: #0f172a; color: white; padding: 5px 15px; border-radius: 5px; font-weight: bold;'>1</span><span style='font-size: 1.3rem; font-weight: bold; margin-left: 10px;'>声母 Thanh mẫu (Initials)</span></div><table class="chinese-table"><tr class="tm-header"><th style="width: 30%;">Vị trí phát âm</th><th>Thanh mẫu</th></tr><tr><td class="cat-col">Âm môi</td><td><span class="pinyin-text">b &nbsp; p &nbsp; m</span></td></tr><tr><td class="cat-col">Âm môi răng</td><td><span class="pinyin-text">f</span></td></tr><tr><td class="cat-col">Âm tròn môi</td><td><span class="pinyin-text">w</span></td></tr><tr><td class="cat-col">Âm đầu lưỡi trước</td><td><span class="pinyin-text">z &nbsp; c &nbsp; s</span></td></tr><tr><td class="cat-col">Âm đầu lưỡi giữa</td><td><span class="pinyin-text">d &nbsp; t &nbsp; n &nbsp; l</span></td></tr><tr><td class="cat-col">Âm đầu lưỡi sau</td><td><span class="pinyin-text">zh &nbsp; ch &nbsp; sh &nbsp; r</span></td></tr><tr><td class="cat-col">Âm mặt lưỡi</td><td><span class="pinyin-text">j &nbsp; q &nbsp; x</span></td></tr><tr><td class="cat-col">Âm cuống lưỡi</td><td><span class="pinyin-text">g &nbsp; k &nbsp; h &nbsp; y</span></td></tr></table><div style='margin-bottom: 10px; margin-top: 20px;'><span style='background-color: #fbbf24; color: #0f172a; padding: 5px 15px; border-radius: 5px; font-weight: bold;'>2</span><span style='font-size: 1.3rem; font-weight: bold; margin-left: 10px;'>韵母 Vận mẫu (Finals)</span></div><table class="chinese-table"><tr class="vm-header"><th style="width: 20%;">Loại</th><th style="text-align: center;">a</th><th style="text-align: center;">o</th><th style="text-align: center;">e</th><th style="text-align: center;">i</th><th style="text-align: center;">u</th><th style="text-align: center;">ü</th></tr><tr><td class="cat-col">Đơn</td><td style="text-align: center;"><span class="pinyin-text">a</span></td><td style="text-align: center;"><span class="pinyin-text">o</span></td><td style="text-align: center;"><span class="pinyin-text">e</span></td><td style="text-align: center;"><span class="pinyin-text">i</span></td><td style="text-align: center;"><span class="pinyin-text">u</span></td><td style="text-align: center;"><span class="pinyin-text">ü</span></td></tr><tr><td class="cat-col">Kép</td><td style="text-align: center;"><span class="pinyin-text">ai ao</span></td><td style="text-align: center;"><span class="pinyin-text">ou</span></td><td style="text-align: center;"><span class="pinyin-text">ei</span></td><td style="text-align: center;"><span class="pinyin-text">ia ie<br>iao iu</span></td><td style="text-align: center;"><span class="pinyin-text">ua uo<br>uai ui</span></td><td style="text-align: center;"><span class="pinyin-text">üe</span></td></tr><tr><td class="cat-col">Mũi</td><td style="text-align: center;"><span class="pinyin-text">an ang</span></td><td style="text-align: center;"><span class="pinyin-text">ong</span></td><td style="text-align: center;"><span class="pinyin-text">en eng</span></td><td style="text-align: center;"><span class="pinyin-text">ian in<br>iang ing<br>iong</span></td><td style="text-align: center;"><span class="pinyin-text">uan un<br>uang</span></td><td style="text-align: center;"><span class="pinyin-text">üan ün</span></td></tr></table>""", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("1. Thanh mẫu và vận mẫu cơ bản")
    st.markdown("#### 1.1. Thanh mẫu (Initials)")
    cols_tm = st.columns(4)
    for i, item in enumerate(B1_INITIALS_CARDS):
        with cols_tm[i % 4]: render_pronunciation_card(item, "b1_tm")
    st.markdown("---")
    st.markdown("#### 1.2. Vận mẫu (Finals)")
    cols_vm = st.columns(4)
    for i, item in enumerate(B1_FINALS_CARDS):
        with cols_vm[i % 4]: render_pronunciation_card(item, "b1_vm")
    
    st.markdown("---")
    st.subheader("2. Thanh điệu (Tones)")
    
    st.markdown("#### 2.1. Bốn thanh điệu cơ bản")
    col_t1, col_t2, col_t3, col_t4 = st.columns(4)
    with col_t1: st.info("**Thanh 1: mā**\n\n(Cao và ngang)")
    with col_t2: st.info("**Thanh 2: má**\n\n(Đi lên)")
    with col_t3: st.info("**Thanh 3: mǎ**\n\n(Hạ xuống rồi lên)")
    with col_t4: st.info("**Thanh 4: mà**\n\n(Đi xuống mạnh)")
    st.write("💡 *Thanh nhẹ: nhẹ, ngắn, không nhấn*")

    st.markdown("#### 2.2. Thanh nhẹ (轻声)")
    st.write("Thanh nhẹ thường xuất hiện ở âm tiết thứ hai trong từ láy hoặc một số từ thông dụng.")
    st.write("Ví dụ:")
    st.write("- **māma** (妈妈): âm tiết **ma** thứ hai là thanh nhẹ")
    st.write("- **bàba** (爸爸): âm tiết **ba** thứ hai là thanh nhẹ")
    st.write("- **gēge** (哥哥), **jiějie** (姐姐), **dìdi** (弟弟)")

    st.markdown("#### 2.3. Quy tắc biến điệu thanh 3")
    st.success("**Quy tắc chuẩn:** Khi hai thanh 3 đi liền nhau (**3 + 3**), âm tiết thứ nhất đổi thành **thanh 2**.")
    col_ex1, col_ex2 = st.columns(2)
    with col_ex1: st.code("nǐ + hǎo → ní hǎo", language="text")
    with col_ex2: st.code("wǒ + hěn → wó hěn", language="text")
    st.warning("⚠️ Với chuỗi **3 + 3 + 3**: Thường đổi 2 âm đầu thành thanh 2 (Ví dụ: nǐ wǒ hǎo → ní wó hǎo).")

elif menu == "Bài 1 - TỪ VỰNG CƠ BẢN":
    render_lesson_intro("👨‍👩‍👧‍👦 Bài 1: Học TỪ VỰNG CƠ BẢN", "Học từ xưng hô, đại từ thường dùng và từ mở rộng để ghép câu ngắn.")
    st.subheader("Từ xưng hô dạng từ láy"); st.table(XUNG_HO_TU_LAY)
    st.subheader("Đại từ xưng hô cơ bản"); st.table(DAI_TU_XUNG_HO)
    st.subheader("Từ vựng bổ sung"); st.table(TU_VUNG_BO_SUNG)

elif menu == "Bài 1 - Bài tập":
    st.header("📝 Bài 1: Bài tập tổng hợp")
    # Sử dụng helper render_quiz_section để rút gọn
    q1 = [
        {"q": "lǎoshī", "choices": ["thầy/cô giáo", "học sinh", "rất"], "answer": "thầy/cô giáo"},
        {"q": "xuéshēng", "choices": ["không", "học sinh", "bận"], "answer": "học sinh"},
        {"q": "hěn", "choices": ["rất", "không", "bận"], "answer": "rất"},
        {"q": "máng", "choices": ["bận", "mẹ", "bố"], "answer": "bận"},
        {"q": "bù", "choices": ["không", "rất", "bạn"], "answer": "không"},
        {"q": "wǒ", "choices": ["tôi/mình", "bạn/cậu", "anh ấy/cô ấy"], "answer": "tôi/mình"},
        {"q": "nǐ", "choices": ["không", "bạn/cậu", "rất"], "answer": "bạn/cậu"},
        {"q": "māma", "choices": ["bố", "mẹ/má", "chị gái"], "answer": "mẹ/má"},
    ]
    render_quiz_section(q1, "bai1", "Bài tập 1: Mini quiz từ vựng", "Chọn nghĩa đúng nhất cho từng từ.", save_progress)

    with st.expander("Bài tập 2: Âm bật hơi", expanded=False):
        col1, col2, col3 = st.columns(3)
        with col1: b = st.checkbox("B", key="q2_b"); p = st.checkbox("P", key="q2_p")
        with col2: d = st.checkbox("D", key="q2_d"); t = st.checkbox("T", key="q2_t")
        with col3: g = st.checkbox("G", key="q2_g"); k = st.checkbox("K", key="q2_k")
        if st.button("Kiểm tra kết quả"):
            if (p and t and k) and not (b or d or g):
                st.balloons(); st.success("Đúng! P, T, K là âm bật hơi."); st.session_state.scores["bai2"] = (1, 1)
            else: st.error("Sai rồi! Nhớ nhé: P, T, K là các âm bật hơi."); st.session_state.scores["bai2"] = (0, 1)
            save_progress()

    with st.expander("Bài tập 3: Điền vận mẫu", expanded=False):
        qs = [("m___ma", "ā"), ("n___", "ǐ"), ("l___oshī", "ǎ"), ("xu___shēng", "é"), ("h___n", "ě"), ("m___ng", "á"), ("b___", "ù"), ("w___", "ǒ")]
        opts = ["...", "ā", "á", "ǎ", "à", "ē", "é", "ě", "è", "ǐ", "ǒ", "ù"]
        score = 0
        for i, (q, ans) in enumerate(qs):
            key = f"vanmau_q_{i}"
            res = st.selectbox(f"Chọn vận mẫu cho {q}", opts, index=opts.index(st.session_state.get(key, "...")), key=key)
            if res == ans: score += 1
        if st.button("Chấm điểm bài 3"): st.session_state.scores["bai3"] = (score, len(qs)); save_progress(); st.success(f"Bạn đúng {score}/{len(qs)} câu.")

    q4 = [
        {"q": "tôi/mình", "choices": ["wǒ", "nǐ", "tā"], "answer": "wǒ"},
        {"q": "bạn/cậu", "choices": ["nǐ", "wǒ", "tā"], "answer": "nǐ"},
        {"q": "mẹ/má", "choices": ["māma", "bàba", "mèimei"], "answer": "māma"},
        {"q": "thầy/cô giáo", "choices": ["lǎoshī", "xuéshēng", "lǎobǎn"], "answer": "lǎoshī"},
        {"q": "học sinh", "choices": ["xuéshēng", "lǎoshī", "tóngxué"], "answer": "xuéshēng"},
        {"q": "rất", "choices": ["hěn", "tài", "zhēn"], "answer": "hěn"},
        {"q": "bận", "choices": ["máng", "lèi", "è"], "answer": "máng"},
        {"q": "không", "choices": ["bù", "méi", "shì"], "answer": "bù"},
    ]
    render_quiz_section(q4, "bai4", "Bài tập 4: Dịch sang Pinyin", "Chọn Pinyin đúng cho nghĩa tiếng Việt tương ứng.", save_progress)

    # Bài tập 5 & 6
    tone_qs = [
        {"q": "妈妈 (māma)", "hanzi": "妈妈", "choices": ["māma", "máng", "mǎma"], "answer": "māma"},
        {"q": "老师 (lǎoshī)", "hanzi": "老师", "choices": ["làoshī", "lǎoshī", "láoshī"], "answer": "lǎoshī"},
        {"q": "学生 (xuéshēng)", "hanzi": "学生", "choices": ["xuěshēng", "xuéshēng", "xuesheng"], "answer": "xuéshēng"},
        {"q": "很 (hěn)", "hanzi": "很", "choices": ["hèn", "hén", "hěn"], "answer": "hěn"},
        {"q": "忙 (máng)", "hanzi": "忙", "choices": ["máng", "mǎng", "màng"], "answer": "máng"},
        {"q": "不 (bù)", "hanzi": "不", "choices": ["bù", "bú", "bǔ"], "answer": "bù"},
    ]
    with st.expander("Bài tập 5: Luyện thanh điệu (nghe)", expanded=False):
        score_5 = 0
        for i, q in enumerate(tone_qs):
            st.write(f"**Câu {i+1}:** Nghe và chọn pinyin đúng")
            if st.button(f"🔊 Nghe mẫu", key=f"listen_{i}"): play_audio(q["hanzi"])
            key = f"tone_q_{i}"
            choices = q["choices"]
            res = st.radio("Chọn đáp án:", choices, index=choices.index(st.session_state.get(key, choices[0])), key=key)
            if res == q["answer"]: score_5 += 1
        if st.button("Chấm điểm bài 5"): st.session_state.scores["bai5"] = (score_5, len(tone_qs)); save_progress(); st.success(f"Bạn đúng {score_5}/{len(tone_qs)} câu.")

    q6 = [
        {"q": "wǒ hěn máng", "choices": ["tôi rất bận", "tôi không bận", "bạn rất bận"], "answer": "tôi rất bận"},
        {"q": "nǐ bù máng", "choices": ["bạn không bận", "bạn rất bận", "tôi không bận"], "answer": "bạn không bận"},
        {"q": "wǒ shì xuéshēng", "choices": ["tôi là học sinh", "tôi là thầy giáo", "bạn là học sinh"], "answer": "tôi là học sinh"},
        {"q": "tā shì lǎoshī", "choices": ["anh ấy/cô ấy là thầy cô giáo", "anh ấy/cô ấy là học sinh", "tôi là thầy cô giáo"], "answer": "anh ấy/cô ấy là thầy cô giáo"},
    ]
    render_quiz_section(q6, "bai6", "Bài tập 6: Câu ngắn", "Chọn nghĩa đúng của câu ngắn.", save_progress)

    with st.expander("📊 Lịch sử & Tổng kết", expanded=True):
        labels = {"bai1": "BT1: Từ vựng", "bai2": "BT2: Bật hơi", "bai3": "BT3: Vận mẫu", "bai4": "BT4: Đọc & Viết", "bai5": "BT5: Nghe", "bai6": "BT6: Câu ngắn"}
        missing = [v for k, v in labels.items() if k not in st.session_state.scores]
        if missing: st.warning(f"Chưa xong: {', '.join(missing)}")
        else:
            earned = sum(s[0] for s in st.session_state.scores.values())
            total = sum(s[1] for s in st.session_state.scores.values())
            score_10 = round((earned / total) * 10, 2)
            percent = round((earned / total) * 100, 1)
            
            st.success(f"📈 Kết quả tổng quát: **{score_10} / 10** điểm ({percent}%)")
            st.info(f"Chi tiết: Đúng {earned} trên tổng số {total} câu hỏi.")
            
            name = st.text_input("Tên học viên", key="student_name")
            if st.button("Nộp bài"):
                if name: 
                    row = {
                        "thời gian": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                        "học viên": name, 
                        "tổng điểm": score_10, 
                        "tổng câu": total, 
                        "phần trăm": percent, 
                        "bài 1": st.session_state.scores.get("bai1",""), 
                        "bài 2": st.session_state.scores.get("bai2",""), 
                        "bài 3": st.session_state.scores.get("bai3",""), 
                        "bài 4": st.session_state.scores.get("bai4",""), 
                        "bài 5": st.session_state.scores.get("bai5",""), 
                        "bài 6": st.session_state.scores.get("bai6","")
                    }
                    if save_score_row(row):
                        st.success("Đã lưu điểm thành công!"); st.session_state.scores = {}; st.rerun()
                else: st.error("Vui lòng nhập tên học viên!")
        
        all_s = load_all_scores()
        if all_s: st.dataframe(all_s, use_container_width=True)

elif menu == "Bài 2 - Vận mẫu kép & Luyện tập":
    render_lesson_intro("📚 Bài 2: Vận mẫu kép & Luyện tập ghép âm", "Nắm vững 4 vận mẫu kép cơ bản và luyện tập ghép âm.")
    st.subheader("1. Vận mẫu kép cơ bản")
    cols = st.columns(4)
    for i, item in enumerate(B2_VAN_KEP_SLIDES):
        with cols[i]: render_pronunciation_card({"chu": item["vận"], "hdsd": item["hướng_dẫn"], "vd_han": item["ví_dụ_hán"], "vd_py": item["ví_dụ_py"], "nghe": item["nghe"]}, "b2_vk")
    
    st.markdown("---")
    st.subheader("2. Bảng luyện tập ghép âm")
    h_cols = st.columns([1.5] + [1] * len(B2_LUYEN_TAP_FINALS))
    h_cols[0].markdown("**T/V**")
    for i, f in enumerate(B2_LUYEN_TAP_FINALS): h_cols[i+1].markdown(f"**{f}**")
    for init in B2_LUYEN_TAP_ROWS.keys():
        r_cols = st.columns([1.5] + [1] * len(B2_LUYEN_TAP_FINALS))
        r_cols[0].markdown(f"**{init}**")
        for i, combo in enumerate(B2_LUYEN_TAP_ROWS[init]):
            if combo:
                with r_cols[i+1]:
                    with st.popover(combo, use_container_width=True):
                        for t in add_tones(combo): st.write(f"- {t}")

elif menu == "Bài 3 - Phiên âm nâng cao (đang khóa)":
    if not teacher_unlock: st.warning("Đang khóa. Bật mở khóa ở sidebar.")
    else:
        render_lesson_intro("🔒 Bài 3: Phiên âm nâng cao", "Học các thanh mẫu khó và vận mẫu kép mở rộng.")
        for g in B2_THANH_MAU_DATA:
            st.markdown(f"#### {g['ten']}")
            cols = st.columns(4)
            for i, item in enumerate(g["items"]):
                with cols[i%4]: render_pronunciation_card(item, "b3_tm")
        for g in B2_VAN_MAU_KEP_DATA:
            st.markdown(f"#### {g['nhom']}")
            cols = st.columns(4)
            for i, item in enumerate(g["items"]):
                with cols[i%4]: render_pronunciation_card(item, "b3_vk")

elif menu == "Bài 3 - Nét chữ Hán cơ bản (đang khóa)":
    if not teacher_unlock: st.warning("Đang khóa.")
    else:
        render_lesson_intro("🔒 Bài 3: Nét chữ Hán cơ bản", "Rèn nét cơ bản và quy tắc thứ tự nét.")
        st.table(NET_CO_BAN)

st.sidebar.markdown("---")
st.sidebar.write("加油! (Jiā yóu! - Cố lên!)")
