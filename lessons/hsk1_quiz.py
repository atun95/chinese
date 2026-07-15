# -*- coding: utf-8 -*-
import streamlit as st
import random
import csv
from datetime import datetime, timezone, timedelta
from ui_utils import render_lesson_intro, render_play_button

# ĐỊNH NGHĨA CÁC ĐỀ QUIZ (1, 2, 3, 4) DỰA TRÊN GIÁO TRÌNH BÀI 1 - BÀI 8
QUIZZES_DATA = {
    "quiz_1": {
        "title": "📝 Đề 1: Nhập môn Ngữ âm & Từ vựng cơ bản (Bài 1 - Bài 3)",
        "description": "Tập trung kiểm tra các thanh mẫu b-h, j-q-x, z-c-s, zh-ch-sh-r; vận mẫu đơn/kép cơ bản; thanh điệu; xưng hô gia đình; đại từ nhân xưng và quy tắc Pinyin cơ bản.",
        "questions": [
            {
                "question": "Chọn phát âm đúng cho từ xưng hô chỉ người mẹ: “妈妈”",
                "pinyin": "Māma",
                "choices": ["A. bàba", "B. māma", "C. gēge", "D. jiějie"],
                "answer": "B. māma",
                "explain": "Từ xưng hô '妈妈' chỉ người mẹ có phiên âm Pinyin tương ứng là 'māma' (thanh 1 đi cùng thanh nhẹ).",
                "sound_txt": "妈妈"
            },
            {
                "question": "Chọn phát âm đúng cho từ chỉ người thầy/cô giáo: “老师”",
                "pinyin": "Lǎoshī",
                "choices": ["A. xuéshēng", "B. lǎoshī", "C. lǜshī", "D. péngyou"],
                "answer": "B. lǎoshī",
                "explain": "Từ vựng '老师' nghĩa là thầy giáo/cô giáo, được phát âm là 'lǎoshī' (thanh 3 đi cùng thanh 1).",
                "sound_txt": "老师"
            },
            {
                "question": "Điền thanh mẫu thích hợp để tạo thành từ 'bạn/cậu': “___ǐ”",
                "pinyin": "nǐ",
                "choices": ["A. m", "B. n", "C. l", "D. d"],
                "answer": "B. n",
                "explain": "Đại từ nhân xưng ngôi thứ hai số ít '你' (bạn/cậu) có thanh mẫu bắt đầu bằng âm đầu lưỡi 'n' phát âm là 'nǐ'.",
                "sound_txt": "你"
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
                "explain": "Khi nguyên âm 'i' đứng sau các thanh mẫu đầu lưỡi-răng (z, c, s) và uốn lưỡi (zh, ch, sh, r), nó phải phát âm biến thành âm 'ư' của tiếng Việt.",
                "sound_txt": "四"
            },
            {
                "question": "Chọn cách viết Pinyin đúng luật chính tả cho âm tiết 'i' khi đứng độc lập (không đi kèm thanh mẫu phía trước):",
                "pinyin": "Quy tắc viết Bính âm cho nguyên âm 'i':",
                "choices": ["A. yi", "B. i", "C. wi", "D. y"],
                "answer": "A. yi",
                "explain": "Khi nguyên âm 'i' đứng một mình tạo thành âm tiết độc lập, ta bắt buộc phải thêm bán nguyên âm 'y' phía trước, viết thành 'yi' để phân biệt.",
                "sound_txt": "yi"
            },
            {
                "question": "Chọn cách biến điệu đúng của từ '不' (bù) trong câu '他不是学生。' (Anh ấy không phải học sinh):",
                "pinyin": "Biến điệu của 'bù' trong 'bù shì':",
                "choices": [
                    "A. Đọc là 'bù' (giữ nguyên thanh 4)",
                    "B. Đọc là 'bú' (biến thành thanh 2)",
                    "C. Đọc là 'bù' nhưng viết là 'bú'",
                    "D. Đọc là 'bǔ' (thanh 3)"
                ],
                "answer": "B. Đọc là 'bú' (biến thành thanh 2)",
                "explain": "Khi phó từ phủ định '不' (bù) đứng trước một từ mang thanh 4 (như 是 - shì), nó phải biến điệu đọc thành thanh 2 là 'bú' (bú shì).",
                "sound_txt": "不是"
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
                "explain": "Khi nguyên âm tròn môi 'ü' đi sau j, q, x, y, ta bỏ hai dấu chấm trên đầu khi viết (viết thành ju, qu, xu, yu) nhưng vẫn phát âm tròn môi là 'ü'.",
                "sound_txt": "去"
            },
            {
                "question": "Chọn từ thích hợp điền vào chỗ trống: “你家有_____口人?” (Nhà bạn có ... người.)",
                "pinyin": "Nǐ jiā yǒu _____ kǒu rén？",
                "choices": ["A. 几 (jǐ)", "B. 多少 (duōshao)", "C. 什么 (shénme)", "D. 谁 (shéi)"],
                "answer": "A. 几 (jǐ)",
                "explain": "Để hỏi số lượng thành viên trong gia đình (thường dưới 10 người), ta dùng từ để hỏi '几' (jǐ). Cấu trúc: 几 + lượng từ (口) + danh từ (人).",
                "sound_txt": "你家有几口人？"
            },
            {
                "question": "Dịch đại từ xưng hô thích hợp cho từ “chúng tôi/chúng ta”:",
                "pinyin": "Chúng tôi / Chúng ta",
                "choices": ["A. 我们 (wǒmen)", "B. 你们 (nǐmen)", "C. 他们 (tāmen)", "D. 它们 (tāmen)"],
                "answer": "A. 我们 (wǒmen)",
                "explain": "'我们' (wǒmen) là đại từ nhân xưng ngôi thứ nhất số nhiều (chúng tôi/chúng ta). '你们' là các bạn, '他们' là họ.",
                "sound_txt": "我们"
            },
            {
                "question": "Chọn phó từ phủ định phù hợp: “他_____是学生，他是老师。”",
                "pinyin": "Tā _____ shì xuéshēng, tā shì lǎoshī.",
                "choices": ["A. 不 (bù)", "B. 没 (méi)", "C. 没有 (méiyǒu)", "D. 的 (de)"],
                "answer": "A. 不 (bù)",
                "explain": "Phủ định của động từ liên hệ '是' (là) là '不是' (không phải là). Ở đây điền '不' (bù) để phủ định.",
                "sound_txt": "他不是学生，他是老师。"
            },
            {
                "question": "Thanh mẫu nào sau đây là phụ âm bật hơi mạnh bằng hai môi?",
                "pinyin": "Phụ âm bật hơi môi:",
                "choices": ["A. b", "B. p", "C. m", "D. f"],
                "answer": "B. p",
                "explain": "Trong nhóm âm môi, 'p' là âm bật hơi mạnh bằng cách mím chặt hai môi rồi đẩy luồng hơi mạnh từ khoang miệng ra ngoài.",
                "sound_txt": "p"
            },
            {
                "question": "Chọn phát âm đúng của âm đầu lưỡi uốn ngược chạm ngạc cứng 'ch' trong động từ '吃' (ăn):",
                "pinyin": "Cách phát âm 'ch' trong 'chī':",
                "choices": ["A. cī (không uốn lưỡi)", "B. chī (uốn lưỡi, bật hơi)", "C. zhī (uốn lưỡi, không bật hơi)", "D. shī (uốn lưỡi, xát)"],
                "answer": "B. chī (uốn lưỡi, bật hơi)",
                "explain": "Thanh mẫu 'ch' thuộc nhóm uốn lưỡi, phát âm ở vị trí uốn đầu lưỡi ngược lên ngạc cứng và đẩy hơi bật ra mạnh.",
                "sound_txt": "吃"
            },
            {
                "question": "Khi nguyên âm 'u' đứng một mình tạo thành âm tiết độc lập, ta viết biến đổi thành dạng nào?",
                "pinyin": "Quy tắc viết Bính âm cho nguyên âm 'u':",
                "choices": ["A. wu", "B. yu", "C. w", "D. u"],
                "answer": "A. wu",
                "explain": "Theo quy tắc chính tả, khi nguyên âm 'u' đứng độc lập không có phụ âm đi trước, ta phải thêm bán nguyên âm 'w' vào trước, viết thành 'wu'.",
                "sound_txt": "wu"
            },
            {
                "question": "Lượng từ nào dùng để đếm thành viên trong gia đình khi đi kèm với động từ sở hữu '有' (có)?",
                "pinyin": "Lượng từ chỉ người trong gia đình:",
                "choices": ["A. 口 (kǒu)", "B. 个 (gè)", "C. 件 (jiàn)", "D. 本 (běn)"],
                "answer": "A. 口 (kǒu)",
                "explain": "Tiếng Trung dùng lượng từ đặc biệt '口' (kǒu) để đếm nhân khẩu trong gia đình (ví dụ: 三口人 - ba người). Lượng từ chung là '个'.",
                "sound_txt": "口"
            },
            {
                "question": "Khi kết hợp với thanh mẫu 'l', nguyên âm 'ü' có bị lược bỏ hai dấu chấm trên đầu không?",
                "pinyin": "ü kết hợp với l:",
                "choices": [
                    "A. Có lược bỏ (viết thành lu)",
                    "B. Bắt buộc giữ nguyên hai dấu chấm (viết thành lü)",
                    "C. Viết thành lyu",
                    "D. Đổi thành luô"
                ],
                "answer": "B. Bắt buộc giữ nguyên hai dấu chấm (viết thành lü)",
                "explain": "Vì thanh mẫu 'l' có thể đi với cả 'u' (lu) và 'ü' (lü) tạo thành hai âm tiết khác nhau (lù - lộ, lǜ - lục), nên bắt buộc phải giữ nguyên dấu 2 chấm.",
                "sound_txt": "绿"
            }
        ]
    },
    "quiz_2": {
        "title": "📝 Đề 2: Ngữ âm mở rộng, Số đếm & Từ vựng Nữ giới (Bài 4 - Bài 5)",
        "description": "Kiểm tra các vận mẫu kép phức tạp bắt đầu bằng i/u/ü; phân biệt nhóm từ chỉ Nữ giới (nǚrén, nǚhái, nǚ'ér, nǚshēng...); số đếm 0 - 10; vận mẫu mũi và phó từ chỉ mức độ.",
        "questions": [
            {
                "question": "Chọn từ vựng chỉ Nữ giới dùng để biểu đạt quan hệ huyết thống gia đình (con gái của bố mẹ):",
                "pinyin": "Con gái (quan hệ gia đình)",
                "choices": ["A. 女生 (nǚshēng)", "B. 女孩 (nǚhái)", "C. 女儿 (nǚ'ér)", "D. 女性 (nǚxìng)"],
                "answer": "C. 女儿 (nǚ'ér)",
                "explain": "Từ '女儿' (nǚ'ér) được dùng duy nhất để chỉ mối quan hệ gia đình (con gái của ai đó). Các từ khác dùng ngoài xã hội.",
                "sound_txt": "女儿"
            },
            {
                "question": "Trong tờ khai hành chính chính thức hoặc hồ sơ bệnh án, phần giới tính ghi 'Nữ' sẽ dùng thuật ngữ sinh học nào?",
                "pinyin": "Giới tính Nữ (trang trọng)",
                "choices": ["A. 女人 (nǚrén)", "B. 女子 (nǚzǐ)", "C. 妇女 (fùnǚ)", "D. 女性 (nǚxìng)"],
                "answer": "D. 女性 (nǚxìng)",
                "explain": "Trong khoa học, pháp lý và hành chính, '女性' (nǚxìng - nữ giới) và '男性' (nánxìng - nam giới) là hai từ quy chuẩn để chỉ giới tính sinh học.",
                "sound_txt": "女性"
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
                "question": "Chọn phó từ chỉ mức độ phù hợp: “那个女生_____漂亮。” (Bạn nữ kia rất xinh đẹp.)",
                "pinyin": "Nàge nǚshēng _____ piàoliang.",
                "choices": ["A. 是 (shì)", "B. 的 (de)", "C. 很 (hěn)", "D. 有 (yǒu)"],
                "answer": "C. 很 (hěn)",
                "explain": "Trong câu có vị ngữ là tính từ (S + Adj), phó từ chỉ mức độ '很' (hěn) đóng vai trò liên kết cấu trúc ngữ pháp bắt buộc.",
                "sound_txt": "那个女生很漂亮。"
            },
            {
                "question": "Chọn số đếm phù hợp: “我买_____个苹果。” (Tôi mua 3 quả táo.)",
                "pinyin": "Wǒ mǎi _____ gè píngguǒ.",
                "choices": ["A. 三 (sān)", "B. 四 (sì)", "C. 五 (wǔ)", "D. 六 (liù)"],
                "answer": "A. 三 (sān)",
                "explain": "Số 3 trong tiếng Trung là '三' (sān). Cụm lượng từ: 三个苹果 (sān gè píngguǒ).",
                "sound_txt": "我买三个苹果。"
            },
            {
                "question": "Chọn động từ thích hợp: “我_____一个女儿。” (Tôi có một người con gái.)",
                "pinyin": "Wǒ _____ yí gè nǚ'ér.",
                "choices": ["A. 是 (shì)", "B. 有 (yǒu)", "C. 去 (qù)", "D. 叫 (jiào)"],
                "answer": "B. 有 (yǒu)",
                "explain": "Động từ sở hữu '有' (yǒu - có) dùng để biểu thị việc có thành viên gia đình (có con gái).",
                "sound_txt": "我有一个女儿。"
            },
            {
                "question": "Chọn trợ từ ngữ khí phù hợp hoàn thành cấu trúc cảm thán: “现在的天气太热_____。” (Thời tiết bây giờ nóng quá rồi.)",
                "pinyin": "Xiànzài de tiānqì tài rè _____.",
                "choices": ["A. 吗 (ma)", "B. 呢 (ne)", "C. 了 (le)", "D. 的 (de)"],
                "answer": "C. 了 (le)",
                "explain": "Trợ từ ngữ khí '了' (le) thường đứng cuối câu để bổ trợ cho phó từ '太' (tài) cấu thành cụm cảm thán '太...了' (quá... rồi).",
                "sound_txt": "现在的天气太热了。"
            },
            {
                "question": "Chọn chỉ định từ phù hợp: “______ 苹果很大，那个苹果很小。” (Quả táo này rất to, quả táo kia rất nhỏ.)",
                "pinyin": "______ píngguǒ hěn dà, nàge píngguǒ hěn xiǎo.",
                "choices": ["A. 这个 (zhège)", "B. 那个 (nàge)", "C. 哪个 (nǎge)", "D. 几口 (jǐkǒu)"],
                "answer": "A. 这个 (zhège)",
                "explain": "Để chỉ vật ở khoảng cách gần ('này'), ta dùng '这个' (zhège), đối lập với '那个' (nàge) chỉ vật ở khoảng cách xa ('kia').",
                "sound_txt": "这个苹果很大，那个苹果很小。"
            },
            {
                "question": "Từ nào sau đây có nghĩa là “bạn trai”?",
                "pinyin": "Bạn trai",
                "choices": ["A. 男朋友 (nánpéngyou)", "B. 女朋友 (nǚpéngyou)", "C. 朋友 (péngyou)", "D. 律师 (lǜshī)"],
                "answer": "A. 男朋友 (nánpéngyou)",
                "explain": "'男朋友' (nánpéngyou) nghĩa là bạn trai. '女朋友' là bạn gái, '朋友' là bạn bè nói chung.",
                "sound_txt": "男朋友"
            },
            {
                "question": "Số đếm '0' (không) trong tiếng Trung phát âm và viết Bính âm là gì?",
                "pinyin": "Số 0",
                "choices": ["A. líng", "B. yī", "C. èr", "D. sān"],
                "answer": "A. líng",
                "explain": "Số 0 trong tiếng Trung là '零', phiên âm Bính âm viết là 'líng'.",
                "sound_txt": "零"
            },
            {
                "question": "Chọn vận mẫu mũi thích hợp cho từ 'cơm' (fàn) thuộc nhóm vận mẫu mũi trước kết thúc bằng âm /n/:",
                "pinyin": "Vận mẫu mũi trong 'fàn':",
                "choices": ["A. an", "B. en", "C. ang", "D. eng"],
                "answer": "A. an",
                "explain": "Từ '饭' (cơm) phát âm là 'fàn', sử dụng vận mẫu mũi trước kết thúc bằng âm 'n' là 'an'.",
                "sound_txt": "饭"
            },
            {
                "question": "Cụm từ 'rất bận' viết bằng Pinyin chuẩn xác là gì?",
                "pinyin": "Rất bận",
                "choices": ["A. hěnmáng", "B. hěnmāng", "C. hēnmáng", "D. hēnmāng"],
                "answer": "A. hěnmáng",
                "explain": "Từ '很' (rất) phát âm là 'hěn', từ '忙' (bận) phát âm là 'máng'. Do đó cụm từ là 'hěnmáng'.",
                "sound_txt": "很忙"
            },
            {
                "question": "Văn hóa: Lễ Tết Đoan Ngọ (mùng 5 tháng 5 âm lịch) trong tiếng Trung gọi là gì?",
                "pinyin": "Tết Đoan Ngọ",
                "choices": ["A. 端午节 (Duānwǔjié)", "B. 中秋节 (Zhōngqiūjié)", "C. 春节 (Chūnjié)", "D. 元宵节 (Yuánxiāojié)"],
                "answer": "A. 端午节 (Duānwǔjié)",
                "explain": "Tết Đoan Ngọ có nguồn gốc văn hóa lâu đời, trong tiếng Trung gọi là '端午节' (Duānwǔjié).",
                "sound_txt": "端午节"
            },
            {
                "question": "Từ 'rén' (người) dùng vận mẫu mũi trước nào sau đây?",
                "pinyin": "Vận mẫu trong 'rén':",
                "choices": ["A. en", "B. an", "C. in", "D. eng"],
                "answer": "A. en",
                "explain": "Chữ '人' (người) phát âm là 'rén', sử dụng thanh mẫu 'r' đi với vận mẫu mũi trước 'en'.",
                "sound_txt": "人"
            },
            {
                "question": "Phó từ nào sau đây mang ý nghĩa chỉ mức độ cao nhất (nhất/bậc nhất)?",
                "pinyin": "Phó từ mức độ cao nhất:",
                "choices": ["A. 最 (zuì)", "B. 很 (hěn)", "C. 非常 (fēicháng)", "D. 太 (tài)"],
                "answer": "A. 最 (zuì)",
                "explain": "Phó từ '最' (zuì) biểu thị mức độ cao nhất ('nhất', ví dụ: 最好 - tốt nhất, 最忙 - bận nhất).",
                "sound_txt": "最"
            }
        ]
    },
    "quiz_3": {
        "title": "📝 Đề 3: Từ để hỏi, Trợ từ 的 & Chỉ định từ (Bài 6 - Bài 7)",
        "description": "Tập trung kiểm tra các vận mẫu mũi phức hợp; hệ thống các từ dùng để hỏi (ai, cái gì, đâu, bao nhiêu, thế nào, tại sao); trợ từ kết cấu 的 và cặp chỉ định từ 这 / 那.",
        "questions": [
            {
                "question": "Chọn động từ phù hợp: “他正在_____电话。” (Anh ấy đang gọi điện thoại.)",
                "pinyin": "Tā zhèngzài _____ diànhuà.",
                "choices": ["A. 写 (xiě)", "B. 听 (tīng)", "C. 打 (dǎ)", "D. 做 (zuò)"],
                "answer": "C. 打 (dǎ)",
                "explain": "Động từ dùng với danh từ '电话' (điện thoại) để chỉ hành động gọi điện là '打' (đỏ) tạo thành cụm '打电话' (gọi điện).",
                "sound_txt": "他正在打电话。"
            },
            {
                "question": "Chọn đại từ nghi vấn hỏi về trạng thái/tính chất phù hợp: “昨天北京的天气_____？”",
                "pinyin": "Zuótiān Běijīng de tiānqì _____?",
                "choices": ["A. 怎么 (zěnme)", "B. 怎么样 (zěnmeyàng)", "C. 几 (jǐ)", "D. 多少 (duōshao)"],
                "answer": "B. 怎么样 (zěnmeyàng)",
                "explain": "Để hỏi về đặc điểm, tính chất, trạng thái (như thế nào) ta dùng đại từ nghi vấn '怎么样' (zěnmeyàng) đứng cuối câu.",
                "sound_txt": "昨天北京的天气怎么样？"
            },
            {
                "question": "Chọn từ để hỏi thích hợp: “这是_____的电脑？” (Đây là máy tính của ai?)",
                "pinyin": "Zhè shì _____ de diànnǎo?",
                "choices": ["A. 谁 (shéi)", "B. 什么 (shénme)", "C. 哪儿 (nǎr)", "D. 几 (jǐ)"],
                "answer": "A. 谁 (shéi)",
                "explain": "Để hỏi về chủ thể người sở hữu ('ai', 'của ai'), ta dùng đại từ nghi vấn '谁' (shéi/shuí).",
                "sound_txt": "这是谁的电脑？"
            },
            {
                "question": "Chọn giới từ phù hợp: “我爸爸_____在医院工作。” (Bố tôi làm việc ở bệnh viện.)",
                "pinyin": "Wǒ bàba _____ yīyuàn gōngzuò.",
                "choices": ["A. 是 (shì)", "B. 有 (yǒu)", "C. 在 (zài)", "D. 去 (qù)"],
                "answer": "C. 在 (zài)",
                "explain": "Giới từ '在' (zài - ở) đứng trước danh từ chỉ địa điểm '医院' để biểu thị nơi diễn ra hành động '工作' (làm việc).",
                "sound_txt": "我爸爸在医院工作。"
            },
            {
                "question": "Chọn lượng từ phù hợp: “爸爸去商店买一个_____。”",
                "pinyin": "Bàba qù shāngdiàn mǎi yí gè _____.",
                "choices": ["A. 杯子 (bēizi)", "B. 衣服 (yīfu)", "C. 猫 (māo)", "D. 书 (shū)"],
                "answer": "A. 杯子 (bēizi)",
                "explain": "Lượng từ '个' (gè) thường đi kèm với các danh từ thông dụng như '杯子' (cái cốc). Các danh từ khác dùng lượng từ khác (件衣服, 只猫, 本书).",
                "sound_txt": "爸爸去商店买一个杯子。"
            },
            {
                "question": "Chọn danh từ chỉ phương vị phù hợp: “书在桌子_____。” (Sách ở trên bàn.)",
                "pinyin": "Shū zài zhuōzi _____.",
                "choices": ["A. 上 (shàng)", "B. 下 (xià)", "C. 里 (lǐ)", "D. 前 (qián)"],
                "answer": "A. 上 (shàng)",
                "explain": "Danh từ phương vị chỉ vị trí bên trên là '上' (shàng) đứng sau danh từ '桌子' (bàn).",
                "sound_txt": "书在桌子上。"
            },
            {
                "question": "Chọn đại từ nghi vấn phù hợp: “你要买_____苹果？” (Bạn muốn mua quả táo nào?)",
                "pinyin": "Nǐ yào mǎi _____ píngguǒ?",
                "choices": ["A. 哪个 (nǎge)", "B. 这个 (zhège)", "C. 那个 (nàge)", "D. 什么 (shénme)"],
                "answer": "A. 哪个 (nǎge)",
                "explain": "Để đưa ra sự lựa chọn giữa các đối tượng ('nào', 'cái nào'), ta dùng đại từ để hỏi '哪个' (nǎge).",
                "sound_txt": "你要哪个苹果？"
            },
            {
                "question": "Chọn từ để hỏi phù hợp: “我不认识他，他是_____？”",
                "pinyin": "Wǒ bù rènshi tā, tā shì _____?",
                "choices": ["A. 谁 (shéi)", "B. 什么 (shénme)", "C. 哪儿 (nǎr)", "D. 几 (jǐ)"],
                "answer": "A. 谁 (shéi)",
                "explain": "Đại từ nghi vấn '谁' (shéi) dùng để hỏi về danh tính của một người ('là ai').",
                "sound_txt": "我不认识他，他是谁？"
            },
            {
                "question": "Chọn trợ từ nghi vấn phù hợp: “你喜欢吃中国菜_____？” (Bạn có thích ăn món Trung Quốc không?)",
                "pinyin": "Nǐ xǐhuan chī Zhōngguócài _____?",
                "choices": ["A. 吗 (ma)", "B. 呢 (ne)", "C. 的 (de)", "D. 了 (le)"],
                "answer": "A. 吗 (ma)",
                "explain": "Trợ từ nghi vấn '吗' (ma) dùng ở cuối câu để tạo thành câu hỏi Có/Không (Yes/No).",
                "sound_txt": "你喜欢吃中国菜吗？"
            },
            {
                "question": "Chọn câu phản hồi phù hợp nhất: 'A: Nǐ xǐhuan nǎge bēizi? - B: ______' (Bạn thích cái cốc nào? - ...)",
                "pinyin": "A: Nǐ xǐhuan nǎge bēizi? - B: ______",
                "choices": [
                    "A. 我喜欢这个。 (Wǒ xǐhuan zhège.)",
                    "B. 那个杯子十块钱。 (Nàge bēizi shí kuài qián.)",
                    "C. 这是 my 电脑。 (Zhè shì wǒ de diànnǎo.)",
                    "D. 我没有杯子。 (Wǒ méiyǒu bēizi.)"
                ],
                "answer": "A. 我喜欢这个。 (Wǒ xǐhuan zhège.)",
                "explain": "Khi được hỏi lựa chọn '哪个' (cái nào), cách phản hồi trực tiếp nhất là chỉ ra đối tượng cụ thể như '这个' (cái này).",
                "sound_txt": "我喜欢这个。"
            },
            {
                "question": "Điền trợ từ phù hợp để diễn đạt quan hệ sở hữu: “这是我_____书。” (Đây là sách của tôi.)",
                "pinyin": "Zhè shì wǒ _____ shū.",
                "choices": ["A. 的 (de)", "B. 吗 (ma)", "C. 呢 (ne)", "D. 了 (le)"],
                "answer": "A. 的 (de)",
                "explain": "Trợ từ kết cấu '的' (de) đặt sau định ngữ '我' để biểu thị mối quan hệ sở hữu đối với trung tâm ngữ '书'.",
                "sound_txt": "这是我的书。"
            },
            {
                "question": "Chọn đại từ nghi vấn dùng để hỏi về nguyên nhân (Tại sao):",
                "pinyin": "Tại sao",
                "choices": ["A. 为什么 (wèishénme)", "B. 怎么 (zěnme)", "C. 怎么样 (zěnmeyàng)", "D. 多少 (duōshao)"],
                "answer": "A. 为什么 (wèishénme)",
                "explain": "Đại từ nghi vấn '为什么' (wèishénme) dùng để hỏi nguyên nhân (Tại sao), thường kết hợp trả lời bằng từ '因为' (bởi vì).",
                "sound_txt": "为什么"
            },
            {
                "question": "Chọn từ thích hợp để dịch nghĩa từ hỏi địa điểm 'nơi nào, đâu' trong tiếng Trung:",
                "pinyin": "Ở đâu / Nơi nào",
                "choices": ["A. 哪儿 (nǎr)", "B. 那儿 (nàr)", "C. 这儿 (zhèr)", "D. 什么 (shénme)"],
                "answer": "A. 哪儿 (nǎr)",
                "explain": "'哪儿' (nǎr) mang thanh 3 là đại từ dùng để hỏi địa điểm (ở đâu). Tránh nhầm với '那儿' (nàr - thanh 4) nghĩa là chỗ kia.",
                "sound_txt": "哪儿"
            },
            {
                "question": "Quy tắc viết Bính âm của vận mẫu 'uen' khi kết hợp với thanh mẫu phía trước (Ví dụ: sh + uen) là gì?",
                "pinyin": "Quy tắc viết 'uen':",
                "choices": [
                    "A. Lược bỏ chữ 'e' ở giữa khi viết (viết là un)",
                    "B. Giữ nguyên toàn bộ cấu trúc (viết là uen)",
                    "C. Đổi thành wen",
                    "D. Đổi thành ueng"
                ],
                "answer": "A. Lược bỏ chữ 'e' ở giữa khi viết (viết là un)",
                "explain": "Khi vận mẫu 'uen' kết hợp với một thanh mẫu phía trước, chữ 'e' ở giữa sẽ bị lược bỏ khi viết (ví dụ: sh + uen -> shun; c + uen -> cun) nhưng khi đọc vẫn giữ nguyên âm đệm.",
                "sound_txt": "un"
            },
            {
                "question": "Vận mẫu mũi phức hợp 'ian' trong chữ '天' (tiān - ngày/trời) phát âm gần giống với âm nào sau đây?",
                "pinyin": "Phát âm 'ian' trong 'tiān':",
                "choices": [
                    "A. i-en (y-ên)",
                    "B. i-an (y-an)",
                    "C. i-ang (y-ang)",
                    "D. i-ong (y-ung)"
                ],
                "answer": "A. i-en (y-ên)",
                "explain": "Trong tiếng Trung, vận mẫu 'ian' không đọc giống 'an' trong tiếng Việt mà phát âm biến đổi gần giống âm 'i-en' (yên/iên) (ví dụ: tiān đọc giống t-iên).",
                "sound_txt": "天"
            }
        ]
    },
    "quiz_4": {
        "title": "📝 Đề 4: Kết cấu chữ Hán & Giao tiếp tổng hợp (Bài 8 & Tổng hợp HSK 1)",
        "description": "Tập trung kiểm tra các nét cơ bản, quy tắc bút thuận, kết cấu chữ Hán, bộ thủ thông dụng ở Bài 8 và các câu giao tiếp đàm thoại tổng hợp từ Bài 1 đến Bài 8.",
        "questions": [
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
                "explain": "Cấu trúc hỏi tên thông dụng là '你叫什么名字？' (Nǐ jiào shénme míngzi?).",
                "sound_txt": "你叫什么名字？"
            },
            {
                "question": "Chọn từ vựng phù hợp: “他是_____，不是学生。” (Anh ấy là luật sư, không phải học sinh.)",
                "pinyin": "Tā shì _____ , bú shì xuéshēng.",
                "choices": ["A. 老师 (lǎoshī)", "B. 医生 (yīshēng)", "C. 律师 (lǜshī)", "D. 朋友 (péngyou)"],
                "answer": "C. 律师 (lǜshī)",
                "explain": "'Luật sư' trong tiếng Trung là '律师' (lǜshī).",
                "sound_txt": "他是律师，不是学生。"
            },
            {
                "question": "Chọn từ vựng phù hợp: “认识你，我很高_____。” (Quen biết bạn, tôi rất vui.)",
                "pinyin": "Rènshi nǐ, wǒ hěn gāo_____.",
                "choices": ["A. 忙 (máng)", "B. 兴 (xìng)", "C. 累 (lèi)", "D. 热 (rè)"],
                "answer": "B. 兴 (xìng)",
                "explain": "Tính từ '高兴' (gāoxìng) có nghĩa là vui vẻ, hân hoan.",
                "sound_txt": "认识 you，我很高兴。"
            },
            {
                "question": "Chọn từ phủ định phù hợp: “因为他今天_____舒服，所以没来。”",
                "pinyin": "Yīnwèi tā jīntiān _____ shūfu, suǒyǐ méi lái.",
                "choices": ["A. 不 (bù)", "B. 没 (méi)", "C. 没有 (méiyǒu)", "D. 是 (shì)"],
                "answer": "A. 不 (bù)",
                "explain": "Phủ định trạng thái sức khỏe '舒服' (khỏe/thoải mái) dùng phó từ phủ định '不' (bù).",
                "sound_txt": "因为 he 今天不舒服，所以没来。"
            },
            {
                "question": "Chọn phó từ phủ định thích hợp: “昨天下午_____下雨。” (Chiều hôm qua không mưa.)",
                "pinyin": "Zuótiān xiàwǔ _____ xiàyǔ.",
                "choices": ["A. 不 (bù)", "B. 没 (méi)", "C. 没有 (méiyǒu)", "D. 是 (shì)"],
                "answer": "C. 没有 (méiyǒu)",
                "explain": "Để phủ định một hành động đã diễn ra trong quá khứ (ngày hôm qua), ta dùng '没有' (méiyǒu) hoặc '没' (méi).",
                "sound_txt": "昨天下午没有下雨。"
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
                "question": "Nét viết cơ bản '横' (héng) trong cấu tạo chữ Hán là nét nào sau đây?",
                "pinyin": "Nét 横 (héng):",
                "choices": ["A. Nét ngang", "B. Nét sổ dọc", "C. Nét phẩy", "D. Nét mác"],
                "answer": "A. Nét ngang",
                "explain": "Nét '横' (héng) là nét ngang, viết kéo thẳng từ trái sang phải.",
                "sound_txt": "横"
            },
            {
                "question": "Nét viết cơ bản '竖' (shù) trong cấu tạo chữ Hán là nét nào sau đây?",
                "pinyin": "Nét 竖 (shù):",
                "choices": ["A. Nét ngang", "B. Nét sổ dọc", "C. Nét phẩy", "D. Nét chấm"],
                "answer": "B. Nét sổ dọc",
                "explain": "Nét '竖' (shù) là nét sổ dọc, kéo thẳng từ trên xuống dưới.",
                "sound_txt": "竖"
            },
            {
                "question": "Quy tắc viết chữ Hán (bút thuận) nào đúng nhất khi viết chữ '十' (shí - số mười)?",
                "pinyin": "Quy tắc viết chữ '十':",
                "choices": [
                    "A. Ngang trước sổ sau (横先竖后)",
                    "B. Sổ trước ngang sau (竖先横后)",
                    "C. Trái trước phải sau",
                    "D. Trên trước dưới sau"
                ],
                "answer": "A. Ngang trước sổ sau (横先竖后)",
                "explain": "Quy tắc bút thuận cơ bản chỉ ra rằng nét ngang viết trước, nét sổ dọc cắt qua viết sau, nên chữ '十' ta viết nét ngang '横' trước rồi viết nét sổ '竖' sau.",
                "sound_txt": "十"
            },
            {
                "question": "Quy tắc bút thuận nào đúng nhất khi viết chữ '八' (bā - số tám)?",
                "pinyin": "Quy tắc viết chữ '八':",
                "choices": [
                    "A. Phẩy trước mác sau (撇先捺后)",
                    "B. Mác trước phẩy sau (捺先撇后)",
                    "C. Trái trước phải sau",
                    "D. Trên trước dưới sau"
                ],
                "answer": "A. Phẩy trước mác sau (撇先捺后)",
                "explain": "Theo quy tắc bút thuận, nét phẩy '撇' (hướng sang trái) viết trước, nét mác '捺' (hướng sang phải) viết sau.",
                "sound_txt": "八"
            },
            {
                "question": "Kết cấu của chữ Hán '你' (nǐ - bạn) thuộc loại kết cấu cấu tạo nào?",
                "pinyin": "Kết cấu chữ '你':",
                "choices": ["A. Kết cấu Trái - Phải", "B. Kết cấu Trên - Dưới", "C. Kết cấu Bao quanh", "D. Kết cấu Độc thể"],
                "answer": "A. Kết cấu Trái - Phải",
                "explain": "Chữ '你' gồm bộ nhân đứng '亻' ở bên trái và chữ '尔' ở bên phải, thuộc kết cấu Trái - Phải.",
                "sound_txt": "你"
            },
            {
                "question": "Bộ thủ '亻' (bộ Nhân đứng) xuất hiện trong chữ '他', '她', '你' liên quan đến ý nghĩa gì?",
                "pinyin": "Ý nghĩa bộ '亻':",
                "choices": ["A. Con người", "B. Nước", "C. Cây cối", "D. Lửa"],
                "answer": "A. Con người",
                "explain": "Bộ Nhân đứng '亻' là biến thể của chữ '人' (người), biểu thị các từ liên quan đến con người, danh xưng.",
                "sound_txt": "人"
            },
            {
                "question": "Chữ Hán '国' (guó - đất nước) có kết cấu cấu tạo nào sau đây?",
                "pinyin": "Kết cấu chữ '国':",
                "choices": ["A. Kết cấu Bao quanh (Toàn vây)", "B. Kết cấu Trái - Phải", "C. Kết cấu Trên - Dưới", "D. Kết cấu Độc thể"],
                "answer": "A. Kết cấu Bao quanh (Toàn vây)",
                "explain": "Chữ '国' có bộ vây '囗' bao bọc chữ '玉' ở bên trong, thuộc kết cấu Bao quanh hoàn toàn (Toàn vây).",
                "sound_txt": "国"
            },
            {
                "question": "Chọn câu chào xã giao tương ứng kính trọng nhất dành cho người lớn tuổi hoặc thầy cô:",
                "pinyin": "Chào kính trọng:",
                "choices": ["A. 你好 (nǐhǎo)", "B. 您好 (nínhǎo)", "C. 你们好 (nǐmenhǎo)", "D. 大家好 (dàjiāhǎo)"],
                "answer": "B. 您好 (nínhǎo)",
                "explain": "'您好' (nínhǎo) sử dụng đại từ kính trọng '您' (Ngài/Ông/Bà) để biểu thị sự tôn trọng tuyệt đối.",
                "sound_txt": "您好"
            },
            {
                "question": "Chọn động từ thích hợp điền vào chỗ trống: “明天我_____商店买东西。” (Ngày mai tôi đi cửa hàng mua đồ.)",
                "pinyin": "Míngtiān wǒ _____ shāngdiàn mǎi dōngxi.",
                "choices": ["A. 去 (qù)", "B. 在 (zài)", "C. 有 (yǒu)", "D. 是 (shì)"],
                "answer": "A. 去 (qù)",
                "explain": "Động từ hành động chuyển dịch địa điểm '去' (qù - đi) thích hợp đi trước danh từ nơi chốn '商店' (cửa hàng) để biểu thị mục đích đi mua đồ.",
                "sound_txt": "明天我去商店买东西。"
            }
        ]
    },
    "quiz_5": {
        "title": "📝 Đề 5: Luyện tập Ngữ âm & Từ vựng Giao tiếp (Bài 1 - Bài 3)",
        "description": "Luyện tập thanh mẫu, vận mẫu đơn/kép cơ bản (Bài 1 - Bài 3), biến điệu thanh 3, quy tắc viết Pinyin của 'ü', các từ xưng hô gia đình và giao tiếp cơ bản.",
        "questions": [
            {
                "question": "Chọn cách phát âm đúng của vận mẫu 'ü' trong từ '鱼' (yú - con cá):",
                "pinyin": "Phát âm 'ü' trong 'yú':",
                "choices": [
                    "A. Đọc giống 'u' trong tiếng Việt",
                    "B. Đọc giống 'ư' trong tiếng Việt",
                    "C. Đọc giống âm 'uy' (như uy trong tiếng Việt nhưng giữ tròn môi)",
                    "D. Đọc giống âm 'o'"
                ],
                "answer": "C. Đọc giống âm 'uy' (như uy trong tiếng Việt nhưng giữ tròn môi)",
                "explain": "Nguyên âm tròn môi 'ü' phát âm bằng cách để vị trí lưỡi và khoang miệng giống âm 'i' nhưng môi khép tròn nhô ra phía trước, tương đương âm 'uy' trong tiếng Việt nhưng giữ nguyên môi tròn đến hết âm.",
                "sound_txt": "鱼"
            },
            {
                "question": "Khi hai âm tiết mang thanh 3 đi liền nhau (ví dụ: 你好 nǐ hǎo), âm tiết thứ nhất sẽ biến điệu phát âm thành thanh mấy?",
                "pinyin": "Biến điệu thanh 3:",
                "choices": ["A. Thanh 1", "B. Thanh 2 (ní)", "C. Thanh 4", "D. Giữ nguyên thanh 3"],
                "answer": "B. Thanh 2 (ní)",
                "explain": "Quy tắc biến điệu thanh 3: Khi hai âm mang thanh 3 (thanh hỏi) đi liền nhau, âm thứ nhất bắt buộc phải đọc thành thanh 2 (thanh sắc), viết vẫn giữ nguyên thanh 3.",
                "sound_txt": "你好"
            },
            {
                "question": "Chọn từ thích hợp điền vào chỗ trống: “他是我的_____， we cùng nhau học tập。” (Anh ấy là bạn học của tôi, chúng tôi học cùng nhau.)",
                "pinyin": "Tā shì wǒ de _____.",
                "choices": ["A. 老师 (lǎoshī)", "B. 医生 (yīshēng)", "C. 同学 (tóngxué)", "D. 爸爸 (bàba)"],
                "answer": "C. 同学 (tóngxué)",
                "explain": "'同学' (tóngxué) nghĩa là bạn học cùng trường/lớp. Phù hợp nhất với ngữ cảnh học tập chung.",
                "sound_txt": "同学"
            },
            {
                "question": "Chọn cách viết Pinyin đúng luật chính tả cho âm tiết 'ia' khi đứng độc lập không có thanh mẫu đi trước:",
                "pinyin": "Quy tắc viết Bính âm của 'ia':",
                "choices": ["A. ia", "B. yia", "C. ya", "D. wa"],
                "answer": "C. ya",
                "explain": "Khi vận mẫu bắt đầu bằng 'i' đứng độc lập tạo thành một âm tiết không có phụ âm đi trước, ta phải đổi 'i' thành 'y'. Do đó 'ia' viết thành 'ya'.",
                "sound_txt": "鸭"
            },
            {
                "question": "Khi nguyên âm 'ü' kết hợp với thanh mẫu 'n', ta viết thế nào trên Bính âm chính thức?",
                "pinyin": "ü kết hợp với n:",
                "choices": ["A. nu", "B. nyu", "C. nü", "D. nou"],
                "answer": "C. nü",
                "explain": "Vì thanh mẫu 'n' có thể đi với cả 'u' (nu - giận dữ) và 'ü' (nü - nữ), nên khi viết ta bắt buộc phải giữ nguyên hai dấu chấm trên đầu 'ü' thành 'nü' để phân biệt.",
                "sound_txt": "女"
            },
            {
                "question": "Chọn câu chào xã giao phù hợp dành cho nhiều người cùng lúc (các bạn chào thầy cô, hoặc thầy cô chào cả lớp):",
                "pinyin": "Chào số nhiều:",
                "choices": ["A. 你好 (nǐhǎo)", "B. 您好 (nínhǎo)", "C. 你们好 (nǐmenhǎo)", "D. 老师好 (lǎoshīhǎo)"],
                "answer": "C. 你们好 (nǐmenhǎo)",
                "explain": "'你们好' (nǐmenhǎo - chào các bạn/chào mọi người) dùng để chào một nhóm từ 2 người trở lên.",
                "sound_txt": "你们好"
            },
            {
                "question": "Dịch câu sau sang tiếng Trung: 'Gia đình bạn có 5 người phải không?'",
                "pinyin": "Dịch câu hỏi số người:",
                "choices": [
                    "A. 你家有五口人吗？ (Nǐ jiā yǒu wǔ kǒu rén ma?)",
                    "B. 我家有五口人。 (Wǒ jiā yǒu wǔ kǒu rén.)",
                    "C. 他家有五个人吗？ (Tā jiā yǒu wǔ gè rén ma?)",
                    "D. 你家有几口人？ (Nǐ jiā yǒu jǐ kǒu rén?)"
                ],
                "answer": "A. 你家有五口人吗？ (Nǐ jiā yǒu wǔ kǒu rén ma?)",
                "explain": "'Gia đình bạn' là 你家, 'có' là 有, '5 người' dùng lượng từ gia đình là 五口人, 'phải không' dùng trợ từ nghi vấn 吗. Do đó câu đúng là: 你家有五口人吗？",
                "sound_txt": "你家有五口人吗？"
            },
            {
                "question": "Thanh mẫu nào sau đây thuộc nhóm âm đầu lưỡi-răng (z, c, s) khi phát âm cần để đầu lưỡi chạm vào răng cửa trên rồi đẩy hơi ra?",
                "pinyin": "Phân loại thanh mẫu:",
                "choices": ["A. z", "B. zh", "C. j", "D. g"],
                "answer": "A. z",
                "explain": "'z' thuộc nhóm âm đầu lưỡi-răng (z, c, s), phát âm không bật hơi. Khác với 'zh' là âm uốn lưỡi, 'j' là âm mặt lưỡi.",
                "sound_txt": "z"
            },
            {
                "question": "Chọn cách viết Bính âm đúng của từ 'tạm biệt' (zàijiàn):",
                "pinyin": "Viết Pinyin của zàijiàn:",
                "choices": ["A. zàijiàn", "B. zàijian", "C. zāijiàn", "D. zāijian"],
                "answer": "A. zàijiàn",
                "explain": "Từ '再' mang thanh 4 (zài), từ '见' mang thanh 4 (jiàn). Do đó viết Bính âm đúng là 'zàijiàn'.",
                "sound_txt": "再见"
            },
            {
                "question": "Từ xưng hô nào mang nghĩa là 'học sinh, sinh viên'?",
                "pinyin": "Từ vựng nghề nghiệp:",
                "choices": ["A. 老师 (lǎoshī)", "B. 学生 (xuéshēng)", "C. 医生 (yīshēng)", "D. 同学 (tóngxué)"],
                "answer": "B. 学生 (xuéshēng)",
                "explain": "'学生' (xuéshēng) có nghĩa là học sinh hoặc sinh viên nói chung. '老师' là giáo viên, '医生' là bác sĩ.",
                "sound_txt": "学生"
            },
            {
                "question": "Chọn từ thích hợp điền vào chỗ trống: “我不是老师，我_____是学生。” (Tôi không phải giáo viên, tôi _____ là học sinh.)",
                "pinyin": "Wǒ bú  shì lǎoshī, wǒ _____  shì xuéshēng.",
                "choices": ["A. 没 (méi)", "B. 是 (shì)", "C. 有 (yǒu)", "D. 不 (bù)"],
                "answer": "B. 是 (shì)",
                "explain": "Vế trước phủ định '我不是老师' (Tôi không phải giáo viên), vế sau khẳng định '我是学生' (Tôi là học sinh), điền '是' (shì) làm động từ liên kết.",
                "sound_txt": "我是学生"
            },
            {
                "question": "Thanh mẫu 'h' trong tiếng Trung phát âm thế nào?",
                "pinyin": "Cách phát âm thanh mẫu 'h':",
                "choices": [
                    "A. Phát âm nhẹ nhàng giống 'h' tiếng Việt",
                    "B. Phát âm mạnh, xát từ cuống họng gần giống 'kh' tiếng Việt",
                    "C. Phát âm câm không đọc",
                    "D. Phát âm giống 'g' tiếng Việt"
                ],
                "answer": "B. Phát âm mạnh, xát từ cuống họng gần giống 'kh' tiếng Việt",
                "explain": "Thanh mẫu 'h' là phụ âm cuống họng, xát, trong khẩu ngữ thực tế thường đọc mạnh và sát hơn chữ 'h' tiếng Việt, hơi thiên về âm 'kh' nhẹ.",
                "sound_txt": "h"
            },
            {
                "question": "Quy tắc viết Bính âm của nguyên âm kép 'ua' khi đứng độc lập không đi kèm phụ âm:",
                "pinyin": "Quy tắc viết Bính âm cho 'ua':",
                "choices": ["A. ua", "B. wa", "C. ya", "D. yua"],
                "answer": "B. wa",
                "explain": "Theo quy tắc chính tả Bính âm, khi nguyên âm kép bắt đầu bằng 'u' đứng độc lập, ta phải đổi 'u' thành 'w'. Do đó 'ua' viết thành 'wa'.",
                "sound_txt": "蛙"
            },
            {
                "question": "Dịch đại từ nhân xưng số nhiều 'họ/chúng nó' (chỉ nam giới hoặc cả nhóm có cả nam lẫn nữ):",
                "pinyin": "Họ / Chúng nó (nam/chung)",
                "choices": ["A. 我们 (wǒmen)", "B. 你们 (nǐmen)", "C. 他们 (tāmen)", "D. 她们 (tāmen)"],
                "answer": "C. 他们 (tāmen)",
                "explain": "'他们' (tāmen) dùng cho nhóm nam giới hoặc nhóm hỗn hợp nam nữ. '她们' chỉ dùng cho nhóm toàn nữ giới.",
                "sound_txt": "他们"
            },
            {
                "question": "Trong câu hỏi “你好吗？” (Bạn khỏe không?), từ “吗” (ma) đóng vai trò gì?",
                "pinyin": "Vai trò của '吗':",
                "choices": [
                    "A. Trợ từ ngữ khí đứng cuối câu để tạo câu hỏi nghi vấn Có/Không",
                    "B. Đại từ nhân xưng chỉ ngôi thứ hai",
                    "C. Tính từ biểu đạt trạng thái sức khỏe tốt",
                    "D. Động từ liên kết"
                ],
                "answer": "A. Trợ từ ngữ khí đứng cuối câu để tạo câu hỏi nghi vấn Có/Không",
                "explain": "Trợ từ ngữ khí '吗' (ma) đặt ở cuối câu trần thuật để biến câu đó thành câu hỏi Có/Không (Yes/No question).",
                "sound_txt": "你好吗？"
            }
        ]
    },
    "quiz_6": {
        "title": "📝 Đề 6: Số đếm, Ngày tháng & Từ vựng Nữ giới (Bài 4 - Bài 5)",
        "description": "Luyện tập số đếm 0 - 10, phân biệt cách dùng các từ chỉ Nữ giới (nǚrén, nǚ'ér, nǚhái, nǚshēng...), phó từ chỉ mức độ, vận mẫu mũi trước và vận mẫu mũi sau.",
        "questions": [
            {
                "question": "Số đếm '8' trong tiếng Trung viết bằng chữ Hán là chữ nào?",
                "pinyin": "Chữ Hán của số 8:",
                "choices": ["A. 八 (bā)", "B. 七 (qī)", "C. 九 (jiǔ)", "D. 六 (liù)"],
                "answer": "A. 八 (bā)",
                "explain": "Số 8 viết là '八' (bā). '七' là 7, '九' là 9, '六' là 6.",
                "sound_txt": "八"
            },
            {
                "question": "Chọn từ vựng chỉ giới tính nữ mang sắc thái thân mật, thường dùng cho các bạn gái nhỏ hoặc thiếu nữ trẻ:",
                "pinyin": "Cô bé / Bạn gái trẻ:",
                "choices": ["A. 女人 (nǚrén)", "B. 女孩 (nǚhái)", "C. 女性 (nǚxìng)", "D. 妇女 (fùnǚ)"],
                "answer": "B. 女孩 (nǚhái)",
                "explain": "'女孩' (nǚhái) nghĩa là cô bé, bạn gái nhỏ tuổi, mang sắc thái trẻ trung thân mật.",
                "sound_txt": "女孩"
            },
            {
                "question": "Chọn từ thích hợp điền vào chỗ trống: “我买两个_____。” (Tôi mua hai cái cốc.)",
                "pinyin": "Wǒ mǎi liǎng gè _____.",
                "choices": ["A. 衣服 (yīfu)", "B. 书 (shū)", "C. 杯子 (bēizi)", "D. 苹果 (píngguǒ)"],
                "answer": "C. 杯子 (bēizi)",
                "explain": "'杯子' (bēizi) nghĩa là cái cốc, đi với lượng từ '个' (gè).",
                "sound_txt": "杯子"
            },
            {
                "question": "Khi đứng trước một lượng từ (như '个', '口'), số đếm '2' (hai) biến đổi thành từ nào?",
                "pinyin": "Quy tắc dùng số 2 trước lượng từ:",
                "choices": ["A. 二 (èr)", "B. 两 (liǎng)", "C. 双 (shuāng)", "D. 俩 (liǎ)"],
                "answer": "B. 两 (liǎng)",
                "explain": "Khi biểu thị số lượng của sự vật đứng trước một lượng từ, ta không dùng '二' (èr) mà bắt buộc phải đổi sang dùng '两' (liǎng). Ví dụ: 两个苹果.",
                "sound_txt": "两个"
            },
            {
                "question": "Vận mẫu kép nào dưới đây bắt đầu bằng nguyên âm 'u' và kết thúc bằng phụ âm mũi trước 'n'?",
                "pinyin": "Vận mẫu mũi bắt đầu bằng u:",
                "choices": ["A. uan", "B. un (uen)", "C. uang", "D. ueng"],
                "answer": "B. un (uen)",
                "explain": "Vận mẫu 'un' thực chất là viết tắt của 'uen' khi kết hợp với thanh mẫu phía trước. Đây là vận mẫu mũi trước kết thúc bằng âm 'n'.",
                "sound_txt": "un"
            },
            {
                "question": "Phó từ chỉ mức độ nào mang ý nghĩa là 'cực kỳ / vô cùng'?",
                "pinyin": "Phó từ mức độ mạnh:",
                "choices": ["A. 很 (hěn)", "B. 非常 (fēicháng)", "C. 太 (tài)", "D. 最 (zuì)"],
                "answer": "B. 非常 (fēicháng)",
                "explain": "'非常' (fēicháng - phi thường, cực kỳ) biểu thị mức độ cao hơn '很' (rất) nhưng chưa đạt mức cực hạn tuyệt đối như '最' (nhất).",
                "sound_txt": "非常"
            },
            {
                "question": "Chọn câu dịch tiếng Trung đúng nhất cho câu: “Hôm nay tôi rất bận.”",
                "pinyin": "Dịch câu 'Hôm nay tôi rất bận':",
                "choices": [
                    "A. 昨天我很忙。 (Zuótiān wǒ hěn máng.)",
                    "B. 今天我很忙。 (Jīntiān wǒ hěn máng.)",
                    "C. 明天我很忙。 (Míngtiān wǒ hěn máng.)",
                    "D. 今天我不忙。 (Jīntiān wǒ bù máng.)"
                ],
                "answer": "B. 今天我很忙。 (Jīntiān wǒ hěn máng.)",
                "explain": "'Hôm nay' là 今天 (jīntiān), 'tôi' là 我 (wǒ), 'rất bận' là 很忙 (hěn máng).",
                "sound_txt": "今天我很忙。"
            },
            {
                "question": "Chữ Hán '零' (líng) biểu thị chữ số nào sau đây?",
                "pinyin": "Số 零 (líng):",
                "choices": ["A. Số 10", "B. Số 0", "C. Số 2", "D. Số 5"],
                "answer": "B. Số 0",
                "explain": "'零' (líng) nghĩa là số 0. Cách viết phức tạp nhưng phiên âm rất dễ đọc.",
                "sound_txt": "零"
            },
            {
                "question": "Chọn cách viết Bính âm đúng của từ 'thời tiết' (tiānqì):",
                "pinyin": "Viết Pinyin của tiānqì:",
                "choices": ["A. tiānqi", "B. tiānqì", "C. tiānqī", "D. tianqí"],
                "answer": "B. tiānqì",
                "explain": "'天' mang thanh 1 (tiān), '气' mang thanh 4 (qì). Do đó viết Bính âm đúng là 'tiānqì'.",
                "sound_txt": "天气"
            },
            {
                "question": "Từ nào sau đây mang nghĩa là 'con gái' (biểu thị quan hệ ruột thịt với cha mẹ)?",
                "pinyin": "Con gái ruột:",
                "choices": ["A. 女孩 (nǚhái)", "B. 女生 (nǚshēng)", "C. 女儿 (nǚ'ér)", "D. 女人 (nǚrén)"],
                "answer": "C. 女儿 (nǚ'ér)",
                "explain": "'女儿' (nǚ'ér - nữ nhi) chỉ duy nhất quan hệ ruột thịt con gái đối với bố mẹ.",
                "sound_txt": "女儿"
            },
            {
                "question": "Trong các số từ 1 đến 10, số nào phát âm là 'qī'?",
                "pinyin": "Số phát âm là qī:",
                "choices": ["A. Số 7 (七)", "B. Số 8 (八)", "C. Số 9 (九)", "D. Số 6 (六)"],
                "answer": "A. Số 7 (七)",
                "explain": "Số 7 viết chữ Hán là '七', phiên âm phát âm là 'qī'.",
                "sound_txt": "七"
            },
            {
                "question": "Vận mẫu kết thúc bằng phụ âm mũi sau 'ng' được gọi là gì?",
                "pinyin": "Vận mẫu mũi sau:",
                "choices": [
                    "A. Vận mẫu mũi trước",
                    "B. Vận mẫu mũi sau",
                    "C. Vận mẫu uốn lưỡi",
                    "D. Vận mẫu kép"
                ],
                "answer": "B. Vận mẫu mũi sau",
                "explain": "Các vận mẫu kết thúc bằng âm 'ng' (ang, eng, ing, ong...) được gọi là vận mẫu mũi sau (âm đóng ở ngạc mềm). Các vận mẫu kết thúc bằng 'n' là mũi trước.",
                "sound_txt": "ng"
            },
            {
                "question": "Chọn phó từ thích hợp điền vào chỗ trống: “这儿的天气_____热了，我不喜欢。” (Thời tiết ở đây nóng quá rồi, tôi không thích.)",
                "pinyin": "Zhèr de tiānqì _____ rè le.",
                "choices": ["A. 很 (hěn)", "B. 太 (tài)", "C. 最 (zuì)", "D. 非常 (fēicháng)"],
                "answer": "B. 太 (tài)",
                "explain": "Cấu trúc cảm thán '太...了' (quá/lắm... rồi) biểu thị mức độ cực cao hoặc không hài lòng. Điền '太' (tài) kết hợp với '了' (le) cuối câu.",
                "sound_txt": "这儿的天气太热了。"
            },
            {
                "question": "Số 10 trong tiếng Trung là '十', phiên âm Pinyin là gì?",
                "pinyin": "Pinyin của số 10:",
                "choices": ["A. shí", "B. sì", "C. shǐ", "D. shī"],
                "answer": "A. shí",
                "explain": "Số 10 viết chữ Hán là '十', phiên âm mang thanh 2 viết là 'shí'.",
                "sound_txt": "十"
            },
            {
                "question": "Từ nào biểu thị giới tính nữ nói chung theo nghĩa sinh học/xã hội thông thường (đối lập với nam giới)?",
                "pinyin": "Nữ giới / Phụ nữ:",
                "choices": ["A. 女性 (nǚxìng)", "B. 女人 (nǚrén)", "C. 妇女 (fùnǚ)", "D. 女生 (nǚshēng)"],
                "answer": "B. 女人 (nǚrén)",
                "explain": "'女人' (nǚrén - nữ nhân) là từ thông dụng chỉ phụ nữ/nữ giới nói chung. '女性' chỉ giới tính nữ trang trọng.",
                "sound_txt": "女人"
            }
        ]
    },
    "quiz_7": {
        "title": "📝 Đề 7: Từ để hỏi, Định ngữ với 的 & Chỉ định từ (Bài 6 - Bài 7)",
        "description": "Luyện tập hệ thống từ nghi vấn (bao nhiêu, ai, cái gì, ở đâu, tại sao), trợ từ kết cấu 的 biểu thị sở hữu và cụm từ chỉ định 这 / 那.",
        "questions": [
            {
                "question": "Khi muốn hỏi về giá tiền ('Bao nhiêu tiền?'), ta dùng cụm từ nghi vấn nào?",
                "pinyin": "Hỏi giá tiền:",
                "choices": ["A. 多少钱 (duōshao qián)", "B. 几钱 (jǐ qián)", "C. 什么钱 (shénme qián)", "D. 哪里钱 (nǎli qián)"],
                "answer": "A. 多少钱 (duōshao qián)",
                "explain": "Cụm từ để hỏi giá tiền cố định là '多少钱' (duōshao qián). '多少' hỏi số lượng lớn hoặc chưa biết khoảng bao nhiêu.",
                "sound_txt": "多少钱"
            },
            {
                "question": "Chọn đại từ chỉ định dùng để chỉ vật ở khoảng cách xa người nói ('kia / đó'):",
                "pinyin": "Chỉ định từ khoảng cách xa:",
                "choices": ["A. 这 (zhè)", "B. 那 (nà)", "C. 哪 (nǎ)", "D. 谁 (shéi)"],
                "answer": "B. 那 (nà)",
                "explain": "'那' (nà - thanh 4) là chỉ định từ khoảng cách xa ('kia/đó'). Khác với 'clean' (zhè) ở gần, và '哪' (nǎ - thanh 3) là từ dùng để hỏi ('nào').",
                "sound_txt": "那"
            },
            {
                "question": "Chọn từ thích hợp điền vào chỗ trống: “这是我_____汉语老师。” (Đây là giáo viên tiếng Trung của tôi.)",
                "pinyin": "Zhè shì wǒ _____ Hànyǔ lǎoshī.",
                "choices": ["A. 吗 (ma)", "B. 的 (de)", "C. 呢 (ne)", "D. 了 (le)"],
                "answer": "B. 的 (de)",
                "explain": "Trợ từ kết cấu '的' (de) đặt sau đại từ nhân xưng '我' làm định ngữ để xác định quan hệ sở hữu đối với danh từ '汉语老师' (giáo viên tiếng Trung của tôi).",
                "sound_txt": "这是我的汉语老师。"
            },
            {
                "question": "Khi muốn hỏi 'Đây là cái gì?', câu tiếng Trung chính xác là gì?",
                "pinyin": "Hỏi 'Đây là cái gì?':",
                "choices": [
                    "A. 这是谁？ (Zhè shì shéi?)",
                    "B. 这是什么？ (Zhè shì shénme?)",
                    "C. 这是哪儿？ (Zhè shì nǎr?)",
                    "D. 这是怎么样？ (Zhè shì zěnmeyàng?)"
                ],
                "answer": "B. 这是什么？ (Zhè shì shénme?)",
                "explain": "'这是什么' (Zhè shì shénme?) nghĩa là 'Đây là cái gì?'. '什么' là đại từ nghi vấn chỉ vật thể.",
                "sound_txt": "这是什么？"
            },
            {
                "question": "Danh từ chỉ địa điểm 'bệnh viện' trong tiếng Trung viết bằng chữ Hán thế nào?",
                "pinyin": "Bệnh viện:",
                "choices": ["A. 医院 (yīyuàn)", "B. 商店 (shāngdiàn)", "C. 学校 (xuéxiào)", "D. 家 (jiā)"],
                "answer": "A. 医院 (yīyuàn)",
                "explain": "'医院' (yīyuàn) là bệnh viện. '商店' là cửa hàng, '学校' là trường học, '家' là nhà.",
                "sound_txt": "医院"
            },
            {
                "question": "Điền danh từ chỉ phương vị thích hợp: “我的电脑在桌子_____。” (Máy tính của tôi ở trên bàn.)",
                "pinyin": "Wǒ de diànnǎo zài zhuōzi _____.",
                "choices": ["A. 里 (lǐ)", "B. 上 (shàng)", "C. 下 (xià)", "D. 前 (qián)"],
                "answer": "B. 上 (shàng)",
                "explain": "Để biểu thị vật nằm trên bề mặt bàn, dùng danh từ chỉ phương hướng/vị trí '上' (shàng) đứng sau danh từ chính '桌子'.",
                "sound_txt": "我的电脑在桌子上。"
            },
            {
                "question": "Chọn đại từ nghi vấn hỏi về số lượng thường dùng khi ước lượng số lượng nhỏ (thường nhỏ hơn 10):",
                "pinyin": "Hỏi số lượng nhỏ:",
                "choices": ["A. 多少 (duōshao)", "B. 几 (jǐ)", "C. 什么 (shénme)", "D. 谁 (shéi)"],
                "answer": "B. 几 (jǐ)",
                "explain": "'几' (jǐ) dùng hỏi số lượng nhỏ dưới 10 và bắt buộc phải đi kèm lượng từ phía sau (ví dụ: 几个人). '多少' dùng cho số lượng lớn hoặc không giới hạn, không nhất thiết phải có lượng từ.",
                "sound_txt": "几"
            },
            {
                "question": "Điền giới từ thích hợp: “他在学校_____学习汉语。” (Anh ấy học tiếng Trung ở trường.)",
                "pinyin": "Tā _____ xuéxiào xuéxí Hànyǔ.",
                "choices": ["A. 去 (qù)", "B. 在 (zài)", "C. 是 (shì)", "D. 有 (yǒu)"],
                "answer": "B. 在 (zài)",
                "explain": "Giới từ '在' (zài - ở) đặt trước cụm địa điểm '学校' để làm trạng ngữ chỉ nơi chốn diễn ra hành động '学习汉语'.",
                "sound_txt": "他在学校学习汉语。"
            },
            {
                "question": "Chọn câu dịch đúng cho câu: “Cái cốc này bao nhiêu tiền?”",
                "pinyin": "Dịch câu hỏi giá cốc này:",
                "choices": [
                    "A. 那个杯子多少钱？ (Nàge bēizi duōshao qián?)",
                    "B. 这个杯子多少钱？ (Zhège bēizi duōshao qián?)",
                    "C. 这个杯子几块钱？ (Zhège bēizi jǐ kuài qián?)",
                    "D. 哪个杯子多少钱？ (Nǎge bēizi duōshao qián?)"
                ],
                "answer": "B. 这个杯子多少钱？ (Zhège bēizi duōshao qián?)",
                "explain": "'Cái cốc này' là 这个杯子, 'bao nhiêu tiền' là 多少钱. Do đó câu đúng là: 这个杯子多少钱？",
                "sound_txt": "这个杯子多少钱？"
            },
            {
                "question": "Để diễn đạt cụm danh từ sở hữu 'sách của thầy giáo', ta nói như thế nào trong tiếng Trung?",
                "pinyin": "Định ngữ chỉ sở hữu:",
                "choices": [
                    "A. 老师的书 (lǎoshī de shū)",
                    "B. 书的老师 (shū de lǎoshī)",
                    "C. 老师书 (lǎoshī shū)",
                    "D. 书老师 (shū lǎoshī)"
                ],
                "answer": "A. 老师的书 (lǎoshī de shū)",
                "explain": "Trong tiếng Trung, định ngữ đứng trước trung tâm ngữ. 'Thầy giáo' (老师) là chủ thể sở hữu đứng trước, nối bằng '的', 'sách' (书) là vật sở hữu đứng sau.",
                "sound_txt": "老师的书"
            },
            {
                "question": "Đại từ để hỏi '哪儿' (nǎr) dùng để hỏi về thông tin gì?",
                "pinyin": "Ý nghĩa nghi vấn của '哪儿':",
                "choices": [
                    "A. Chỉ người (Ai)",
                    "B. Chỉ địa điểm, nơi chốn (Ở đâu)",
                    "C. Chỉ thời gian (Khi nào)",
                    "D. Chỉ lý do (Tại sao)"
                ],
                "answer": "B. Chỉ địa điểm, nơi chốn (Ở đâu)",
                "explain": "'哪儿' (nǎr - thanh 3, có âm cuốn lưỡi) là đại từ nghi vấn dùng để hỏi về nơi chốn, địa điểm (ở đâu, hướng nào).",
                "sound_txt": "哪儿"
            },
            {
                "question": "Chọn từ thích hợp điền vào chỗ trống: “我不喜欢这个，我要_____。” (Tôi không thích cái này, tôi muốn cái kia.)",
                "pinyin": "Wǒ bù xǐhuan zhège, wào _____.",
                "choices": ["A. 这个 (zhège)", "B. 那个 (nàge)", "C. 哪个 (nǎge)", "D. 什么 (shénme)"],
                "answer": "B. 那个 (nàge)",
                "explain": "'那个' (nàge) chỉ vật ở xa ('cái kia'). Thích hợp để tạo sự đối lập với '这个' (zhège - cái này).",
                "sound_txt": "我要那个。"
            },
            {
                "question": "Lượng từ nào là lượng từ chuyên dùng cho sách vở, tạp chí, từ điển?",
                "pinyin": "Lượng từ của sách:",
                "choices": ["A. 个 (gè)", "B. 本 (běn)", "C. 件 (jiàn)", "D. 口 (kǒu)"],
                "answer": "B. 本 (běn)",
                "explain": "'本' (běn) là lượng từ chuyên dụng đi kèm danh từ sách vở (ví dụ: 一本书 - một cuốn sách).",
                "sound_txt": "本"
            },
            {
                "question": "Cụm câu tiếng Trung '医生在医院工作' dịch sang tiếng Việt có nghĩa là gì?",
                "pinyin": "Dịch câu 'Yīshēng zài yīyuàn gōngzuò':",
                "choices": [
                    "A. Thầy giáo làm việc ở trường học.",
                    "B. Bác sĩ làm việc ở bệnh viện.",
                    "C. Luật sư làm việc ở tòa án.",
                    "D. Bố tôi làm việc ở bệnh viện."
                ],
                "answer": "B. Bác sĩ làm việc ở bệnh viện.",
                "explain": "'医生' (yīshēng) là bác sĩ, '在医院' là ở bệnh viện, '工作' là làm việc. Dịch nghĩa là: Bác sĩ làm việc ở bệnh viện.",
                "sound_txt": "医生在医院工作。"
            },
            {
                "question": "Chọn trợ từ nghi vấn dùng để hỏi tỉnh lược theo ngữ cảnh ('Còn... thì sao?'):",
                "pinyin": "Hỏi tỉnh lược:",
                "choices": ["A. 吗 (ma)", "B. 呢 (ne)", "C. 的 (de)", "D. 吧 (ba)"],
                "answer": "B. 呢 (ne)",
                "explain": "Trợ từ ngữ khí '呢' (ne) đặt sau danh từ hoặc đại từ để tạo thành câu hỏi tỉnh lược (ví dụ: 你呢？ - Còn bạn thì sao?).",
                "sound_txt": "呢"
            }
        ]
    },
    "quiz_8": {
        "title": "📝 Đề 8: Quy tắc chữ Hán & Đàm thoại Thực tế (Bài 8 & Tổng hợp)",
        "description": "Luyện tập các nét chữ Hán cơ bản, quy tắc viết bút thuận, kết cấu chữ Hán, bộ thủ, đàm thoại thực tế giao tiếp xã giao và tổng hợp toàn bộ HSK 1.",
        "questions": [
            {
                "question": "Quy tắc bút thuận cơ bản nào quy định cách viết của chữ Hán có phần bao vây xung quanh và nét bên trong (như chữ '国'):",
                "pinyin": "Quy tắc viết chữ bao quanh:",
                "choices": [
                    "A. Trái trước phải sau",
                    "B. Vào trước đóng sau (先进入后关门)",
                    "C. Giữa trước hai bên sau",
                    "D. Trên trước dưới sau"
                ],
                "answer": "B. Vào trước đóng sau (先进入后关门)",
                "explain": "Quy tắc bút thuận quy định: với các chữ có kết cấu bao quanh (như 国, 回, 园), ta viết khung ngoài trước, viết nội dung bên trong, rồi cuối cùng mới viết nét đóng đáy khung lại (gọi là Vào trước đóng sau).",
                "sound_txt": "国"
            },
            {
                "question": "Chữ Hán '她' (tā - cô ấy) có bộ thủ nào ở bên trái để chỉ giới tính nữ giới?",
                "pinyin": "Bộ thủ của chữ '她':",
                "choices": ["A. Bộ Nhân đứng (亻)", "B. Bộ Nữ (女)", "C. Bộ Vương (王)", "D. Bộ Khẩu (口)"],
                "answer": "B. Bộ Nữ (女)",
                "explain": "Chữ '她' (cô ấy) chứa bộ Nữ '女' ở bên trái làm biểu nghĩa cho phái nữ, giúp phân biệt với '他' (anh ấy - bộ Nhân đứng) và '它' (nó - chỉ vật).",
                "sound_txt": "她"
            },
            {
                "question": "Chọn từ thích hợp điền vào chỗ trống: “A: Xièxie nǐ! - B: _____” (A: Cảm ơn bạn! - B: Không khách khí / Đừng khách sáo.)",
                "pinyin": "Giao tiếp đáp lại lời cảm ơn:",
                "choices": ["A. 不客气 (Bú kèqi)", "B. 对不起 (Duìbuqǐ)", "C. 没关系 (Méi guānxi)", "D. 再见 (Zàijiàn)"],
                "answer": "A. 不客气 (Bú kèqi)",
                "explain": "Khi nhận được lời cảm ơn '谢谢', cách trả lời lịch sự phổ thông nhất là '不客气' (Bú kèqi - Đừng khách sáo/Không có gì).",
                "sound_txt": "不客气"
            },
            {
                "question": "Bộ thủ '口' (bộ Khẩu) trong chữ Hán liên quan đến ý nghĩa gì sau đây?",
                "pinyin": "Ý nghĩa bộ Khẩu '口':",
                "choices": [
                    "A. Cây cối, gỗ",
                    "B. Miệng, ngôn ngữ, ăn uống hoặc hành động liên quan đến miệng",
                    "C. Nước, chất lỏng",
                    "D. Bàn tay, hành động của tay"
                ],
                "answer": "B. Miệng, ngôn ngữ, ăn uống hoặc hành động liên quan đến miệng",
                "explain": "Bộ Khẩu '口' mô phỏng chiếc miệng, biểu thị các chữ liên quan đến ăn uống, nói năng, gọi hoặc các hoạt động phát âm (như 吃, 叫, 听, 吗).",
                "sound_txt": "口"
            },
            {
                "question": "Nét viết chữ Hán nào kéo chéo từ trên xuống dưới và hướng dần sang bên phải?",
                "pinyin": "Nét mác (nà):",
                "choices": ["A. Nét phẩy (撇 - piě)", "B. Nét mác (捺 - nà)", "C. Nét sổ (竖 - shù)", "D. Nét hất (提 - tí)"],
                "answer": "B. Nét mác (捺 - nà)",
                "explain": "Nét mác (捺 - nà) là nét chéo kéo từ trên xuống dưới nghiêng sang bên phải. Ngược với nét phẩy (撇) kéo nghiêng sang trái.",
                "sound_txt": "捺"
            },
            {
                "question": "Bộ thủ '氵' (bộ Chấm thủy) xuất hiện trong các chữ như '汉语', '没' biểu thị ý nghĩa liên quan đến:",
                "pinyin": "Ý nghĩa bộ Chấm thủy '氵':",
                "choices": ["A. Lửa", "B. Nước và chất lỏng", "C. Đất đai", "D. Cây cối"],
                "answer": "B. Nước và chất lỏng",
                "explain": "Bộ Chấm thủy '氵' là biến thể của chữ '水' (nước), biểu thị các chữ liên quan đến nước, sông ngòi hoặc chất lỏng.",
                "sound_txt": "水"
            },
            {
                "question": "Quy tắc bút thuận khi viết chữ '小' (xiǎo - nhỏ) là quy tắc nào?",
                "pinyin": "Quy tắc viết chữ '小':",
                "choices": [
                    "A. Trái trước phải sau",
                    "B. Giữa trước hai bên sau (先中间后两边)",
                    "C. Trên trước dưới sau",
                    "D. Ngang trước sổ sau"
                ],
                "answer": "B. Giữa trước hai bên sau (先中间后两边)",
                "explain": "Với các chữ đối xứng hai bên như '小', '水', quy tắc bút thuận yêu cầu viết nét sổ ở giữa trước, sau đó mới viết các nét đối xứng ở bên trái và bên phải.",
                "sound_txt": "小"
            },
            {
                "question": "Chữ Hán '爸' (bà - bố) thuộc loại kết cấu cấu tạo nào?",
                "pinyin": "Kết cấu chữ '爸':",
                "choices": ["A. Kết cấu Trái - Phải", "B. Kết cấu Trên - Dưới", "C. Kết cấu Bao quanh", "D. Kết cấu Độc thể"],
                "answer": "B. Kết cấu Trên - Dưới",
                "explain": "Chữ '爸' gồm bộ Phụ '父' ở phía trên và chữ '巴' ở phía dưới, thuộc kết cấu Trên - Dưới.",
                "sound_txt": "爸"
            },
            {
                "question": "Chọn câu dịch đúng nhất cho câu: “Xin lỗi, tôi không biết.”",
                "pinyin": "Dịch câu 'Xin lỗi, tôi không biết':",
                "choices": [
                    "A. 没关系，/我不知道。 (Méi guānxi, wǒ bù zhīdào.)",
                    "B. 对不起，/我不认识他。 (Duìbuqǐ, wǒ bú rènshi tā.)",
                    "C. 对不起，/我不知道。 (Duìbuqǐ, wǒ bù zhīdào.)",
                    "D. 谢谢你，/我不知道。 (Xièxie nǐ, wǒ bù zhīdào.)"
                ],
                "answer": "C. 对不起，我不知道。 (Duìbuqǐ, wǒ bù zhīdào.)",
                "explain": "'Xin lỗi' là 对不起 (duìbuqǐ), 'tôi' là 我 (wǒ), 'không biết' là 不知道 (bù zhīdào). Do đó câu đúng là: 对不起，我不知道。",
                "sound_txt": "对不起，我不知道。"
            },
            {
                "question": "Khi có người nói lời xin lỗi với bạn bằng câu '对不起' (Duìbuqǐ), bạn nên đáp lại lịch sự bằng câu nào?",
                "pinyin": "Đáp lại lời xin lỗi:",
                "choices": ["A. 不客气 (Bú kèqi)", "B. 没关系 (Méi guānxi)", "C. 谢谢 (Xièxie)", "D. 再见 (Zàijiàn)"],
                "answer": "B. 没关系 (Méi guānxi)",
                "explain": "Lời đáp lịch sự thông dụng cho câu xin lỗi '对不起' là '没关系' (Méi guānxi - Không sao đâu/Không có gì đáng ngại).",
                "sound_txt": "没关系"
            },
            {
                "question": "Nét viết chữ Hán cơ bản '点' (diǎn) là nét viết nào sau đây?",
                "pinyin": "Nét 点 (diǎn):",
                "choices": ["A. Nét ngang", "B. Nét chấm", "C. Nét phẩy", "D. Nét hất"],
                "answer": "B. Nét chấm",
                "explain": "Nét '点' (diǎn) là nét chấm, đặt bút xuống nhẹ rồi nhấc lên nhanh tạo thành hình giọt nước nhỏ.",
                "sound_txt": "点"
            },
            {
                "question": "Chữ Hán '我' (wǒ - tôi) thuộc loại cấu trúc kết cấu nào sau đây?",
                "pinyin": "Kết cấu chữ '我':",
                "choices": [
                    "A. Kết cấu Độc thể (chữ đơn không ghép bộ)",
                    "B. Kết cấu Trái - Phải",
                    "C. Kết cấu Trên - Dưới",
                    "D. Kết cấu Bao quanh"
                ],
                "answer": "A. Kết cấu Độc thể (chữ đơn không ghép bộ)",
                "explain": "Chữ '我' (tôi) là chữ độc thể (không phân chia thành các phần trái phải hay trên dưới độc lập mà viết liên hoàn từ các nét đơn lẻ).",
                "sound_txt": "我"
            },
            {
                "question": "Chữ Hán nào sau đây có chứa bộ thủ '亻' (Nhân đứng)?",
                "pinyin": "Chữ chứa bộ '亻':",
                "choices": ["A. 她 (tā)", "B. 们 (men)", "C. 国 (guó)", "D. 爸 (bà)"],
                "answer": "B. 们 (men)",
                "explain": "Chữ '们' (men) có bộ Nhân đứng '亻' ở bên trái biểu thị từ chỉ con người số nhiều. '她' có bộ Nữ '女', '国' có bộ vây '囗', '爸' có bộ Phụ '父'.",
                "sound_txt": "们"
            },
            {
                "question": "Chọn từ thích hợp điền vào chỗ trống: “A: Nǐ hǎo ma? - B: Wǒ hěn hǎo, _____ nǐ?” (A: Bạn khỏe không? - B: Tôi rất khỏe, còn bạn?)",
                "pinyin": "Hội thoại hỏi thăm sức khỏe:",
                "choices": ["A. 吗 (ma)", "B. 呢 (ne)", "C. 的 (de)", "D. 了 (le)"],
                "answer": "B. 呢 (ne)",
                "explain": "Trợ từ nghi vấn tỉnh lược '呢' đặt sau đại từ nhân xưng '你' thành '你呢？' (Còn bạn thì sao?) để hỏi ngược lại câu hỏi sức khỏe.",
                "sound_txt": "你呢"
            },
            {
                "question": "Dịch câu sau sang tiếng Trung: 'Ngày mai tôi đi cửa hàng mua cốc.'",
                "pinyin": "Dịch câu đi mua cốc:",
                "choices": [
                    "A. 昨天我去商店买杯子。 (Zuótiān wǒ qù shāngdiàn mǎi bēizi.)",
                    "B. 明天我去商店买杯子。 (Míngtiān wǒ qù shāngdiàn mǎi bēizi.)",
                    "C. 明天我去学校买杯子。 (Míngtiān wǒ qù xuéxiào mǎi bēizi.)",
                    "D. 明天他在商店买杯子。 (Míngtiān tā zài shāngdiàn mǎi bēizi.)"
                ],
                "answer": "B. 明天我去商店买杯子。 (Míngtiān wǒ qù shāngdiàn mǎi bēizi.)",
                "explain": "'Ngày mai' là 明天 (míngtiān), 'tôi' là 我 (wǒ), 'đi cửa hàng' là 去商店 (qù shāngdiàn), 'mua cốc' là 买杯子 (mǎi bēizi). Do đó câu chính xác là: 明天我去商店买杯子。",
                "sound_txt": "明天我去商店买杯子。"
            }
        ]
    }
}

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
        color: #e11d48;
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
    
    /* Selection Cards CSS */
    .quiz-selector-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px -1px rgba(0, 0, 0, 0.006);
        transition: all 0.3s ease;
        margin-bottom: 12px;
        position: relative;
        min-height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .quiz-selector-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 24px -5px rgba(0, 0, 0, 0.08);
        border-color: #cbd5e1;
    }
    .quiz-card-badge {
        position: absolute;
        top: 20px;
        right: 20px;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 700;
    }
    .quiz-card-icon {
        font-size: 2.2rem;
        margin-bottom: 12px;
        text-align: left;
    }
    .quiz-card-title {
        font-size: 1.15rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 8px;
        line-height: 1.35;
        text-align: left;
    }
    .quiz-card-desc {
        font-size: 0.88rem;
        color: #475569;
        line-height: 1.5;
        margin-bottom: 15px;
        text-align: left;
        flex-grow: 1;
    }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "📝 Hệ thống Đề Trắc nghiệm HSK 1"
    )

    # --- KHỞI TẠO STATE CHO QUIZ MỚI ---
    if "hsk1_active_quiz_id" not in st.session_state:
        st.session_state.hsk1_active_quiz_id = None
    if "hsk1_quiz_started" not in st.session_state:
        st.session_state.hsk1_quiz_started = False
    if "hsk1_quiz_idx" not in st.session_state:
        st.session_state.hsk1_quiz_idx = 0
    if "hsk1_quiz_answers" not in st.session_state:
        st.session_state.hsk1_quiz_answers = []
    if "hsk1_quiz_score" not in st.session_state:
        st.session_state.hsk1_quiz_score = 0
    if "hsk1_quiz_submitted" not in st.session_state:
        st.session_state.hsk1_quiz_submitted = False
    if "hsk1_quiz_shuffled_options" not in st.session_state:
        st.session_state.hsk1_quiz_shuffled_options = {}

    # ================= 1. GIAO DIỆN CHỌN ĐỀ (CHƯA BẮT ĐẦU HOẶC CHƯA CHỌN ĐỀ) =================
    if not st.session_state.hsk1_quiz_started or not st.session_state.hsk1_active_quiz_id:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 35px; margin-top: 10px;">
            <h2 style="color: #0f172a; font-weight: 800; font-size: 2.2rem; margin-bottom: 0;">📚 Lựa chọn Đề trắc nghiệm ôn tập</h2>
        </div>
        """, unsafe_allow_html=True)

        # Helper function to start a quiz
        def init_quiz_state(selected_quiz_key):
            questions = QUIZZES_DATA[selected_quiz_key]["questions"]
            st.session_state.hsk1_active_quiz_id = selected_quiz_key
            st.session_state.hsk1_quiz_started = True
            st.session_state.hsk1_quiz_idx = 0
            st.session_state.hsk1_quiz_answers = [None] * len(questions)
            st.session_state.hsk1_quiz_score = 0
            st.session_state.hsk1_quiz_submitted = False
            
            # Xáo trộn đáp án của đề
            shuffled = []
            for i, q in enumerate(questions):
                opts = q["choices"][:]
                random.Random(selected_quiz_key + str(i)).shuffle(opts)
                shuffled.append(opts)
            st.session_state.hsk1_quiz_shuffled_options[selected_quiz_key] = shuffled
            st.rerun()

        # Grid layout (Loop through 8 quizzes in pairs to create a clean responsive grid)
        quiz_metadata = {
            "quiz_1": {"badge": "Bài 1 - Bài 3", "badge_bg": "#dbeafe", "badge_color": "#1e40af", "icon": "🎒", "color": "#3b82f6", "title": "Đề 1: Nhập môn Ngữ âm & Từ vựng"},
            "quiz_2": {"badge": "Bài 4 - Bài 5", "badge_bg": "#f3e8ff", "badge_color": "#6b21a8", "icon": "🌸", "color": "#8b5cf6", "title": "Đề 2: Ngữ âm mở rộng & Số đếm"},
            "quiz_3": {"badge": "Bài 6 - Bài 7", "badge_bg": "#fce7f3", "badge_color": "#9d174d", "icon": "⚡", "color": "#ec4899", "title": "Đề 3: Từ để hỏi & Trợ từ 的"},
            "quiz_4": {"badge": "Bài 8 & Tổng hợp", "badge_bg": "#fef3c7", "badge_color": "#92400e", "icon": "🔥", "color": "#f59e0b", "title": "Đề 4: Chữ Hán & Đàm thoại tổng hợp"},
            "quiz_5": {"badge": "Bài 1 - Bài 3", "badge_bg": "#e0f2fe", "badge_color": "#0369a1", "icon": "📝", "color": "#0ea5e9", "title": "Đề 5: Luyện tập Ngữ âm & Giao tiếp"},
            "quiz_6": {"badge": "Bài 4 - Bài 5", "badge_bg": "#d1fae5", "badge_color": "#065f46", "icon": "📊", "color": "#10b981", "title": "Đề 6: Số đếm & Từ vựng Nữ giới"},
            "quiz_7": {"badge": "Bài 6 - Bài 7", "badge_bg": "#ffedd5", "badge_color": "#9a3412", "icon": "🔍", "color": "#f97316", "title": "Đề 7: Từ để hỏi & Định ngữ"},
            "quiz_8": {"badge": "Bài 8 & Tổng hợp", "badge_bg": "#e2e8f0", "badge_color": "#334155", "icon": "🏆", "color": "#64748b", "title": "Đề 8: Quy tắc bút thuận & Tổng hợp"}
        }

        keys = ["quiz_1", "quiz_2", "quiz_3", "quiz_4", "quiz_5", "quiz_6", "quiz_7", "quiz_8"]
        for row_idx in range(0, len(keys), 2):
            col1, col2 = st.columns(2)
            
            # Left Column Card
            k1 = keys[row_idx]
            meta1 = quiz_metadata[k1]
            with col1:
                st.markdown(f"""
                <div class="quiz-selector-card" style="border-top: 4px solid {meta1['color']};">
                    <div class="quiz-card-badge" style="background-color: {meta1['badge_bg']}; color: {meta1['badge_color']};">{meta1['badge']}</div>
                    <div class="quiz-card-icon">{meta1['icon']}</div>
                    <div class="quiz-card-title">{meta1['title']}</div>
                    <div class="quiz-card-desc">{QUIZZES_DATA[k1]['description']}</div>
                </div>
                """, unsafe_allow_html=True)
                if st.button("🚀 Bắt đầu làm bài", key=f"btn_start_{k1}", type="primary", use_container_width=True):
                    init_quiz_state(k1)
            
            # Right Column Card
            if row_idx + 1 < len(keys):
                k2 = keys[row_idx + 1]
                meta2 = quiz_metadata[k2]
                with col2:
                    st.markdown(f"""
                    <div class="quiz-selector-card" style="border-top: 4px solid {meta2['color']};">
                        <div class="quiz-card-badge" style="background-color: {meta2['badge_bg']}; color: {meta2['badge_color']};">{meta2['badge']}</div>
                        <div class="quiz-card-icon">{meta2['icon']}</div>
                        <div class="quiz-card-title">{meta2['title']}</div>
                        <div class="quiz-card-desc">{QUIZZES_DATA[k2]['description']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button("🚀 Bắt đầu làm bài", key=f"btn_start_{k2}", type="primary", use_container_width=True):
                        init_quiz_state(k2)

    # ================= 2. GIAO DIỆN LÀM BÀI =================
    else:
        active_key = st.session_state.hsk1_active_quiz_id
        quiz_info = QUIZZES_DATA[active_key]
        questions = quiz_info["questions"]
        current_idx = st.session_state.hsk1_quiz_idx

        # Nút Quay lại chọn đề (chỉ khi chưa hoàn thành hoặc muốn đổi)
        if st.sidebar.button("🔙 Chọn đề thi khác", use_container_width=True):
            st.session_state.hsk1_quiz_started = False
            st.session_state.hsk1_active_quiz_id = None
            st.rerun()

        # Khôi phục shuffled options nếu bị mất do hot reload / restart
        if active_key not in st.session_state.hsk1_quiz_shuffled_options:
            shuffled = []
            for i, q in enumerate(questions):
                opts = q["choices"][:]
                random.Random(active_key + str(i)).shuffle(opts)
                shuffled.append(opts)
            st.session_state.hsk1_quiz_shuffled_options[active_key] = shuffled

        # Khôi phục answers list nếu bị trống hoặc lệch độ dài
        if not st.session_state.hsk1_quiz_answers or len(st.session_state.hsk1_quiz_answers) != len(questions):
            st.session_state.hsk1_quiz_answers = [None] * len(questions)

        # Nếu hoàn thành tất cả câu hỏi
        if current_idx >= len(questions):
            show_quiz_results(active_key, questions, save_progress, save_score_row_hsk1_consolidated, load_all_scores_hsk1_consolidated)
            return

        q_data = questions[current_idx]
        shuffled_choices = st.session_state.hsk1_quiz_shuffled_options[active_key][current_idx]
        correct_choice = q_data["answer"]
        user_choice = st.session_state.hsk1_quiz_answers[current_idx]
        is_answered = (user_choice is not None)

        # Thanh tiến độ và số câu hỏi
        percent_done = int((current_idx / len(questions)) * 100)
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; font-weight: bold; color: #475569; margin-bottom: 8px; font-size: 0.95rem;">
            <span>{quiz_info['title']}</span>
            <span>Câu {current_idx + 1} / {len(questions)} ({percent_done}%)</span>
        </div>
        """, unsafe_allow_html=True)
        st.progress(current_idx / len(questions))

        # Khung thẻ câu hỏi chuẩn giao diện
        st.markdown(f"""
        <div class="quiz-card">
            <div class="quiz-q-num">Câu hỏi {current_idx + 1}</div>
            <div class="quiz-q-text">{q_data['question']}</div>
        </div>
        """, unsafe_allow_html=True)

        # Phát âm câu mẫu
        col_audio, col_empty = st.columns([4, 6])
        with col_audio:
            render_play_button(q_data["sound_txt"], "🔊 Phát âm câu hỏi mẫu", key=f"audio_q_{active_key}_{current_idx}")
        st.markdown("<br/>", unsafe_allow_html=True)

        # ================= 2.1 TRẠNG THÁI: CHƯA TRẢ LỜI =================
        if not is_answered:
            st.markdown('<div class="quiz-option-container">', unsafe_allow_html=True)
            for i, choice in enumerate(shuffled_choices):
                if st.button(choice, key=f"btn_choice_{active_key}_{i}_{current_idx}", use_container_width=True):
                    st.session_state.hsk1_quiz_answers[current_idx] = choice
                    if choice == correct_choice:
                        st.session_state.hsk1_quiz_score += 1
                    save_progress()
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        # ================= 2.2 TRẠNG THÁI: ĐÃ TRẢ LỜI =================
        else:
            # Hiển thị các block đáp án tĩnh, tô màu chuẩn
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

            # Khung thông báo và giải thích kết quả
            if user_choice == correct_choice:
                st.success(f"🎉 **Chính xác!**\n\n**Giải thích:** {q_data['explain']}")
            else:
                st.error(f"😢 **Chưa chính xác!** (Bạn đã chọn: {user_choice})\n\n👉 Đáp án đúng là: **{correct_choice}**\n\n**Giải thích:** {q_data['explain']}")

            # Điều hướng
            st.markdown("<br/>", unsafe_allow_html=True)
            col_nav_1, col_nav_2 = st.columns([1, 1])
            with col_nav_1:
                if current_idx > 0:
                    if st.button("⬅️ Câu trước đó", use_container_width=True):
                        st.session_state.hsk1_quiz_idx -= 1
                        st.rerun()
            with col_nav_2:
                btn_label = "Xem kết quả tổng kết 📊" if current_idx == len(questions) - 1 else "Câu tiếp theo ➡️"
                if st.button(btn_label, type="primary", use_container_width=True):
                    st.session_state.hsk1_quiz_idx += 1
                    st.rerun()


def show_quiz_results(active_key, questions, save_progress, save_score_row_hsk1_consolidated, load_all_scores_hsk1_consolidated):
    score = st.session_state.hsk1_quiz_score
    total = len(questions)
    final_score_10 = round((score / total) * 10, 2)
    quiz_title = QUIZZES_DATA[active_key]["title"]

    st.balloons()
    st.markdown(f"""
    <div style="background-color: #fff; border: 2px solid #22c55e; border-radius: 20px; padding: 40px; text-align: center; max-width: 600px; margin: 30px auto; box-shadow: 0 10px 25px rgba(0,0,0,0.05);">
        <span style="font-size: 4rem;">🏆</span>
        <h2 style="color: #1e3a8a; margin-top: 15px; font-weight: 800;">Hoàn thành bài thi!</h2>
        <p style="font-size: 1.1rem; color: #475569; margin-bottom: 25px;">Bạn đã hoàn thành <b>{quiz_title}</b></p>
        <div style="background-color: #f0fdf4; border-radius: 12px; padding: 20px; display: inline-block; margin-bottom: 10px;">
            <span style="font-size: 1.1rem; color: #166534; font-weight: bold; display: block;">KẾT QUẢ ĐẠT ĐƯỢC:</span>
            <span style="font-size: 3rem; color: #15803d; font-weight: 900;">{score} / {total}</span>
            <span style="font-size: 1.3rem; color: #15803d; font-weight: 700; display: block; margin-top: 5px;">({final_score_10} điểm hệ 10)</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Form nộp bài lên data backend (lưu ở CSV)
    if not st.session_state.hsk1_quiz_submitted:
        name = st.text_input("Nhập họ và tên học viên để nộp điểm lên data backend:", placeholder="Ví dụ: Nguyễn Văn A", key="hsk1_quiz_student_name")
        if st.button("💾 Nộp bài & Lưu điểm lên hệ thống", type="primary", use_container_width=True):
            if name:
                row = {
                    "thời gian": datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S"),
                    "học viên": name,
                    "Đề kiểm tra": quiz_title,
                    "tổng điểm": final_score_10,
                    "Kết quả": f"{score}/{total}"
                }
                if save_score_row_hsk1_consolidated(row):
                    st.session_state.hsk1_quiz_submitted = True
                    st.success("Đã nộp bài và lưu điểm số vào data backend thành công!")
                    save_progress()
                    st.rerun()
            else:
                st.error("Vui lòng điền tên trước khi bấm nộp bài!")
    else:
        st.success("Chúc mừng bạn đã nộp bài thành công lên hệ thống data backend!")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔄 Làm lại đề này", use_container_width=True):
            st.session_state.hsk1_quiz_idx = 0
            st.session_state.hsk1_quiz_answers = [None] * len(questions)
            st.session_state.hsk1_quiz_score = 0
            st.session_state.hsk1_quiz_submitted = False
            save_progress()
            st.rerun()
    with col2:
        if st.button("🔙 Trở về danh sách đề thi", use_container_width=True):
            st.session_state.hsk1_quiz_started = False
            st.session_state.hsk1_active_quiz_id = None
            save_progress()
            st.rerun()

    # Bảng xếp hạng nộp bài
    st.markdown("---")
    st.markdown("### 🏆 Bảng xếp hạng nộp bài trắc nghiệm HSK 1")
    all_scores = load_all_scores_hsk1_consolidated()
    if all_scores:
        st.dataframe(all_scores, use_container_width=True)
    else:
        st.info("Chưa có lượt nộp điểm nào cho các đề. Hãy nộp điểm đầu tiên!")
