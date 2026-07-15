# -*- coding: utf-8 -*-
import streamlit as st
import random
import csv
from datetime import datetime, timezone, timedelta
from ui_utils import render_lesson_intro, render_play_button

# DANH SÁCH 30 CÂU HỎI TRẮC NGHIỆM TỔNG HỢP HSK 1
HSK1_QUESTIONS = [
    {
        "question": "Chọn động từ phù hợp: “他正在_____电话。”",
        "pinyin": "Tā zhèngzài _____ diànhuà.",
        "choices": [
            "A. 写 (xiě)",
            "B. 听 (tīng)",
            "C. 打 (dǎ)",
            "D. 做 (zuò)"
        ],
        "answer": "C. 打 (dǎ)",
        "explain": "Cụm từ '打电话' (dǎ diànhuà) có nghĩa là 'gọi điện thoại'. Động từ '打' là phù hợp nhất.",
        "sound_txt": "他正在打电话。"
    },
    {
        "question": "Chọn đại từ nghi vấn phù hợp: “昨天北京的天气_____？”",
        "pinyin": "Zuótiān Běijīng de tiānqì _____?",
        "choices": [
            "A. 怎么 (zěnme)",
            "B. 怎么样 (zěnmeyàng)",
            "C. 几 (jǐ)",
            "D. 多少 (duōshao)"
        ],
        "answer": "B. 怎么样 (zěnmeyàng)",
        "explain": "Để hỏi về tình trạng hoặc tính chất (thời tiết như thế nào), ta dùng đại từ nghi vấn '怎么样' (zěnmeyàng) đứng ở cuối câu.",
        "sound_txt": "昨天北京的天气怎么样？"
    },
    {
        "question": "Chọn từ thích hợp điền vào chỗ trống: “我家有_____口人。”",
        "pinyin": "Wǒ jiā yǒu _____ kǒu rén.",
        "choices": [
            "A. 几 (jǐ)",
            "B. 多少 (duōshao)",
            "C. 什么 (shénme)",
            "D. 谁 (shéi)"
        ],
        "answer": "A. 几 (jǐ)",
        "explain": "Hỏi số lượng thành viên trong gia đình (thường ít hơn 10) dùng '几' (jǐ). Cấu trúc: 几 + lượng từ (口) + danh từ (人).",
        "sound_txt": "我家有几口人？"
    },
    {
        "question": "Chọn từ để hỏi thích hợp: “这是_____的电脑？” (Đây là máy tính của ai?)",
        "pinyin": "Zhè shì _____ de diànnǎo?",
        "choices": [
            "A. 谁 (shéi)",
            "B. 什么 (shénme)",
            "C. 哪儿 (nǎr)",
            "D. 几 (jǐ)"
        ],
        "answer": "A. 谁 (shéi)",
        "explain": "Để hỏi về chủ sở hữu ('của ai'), ta dùng đại từ '谁' (shéi - ai).",
        "sound_txt": "这是谁的电脑？"
    },
    {
        "question": "Chọn từ phủ định phù hợp: “他_____是学生，他是老师。”",
        "pinyin": "Tā _____ shì xuéshēng, tā shì lǎoshī.",
        "choices": [
            "A. 不 (bù)",
            "B. 没 (méi)",
            "C. 没有 (méiyǒu)",
            "D. 的 (de)"
        ],
        "answer": "A. 不 (bù)",
        "explain": "Phủ định của động từ liên hệ '是' (là) là '不是' (bú shì - không phải là). Lưu ý biến điệu đọc thành 'bú' khi đi trước thanh 4.",
        "sound_txt": "他不是学生，他是老师。"
    },
    {
        "question": "Chọn phó từ chỉ mức độ phù hợp: “那个女生_____漂亮。”",
        "pinyin": "Nàge nǚshēng _____ piàoliang.",
        "choices": [
            "A. 是 (shì)",
            "B. 的 (de)",
            "C. 很 (hěn)",
            "D. 有 (yǒu)"
        ],
        "answer": "C. 很 (hěn)",
        "explain": "Trong câu miêu tả tính từ, phó từ chỉ mức độ '很' (hěn) đứng trước tính từ làm vị ngữ để liên kết câu trần thuật.",
        "sound_txt": "那个女生很漂亮。"
    },
    {
        "question": "Chọn giới từ phù hợp: “我爸爸_____在医院工作。” (Bố tôi làm việc ở bệnh viện.)",
        "pinyin": "Wǒ bàba _____ yīyuàn gōngzuò.",
        "choices": [
            "A. 是 (shì)",
            "B. 有 (yǒu)",
            "C. 在 (zài)",
            "D. 去 (qù)"
        ],
        "answer": "C. 在 (zài)",
        "explain": "Giới từ '在' (zài - ở) đứng trước từ chỉ địa điểm để biểu thị hành động diễn ra tại địa điểm đó.",
        "sound_txt": "我爸爸在医院工作。"
    },
    {
        "question": "Chọn lượng từ phù hợp: “爸爸去商店买一个_____。”",
        "pinyin": "Bàba qù shāngdiàn mǎi yí gè _____.",
        "choices": [
            "A. 杯子 (bēizi)",
            "B. 衣服 (yīfu)",
            "C. 猫 (māo)",
            "D. 书 (shū)"
        ],
        "answer": "A. 杯子 (bēizi)",
        "explain": "Lượng từ '个' (gè) phù hợp đi kèm với các danh từ như '杯子' (cái cốc), '苹果' (quả táo). Các danh từ khác dùng lượng từ khác (件衣服, 只猫, 本书).",
        "sound_txt": "爸爸去商店买一个杯子。"
    },
    {
        "question": "Chọn từ vựng phù hợp: “认识你，我很高_____。”",
        "pinyin": "Rènshi nǐ, wǒ hěn gāo_____.",
        "choices": [
            "A. 忙 (máng)",
            "B. 兴 (xìng)",
            "C. 累 (lèi)",
            "D. 热 (rè)"
        ],
        "answer": "B. 兴 (xìng)",
        "explain": "Cụm từ '高兴' (gāoxìng) nghĩa là vui vẻ, mừng rỡ. Câu giao tiếp chuẩn: '认识你，我很高兴。' (Rất vui được quen biết bạn).",
        "sound_txt": "认识你，我很高兴。"
    },
    {
        "question": "Chọn từ phủ định phù hợp: “因为他今天_____舒服，so 没来。”",
        "pinyin": "Yīnwèi tā jīntiān _____ shūfu, suǒyǐ méi lái.",
        "choices": [
            "A. 不 (bù)",
            "B. 没 (méi)",
            "C. 没有 (méiyǒu)",
            "D. 是 (shì)"
        ],
        "answer": "A. 不 (bù)",
        "explain": "Phủ định tính từ/trạng thái '舒服' (shūfu - khỏe, thoải mái) ta dùng phó từ '不' (bù).",
        "sound_txt": "因为 he 今天不舒服，所以没来。"
    },
    {
        "question": "Chọn động từ thích hợp: “我_____一个女儿。” (Tôi có một người con gái.)",
        "pinyin": "Wǒ _____ yí gè nǚ'ér.",
        "choices": [
            "A. 是 (shì)",
            "B. 有 (yǒu)",
            "C. 去 (qù)",
            "D. 叫 (jiào)"
        ],
        "answer": "B. 有 (yǒu)",
        "explain": "Động từ '有' (yǒu - có) biểu thị sự sở hữu hoặc quan hệ gia đình (có con gái).",
        "sound_txt": "我有一个女儿。"
    },
    {
        "question": "Chọn từ chỉ định phù hợp: “______ 苹果很大，那个苹果很小。” (Quả táo này rất to...)",
        "pinyin": "______ píngguǒ hěn dà, nàge píngguǒ hěn xiǎo.",
        "choices": [
            "A. 这个 (zhège)",
            "B. 那个 (nàge)",
            "C. 哪个 (nǎge)",
            "D. 几口 (jǐkǒu)"
        ],
        "answer": "A. 这个 (zhège)",
        "explain": "Để chỉ vật ở cự ly gần ('này'), ta dùng '这个' (zhège) đối lập với '那个' (nàge) ở cự ly xa ('kia').",
        "sound_txt": "这个苹果很大，那个苹果很小。"
    },
    {
        "question": "Chọn trợ từ ngữ khí phù hợp: “现在的天气太热_____。”",
        "pinyin": "Xiànzài de tiānqì tài rè _____.",
        "choices": [
            "A. 吗 (ma)",
            "B. 呢 (ne)",
            "C. 了 (le)",
            "D. 的 (de)"
        ],
        "answer": "C. 了 (le)",
        "explain": "Trợ từ ngữ khí '了' (le) thường đi kèm cấu trúc cảm thán '太...了' (tài ... le - quá... rồi).",
        "sound_txt": "现在的天气太热了。"
    },
    {
        "question": "Chọn danh từ chỉ phương vị phù hợp: “书在桌子_____。” (Sách ở trên bàn.)",
        "pinyin": "Shū zài zhuōzi _____.",
        "choices": [
            "A. 上 (shàng)",
            "B. 下 (xià)",
            "C. 里 (lǐ)",
            "D. 前 (qián)"
        ],
        "answer": "A. 上 (shàng)",
        "explain": "Phương vị từ '上' (shàng - trên) đứng sau danh từ '桌子' chỉ vị trí phía trên cái bàn.",
        "sound_txt": "书在桌子上。"
    },
    {
        "question": "Chọn động từ năng nguyện phù hợp: “哥哥会_____汉语。”",
        "pinyin": "Gēge huì _____ Hànyǔ.",
        "choices": [
            "A. 说 (shuō)",
            "B. 写 (xiě)",
            "C. 听 (tīng)",
            "D. 读 (dú)"
        ],
        "answer": "A. 说 (shuō)",
        "explain": "Động từ '说' (shuō - nói) thường dùng để biểu thị khả năng giao tiếp bằng một ngôn ngữ (说汉语 - nói tiếng Trung).",
        "sound_txt": "哥哥会说汉语。"
    },
    {
        "question": "Chọn đại từ nghi vấn phù hợp: “你要买_____苹果？” (Bạn muốn mua quả táo nào?)",
        "pinyin": "Nǐ yào mǎi _____ píngguǒ?",
        "choices": [
            "A. 哪个 (nǎge)",
            "B. 这个 (zhège)",
            "C. 那个 (nàge)",
            "D. 什么 (shénme)"
        ],
        "answer": "A. 哪个 (nǎge)",
        "explain": "Để hỏi lựa chọn ('nào', 'cái nào'), ta dùng đại từ nghi vấn chỉ định '哪个' (nǎge).",
        "sound_txt": "你要哪个苹果？"
    },
    {
        "question": "Chọn phó từ phủ định thích hợp: “昨天下午_____下雨。” (Chiều qua không mưa.)",
        "pinyin": "Zuótiān xiàwǔ _____ xiàyǔ.",
        "choices": [
            "A. 不 (bù)",
            "B. 没 (méi)",
            "C. 没有 (méiyǒu)",
            "D. 是 (shì)"
        ],
        "answer": "C. 没有 (méiyǒu)",
        "explain": "Để phủ định hành động đã xảy ra hoặc trạng thái trong quá khứ, ta dùng '没有' (méiyǒu) hoặc '没' (méi).",
        "sound_txt": "昨天下午没有下雨。"
    },
    {
        "question": "Chọn từ để hỏi phù hợp: “我不认识他，他是_____？”",
        "pinyin": "Wǒ bù rènshi tā, tā shì _____?",
        "choices": [
            "A. 谁 (shéi)",
            "B. 什么 (shénme)",
            "C. 哪儿 (nǎr)",
            "D. 几 (jǐ)"
        ],
        "answer": "A. 谁 (shéi)",
        "explain": "Đại từ nghi vấn '谁' (shéi/shuí - ai) dùng để hỏi về danh tính của một người.",
        "sound_txt": "我不认识他，他是谁？"
    },
    {
        "question": "Chọn trợ từ nghi vấn phù hợp: “你喜欢吃中国菜_____？”",
        "pinyin": "Nǐ xǐhuan chī Zhōngguócài _____?",
        "choices": [
            "A. 吗 (ma)",
            "B. 呢 (ne)",
            "C. 的 (de)",
            "D. 了 (le)"
        ],
        "answer": "A. 吗 (ma)",
        "explain": "Trợ từ nghi vấn '吗' (ma) đứng ở cuối câu trần thuật để biến câu đó thành câu hỏi Có/Không (Yes/No).",
        "sound_txt": "你喜欢吃中国菜吗？"
    },
    {
        "question": "Chọn từ vựng phù hợp: “他是我的_____。” (Anh ấy là thầy giáo dạy tiếng Trung của tôi.)",
        "pinyin": "Tā shì wǒ de _____.",
        "choices": [
            "A. 汉语老师 (Hànyǔ lǎoshī)",
            "B. 学生 (xuéshēng)",
            "C. 朋友 (péngyou)",
            "D. 医生 (yīshēng)"
        ],
        "answer": "A. 汉语老师 (Hànyǔ lǎoshī)",
        "explain": "Cụm từ '汉语老师' (Hànyǔ lǎoshī) nghĩa là thầy/cô giáo dạy tiếng Trung.",
        "sound_txt": "他是我的汉语老师。"
    },
    {
        "question": "Chọn cách viết Pinyin đúng luật chính tả cho âm tiết 'i' khi đứng độc lập:",
        "pinyin": "Quy tắc viết Bính âm cho nguyên âm 'i':",
        "choices": [
            "A. yi",
            "B. i",
            "C. wi",
            "D. y"
        ],
        "answer": "A. yi",
        "explain": "Khi nguyên âm 'i' đứng một mình tạo thành âm tiết độc lập, ta phải thêm bán nguyên âm 'y' phía trước, viết thành 'yi' nhưng phát âm vẫn là 'i'.",
        "sound_txt": "yi"
    },
    {
        "question": "Chọn cách phát âm đúng của nguyên âm 'i' trong từ '四' (sì - số bốn):",
        "pinyin": "Cách phát âm 'i' trong 'sì':",
        "choices": [
            "A. Đọc là 'i' như tiếng Việt",
            "B. Đọc là 'ư' như tiếng Việt",
            "C. Đọc là 'u' tròn môi",
            "D. Đọc là 'ơ'"
        ],
        "answer": "B. Đọc là 'ư' như tiếng Việt",
        "explain": "Khi nguyên âm 'i' đi sau các thanh mẫu đầu lưỡi-răng (z, c, s) và uốn lưỡi (zh, ch, sh, r), nó bắt buộc phát âm biến thành âm 'ư' của tiếng Việt.",
        "sound_txt": "sì"
    },
    {
        "question": "Chọn cách biến điệu đúng của từ '不' (bù) trong câu '他不是学生。':",
        "pinyin": "Biến điệu của 'bù' trong 'bù shì':",
        "choices": [
            "A. Đọc là 'bù' (giữ nguyên thanh 4)",
            "B. Đọc là 'bú' (biến thành thanh 2)",
            "C. Đọc là 'bù' nhưng viết là 'bú'",
            "D. Đọc là 'bǔ' (thanh 3)"
        ],
        "answer": "B. Đọc là 'bú' (biến thành thanh 2)",
        "explain": "Khi phó từ phủ định '不' (bù) đứng trước một từ mang thanh 4 (như 是 - shì), nó phải biến âm đọc thành thanh 2 là 'bú' (nhưng Bính âm tiêu chuẩn vẫn có thể ghi là bù hoặc ghi theo giọng đọc thực tế).",
        "sound_txt": "bú shì"
    },
    {
        "question": "Chọn cách viết đúng luật chính tả khi nguyên âm 'ü' đi sau thanh mẫu 'q':",
        "pinyin": "Quy tắc lược bỏ dấu chấm của 'ü' sau 'q':",
        "choices": [
            "A. Bắt buộc giữ nguyên hai dấu chấm (qü)",
            "B. Lược bỏ hai dấu chấm trên đầu (qu) nhưng vẫn đọc tròn môi 'ü'",
            "C. Thay ü bằng u và đọc giống u thường (qu)",
            "D. Thêm y phía trước (qyu)"
        ],
        "answer": "B. Lược bỏ hai dấu chấm trên đầu (qu) nhưng vẫn đọc tròn môi 'ü'",
        "explain": "Khi nguyên âm tròn môi 'ü' đi sau j, q, x, y, ta bỏ hai dấu chấm trên đầu khi viết (viết là ju, qu, xu, yu) nhưng vẫn phát âm tròn môi là 'ü'.",
        "sound_txt": "qu"
    },
    {
        "question": "Chọn từ vựng chỉ Nữ giới dùng trong quan hệ gia đình (con gái của ai đó):",
        "pinyin": "Từ vựng chỉ con gái ruột trong gia đình:",
        "choices": [
            "A. 女生 (nǚshēng)",
            "B. 女孩 (nǚhái)",
            "C. 女儿 (nǚ'ér)",
            "D. 女性 (nǚxìng)"
        ],
        "answer": "C. 女儿 (nǚ'ér)",
        "explain": "Để chỉ mối quan hệ gia đình (con gái của bố mẹ), tiếng Trung dùng từ '女儿' (nǚ'ér). Các từ khác chỉ giới tính hoặc nhóm xã hội ngoài gia đình.",
        "sound_txt": "女儿"
    },
    {
        "question": "Chọn câu dịch đúng nhất cho câu: “Hôm nay thời tiết rất tốt.”",
        "pinyin": "Dịch câu: “Hôm nay thời tiết rất tốt.”",
        "choices": [
            "A. 今天天气很好。 (Jīntiān tiānqì hěn hǎo.)",
            "B. 昨天天气很好。 (Zuótiān tiānqì hěn hǎo.)",
            "C. 今天天气不冷。 (Jīntiān tiānqì bù lěng.)",
            "D. 明天天气很好。 (Míngtiān tiānqì hěn hǎo.)"
        ],
        "answer": "A. 今天天气很好。 (Jīntiān tiānqì hěn hǎo.)",
        "explain": "'Hôm nay' là 今天 (jīntiān), 'thời tiết' là 天气 (tiānqì), 'rất tốt' là 很好 (hěn hǎo).",
        "sound_txt": "今天天气很好。"
    },
    {
        "question": "Chọn câu dịch đúng nhất cho câu: “Bạn tên là gì?”",
        "pinyin": "Dịch câu: “Bạn tên là gì?”",
        "choices": [
            "A. 你叫什么名字？ (Nǐ jiào shénme míngzi?)",
            "B. 这是什么名字？ (Zhè shì shénme míngzi?)",
            "C. 他叫什么名字？ (Tā jiào shénme míngzi?)",
            "D. 你叫谁的名字？ (Nǐ jiào shéi de míngzi?)"
        ],
        "answer": "A. 你叫什么名字？ (Nǐ jiào shénme míngzi?)",
        "explain": "Cấu trúc hỏi tên chuẩn và phổ biến nhất trong tiếng Trung giao tiếp là '你叫什么名字？' (Nǐ jiào shénme míngzi?).",
        "sound_txt": "你叫什么名字？"
    },
    {
        "question": "Chọn số đếm phù hợp: “我买_____个苹果。” (Tôi mua 3 quả táo.)",
        "pinyin": "Wǒ mǎi _____ gè píngguǒ.",
        "choices": [
            "A. 三 (sān)",
            "B. 四 (sì)",
            "C. 五 (wǔ)",
            "D. 六 (liù)"
        ],
        "answer": "A. 三 (sān)",
        "explain": "Số 3 trong tiếng Trung viết là '三' (sān). Cụm lượng từ: 三个苹果 (sān gè píngguǒ).",
        "sound_txt": "我买三个苹果。"
    },
    {
        "question": "Chọn từ vựng phù hợp: “他是_____，不是学生。” (Anh ấy là luật sư, không phải học sinh.)",
        "pinyin": "Tā shì _____ , bú shì xuéshēng.",
        "choices": [
            "A. 老师 (lǎoshī)",
            "B. 医生 (yīshēng)",
            "C. 律师 (lǜshī)",
            "D. 朋友 (péngyou)"
        ],
        "answer": "C. 律师 (lǜshī)",
        "explain": "'Luật sư' trong tiếng Trung là '律师' (lǜshī).",
        "sound_txt": "他是律师，不是学生。"
    },
    {
        "question": "Chọn câu phản hồi phù hợp nhất: 'A: Nǐ xǐhuan nǎge bēizi? - B: ______'",
        "pinyin": "A: Nǐ xǐhuan nǎge bēizi? (Bạn thích cái cốc nào?) - B: ______",
        "choices": [
            "A. 我喜欢这个。 (Wǒ xǐhuan zhège.)",
            "B. 那个杯子十块钱。 (Nàge bēizi shí kuài qián.)",
            "C. 这是我的电脑。 (Zhè shì wǒ de diànnǎo.)",
            "D. 我没有杯子。 (Wǒ méiyǒu bēizi.)"
        ],
        "answer": "A. 我喜欢这个。 (Wǒ xǐhuan zhège.)",
        "explain": "Khi đối phương hỏi lựa chọn '哪个' (nào), câu trả lời thích hợp nhất là chọn một đối tượng cụ thể như '这个' (cái này) hoặc '那个' (cái kia).",
        "sound_txt": "我喜欢这个。"
    }
]

def show_hsk1_consolidated_quiz(save_progress, save_score_row_hsk1_consolidated, load_all_scores_hsk1_consolidated):
    # CSS Styles cao cấp, mô phỏng đúng thiết kế của ảnh người dùng gửi và tăng trải nghiệm premium
    st.markdown("""
    <style>
    /* Card Container */
    .quiz-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 24px;
        padding: 35px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
        margin-bottom: 25px;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Question Number */
    .quiz-q-num {
        font-size: 1.4rem;
        font-weight: 800;
        color: #1e3a8a;
        margin-bottom: 12px;
        font-family: 'Inter', sans-serif;
    }
    
    /* Question Text */
    .quiz-q-text {
        font-size: 1.25rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 8px;
        line-height: 1.45;
        font-family: 'Inter', sans-serif;
    }
    
    /* Pinyin Text */
    .quiz-q-pinyin {
        font-family: 'Courier New', monospace;
        font-size: 1.15rem;
        font-weight: bold;
        color: #2563eb;
        margin-bottom: 25px;
        background-color: #eff6ff;
        padding: 8px 16px;
        border-radius: 12px;
        display: inline-block;
        border: 1px solid #dbeafe;
    }
    
    /* Option Buttons Container */
    .quiz-option-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-bottom: 20px;
    }
    
    /* Styled Streamlit buttons inside container - EXACTLY like the image */
    .quiz-option-container div.stButton > button {
        background-color: #f3f4f6 !important;
        color: #1f2937 !important;
        border-radius: 24px !important;
        border: 1px solid transparent !important;
        padding: 20px 25px !important;
        font-size: 1.15rem !important;
        font-weight: 600 !important;
        text-align: left !important;
        align-items: center !important;
        justify-content: flex-start !important;
        width: 100% !important;
        display: flex !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.01) !important;
        transition: all 0.2s ease !important;
    }
    
    .quiz-option-container div.stButton > button:hover {
        background-color: #e5e7eb !important;
        border-color: #d1d5db !important;
        color: #000000 !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
    }
    
    /* Static Option Cards (for showing result) */
    .quiz-option-static {
        background-color: #f3f4f6;
        color: #1f2937;
        border-radius: 24px;
        padding: 20px 25px;
        font-size: 1.15rem;
        font-weight: 600;
        text-align: left;
        display: flex;
        align-items: center;
        border: 2px solid transparent;
        margin-bottom: 12px;
    }
    
    .quiz-option-static.correct {
        background-color: #f0fdf4;
        color: #14532d;
        border-color: #22c55e;
    }
    
    .quiz-option-static.incorrect {
        background-color: #fef2f2;
        color: #7f1d1d;
        border-color: #ef4444;
    }
    
    .quiz-option-static.normal {
        background-color: #f9fafb;
        color: #9ca3af;
        border-color: #e5e7eb;
        opacity: 0.65;
    }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "📝 Trắc nghiệm Tổng hợp HSK 1",
        "Hệ thống 30 câu hỏi trắc nghiệm ôn tập toàn diện kiến thức ngữ pháp, từ vựng và quy tắc Bính âm (Pinyin) HSK 1 đã học."
    )

    # --- KHỞI TẠO STATE CHO QUIZ ---
    if "hsk1_quiz_started" not in st.session_state:
        st.session_state.hsk1_quiz_started = False
    if "hsk1_quiz_idx" not in st.session_state:
        st.session_state.hsk1_quiz_idx = 0
    if "hsk1_quiz_answers" not in st.session_state:
        st.session_state.hsk1_quiz_answers = [None] * len(HSK1_QUESTIONS)
    if "hsk1_quiz_score" not in st.session_state:
        st.session_state.hsk1_quiz_score = 0
    if "hsk1_quiz_submitted" not in st.session_state:
        st.session_state.hsk1_quiz_submitted = False
    if "hsk1_quiz_shuffled_options" not in st.session_state:
        # Xáo trộn đáp án một lần duy nhất cho mỗi phiên
        shuffled = []
        for i, q in enumerate(HSK1_QUESTIONS):
            opts = q["choices"][:]
            # Đảm bảo xáo trộn có tổ chức
            random.Random(i + 42).shuffle(opts)
            shuffled.append(opts)
        st.session_state.hsk1_quiz_shuffled_options = shuffled

    # ================= 1. GIAO DIỆN LÀM BÀI (CHƯA BẮT ĐẦU) =================
    if not st.session_state.hsk1_quiz_started:
        st.markdown("""
        <div style="background-color: #f8fafc; border-left: 6px solid #e11d48; border-radius: 12px; padding: 24px; margin-bottom: 25px;">
            <h3 style="color: #e11d48; margin-top: 0; font-weight: 800;">🎯 Hướng dẫn ôn tập & kiểm tra:</h3>
            <p style="color: #334155; font-size: 1.05rem; line-height: 1.6;">
                • Bài kiểm tra gồm <b>30 câu hỏi trắc nghiệm</b> phủ rộng toàn bộ các chủ điểm ngữ pháp, phát âm, từ vựng và chữ viết HSK 1.<br/>
                • Định dạng bài tập <b>theo chuẩn trực quan cao cấp</b> với hỗ trợ phiên âm Pinyin và âm thanh đọc mẫu.<br/>
                • Mỗi câu hỏi có 1 đáp án chính xác duy nhất. Sau khi lựa chọn, bạn sẽ nhận được <b>phản hồi và giải thích ngữ nghĩa chi tiết</b> ngay lập tức.<br/>
                • Hãy làm hết khả năng và lưu điểm để cạnh tranh trên bảng xếp hạng lớp học nhé!
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("🚀 Bắt đầu làm bài", type="primary", use_container_width=True):
                st.session_state.hsk1_quiz_started = True
                st.session_state.hsk1_quiz_idx = 0
                st.session_state.hsk1_quiz_answers = [None] * len(HSK1_QUESTIONS)
                st.session_state.hsk1_quiz_score = 0
                st.session_state.hsk1_quiz_submitted = False
                st.rerun()
        with col2:
            # Xem bảng xếp hạng
            all_scores = load_all_scores_hsk1_consolidated()
            if all_scores:
                with st.expander("🏆 Xem Bảng xếp hạng nộp điểm hiện tại", expanded=False):
                    st.dataframe(all_scores, use_container_width=True)
            else:
                st.info("Chưa có lượt nộp điểm nào. Hãy là người đầu tiên!")

    # ================= 2. GIAO DIỆN LÀM BÀI (ĐANG LÀM) =================
    else:
        current_idx = st.session_state.hsk1_quiz_idx
        
        # Nếu đã trả lời hết 30 câu hỏi
        if current_idx >= len(HSK1_QUESTIONS):
            show_quiz_results(save_progress, save_score_row_hsk1_consolidated, load_all_scores_hsk1_consolidated)
            return

        q_data = HSK1_QUESTIONS[current_idx]
        shuffled_choices = st.session_state.hsk1_quiz_shuffled_options[current_idx]
        correct_choice = q_data["answer"]
        user_choice = st.session_state.hsk1_quiz_answers[current_idx]
        is_answered = (user_choice is not None)

        # Thanh tiến độ ở trên cùng
        percent_done = int((current_idx / len(HSK1_QUESTIONS)) * 100)
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; font-weight: bold; color: #475569; margin-bottom: 8px; font-size: 0.95rem;">
            <span>Tiến độ: Câu {current_idx + 1} / {len(HSK1_QUESTIONS)}</span>
            <span>{percent_done}% hoàn thành</span>
        </div>
        """, unsafe_allow_html=True)
        st.progress(current_idx / len(HSK1_QUESTIONS))

        # Khung thẻ câu hỏi
        st.markdown(f"""
        <div class="quiz-card">
            <div class="quiz-q-num">Câu hỏi {current_idx + 1}</div>
            <div class="quiz-q-text">{q_data['question']}</div>
            <div class="quiz-q-pinyin">Pinyin: {q_data['pinyin']}</div>
        </div>
        """, unsafe_allow_html=True)

        # Hỗ trợ nghe phát âm câu đầy đủ
        col_audio, col_empty = st.columns([4, 6])
        with col_audio:
            render_play_button(q_data["sound_txt"], "🔊 Phát âm câu hỏi mẫu", key=f"audio_q_{current_idx}")
        st.markdown("<br/>", unsafe_allow_html=True)

        # ================= 2.1 TRẠNG THÁI: CHƯA CHỌN ĐÁP ÁN =================
        if not is_answered:
            # Render các nút chọn đáp án (Khi click sẽ tự động chuyển state)
            st.markdown('<div class="quiz-option-container">', unsafe_allow_html=True)
            
            # Sử dụng columns để render các button Streamlit nằm dọc
            for i, choice in enumerate(shuffled_choices):
                # Bắt click đáp án
                if st.button(choice, key=f"btn_choice_{i}_{current_idx}", use_container_width=True):
                    st.session_state.hsk1_quiz_answers[current_idx] = choice
                    # Cộng điểm nếu đúng
                    if choice == correct_choice:
                        st.session_state.hsk1_quiz_score += 1
                    save_progress()
                    st.rerun()
                    
            st.markdown('</div>', unsafe_allow_html=True)

        # ================= 2.2 TRẠNG THÁI: ĐÃ CHỌN ĐÁP ÁN (HIỂN THỊ KẾT QUẢ CỦA CÂU) =================
        else:
            # Hiển thị các block đáp án tĩnh, tô màu xanh/đỏ/xám theo đúng chuẩn thiết kế
            static_options_html = '<div class="quiz-option-container">'
            for choice in shuffled_choices:
                if choice == correct_choice:
                    static_options_html += f'<div class="quiz-option-static correct">✅ {choice}</div>'
                elif choice == user_choice:
                    static_options_html += f'<div class="quiz-option-static incorrect">❌ {choice}</div>'
                else:
                    static_options_html += f'<div class="quiz-option-static normal">{choice}</div>'
            static_options_html += '</div>'
            st.markdown(static_options_html, unsafe_allow_html=True)

            # Hiển thị ô giải thích chi tiết
            if user_choice == correct_choice:
                st.success(f"🎉 **Chính xác!**\n\n**Giải thích:** {q_data['explain']}")
            else:
                st.error(f"😢 **Chưa chính xác!** (Bạn đã chọn: {user_choice})\n\n👉 Đáp án đúng là: **{correct_choice}**\n\n**Giải thích:** {q_data['explain']}")

            # Nút điều hướng câu tiếp theo
            st.markdown("<br/>", unsafe_allow_html=True)
            col_nav_1, col_nav_2 = st.columns([1, 1])
            with col_nav_1:
                # Nút cho phép quay lại xem câu trước
                if current_idx > 0:
                    if st.button("⬅️ Câu trước đó", use_container_width=True):
                        st.session_state.hsk1_quiz_idx -= 1
                        st.rerun()
            with col_nav_2:
                btn_label = "Xem kết quả tổng kết 📊" if current_idx == len(HSK1_QUESTIONS) - 1 else "Câu tiếp theo ➡️"
                if st.button(btn_label, type="primary", use_container_width=True):
                    st.session_state.hsk1_quiz_idx += 1
                    st.rerun()


def show_quiz_results(save_progress, save_score_row_hsk1_consolidated, load_all_scores_hsk1_consolidated):
    score = st.session_state.hsk1_quiz_score
    total = len(HSK1_QUESTIONS)
    final_score_10 = round((score / total) * 10, 2)

    st.balloons()
    st.markdown(f"""
    <div style="background-color: #fff; border: 2px solid #22c55e; border-radius: 20px; padding: 40px; text-align: center; max-width: 600px; margin: 30px auto; box-shadow: 0 10px 25px rgba(0,0,0,0.05);">
        <span style="font-size: 4rem;">🏆</span>
        <h2 style="color: #1e3a8a; margin-top: 15px; font-weight: 800;">Hoàn thành bài thi trắc nghiệm!</h2>
        <p style="font-size: 1.1rem; color: #475569; margin-bottom: 25px;">Bạn đã trả lời đúng tất cả các câu hỏi của bài kiểm tra tổng hợp.</p>
        <div style="background-color: #f0fdf4; border-radius: 12px; padding: 20px; display: inline-block; margin-bottom: 10px;">
            <span style="font-size: 1.1rem; color: #166534; font-weight: bold; display: block;">TỔNG ĐIỂM CỦA BẠN:</span>
            <span style="font-size: 3rem; color: #15803d; font-weight: 900;">{score} / {total}</span>
            <span style="font-size: 1.3rem; color: #15803d; font-weight: 700; display: block; margin-top: 5px;">({final_score_10} điểm hệ 10)</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Form nộp bài và lưu điểm
    if not st.session_state.hsk1_quiz_submitted:
        name = st.text_input("Nhập họ và tên học viên để nộp điểm lên bảng vàng:", placeholder="Ví dụ: Nguyễn Văn A", key="hsk1_quiz_student_name")
        if st.button("💾 Nộp bài & Lưu điểm số", type="primary", use_container_width=True):
            if name:
                row = {
                    "thời gian": datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S"),
                    "học viên": name,
                    "tổng điểm": final_score_10,
                    "Kết quả": f"{score}/{total}"
                }
                if save_score_row_hsk1_consolidated(row):
                    st.session_state.hsk1_quiz_submitted = True
                    st.success("Đã lưu điểm số của bạn thành công!")
                    save_progress()
                    st.rerun()
            else:
                st.error("Vui lòng điền tên trước khi bấm nộp bài!")
    else:
        st.success("Chúc mừng bạn đã nộp bài thành công!")

    # Nút làm lại bài
    if st.button("🔄 Làm lại bài trắc nghiệm", use_container_width=True):
        st.session_state.hsk1_quiz_started = False
        st.session_state.hsk1_quiz_idx = 0
        st.session_state.hsk1_quiz_answers = [None] * len(HSK1_QUESTIONS)
        st.session_state.hsk1_quiz_score = 0
        st.session_state.hsk1_quiz_submitted = False
        save_progress()
        st.rerun()

    # Bảng xếp hạng nộp bài
    st.markdown("---")
    st.markdown("### 🏆 Bảng xếp hạng nộp bài trắc nghiệm HSK 1")
    all_scores = load_all_scores_hsk1_consolidated()
    if all_scores:
        st.dataframe(all_scores, use_container_width=True)
    else:
        st.info("Chưa có lượt nộp điểm nào. Hãy làm bài và lưu điểm số đầu tiên!")
