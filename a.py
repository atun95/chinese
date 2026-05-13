import streamlit as st
import random
import json
import streamlit.components.v1 as components
import csv
from datetime import datetime
from pathlib import Path

# Cấu hình trang
st.set_page_config(page_title="Học Tiếng Trung", page_icon="🇨🇳", layout="wide")
st.markdown(
    """
    <style>
    .block-container { padding-top: 1.1rem; }
    .main h1, .main h2, .main h3 { letter-spacing: 0.2px; }
    .lesson-card {
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 12px 14px;
        margin-bottom: 10px;
        background-color: #fafafa;
    }
    .lesson-card b { font-size: 1.02rem; }
    .lesson-muted { color: #6b7280; }
    
    /* Table Redesign */
    .chinese-table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 24px;
        background-color: white;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        border: 1px solid #e2e8f0;
    }
    .chinese-table th {
        padding: 18px;
        text-align: left;
        font-size: 1.2rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .chinese-table td {
        padding: 14px 18px;
        border: 1px solid #f1f5f9;
        color: #1e293b;
        font-size: 1.1rem;
    }
    .tm-header { background-color: #0f172a; color: white; }
    .vm-header { background-color: #fbbf24; color: #0f172a; }
    .cat-col { 
        background-color: #f8fafc; 
        font-weight: 600; 
        width: 25%; 
        color: #475569;
        border-right: 2px solid #e2e8f0 !important;
    }
    .pinyin-text {
        font-family: 'Inter', system-ui, sans-serif;
        font-weight: 700;
        color: #2563eb;
        font-size: 1.25rem;
        letter-spacing: 1px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- DỮ LIỆU ---
thanh_mau = {
    'b': 'bờ (môi, không bật hơi)', 'p': 'phờ (môi, bật hơi)', 'm': 'mờ (môi, mũi)',
    'f': 'phờ (răng-môi)', 'd': 'đờ (lưỡi, không bật hơi)', 't': 'thờ (lưỡi, bật hơi)',
    'n': 'nờ (lưỡi, mũi)', 'l': 'lờ (lưỡi, bên)', 'g': 'cờ (họng, không bật hơi)',
    'k': 'khờ (họng, bật hơi)', 'h': 'hờ (họng, xát)'
}

van_mau = {
    'a': 'a (miệng mở rộng)', 'o': 'ô (miệng tròn)', 'e': 'ơ/ưa (miệng hơi mở)', 
    'i': 'i (miệng hẹp, ngang)', 'u': 'u (môi tròn)', 'ü': 'uy (môi tròn, lưỡi cao)'
}

B1_INITIALS_CARDS = [
    {"chu": "b", "hdsd": "Âm môi, không bật hơi. Đọc gần giống 'p' nhẹ.", "vd_han": "爸爸", "vd_py": "bàba", "nghe": "爸爸"},
    {"chu": "p", "hdsd": "Âm môi, bật hơi mạnh. Đọc giống 'ph' nhưng mím môi.", "vd_han": "跑步", "vd_py": "pǎobù", "nghe": "跑步"},
    {"chu": "m", "hdsd": "Âm môi, âm mũi. Đọc giống 'm'.", "vd_han": "妈妈", "vd_py": "māma", "nghe": "妈妈"},
    {"chu": "f", "hdsd": "Âm răng môi. Đọc giống 'ph'.", "vd_han": "饭", "vd_py": "fàn", "nghe": "饭"},
    {"chu": "d", "hdsd": "Âm đầu lưỡi, không bật hơi. Đọc gần giống 't'.", "vd_han": "弟弟", "vd_py": "dìdi", "nghe": "弟弟"},
    {"chu": "t", "hdsd": "Âm đầu lưỡi, bật hơi mạnh. Đọc giống 'th'.", "vd_han": "他", "vd_py": "tā", "nghe": "他"},
    {"chu": "n", "hdsd": "Âm đầu lưỡi, âm mũi. Đọc giống 'n'.", "vd_han": "你", "vd_py": "nǐ", "nghe": "你"},
    {"chu": "l", "hdsd": "Âm đầu lưỡi, âm bên. Đọc giống 'l'.", "vd_han": "老师", "vd_py": "lǎoshī", "nghe": "老师"},
    {"chu": "g", "hdsd": "Âm cuống lưỡi, không bật hơi. Đọc gần giống 'c/k'.", "vd_han": "哥哥", "vd_py": "gēge", "nghe": "哥哥"},
    {"chu": "k", "hdsd": "Âm cuống lưỡi, bật hơi mạnh. Đọc gần giống 'kh'.", "vd_han": "渴", "vd_py": "kě", "nghe": "渴"},
    {"chu": "h", "hdsd": "Âm cuống lưỡi, âm xát. Đọc giống 'h'.", "vd_han": "好", "vd_py": "hǎo", "nghe": "好"},
]

B1_FINALS_CARDS = [
    {"chu": "a", "hdsd": "Miệng mở rộng, lưỡi hạ thấp. Đọc giống 'a'.", "vd_han": "爸", "vd_py": "bà", "nghe": "爸"},
    {"chu": "o", "hdsd": "Miệng hơi tròn, lưỡi rút về sau. Đọc giống 'ô'.", "vd_han": "我", "vd_py": "wǒ", "nghe": "我"},
    {"chu": "e", "hdsd": "Miệng hơi mở, lưỡi rút về sau. Đọc giống 'ưa' hoặc 'ơ'.", "vd_han": "鹅", "vd_py": "é", "nghe": "鹅"},
    {"chu": "i", "hdsd": "Miệng dẹt, lưỡi nâng cao. Đọc giống 'i'.", "vd_han": "一", "vd_py": "yī", "nghe": "一"},
    {"chu": "u", "hdsd": "Môi tròn, lưỡi rút về sau. Đọc giống 'u'.", "vd_han": "五", "vd_py": "wǔ", "nghe": "五"},
    {"chu": "ü", "hdsd": "Môi tròn (giống u), lưỡi nâng cao (giống i). Đọc giống 'uy'.", "vd_han": "绿", "vd_py": "lǜ", "nghe": "绿"},
]

xung_ho_tu_lay = [
    {"Chữ Hán": "爸爸", "Pinyin": "bàba", "Nghĩa tiếng Việt": "ba/bố"},
    {"Chữ Hán": "妈妈", "Pinyin": "māma", "Nghĩa tiếng Việt": "mẹ/má"},
    {"Chữ Hán": "哥哥", "Pinyin": "gēge", "Nghĩa tiếng Việt": "anh trai"},
    {"Chữ Hán": "姐姐", "Pinyin": "jiějie", "Nghĩa tiếng Việt": "chị gái"},
    {"Chữ Hán": "弟弟", "Pinyin": "dìdi", "Nghĩa tiếng Việt": "em trai"},
    {"Chữ Hán": "妹妹", "Pinyin": "mèimei", "Nghĩa tiếng Việt": "em gái"},
    {"Chữ Hán": "爷爷", "Pinyin": "yéye", "Nghĩa tiếng Việt": "ông nội"},
    {"Chữ Hán": "奶奶", "Pinyin": "nǎinai", "Nghĩa tiếng Việt": "bà nội"}
]

dai_tu_xung_ho = [
    {"Chữ Hán": "我", "Pinyin": "wǒ", "Nghĩa tiếng Việt": "tôi/mình"},
    {"Chữ Hán": "你", "Pinyin": "nǐ", "Nghĩa tiếng Việt": "bạn/cậu"},
    {"Chữ Hán": "他", "Pinyin": "tā", "Nghĩa tiếng Việt": "anh ấy/ông ấy"},
    {"Chữ Hán": "她", "Pinyin": "tā", "Nghĩa tiếng Việt": "cô ấy/chị ấy"},
    {"Chữ Hán": "我们", "Pinyin": "wǒmen", "Nghĩa tiếng Việt": "chúng tôi/chúng ta"},
    {"Chữ Hán": "你们", "Pinyin": "nǐmen", "Nghĩa tiếng Việt": "các bạn"},
    {"Chữ Hán": "他们", "Pinyin": "tāmen", "Nghĩa tiếng Việt": "họ"}
]

tu_vung_bo_sung = [
    {"Chữ Hán": "老师", "Pinyin": "lǎoshī", "Nghĩa tiếng Việt": "thầy/cô giáo"},
    {"Chữ Hán": "学生", "Pinyin": "xuéshēng", "Nghĩa tiếng Việt": "học sinh"},
    {"Chữ Hán": "很", "Pinyin": "hěn", "Nghĩa tiếng Việt": "rất"},
    {"Chữ Hán": "忙", "Pinyin": "máng", "Nghĩa tiếng Việt": "bận"},
    {"Chữ Hán": "不", "Pinyin": "bù", "Nghĩa tiếng Việt": "không"}
]

# Bài 2 — vận mẫu kép (theo slide) + bảng luyện tập thanh mẫu × vận mẫu
B2_VAN_KEP_SLIDES = [
    {
        "vận": "ai",
        "hướng_dẫn": "Miệng mở rộng, đọc giống “ai” trong tiếng Việt.",
        "ví_dụ_hán": "来",
        "ví_dụ_py": "lái",
        "nghe": "来",
    },
    {
        "vận": "ei",
        "hướng_dẫn": "Khẩu hình miệng hơi dẹt, đọc gần giống “ây” trong tiếng Việt.",
        "ví_dụ_hán": "内",
        "ví_dụ_py": "nèi",
        "nghe": "内",
    },
    {
        "vận": "ao",
        "hướng_dẫn": "Miệng mở rộng, đọc gần giống “ao” trong tiếng Việt.",
        "ví_dụ_hán": "宝贝",
        "ví_dụ_py": "bǎobèi",
        "nghe": "宝贝",
    },
    {
        "vận": "ou",
        "hướng_dẫn": "Miệng ngậm hơi tròn, đọc gần giống “âu” trong tiếng Việt.",
        "ví_dụ_hán": "狗",
        "ví_dụ_py": "gǒu",
        "nghe": "狗",
    },
]

B2_THANH_MAU_DATA = [
    {
        "ky_hieu": "j / q / x",
        "ten": "Nhóm mặt lưỡi",
        "items": [
            {"chu": "j", "hdsd": "Mặt lưỡi áp sát ngạc cứng, không bật hơi.", "vd_han": "鸡", "vd_py": "jī", "nghe": "jī"},
            {"chu": "q", "hdsd": "Vị trí giống 'j' nhưng cần bật hơi mạnh.", "vd_han": "七", "vd_py": "qī", "nghe": "qī"},
            {"chu": "x", "hdsd": "Âm xát nhẹ, luồng hơi đi ra đều.", "vd_han": "西", "vd_py": "xī", "nghe": "xī"},
        ]
    },
    {
        "ky_hieu": "zh / ch / sh / r",
        "ten": "Nhóm uốn lưỡi",
        "items": [
            {"chu": "zh", "hdsd": "Đầu lưỡi uốn ngược chạm ngạc cứng, không bật hơi.", "vd_han": "这", "vd_py": "zhè", "nghe": "zhè"},
            {"chu": "ch", "hdsd": "Vị trí giống 'zh' nhưng bật hơi mạnh.", "vd_han": "吃", "vd_py": "chī", "nghe": "chī"},
            {"chu": "sh", "hdsd": "Uốn lưỡi, để khe hở nhỏ cho hơi thoát ra.", "vd_han": "是", "vd_py": "shì", "nghe": "shì"},
            {"chu": "r", "hdsd": "Âm uốn lưỡi, có độ rung nhẹ của dây thanh.", "vd_han": "日", "vd_py": "rì", "nghe": "rì"},
        ]
    },
    {
        "ky_hieu": "z / c / s",
        "ten": "Nhóm đầu lưỡi - răng",
        "items": [
            {"chu": "z", "hdsd": "Đầu lưỡi chạm mặt sau răng trên, không bật hơi.", "vd_han": "字", "vd_py": "zì", "nghe": "zì"},
            {"chu": "c", "hdsd": "Vị trí giống 'z' nhưng bật hơi mạnh.", "vd_han": "词", "vd_py": "cí", "nghe": "cí"},
            {"chu": "s", "hdsd": "Đầu lưỡi để hở khe nhỏ với răng trên, âm xát.", "vd_han": "四", "vd_py": "sì", "nghe": "sì"},
        ]
    },
    {
        "ky_hieu": "y / w",
        "ten": "Âm đệm",
        "items": [
            {"chu": "y", "hdsd": "Phát âm gần giống 'i' nhưng đi kèm vận mẫu khác.", "vd_han": "一", "vd_py": "yī", "nghe": "yī"},
            {"chu": "w", "hdsd": "Phát âm gần giống 'u' nhưng đi kèm vận mẫu khác.", "vd_han": "五", "vd_py": "wǔ", "nghe": "wǔ"},
        ]
    }
]

B2_VAN_MAU_KEP_DATA = [
    {
        "nhom": "Nhóm mở rộng từ i",
        "items": [
            {"chu": "ia", "hdsd": "Đọc i mở nhanh sang a.", "vd_han": "家", "vd_py": "jiā", "nghe": "jiā"},
            {"chu": "ie", "hdsd": "Đọc i trượt sang e.", "vd_han": "姐", "vd_py": "jiě", "nghe": "jiě"},
            {"chu": "iao", "hdsd": "Đọc i -> a -> o liền mạch.", "vd_han": "小", "vd_py": "xiǎo", "nghe": "xiǎo"},
            {"chu": "iu", "hdsd": "Thực chất là i + ou.", "vd_han": "六", "vd_py": "liù", "nghe": "liù"},
        ]
    },
    {
        "nhom": "Nhóm mở rộng từ u/ü",
        "items": [
            {"chu": "ua", "hdsd": "Tròn môi u mở sang a.", "vd_han": "花", "vd_py": "huā", "nghe": "huā"},
            {"chu": "uo", "hdsd": "Tròn môi u mở sang o.", "vd_han": "我", "vd_py": "wǒ", "nghe": "wǒ"},
            {"chu": "uai", "hdsd": "Đọc u -> a -> i nhanh.", "vd_han": "快", "vd_py": "kuài", "nghe": "kuài"},
            {"chu": "ui", "hdsd": "Thực chất là u + ei.", "vd_han": "水", "vd_py": "shuǐ", "nghe": "shuǐ"},
            {"chu": "üe", "hdsd": "Tròn môi ü mở sang e.", "vd_han": "月", "vd_py": "yuè", "nghe": "yuè"},
        ]
    }
]

B2_LUYEN_TAP_FINALS = ["a", "o", "e", "i", "u", "ü", "ai", "ei", "ao", "ou"]
B2_LUYEN_TAP_ROWS = {
    "b": ["ba", "bo", "", "bi", "bu", "", "bai", "bei", "bao", ""],
    "p": ["pa", "po", "", "pi", "pu", "", "pai", "pei", "pao", "pou"],
    "m": ["ma", "mo", "me", "mi", "mu", "", "mai", "mei", "mao", "mou"],
    "f": ["fa", "fo", "", "", "fu", "", "", "fei", "", "fou"],
    "d": ["da", "", "de", "di", "du", "", "dai", "dei", "dao", "dou"],
    "t": ["ta", "", "te", "ti", "tu", "", "tai", "", "tao", "tou"],
    "n": ["na", "", "ne", "ni", "nu", "nü", "nai", "nei", "nao", "nou"],
    "l": ["la", "", "le", "li", "lu", "lü", "lai", "lei", "lao", "lou"],
    "g": ["ga", "", "ge", "", "gu", "", "gai", "gei", "gao", "gou"],
    "k": ["ka", "", "ke", "", "ku", "", "kai", "kei", "kao", "kou"],
    "h": ["ha", "", "he", "", "hu", "", "hai", "hei", "hao", "hou"],
}

if "scores" not in st.session_state:
    st.session_state.scores = {}

SCORES_FILE = Path(__file__).with_name("scores.csv")
PROGRESS_FILE = Path(__file__).with_name("progress_lesson1.json")


def save_progress():
    """Lưu tiến độ làm bài hiện tại vào file JSON"""
    try:
        # Chỉ lưu các phím liên quan đến bài tập
        quiz_keys = [k for k in st.session_state.keys() if k.startswith(("bai", "vanmau_", "docviet_", "tone_", "cau_ngan_", "q2_", "student_name"))]
        data = {
            "scores": st.session_state.scores,
            "values": {k: st.session_state[k] for k in quiz_keys}
        }
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Lỗi lưu tiến độ: {e}")


def load_progress():
    """Tải tiến độ đã lưu từ file JSON"""
    if PROGRESS_FILE.exists():
        try:
            with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if "scores" in data:
                    st.session_state.scores = data["scores"]
                if "values" in data:
                    for k, v in data["values"].items():
                        st.session_state[k] = v
        except Exception as e:
            print(f"Lỗi tải tiến độ: {e}")


# Tải tiến độ ngay khi khởi động
load_progress()


def save_score_row(row_data):
    file_exists = SCORES_FILE.exists()
    try:
        with open(SCORES_FILE, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "thoi_gian",
                    "hoc_vien",
                    "tong_diem",
                    "tong_cau",
                    "phan_tram",
                    "bai1",
                    "bai2",
                    "bai3",
                    "bai4",
                    "bai5",
                    "bai6",
                ],
            )
            if not file_exists:
                writer.writeheader()
            writer.writerow(row_data)
        return True
    except Exception as e:
        st.error(f"Lỗi khi lưu file CSV: {e}")
        return False


def load_all_scores():
    if not SCORES_FILE.exists():
        return []
    with open(SCORES_FILE, "r", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        return list(reader)


def shuffled_options(options, seed_text):
    opts = options[:]
    rnd = random.Random(seed_text)
    rnd.shuffle(opts)
    return opts


def add_tones(base):
    # Quy tắc đánh dấu thanh điệu: a > o/e > i/u (thứ tự ưu tiên)
    # Riêng iu và ui thì đánh vào âm sau
    vowels = {
        'a': ['ā', 'á', 'ǎ', 'à'],
        'o': ['ō', 'ó', 'ǒ', 'ò'],
        'e': ['ē', 'é', 'ě', 'è'],
        'i': ['ī', 'í', 'ǐ', 'ì'],
        'u': ['ū', 'ú', 'ǔ', 'ù'],
        'ü': ['ǖ', 'ǘ', 'ǚ', 'ǜ']
    }
    
    tones = []
    for i in range(4):
        res = base
        if 'a' in res:
            res = res.replace('a', vowels['a'][i])
        elif 'e' in res:
            res = res.replace('e', vowels['e'][i])
        elif 'o' in res:
            res = res.replace('o', vowels['o'][i])
        elif 'iu' in res:
            res = res.replace('u', vowels['u'][i])
        elif 'ui' in res:
            res = res.replace('i', vowels['i'][i])
        elif 'i' in res:
            res = res.replace('i', vowels['i'][i])
        elif 'u' in res:
            res = res.replace('u', vowels['u'][i])
        elif 'ü' in res:
            res = res.replace('ü', vowels['ü'][i])
        tones.append(res)
    return tones


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

# --- GIAO DIỆN CHÍNH ---
st.title("Học Pinyin Cơ Bản")
st.caption("Trình bày theo giáo án từng bài, gọn và dễ theo dõi trên lớp.")
st.markdown("""
<style>
    .chinese-table { width: 100%; border-collapse: collapse; margin-top: 10px; }
    .chinese-table th, .chinese-table td { border: 1px solid #ddd; padding: 8px; text-align: left; }
    .tm-header { background-color: #0f172a; color: white; }
    .vm-header { background-color: #fbbf24; color: #0f172a; }
    .cat-col { font-weight: bold; background-color: #f8fafc; }
    .pinyin-text { font-family: 'Courier New', monospace; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Sidebar - Điều hướng bài tập
st.sidebar.header("Danh mục giáo án")
teacher_unlock = st.sidebar.checkbox("Mở khóa nội dung Bài 2 (GV)")
menu = st.sidebar.radio(
    "Chọn mục:",
    [
        "Bài 1 - Phiên âm cơ bản",
        "Bài 1 - TỪ VỰNG CƠ BẢN",
        "Bài 1 - Bài tập",
        "Bài 2 - Vận mẫu kép & Luyện tập",
        "Bài 3 - Phiên âm nâng cao (đang khóa)",
        "Bài 3 - Nét chữ Hán cơ bản (đang khóa)"
    ]
)

# --- 1. Kiến thức cần nhớ ---
if menu == "Bài 1 - Phiên âm cơ bản":
    st.header("📚 Bài 1: Học phiên âm cơ bản")
    st.markdown(
        """
        <div class="lesson-card">
            <b>Mục tiêu</b><br/>
            <span class="lesson-muted">Nắm thanh mẫu cơ bản, vận mẫu đơn, 5 thanh điệu và biến điệu thanh 3.</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("📊 Bảng tổng hợp Thanh mẫu & Vận mẫu", expanded=True):
        st.markdown(
            """
            <div style='margin-bottom: 10px;'>
                <span style='background-color: #0f172a; color: white; padding: 5px 15px; border-radius: 5px; font-weight: bold;'>1</span>
                <span style='font-size: 1.3rem; font-weight: bold; margin-left: 10px;'>声母 Thanh mẫu (Initials)</span>
            </div>
            <table class="chinese-table">
                <tr class="tm-header">
                    <th style="width: 30%;">Vị trí phát âm</th>
                    <th>Thanh mẫu</th>
                </tr>
                <tr><td class="cat-col">Âm môi</td><td><span class="pinyin-text">b &nbsp; p &nbsp; m</span></td></tr>
                <tr><td class="cat-col">Âm môi răng</td><td><span class="pinyin-text">f</span></td></tr>
                <tr><td class="cat-col">Âm tròn môi</td><td><span class="pinyin-text">w</span></td></tr>
                <tr><td class="cat-col">Âm đầu lưỡi trước</td><td><span class="pinyin-text">z &nbsp; c &nbsp; s</span></td></tr>
                <tr><td class="cat-col">Âm đầu lưỡi giữa</td><td><span class="pinyin-text">d &nbsp; t &nbsp; n &nbsp; l</span></td></tr>
                <tr><td class="cat-col">Âm đầu lưỡi sau</td><td><span class="pinyin-text">zh &nbsp; ch &nbsp; sh &nbsp; r</span></td></tr>
                <tr><td class="cat-col">Âm mặt lưỡi</td><td><span class="pinyin-text">j &nbsp; q &nbsp; x</span></td></tr>
                <tr><td class="cat-col">Âm cuống lưỡi</td><td><span class="pinyin-text">g &nbsp; k &nbsp; h &nbsp; y</span></td></tr>
            </table>
            """,
            unsafe_allow_html=True
        )

        # 2. Vận mẫu table
        st.markdown(
            """
            <div style='margin-bottom: 10px; margin-top: 20px;'>
                <span style='background-color: #fbbf24; color: #0f172a; padding: 5px 15px; border-radius: 5px; font-weight: bold;'>2</span>
                <span style='font-size: 1.3rem; font-weight: bold; margin-left: 10px;'>韵母 Vận mẫu (Finals)</span>
            </div>
            <table class="chinese-table">
                <tr class="vm-header">
                    <th style="width: 20%;">Loại</th>
                    <th style="text-align: center;">a</th>
                    <th style="text-align: center;">o</th>
                    <th style="text-align: center;">e</th>
                    <th style="text-align: center;">i</th>
                    <th style="text-align: center;">u</th>
                    <th style="text-align: center;">ü</th>
                </tr>
                <tr>
                    <td class="cat-col">Đơn</td>
                    <td style="text-align: center;"><span class="pinyin-text">a</span></td>
                    <td style="text-align: center;"><span class="pinyin-text">o</span></td>
                    <td style="text-align: center;"><span class="pinyin-text">e</span></td>
                    <td style="text-align: center;"><span class="pinyin-text">i</span></td>
                    <td style="text-align: center;"><span class="pinyin-text">u</span></td>
                    <td style="text-align: center;"><span class="pinyin-text">ü</span></td>
                </tr>
                <tr>
                    <td class="cat-col">Kép</td>
                    <td style="text-align: center;"><span class="pinyin-text">ai ao</span></td>
                    <td style="text-align: center;"><span class="pinyin-text">ou</span></td>
                    <td style="text-align: center;"><span class="pinyin-text">ei</span></td>
                    <td style="text-align: center;"><span class="pinyin-text">ia ie<br>iao iu</span></td>
                    <td style="text-align: center;"><span class="pinyin-text">ua uo<br>uai ui</span></td>
                    <td style="text-align: center;"><span class="pinyin-text">üe</span></td>
                </tr>
                <tr>
                    <td class="cat-col">Mũi</td>
                    <td style="text-align: center;"><span class="pinyin-text">an ang</span></td>
                    <td style="text-align: center;"><span class="pinyin-text">ong</span></td>
                    <td style="text-align: center;"><span class="pinyin-text">en eng</span></td>
                    <td style="text-align: center;"><span class="pinyin-text">ian in<br>iang ing<br>iong</span></td>
                    <td style="text-align: center;"><span class="pinyin-text">uan un<br>uang</span></td>
                    <td style="text-align: center;"><span class="pinyin-text">üan ün</span></td>
                </tr>
            </table>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.subheader("1. Thanh mẫu và vận mẫu cơ bản")
    
    st.markdown("#### 1.1. Thanh mẫu (Initials)")
    cols_tm = st.columns(4)
    for i, item in enumerate(B1_INITIALS_CARDS):
        with cols_tm[i % 4]:
            render_pronunciation_card(item, "b1_tm")
            
    st.markdown("---")
    st.markdown("#### 1.2. Vận mẫu (Finals)")
    cols_vm = st.columns(4)
    for i, item in enumerate(B1_FINALS_CARDS):
        with cols_vm[i % 4]:
            render_pronunciation_card(item, "b1_vm")
    
    st.markdown("---")
    st.subheader("2. Thanh điệu (Tones)")
    
    st.markdown("#### 2.1. Bốn thanh điệu cơ bản")
    st.write("1️⃣ Thanh 1: **mā** (cao và ngang)")
    st.write("2️⃣ Thanh 2: **má** (đi lên)")
    st.write("3️⃣ Thanh 3: **mǎ** (hạ xuống rồi lên)")
    st.write("4️⃣ Thanh 4: **mà** (đi xuống mạnh)")
    st.write("5️⃣ Thanh nhẹ: **ma** (nhẹ, ngắn, không nhấn)")

    st.markdown("#### 2.2. Thanh nhẹ (轻声)")
    st.write("Ví dụ từ láy đọc thanh nhẹ ở âm tiết thứ hai:")
    st.write("- **māma** (妈妈): âm tiết **ma** thứ hai là thanh nhẹ")
    st.write("- **bàba** (爸爸): âm tiết **ba** thứ hai là thanh nhẹ")
    st.write("- **gēge** (哥哥): âm tiết **ge** thứ hai là thanh nhẹ")
    st.write("- **jiějie** (姐姐): âm tiết **jie** thứ hai là thanh nhẹ")
    st.write("- **dìdi** (弟弟): âm tiết **di** thứ hai là thanh nhẹ")

    st.markdown("#### 2.3. Quy tắc biến điệu thanh 3")
    st.info(
        "Quy tắc chuẩn: khi **hai thanh 3 liền nhau (3 + 3)**, "
        "âm tiết đứng trước phải đổi thành **thanh 2**."
    )
    st.write("Ví dụ 1: **nǐ hǎo** → đọc thành **ní hǎo**.")
    st.write("Ví dụ 2: **wǒ hěn** → đọc thành **wó hěn**.")
    st.warning(
        "Với chuỗi **3 + 3 + 3**: khi đọc liền mạch, thường đổi các thanh 3 đứng trước thành thanh 2.\n\n"
        "Ví dụ: **nǐ wǒ hǎo** thường đọc gần như **ní wó hǎo** (2 + 2 + 3)."
    )

# --- 2. BÀI 1: TỪ VỰNG CƠ BẢN ---
elif menu == "Bài 1 - TỪ VỰNG CƠ BẢN":
    st.header("👨‍👩‍👧‍👦 Bài 1: Học TỪ VỰNG CƠ BẢN")
    st.markdown(
        """
        <div class="lesson-card">
            <b>Mục tiêu</b><br/>
            <span class="lesson-muted">Học từ xưng hô, đại từ thường dùng và từ mở rộng để ghép câu ngắn.</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.subheader("Từ xưng hô dạng từ láy")
    st.table(xung_ho_tu_lay)
    st.subheader("Đại từ xưng hô cơ bản")
    st.table(dai_tu_xung_ho)
    st.subheader("Từ vựng bổ sung")
    st.table(tu_vung_bo_sung)

# --- 3. BÀI TẬP BÀI 1 ---
elif menu == "Bài 1 - Bài tập":
    st.header("📝 Bài 1: Bài tập tổng hợp")
    

    with st.expander("Bài tập 1: Mini quiz từ vựng", expanded=True):
        st.caption("Chọn nghĩa đúng nhất cho từng từ.")
        bai1_questions = [
            {"q": "lǎoshī", "choices": ["thầy/cô giáo", "học sinh", "rất"], "answer": "thầy/cô giáo"},
            {"q": "xuéshēng", "choices": ["không", "học sinh", "bận"], "answer": "học sinh"},
            {"q": "hěn", "choices": ["rất", "không", "bận"], "answer": "rất"},
            {"q": "máng", "choices": ["bận", "mẹ", "bố"], "answer": "bận"},
            {"q": "bù", "choices": ["không", "rất", "bạn"], "answer": "không"},
            {"q": "wǒ", "choices": ["tôi/mình", "bạn/cậu", "anh ấy/cô ấy"], "answer": "tôi/mình"},
            {"q": "nǐ", "choices": ["không", "bạn/cậu", "rất"], "answer": "bạn/cậu"},
            {"q": "māma", "choices": ["bố", "mẹ/má", "chị gái"], "answer": "mẹ/má"},
        ]
        score = 0
        for idx, item in enumerate(bai1_questions):
            choices = shuffled_options(item["choices"], f"mini-{idx}-{item['q']}")
            key = f"bai1_q_{idx}"
            
            # Lấy index đã lưu nếu có
            saved_val = st.session_state.get(key)
            default_idx = 0
            if saved_val in choices:
                default_idx = choices.index(saved_val)
                
            selected = st.radio(
                f"Câu {idx + 1}: {item['q']} nghĩa là gì?",
                choices,
                index=default_idx,
                key=key,
            )
            if selected == item["answer"]:
                score += 1
        if st.button("Chấm điểm mini quiz từ vựng"):
            total = len(bai1_questions)
            st.session_state.scores["bai1"] = (score, total)
            save_progress()
            st.success(f"Bạn đúng {score}/{total} câu.")

    with st.expander("Bài tập 2: Âm bật hơi", expanded=False):
        st.caption("Nhận diện nhanh nhóm âm bật hơi.")
        st.write("Chọn các âm là **ÂM BẬT HƠI**:")
        col1, col2, col3 = st.columns(3)
        with col1:
            b = st.checkbox("B", key="q2_b")
            p = st.checkbox("P", key="q2_p")
        with col2:
            d = st.checkbox("D", key="q2_d")
            t = st.checkbox("T", key="q2_t")
        with col3:
            g = st.checkbox("G", key="q2_g")
            k = st.checkbox("K", key="q2_k")

        if st.button("Kiểm tra kết quả"):
            correct = (p and t and k) and not (b or d or g)
            if correct:
                st.balloons()
                st.success("Tuyệt vời! P, T, K là các âm cần bật hơi mạnh.")
                st.session_state.scores["bai2"] = (1, 1)
            else:
                st.error("Sai rồi! Nhớ nhé: P, T, K là các âm bật hơi.")
                st.session_state.scores["bai2"] = (0, 1)
            save_progress()

    with st.expander("Bài tập 3: Điền vận mẫu", expanded=False):
        st.caption("Điền đúng vận mẫu để hoàn chỉnh pinyin.")
        questions = [
            ("m___ma (mẹ)", "ā"),
            ("n___ (bạn)", "ǐ"),
            ("l___oshī (thầy/cô giáo)", "ǎ"),
            ("xu___shēng (học sinh)", "é"),
            ("h___n (rất)", "ě"),
            ("m___ng (bận)", "á"),
            ("b___ (không)", "ù"),
            ("w___ (tôi/mình)", "ǒ"),
        ]
        options = ["...", "ā", "á", "ǎ", "à", "ē", "é", "ě", "è", "ǐ", "ǒ", "ù"]
        score = 0
        for idx, (q, ans) in enumerate(questions):
            key = f"vanmau_q_{idx}"
            saved_val = st.session_state.get(key)
            default_idx = 0
            if saved_val in options:
                default_idx = options.index(saved_val)
                
            res = st.selectbox(
                f"Câu {idx + 1}: Chọn vận mẫu đúng cho {q}",
                options,
                index=default_idx,
                key=key,
            )
            if res == ans:
                score += 1

        if st.button("Chấm điểm điền vận mẫu"):
            total = len(questions)
            st.session_state.scores["bai3"] = (score, total)
            save_progress()
            st.success(f"Bạn đúng {score}/{total} câu.")

    with st.expander("Bài tập 4: Đọc & viết pinyin", expanded=False):
        st.caption("Đọc pinyin và điền nghĩa tiếng Việt.")
        tu_vung = {
            "wǒ": "tôi/mình",
            "nǐ": "bạn/cậu",
            "māma": "mẹ/má",
            "lǎoshī": "thầy/cô giáo",
            "xuéshēng": "học sinh",
            "hěn": "rất",
            "máng": "bận",
            "bù": "không",
        }

        score = 0
        for py, nghia in tu_vung.items():
            key = f"docviet_{py}"
            user_ans = st.text_input(f"Nghĩa của từ '{py}' là gì?", key=key)
            if user_ans.strip().lower() == nghia:
                score += 1

        if st.button("Chấm điểm đọc & viết"):
            total = len(tu_vung)
            st.session_state.scores["bai4"] = (score, total)
            save_progress()
            st.success(f"Bạn đúng {score}/{total} câu.")

    with st.expander("Bài tập 5: Luyện thanh điệu (nghe)", expanded=False):
        st.caption("Nếu chưa nghe được, hãy bấm nút nghe lại và kiểm tra âm lượng trình duyệt.")
        tone_questions = [
            {"hanzi": "妈妈", "pinyin": "māma", "choices": ["māma", "máng", "mǎma"], "answer": "māma"},
            {"hanzi": "老师", "pinyin": "lǎoshī", "choices": ["làoshī", "lǎoshī", "láoshī"], "answer": "lǎoshī"},
            {"hanzi": "学生", "pinyin": "xuéshēng", "choices": ["xuěshēng", "xuéshēng", "xuesheng"], "answer": "xuéshēng"},
            {"hanzi": "很", "pinyin": "hěn", "choices": ["hèn", "hén", "hěn"], "answer": "hěn"},
            {"hanzi": "忙", "pinyin": "máng", "choices": ["máng", "mǎng", "màng"], "answer": "máng"},
            {"hanzi": "不", "pinyin": "bù", "choices": ["bù", "bú", "bǔ"], "answer": "bù"},
        ]
        score = 0
        for idx, q in enumerate(tone_questions):
            st.write(f"Câu {idx + 1}: Nghe và chọn pinyin đúng")
            if st.button(f"🔊 Nghe: {q['hanzi']}", key=f"listen_{idx}"):
                components.html(
                    f"""
                    <script>
                    const text = {q["hanzi"]!r};
                    const u = new SpeechSynthesisUtterance(text);
                    u.lang = "zh-CN";
                    u.rate = 0.9;
                    window.speechSynthesis.cancel();
                    window.speechSynthesis.speak(u);
                    </script>
                    """,
                    height=0,
                )
            
            key = f"tone_q_{idx}"
            saved_val = st.session_state.get(key)
            default_idx = 0
            if saved_val in q["choices"]:
                default_idx = q["choices"].index(saved_val)
                
            selected = st.radio("Chọn đáp án:", q["choices"], index=default_idx, key=key)
            if selected == q["answer"]:
                score += 1

        if st.button("Chấm điểm thanh điệu"):
            total = len(tone_questions)
            st.session_state.scores["bai5"] = (score, total)
            save_progress()
            st.success(f"Bạn đúng {score}/{total} câu.")

    with st.expander("Bài tập 6: Câu ngắn", expanded=False):
        st.caption("Chọn nghĩa đúng của câu ngắn.")
        short_sentence_questions = [
            {"q": "wǒ hěn máng", "choices": ["tôi rất bận", "tôi không bận", "bạn rất bận"], "answer": "tôi rất bận"},
            {"q": "nǐ bù máng", "choices": ["bạn không bận", "bạn rất bận", "tôi không bận"], "answer": "bạn không bận"},
            {"q": "wǒ shì xuéshēng", "choices": ["tôi là học sinh", "tôi là thầy giáo", "bạn là học sinh"], "answer": "tôi là học sinh"},
            {"q": "tā shì lǎoshī", "choices": ["anh ấy/cô ấy là thầy cô giáo", "anh ấy/cô ấy là học sinh", "tôi là thầy cô giáo"], "answer": "anh ấy/cô ấy là thầy cô giáo"},
        ]
        score = 0
        for idx, item in enumerate(short_sentence_questions):
            key = f"cau_ngan_q_{idx}"
            saved_val = st.session_state.get(key)
            default_idx = 0
            if saved_val in item["choices"]:
                default_idx = item["choices"].index(saved_val)
                
            selected = st.radio(f"Câu {idx + 1}: {item['q']}", item["choices"], index=default_idx, key=key)
            if selected == item["answer"]:
                score += 1
        if st.button("Chấm điểm câu ngắn"):
            total = len(short_sentence_questions)
            st.session_state.scores["bai6"] = (score, total)
            save_progress()
            st.success(f"Bạn đúng {score}/{total} câu.")

    with st.expander("Tổng kết điểm & lưu kết quả", expanded=True):
        labels = {
            "bai1": "Bài tập 1: Mini quiz từ vựng",
            "bai2": "Bài tập 2: Âm bật hơi",
            "bai3": "Bài tập 3: Điền vận mẫu",
            "bai4": "Bài tập 4: Đọc & Viết",
            "bai5": "Bài tập 5: Thanh điệu nghe",
            "bai6": "Bài tập 6: Câu ngắn",
        }
        
        missing = [label for key, label in labels.items() if key not in st.session_state.scores]
        if missing:
            st.warning("Bạn chưa hoàn thành đủ các bài sau để tính điểm tổng kết:")
            for label in missing:
                st.write(f"- {label}")
        else:
            earned_total = 0
            max_total = 0
            per_lesson_score = {}
            for key, label in labels.items():
                earned, total = st.session_state.scores[key]
                earned_total += earned
                max_total += total
                per_lesson_score[key] = f"{earned}/{total}"
                st.write(f"- {label}: {earned}/{total}")
            percent = round((earned_total / max_total) * 100, 1)
            st.success(f"Điểm overall: {earned_total}/{max_total} ({percent}%)")

            student_name = st.text_input("Ghi chú tên học viên", key="student_name")
            if st.button("Nộp bài (lưu điểm)"):
                if not student_name.strip():
                    st.error("Vui lòng nhập tên học viên trước khi nộp bài.")
                else:
                    row = {
                        "thoi_gian": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "hoc_vien": student_name.strip(),
                        "tong_diem": earned_total,
                        "tong_cau": max_total,
                        "phan_tram": percent,
                        "bai1": per_lesson_score["bai1"],
                        "bai2": per_lesson_score["bai2"],
                        "bai3": per_lesson_score["bai3"],
                        "bai4": per_lesson_score["bai4"],
                        "bai5": per_lesson_score["bai5"],
                        "bai6": per_lesson_score["bai6"],
                    }
                    if save_score_row(row):
                        st.success("Đã lưu điểm thành công vào hệ thống.")
                        # Xóa file tiến độ sau khi đã nộp bài thành công (tùy chọn)
                        if PROGRESS_FILE.exists():
                            PROGRESS_FILE.unlink()
                        st.session_state.scores = {}
                        st.rerun()

    with st.expander("📊 Lịch sử điểm đã lưu", expanded=False):
        all_scores = load_all_scores()
        if all_scores:
            keyword = st.text_input("Tìm theo tên học viên", key="search_score_name")
            if keyword.strip():
                filtered = [
                    r
                    for r in all_scores
                    if keyword.strip().lower() in (r.get("hoc_vien") or "").lower()
                ]
            else:
                filtered = all_scores
            st.dataframe(filtered, use_container_width=True)
        else:
            st.info("Chưa có dữ liệu điểm nào được lưu.")

# --- 4. BÀI 2: PHIÊN ÂM NÂNG CAO (KHÓA) ---
elif menu == "Bài 2 - Vận mẫu kép & Luyện tập":
    st.header("📚 Bài 2: Vận mẫu kép & Luyện tập ghép âm")
    st.markdown(
        """
        <div class="lesson-card">
            <b>Mục tiêu</b><br/>
            <span class="lesson-muted">Nắm vững 4 vận mẫu kép cơ bản (ai, ei, ao, ou) và luyện tập ghép âm với thanh mẫu đã học.</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("1. Vận mẫu kép (Finals) - Nhóm cơ bản")
    c_ai, c_ei, c_ao, c_ou = st.columns(4)
    for col, item in zip((c_ai, c_ei, c_ao, c_ou), B2_VAN_KEP_SLIDES):
        with col:
            render_pronunciation_card({
                "chu": item["vận"],
                "hdsd": item["hướng_dẫn"],
                "vd_han": item["ví_dụ_hán"],
                "vd_py": item["ví_dụ_py"],
                "nghe": item["nghe"]
            }, "b2_vk_base")

    st.markdown("---")
    st.subheader("2. 练习 liànxí — Bảng luyện tập ghép âm")
    st.caption("Click vào từng âm để xem 4 thanh điệu.")

    # Tiêu đề bảng
    header_cols = st.columns([1.5] + [1] * len(B2_LUYEN_TAP_FINALS))
    header_cols[0].markdown("**Thanh/Vận**")
    for i, final in enumerate(B2_LUYEN_TAP_FINALS):
        header_cols[i+1].markdown(f"**{final}**")
    
    for init in ["b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h"]:
        row_cols = st.columns([1.5] + [1] * len(B2_LUYEN_TAP_FINALS))
        row_cols[0].markdown(f"**{init}**")
        combos = B2_LUYEN_TAP_ROWS[init]
        for i, combo in enumerate(combos):
            if combo:
                with row_cols[i+1]:
                    with st.popover(combo, use_container_width=True):
                        tones = add_tones(combo)
                        for t in tones:
                            st.write(f"- {t}")
            else:
                row_cols[i+1].write("")

    st.markdown("---")
    st.subheader("3. 💡 Luyện tập đọc từ và câu ngắn")
    st.info("Ghép các thanh mẫu đã học với vận mẫu kép để tạo thành từ có nghĩa. Hãy tập đọc to!")

    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown("**🔹 Từ vựng thực hành:**")
        st.write("- **你好** (nǐ hǎo): Chào bạn")
        st.write("- **老师** (lǎoshī): Thầy/Cô giáo")
        st.write("- **大** (dà): Lớn / To")
        st.write("- **好** (hǎo): Tốt / Khỏe / Ngon")
        st.write("- **买** (mǎi): Mua")
        st.write("- **卖** (mài): Bán")
        st.write("- **猫** (māo): Con mèo")
        st.write("- **马** (mǎ): Con ngựa")
        st.write("- **口** (kǒu): Miệng / Nhân khẩu")
        st.write("- **白** (bái): Màu trắng")
        st.write("- **开** (kāi): Mở / Nở (hoa)")

    with col_t2:
        st.markdown("**🔹 Câu nói thực hành:**")
        st.write("- **你好吗?** (nǐ hǎo ma?): Bạn khỏe không?")
        st.write("- **我很好。** (wǒ hěn hǎo): Tôi rất khỏe.")
        st.write("- **他不来。** (tā bù lái): Anh ấy không đến.")
        st.write("- **妈妈买猫。** (māma mǎi māo): Mẹ mua mèo.")
        st.write("- **爸爸 mǎi mǎ.** (bàba mǎi mǎ): Ba mua ngựa.")
        st.write("- **老师忙吗?** (lǎoshī máng ma?): Thầy cô bận không?")
        st.write("- **他不忙。** (tā bù máng): Anh ấy không bận.")
        st.write("- **大马。** (dà mǎ): Ngựa lớn.")
        st.write("- **白猫。** (bái māo): Mèo trắng.")
        st.write("- **开门。** (kāi mén): Mở cửa (m-en bài sau sẽ học kỹ hơn)")

    if st.button("🔊 Nghe mẫu toàn bộ phần thực hành"):
        full_practice_text = (
            "nǐ hǎo. lǎoshī. dà. hǎo. mǎi. mài. māo. mǎ. kǒu. bái. kāi. "
            "nǐ hǎo ma? wǒ hěn hǎo. tā bù lái. māma mǎi māo. bàba mǎi mǎ. "
            "lǎoshī máng ma? tā bù máng. dà mǎ. bái māo. kāi mén."
        )
        play_audio(full_practice_text)

# --- 4. BÀI 3: PHIÊN ÂM NÂNG CAO (KHÓA) ---
elif menu == "Bài 3 - Phiên âm nâng cao (đang khóa)":
    st.header("🔒 Bài 3: Phiên âm nâng cao")
    if not teacher_unlock:
        st.warning("Nội dung này đang khóa. Bật 'Mở khóa nội dung Bài 2 (GV)' ở sidebar để xem.")
    else:
        st.success("Chế độ giáo viên đã bật. Đây là nội dung giảng dạy Bài 3.")
        st.markdown(
            """
            <div class="lesson-card">
                <b>Mục tiêu</b><br/>
                <span class="lesson-muted">Học các thanh mẫu khó (j, q, x, zh, ch, sh, r...) và vận mẫu kép mở rộng.</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.subheader("1. Thanh mẫu còn lại (Initials)")
        for group in B2_THANH_MAU_DATA:
            st.markdown(f"#### {group['ten']} ({group['ky_hieu']})")
            cols = st.columns(4)
            for i, item in enumerate(group["items"]):
                with cols[i % 4]:
                    render_pronunciation_card(item, "b3_tm")
            st.markdown("<br/>", unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("2. Vận mẫu kép (Finals) - Nhóm mở rộng")
        for group in B2_VAN_MAU_KEP_DATA:
            st.markdown(f"#### {group['nhom']}")
            cols = st.columns(4)
            for i, item in enumerate(group["items"]):
                with cols[i % 4]:
                    render_pronunciation_card(item, "b3_vk_ext")
            st.markdown("<br/>", unsafe_allow_html=True)

        st.subheader("3. Luyện tập đọc âm tiết khó")
        with st.expander("Mẫu 1: j / q / x + vận mẫu kép", expanded=True):
            c1, c2, c3 = st.columns(3)
            with c1:
                st.write("**j-**")
                st.write("jiā, jiě, jiào, jiǔ")
            with c2:
                st.write("**q-**")
                st.write("qiā, qié, qiào, qiú")
            with c3:
                st.write("**x-**")
                st.write("xiā, xiě, xiǎo, xué")

        with st.expander("Mẫu 2: zh / ch / sh + ai/ei/ao/ou", expanded=False):
            c1, c2, c3 = st.columns(3)
            with c1: st.write("**zh-**: zhāi, zhēi, zhāo, zhōu")
            with c2: st.write("**ch-**: chái, chēi, chāo, chōu")
            with c3: st.write("**sh-**: shài, shéi, shāo, shōu")

# --- 5. BÀI 3: NÉT CHỮ HÁN CƠ BẢN (KHÓA) ---
elif menu == "Bài 3 - Nét chữ Hán cơ bản (đang khóa)":
    st.header("🔒 Bài 3: Nét chữ Hán cơ bản")
    if not teacher_unlock:
        st.warning("Nội dung này đang khóa. Bật 'Mở khóa nội dung Bài 2 (GV)' ở sidebar để xem.")
    else:
        st.success("Chế độ giáo viên đã bật.")
        st.markdown(
            """
            <div class="lesson-card">
                <b>Mục tiêu</b><br/>
                <span class="lesson-muted">Rèn nét cơ bản và quy tắc thứ tự nét trước khi viết chữ hoàn chỉnh.</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        net_co_ban = [
            {"Nét": "横", "Pinyin": "héng", "Mô tả": "nét ngang"},
            {"Nét": "竖", "Pinyin": "shù", "Mô tả": "nét sổ"},
            {"Nét": "撇", "Pinyin": "piě", "Mô tả": "nét phẩy"},
            {"Nét": "捺", "Pinyin": "nà", "Mô tả": "nét mác"},
            {"Nét": "点", "Pinyin": "diǎn", "Mô tả": "nét chấm"},
            {"Nét": "提", "Pinyin": "tí", "Mô tả": "nét hất"},
            {"Nét": "折", "Pinyin": "zhé", "Mô tả": "nét gập"},
            {"Nét": "钩", "Pinyin": "gōu", "Mô tả": "nét móc"},
        ]
        st.table(net_co_ban)

        st.subheader("Quy tắc thứ tự nét cần nhớ")
        st.write("- Ngang trước, sổ sau")
        st.write("- Phẩy trước, mác sau")
        st.write("- Trên trước, dưới sau")
        st.write("- Trái trước, phải sau")
        st.write("- Ngoài trước, trong sau, đóng khung cuối")


# Footer
st.sidebar.markdown("---")
st.sidebar.write("加油! (Jiā yóu! - Cố lên!)")
