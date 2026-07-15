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
                "question": "Chọn từ thích hợp điền vào chỗ trống: “我家有_____口人。” (Nhà tôi có ... người.)",
                "pinyin": "Wǒ jiā yǒu _____ kǒu rén.",
                "choices": ["A. 几 (jǐ)", "B. 多少 (duōshao)", "C. 什么 (shénme)", "D. 谁 (shéi)"],
                "answer": "A. 几 (jǐ)",
                "explain": "Để hỏi số lượng thành viên trong gia đình (thường dưới 10 người), ta dùng từ để hỏi '几' (jǐ). Cấu trúc: 几 + lượng từ (口) + danh từ (人).",
                "sound_txt": "我家有几口人？"
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

        # Grid layout (2 rows, 2 columns)
        row1_col1, row1_col2 = st.columns(2)
        row2_col1, row2_col2 = st.columns(2)

        # Quiz 1 Card
        with row1_col1:
            st.markdown(f"""
            <div class="quiz-selector-card" style="border-top: 4px solid #3b82f6;">
                <div class="quiz-card-badge" style="background-color: #dbeafe; color: #1e40af;">Bài 1 - Bài 3</div>
                <div class="quiz-card-icon">🎒</div>
                <div class="quiz-card-title">Đề 1: Nhập môn Ngữ âm & Từ vựng</div>
                <div class="quiz-card-desc">{QUIZZES_DATA['quiz_1']['description']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("🚀 Bắt đầu làm bài", key="btn_start_quiz_1", type="primary", use_container_width=True):
                init_quiz_state("quiz_1")

        # Quiz 2 Card
        with row1_col2:
            st.markdown(f"""
            <div class="quiz-selector-card" style="border-top: 4px solid #8b5cf6;">
                <div class="quiz-card-badge" style="background-color: #f3e8ff; color: #6b21a8;">Bài 4 - Bài 5</div>
                <div class="quiz-card-icon">🌸</div>
                <div class="quiz-card-title">Đề 2: Ngữ âm mở rộng & Số đếm</div>
                <div class="quiz-card-desc">{QUIZZES_DATA['quiz_2']['description']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("🚀 Bắt đầu làm bài", key="btn_start_quiz_2", type="primary", use_container_width=True):
                init_quiz_state("quiz_2")

        # Quiz 3 Card
        with row2_col1:
            st.markdown(f"""
            <div class="quiz-selector-card" style="border-top: 4px solid #ec4899;">
                <div class="quiz-card-badge" style="background-color: #fce7f3; color: #9d174d;">Bài 6 - Bài 7</div>
                <div class="quiz-card-icon">⚡</div>
                <div class="quiz-card-title">Đề 3: Từ để hỏi & Trợ từ 的</div>
                <div class="quiz-card-desc">{QUIZZES_DATA['quiz_3']['description']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("🚀 Bắt đầu làm bài", key="btn_start_quiz_3", type="primary", use_container_width=True):
                init_quiz_state("quiz_3")

        # Quiz 4 Card
        with row2_col2:
            st.markdown(f"""
            <div class="quiz-selector-card" style="border-top: 4px solid #f59e0b;">
                <div class="quiz-card-badge" style="background-color: #fef3c7; color: #92400e;">Bài 8 & Tổng hợp</div>
                <div class="quiz-card-icon">🔥</div>
                <div class="quiz-card-title">Đề 4: Chữ Hán & Đàm thoại tổng hợp</div>
                <div class="quiz-card-desc">{QUIZZES_DATA['quiz_4']['description']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("🚀 Bắt đầu làm bài", key="btn_start_quiz_4", type="primary", use_container_width=True):
                init_quiz_state("quiz_4")

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
            <div class="quiz-q-pinyin">Pinyin: {q_data['pinyin']}</div>
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
