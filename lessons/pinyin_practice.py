# -*- coding: utf-8 -*-
"""
Studio Ghép Vần & Tự Luyện Phát Âm Pinyin Tương Tác
Cho phép học viên tự chọn Thanh mẫu + Vận mẫu + Thanh điệu:
- Kiểm tra tính hợp lệ trong tiếng Trung (phiên âm nào không có sẽ báo rõ).
- Quy tắc chính tả (j/q/x + ü -> u, i/u/ü đứng độc lập...).
- Nút bấm phát âm chuẩn tiếng Trung qua TTS.
- Hiển thị cả 4 thanh điệu và chữ Hán ví dụ.
"""
import streamlit as st
import streamlit.components.v1 as components
import json
import sys
from pathlib import Path

# Thêm thư mục gốc vào sys.path để luôn tìm thấy ui_utils
_ROOT_DIR = str(Path(__file__).resolve().parent.parent)
if _ROOT_DIR not in sys.path:
    sys.path.insert(0, _ROOT_DIR)

try:
    from ui_utils import inject_tts_to_parent, _TTS_JS_CORE
except (ImportError, AttributeError):
    try:
        import ui_utils
        import importlib
        importlib.reload(ui_utils)
        from ui_utils import inject_tts_to_parent, _TTS_JS_CORE
    except Exception:
        _TTS_JS_CORE = """
<script>
(function(){
  window.chineseTTS = function(txt) {
    if (!txt) return;
    window.parent.postMessage({type:'CHINESE_TTS', text: String(txt).trim()}, '*');
  };
})();
</script>
"""
        def inject_tts_to_parent():
            pass

# ─────────────────────────────────────────────────────────────────────────────
# 1. HỆ THỐNG DỮ LIỆU THANH MẪU & VẬN MẪU
# ─────────────────────────────────────────────────────────────────────────────


ALL_INITIALS = [
    "(Không có)",
    "b", "p", "m", "f",
    "d", "t", "n", "l",
    "g", "k", "h",
    "j", "q", "x",
    "zh", "ch", "sh", "r",
    "z", "c", "s",
]

ALL_FINALS = [
    # Đơn
    "a", "o", "e", "i", "u", "ü", "er",
    # Kép
    "ai", "ei", "ao", "ou", "ia", "ie", "iao", "iu", "ua", "uo", "uai", "ui", "üe",
    # Mũi trước
    "an", "en", "in", "un", "ün", "ian", "uan", "üan",
    # Mũi sau
    "ang", "eng", "ing", "ong", "iang", "iong", "uang", "ueng",
]

TONES_DATA = [
    {"val": 1, "name": "Thanh 1 (Âm bình)", "mark": "ˉ", "desc": "Cao, phẳng và ngân đều (55)"},
    {"val": 2, "name": "Thanh 2 (Dương bình)", "mark": "ˊ", "desc": "Lên giọng như dấu sắc (35)"},
    {"val": 3, "name": "Thanh 3 (Thượng thanh)", "mark": "ˇ", "desc": "Xuống thấp rồi lên nhẹ (214)"},
    {"val": 4, "name": "Thanh 4 (Khứ thanh)", "mark": "ˋ", "desc": "Rơi mạnh, dứt khoát (51)"},
    {"val": 0, "name": "Thanh nhẹ (Khinh thanh)", "mark": "·", "desc": "Đọc ngắn, nhẹ và không dấu"},
]

# ─────────────────────────────────────────────────────────────────────────────
# 2. TOÀN BỘ TỔ HỢP HỢP LỆ TRONG TIẾNG TRUNG (VALID PINYIN COMBINATIONS)
# Mapping: (initial, final) -> dict(pinyin, rule_note, examples)
# ─────────────────────────────────────────────────────────────────────────────

def _build_valid_combinations():
    """Xây dựng cơ sở dữ liệu các tổ hợp pinyin chuẩn ngữ âm Hán ngữ."""
    combos = {}

    def add(init, final, pinyin_written, note=None, examples=None):
        combos[(init, final)] = {
            "pinyin": pinyin_written,
            "note": note,
            "examples": examples or []
        }

    # ── b ─────────────────────────────────────────────────────────────────────
    add("b", "a", "ba", examples=["八 (bā - số 8)", "拔 (bá - nhổ)", "把 (bǎ - cầm)", "爸 (bà - bố)"])
    add("b", "o", "bo", examples=["播 (bō - phát thanh)", "伯 (bó - bác)", "跛 (bǒ - đi khập khiễng)", "破 (bò - mỏng)"])
    add("b", "ai", "bai", examples=["掰 (bāi - bẻ)", "白 (bái - trắng)", "百 (bǎi - trăm)", "败 (bài - bại)"])
    add("b", "ei", "bei", examples=["杯 (bēi - cốc)", "北 (běi - phía bắc)", "被 (bèi - bị/chăn)"])
    add("b", "ao", "bao", examples=["包 (bāo - bao/túi)", "薄 (báo - mỏng)", "饱 (bǎo - no)", "报 (bào - báo/báo cáo)"])
    add("b", "an", "ban", examples=["班 (bān - lớp)", "搬 (bān - dọn/chuyển)", "板 (bǎn - tấm ván)", "半 (bàn - một nửa)"])
    add("b", "en", "ben", examples=["奔 (bēn - chạy nhanh)", "本 (běn - quyển/gốc)", "笨 (bèn - ngốc nghếch)"])
    add("b", "ang", "bang", examples=["帮 (bāng - giúp đỡ)", "榜 (bǎng - bảng vàng)", "棒 (bàng - gậy/giỏi)"])
    add("b", "eng", "beng", examples=["崩 (bēng - sụp đổ)", "绷 (běng - căng ra)", "蹦 (bèng - nhảy nhót)"])
    add("b", "i", "bi", examples=["逼 (bī - bức bách)", "鼻 (bí - mũi)", "比 (bǐ - so sánh)", "必 (bì - nhất định)"])
    add("b", "ie", "bie", examples=["憋 (biē - nín/nhịn)", "别 (bié - đừng/khác)", "瘪 (biě - xẹp)", "别 (biè - bướng)"])
    add("b", "iao", "biao", examples=["标 (biāo - tiêu chuẩn)", "表 (biǎo - biểu/đồng hồ)"])
    add("b", "ian", "bian", examples=["边 (biān - bên cạnh)", "扁 (biǎn - dẹp/phẳng)", "变 (biàn - thay đổi)"])
    add("b", "in", "bin", examples=["宾 (bīn - khách)", "滨 (bīn - ven bờ)"])
    add("b", "ing", "bing", examples=["兵 (bīng - lính)", "冰 (bīng - băng đá)", "饼 (bǐng - bánh)", "病 (bìng - bệnh)"])
    add("b", "u", "bu", examples=["不 (bù - không)", "布 (bù - vải)", "补 (bǔ - bổ sung)"])

    # ── p ─────────────────────────────────────────────────────────────────────
    add("p", "a", "pa", examples=["趴 (pā - nằm sấp)", "爬 (pá - leo trèo)", "怕 (pà - sợ)"])
    add("p", "o", "po", examples=["坡 (pō - dốc)", "婆 (pó - bà)", "破 (pò - rách/vỡ)"])
    add("p", "ai", "pai", examples=["拍 (pāi - vỗ/chụp)", "排 (pái - hàng)", "派 (pài - phái)"])
    add("p", "ei", "pei", examples=["陪 (péi - cùng/đi cùng)", "培 (péi - bồi dưỡng)", "配 (pèi - phối hợp)"])
    add("p", "ao", "pao", examples=["抛 (pāo - ném)", "跑 (pǎo - chạy)", "泡 (pào - ngâm/bong bóng)"])
    add("p", "ou", "pou", examples=["剖 (pōu - mổ/phân tích)"])
    add("p", "an", "pan", examples=["潘 (pān - họ Phan)", "盘 (pán - cái đĩa)", "盼 (pàn - mong ước)"])
    add("p", "en", "pen", examples=["喷 (pēn - phun)", "盆 (pén - cái chậu)"])
    add("p", "ang", "pang", examples=["乓 (pāng - bóng bàn)", "旁 (páng - bên cạnh)", "胖 (pàng - béo/mập)"])
    add("p", "eng", "peng", examples=["烹 (pēng - nấu)", "朋 (péng - bạn bè)", "捧 (pěng - bưng/nâng)", "碰 (pèng - chạm)"])
    add("p", "i", "pi", examples=["批 (pī - phê duyệt)", "皮 (pí - da/vỏ)", "匹 (pǐ - ngựa)", "屁 (pì - rắm/vớ vẩn)"])
    add("p", "ie", "pie", examples=["撇 (piē - vứt bỏ)", "瞥 (piē - liếc nhìn)"])
    add("p", "iao", "piao", examples=["飘 (piāo - bay lượn)", "票 (piào - vé)", "漂 (piào - xinh đẹp)"])
    add("p", "ian", "pian", examples=["片 (piàn - mảnh/tấm)", "便 (pián - rẻ)"])
    add("p", "in", "pin", examples=["拼 (pīn - ghép âm)", "贫 (pín - nghèo)", "品 (pǐn - sản phẩm)"])
    add("p", "ing", "ping", examples=["乒 (pīng - bóng bàn)", "平 (píng - hòa bình)", "瓶 (píng - cái lọ)"])
    add("p", "u", "pu", examples=["扑 (pū - lao tới)", "葡 (pú - nho)", "普 (pǔ - phổ thông)"])

    # ── m ─────────────────────────────────────────────────────────────────────
    add("m", "a", "ma", examples=["妈 (mā - mẹ)", "麻 (má - vừng)", "马 (mǎ - ngựa)", "骂 (mà - mắng)"])
    add("m", "o", "mo", examples=["摸 (mō - sờ/chạm)", "模 (mó - khuôn mẫu)", "莫 (mò - chớ/đừng)"])
    add("m", "e", "me", examples=["么 (me - cái gì)"])
    add("m", "ai", "mai", examples=["埋 (mái - chôn)", "买 (mǎi - mua)", "卖 (mài - bán)"])
    add("m", "ei", "mei", examples=["没 (méi - không có)", "美 (měi - đẹp)", "妹 (mèi - em gái)"])
    add("m", "ao", "mao", examples=["猫 (māo - con mèo)", "毛 (máo - lông)", "帽 (mào - cái mũ)"])
    add("m", "ou", "mou", examples=["眸 (móu - con ngươi)", "某 (mǒu - ai đó)"])
    add("m", "an", "man", examples=["满 (mǎn - đầy)", "慢 (màn - chậm)"])
    add("m", "en", "men", examples=["门 (mén - cánh cửa)", "们 (men - các/chúng)"])
    add("m", "ang", "mang", examples=["盲 (máng - mù)", "忙 (máng - bận rộn)"])
    add("m", "eng", "meng", examples=["蒙 (méng - Mông Cổ)", "梦 (mèng - giấc mơ)"])
    add("m", "i", "mi", examples=["咪 (mī - mi)", "米 (mǐ - gạo/mét)", "密 (mì - bí mật)"])
    add("m", "ie", "mie", examples=["灭 (miè - dập tắt)"])
    add("m", "iao", "miao", examples=["苗 (miáo - cây non)", "秒 (miǎo - giây)", "庙 (miào - ngôi chùa)"])
    add("m", "iu", "miu", note="Vận mẫu iou viết gọn thành iu khi ghép với thanh mẫu.", examples=["谬 (miù - sai lầm)"])
    add("m", "ian", "mian", examples=["棉 (mián - bông)", "免 (miǎn - miễn phí)", "面 (miàn - mì/mặt)"])
    add("m", "in", "min", examples=["民 (mín - nhân dân)", "敏 (mǐn - mẫn cảm)"])
    add("m", "ing", "ming", examples=["明 (míng - sáng/ngày mai)", "名 (míng - tên/danh)", "命 (mìng - mệnh)"])
    add("m", "u", "mu", examples=["母 (mǔ - mẹ)", "木 (mù - gỗ)", "目 (mù - mắt)"])

    # ── f ─────────────────────────────────────────────────────────────────────
    add("f", "a", "fa", examples=["发 (fā - phát/tóc)", "法 (fǎ - pháp luật/nước Pháp)"])
    add("f", "o", "fo", examples=["佛 (fó - Phật)"])
    add("f", "ei", "fei", examples=["飞 (fēi - bay)", "肥 (féi - béo)", "费 (fèi - phí)"])
    add("f", "ou", "fou", examples=["否 (fǒu - phủ nhận)"])
    add("f", "an", "fan", examples=["翻 (fān - lật/dịch)", "烦 (fán - phiền)", "反 (fǎn - phản đối)", "饭 (fàn - cơm)"])
    add("f", "en", "fen", examples=["分 (fēn - phút/chia)", "粉 (fěn - bột/màu hồng)", "份 (fèn - phần)"])
    add("f", "ang", "fang", examples=["方 (fāng - vuông/phương hướng)", "房 (fáng - phòng/nhà)", "放 (fàng - buông/thả)"])
    add("f", "eng", "feng", examples=["风 (fēng - gió)", "封 (fēng - phong bì)", "逢 (féng - gặp)"])
    add("f", "u", "fu", examples=["夫 (fū - phu)", "服 (fú - trang phục)", "府 (fǔ - phủ)", "父 (fù - cha)"])

    # ── d ─────────────────────────────────────────────────────────────────────
    add("d", "a", "da", examples=["搭 (dā - dựng)", "达 (dá - đạt)", "打 (dǎ - đánh)", "大 (dà - to lớn)"])
    add("d", "e", "de", examples=["得 (dé - được)", "德 (dé - đạo đức)", "的 (de - của)"])
    add("d", "ai", "dai", examples=["呆 (dāi - ngây ngô)", "带 (dài - mang theo)", "袋 (dài - cái túi)"])
    add("d", "ei", "dei", examples=["得 (děi - phải làm gì)"])
    add("d", "ao", "dao", examples=["刀 (dāo - con dao)", "岛 (dǎo - hòn đảo)", "到 (dào - đến)"])
    add("d", "ou", "dou", examples=["都 (dōu - đều)", "豆 (dòu - hạt đậu)"])
    add("d", "an", "dan", examples=["丹 (dān - màu đỏ)", "胆 (dǎn - gan dạ)", "但 (dàn - nhưng)"])
    add("d", "en", "den", examples=["扽 (dèn - giật mạnh)"])
    add("d", "ang", "dang", examples=["当 (dāng - làm/đang)", "党 (dǎng - đảng)"])
    add("d", "eng", "deng", examples=["灯 (dēng - cái đèn)", "等 (děng - đợi/chờ)", "凳 (dèng - cái ghế đẩu)"])
    add("d", "ong", "dong", examples=["东 (dōng - phía đông)", "懂 (dǒng - hiểu)", "动 (dòng - động/cử động)"])
    add("d", "i", "di", examples=["低 (dī - thấp)", "敌 (dí - kẻ thù)", "底 (dǐ - đáy)", "第 (dì - thứ tự)"])
    add("d", "ia", "dia", examples=["嗲 (diǎ - nũng nịu)"])
    add("d", "ie", "die", examples=["爹 (diē - cha/bố)", "跌 (diē - ngã)", "蝶 (dié - bướm)"])
    add("d", "iao", "diao", examples=["雕 (diāo - điêu khắc)", "掉 (diào - rơi/rụng)"])
    add("d", "iu", "diu", note="Vận mẫu iou viết gọn thành iu.", examples=["丢 (diū - đánh mất)"])
    add("d", "ian", "dian", examples=["颠 (diān - đỉnh)", "点 (diǎn - giờ/chút)", "电 (diàn - điện)"])
    add("d", "ing", "ding", examples=["丁 (dīng - đinh)", "顶 (dǐng - đỉnh)", "定 (dìng - cố định)"])
    add("d", "u", "du", examples=["嘟 (dū - kêu bíp)", "读 (dú - đọc)", "堵 (dǔ - tắc nghẽn)", "度 (dù - độ)"])
    add("d", "uo", "duo", examples=["多 (duō - nhiều)", "夺 (duó - đoạt)", "朵 (duǒ - đóa hoa)"])
    add("d", "ui", "dui", note="Vận mẫu uei viết gọn thành ui.", examples=["堆 (duī - đống)", "对 (duì - đúng/đối với)"])
    add("d", "uan", "duan", examples=["端 (duān - đoan trang)", "短 (duǎn - ngắn)", "断 (duàn - đứt)"])
    add("d", "un", "dun", note="Vận mẫu uen viết gọn thành un.", examples=["蹲 (dūn - ngồi xổm)", "吨 (dūn - tấn)", "顿 (dùn - bữa cơm)"])

    # ── t ─────────────────────────────────────────────────────────────────────
    add("t", "a", "ta", examples=["他 (tā - anh ấy)", "她 (tā - cô ấy)", "塔 (tǎ - cái tháp)", "踏 (tà - giẫm)"])
    add("t", "e", "te", examples=["特 (tè - đặc biệt)"])
    add("t", "ai", "tai", examples=["胎 (tāi - thai)", "台 (tái - đài/bệ)", "太 (tài - quá)"])
    add("t", "ao", "tao", examples=["掏 (tāo - móc)", "桃 (táo - quả đào)", "套 (tào - bộ/áo khoác)"])
    add("t", "ou", "tou", examples=["偷 (tōu - trộm)", "头 (tóu - đầu)", "透 (tòu - thấu)"])
    add("t", "an", "tan", examples=["贪 (tān - tham)", "谈 (tán - nói chuyện)", "碳 (tàn - các-bon)"])
    add("t", "ang", "tang", examples=["汤 (tāng - canh)", "糖 (táng - đường/kẹo)", "躺 (tǎng - nằm)"])
    add("t", "eng", "teng", examples=["疼 (téng - đau)", "腾 (téng - bay vút)"])
    add("t", "ong", "tong", examples=["通 (tōng - thông suốt)", "同 (tóng - cùng)", "痛 (tòng - đau đớn)"])
    add("t", "i", "ti", examples=["梯 (tī - cái thang)", "题 (tí - đề mục)", "体 (tǐ - thân thể)", "替 (tì - thay thế)"])
    add("t", "ie", "tie", examples=["贴 (tiē - dán)", "铁 (tiě - sắt)"])
    add("t", "iao", "tiao", examples=["挑 (tiāo - chọn)", "条 (tiáo - sợi/con)", "跳 (tiào - nhảy)"])
    add("t", "ian", "tian", examples=["天 (tiān - trời/ngày)", "田 (tián - ruộng)", "甜 (tián - ngọt)"])
    add("t", "ing", "ting", examples=["厅 (tīng - phòng khách)", "听 (tīng - nghe)", "停 (tíng - dừng)"])
    add("t", "u", "tu", examples=["凸 (tū - lồi)", "图 (tú - bức tranh)", "土 (tǔ - đất)", "兔 (tù - con thỏ)"])
    add("t", "uo", "tuo", examples=["拖 (tuō - kéo lê)", "脱 (tuō - cởi)", "妥 (tuǒ - thỏa đáng)"])
    add("t", "ui", "tui", note="Vận mẫu uei viết gọn thành ui.", examples=["推 (tuī - đẩy)", "腿 (tuǐ - cái chân)", "退 (tuì - rút lui)"])
    add("t", "uan", "tuan", examples=["团 (tuán - đoàn kết/đoàn)"])
    add("t", "un", "tun", note="Vận mẫu uen viết gọn thành un.", examples=["吞 (tūn - nuốt)", "褪 (tùn - phai màu)"])

    # ── n ─────────────────────────────────────────────────────────────────────
    add("n", "a", "na", examples=["拿 (ná - cầm/lấy)", "哪 (nǎ - ở đâu)", "那 (nà - kia/đó)"])
    add("n", "e", "ne", examples=["呢 (ne - trợ từ nghi vấn)"])
    add("n", "ai", "nai", examples=["奶 (nǎi - sữa/bà)", "耐 (nài - kiên nhẫn)"])
    add("n", "ei", "nei", examples=["内 (nèi - bên trong)"])
    add("n", "ao", "nao", examples=["闹 (nào - náo nhiệt)"])
    add("n", "ou", "nou", examples=["耨 (nòu - làm cỏ)"])
    add("n", "an", "nan", examples=["男 (nán - con trai)", "南 (nán - phía nam)", "难 (nán - khó)"])
    add("n", "en", "nen", examples=["嫩 (nèn - non/mềm)"])
    add("n", "ang", "nang", examples=["囊 (náng - cái túi)"])
    add("n", "eng", "neng", examples=["能 (néng - có thể)"])
    add("n", "ong", "nong", examples=["农 (nóng - nông nghiệp)", "弄 (nòng - làm)"])
    add("n", "i", "ni", examples=["你 (nǐ - bạn)", "泥 (ní - bùn)", "逆 (nì - ngược)"])
    add("n", "ia", "nia", examples=["嗲 (niǎ - tiếng địa phương)"])
    add("n", "ie", "nie", examples=["捏 (niē - véo/nặn)", "贴 (niè)"])
    add("n", "iao", "niao", examples=["鸟 (niǎo - con chim)", "尿 (niào - tiểu tiện)"])
    add("n", "iu", "niu", note="Vận mẫu iou viết gọn thành iu.", examples=["牛 (niú - con bò)", "纽 (niǔ - khuy áo)"])
    add("n", "ian", "nian", examples=["年 (nián - năm)", "念 (niàn - nhớ/đọc)"])
    add("n", "in", "nin", examples=["您 (nín - ngài/ông)"])
    add("n", "iang", "niang", examples=["娘 (niáng - mẹ/cô nương)"])
    add("n", "ing", "ning", examples=["宁 (níng - yên bình)", "拧 (nǐng - vặn xoắn)"])
    add("n", "u", "nu", examples=["奴 (nú - nô lệ)", "努 (nǔ - nỗ lực)", "怒 (nù - giận dữ)"])
    add("n", "uo", "nuo", examples=["挪 (nuó - di chuyển)", "懦 (nuò - nhu nhược)"])
    add("n", "uan", "nuan", examples=["暖 (nuǎn - ấm áp)"])
    add("n", "ü", "nü", note="Thanh mẫu n khi đi với ü PHẢI GIỮ NGUYÊN hai dấu chấm trên đầu (nü) để phân biệt với nu.", examples=["女 (nǚ - phụ nữ)"])
    add("n", "üe", "nüe", note="Thanh mẫu n khi đi với üe PHẢI GIỮ NGUYÊN hai dấu chấm trên đầu (nüe).", examples=["虐 (nüè - ngược đãi)"])

    # ── l ─────────────────────────────────────────────────────────────────────
    add("l", "a", "la", examples=["拉 (lā - kéo)", "蜡 (là - sáp/nến)", "辣 (là - cay)"])
    add("l", "e", "le", examples=["乐 (lè - vui vẻ)", "了 (le - rồi)"])
    add("l", "ai", "lai", examples=["来 (lái - đến)", "赖 (lài - dựa dẫm)"])
    add("l", "ei", "lei", examples=["雷 (léi - sấm sét)", "累 (lèi - mệt mỏi)"])
    add("l", "ao", "lao", examples=["老 (lǎo - già)", "捞 (lāo - vớt)"])
    add("l", "ou", "lou", examples=["楼 (lóu - tòa lầu)", "漏 (lòu - rò rỉ)"])
    add("l", "an", "lan", examples=["蓝 (lán - màu xanh)", "懒 (lǎn - lười)"])
    add("l", "ang", "lang", examples=["浪 (làng - sóng biển)", "狼 (láng - con sói)"])
    add("l", "eng", "leng", examples=["冷 (lěng - lạnh)"])
    add("l", "ong", "long", examples=["龙 (lóng - con rồng)", "拢 (lǒng - gom lại)"])
    add("l", "i", "li", examples=["梨 (lí - quả lê)", "里 (lǐ - bên trong)", "立 (lì - đứng)"])
    add("l", "ia", "lia", examples=["俩 (liǎ - hai người)"])
    add("l", "ie", "lie", examples=["猎 (liè - săn bắn)", "列 (liè - hàng)"])
    add("l", "iao", "liao", examples=["聊 (liáo - nói chuyện)", "料 (liào - nguyên liệu)"])
    add("l", "iu", "liu", note="Vận mẫu iou viết gọn thành iu.", examples=["六 (liù - số 6)", "流 (liú - chảy)"])
    add("l", "ian", "lian", examples=["连 (lián - liền)", "脸 (liǎn - khuôn mặt)", "练 (liàn - luyện tập)"])
    add("l", "in", "lin", examples=["林 (lín - rừng cây)", "临 (lín - gần/sắp)"])
    add("l", "iang", "liang", examples=["良 (liáng - lương thiện)", "亮 (liàng - sáng)"])
    add("l", "ing", "ling", examples=["零 (líng - số 0)", "领 (lǐng - dẫn dắt)"])
    add("l", "u", "lu", examples=["路 (lù - con đường)", "录 (lù - ghi âm)"])
    add("l", "uo", "luo", examples=["罗 (luó - la bàn)", "落 (luò - rơi)"])
    add("l", "uan", "luan", examples=["乱 (luàn - hỗn loạn)"])
    add("l", "un", "lun", note="Vận mẫu uen viết gọn thành un.", examples=["轮 (lún - bánh xe)", "论 (lùn - lý luận)"])
    add("l", "ü", "lü", note="Thanh mẫu l khi đi với ü PHẢI GIỮ NGUYÊN hai dấu chấm trên đầu (lü) để phân biệt với lu.", examples=["绿 (lǜ - màu xanh lá)", "驴 (lǘ - con lừa)"])
    add("l", "üe", "lüe", note="Thanh mẫu l khi đi với üe PHẢI GIỮ NGUYÊN hai dấu chấm trên đầu (lüe).", examples=["略 (lüè - lược/sơ lược)"])

    # ── g ─────────────────────────────────────────────────────────────────────
    add("g", "a", "ga", examples=["嘎 (gā - tiếng vịt kêu)"])
    add("g", "e", "ge", examples=["哥 (gē - anh trai)", "歌 (gē - bài hát)", "个 (gè - cái/chiếc)"])
    add("g", "ai", "gai", examples=["该 (gāi - nên/phải)", "改 (gǎi - sửa)", "盖 (gài - cái nắp)"])
    add("g", "ei", "gei", examples=["给 (gěi - cho/tặng)"])
    add("g", "ao", "gao", examples=["高 (gāo - cao)", "告 (gào - bảo/báo)"])
    add("g", "ou", "gou", examples=["沟 (gōu - mương)", "狗 (gǒu - con chó)", "够 (gòu - đủ)"])
    add("g", "an", "gan", examples=["干 (gān - khô)", "赶 (gǎn - đuổi theo)", "敢 (gǎn - dám)"])
    add("g", "en", "gen", examples=["根 (gēn - cái rễ)", "跟 (gēn - đi cùng)"])
    add("g", "ang", "gang", examples=["刚 (gāng - vừa mới)", "港 (gǎng - bến cảng)"])
    add("g", "eng", "geng", examples=["更 (gèng - càng/hơn)", "耕 (gēng - cày cấy)"])
    add("g", "ong", "gong", examples=["工 (gōng - công nhân)", "共 (gòng - tổng cộng)"])
    add("g", "u", "gu", examples=["姑 (gū - cô/dì)", "古 (gǔ - cổ xưa)", "故 (gù - cố nhân)"])
    add("g", "ua", "gua", examples=["瓜 (guā - quả dưa)", "刮 (guā - cạo/thổi gió)"])
    add("g", "uo", "guo", examples=["锅 (guō - cái nồi)", "国 (guó - quốc gia)", "果 (guǒ - hoa quả)"])
    add("g", "uai", "guai", examples=["乖 (guāi - ngoan ngoãn)", "怪 (guài - quái lạ)"])
    add("g", "ui", "gui", note="Vận mẫu uei viết gọn thành ui.", examples=["归 (guī - trở về)", "鬼 (guǐ - con ma)", "贵 (guì - đắt/quý)"])
    add("g", "uan", "guan", examples=["关 (guān - đóng)", "官 (guān - quan)", "馆 (guǎn - quán/bảo tàng)"])
    add("g", "un", "gun", note="Vận mẫu uen viết gọn thành un.", examples=["棍 (gùn - cây gậy)", "滚 (gǔn - cút/lăn)"])
    add("g", "uang", "guang", examples=["光 (guāng - ánh sáng)", "广 (guǎng - rộng lớn)"])

    # ── k ─────────────────────────────────────────────────────────────────────
    add("k", "a", "ka", examples=["咖 (kā - cà phê)", "卡 (kǎ - cái thẻ)"])
    add("k", "e", "ke", examples=["科 (kē - môn học)", "渴 (kě - khát nước)", "课 (kè - bài học)"])
    add("k", "ai", "kai", examples=["开 (kāi - mở)", "凯 (kǎi - chiến thắng)"])
    add("k", "ei", "kei", examples=["剋 (kēi - mắng mỏ)"])
    add("k", "ao", "kao", examples=["考 (kǎo - thi cử)", "烤 (kǎo - nướng)"])
    add("k", "ou", "kou", examples=["口 (kǒu - cái miệng)", "扣 (kòu - cài cúc)"])
    add("k", "an", "kan", examples=["看 (kàn - xem/nhìn)", "砍 (kǎn - chặt)"])
    add("k", "en", "ken", examples=["肯 (kěn - đồng ý)", "啃 (kěn - gặm)"])
    add("k", "ang", "kang", examples=["康 (kāng - khỏe mạnh)", "抗 (kàng - kháng cự)"])
    add("k", "eng", "keng", examples=["坑 (kēng - cái hố)"])
    add("k", "ong", "kong", examples=["空 (kōng - không trung)", "恐 (kǒng - khủng hoảng)"])
    add("k", "u", "ku", examples=["哭 (kū - khóc)", "苦 (kǔ - đắng)", "裤 (kù - cái quần)"])
    add("k", "ua", "kua", examples=["夸 (kuā - khen ngợi)", "跨 (kuà - sải bước)"])
    add("k", "uo", "kuo", examples=["扩 (kuò - mở rộng)", "阔 (kuò - rộng rãi)"])
    add("k", "uai", "kuai", examples=["快 (kuài - nhanh)", "块 (kuài - đồng/miếng)", "筷 (kuài - đôi đũa)"])
    add("k", "ui", "kui", note="Vận mẫu uei viết gọn thành ui.", examples=["亏 (kuī - thua lỗ)", "愧 (kuì - hổ thẹn)"])
    add("k", "uan", "kuan", examples=["款 (kuǎn - khoản tiền)", "宽 (kuān - rộng)"])
    add("k", "un", "kun", note="Vận mẫu uen viết gọn thành un.", examples=["捆 (kǔn - trói)", "困 (kùn - buồn ngủ)"])
    add("k", "uang", "kuang", examples=["狂 (kuáng - cuồng)", "矿 (kuàng - mỏ quặng)"])

    # ── h ─────────────────────────────────────────────────────────────────────
    add("h", "a", "ha", examples=["哈 (hā - cười ha ha)"])
    add("h", "e", "he", examples=["喝 (hē - uống)", "河 (hé - dòng sông)", "合 (hé - thích hợp)", "和 (hé - và)"])
    add("h", "ai", "hai", examples=["海 (hǎi - biển)", "孩 (hái - đứa trẻ)", "害 (hài - hại)"])
    add("h", "ei", "hei", examples=["黑 (hēi - màu đen)"])
    add("h", "ao", "hao", examples=["好 (hǎo - tốt)", "号 (hào - số)", "耗 (hào - tiêu hao)"])
    add("h", "ou", "hou", examples=["猴 (hóu - con khỉ)", "后 (hòu - phía sau)", "厚 (hòu - dày)"])
    add("h", "an", "han", examples=["汉 (hàn - Hán/tiếng Trung)", "喊 (hǎn - kêu to)", "汗 (hàn - mồ hôi)"])
    add("h", "en", "hen", examples=["很 (hěn - rất)", "恨 (hèn - oán hận)"])
    add("h", "ang", "hang", examples=["航 (háng - hàng hải)", "行 (háng - ngành/ngân hàng)"])
    add("h", "eng", "heng", examples=["横 (héng - nét ngang)", "哼 (hēng - hừm)"])
    add("h", "ong", "hong", examples=["红 (hóng - màu đỏ)", "洪 (hóng - lũ lụt)"])
    add("h", "u", "hu", examples=["胡 (hú - họ Hồ)", "虎 (hǔ - con hổ)", "户 (hù - hộ gia đình)"])
    add("h", "ua", "hua", examples=["花 (huā - hoa)", "华 (huá - hoa lệ/Trung Hoa)", "话 (huà - lời nói)"])
    add("h", "uo", "huo", examples=["火 (huǒ - lửa)", "活 (huó - sống)", "或 (huò - hoặc)"])
    add("h", "uai", "huai", examples=["坏 (huài - xấu/hỏng)", "怀 (huái - hoài niệm)"])
    add("h", "ui", "hui", note="Vận mẫu uei viết gọn thành ui.", examples=["回 (huí - trở về)", "会 (huì - biết/hội)", "灰 (huī - màu tro)"])
    add("h", "uan", "huan", examples=["欢 (huān - hoan nghênh)", "换 (huàn - đổi)"])
    add("h", "un", "hun", note="Vận mẫu uen viết gọn thành un.", examples=["婚 (hūn - kết hôn)", "混 (hùn - hỗn hợp)"])
    add("h", "uang", "huang", examples=["黄 (huáng - màu vàng)", "谎 (huǎng - lời nói dối)"])

    # ── j, q, x (Mặt lưỡi: CHỈ ĐI VỚI HÀNG i VÀ ü) ───────────────────────────
    for init in ["j", "q", "x"]:
        # Đi với hàng i:
        add(init, "i", f"{init}i")
        add(init, "ia", f"{init}ia")
        add(init, "ie", f"{init}ie")
        add(init, "iao", f"{init}iao")
        add(init, "iu", f"{init}iu", note="Vận mẫu iou viết gọn thành iu.")
        add(init, "ian", f"{init}ian")
        add(init, "in", f"{init}in")
        add(init, "iang", f"{init}iang")
        add(init, "ing", f"{init}ing")
        add(init, "iong", f"{init}iong")
        # Đi với hàng ü (LƯỢC BỎ HAI CHẤM THÀNH u KHI VIẾT):
        rule_u = f"QUY TẮC CHÍNH TẢ: Thanh mẫu {init} khi đi với vận mẫu ü thì LƯỢC BỎ HAI DẤU CHẤM trên đầu và viết thành '{init}u', nhưng PHÁT ÂM VẪN LÀ [ü] tròn môi!"
        add(init, "ü", f"{init}u", note=rule_u)
        add(init, "üe", f"{init}ue", note=f"QUY TẮC CHÍNH TẢ: {init} + üe viết thành '{init}ue'.")
        add(init, "üan", f"{init}uan", note=f"QUY TẮC CHÍNH TẢ: {init} + üan viết thành '{init}uan'.")
        add(init, "ün", f"{init}un", note=f"QUY TẮC CHÍNH TẢ: {init} + ün viết thành '{init}un'.")

    # Ví dụ cụ thể cho j, q, x:
    combos[("j", "i")]["examples"] = ["几 (jǐ - mấy)", "鸡 (jī - con gà)", "机 (jī - máy bay)"]
    combos[("j", "ia")]["examples"] = ["家 (jiā - nhà/gia đình)", "加 (jiā - cộng/thêm)"]
    combos[("j", "ie")]["examples"] = ["接 (jiē - đón)", "姐 (jiě - chị gái)", "节 (jié - ngày lễ)"]
    combos[("j", "iao")]["examples"] = ["叫 (jiào - gọi là)", "教 (jiào - dạy học)"]
    combos[("j", "iu")]["examples"] = ["九 (jiǔ - số 9)", "酒 (jiǔ - rượu)", "久 (jiǔ - lâu)"]
    combos[("j", "ian")]["examples"] = ["见 (jiàn - gặp)", "件 (jiàn - cái/chiếc)"]
    combos[("j", "in")]["examples"] = ["金 (jīn - vàng)", "进 (jìn - vào)", "近 (jìn - gần)"]
    combos[("j", "ing")]["examples"] = ["经 (jīng - kinh qua)", "景 (jǐng - cảnh)"]
    combos[("j", "ü")]["examples"] = ["句 (jù - câu)", "菊 (jú - hoa cúc)"]
    combos[("j", "üe")]["examples"] = ["决 (jué - quyết định)", "绝 (jué - tuyệt vời)"]

    combos[("q", "i")]["examples"] = ["七 (qī - số 7)", "期 (qī - kỳ/thời hạn)", "起 (qǐ - thức dậy)", "气 (qì - không khí)"]
    combos[("q", "ian")]["examples"] = ["千 (qiān - nghìn)", "钱 (qián - tiền)"]
    combos[("q", "ing")]["examples"] = ["请 (qǐng - xin/mời)", "青 (qīng - màu xanh)"]
    combos[("q", "ü")]["examples"] = ["去 (qù - đi)"]
    combos[("q", "üe")]["examples"] = ["确 (què - chính xác)", "雀 (què - chim sẻ)"]

    combos[("x", "i")]["examples"] = ["西 (xī - phía tây)", "洗 (xǐ - rửa/giặt)", "细 (xì - tinh tế)"]
    combos[("x", "ia")]["examples"] = ["下 (xià - bên dưới)", "夏 (xià - mùa hè)"]
    combos[("x", "ie")]["examples"] = ["写 (xiě - viết)", "谢 (xiè - cảm ơn)"]
    combos[("x", "iao")]["examples"] = ["小 (xiǎo - nhỏ bé)", "笑 (xiào - cười)"]
    combos[("x", "ian")]["examples"] = ["先 (xiān - trước tiên)", "线 (xiàn - đường dây)"]
    combos[("x", "in")]["examples"] = ["新 (xīn - mới)", "信 (xìn - bức thư/tin tưởng)"]
    combos[("x", "ing")]["examples"] = ["星 (xīng - ngôi sao)", "行 (xíng - được/đi)"]
    combos[("x", "ü")]["examples"] = ["需 (xū - cần thiết)", "许 (xǔ - cho phép)"]
    combos[("x", "üe")]["examples"] = ["学 (xué - học)", "雪 (xuě - tuyết)"]

    # ── zh ────────────────────────────────────────────────────────────────────
    add("zh", "a", "zha", examples=["炸 (zhá - rán/chiên)", "扎 (zhā - đâm/cắm)"])
    add("zh", "e", "zhe", examples=["这 (zhè - đây/này)", "者 (zhě - người/kẻ)"])
    add("zh", "i", "zhi", note="Thanh mẫu zh khi đi với i đọc là [zhi] (âm uốn lưỡi, không đọc là di).", examples=["知 (zhī - biết)", "只 (zhǐ - chỉ/con)", "这 (zhì)"])
    add("zh", "ai", "zhai", examples=["摘 (zhāi - hái)", "窄 (zhǎi - hẹp)"])
    add("zh", "ei", "zhei", examples=["这 (zhèi - đây/này)"])
    add("zh", "ao", "zhao", examples=["找 (zhǎo - tìm kiếm)", "照 (zhào - chiếu/chụp ảnh)"])
    add("zh", "ou", "zhou", examples=["周 (zhōu - tuần/chu)", "州 (zhōu - châu/tỉnh)"])
    add("zh", "an", "zhan", examples=["站 (zhàn - trạm/đứng)", "战 (zhàn - chiến tranh)"])
    add("zh", "en", "zhen", examples=["真 (zhēn - thật)", "阵 (zhèn - trận)"])
    add("zh", "ang", "zhang", examples=["张 (zhāng - họ Trương/tờ)", "长 (zhǎng - trưởng/lớn)"])
    add("zh", "eng", "zheng", examples=["正 (zhèng - chính/đang)", "整 (zhěng - nguyên vẹn)"])
    add("zh", "ong", "zhong", examples=["中 (zhōng - trung tâm)", "重 (zhòng - nặng)"])
    add("zh", "u", "zhu", examples=["猪 (zhū - con lợn)", "住 (zhù - sống/ở)"])
    add("zh", "ua", "zhua", examples=["抓 (zhuā - bắt/nắm)"])
    add("zh", "uo", "zhuo", examples=["桌 (zhuō - cái bàn)", "捉 (zhuō - bắt)"])
    add("zh", "uai", "zhuai", examples=["拽 (zhuài - lôi kéo)"])
    add("zh", "ui", "zhui", note="Vận mẫu uei viết gọn thành ui.", examples=["追 (zhuī - đuổi theo)"])
    add("zh", "uan", "zhuan", examples=["专 (zhuān - chuyên môn)", "转 (zhuǎn - chuyển)"])
    add("zh", "un", "zhun", note="Vận mẫu uen viết gọn thành un.", examples=["准 (zhǔn - chuẩn xác)"])
    add("zh", "uang", "zhuang", examples=["装 (zhuāng - trang bị/mặc)", "状 (zhuàng - hình trạng)"])

    # ── ch ────────────────────────────────────────────────────────────────────
    add("ch", "a", "cha", examples=["茶 (chá - trà)", "差 (chà - kém)"])
    add("ch", "e", "che", examples=["车 (chē - xe cộ)"])
    add("ch", "i", "chi", note="Thanh mẫu ch khi đi với i đọc bật hơi uốn lưỡi [chī].", examples=["吃 (chī - ăn)", "迟 (chí - muộn)"])
    add("ch", "ai", "chai", examples=["拆 (chāi - tháo gỡ)", "柴 (chái - củi)"])
    add("ch", "ao", "chao", examples=["抄 (chāo - chép)", "超 (chāo - siêu thị)"])
    add("ch", "ou", "chou", examples=["抽 (chōu - rút/hút thuốc)", "愁 (chóu - buồn rầu)"])
    add("ch", "an", "chan", examples=["产 (chǎn - sản xuất)", "馋 (chán - thèm ăn)"])
    add("ch", "en", "chen", examples=["陈 (chén - họ Trần)", "晨 (chén - buổi sớm)"])
    add("ch", "ang", "chang", examples=["长 (cháng - dài)", "唱 (chàng - hát)", "常 (cháng - thường xuyên)"])
    add("ch", "eng", "cheng", examples=["成 (chéng - trở thành)", "城 (chéng - thành phố)"])
    add("ch", "ong", "chong", examples=["虫 (chóng - con sâu)", "重 (chóng - lặp lại)"])
    add("ch", "u", "chu", examples=["出 (chū - ra ngoài)", "初 (chū - ban đầu)"])
    add("ch", "uo", "chuo", examples=["戳 (chuō - chọc/đâm)"])
    add("ch", "uai", "chuai", examples=["揣 (chuāi - nhét vào túi)"])
    add("ch", "ui", "chui", note="Vận mẫu uei viết gọn thành ui.", examples=["吹 (chuī - thổi)"])
    add("ch", "uan", "chuan", examples=["穿 (chuān - mặc)", "船 (chuán - chiếc thuyền)"])
    add("ch", "un", "chun", note="Vận mẫu uen viết gọn thành un.", examples=["春 (chūn - mùa xuân)"])
    add("ch", "uang", "chuang", examples=["窗 (chuāng - cửa sổ)", "床 (chuáng - cái giường)"])

    # ── sh ────────────────────────────────────────────────────────────────────
    add("sh", "a", "sha", examples=["沙 (shā - cát)", "傻 (shǎ - ngốc)"])
    add("sh", "e", "she", examples=["蛇 (shé - con rắn)", "舍 (shè - xá)"])
    add("sh", "i", "shi", note="Thanh mẫu sh khi đi với i đọc uốn lưỡi [shī].", examples=["是 (shì - là)", "十 (shí - số 10)", "事 (shì - việc)"])
    add("sh", "ai", "shai", examples=["晒 (shài - phơi nắng)"])
    add("sh", "ei", "shei", examples=["谁 (shéi - ai)"])
    add("sh", "ao", "shao", examples=["少 (shǎo - ít)", "烧 (shāo - nấu/thiêu)"])
    add("sh", "ou", "shou", examples=["手 (shǒu - bàn tay)", "收 (shōu - thu nhận)"])
    add("sh", "an", "shan", examples=["山 (shān - ngọn núi)", "扇 (shàn - cái quạt)"])
    add("sh", "en", "shen", examples=["身 (shēn - thân thể)", "什 (shén - cái gì)"])
    add("sh", "ang", "shang", examples=["上 (shàng - bên trên)", "商 (shāng - thương nghiệp)"])
    add("sh", "eng", "sheng", examples=["生 (shēng - sinh ra)", "声 (shēng - âm thanh)"])
    add("sh", "u", "shu", examples=["书 (shū - cuốn sách)", "树 (shù - cái cây)"])
    add("sh", "ua", "shua", examples=["刷 (shuā - đánh răng/quét)"])
    add("sh", "uo", "shuo", examples=["说 (shuō - nói)"])
    add("sh", "uai", "shuai", examples=["摔 (shuāi - ngã)", "帅 (shuài - đẹp trai)"])
    add("sh", "ui", "shui", note="Vận mẫu uei viết gọn thành ui.", examples=["水 (shuǐ - nước)", "睡 (shuì - ngủ)"])
    add("sh", "uan", "shuan", examples=["栓 (shuān - then chốt)"])
    add("sh", "un", "shun", note="Vận mẫu uen viết gọn thành un.", examples=["顺 (shùn - thuận lợi)"])
    add("sh", "uang", "shuang", examples=["双 (shuāng - đôi/cặp)"])

    # ── r ─────────────────────────────────────────────────────────────────────
    add("r", "e", "re", examples=["热 (rè - nóng)"])
    add("r", "i", "ri", note="Thanh mẫu r khi đi với i đọc uốn lưỡi [rì].", examples=["日 (rì - mặt trời/ngày)"])
    add("r", "ao", "rao", examples=["饶 (ráo - tha thứ)"])
    add("r", "ou", "rou", examples=["肉 (ròu - thịt)"])
    add("r", "an", "ran", examples=["然 (rán - nhiên)", "染 (rǎn - nhuộm)"])
    add("r", "en", "ren", examples=["人 (rén - con người)", "认 (rèn - nhận biết)"])
    add("r", "ang", "rang", examples=["让 (ràng - nhường/cho phép)"])
    add("r", "eng", "reng", examples=["扔 (rēng - ném)"])
    add("r", "ong", "rong", examples=["容 (róng - dung mạo)", "荣 (róng - vinh hoa)"])
    add("r", "u", "ru", examples=["如 (rú - như/nếu)"])
    add("r", "uo", "ruo", examples=["弱 (ruò - yếu ớt)"])
    add("r", "ui", "rui", note="Vận mẫu uei viết gọn thành ui.", examples=["瑞 (ruì - điềm lành)"])
    add("r", "uan", "ruan", examples=["软 (ruǎn - mềm)"])
    add("r", "un", "run", note="Vận mẫu uen viết gọn thành un.", examples=["润 (rùn - nhuận)"])

    # ── z ─────────────────────────────────────────────────────────────────────
    add("z", "a", "za", examples=["杂 (zá - phức tạp)"])
    add("z", "e", "ze", examples=["则 (zé - quy tắc)", "责 (zé - trách nhiệm)"])
    add("z", "i", "zi", note="Thanh mẫu z khi đi với i đọc đầu lưỡi thẳng [zī].", examples=["字 (zì - chữ Hán)", "子 (zǐ - con)"])
    add("z", "ai", "zai", examples=["在 (zài - ở)", "再 (zài - lại/lần nữa)"])
    add("z", "ei", "zei", examples=["贼 (zéi - kẻ trộm)"])
    add("z", "ao", "zao", examples=["早 (zǎo - buổi sáng)", "造 (zào - chế tạo)"])
    add("z", "ou", "zou", examples=["走 (zǒu - đi bộ)"])
    add("z", "an", "zan", examples=["赞 (zàn - khen ngợi)"])
    add("z", "en", "zen", examples=["怎 (zěn - làm sao/thế nào)"])
    add("z", "ang", "zang", examples=["脏 (zāng - bẩn)"])
    add("z", "eng", "zeng", examples=["增 (zēng - tăng thêm)"])
    add("z", "ong", "zong", examples=["总 (zǒng - tổng cộng)"])
    add("z", "u", "zu", examples=["组 (zǔ - tổ/nhóm)", "足 (zú - chân/đầy đủ)"])
    add("z", "uo", "zuo", examples=["做 (zuò - làm)", "坐 (zuò - ngồi)", "昨 (zuó - hôm qua)"])
    add("z", "ui", "zui", note="Vận mẫu uei viết gọn thành ui.", examples=["最 (zuì - nhất)", "嘴 (zuǐ - cái miệng)"])
    add("z", "uan", "zuan", examples=["钻 (zuān - khoan/kim cương)"])
    add("z", "un", "zun", note="Vận mẫu uen viết gọn thành un.", examples=["尊 (zūn - tôn kính)"])

    # ── c ─────────────────────────────────────────────────────────────────────
    add("c", "a", "ca", examples=["擦 (cā - lau chùi)"])
    add("c", "e", "ce", examples=["策 (cè - đối sách)", "厕 (cè - nhà vệ sinh)"])
    add("c", "i", "ci", note="Thanh mẫu c bật hơi mạnh khi đi với i: [cī].", examples=["词 (cí - từ vựng)", "次 (cì - lần)"])
    add("c", "ai", "cai", examples=["菜 (cài - món ăn/rau)", "猜 (cāi - đoán)"])
    add("c", "ao", "cao", examples=["草 (cǎo - ngọn cỏ)"])
    add("c", "ou", "cou", examples=["凑 (còu - tụ họp)"])
    add("c", "an", "can", examples=["餐 (cān - bữa ăn)", "参 (cān - tham gia)"])
    add("c", "en", "cen", examples=["参 (cēn - không đều)"])
    add("c", "ang", "cang", examples=["藏 (cáng - giấu/tàng)"])
    add("c", "eng", "ceng", examples=["层 (céng - tầng lầu)"])
    add("c", "ong", "cong", examples=["从 (cóng - từ đâu)", "聪 (cōng - thông minh)"])
    add("c", "u", "cu", examples=["醋 (cù - giấm chua)", "粗 (cū - thô kệch)"])
    add("c", "uo", "cuo", examples=["错 (cuò - sai/lỗi)"])
    add("c", "ui", "cui", note="Vận mẫu uei viết gọn thành ui.", examples=["催 (cuī - thúc giục)"])
    add("c", "uan", "cuan", examples=["窜 (cuàn - chạy trốn)"])
    add("c", "un", "cun", note="Vận mẫu uen viết gọn thành un.", examples=["村 (cūn - ngôi làng)", "存 (cún - tiết kiệm)"])

    # ── s ─────────────────────────────────────────────────────────────────────
    add("s", "a", "sa", examples=["洒 (sǎ - tưới nước)"])
    add("s", "e", "se", examples=["色 (sè - màu sắc)"])
    add("s", "i", "si", note="Thanh mẫu s khi đi với i phát âm đầu lưỡi răng [sī].", examples=["四 (sì - số 4)", "死 (sǐ - chết)", "司 (sī - công ty)"])
    add("s", "ai", "sai", examples=["赛 (sài - thi đấu)"])
    add("s", "ao", "sao", examples=["扫 (sǎo - quét nhà)"])
    add("s", "ou", "sou", examples=["搜 (sōu - tìm kiếm)"])
    add("s", "an", "san", examples=["三 (sān - số 3)", "散 (sàn - tản ra)"])
    add("s", "en", "sen", examples=["森 (sēn - rừng rậm)"])
    add("s", "ang", "sang", examples=["桑 (sāng - cây dâu tằm)"])
    add("s", "eng", "seng", examples=["僧 (sēng - nhà sư)"])
    add("s", "ong", "song", examples=["送 (sòng - tặng/tiễn)", "松 (sōng - lỏng)"])
    add("s", "u", "su", examples=["宿 (sù - túc xá)", "速 (sù - tốc độ)"])
    add("s", "uo", "suo", examples=["所 (suǒ - sở/nơi)", "锁 (suǒ - cái khóa)"])
    add("s", "ui", "sui", note="Vận mẫu uei viết gọn thành ui.", examples=["岁 (suì - tuổi)", "随 (suí - tùy theo)"])
    add("s", "uan", "suan", examples=["算 (suàn - tính toán)", "酸 (suān - chua)"])
    add("s", "un", "sun", note="Vận mẫu uen viết gọn thành un.", examples=["孙 (sūn - cháu trai)"])

    # ── (Không có) - ÂM TIẾT ĐỘC LẬP (零声母) ───────────────────────────────────
    z = "(Không có)"
    add(z, "a", "a", examples=["啊 (a - từ cảm thán)"])
    add(z, "o", "o", examples=["哦 (ó - ồ)"])
    add(z, "e", "e", examples=["鹅 (é - con ngỗng)", "饿 (è - đói bụng)"])
    add(z, "er", "er", note="Vận mẫu uốn lưỡi đặc biệt er đứng một mình.", examples=["二 (èr - số 2)", "儿 (ér - con trai)"])
    add(z, "ai", "ai", examples=["爱 (ài - tình yêu)", "矮 (ǎi - thấp)"])
    add(z, "ei", "ei", examples=["诶 (ēi - này)"])
    add(z, "ao", "ao", examples=["熬 (áo - ninh/nấu)", "傲 (ào - kiêu ngạo)"])
    add(z, "ou", "ou", examples=["偶 (ǒu - ngẫu nhiên)", "欧 (ōu - châu Âu)"])
    add(z, "an", "an", examples=["安 (ān - bình an)", "暗 (àn - tối tăm)"])
    add(z, "en", "en", examples=["恩 (ēn - ân nghĩa)"])
    add(z, "ang", "ang", examples=["昂 (áng - ngẩng cao)"])
    add(z, "eng", "eng", examples=["鞥 (ēng - dây cương)"])

    # Vận mẫu bắt đầu bằng i khi đứng một mình:
    add(z, "i", "yi", note="Quy tắc: i đứng một mình viết thêm y thành 'yi'.", examples=["一 (yī - số 1)", "衣 (yī - quần áo)"])
    add(z, "ia", "ya", note="Quy tắc: ia đứng đầu biến i thành y: 'ya'.", examples=["鸭 (yā - con vịt)", "牙 (yá - cái răng)"])
    add(z, "ie", "ye", note="Quy tắc: ie đứng đầu biến i thành y: 'ye'.", examples=["也 (yě - cũng)", "夜 (yè - ban đêm)"])
    add(z, "iao", "yao", note="Quy tắc: iao đứng đầu biến i thành y: 'yao'.", examples=["要 (yào - muốn/phải)", "药 (yào - thuốc)"])
    add(z, "iu", "you", note="Quy tắc: iu gốc là iou, khi đứng một mình viết thành 'you'.", examples=["有 (yǒu - có)", "友 (yǒu - bạn bè)"])
    add(z, "ian", "yan", note="Quy tắc: ian đứng đầu biến i thành y: 'yan'.", examples=["眼 (yǎn - mắt)", "言 (yán - ngôn ngữ)"])
    add(z, "in", "yin", note="Quy tắc: in đứng một mình thêm y thành 'yin'.", examples=["音 (yīn - âm thanh)", "银 (yín - bạc)"])
    add(z, "iang", "yang", note="Quy tắc: iang đứng đầu biến i thành y: 'yang'.", examples=["羊 (yáng - con cừu)", "样 (yàng - dáng vẻ)"])
    add(z, "ing", "ying", note="Quy tắc: ing đứng một mình thêm y thành 'ying'.", examples=["英 (yīng - nước Anh)", "影 (yǐng - bóng/phim)"])
    add(z, "iong", "yong", note="Quy tắc: iong đứng đầu biến i thành y: 'yong'.", examples=["用 (yòng - dùng)", "勇 (yǒng - dũng cảm)"])

    # Vận mẫu bắt đầu bằng u khi đứng một mình:
    add(z, "u", "wu", note="Quy tắc: u đứng một mình viết thêm w thành 'wu'.", examples=["五 (wǔ - số 5)", "屋 (wū - căn phòng)"])
    add(z, "ua", "wa", note="Quy tắc: ua đứng đầu biến u thành w: 'wa'.", examples=["袜 (wà - đôi tất)", "蛙 (wā - con ếch)"])
    add(z, "uo", "wo", note="Quy tắc: uo đứng đầu biến u thành w: 'wo'.", examples=["我 (wǒ - tôi)", "握 (wò - nắm lấy)"])
    add(z, "uai", "wai", note="Quy tắc: uai đứng đầu biến u thành w: 'wai'.", examples=["外 (wài - bên ngoài)"])
    add(z, "ui", "wei", note="Quy tắc: ui gốc là uei, khi đứng một mình viết thành 'wei'.", examples=["为 (wèi - vì)", "位 (wèi - vị trí)"])
    add(z, "uan", "wan", note="Quy tắc: uan đứng đầu biến u thành w: 'wan'.", examples=["万 (wàn - vạn/mười nghìn)", "玩 (wán - chơi)"])
    add(z, "un", "wen", note="Quy tắc: un gốc là uen, khi đứng một mình viết thành 'wen'.", examples=["文 (wén - văn học)", "问 (wèn - hỏi)"])
    add(z, "uang", "wang", note="Quy tắc: uang đứng đầu biến u thành w: 'wang'.", examples=["王 (wáng - họ Vương)", "网 (wǎng - mạng)"])
    add(z, "ueng", "weng", note="Quy tắc: ueng đứng đầu biến u thành w: 'weng'.", examples=["翁 (wēng - ông già)"])

    # Vận mẫu bắt đầu bằng ü khi đứng một mình:
    add(z, "ü", "yu", note="Quy tắc: ü đứng một mình viết thêm y và bỏ 2 dấu chấm thành 'yu'.", examples=["雨 (yǔ - cơn mưa)", "鱼 (yú - con cá)"])
    add(z, "üe", "yue", note="Quy tắc: üe đứng đầu thêm y và bỏ 2 dấu chấm thành 'yue'.", examples=["月 (yuè - mặt trăng/tháng)"])
    add(z, "üan", "yuan", note="Quy tắc: üan đứng đầu thêm y và bỏ 2 dấu chấm thành 'yuan'.", examples=["元 (yuán - tệ)", "远 (yuǎn - xa xôi)"])
    add(z, "ün", "yun", note="Quy tắc: ün đứng đầu thêm y và bỏ 2 dấu chấm thành 'yun'.", examples=["云 (yún - mây)", "运 (yùn - vận chuyển)"])

    return combos

VALID_COMBINATIONS = _build_valid_combinations()


# ─────────────────────────────────────────────────────────────────────────────
# 3. HÀM GẮN DẤU THANH ĐIỆU (TONE PLACEMENT RULE)
# ─────────────────────────────────────────────────────────────────────────────

def add_tone(syllable, tone_idx):
    """
    Gắn dấu thanh điệu chuẩn tiếng Trung (Quy tắc ưu tiên a > o > e > i > u > ü).
    tone_idx: 1 (¯), 2 (ˊ), 3 (ˇ), 4 (ˋ), 0 (thanh nhẹ - giữ nguyên)
    """
    if tone_idx == 0:
        return syllable

    tone_marks = {
        'a': ['ā', 'á', 'ǎ', 'à'],
        'o': ['ō', 'ó', 'ǒ', 'ò'],
        'e': ['ē', 'é', 'ě', 'è'],
        'i': ['ī', 'í', 'ǐ', 'ì'],
        'u': ['ū', 'ú', 'ǔ', 'ù'],
        'ü': ['ǖ', 'ǘ', 'ǚ', 'ǜ'],
    }

    s = syllable
    # 1. Ưu tiên a > o > e
    for v in ['a', 'o', 'e']:
        if v in s:
            return s.replace(v, tone_marks[v][tone_idx - 1], 1)

    # 2. Cặp đặc biệt: 'iu', 'ui' -> đánh dấu lên nguyên âm đứng sau
    if 'iu' in s:
        return s.replace('u', tone_marks['u'][tone_idx - 1], 1)
    if 'ui' in s:
        return s.replace('i', tone_marks['i'][tone_idx - 1], 1)

    # 3. Còn lại i, u, ü
    for v in ['i', 'u', 'ü']:
        if v in s:
            return s.replace(v, tone_marks[v][tone_idx - 1], 1)

    return s


# ─────────────────────────────────────────────────────────────────────────────
# 4. HÀM GIẢI THÍCH LÝ DO KHÔNG TỒN TẠI TỔ HỢP
# ─────────────────────────────────────────────────────────────────────────────

def get_invalid_explanation(init, final):
    """Đưa ra giải thích chi tiết, dễ hiểu vì sao tổ hợp này không có trong tiếng Trung."""
    # Nhóm j, q, x + u thường
    if init in ["j", "q", "x"]:
        if final in ["u", "ua", "uo", "uai", "ui", "uan", "un", "uang"]:
            return (
                f"💡 **Quy tắc quan trọng của nhóm mặt lưỡi (j, q, x):**\n\n"
                f"- Các thanh mẫu **j, q, x** **KHÔNG BAO GIỜ** kết hợp với nguyên âm [u] thường!\n"
                f"- Khi bạn nhìn thấy chữ viết là *ju, qu, xu*, thực chất đó là kết hợp với **ü** tròn môi (nhưng đã được lược bỏ 2 dấu chấm theo quy tắc chính tả).\n"
                f"- 👉 Hãy thử chọn vận mẫu **ü**, **üe**, **üan**, hoặc **ün**!"
            )
        elif final in ["a", "o", "e", "ai", "ei", "ao", "ou", "an", "en", "ang", "eng", "ong"]:
            return (
                f"💡 Nhóm thanh mẫu mặt lưỡi **{init}** chỉ kết hợp với các vận mẫu thuộc **hàng i** (i, ia, ie, iao, iu, ian, in, iang, ing, iong) "
                f"và **hàng ü** (ü, üe, üan, ün). Hoàn toàn không đi với các vận mẫu mở rộng hàng a, o, e!"
            )

    # Nhóm âm môi b, p, m, f
    if init in ["b", "p", "m", "f"]:
        if final in ["ua", "uo", "uai", "ui", "uan", "un", "uang"]:
            return f"💡 Thanh mẫu âm môi **{init}** không kết hợp với các vận mẫu phức hợp hàng u ({final})."
        if final in ["ia", "iong", "iang"]:
            return f"💡 Thanh mẫu **{init}** không đi cùng vận mẫu {final}."
        if final in ["ü", "üe", "üan", "ün"]:
            return f"💡 Thanh mẫu âm môi **{init}** không bao giờ kết hợp với nguyên âm tròn môi [ü]!"
        if init == "f" and final in ["i", "ie", "in", "ing", "ai", "ao"]:
            return "💡 Thanh mẫu **f** là âm môi-răng, chỉ kết hợp với các vận mẫu: a, o, u, ei, ou, an, en, ang, eng. Không kết hợp với hàng i hay ü!"

    # Nhóm cuống lưỡi g, k, h và uốn lưỡi zh, ch, sh, r và răng z, c, s
    if init in ["g", "k", "h", "zh", "ch", "sh", "r", "z", "c", "s"]:
        if final in ["ü", "üe", "üan", "ün"]:
            return f"💡 Thanh mẫu **{init}** không bao giờ kết hợp với nguyên âm tròn môi **[ü]** (chỉ có j, q, x, n, l mới đi với ü)!"
        if init in ["g", "k", "h"] and final in ["i", "ia", "ie", "iao", "iu", "ian", "in", "iang", "ing", "iong"]:
            return f"💡 Thanh mẫu cuống lưỡi **{init}** không kết hợp với bất kỳ vận mẫu nào thuộc hàng **i**!"

    # Nhóm r
    if init == "r" and final in ["a", "o", "ai", "ei"]:
        return "💡 Thanh mẫu **r** không kết hợp với các nguyên âm đơn a, o hoặc nhị trùng âm ai, ei."

    # Âm tiết độc lập er
    if final == "er" and init != "(Không có)":
        return "💡 Vận mẫu uốn lưỡi **er** là vận mẫu đặc biệt, **chỉ đứng một mình** độc lập chứ không bao giờ ghép với thanh mẫu nào!"

    return f"Trong bảng phiên âm ngữ âm chuẩn tiếng Hán (Hán ngữ hiện đại), không có sự kết hợp giữa thanh mẫu **'{init}'** và vận mẫu **'{final}'**."


# ─────────────────────────────────────────────────────────────────────────────
# 5. GIAO DIỆN CHÍNH (STREAMLIT PAGE)
# ─────────────────────────────────────────────────────────────────────────────

def show_pinyin_practice():
    inject_tts_to_parent()

    # ── Header phong cách Studio ─────────────────────────────────────────────
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
                border-radius: 16px; padding: 24px 28px; margin-bottom: 24px;
                color: #ffffff; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.2);">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
            <div>
                <h2 style="margin: 0; font-size: 1.7rem; font-weight: 800; color: #f8fafc; letter-spacing: -0.5px;">
                    🎙️ Phòng Ghép Âm & Luyện Phát Âm Pinyin
                </h2>
                <p style="margin: 6px 0 0; color: #94a3b8; font-size: 0.95rem;">
                    Tự do ghép <b>Thanh mẫu + Vận mẫu + Thanh điệu</b>. Hệ thống tự động kiểm tra quy tắc ngữ âm & phát âm chuẩn tiếng Trung!
                </p>
            </div>
            <div style="background: rgba(59, 130, 246, 0.15); border: 1px solid rgba(59, 130, 246, 0.4);
                        padding: 8px 16px; border-radius: 999px; font-size: 0.85rem; color: #60a5fa; font-weight: 600;">
                ✨ Kiểm tra quy tắc Real-time
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Khối điều khiển chọn Thanh mẫu, Vận mẫu, Thanh điệu ──────────────────
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("#### 1️⃣ Thanh mẫu (声母)")
        selected_initial = st.selectbox(
            "Chọn Thanh mẫu:",
            ALL_INITIALS,
            index=1,
            key="selected_initial_val",
            help="Chọn thanh mẫu (phụ âm đầu) hoặc chọn (Không có) nếu là âm tiết độc lập"
        )

    with c2:
        st.markdown("#### 2️⃣ Vận mẫu (韵母)")
        selected_final = st.selectbox(
            "Chọn Vận mẫu:",
            ALL_FINALS,
            index=0,
            key="selected_final_val",
            help="Chọn vận mẫu (vần) để ghép"
        )

    with c3:
        st.markdown("#### 3️⃣ Thanh điệu (声调)")
        tone_options = [f"{t['mark']} {t['name']}" for t in TONES_DATA]
        selected_tone_label = st.selectbox(
            "Chọn Thanh điệu:",
            tone_options,
            index=0,
            key="selected_tone_val",
            help="Chọn 1 trong 4 thanh điệu hoặc thanh nhẹ"
        )
        selected_tone_idx = next(t["val"] for t in TONES_DATA if f"{t['mark']} {t['name']}" == selected_tone_label)

    st.markdown("<hr style='margin: 20px 0 24px; border: 0; border-top: 1px solid #e2e8f0;'/>", unsafe_allow_html=True)

    # ── XỬ LÝ GHÉP VÀ KIỂM TRA HỢP LỆ ────────────────────────────────────────
    key_pair = (selected_initial, selected_final)
    is_valid = key_pair in VALID_COMBINATIONS

    # Công thức ghép
    init_display = "Ø" if selected_initial == "(Không có)" else selected_initial
    tone_symbol = next(t["mark"] for t in TONES_DATA if t["val"] == selected_tone_idx)

    st.markdown(f"""
    <div style="display: flex; align-items: center; justify-content: center; gap: 14px; margin-bottom: 24px; flex-wrap: wrap;">
        <span style="background: #f1f5f9; padding: 6px 14px; border-radius: 8px; font-weight: 700; color: #334155; font-size: 1.1rem; border: 1px solid #cbd5e1;">
            Thanh mẫu: <b style="color: #2563eb;">{init_display}</b>
        </span>
        <span style="font-size: 1.2rem; font-weight: 800; color: #94a3b8;">+</span>
        <span style="background: #f1f5f9; padding: 6px 14px; border-radius: 8px; font-weight: 700; color: #334155; font-size: 1.1rem; border: 1px solid #cbd5e1;">
            Vận mẫu: <b style="color: #059669;">{selected_final}</b>
        </span>
        <span style="font-size: 1.2rem; font-weight: 800; color: #94a3b8;">+</span>
        <span style="background: #f1f5f9; padding: 6px 14px; border-radius: 8px; font-weight: 700; color: #334155; font-size: 1.1rem; border: 1px solid #cbd5e1;">
            Thanh điệu: <b style="color: #d97706;">{tone_symbol} ({selected_tone_label.split('(')[1].rstrip(')')})</b>
        </span>
    </div>
    """, unsafe_allow_html=True)

    # ─────────────────────────────────────────────────────────────────────────
    # TRƯỜNG HỢP 1: TỔ HỢP HỢP LỆ TRONG TIẾNG TRUNG
    # ─────────────────────────────────────────────────────────────────────────
    if is_valid:
        data = VALID_COMBINATIONS[key_pair]
        base_pinyin = data["pinyin"]
        toned_pinyin = add_tone(base_pinyin, selected_tone_idx)
        rule_note = data.get("note")
        examples = data.get("examples", [])

        # Thẻ kết quả màu xanh ngọc / indigo cao cấp
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%);
                    border: 2px solid #86efac; border-radius: 18px; padding: 28px;
                    box-shadow: 0 10px 30px -10px rgba(16, 185, 129, 0.2); margin-bottom: 24px;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; flex-wrap: wrap; gap: 8px;">
                <span style="display: inline-flex; align-items: center; gap: 6px;
                             background: #dcfce7; color: #15803d; font-weight: 800;
                             padding: 5px 14px; border-radius: 999px; font-size: 0.88rem; border: 1px solid #bbf7d0;">
                    ✓ TỔ HỢP HỢP LỆ TRONG TIẾNG TRUNG
                </span>
                <span style="color: #64748b; font-size: 0.9rem;">
                    Âm tiết chuẩn: <b>{base_pinyin}</b>
                </span>
            </div>
            <div style="text-align: center; padding: 10px 0 20px;">
                <div style="font-size: 4.8rem; font-weight: 900; color: #065f46;
                            font-family: 'Georgia', 'Noto Serif SC', serif; line-height: 1.1;
                            text-shadow: 0 2px 8px rgba(0,0,0,0.05); letter-spacing: 1px;">
                    {toned_pinyin}
                </div>
                <div style="color: #047857; font-size: 1.05rem; font-weight: 600; margin-top: 8px;">
                    {f"Ký hiệu thanh: {tone_symbol} ({selected_tone_label})" if selected_tone_idx != 0 else "Thanh nhẹ (đọc ngắn, nhẹ)"}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Nút bấm phát âm to rõ (dùng postMessage tới TTS parent)
        safe_toned = json.dumps(toned_pinyin, ensure_ascii=False)
        components.html(
            f"""
            {_TTS_JS_CORE}
            <div style="display: flex; justify-content: center; margin: 0 0 16px;">
                <button id="main-speak-btn" onclick="playCurrent()"
                    style="display: inline-flex; align-items: center; justify-content: center; gap: 10px;
                           background: linear-gradient(135deg, #059669 0%, #047857 100%);
                           color: #ffffff; border: none; border-radius: 12px;
                           padding: 14px 32px; font-size: 1.15rem; font-weight: 700;
                           cursor: pointer; box-shadow: 0 6px 18px rgba(5, 150, 105, 0.35);
                           transition: all 0.2s ease; outline: none; font-family: -apple-system, sans-serif;">
                    <span style="font-size: 1.4rem;">🔊</span>
                    <span>NGHE PHÁT ÂM: {toned_pinyin}</span>
                </button>
            </div>
            <script>
            function playCurrent() {{
                const txt = {safe_toned};
                if (window.chineseTTS) {{
                    window.chineseTTS(txt);
                }}
            }}
            </script>
            """,
            height=60,
        )

        # Ghi chú quy tắc chính tả nếu có
        if rule_note:
            st.info(f"📌 **Quy tắc chính tả:** {rule_note}")

        # Bảng 4 thanh điệu của âm tiết này
        st.markdown("#### 🎧 Nghe 4 thanh điệu của âm tiết này:")
        tone_cols = st.columns(4)
        for t_idx in range(1, 5):
            t_syl = add_tone(base_pinyin, t_idx)
            with tone_cols[t_idx - 1]:
                t_info = next(t for t in TONES_DATA if t["val"] == t_idx)
                st.markdown(f"""
                <div style="text-align: center; background: #ffffff; border: 1.5px solid #e2e8f0;
                            border-radius: 12px; padding: 12px 6px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="font-size: 0.8rem; font-weight: 700; color: #64748b;">{t_info['name'].split('(')[0]}</div>
                    <div style="font-size: 1.8rem; font-weight: 800; color: #1e293b; margin: 4px 0; font-family: 'Georgia', serif;">
                        {t_syl}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                # Nút phát âm mini cho từng thanh
                safe_t = json.dumps(t_syl, ensure_ascii=False)
                components.html(
                    f"""
                    {_TTS_JS_CORE}
                    <button onclick="playT()"
                        style="width: 100%; margin-top: 4px; padding: 6px 0; background: #f8fafc;
                               border: 1px solid #cbd5e1; border-radius: 8px; font-size: 0.88rem;
                               color: #047857; font-weight: 700; cursor: pointer; transition: all 0.2s;">
                        🔊 Nghe
                    </button>
                    <script>
                    function playT() {{
                        if (window.chineseTTS) window.chineseTTS({safe_t});
                    }}
                    </script>
                    """,
                    height=38,
                )

        # Chữ Hán ví dụ thông dụng
        if examples:
            st.markdown("#### 📚 Chữ Hán ví dụ thông dụng:")
            ex_html = "".join([
                f"<span style='display:inline-block; background:#ffffff; border:1px solid #e2e8f0; "
                f"border-radius:8px; padding:6px 14px; margin:4px 6px; font-size:0.95rem; color:#1e293b; "
                f"box-shadow:0 1px 3px rgba(0,0,0,0.04);'><b>{ex}</b></span>"
                for ex in examples
            ])
            st.markdown(f"<div style='margin-bottom: 15px;'>{ex_html}</div>", unsafe_allow_html=True)

    # ─────────────────────────────────────────────────────────────────────────
    # TRƯỜNG HỢP 2: TỔ HỢP KHÔNG TỒN TẠI TRONG TIẾNG TRUNG
    # ─────────────────────────────────────────────────────────────────────────
    else:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #fff1f2 0%, #ffe4e6 100%);
                    border: 2px solid #fca5a5; border-radius: 18px; padding: 28px;
                    box-shadow: 0 10px 30px -10px rgba(239, 68, 68, 0.2); margin-bottom: 24px;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <span style="display: inline-flex; align-items: center; gap: 6px;
                             background: #fee2e2; color: #b91c1c; font-weight: 800;
                             padding: 5px 14px; border-radius: 999px; font-size: 0.88rem; border: 1px solid #fecaca;">
                    ✕ TỔ HỢP NÀY KHÔNG TỒN TẠI TRONG TIẾNG TRUNG
                </span>
                <span style="color: #991b1b; font-size: 0.9rem; font-weight: 600;">
                    Không có âm: <b>{init_display}{selected_final}</b>
                </span>
            </div>
            <div style="text-align: center; padding: 15px 0;">
                <div style="font-size: 3.8rem; font-weight: 900; color: #dc2626;
                            font-family: 'Georgia', serif; text-decoration: line-through;
                            text-decoration-color: #ef4444; opacity: 0.7;">
                    {init_display}{selected_final}
                </div>
                <div style="color: #991b1b; font-size: 1.15rem; font-weight: 700; margin-top: 12px;">
                    ⚠️ Không thể phát âm vì đây là âm tiết không hợp lệ trong tiếng Hán chuẩn!
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Giải thích chi tiết nguyên nhân
        explanation = get_invalid_explanation(selected_initial, selected_final)
        st.warning(explanation)

        # Gợi ý các vận mẫu hợp lệ mà thanh mẫu này CÓ THỂ kết hợp được
        valid_finals_for_initial = [
            f for (i, f) in VALID_COMBINATIONS.keys()
            if i == selected_initial
        ]

        if valid_finals_for_initial:
            st.markdown(f"#### 💡 Thanh mẫu **'{init_display}'** CÓ THỂ kết hợp với các vận mẫu sau:")
            chips_html = "".join([
                f"<span style='display:inline-block; background:#eff6ff; border:1px solid #bfdbfe; "
                f"color:#1d4ed8; font-weight:700; border-radius:8px; padding:6px 12px; margin:4px; "
                f"font-size:0.92rem; font-family:monospace;'>{f} ➔ <b>{VALID_COMBINATIONS[(selected_initial, f)]['pinyin']}</b></span>"
                for f in valid_finals_for_initial
            ])
            st.markdown(f"<div style='margin-top: 10px; margin-bottom: 20px;'>{chips_html}</div>", unsafe_allow_html=True)
            st.caption("👉 Hãy chọn một trong các vận mẫu gợi ý phía trên để ghép thành âm tiết hợp lệ!")
