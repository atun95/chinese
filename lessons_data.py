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
            {"chu": "sh", "hdsd": "Uốn lưỡi, để khe hở nhỏ cho hơi thoát ra.", "vd_han": "shì", "vd_py": "shì", "nghe": "shì"},
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
