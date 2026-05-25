# File này chứa toàn bộ dữ liệu giáo án để code chính gọn gàng hơn

THANH_MAU_DICT = {
    'b': 'bờ (môi, không bật hơi)', 'p': 'phờ (môi, bật hơi)', 'm': 'mờ (môi, mũi)',
    'f': 'phờ (răng-môi)', 'd': 'đờ (lưỡi, không bật hơi)', 't': 'thờ (lưỡi, bật hơi)',
    'n': 'nờ (lưỡi, mũi)', 'l': 'lờ (lưỡi, bên)', 'g': 'cờ (họng, không bật hơi)',
    'k': 'khờ (họng, bật hơi)', 'h': 'hờ (họng, xát)'
}

VAN_MAU_DICT = {
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
    {"chu": "n", "hdsd": "Âm đầu lưỡi, âm mũi. Đọc giống 'n'.", "vd_han": "nǐ", "vd_py": "nǐ", "nghe": "你"},
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

XUNG_HO_TU_LAY = [
    {"Chữ Hán": "爸爸", "Pinyin": "bàba", "Nghĩa tiếng Việt": "ba/bố"},
    {"Chữ Hán": "妈妈", "Pinyin": "māma", "Nghĩa tiếng Việt": "mẹ/má"},
    {"Chữ Hán": "哥哥", "Pinyin": "gēge", "Nghĩa tiếng Việt": "anh trai"},
    {"Chữ Hán": "姐姐", "Pinyin": "jiějie", "Nghĩa tiếng Việt": "chị gái"},
    {"Chữ Hán": "弟弟", "Pinyin": "dìdi", "Nghĩa tiếng Việt": "em trai"},
    {"Chữ Hán": "妹妹", "Pinyin": "mèimei", "Nghĩa tiếng Việt": "em gái"},
    {"Chữ Hán": "爷爷", "Pinyin": "yéye", "Nghĩa tiếng Việt": "ông nội"},
    {"Chữ Hán": "奶奶", "Pinyin": "nǎinai", "Nghĩa tiếng Việt": "bà nội"}
]

DAI_TU_XUNG_HO = [
    {"Chữ Hán": "我", "Pinyin": "wǒ", "Nghĩa tiếng Việt": "tôi/mình"},
    {"Chữ Hán": "你", "Pinyin": "nǐ", "Nghĩa tiếng Việt": "bạn/cậu"},
    {"Chữ Hán": "他", "Pinyin": "tā", "Nghĩa tiếng Việt": "anh ấy/ông ấy"},
    {"Chữ Hán": "彼女", "Pinyin": "tā", "Nghĩa tiếng Việt": "cô ấy/chị ấy"},
    {"Chữ Hán": "我们", "Pinyin": "wǒmen", "Nghĩa tiếng Việt": "chúng tôi/chúng ta"},
    {"Chữ Hán": "你们", "Pinyin": "nǐmen", "Nghĩa tiếng Việt": "các bạn"},
    {"Chữ Hán": "他们", "Pinyin": "tāmen", "Nghĩa tiếng Việt": "họ"}
]

TU_VUNG_BO_SUNG = [
    {"Chữ Hán": "老师", "Pinyin": "lǎoshī", "Nghĩa tiếng Việt": "thầy/cô giáo"},
    {"Chữ Hán": "学生", "Pinyin": "xuéshēng", "Nghĩa tiếng Việt": "học sinh"},
    {"Chữ Hán": "很", "Pinyin": "hěn", "Nghĩa tiếng Việt": "rất"},
    {"Chữ Hán": "忙", "Pinyin": "máng", "Nghĩa tiếng Việt": "bận"},
    {"Chữ Hán": "不", "Pinyin": "bù", "Nghĩa tiếng Việt": "không"}
]

B2_VAN_KEP_SLIDES = [
    {"vận": "ai", "hướng_dẫn": "Miệng mở rộng, đọc giống “ai” trong tiếng Việt.", "ví_dụ_hán": "来", "ví_dụ_py": "lái", "nghe": "来"},
    {"vận": "ei", "hướng_dẫn": "Khẩu hình miệng hơi dẹt, đọc gần giống “ây” trong tiếng Việt.", "ví_dụ_hán": "内", "ví_dụ_py": "nèi", "nghe": "内"},
    {"vận": "ao", "hướng_dẫn": "Miệng mở rộng, đọc gần giống “ao” trong tiếng Việt.", "ví_dụ_hán": "宝贝", "ví_dụ_py": "bǎobèi", "nghe": "宝贝"},
    {"vận": "ou", "hướng_dẫn": "Miệng ngậm hơi tròn, đọc gần giống “âu” trong tiếng Việt.", "ví_dụ_hán": "狗", "ví_dụ_py": "gǒu", "nghe": "狗"},
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

B3_LUYEN_TAP_FINALS = ["a", "o", "e", "i", "u", "ü", "ai", "ao", "ou", "ei"]
B3_LUYEN_TAP_ROWS = {
    "z": ["za", "", "ze", "zi", "zu", "", "zai", "zao", "zou", "zei"],
    "c": ["ca", "", "ce", "ci", "cu", "", "cai", "cao", "cou", ""],
    "s": ["sa", "", "se", "si", "su", "", "sai", "sao", "sou", ""],
    "zh": ["zha", "", "zhe", "zhi", "zhu", "", "zhai", "zhao", "zhou", "zhei"],
    "ch": ["cha", "", "che", "chi", "chu", "", "chai", "chao", "chou", ""],
    "sh": ["sha", "", "she", "shi", "shu", "", "shai", "shao", "shou", "shei"],
    "r": ["", "", "re", "ri", "ru", "", "", "rao", "rou", ""],
    "j": ["", "", "", "ji", "", "ju", "", "", "", ""],
    "q": ["", "", "", "qi", "", "qu", "", "", "", ""],
    "x": ["", "", "", "xi", "", "xu", "", "", "", ""],
}

NET_CO_BAN = [
    {"Nét": "横", "Pinyin": "héng", "Mô tả": "nét ngang"},
    {"Nét": "竖", "Pinyin": "shù", "Mô tả": "nét sổ"},
    {"Nét": "撇", "Pinyin": "piě", "Mô tả": "nét phẩy"},
    {"Nét": "捺", "Pinyin": "nà", "Mô tả": "nét mác"},
    {"Nét": "点", "Pinyin": "diǎn", "Mô tả": "nét chấm"},
    {"Nét": "提", "Pinyin": "tí", "Mô tả": "nét hất"},
    {"Nét": "折", "Pinyin": "zhé", "Mô tả": "nét gập"},
    {"Nét": "钩", "Pinyin": "gōu", "Mô tả": "nét móc"},
]

B2_QUIZ_VOCAB = [
    {"q": "lái", "choices": ["đến/lại", "đi", "về"], "answer": "đến/lại"},
    {"q": "nèi", "choices": ["trong/nội", "ngoài", "trên"], "answer": "trong/nội"},
    {"q": "bǎobèi", "choices": ["bảo bối/em bé", "người lớn", "bạn bè"], "answer": "bảo bối/em bé"},
    {"q": "gǒu", "choices": ["con chó", "con mèo", "con lợn"], "answer": "con chó"},
    {"q": "máng", "choices": ["bận", "rất", "không"], "answer": "bận"},
    {"q": "hǎo", "choices": ["tốt/ngon/được", "xấu", "không"], "answer": "tốt/ngon/được"},
    {"q": "mā", "choices": ["mẹ", "bố", "anh"], "answer": "mẹ"},
    {"q": "bà", "choices": ["bố", "mẹ", "em"], "answer": "bố"}
]

B2_QUIZ_LISTENING = [
    {"q": "Bảo bối", "hanzi": "宝贝", "choices": ["bǎobèi", "bǎobēi", "bàobèi"], "answer": "bǎobèi"},
    {"q": "Đến đây", "hanzi": "来", "choices": ["lái", "lāi", "lài"], "answer": "lái"},
    {"q": "Con chó", "hanzi": "狗", "choices": ["gǒu", "kǒu", "hǒu"], "answer": "gǒu"},
    {"q": "Bên trong", "hanzi": "内", "choices": ["nèi", "mèi", "lèi"], "answer": "nèi"},
    {"q": "Chúng tôi", "hanzi": "我们", "choices": ["wǒmen", "wǒmèn", "wǒmēn"], "answer": "wǒmen"},
    {"q": "Bà nội", "hanzi": "奶奶", "choices": ["nǎinai", "nǎinái", "nāinai"], "answer": "nǎinai"}
]

B2_QUIZ_FILL_BLANKS = [
    {"q": "l___", "ans": "ái", "meaning": "đến/lại"},
    {"q": "g___", "ans": "ǒu", "meaning": "con chó"},
    {"q": "bǎob___", "ans": "èi", "meaning": "bảo bối"},
    {"q": "n___", "ans": "èi", "meaning": "bên trong/nội"},
    {"q": "h___", "ans": "ǎo", "meaning": "tốt/ngon"},
    {"q": "m___", "ans": "áng", "meaning": "bận"}
]

B1_QUIZ_VOCAB = [
    {"q": "lǎoshī", "choices": ["thầy/cô giáo", "học sinh", "rất"], "answer": "thầy/cô giáo"},
    {"q": "xuéshēng", "choices": ["không", "học sinh", "bận"], "answer": "học sinh"},
    {"q": "hěn", "choices": ["rất", "không", "bận"], "answer": "rất"},
    {"q": "máng", "choices": ["bận", "mẹ", "bố"], "answer": "bận"},
    {"q": "bù", "choices": ["không", "rất", "bạn"], "answer": "không"},
    {"q": "wǒ", "choices": ["tôi/mình", "bạn/cậu", "anh ấy/cô ấy"], "answer": "tôi/mình"},
    {"q": "nǐ", "choices": ["không", "bạn/cậu", "rất"], "answer": "bạn/cậu"},
    {"q": "mā", "choices": ["mẹ", "bố", "anh"], "answer": "mẹ"},
    {"q": "bà", "choices": ["bố", "mẹ", "em"], "answer": "bố"}
]

B1_QUIZ_FILL_VM = [
    ("m___ma", "ā", "mẹ"), ("n___", "ǐ", "bạn/cậu"), 
    ("l___oshī", "ǎ", "thầy/cô giáo"), ("xu___shēng", "é", "học sinh"), 
    ("h___n", "ě", "rất"), ("m___ng", "á", "bận"), 
    ("b___", "ù", "không"), ("w___", "ǒ", "tôi/mình")
]

B1_QUIZ_PY = [
    {"q": "tôi/mình", "choices": ["wǒ", "nǐ", "tā"], "answer": "wǒ"},
    {"q": "bạn/cậu", "choices": ["nǐ", "wǒ", "tā"], "answer": "nǐ"},
    {"q": "mẹ/má", "choices": ["māma", "bàba", "mèimei"], "answer": "māma"},
    {"q": "thầy/cô giáo", "choices": ["lǎoshī", "xuéshēng", "lǎobǎn"], "answer": "lǎoshī"},
    {"q": "học sinh", "choices": ["xuéshēng", "lǎoshī", "tóngxué"], "answer": "xuéshēng"},
    {"q": "rất", "choices": ["hěn", "tài", "zhēn"], "answer": "hěn"},
    {"q": "bận", "choices": ["máng", "lèi", "è"], "answer": "máng"},
    {"q": "không", "choices": ["bù", "méi", "shì"], "answer": "bù"},
]

B1_QUIZ_TONE = [
    {"q": "妈妈 (māma)", "hanzi": "妈妈", "choices": ["māma", "máng", "mǎma"], "answer": "māma"},
    {"q": "老师 (lǎoshī)", "hanzi": "老师", "choices": ["làoshī", "lǎoshī", "láoshī"], "answer": "lǎoshī"},
    {"q": "学生 (xuéshēng)", "hanzi": "学生", "choices": ["xuěshēng", "xuéshēng", "xuesheng"], "answer": "xuéshēng"},
    {"q": "很 (hěn)", "hanzi": "很", "choices": ["hèn", "hén", "hěn"], "answer": "hěn"},
    {"q": "忙 (máng)", "hanzi": "忙", "choices": ["máng", "mǎng", "màng"], "answer": "máng"},
    {"q": "不 (bù)", "hanzi": "不", "choices": ["bù", "bú", "bǔ"], "answer": "bù"},
]

B1_QUIZ_SENTENCE = [
    {"q": "wǒ hěn máng", "choices": ["tôi rất bận", "tôi không bận", "bạn rất bận"], "answer": "tôi rất bận"},
    {"q": "nǐ bù máng", "choices": ["bạn không bận", "bạn rất bận", "tôi không bận"], "answer": "bạn không bận"},
    {"q": "wǒ shì xuéshēng", "choices": ["tôi là học sinh", "tôi là thầy giáo", "bạn là học sinh"], "answer": "tôi là học sinh"},
    {"q": "tā shì lǎoshī", "choices": ["anh ấy/cô ấy là thầy cô giáo", "anh ấy/cô ấy là học sinh", "tôi là thầy cô giáo"], "answer": "anh ấy/cô ấy là thầy cô giáo"},
]

# --- DỮ LIỆU SO SÁNH TỪ VỰNG CHỈ NỮ GIỚI (BÀI 4) ---
FEMALE_VOCAB_COMPARISON_DATA = [
    {
        "word": "女人",
        "pinyin": "nǚrén",
        "vietnamese": "Phụ nữ / Đàn bà",
        "antonym": "男人 (nánrén - đàn ông)",
        "formality": 2,
        "age": "Trưởng thành (trên 18 tuổi)",
        "context": "Khẩu ngữ & Giao tiếp đời sống",
        "explanation": "Chỉ người nữ đã trưởng thành một cách chung chung. Mang tính khẩu ngữ tự nhiên, đôi khi hơi suồng sã hoặc mang sắc thái tình cảm đời thường.",
        "example_han": "她是一个非常有魅力的女人。",
        "example_py": "Tā shì yí gè fēi cháng yǒu mèilì de nǚrén.",
        "example_vi": "Cô ấy là một người phụ nữ vô cùng quyến rũ.",
        "color": "linear-gradient(135deg, #FFF1F2 0%, #FFE4E6 100%)",
        "border_color": "#F43F5E",
        "text_color": "#9F1239"
    },
    {
        "word": "女孩",
        "pinyin": "nǚhái",
        "vietnamese": "Cô bé / Cô gái trẻ / Con gái",
        "antonym": "男孩 (nánhái - cậu bé)",
        "formality": 2,
        "age": "Trẻ em & Thiếu nữ (dưới 20 tuổi)",
        "context": "Khẩu ngữ & Đời sống thân mật",
        "explanation": "Chỉ các bé gái hoặc cô gái trẻ chưa kết hôn, mang sắc thái đáng yêu, trẻ trung, thân mật và ngọt ngào.",
        "example_han": "那个可爱的小女孩是谁的女儿？",
        "example_py": "Nàge kě'ài de xiǎo nǚhái shì shéi de nǚ'ér?",
        "example_vi": "Cô bé đáng yêu kia là con gái của ai thế?",
        "color": "linear-gradient(135deg, #FDF2F8 0%, #FCE7F3 100%)",
        "border_color": "#EC4899",
        "text_color": "#9D174D"
    },
    {
        "word": "女儿",
        "pinyin": "nǚ'ér",
        "vietnamese": "Con gái (quan hệ gia đình)",
        "antonym": "儿子 (érzi - con trai)",
        "formality": 3,
        "age": "Mọi lứa tuổi (trong mối quan hệ với bố mẹ)",
        "context": "Xưng hô gia đình & Huyết thống",
        "explanation": "Chỉ mối quan hệ huyết thống hoặc nuôi nấng (con gái của ai đó). Tuyệt đối không dùng để chỉ người phụ nữ xa lạ ngoài xã hội.",
        "example_han": "我有两个女儿，她们都听话。",
        "example_py": "Wǒ yǒu liǎng gè nǚ'ér, tāmen dōu tīnghuà.",
        "example_vi": "Tôi có hai đứa con gái, chúng đều rất nghe lời.",
        "color": "linear-gradient(135deg, #F5F3FF 0%, #EDE9FE 100%)",
        "border_color": "#8B5CF6",
        "text_color": "#5B21B6"
    },
    {
        "word": "女生",
        "pinyin": "nǚshēng",
        "vietnamese": "Nữ sinh / Bạn nữ / Cô gái trẻ",
        "antonym": "男生 (nánshēng - bạn nam)",
        "formality": 2,
        "age": "Học sinh, sinh viên & Cô gái trẻ (12 - 30 tuổi)",
        "context": "Trường học, giới trẻ & Khẩu ngữ hiện đại",
        "explanation": "Ban đầu dùng trong học đường (nữ sinh). Ngày nay, giới trẻ dùng rất rộng rãi để gọi các cô gái trẻ một cách lịch sự, thời thượng, dễ thương, tránh cảm giác già dặn của từ '女人' hay '妇女'.",
        "example_han": "我们班的女生都非常聪明。",
        "example_py": "Wǒmen bān de nǚshēng dōu fēi cháng cōngming.",
        "example_vi": "Các bạn nữ trong lớp chúng tôi đều vô cùng thông minh.",
        "color": "linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%)",
        "border_color": "#3B82F6",
        "text_color": "#1E40AF"
    },
    {
        "word": "女性",
        "pinyin": "nǚxìng",
        "vietnamese": "Nữ giới / Phái nữ / Phụ nữ (trang trọng)",
        "antonym": "男性 (nánxìng - nam giới)",
        "formality": 5,
        "age": "Mọi lứa tuổi (chủ yếu là người lớn)",
        "context": "Văn bản, Báo chí, Khoa học, Y tế, Hội thảo",
        "explanation": "Từ mang tính trang trọng, khách quan để chỉ giới tính sinh học hoặc nhóm xã hội của nữ giới. Hay dùng trong tin tức thời sự, nghiên cứu hoặc văn bản luật pháp.",
        "example_han": "现代女性在社会中发挥着重要作用。",
        "example_py": "Xiàndài nǚxìng zài shèhuì zhōng fāhuī zhe zhòngyào zuòyòng.",
        "example_vi": "Phụ nữ hiện đại đóng vai trò quan trọng trong xã hội.",
        "color": "linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%)",
        "border_color": "#64748B",
        "text_color": "#334155"
    },
    {
        "word": "女子",
        "pinyin": "nǚzǐ",
        "vietnamese": "Nữ / Nữ tử / Phụ nữ",
        "antonym": "男子 (nánzǐ - nam / nam tử)",
        "formality": 4,
        "age": "Mọi lứa tuổi",
        "context": "Văn viết, Sự kiện thể thao, Tiêu đề chính thống",
        "explanation": "Mang sắc thái cổ kính hoặc trang trọng. Trong tiếng Trung hiện đại, từ này xuất hiện cực kỳ phổ biến trong các giải đấu thể thao hoặc tên tổ chức chính quy.",
        "example_han": "她获得了女子单打网球比赛的冠军。",
        "example_py": "Tā huòdéle nǚzǐ dāndǎ wǎngqiú bǐsài de guànjūn.",
        "example_vi": "Cô ấy đã giành chức vô địch nội dung đơn nữ quần vợt.",
        "color": "linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%)",
        "border_color": "#10B981",
        "text_color": "#065F46"
    },
    {
        "word": "妇女",
        "pinyin": "fùnǚ",
        "vietnamese": "Phụ nữ (trưởng thành / trung niên / đã kết hôn)",
        "antonym": "Không có từ đối lập trực tiếp (thường đi với nam giới)",
        "formality": 4,
        "age": "Người lớn, phụ nữ đã kết hôn / trung niên (trên 25-30 tuổi)",
        "context": "Chính trị, Pháp luật, Lễ kỷ niệm, Tổ chức xã hội",
        "explanation": "Chỉ phụ nữ trưởng thành nói chung dưới góc độ pháp lý và xã hội. Thường mang hàm ý người phụ nữ đã kết hôn hoặc có gia đình. Tránh dùng gọi các cô gái trẻ tuổi vì dễ tạo cảm giác già dặn.",
        "example_han": "三八国际妇女节是全人类的节日。",
        "example_py": "Sānbā Guójì Fùnǚjié shì quán rénlèi de jiérì.",
        "example_vi": "Ngày Quốc tế Phụ nữ 8/3 là ngày hội của toàn nhân loại.",
        "color": "linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%)",
        "border_color": "#D97706",
        "text_color": "#92400E"
    }
]

# --- DỮ LIỆU TRẮC NGHIỆM PHÂN BIỆT TỪ VỰNG CHỈ NỮ GIỚI (BÀI 4) ---
FEMALE_VOCAB_QUIZ_DATA = [
    {
        "q": "Bạn muốn gửi lời chúc mừng nhân ngày Quốc tế Phụ nữ 8/3 một cách trang trọng trên báo chí hoặc diễn đàn chính thức, từ nào là chuẩn xác nhất?",
        "choices": ["妇女 (fùnǚ)", "女孩 (nǚhái)", "女生 (nǚshēng)"],
        "answer": "妇女 (fùnǚ)",
        "explain": "Tên chính thức của ngày Quốc tế Phụ nữ là '三八妇女节' (Sānbā Fùnǚjié). Từ '妇女' mang sắc thái trang trọng, xã hội và pháp lý, cực kỳ thích hợp cho các ngày lễ và tổ chức chính thống."
    },
    {
        "q": "Bạn đang giao tiếp với một nhóm các bạn nữ trẻ trung năng động trong trường học hoặc đồng nghiệp trẻ tuổi ngoài đời. Để tạo không khí gần gũi, tôn trọng và thời thượng, bạn nên dùng từ nào?",
        "choices": ["妇女 (fùnǚ)", "女生 (nǚshēng)", "女性 (nǚxìng)"],
        "answer": "女生 (nǚshēng)",
        "explain": "Trong ngôn ngữ hiện đại của giới trẻ, '女生' là từ vô cùng phổ biến để chỉ các cô gái/bạn nữ trẻ tuổi, mang cảm giác nhẹ nhàng, trẻ trung và tôn trọng, tránh được sự già dặn của '妇女' hay '女人'."
    },
    {
        "q": "Trong một tờ khai hành chính chính thức bằng tiếng Trung (ví dụ như hồ sơ xin visa hoặc hồ sơ khám bệnh ở bệnh viện), phần giới tính ghi 'Nữ' sẽ dùng từ nào?",
        "choices": ["女儿 (nǚ'ér)", "女孩 (nǚhái)", "女性 (nǚxìng)"],
        "answer": "女性 (nǚxìng)",
        "explain": "Trong khoa học, y tế và thủ tục hành chính, '女性' (Nữ giới) và '男性' (Nam giới) là hai thuật ngữ chuẩn quy nhất để chỉ giới tính sinh học của con người."
    },
    {
        "q": "Người mẹ tự hào giới thiệu đứa con gái ruột của mình với các đồng nghiệp ở cơ quan. Người mẹ bắt buộc phải dùng từ nào sau đây?",
        "choices": ["女儿 (nǚ'ér)", "女孩 (nǚhái)", "女生 (nǚshēng)"],
        "answer": "女儿 (nǚ'ér)",
        "explain": "Để chỉ mối quan hệ gia đình (con gái của bố mẹ), tiếng Trung dùng duy nhất từ '女儿'. Các từ khác chỉ dùng để gọi ngoài xã hội."
    },
    {
        "q": "Trên chương trình thể thao quốc tế Olympic, ở hạng mục thi đấu tranh huy chương 'Bóng đá Nữ' hoặc 'Đơn Nữ quần vợt', ban tổ chức sẽ ghi tiêu đề dùng từ nào?",
        "choices": ["女人 (nǚrén)", "女子 (nǚzǐ)", "女生 (nǚshēng)"],
        "answer": "女子 (nǚzǐ)",
        "explain": "Trong các văn bản viết trang trọng, cổ kính và đặc biệt là các hạng mục thi đấu thể thao chính quy, tiếng Trung luôn dùng từ '女子' (ví dụ: 女子足球 - bóng đá nữ, 女子单打 - đơn nữ)."
    }
]

