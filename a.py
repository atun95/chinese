import streamlit as st
import random
import streamlit.components.v1 as components

# Cấu hình trang
st.set_page_config(page_title="Học Pinyin Tiếng Trung", page_icon="🇨🇳", layout="wide")

# --- DỮ LIỆU ---
thanh_mau = {
    'b': 'bờ (môi, không bật hơi)', 'p': 'phờ (môi, bật hơi)', 'm': 'mờ (môi, mũi)',
    'f': 'phờ (răng-môi)', 'd': 'đờ (lưỡi, không bật hơi)', 't': 'thờ (lưỡi, bật hơi)',
    'n': 'nờ (lưỡi, mũi)', 'l': 'lờ (lưỡi, bên)', 'g': 'cờ (họng, không bật hơi)',
    'k': 'khờ (họng, bật hơi)', 'h': 'hờ (họng, xát)'
}

van_mau = {
    'a': 'a (miệng mở rộng)', 'e': 'ơ (miệng hơi mở)', 'i': 'i (miệng hẹp, ngang)',
    'u': 'u (môi tròn)', 'ü': 'uy (môi tròn, lưỡi cao)'
}

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

if "scores" not in st.session_state:
    st.session_state.scores = {}

# --- GIAO DIỆN CHÍNH ---
st.title("Học Pinyin Cơ Bản")
st.markdown("---")

# Sidebar - Điều hướng bài tập
st.sidebar.header("Danh mục bài tập")
menu = st.sidebar.radio(
    "Chọn bài học:",
    [
        "Kiến thức cần nhớ",
        "Bài 1: Từ vựng xưng hô",
        "Bài 2: Phân biệt âm bật hơi",
        "Bài 3: Điền vận mẫu",
        "Bài 4: Đọc & Viết Pinyin",
        "Bài 5: Luyện thanh điệu",
        "Bài 6: Câu ngắn",
        "Tổng kết điểm"
    ]
)

# --- 1. Kiến thức cần nhớ ---
if menu == "Kiến thức cần nhớ":
    st.header("📚 Kiến thức cần nhớ")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Thanh mẫu (Initials)")
        initials_can_nho = {
            "b": "môi, không bật hơi",
            "p": "môi, bật hơi",
            "m": "môi, âm mũi",
            "f": "răng - môi, âm xát",
            "d": "đầu lưỡi, không bật hơi",
            "t": "đầu lưỡi, bật hơi",
            "n": "đầu lưỡi, âm mũi",
            "l": "đầu lưỡi, âm bên",
            "g": "cuống lưỡi, không bật hơi",
            "k": "cuống lưỡi, bật hơi",
            "h": "cuống lưỡi, âm xát"
        }
        for x, mo_ta in initials_can_nho.items():
            st.info(f"**{x.upper()}**: {mo_ta}")
        
            
    with col2:
        st.subheader("Vận mẫu (Finals)")
        for k, v in van_mau.items():
            st.success(f"**{k}**: {v}")
    
    st.markdown("---")
    st.subheader("4 thanh điệu cơ bản")
    st.write("1️⃣ Thanh 1: **mā** (cao và ngang)")
    st.write("2️⃣ Thanh 2: **má** (đi lên)")
    st.write("3️⃣ Thanh 3: **mǎ** (hạ xuống rồi lên)")
    st.write("4️⃣ Thanh 4: **mà** (đi xuống mạnh)")
    st.write("5️⃣ Thanh nhẹ: **ma** (nhẹ, ngắn, không nhấn)")

    st.subheader("Thanh nhẹ (轻声)")
    st.info("Thanh nhẹ thường xuất hiện ở âm tiết thứ hai trong từ láy hoặc một số từ thông dụng.")
    st.write("Ví dụ từ láy đọc thanh nhẹ ở âm tiết sau:")
    st.write("- **māma** (妈妈): âm tiết **ma** thứ hai là thanh nhẹ")
    st.write("- **bàba** (爸爸): âm tiết **ba** thứ hai là thanh nhẹ")
    st.write("- **gēge** (哥哥): âm tiết **ge** thứ hai là thanh nhẹ")
    st.write("- **jiějie** (姐姐): âm tiết **jie** thứ hai là thanh nhẹ")
    st.write("- **dìdi** (弟弟): âm tiết **di** thứ hai là thanh nhẹ")

    st.subheader("Quy tắc biến điệu thanh 3")
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

# --- 2. BÀI 1: TỪ VỰNG XƯNG HÔ ---
elif menu == "Bài 1: Từ vựng xưng hô":
    st.header("👨‍👩‍👧‍👦 Từ vựng xưng hô")
    st.write("Từ vựng xưng hô và đại từ cơ bản.")
    st.subheader("Từ xưng hô dạng từ láy")
    st.table(xung_ho_tu_lay)
    st.subheader("Đại từ xưng hô cơ bản")
    st.table(dai_tu_xung_ho)
    st.subheader("Từ vựng bổ sung")
    st.table(tu_vung_bo_sung)

    st.markdown("---")
    st.subheader("Mini quiz Bài 1")
    st.write("Chọn nghĩa đúng của từ đã học:")
    bai1_questions = [
        {"q": "lǎoshī", "choices": ["thầy/cô giáo", "học sinh", "rất"], "answer": "thầy/cô giáo"},
        {"q": "xuéshēng", "choices": ["không", "học sinh", "bận"], "answer": "học sinh"},
        {"q": "hěn", "choices": ["rất", "không", "bận"], "answer": "rất"},
        {"q": "máng", "choices": ["bận", "mẹ", "bố"], "answer": "bận"},
        {"q": "bù", "choices": ["không", "rất", "bạn"], "answer": "không"}
    ]
    score = 0
    for idx, item in enumerate(bai1_questions):
        selected = st.radio(
            f"Câu {idx + 1}: {item['q']} nghĩa là gì?",
            item["choices"],
            key=f"bai1_{idx}"
        )
        if selected == item["answer"]:
            score += 1

    if st.button("Chấm điểm Bài 1"):
        total = len(bai1_questions)
        st.session_state.scores["bai1"] = (score, total)
        st.success(f"Bạn đúng {score}/{total} câu.")

# --- 3. BÀI 2: ÂM BẬT HƠI ---
elif menu == "Bài 2: Phân biệt âm bật hơi":
    st.header("🌬️ Âm bật hơi hay không?")
    st.write("Chọn các âm là **ÂM BẬT HƠI**:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        b = st.checkbox("B")
        p = st.checkbox("P")
    with col2:
        d = st.checkbox("D")
        t = st.checkbox("T")
    with col3:
        g = st.checkbox("G")
        k = st.checkbox("K")
        
    if st.button("Kiểm tra kết quả"):
        correct = (p and t and k) and not (b or d or g)
        if correct:
            st.balloons()
            st.success("Tuyệt vời! P, T, K là các âm cần bật hơi mạnh.")
            st.session_state.scores["bai2"] = (1, 1)
        else:
            st.error("Sai rồi! Nhớ nhé: P, T, K là các âm bật hơi.")
            st.session_state.scores["bai2"] = (0, 1)

# --- 4. BÀI 3: ĐIỀN VẬN MẪU ---
elif menu == "Bài 3: Điền vận mẫu":
    st.header("填空 - Điền vào chỗ trống")
    questions = [
        ("m___ma (mẹ)", "ā"),
        ("n___ (bạn)", "ǐ"),
        ("l___oshī (thầy/cô giáo)", "ǎ"),
        ("xu___shēng (học sinh)", "é"),
        ("h___n (rất)", "ě"),
        ("m___ng (bận)", "á"),
        ("b___ (không)", "ù"),
        ("w___ (tôi/mình)", "ǒ")
    ]

    options = ["...", "ā", "á", "ǎ", "à", "ē", "é", "ě", "è", "ǐ", "ǒ", "ù"]
    score = 0
    for idx, (q, ans) in enumerate(questions):
        res = st.selectbox(
            f"Câu {idx + 1}: Chọn vận mẫu đúng cho {q}",
            options,
            key=f"vanmau_{idx}"
        )
        if res == ans:
            score += 1

    if st.button("Chấm điểm điền vận mẫu"):
        total = len(questions)
        st.session_state.scores["bai3"] = (score, total)
        st.success(f"Bạn đúng {score}/{total} câu.")

# --- 5. BÀI 4: ĐỌC & VIẾT ---
elif menu == "Bài 4: Đọc & Viết Pinyin":
    st.header("📖 Luyện đọc và nghĩa")
    tu_vung = {
        "wǒ": "tôi/mình",
        "nǐ": "bạn/cậu",
        "māma": "mẹ/má",
        "lǎoshī": "thầy/cô giáo",
        "xuéshēng": "học sinh",
        "hěn": "rất",
        "máng": "bận",
        "bù": "không"
    }

    score = 0
    for py, nghia in tu_vung.items():
        user_ans = st.text_input(f"Nghĩa của từ '{py}' là gì?", key=f"docviet_{py}")
        if user_ans.strip().lower() == nghia:
            score += 1

    if st.button("Chấm điểm đọc & viết"):
        total = len(tu_vung)
        st.session_state.scores["bai4"] = (score, total)
        st.success(f"Bạn đúng {score}/{total} câu.")

# --- 6. BÀI 5: LUYỆN THANH ĐIỆU ---
elif menu == "Bài 5: Luyện thanh điệu":
    st.header("🎵 Luyện thanh điệu (nghe và chọn đáp án)")
    st.write("Bấm nghe từng từ rồi chọn đáp án đúng. Chỉ dùng từ đã học.")
    st.caption("Nếu chưa nghe được, hãy bấm nút nghe lại và kiểm tra âm lượng trình duyệt.")

    tone_questions = [
        {
            "hanzi": "妈妈",
            "pinyin": "māma",
            "choices": ["māma", "máng", "mǎma"],
            "answer": "māma"
        },
        {
            "hanzi": "老师",
            "pinyin": "lǎoshī",
            "choices": ["làoshī", "lǎoshī", "láoshī"],
            "answer": "lǎoshī"
        },
        {
            "hanzi": "学生",
            "pinyin": "xuéshēng",
            "choices": ["xuěshēng", "xuéshēng", "xuesheng"],
            "answer": "xuéshēng"
        },
        {
            "hanzi": "很",
            "pinyin": "hěn",
            "choices": ["hèn", "hén", "hěn"],
            "answer": "hěn"
        },
        {
            "hanzi": "忙",
            "pinyin": "máng",
            "choices": ["máng", "mǎng", "màng"],
            "answer": "máng"
        },
        {
            "hanzi": "不",
            "pinyin": "bù",
            "choices": ["bù", "bú", "bǔ"],
            "answer": "bù"
        }
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
                height=0
            )
        selected = st.radio(
            "Chọn đáp án:",
            q["choices"],
            key=f"tone_{idx}"
        )
        if selected == q["answer"]:
            score += 1

    if st.button("Chấm điểm thanh điệu"):
        total = len(tone_questions)
        st.session_state.scores["bai5"] = (score, total)
        st.success(f"Bạn đúng {score}/{total} câu.")
        st.info("Nhắc lại: nǐ hǎo là 3 + 3 nên đọc thành ní hǎo.")

# --- 7. BÀI 6: CÂU NGẮN ---
elif menu == "Bài 6: Câu ngắn":
    st.header("🗣️ Luyện câu ngắn")
    st.write("Chọn nghĩa đúng của câu. Chỉ dùng từ đã học.")

    short_sentence_questions = [
        {
            "q": "wǒ hěn máng",
            "choices": ["tôi rất bận", "tôi không bận", "bạn rất bận"],
            "answer": "tôi rất bận"
        },
        {
            "q": "nǐ bù máng",
            "choices": ["bạn không bận", "bạn rất bận", "tôi không bận"],
            "answer": "bạn không bận"
        },
        {
            "q": "wǒ shì xuéshēng",
            "choices": ["tôi là học sinh", "tôi là thầy giáo", "bạn là học sinh"],
            "answer": "tôi là học sinh"
        },
        {
            "q": "tā shì lǎoshī",
            "choices": ["anh ấy/cô ấy là thầy cô giáo", "anh ấy/cô ấy là học sinh", "tôi là thầy cô giáo"],
            "answer": "anh ấy/cô ấy là thầy cô giáo"
        }
    ]

    score = 0
    for idx, item in enumerate(short_sentence_questions):
        selected = st.radio(
            f"Câu {idx + 1}: {item['q']}",
            item["choices"],
            key=f"cau_ngan_{idx}"
        )
        if selected == item["answer"]:
            score += 1

    if st.button("Chấm điểm câu ngắn"):
        total = len(short_sentence_questions)
        st.session_state.scores["bai6"] = (score, total)
        st.success(f"Bạn đúng {score}/{total} câu.")

# --- 8. TỔNG KẾT ĐIỂM ---
elif menu == "Tổng kết điểm":
    st.header("🏁 Chấm điểm Overall")
    st.write("Bạn cần hoàn thành và bấm chấm điểm ở tất cả bài tập trước khi xem tổng điểm.")

    labels = {
        "bai1": "Bài 1: Mini quiz từ vựng",
        "bai2": "Bài 2: Âm bật hơi",
        "bai3": "Bài 3: Điền vận mẫu",
        "bai4": "Bài 4: Đọc & Viết",
        "bai5": "Bài 5: Thanh điệu nghe",
        "bai6": "Bài 6: Câu ngắn"
    }

    missing = [label for key, label in labels.items() if key not in st.session_state.scores]
    if missing:
        st.warning("Bạn chưa hoàn thành đủ các bài sau:")
        for label in missing:
            st.write(f"- {label}")
        st.info("Làm xong từng bài và bấm nút chấm điểm của bài đó, rồi quay lại đây.")
    else:
        earned_total = 0
        max_total = 0
        st.subheader("Kết quả chi tiết")
        for key, label in labels.items():
            earned, total = st.session_state.scores[key]
            earned_total += earned
            max_total += total
            st.write(f"- {label}: {earned}/{total}")

        st.markdown("---")
        percent = round((earned_total / max_total) * 100, 1)
        st.success(f"Điểm overall: {earned_total}/{max_total} ({percent}%)")


# Footer
st.sidebar.markdown("---")
st.sidebar.write("加油! (Jiā yóu! - Cố lên!)")
