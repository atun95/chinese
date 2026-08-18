import os

file_path = 'c:/Users/lyquo/OneDrive/Desktop/chinese/a.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add to menu options under mode == "🗣️ Thực hành trên lớp":
old_menu_6_1 = '"Bài 6.1 - Thực hành Giao tiếp & Phản xạ"'
new_menu_9_1 = '"Bài 9.1 - Thực hành Giao tiếp & Phản xạ"'

if new_menu_9_1 not in content:
    content = content.replace(old_menu_6_1 + '\n      ]', old_menu_6_1 + ',\n          ' + new_menu_9_1 + '\n      ]')
    
    # Try another variation in case there is a comma
    content = content.replace(old_menu_6_1 + ',\n      ]', old_menu_6_1 + ',\n          ' + new_menu_9_1 + '\n      ]')

# Add handler
handler_6_1 = '''elif menu == "Bài 6.1 - Thực hành Giao tiếp & Phản xạ":
    lesson6.show_lesson6_1_classroom_practice()'''
new_handler = '''elif menu == "Bài 6.1 - Thực hành Giao tiếp & Phản xạ":
    lesson6.show_lesson6_1_classroom_practice()
    
elif menu == "Bài 9.1 - Thực hành Giao tiếp & Phản xạ":
    lesson9.show_lesson9_1_classroom_practice()'''
if 'lesson9.show_lesson9_1_classroom_practice()' not in content:
    content = content.replace(handler_6_1, new_handler)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("a.py practice menu updated.")
