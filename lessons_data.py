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
    {"Chữ Hán": "她", "Pinyin": "tā", "Nghĩa tiếng Việt": "cô ấy/chị ấy"},
    {"Chữ Hán": "它", "Pinyin": "tā", "Nghĩa tiếng Việt": "nó"},
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
            {
                "chu": "ia", 
                "hdsd": "Đọc i mở nhanh sang a.", 
                "cach_doc_sau": "Khởi đầu bằng nguyên âm /i/, sau đó nhanh chóng mở rộng miệng sang nguyên âm /a/.",
                "tuong_duong": "Gần giống âm **ia** hoặc **ya** trong tiếng Việt.",
                "luu_y": "Khi đứng một mình (không có thanh mẫu), âm này viết thành <span class='spelling-highlight'>ya</span>.",
                "vd_han": "家", 
                "vd_py": "jiā", 
                "nghe": "家",
                "vietnamese": "Nhà / Gia đình",
                "more_examples": [
                    {"han": "牙", "py": "yá", "vi": "răng"},
                    {"han": "鸭", "py": "yā", "vi": "con vịt"},
                    {"han": "虾", "py": "xiā", "vi": "con tôm"}
                ],
                "color": "linear-gradient(135deg, #FFF1F2 0%, #FFE4E6 100%)",
                "border_color": "#F43F5E",
                "text_color": "#9F1239"
            },
            {
                "chu": "ie", 
                "hdsd": "Đọc i trượt sang e (ê).", 
                "cach_doc_sau": "Phát âm âm /i/ trước, rồi trượt lưỡi hạ xuống để phát âm /ê/ (nguyên âm nửa mở). Hai hàm răng khép hờ.",
                "tuong_duong": "Gần giống âm **iê** hoặc **yê** trong tiếng Việt.",
                "luu_y": "Khi đứng một mình viết thành <span class='spelling-highlight'>ye</span>. Lưu ý nguyên âm ở đây đọc là <span class='spelling-highlight'>ê</span> chứ không đọc là <span class='spelling-highlight'>e</span> hay <span class='spelling-highlight'>ơ</span>.",
                "vd_han": "姐", 
                "vd_py": "jiě", 
                "nghe": "姐",
                "vietnamese": "Chị gái",
                "more_examples": [
                    {"han": "爷", "py": "yé", "vi": "ông nội"},
                    {"han": "写", "py": "xiě", "vi": "viết"},
                    {"han": "鞋", "py": "xié", "vi": "đôi giày"}
                ],
                "color": "linear-gradient(135deg, #FDF2F8 0%, #FCE7F3 100%)",
                "border_color": "#EC4899",
                "text_color": "#9D174D"
            },
            {
                "chu": "iao", 
                "hdsd": "Đọc i -> a -> o liền mạch.", 
                "cach_doc_sau": "Đây là vận mẫu kép ba. Bắt đầu tròn môi ở /i/, trượt thật mượt sang /a/ rộng, rồi thu nhỏ môi lại sang /o/.",
                "tuong_duong": "Gần giống âm **i-ao** hay **yeo** (như từ 'miêu' đọc lướt nhanh).",
                "luu_y": "Khi không có thanh mẫu đứng trước, âm này viết thành <span class='spelling-highlight'>yao</span>.",
                "vd_han": "小", 
                "vd_py": "xiǎo", 
                "nghe": "小",
                "vietnamese": "Nhỏ / Bé",
                "more_examples": [
                    {"han": "药", "py": "yào", "vi": "thuốc"},
                    {"han": "鸟", "py": "niǎo", "vi": "con chim"},
                    {"han": "叫", "py": "jiào", "vi": "gọi/tên là"}
                ],
                "color": "linear-gradient(135deg, #F5F3FF 0%, #EDE9FE 100%)",
                "border_color": "#8B5CF6",
                "text_color": "#5B21B6"
            },
            {
                "chu": "iu", 
                "hdsd": "Đọc i -> u nhanh (thực chất là i + ou).", 
                "cach_doc_sau": "Bắt đầu bằng âm /i/, sau đó chuyển nhanh và thu tròn môi sang âm /ou/ (gần giống âu).",
                "tuong_duong": "Gần giống âm **yêu** hay **iu** trong tiếng Việt.",
                "luu_y": "Đây là dạng viết gọn của <span class='spelling-highlight'>iou</span>. Khi có thanh mẫu viết là <span class='spelling-highlight'>iu</span> (như <span class='spelling-highlight'>liù</span>), khi đứng một mình viết là <span class='spelling-highlight'>you</span>.",
                "vd_han": "六", 
                "vd_py": "liù", 
                "nghe": "六",
                "vietnamese": "Số sáu",
                "more_examples": [
                    {"han": "九", "py": "jiǔ", "vi": "số chín"},
                    {"han": "牛", "py": "niú", "vi": "con bò"},
                    {"han": "秋", "py": "qiū", "vi": "mùa thu"}
                ],
                "color": "linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%)",
                "border_color": "#3B82F6",
                "text_color": "#1E40AF"
            }
        ]
    },
    {
        "nhom": "Nhóm mở rộng từ u/ü",
        "items": [
            {
                "chu": "ua", 
                "hdsd": "Tròn môi u mở sang a.", 
                "cach_doc_sau": "Tròn môi phát âm /u/ làm đệm trước, sau đó mở rộng khẩu hình phát âm nguyên âm /a/ thật nhanh chóng.",
                "tuong_duong": "Đọc gần giống âm **oa** trong tiếng Việt.",
                "luu_y": "Khi đứng một mình không có thanh mẫu, âm này viết thành <span class='spelling-highlight'>wa</span>.",
                "vd_han": "花", 
                "vd_py": "huā", 
                "nghe": "花",
                "vietnamese": "Bông hoa",
                "more_examples": [
                    {"han": "袜", "py": "wà", "vi": "đôi tất/vớ"},
                    {"han": "画", "py": "huà", "vi": "vẽ / bức tranh"},
                    {"han": "挂", "py": "guà", "vi": "treo lên"}
                ],
                "color": "linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%)",
                "border_color": "#10B981",
                "text_color": "#065F46"
            },
            {
                "chu": "uo", 
                "hdsd": "Tròn môi u mở sang o.", 
                "cach_doc_sau": "Tròn môi phát âm /u/ làm đệm trước, rồi chuyển thật nhanh sang âm /o/ (hoặc ô).",
                "tuong_duong": "Đọc gần giống âm **uô** hoặc **ua** trong tiếng Việt.",
                "luu_y": "Khi đứng một mình viết thành <span class='spelling-highlight'>wo</span>. Khi đứng sau các thanh mẫu môi như <span class='spelling-highlight'>b, p, m, f</span>, ta chỉ viết là <span class='spelling-highlight'>o</span> (ví dụ: <span class='spelling-highlight'>bo, po, mo, fo</span>) nhưng vẫn giữ âm đệm nhẹ.",
                "vd_han": "我", 
                "vd_py": "wǒ", 
                "nghe": "我",
                "vietnamese": "Tôi / Tớ",
                "more_examples": [
                    {"han": "火", "py": "huǒ", "vi": "lửa"},
                    {"han": "国", "py": "guó", "vi": "đất nước"},
                    {"han": "多", "py": "duō", "vi": "nhiều"}
                ],
                "color": "linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%)",
                "border_color": "#D97706",
                "text_color": "#92400E"
            },
            {
                "chu": "uai", 
                "hdsd": "Đọc u -> a -> i nhanh.", 
                "cach_doc_sau": "Vận mẫu kép ba. Tròn môi bắt đầu từ /u/ làm đệm, chuyển mượt sang /a/ rộng miệng rồi kết thúc khép môi ở /i/.",
                "tuong_duong": "Đọc gần giống âm **oai** trong tiếng Việt.",
                "luu_y": "Khi đứng độc lập không có thanh mẫu đứng trước, viết thành <span class='spelling-highlight'>wai</span>.",
                "vd_han": "快", 
                "vd_py": "kuài", 
                "nghe": "快",
                "vietnamese": "Nhanh / Nhanh chóng",
                "more_examples": [
                    {"han": "外", "py": "wài", "vi": "bên ngoài"},
                    {"han": "怪", "py": "guài", "vi": "quái vật / kỳ lạ"},
                    {"han": "帅", "py": "shuài", "vi": "đẹp trai"}
                ],
                "color": "linear-gradient(135deg, #F0FDFA 0%, #CCFBF1 100%)",
                "border_color": "#0D9488",
                "text_color": "#0F766E"
            },
            {
                "chu": "ui", 
                "hdsd": "Đọc u -> i nhanh (thực chất là u + ei).", 
                "cach_doc_sau": "Tròn môi phát âm /u/ làm đệm, sau đó lướt nhanh sang âm /ei/ (gần giống ây).",
                "tuong_duong": "Gần giống âm **uây** trong tiếng Việt.",
                "luu_y": "Đây là dạng viết rút gọn của <span class='spelling-highlight'>uei</span>. Khi có thanh mẫu đứng trước viết là <span class='spelling-highlight'>ui</span> (như <span class='spelling-highlight'>shuǐ</span>), đứng một mình viết là <span class='spelling-highlight'>wei</span>.",
                "vd_han": "水", 
                "vd_py": "shuǐ", 
                "nghe": "水",
                "vietnamese": "Nước",
                "more_examples": [
                    {"han": "回", "py": "huí", "vi": "trở về"},
                    {"han": "喂", "py": "wèi", "vi": "alo / cho ăn"},
                    {"han": "贵", "py": "guì", "vi": "đắt / quý"}
                ],
                "color": "linear-gradient(135deg, #F0F9FF 0%, #E0F2FE 100%)",
                "border_color": "#0284C7",
                "text_color": "#0369A1"
            },
            {
                "chu": "üe", 
                "hdsd": "Tròn môi ü mở sang e (ê).", 
                "cach_doc_sau": "Giữ nguyên môi tròn của âm /ü/ (như âm uy), sau đó mở rộng nhanh khẩu hình để chuyển sang /e/ (ê).",
                "tuong_duong": "Đọc gần giống âm **uyê** trong tiếng Việt.",
                "luu_y": "Khi đứng một mình viết là <span class='spelling-highlight'>yue</span>. Khi đi sau <span class='spelling-highlight'>j, q, x</span>, hai dấu chấm trên đầu chữ <span class='spelling-highlight'>ü</span> sẽ biến mất, viết thành <span class='spelling-highlight'>ue</span> (nhưng vẫn đọc là tròn môi <span class='spelling-highlight'>üe</span>).",
                "vd_han": "月", 
                "vd_py": "yuè", 
                "nghe": "月",
                "vietnamese": "Mặt trăng / Tháng",
                "more_examples": [
                    {"han": "雪", "py": "xuě", "vi": "tuyết"},
                    {"han": "学", "py": "xué", "vi": "học"},
                    {"han": "缺", "py": "quē", "vi": "thiếu thốn"}
                ],
                "color": "linear-gradient(135deg, #FAF5FF 0%, #F3E8FF 100%)",
                "border_color": "#A855F7",
                "text_color": "#7E22CE"
            }
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
        "example_han": "她是一个好女人。",
        "example_py": "Tā shì yí gè hǎo nǚrén.",
        "example_vi": "Cô ấy là một người phụ nữ tốt.",
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
        "example_han": "那个女孩可爱。",
        "example_py": "Nàge nǚhái kě'ài.",
        "example_vi": "Cô bé kia thật đáng yêu.",
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
        "example_han": "她是我的女儿。",
        "example_py": "Tā shì wǒ de nǚ'ér.",
        "example_vi": "Cô ấy là con gái của tôi.",
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
        "explanation": "Chỉ nữ học sinh, nữ sinh viên, đây là nghĩa gốc, dùng để chỉ các bạn nữ đang ngồi trên ghế nhà trường hoặc giảng đường đại học.  Trong giao tiếp hàng ngày, từ này được mở rộng để gọi những người con gái trẻ tuổi, các thiếu nữ.",
        "example_han": "那个女生是谁？",
        "example_py": "Nàge nǚshēng shì shéi?",
        "example_vi": "Bạn nữ kia là ai thế?",
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
        "example_han": "这里的女性多。",
        "example_py": "Zhèlǐ de nǚxìng duō.",
        "example_vi": "Nữ giới ở đây rất đông.",
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
        "explanation": "Mang sắc thái cổ kính hoặc trang trọng. Trong tiếng Trung hiện đại, từ này xuất hiện cực kỳ phổ biến trong các giải đấu thể thao, các cuộc thi, trong văn bản hành chính, pháp luật, báo chí,  trong các tổ chức, hội nhóm chính thức, trong phim ảnh, tiểu thuyết cổ trang .",
        "example_han": "那个女子爱花。",
        "example_py": "Nàge nǚzǐ ài huā.",
        "example_vi": "Người phụ nữ kia yêu hoa.",
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
        "example_han": "那个妇女爱孩子。",
        "example_py": "Nàge fùnǚ ài háizi.",
        "example_vi": "Người phụ nữ kia yêu trẻ con.",
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

# --- DỮ LIỆU BÀI TẬP BÀI 3 ---
B3_QUIZ_VOCAB = [
    {"q": "lǜshī", "choices": ["luật sư", "bạn bè", "thầy giáo"], "answer": "luật sư"},
    {"q": "péngyou", "choices": ["bạn, bạn bè", "người yêu", "học sinh"], "answer": "bạn, bạn bè"},
    {"q": "nánpéngyou", "choices": ["bạn trai", "bạn gái", "anh trai"], "answer": "bạn trai"},
    {"q": "nǚpéngyou", "choices": ["bạn gái", "bạn trai", "chị gái"], "answer": "bạn gái"},
    {"q": "míngzi", "choices": ["tên", "chữ Hán", "họ"], "answer": "tên"},
    {"q": "gāoxìng", "choices": ["vui vẻ/mừng", "bận rộn", "mệt mỏi"], "answer": "vui vẻ/mừng"},
    {"q": "rènshi", "choices": ["quen biết", "học tập", "gọi là"], "answer": "quen biết"},
    {"q": "lǎoshī (Ôn tập)", "choices": ["thầy/cô giáo", "học sinh", "luật sư"], "answer": "thầy/cô giáo"},
    {"q": "xuéshēng (Ôn tập)", "choices": ["học sinh", "giáo viên", "bạn bè"], "answer": "học sinh"},
    {"q": "máng (Ôn tập)", "choices": ["bận rộn", "rất", "không"], "answer": "bận rộn"},
]

B3_QUIZ_SPELLING = [
    {"q": "Trong Pinyin, chữ 'i' đứng sau thanh mẫu nào sau đây sẽ phát âm là 'ư'?", "choices": ["sh, zh, s", "j, q, x", "b, p, m"], "answer": "sh, zh, s"},
    {"q": "Khi nguyên âm 'üe' đứng độc lập không có thanh mẫu phía trước, nó sẽ được viết thành dạng nào?", "choices": ["yue", "wue", "yüe"], "answer": "yue"},
    {"q": "Khi vận mẫu tròn môi 'ü' đi sau thanh mẫu 'q', quy tắc chính tả viết chữ là gì?", "choices": ["Bỏ dấu 2 chấm trên đầu (qu)", "Giữ nguyên dấu 2 chấm (qü)", "Đổi ü thành w (qw)"], "answer": "Bỏ dấu 2 chấm trên đầu (qu)"},
    {"q": "Khi vận mẫu tròn môi 'ü' đi sau thanh mẫu 'l', quy tắc chính tả viết chữ là gì?", "choices": ["Bắt buộc giữ nguyên dấu 2 chấm (lü)", "Lược bỏ dấu 2 chấm (lu)", "Viết thêm y ở trước (lyu)"], "answer": "Bắt buộc giữ nguyên dấu 2 chấm (lü)"},
    {"q": "Nguyên âm 'i' trong từ 'nǐ' (nǐ - bạn) phát âm như thế nào?", "choices": ["Đọc là 'i' như tiếng Việt", "Đọc là 'ư' như tiếng Việt", "Đọc là 'u'"], "answer": "Đọc là 'i' như tiếng Việt"},
    {"q": "Khi nguyên âm 'u' đứng một mình không có thanh mẫu, nó viết biến đổi thành gì?", "choices": ["wu", "yu", "w"], "answer": "wu"}
]

B3_QUIZ_FILL_BLANKS = [
    {"q": "l___shī", "ans": "ǜ", "meaning": "luật sư"},
    {"q": "péngy___", "ans": "ou", "meaning": "bạn bè"},
    {"q": "nánp___ngyou", "ans": "é", "meaning": "bạn trai"},
    {"q": "n___péngyou", "ans": "ǚ", "meaning": "bạn gái"},
    {"q": "míngz___", "ans": "i", "meaning": "tên"},
    {"q": "gāox___ng", "ans": "ì", "meaning": "vui vẻ/mừng"},
    {"q": "r___nshi", "ans": "è", "meaning": "quen biết/nhận biết"}
]

B3_QUIZ_LISTENING = [
    {"q": "Số bảy (Thanh mẫu bật hơi q)", "hanzi": "七", "choices": ["qī", "jī", "xī"], "answer": "qī"},
    {"q": "Ăn uống (Thanh mẫu uốn lưỡi ch)", "hanzi": "吃", "choices": ["chī", "cī", "shī"], "answer": "chī"},
    {"q": "Số bốn (Thanh mẫu đầu lưỡi s)", "hanzi": "四", "choices": ["sì", "shì", "zì"], "answer": "sì"},
    {"q": "Thầy giáo / Cô giáo (Thanh mẫu uốn lưỡi sh - Ôn tập)", "hanzi": "老师", "choices": ["lǎoshī", "lǎosī", "làoshī"], "answer": "lǎoshī"},
    {"q": "Con gà (Thanh mẫu mặt lưỡi j)", "hanzi": "鸡", "choices": ["jī", "qī", "xī"], "answer": "jī"},
    {"q": "Biến điệu thanh 3: Rất khỏe (3 + 3 - Ôn tập)", "hanzi": "很好", "choices": ["hěnhǎo", "hěnhāo", "hènhǎo"], "answer": "hěnhǎo"}
]

B3_QUIZ_DIALOGUE = [
    {"q": "Học viên A: Nǐ jiào shénme míngzi? (Bạn tên là gì vậy?) \n Học viên B: ______", "choices": ["Wǒ jiào Ā Qīng. (Tôi tên là A Thanh.)", "Wǒ hěn hǎo. (Tôi rất khỏe.)", "Wǒ shì lǜshī. (Tôi là luật sư.)"], "answer": "Wǒ jiào Ā Qīng. (Tôi tên là A Thanh.)"},
    {"q": "Học viên A: Zhè shì wǒ péngyou, tā jiào Ā Qīng. (Đây là bạn tôi, cậu ấy tên A Thanh.) \n Học viên B: Nǐ hǎo, Ā Qīng! ______", "choices": ["Hěn gāoxìng rènshi nǐ! (Rất vui quen biết bạn!)", "Wǒ bú shì xuéshēng. (Tôi không phải học sinh.)", "Wǒ hěn máng. (Tôi rất bận.)"], "answer": "Hěn gāoxìng rènshi nǐ! (Rất vui quen biết bạn!)"},
    {"q": "Học viên A: Nǐ è ma? Qù chī ma? (Bạn có đói không? Có đi ăn không?) \n Học viên B: Wǒ hěn è. ______", "choices": ["Qù ba, qù chī jī! (Đi thôi, đi ăn thịt gà!)", "Tā méiyǒu nánpéngyou. (Cô ấy không có bạn trai.)", "Wǒ bú shì lǜshī. (Tôi không phải luật sư.)"], "answer": "Qù ba, qù chī jī! (Đi thôi, đi ăn thịt gà!)"},
    {"q": "Học viên A: Nǐmen lèi ma? Qù hē nǎichá ba? (Các bạn mệt không? Đi uống trà sữa nhé?) \n Học viên B: ______", "choices": ["Wǒmen bú lèi. Qù ba! (Chúng tôi không mệt. Đi thôi!)", "Wǒ yǒu nǚpéngyou. (Tôi có bạn gái rồi.)", "Tā hěn hǎo. (Cô ấy rất tốt.)"], "answer": "Wǒmen bú lèi. Qù ba! (Chúng tôi không mệt. Đi thôi!)"}
]

# --- DỮ LIỆU BÀI 5.2: VẬN MẪU MŨI ---
B5_NASAL_FINALS_DATA = [
    {
        "nhom": "Vận mẫu mũi trước (Front Nasal Finals) - Kết thúc bằng âm /n/",
        "items": [
            {
                "chu": "an",
                "hdsd": "Miệng mở rộng rồi thu hẹp lại, đầu lưỡi chạm vào nướu răng trên. Đọc gần giống 'an' trong tiếng Việt.",
                "cach_doc_sau": "Bắt đầu bằng nguyên âm /a/, sau đó nâng đầu lưỡi chạm lên vòm miệng trên (nướu răng) để kết thúc bằng âm /n/. Hơi thoát ra qua mũi.",
                "tuong_duong": "Gần giống âm **an** trong tiếng Việt.",
                "luu_y": "Khi đứng một mình giữ nguyên là <span class='spelling-highlight'>an</span>. Khi kết hợp với các thanh mẫu đầu lưỡi, chú ý kết thúc âm bằng việc đặt đầu lưỡi chạm chân răng trên.",
                "vd_han": "饭",
                "vd_py": "fàn",
                "nghe": "饭",
                "vietnamese": "cơm / ăn cơm",
                "more_examples": [
                    {"han": "山", "py": "shān", "vi": "núi"},
                    {"han": "看", "py": "kàn", "vi": "nhìn / xem"},
                    {"han": "三", "py": "sān", "vi": "số ba"}
                ],
                "color": "linear-gradient(135deg, #FFF1F2 0%, #FFE4E6 100%)",
                "border_color": "#F43F5E",
                "text_color": "#9F1239"
            },
            {
                "chu": "en",
                "hdsd": "Phát âm nguyên âm 'e' (ơ) rồi chuyển nhanh sang phụ âm 'n'. Đọc gần giống 'ân' trong tiếng Việt.",
                "cach_doc_sau": "Khẩu hình hơi mở tự nhiên như âm /ơ/ (e), sau đó nhanh chóng nâng đầu lưỡi lên chạm vòm miệng cứng để khép hơi bằng âm /n/.",
                "tuong_duong": "Gần giống âm **ân** trong tiếng Việt.",
                "luu_y": "Khi đứng một mình giữ nguyên là <span class='spelling-highlight'>en</span> (ví dụ: 恩 ēn - ơn huệ).",
                "vd_han": "很",
                "vd_py": "hěn",
                "nghe": "很",
                "vietnamese": "rất",
                "more_examples": [
                    {"han": "人", "py": "rén", "vi": "người"},
                    {"han": "门", "py": "mén", "vi": "cửa"},
                    {"han": "本", "py": "běn", "vi": "sách / cuốn"}
                ],
                "color": "linear-gradient(135deg, #FDF2F8 0%, #FCE7F3 100%)",
                "border_color": "#EC4899",
                "text_color": "#9D174D"
            },
            {
                "chu": "in",
                "hdsd": "Phát âm âm 'i' rồi nhanh chóng khép lưỡi sang phụ âm 'n'. Đọc gần giống 'in' trong tiếng Việt.",
                "cach_doc_sau": "Bắt đầu với vị trí miệng hẹp của nguyên âm /i/, sau đó di chuyển đầu lưỡi lên trên chạm vòm họng để tạo âm mũi /n/.",
                "tuong_duong": "Gần giống âm **in** trong tiếng Việt.",
                "luu_y": "Khi đứng một mình (không có thanh mẫu), viết thành <span class='spelling-highlight'>yin</span> (ví dụ: 银 yín - bạc, 因 yīn - nguyên nhân).",
                "vd_han": "您",
                "vd_py": "nín",
                "nghe": "您",
                "vietnamese": "Ngài / Ông / Bà (kính trọng)",
                "more_examples": [
                    {"han": "拼音", "py": "pīnyīn", "vi": "Bính âm"},
                    {"han": "林", "py": "lín", "vi": "rừng"},
                    {"han": "琴", "py": "qín", "vi": "đàn cầm"}
                ],
                "color": "linear-gradient(135deg, #F5F3FF 0%, #EDE9FE 100%)",
                "border_color": "#8B5CF6",
                "text_color": "#5B21B6"
            }
        ]
    },
    {
        "nhom": "Vận mẫu mũi sau (Back Nasal Finals) - Kết thúc bằng âm /ng/",
        "items": [
            {
                "chu": "ang",
                "hdsd": "Miệng mở rộng, cuống lưỡi rút về phía sau, hơi thoát ra qua đường mũi. Đọc gần giống 'ang' trong tiếng Việt.",
                "cach_doc_sau": "Mở rộng miệng phát âm /a/, sau đó hạ thấp lưỡi và nâng phần gốc (cuống) lưỡi chạm nhẹ vào ngạc mềm phía sau để tạo âm /ng/.",
                "tuong_duong": "Gần giống âm **ang** trong tiếng Việt.",
                "luu_y": "Khi đứng một mình giữ nguyên là <span class='spelling-highlight'>ang</span> (ví dụ: 昂 áng - ngẩng cao). Chú ý gốc lưỡi phải rút về sau, không chạm vòm họng trước.",
                "vd_han": "忙",
                "vd_py": "máng",
                "nghe": "忙",
                "vietnamese": "bận rộn",
                "more_examples": [
                    {"han": "唱", "py": "chàng", "vi": "hát"},
                    {"han": "胖", "py": "pàng", "vi": "béo"},
                    {"han": "糖", "py": "táng", "vi": "đường / kẹo"}
                ],
                "color": "linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%)",
                "border_color": "#3B82F6",
                "text_color": "#1E40AF"
            },
            {
                "chu": "eng",
                "hdsd": "Phát âm nguyên âm 'e' (ơ) rồi chuyển hơi ra sau mũi tạo âm 'ng'. Đọc gần giống 'âng' trong tiếng Việt.",
                "cach_doc_sau": "Khẩu hình giống như phát âm /e/ (ơ) trong tiếng Trung, sau đó rút cuống lưỡi về sau nâng lên ngạc mềm để kết thúc bằng âm /ng/.",
                "tuong_duong": "Đọc gần giống **âng** trong tiếng Việt.",
                "luu_y": "Khi đứng một mình giữ nguyên là <span class='spelling-highlight'>eng</span>. Sau các phụ âm môi b, p, m, f, vận mẫu này thường được đọc hơi có xu hướng chuyển thành 'ông' hoặc 'âng' tròn môi nhẹ.",
                "vd_han": "朋",
                "vd_py": "péng",
                "nghe": "朋",
                "vietnamese": "bạn bè (trong péngyou)",
                "more_examples": [
                    {"han": "风", "py": "fēng", "vi": "gió"},
                    {"han": "冷", "py": "lěng", "vi": "lạnh"},
                    {"han": "生", "py": "shēng", "vi": "học sinh / sinh"}
                ],
                "color": "linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%)",
                "border_color": "#10B981",
                "text_color": "#065F46"
            },
            {
                "chu": "ing",
                "hdsd": "Phát âm âm 'i' rồi chuyển hơi ra sau mũi tạo âm 'ng'. Đọc gần giống 'inh' trong tiếng Việt.",
                "cach_doc_sau": "Bắt đầu với âm /i/, sau đó hạ lưỡi xuống một chút và kéo gốc lưỡi về phía sau ngạc mềm để tạo âm mũi /ng/.",
                "tuong_duong": "Gần giống âm **inh** trong tiếng Việt.",
                "luu_y": "Khi đứng một mình viết thành <span class='spelling-highlight'>ying</span> (ví dụ: 影 yǐng - phim/ảnh, 迎 yíng - chào đón). Chú ý không đọc thành 'i-âng' mà đọc trơn tru như 'inh'.",
                "vd_han": "听",
                "vd_py": "tīng",
                "nghe": "听",
                "vietnamese": "nghe",
                "more_examples": [
                    {"han": "苹果", "py": "píngguǒ", "vi": "quả táo"},
                    {"han": "明", "py": "míng", "vi": "sáng / rõ"},
                    {"han": "星", "py": "xīng", "vi": "ngôi sao"}
                ],
                "color": "linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%)",
                "border_color": "#D97706",
                "text_color": "#92400E"
            },
            {
                "chu": "ong",
                "hdsd": "Tròn môi phát âm âm 'o' (ô) rồi chuyển hơi ra sau mũi tạo âm 'ng'. Đọc gần giống 'ung' trong tiếng Việt.",
                "cach_doc_sau": "Bắt đầu bằng nguyên âm tròn môi /o/ (ô), sau đó rút lưỡi về phía sau để luồng khí thoát ra qua đường mũi kết thúc bằng phụ âm /ng/.",
                "tuong_duong": "Gần giống âm **ung** trong tiếng Việt.",
                "luu_y": "Không có âm tiết bắt đầu bằng 'ong' đứng độc lập trong tiếng Trung (khi đứng một mình, âm tương đương bắt đầu bằng u sẽ viết thành <span class='spelling-highlight'>weng</span>). Chú ý tránh đọc nhầm thành 'ong' của tiếng Việt.",
                "vd_han": "红",
                "vd_py": "hóng",
                "nghe": "红",
                "vietnamese": "màu đỏ",
                "more_examples": [
                    {"han": "东", "py": "dōng", "vi": "phía đông"},
                    {"han": "龙", "py": "lóng", "vi": "con rồng"},
                    {"han": "公", "py": "gōng", "vi": "công cộng / công"}
                ],
                "color": "linear-gradient(135deg, #F0FDFA 0%, #CCFBF1 100%)",
                "border_color": "#0D9488",
                "text_color": "#0F766E"
            }
        ]
    }
]

# --- DỮ LIỆU BÀI TẬP BÀI 5.2: VẬN MẪU MŨI ---
B5_QUIZ_VOCAB = [
    {"q": "fàn", "choices": ["cơm / ăn cơm", "núi", "rất"], "answer": "cơm / ăn cơm"},
    {"q": "hěn", "choices": ["rất", "bạn bè", "nghe"], "answer": "rất"},
    {"q": "máng", "choices": ["bận rộn", "lạnh", "màu đỏ"], "answer": "bận rộn"},
    {"q": "nín", "choices": ["Ngài / Ông / Bà (kính trọng)", "bố", "mẹ"], "answer": "Ngài / Ông / Bà (kính trọng)"},
    {"q": "péngyou", "choices": ["bạn bè", "học sinh", "thầy giáo"], "answer": "bạn bè"},
    {"q": "tīng", "choices": ["nghe", "nói", "đọc"], "answer": "nghe"},
    {"q": "hóng", "choices": ["màu đỏ", "màu xanh", "phía đông"], "answer": "màu đỏ"}
]

B5_QUIZ_LISTENING = [
    {"q": "Ăn cơm (Vận mẫu an)", "hanzi": "吃饭", "choices": ["chīfàn", "chīfàng", "chīfèn"], "answer": "chīfàn"},
    {"q": "Rất bận (Biến điệu thanh 3 & Vận mẫu mũi sau ang)", "hanzi": "很忙", "choices": ["hěnmáng", "hēnmáng", "hěnmāng"], "answer": "hěnmáng"},
    {"q": "Học sinh (Vận mẫu eng)", "hanzi": "学生", "choices": ["xuéshēng", "xuéshēn", "xuésēn"], "answer": "xuéshēng"},
    {"q": "Chào ông/bà (Kính trọng - Vận mẫu in)", "hanzi": "您好", "choices": ["nínhǎo", "nǐhǎo", "línhǎo"], "answer": "nínhǎo"},
    {"q": "Quả táo (Vận mẫu ing)", "hanzi": "苹果", "choices": ["píngguǒ", "pīngguǒ", "pínggǔ"], "answer": "píngguǒ"},
    {"q": "Phía đông (Vận mẫu ong)", "hanzi": "东", "choices": ["dōng", "dōngg", "dāng"], "answer": "dōng"}
]

B5_QUIZ_FILL_BLANKS = [
    {"q": "f___", "ans": "àn", "meaning": "cơm/ăn cơm"},
    {"q": "h___", "ans": "ěn", "meaning": "rất"},
    {"q": "m___g", "ans": "án", "meaning": "bận"},
    {"q": "p___g", "ans": "én", "meaning": "bạn bè"},
    {"q": "n___", "ans": "ín", "meaning": "ngài/ông/bà"},
    {"q": "t___g", "ans": "īng", "meaning": "nghe"},
    {"q": "h___g", "ans": "óng", "meaning": "màu đỏ"}
]

# --- DỮ LIỆU BÀI 5.3: TỪ CHỈ MỨC ĐỘ ---
B5_3_ADVERBS_DATA = [
    {
        "adv": "很",
        "pinyin": "hěn",
        "level": "Rất (Mức độ thông thường, mang tính liên kết ngữ pháp)",
        "formula": "S + 很 + Adj",
        "example_han": "我很忙",
        "example_py": "Wǒ hěn máng",
        "meaning": "Tôi rất bận",
        "desc": "Trong câu khẳng định với tính từ làm vị ngữ (S + Adj), '很' đóng vai trò liên kết ngữ pháp bắt buộc. Nếu thiếu '很', câu sẽ mang nghĩa so sánh ngầm (ví dụ: 'Tôi bận, người khác rảnh') hoặc nghe không tự nhiên, lửng lơ."
    },
    {
        "adv": "非常",
        "pinyin": "fēicháng",
        "level": "Vô cùng, cực kỳ (Mức độ cao hơn '很')",
        "formula": "S + 非常 + Adj",
        "example_han": "她非常漂亮",
        "example_py": "Tā fēicháng piàoliang",
        "meaning": "Cô ấy vô cùng xinh đẹp",
        "desc": "Dùng để nhấn mạnh mức độ vượt trội của tính từ."
    },
    {
        "adv": "太 ... 了",
        "pinyin": "tài ... le",
        "level": "Quá, lắm (Mức độ cao, biểu thị cảm thán)",
        "formula": "S + 太 + Adj + 了",
        "example_han": "今天太热了",
        "example_py": "Jīntiān tài rè le",
        "meaning": "Hôm nay nóng quá rồi",
        "desc": "Thường dùng trong câu cảm thán. Có thể dùng cho cả nghĩa tích cực (tốt quá) và tiêu cực (nóng quá)."
    },
    {
        "adv": "特别",
        "pinyin": "tèbié",
        "level": "Đặc biệt (Nhấn mạnh sự khác biệt so với bình thường)",
        "formula": "S + 特別 + Adj",
        "example_han": "汉语特别有趣",
        "example_py": "Hànyǔ tèbié yǒuqù",
        "meaning": "Tiếng Trung đặc biệt thú vị",
        "desc": "Diễn tả mức độ nổi bật, có nét riêng biệt."
    },
    {
        "adv": "挺 ... 的",
        "pinyin": "tǐng ... de",
        "level": "Khá là, tương đối (Khẩu ngữ sinh động)",
        "formula": "S + 挺 + Adj + 的",
        "example_han": "他挺好的",
        "example_py": "Tā tǐng hǎo de",
        "meaning": "Anh ấy khá là tốt",
        "desc": "Cấu trúc phổ biến trong văn nói, mang sắc thái nhẹ nhàng, thân thiện."
    },
    {
        "adv": "比较",
        "pinyin": "bǐjiào",
        "level": "Tương đối, khá (Mang tính so sánh ngầm)",
        "formula": "S + 比较 + Adj",
        "example_han": "汉语比较难",
        "example_py": "Hànyǔ bǐjiào nán",
        "meaning": "Tiếng Trung tương đối khó",
        "desc": "Dùng khi so sánh tương đối giữa các đối tượng."
    },
    {
        "adv": "极了",
        "pinyin": "jí le",
        "level": "Cực kỳ (Mức độ cực độ, đứng SAU tính từ)",
        "formula": "S + Adj + 极了",
        "example_han": "累极了",
        "example_py": "Lèi jíle",
        "meaning": "Mệt cực kỳ",
        "desc": "Khác với các phó từ khác, '极了' bắt buộc đứng sau tính từ mà nó bổ nghĩa."
    }
]

B5_3_QUIZ = [
    {
        "q": "Câu nào sau đây diễn đạt đúng ngữ pháp và tự nhiên nhất cho câu 'Tôi bận'?",
        "choices": ["我忙 (Wǒ máng)", "我很忙 (Wǒ hěn máng)", "我不很忙 (Wǒ bù hěn máng)", "我太忙 (Wǒ tài máng)"],
        "answer": "我很忙 (Wǒ hěn máng)"
    },
    {
        "q": "Điền phó từ phù hợp vào chỗ trống để tạo câu cảm thán: '今天___热了！' (Hôm nay nóng quá rồi!)",
        "choices": ["很 (hěn)", "非常 (fēicháng)", "太 (tài)", "比较 (bǐjiào)"],
        "answer": "太 (tài)"
    },
    {
        "q": "Dịch câu 'Tôi mệt cực kỳ!' sang tiếng Trung sử dụng bổ ngữ mức độ '极了' (jíle):",
        "choices": ["我 cực mệt 了", "我 mệt 极lự 了", "我累极了 (Wǒ lèi jíle)", "我极了累 (Wǒ jíle lèi)"],
        "answer": "我累极了 (Wǒ lèi jíle)"
    },
    {
        "q": "Chọn câu phủ định đúng của '他很好' (Anh ấy rất tốt):",
        "choices": ["他狠不好 (Tā hěn bù hǎo)", "他不好 (Tā bù hǎo)", "他很不好 (Tā hěn bù hǎo)", "他太不好 (Tā tài bù hǎo)"],
        "answer": "他不好 (Tā bù hǎo)"
    },
    {
        "q": "Cấu trúc '挺 + Adj + 的' mang nghĩa là gì?",
        "choices": ["Không bận lắm", "Khá là, tương đối", "Quá, lắm", "Vô cùng, cực kỳ"],
        "answer": "Khá là, tương đối"
    }
]

# --- DỮ LIỆU BÀI 6.1: VẬN MẪU MŨI CÒN LẠI (ian, iang, iong, uan, uang, un, ün, üan) ---
B6_1_NASAL_FINALS_DATA = [
    {
        "nhom": "Vận mẫu mũi bắt đầu bằng i (ian, iang, iong)",
        "items": [
            {
                "chu": "ian",
                "hdsd": "Bắt đầu với nguyên âm hẹp dẹt môi /i/, sau đó nhanh chóng chuyển sang phát âm dẹt môi của âm /e/ (như ê) và kết thúc bằng cách đưa đầu lưỡi chạm nướu răng trên.",
                "cach_doc_sau": "Khẩu hình ban đầu dẹt môi phát âm /i/ làm đệm, sau đó mở nhẹ miệng sang hai bên và nâng đầu lưỡi chạm vào ngạc cứng phía trên để kết hơi ở phụ âm mũi /n/.",
                "luu_y": "Dù viết là 'ian' nhưng phần 'an' ở đây biến âm thành /en/ (đọc dẹt môi). Khi đứng độc lập viết thành <span class='spelling-highlight'>yan</span> (ví dụ: 言 yán - ngôn ngữ).",
                "vd_han": "钱",
                "vd_py": "qián",
                "nghe": "钱",
                "vietnamese": "tiền",
                "more_examples": [
                    {"han": "烟", "py": "yān", "vi": "khói"},
                    {"han": "天", "py": "tiān", "vi": "trời / ngày"},
                    {"han": "面", "py": "miàn", "vi": "mặt / mì"}
                ],
                "color": "linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%)",
                "border_color": "#3B82F6",
                "text_color": "#1E3A8A"
            },
            {
                "chu": "iang",
                "hdsd": "Bắt đầu phát âm dẹt môi /i/, sau đó mở rộng miệng phát âm nguyên âm /a/ và kết hơi bằng cách rút cuống lưỡi về sau ngạc mềm.",
                "cach_doc_sau": "Phát âm âm đệm dẹt môi /i/, ngay sau đó mở rộng miệng đẩy luồng hơi ra sau để phát âm nguyên âm /a/ mở rộng miệng, đồng thời nâng gốc lưỡi chạm nhẹ ngạc mềm để tạo âm mũi sau /ng/.",
                "luu_y": "Khi đứng độc lập (không đi kèm thanh mẫu), viết biến đổi thành <span class='spelling-highlight'>yang</span> (ví dụ: 羊 yáng - con dê).",
                "vd_han": "想",
                "vd_py": "xiǎng",
                "nghe": "想",
                "vietnamese": "nhớ / muốn / nghĩ",
                "more_examples": [
                    {"han": "羊", "py": "yáng", "vi": "con dê"},
                    {"han": "强", "py": "qiáng", "vi": "mạnh mẽ"},
                    {"han": "香", "py": "xiāng", "vi": "thơm"}
                ],
                "color": "linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%)",
                "border_color": "#22C55E",
                "text_color": "#14532D"
            },
            {
                "chu": "iong",
                "hdsd": "Phát âm nguyên âm dẹt môi /i/ cực nhanh làm đệm, sau đó nhanh chóng khum tròn môi phát âm /o/ (ô) và hạ thấp cuống lưỡi kết âm mũi sau.",
                "cach_doc_sau": "Bắt đầu bằng vị trí dẹt của âm /i/, sau đó chuyển nhanh khẩu hình sang khum tròn nhô ra của âm /o/ (ô) đồng thời rút gốc lưỡi nâng lên ngạc mềm để tạo âm mũi sau /ng/.",
                "luu_y": "Không đứng độc lập. Khi đứng một mình viết thành <span class='spelling-highlight'>yong</span> (ví dụ: 用 yòng - sử dụng).",
                "vd_han": "熊",
                "vd_py": "xióng",
                "nghe": "熊",
                "vietnamese": "con gấu",
                "more_examples": [
                    {"han": "兄", "py": "xiōng", "vi": "anh trai"},
                    {"han": "穷", "py": "qióng", "vi": "nghèo"},
                    {"han": "用", "py": "yòng", "vi": "sử dụng"}
                ],
                "color": "linear-gradient(135deg, #F5F3FF 0%, #EDE9FE 100%)",
                "border_color": "#8B5CF6",
                "text_color": "#4C1D95"
            }
        ]
    },
    {
        "nhom": "Vận mẫu mũi bắt đầu bằng u (uan, uang, un)",
        "items": [
            {
                "chu": "uan",
                "hdsd": "Khum tròn môi phát âm nguyên âm đệm /u/, sau đó mở rộng miệng chuyển sang phát âm /a/, khép miệng dần và đưa đầu lưỡi chạm chân răng trên.",
                "cach_doc_sau": "Bắt đầu bằng khẩu hình tròn môi nhô ra của âm /u/, tiếp nối mượt mà mở rộng hàm để phát âm nguyên âm /a/, sau đó đưa lưỡi lên chạm nướu răng cửa trên chặn hơi tạo âm mũi trước /n/.",
                "luu_y": "Khi đứng độc lập viết thành <span class='spelling-highlight'>wan</span> (ví dụ: 万 wàn - mười nghìn). Hãy phân biệt với uan tròn môi üan sau j, q, x.",
                "vd_han": "玩",
                "vd_py": "wán",
                "nghe": "玩",
                "vietnamese": "chơi",
                "more_examples": [
                    {"han": "晚", "py": "wǎn", "vi": "muộn / tối"},
                    {"han": "酸", "py": "suān", "vi": "chua"},
                    {"han": "关", "py": "guān", "vi": "đóng"}
                ],
                "color": "linear-gradient(135deg, #FFF1F2 0%, #FFE4E6 100%)",
                "border_color": "#F43F5E",
                "text_color": "#881337"
            },
            {
                "chu": "uang",
                "hdsd": "Tròn môi phát âm /u/ làm đệm, tiếp tục mở rộng miệng sang phát âm nguyên âm /a/, rồi rút gốc lưỡi chạm nhẹ ngạc mềm để tạo âm mũi sau.",
                "cach_doc_sau": "Khởi đầu bằng môi tròn nhô ra của âm /u/, chuyển tiếp nhanh mở rộng vòm miệng phát âm /a/, kết hơi bằng cách kéo gốc lưỡi lùi về sau ngạc mềm tạo âm mũi sau /ng/.",
                "luu_y": "Khi đứng độc lập viết thành <span class='spelling-highlight'>wang</span> (ví dụ: 王 wáng - vua/họ Vương).",
                "vd_han": "黄",
                "vd_py": "huáng",
                "nghe": "黄",
                "vietnamese": "màu vàng",
                "more_examples": [
                    {"han": "王", "py": "wáng", "vi": "vua / họ Vương"},
                    {"han": "光", "py": "guāng", "vi": "ánh sáng"},
                    {"han": "双", "py": "shuāng", "vi": "đôi / cặp"}
                ],
                "color": "linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%)",
                "border_color": "#10B981",
                "text_color": "#065F46"
            },
            {
                "chu": "un",
                "hdsd": "Môi tròn ở âm đệm /u/, sau đó chuyển khẩu hình sang phát âm dẹt môi nhẹ của âm /e/ (giữa ơ và ư), khép hơi bằng đầu lưỡi chạm chân răng trên.",
                "cach_doc_sau": "Khởi đầu bằng khẩu hình tròn môi của âm /u/, sau đó chuyển tiếp mượt mà hạ lưỡi phát âm /e/ nhẹ rồi kết thúc bằng việc đặt đầu lưỡi chạm ngạc cứng chặn luồng khí.",
                "luu_y": "Đây là dạng viết giản lược của <span class='spelling-highlight'>uen</span>. Khi đi kèm thanh mẫu viết là <span class='spelling-highlight'>un</span> (ví dụ: chūn, lùn), khi đứng một mình viết đầy đủ là <span class='spelling-highlight'>wen</span> (ví dụ: 问 wèn - hỏi).",
                "vd_han": "春",
                "vd_py": "chūn",
                "nghe": "春",
                "vietnamese": "mùa xuân",
                "more_examples": [
                    {"han": "问", "py": "wèn", "vi": "hỏi"},
                    {"han": "滚", "py": "gǔn", "vi": "lăn / cút"},
                    {"han": "婚", "py": "hūn", "vi": "kết hôn"}
                ],
                "color": "linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%)",
                "border_color": "#D97706",
                "text_color": "#92400E"
            }
        ]
    },
    {
        "nhom": "Vận mẫu mũi bắt đầu bằng ü (ün, üan)",
        "items": [
            {
                "chu": "ün",
                "hdsd": "Giữ môi khum tròn hẹp phát âm /ü/, sau đó hạ đầu lưỡi nhẹ rồi khép âm bằng đầu lưỡi chạm nướu răng trên.",
                "cach_doc_sau": "Duy trì vị trí môi tròn nhô ra của âm /ü/ làm đệm, sau đó trượt nhanh lưỡi về vị trí âm mũi trước /n/ mà không làm bẹt môi.",
                "luu_y": "Khi đứng một mình viết thành <span class='spelling-highlight'>yun</span> (ví dụ: 云 yún - đám mây). Khi đi sau j, q, x, hai dấu chấm trên chữ ü bị lược bỏ, viết thành <span class='spelling-highlight'>un</span> (ví dụ: jun, qun, xun) nhưng vẫn phát âm tròn môi là 'uyn'!",
                "vd_han": "裙",
                "vd_py": "qún",
                "nghe": "裙",
                "vietnamese": "cái váy",
                "more_examples": [
                    {"han": "云", "py": "yún", "vi": "mây / đám mây"},
                    {"han": "军", "py": "jūn", "vi": "quân đội"},
                    {"han": "寻", "py": "xún", "vi": "tìm kiếm"}
                ],
                "color": "linear-gradient(135deg, #F0FDFA 0%, #CCFBF1 100%)",
                "border_color": "#0D9488",
                "text_color": "#0F766E"
            },
            {
                "chu": "üan",
                "hdsd": "Môi khum tròn phát âm /ü/ làm đệm, chuyển nhanh sang mở khẩu hình dẹt và chạm đầu lưỡi lên răng trên.",
                "cach_doc_sau": "Giữ môi tròn nhô ra phát âm /ü/, sau đó nhanh chóng mở rộng miệng sang hai bên phát âm âm /an/ kết thúc bằng đầu lưỡi chạm nướu răng trên.",
                "luu_y": "Khi đứng một mình viết thành <span class='spelling-highlight'>yuan</span> (ví dụ: 元 yuán - đồng Nhân dân tệ). Khi đi sau j, q, x, hai dấu chấm trên đầu chữ ü bị lược bỏ, viết thành <span class='spelling-highlight'>uan</span> (ví dụ: juan, quan, xuan) nhưng vẫn phát âm tròn môi là 'uyên'!",
                "vd_han": "选",
                "vd_py": "xuǎn",
                "nghe": "选",
                "vietnamese": "chọn lựa",
                "more_examples": [
                    {"han": "元", "py": "yuán", "vi": "đồng tệ / nguyên"},
                    {"han": "远", "py": "yuǎn", "vi": "xa xôi"},
                    {"han": "穿 (Lưu ý: đây là uan thường)", "py": "chuān", "vi": "mặc (để phân biệt)"}
                ],
                "color": "linear-gradient(135deg, #FAF5FF 0%, #F3E8FF 100%)",
                "border_color": "#A855F7",
                "text_color": "#7E22CE"
            }
        ]
    }
]

# --- DỮ LIỆU BÀI TẬP BÀI 6.1 ---
B6_1_QUIZ_DATA = [
    {
        "q": "Vận mẫu 'ian' trong chữ '钱' (qián - tiền) được phát âm như thế nào là chính xác nhất?",
        "choices": [
            "Phát âm mở miệng rộng thành âm 'a' ở cuối.",
            "Phát âm dẹt môi thành âm 'ê' (/ɛ/) ở giữa và kết thúc bằng đầu lưỡi chạm răng trên.",
            "Phát âm tròn môi với âm đệm 'u' ở đầu."
        ],
        "answer": "Phát âm dẹt môi thành âm 'ê' (/ɛ/) ở giữa và kết thúc bằng đầu lưỡi chạm răng trên.",
        "explain": "Quy tắc ngữ âm: vận mẫu 'ian' tuy viết là 'a' nhưng bắt buộc đọc biến đổi thành nguyên âm nửa mở dẹt môi /ɛ/ trước khi khép âm bằng đầu lưỡi chạm răng trên."
    },
    {
        "q": "Khi các vận mẫu 'ün' và 'üan' kết hợp với các thanh mẫu mặt lưỡi 'j, q, x', quy tắc chính tả viết chữ là gì?",
        "choices": [
            "Giữ nguyên hai dấu chấm trên đầu chữ ü (viết qün, jüan)",
            "Bỏ hai dấu chấm trên đầu chữ ü (viết qun, juan) nhưng miệng phát âm vẫn tròn môi (/yn/, /yɛn/)",
            "Đổi ü thành w (viết qwn, jwan)"
        ],
        "answer": "Bỏ hai dấu chấm trên đầu chữ ü (viết qun, juan) nhưng miệng phát âm vẫn tròn môi (/yn/, /yɛn/)",
        "explain": "Quy tắc chính tả cực kỳ quan trọng: Khi ü đi với j, q, x, dấu hai chấm bị lược bỏ để chữ gọn gàng hơn, tuy nhiên bản chất âm vẫn là tròn môi ü."
    },
    {
        "q": "Từ 'mùa xuân' trong tiếng Trung viết là '春' (chūn). Vận mẫu 'un' ở đây thực chất là dạng viết gọn của vận mẫu nào?",
        "choices": [
            "Vận mẫu 'uen'",
            "Vận mẫu 'uan'",
            "Vận mẫu 'uon'"
        ],
        "answer": "Vận mẫu 'uen'",
        "explain": "Vận mẫu 'un' thực chất là dạng viết giản lược của 'uen'. Khi đứng độc lập không đi với thanh mẫu, nó sẽ được viết đầy đủ là 'wen'."
    },
    {
        "q": "Khi đứng độc lập một mình (không đi kèm thanh mẫu), các vận mẫu 'ian', 'uan' và 'üan' sẽ được viết biến đổi thành gì?",
        "choices": [
            "Giữ nguyên cách viết cũ (ian, uan, üan)",
            "Biến đổi thành: yan, wan, yuan",
            "Biến đổi thành: ian, wan, yian"
        ],
        "answer": "Biến đổi thành: yan, wan, yuan",
        "explain": "Quy tắc chính tả: Bán nguyên âm /i/ đứng đầu biến thành y (ian -> yan, üan -> yuan), bán nguyên âm /u/ đứng đầu biến thành w (uan -> wan)."
    },
    {
        "q": "Nghe âm phát và chọn Bính âm chính xác của từ 'cái váy' trong chữ Hán '裙':",
        "hanzi": "裙",
        "choices": ["qún", "qúng", "chún"],
        "answer": "qún",
        "explain": "Chữ '裙' (cái váy) có thanh mẫu 'q', vận mẫu 'ün' (đã lược bỏ dấu 2 chấm khi viết) và thanh 2, đọc là qún."
    },
    {
        "q": "Nghe âm phát và chọn Bính âm chính xác của từ 'nghĩ/muốn/nhớ' trong chữ Hán '想':",
        "hanzi": "想",
        "choices": ["xiǎng", "xiǎn", "qiǎng"],
        "answer": "xiǎng",
        "explain": "Chữ '想' có thanh mẫu 'x', vận mẫu mũi sau 'iang', thanh 3, đọc là xiǎng."
    }
]






# --- DỮ LIỆU BÀI 6.2: QUY TẮC BIẾN ĐỔI VẬN MẪU KHI ĐỨNG ĐỘC LẬP ---
B6_2_STANDALONE_FINALS_DATA = [
    {
        "nhom": "Nhóm 1: Các vận mẫu bắt đầu bằng 'i' (ia, iao, ian, iang, ie, iong, iou, in, ing, i)",
        "mota": "Khi đứng độc lập (không đi kèm thanh mẫu):\n- Vận mẫu đơn <b>i</b> thêm <b>y</b> phía trước (thành <b>yi</b>).\n- Vận mẫu <b>in, ing</b> thêm <b>y</b> phía trước (thành <b>yin, ying</b>).\n- Các vận mẫu khác bắt đầu bằng <b>i</b> (ia, iao, ian, iang, ie, iong, iou) sẽ <b>đổi i thành y</b> (thành ya, yao, yan, yang, ye, yong, you).",
        "items": [
            {"goc": "i", "bien": "yi", "vd_han": "一", "vd_py": "yī", "meaning": "số một"},
            {"goc": "ia", "bien": "ya", "vd_han": "鸭", "vd_py": "yā", "meaning": "con vịt"},
            {"goc": "iao", "bien": "yao", "vd_han": "药", "vd_py": "yào", "meaning": "thuốc"},
            {"goc": "ian", "bien": "yan", "vd_han": "言", "vd_py": "yán", "meaning": "ngôn ngữ / lời nói"},
            {"goc": "iang", "bien": "yang", "vd_han": "羊", "vd_py": "yáng", "meaning": "con dê"},
            {"goc": "ie", "bien": "ye", "vd_han": "爷", "vd_py": "yé", "meaning": "ông nội"},
            {"goc": "iou", "bien": "you", "vd_han": "有", "vd_py": "yǒu", "meaning": "có"},
            {"goc": "iong", "bien": "yong", "vd_han": "用", "vd_py": "yòng", "meaning": "sử dụng / dùng"},
            {"goc": "in", "bien": "yin", "vd_han": "音", "vd_py": "yīn", "meaning": "âm thanh"},
            {"goc": "ing", "bien": "ying", "vd_han": "影", "vd_py": "yǐng", "meaning": "ảnh / bóng"}
        ]
    },
    {
        "nhom": "Nhóm 2: Các vận mẫu bắt đầu bằng 'u' (ua, uai, uan, uang, uo, uei, uen, ueng, u)",
        "mota": "Khi đứng độc lập (không đi kèm thanh mẫu):\n- Vận mẫu đơn <b>u</b> thêm <b>w</b> phía trước (thành <b>wu</b>).\n- Các vận mẫu khác bắt đầu bằng <b>u</b> (ua, uai, uan, uang, uo, uei, uen, ueng) sẽ <b>đổi u thành w</b> (thành wa, wai, wan, wang, wo, wei, wen, weng).",
        "items": [
            {"goc": "u", "bien": "wu", "vd_han": "五", "vd_py": "wǔ", "meaning": "số năm"},
            {"goc": "ua", "bien": "wa", "vd_han": "娃", "vd_py": "wá", "meaning": "em bé / búp bê"},
            {"goc": "uai", "bien": "wai", "vd_han": "外", "vd_py": "wài", "meaning": "bên ngoài"},
            {"goc": "uan", "bien": "wan", "vd_han": "玩", "vd_py": "wán", "meaning": "chơi / đùa"},
            {"goc": "uang", "bien": "wang", "vd_han": "王", "vd_py": "wáng", "meaning": "vua / họ Vương"},
            {"goc": "uo", "bien": "wo", "vd_han": "我", "vd_py": "wǒ", "meaning": "tôi / ta"},
            {"goc": "uei", "bien": "wei", "vd_han": "喂", "vd_py": "wèi", "meaning": "alo (khi nghe điện thoại)"},
            {"goc": "uen", "bien": "wen", "vd_han": "问", "vd_py": "wèn", "meaning": "hỏi"},
            {"goc": "ueng", "bien": "weng", "vd_han": "翁", "vd_py": "wēng", "meaning": "ông già"}
        ]
    },
    {
        "nhom": "Nhóm 3: Các vận mẫu bắt đầu bằng 'ü' (ü, üe, üan, ün)",
        "mota": "Khi đứng độc lập (không đi kèm thanh mẫu):\n- Tất cả các vận mẫu bắt đầu bằng <b>ü</b> (ü, üe, üan, ün) đều <b>thêm y ở phía trước và bỏ hai dấu chấm trên đầu chữ ü</b> (viết thành yu, yue, yuan, yun).",
        "items": [
            {"goc": "ü", "bien": "yu", "vd_han": "鱼", "vd_py": "yú", "meaning": "con cá", "highlight": True, "note_doc": "⚠️ <b>Điểm bẫy phát âm:</b> Mặt chữ ghi là 'yu' (giống u) nhưng bắt buộc phát âm tròn môi /ü/, tuyệt đối không đọc thành 'u' thường!"},
            {"goc": "üe", "bien": "yue", "vd_han": "月", "vd_py": "yuè", "meaning": "mặt trăng / tháng", "highlight": True, "note_doc": "⚠️ <b>Điểm bẫy phát âm:</b> Mặt chữ ghi 'yue' nhưng bắt buộc phát âm tròn môi /ü/ trượt sang /e/ (như uyê), không đọc bẹt môi giống 'de' hay 'u-e'!"},
            {"goc": "üan", "bien": "yuan", "vd_han": "元", "vd_py": "yuán", "meaning": "đồng Nhân dân tệ", "highlight": True, "note_doc": "⚠️ <b>Điểm bẫy phát âm:</b> Mặt chữ ghi 'yuan' nhưng bắt buộc phát âm tròn môi /ü/ làm đệm rồi sang /an/ (như uyên), tránh đọc nhầm thành 'oan' của 'wan'!"},
            {"goc": "ün", "bien": "yun", "vd_han": "云", "vd_py": "yún", "meaning": "mây / đám mây", "highlight": True, "note_doc": "⚠️ <b>Điểm bẫy phát âm:</b> Mặt chữ ghi 'yun' nhưng bắt buộc phát âm tròn môi /ü/ rồi kết hơi ở ngạc trên (như uyn), tránh đọc nhầm thành 'un' (uân) của 'wen'!"}
        ]
    }
]

# --- DỮ LIỆU BÀI TẬP BÀI 6.2 ---
B6_2_QUIZ_DATA = [
    {
        "q": "Khi vận mẫu đơn 'ü' đứng một mình không có thanh mẫu đi kèm, cách viết đúng chính tả là gì?",
        "choices": ["ü", "yü", "yu", "wu"],
        "answer": "yu",
        "explain": "Quy tắc chính tả: Vận mẫu bắt đầu bằng ü khi đứng độc lập sẽ thêm y phía trước và lược bỏ hai dấu chấm trên đầu, viết thành yu."
    },
    {
        "q": "Bính âm 'wèn' (hỏi) có vận mẫu gốc là gì?",
        "choices": ["un (uen)", "uan", "u", "uo"],
        "answer": "un (uen)",
        "explain": "Từ '问' (wèn) có vận mẫu gốc là uen (viết tắt là un). Khi đứng độc lập, u đổi thành w tạo thành wen."
    },
    {
        "q": "Từ 'con cá' trong tiếng Trung phát âm là 'yú'. Vận mẫu gốc của từ này là gì?",
        "choices": ["u", "ü", "iu", "yu"],
        "answer": "ü",
        "explain": "Chữ Hán '鱼' (yú - con cá) có vận mẫu gốc là ü. Do đứng một mình nên thêm y ở trước và bỏ hai dấu chấm thành yu."
    },
    {
        "q": "Chọn cách viết đúng chính tả Pinyin của vận mẫu 'iang' khi đứng một mình:",
        "choices": ["iang", "yiang", "yang", "wiang"],
        "answer": "yang",
        "explain": "Vận mẫu 'iang' bắt đầu bằng i, khi đứng độc lập sẽ đổi i thành y, viết thành yang."
    },
    {
        "q": "Từ 'tôi' trong tiếng Trung viết là '我' (wǒ). Vận mẫu gốc của nó là gì?",
        "choices": ["o", "uo", "u", "ou"],
        "answer": "uo",
        "explain": "Từ '我' (wǒ) có vận mẫu gốc là uo. Khi đứng một mình, u đổi thành w tạo thành wo."
    }
]
