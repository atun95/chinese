import os

file_path = 'c:/Users/lyquo/OneDrive/Desktop/chinese/a.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add import
if 'import lessons.lesson9 as lesson9' not in content:
    content = content.replace('import lessons.lesson8 as lesson8\n', 
                            'import lessons.lesson8 as lesson8\nimport lessons.lesson9 as lesson9\n')

# Add reload
reload_block = '''try:
    importlib.reload(lesson8)
except Exception as e:
    pass'''
new_reload = '''try:
    importlib.reload(lesson8)
except Exception as e:
    pass

try:
    importlib.reload(lesson9)
except Exception as e:
    pass'''
if 'importlib.reload(lesson9)' not in content:
    content = content.replace(reload_block, new_reload)

# Add to menu options
menu_8_5 = '"Bài 8.5 - Đơn thể & Hợp thể"'
new_menu_9_1 = '"Bài 9.1 - Quốc gia, Quốc tịch và Tiền tệ"'
if new_menu_9_1 not in content:
    content = content.replace(menu_8_5 + '\n      ]', menu_8_5 + ',\n          ' + new_menu_9_1 + '\n      ]')
    
    # Try another variation in case there is a comma
    content = content.replace(menu_8_5 + ',\n      ]', menu_8_5 + ',\n          ' + new_menu_9_1 + '\n      ]')

# Add handler
handler_8_5 = '''elif menu == "Bài 8.5 - Đơn thể & Hợp thể":
    lesson8.show_lesson8_5_structures()'''
new_handler = '''elif menu == "Bài 8.5 - Đơn thể & Hợp thể":
    lesson8.show_lesson8_5_structures()
    
elif menu == "Bài 9.1 - Quốc gia, Quốc tịch và Tiền tệ":
    lesson9.show_lesson9_1_countries_currency()'''
if 'lesson9.show_lesson9_1_countries_currency()' not in content:
    content = content.replace(handler_8_5, new_handler)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("a.py updated.")
