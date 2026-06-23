# -*- coding: utf-8 -*-
with open("build_giao_trinh.py", "r", encoding="utf-8") as f:
    content = f.read()

# Fix 1: bù ① in Lesson 3
content = content.replace("bù ①", "bù shì")

# Fix 2: 他tên và 你sẽ in Lesson 3 Markdown comparison table
old_table_row = '| **Ý nghĩa:** Định danh, biểu thị quan hệ tương đương.<br>**Khẳng định:** S + 是 + O<br>*Ví dụ:* 我是老师 (Tôi là giáo viên).<br>**Phủ định:** S + 不是 + O<br>*Ví dụ:* 他tên...不是学生 (Anh ấy không phải học sinh).<br>**Nghi vấn:** S + 是 + O + 吗？<br>*Ví dụ:* 你sẽ...学生吗？ (Bạn là học sinh phải không?) |'
# Let's search by a smaller substring to be safe
content = content.replace("他tên...不是学生", "他不是学生")
content = content.replace("你sẽ...学生吗？", "你是学生吗？")
content = content.replace("他tiếng không có bạn gái", "他没有女朋友")

# Fix 3: 她es my 女儿 in Lesson 4
content = content.replace("她是 my 女儿", "她是我的女儿")

# Fix 4: 挺... của in Lesson 5
content = content.replace("挺... của <span class=\"pinyin\">tǐng...de</span>", "挺...的 <span class=\"pinyin\">tǐng...de</span>")

# Fix 5: 太... lự in Lesson 5
content = content.replace("太... lự <span class=\"pinyin\">tài...le</span>", "太...了 <span class=\"pinyin\">tài...le</span>")

with open("build_giao_trinh.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Fix completed successfully!")
