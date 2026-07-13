# -*- coding: utf-8 -*-
import os
import ast
import json
import csv

def extract_variable_from_file(filepath, var_name, func_name=None):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
            
        class VarExtractor(ast.NodeVisitor):
            def __init__(self):
                self.value = None
                self.in_func = False
                
            def visit_FunctionDef(self, node):
                if func_name and node.name == func_name:
                    self.in_func = True
                    self.generic_visit(node)
                    self.in_func = False
                else:
                    self.generic_visit(node)
                    
            def visit_Assign(self, node):
                if func_name and not self.in_func:
                    self.generic_visit(node)
                    return
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == var_name:
                        self.value = ast.literal_eval(node.value)
                        return
                self.generic_visit(node)
                
        extractor = VarExtractor()
        extractor.visit(tree)
        return extractor.value
    except Exception as e:
        print(f"Error parsing {filepath} for {var_name}: {e}")
        return None

def generate_vocabulary():
    lessons_dir = "lessons"
    all_vocab = []

    # --- BÀI 1 ---
    lessons_data_path = os.path.join(lessons_dir, "lessons_data.py")
    
    # 1. Từ xưng hô dạng từ láy
    xung_ho = extract_variable_from_file(lessons_data_path, "XUNG_HO_TU_LAY")
    if xung_ho:
        for item in xung_ho:
            all_vocab.append({
                "word": item.get("Chữ Hán", ""),
                "pinyin": item.get("Pinyin", ""),
                "vietnamese": item.get("Nghĩa tiếng Việt", ""),
                "lesson": "Bài 1",
                "category": "Từ xưng hô (Láy)",
                "example_han": "",
                "example_py": "",
                "example_vi": ""
            })
            
    # 2. Đại từ xưng hô cơ bản
    dai_tu = extract_variable_from_file(lessons_data_path, "DAI_TU_XUNG_HO")
    if dai_tu:
        for item in dai_tu:
            all_vocab.append({
                "word": item.get("Chữ Hán", ""),
                "pinyin": item.get("Pinyin", ""),
                "vietnamese": item.get("Nghĩa tiếng Việt", ""),
                "lesson": "Bài 1",
                "category": "Đại từ xưng hô",
                "example_han": "",
                "example_py": "",
                "example_vi": ""
            })
            
    # 3. Từ vựng bổ sung
    bo_sung = extract_variable_from_file(lessons_data_path, "TU_VUNG_BO_SUNG")
    if bo_sung:
        for item in bo_sung:
            all_vocab.append({
                "word": item.get("Chữ Hán", ""),
                "pinyin": item.get("Pinyin", ""),
                "vietnamese": item.get("Nghĩa tiếng Việt", ""),
                "lesson": "Bài 1",
                "category": "Từ vựng bổ sung",
                "example_han": "",
                "example_py": "",
                "example_vi": ""
            })

    # --- BÀI 2 ---
    # Trích xuất từ B2_VAN_MAU_KEP_DATA
    b2_data = extract_variable_from_file(lessons_data_path, "B2_VAN_MAU_KEP_DATA")
    if b2_data:
        for group in b2_data:
            g_name = group.get("nhom", "Vận mẫu kép")
            for item in group.get("items", []):
                # Main word
                all_vocab.append({
                    "word": item.get("vd_han", ""),
                    "pinyin": item.get("vd_py", ""),
                    "vietnamese": item.get("vietnamese", ""),
                    "lesson": "Bài 2",
                    "category": f"Vận mẫu {item.get('chu', '')}",
                    "example_han": "",
                    "example_py": "",
                    "example_vi": ""
                })
                # Extra examples
                for ex in item.get("more_examples", []):
                    all_vocab.append({
                        "word": ex.get("han", ""),
                        "pinyin": ex.get("py", ""),
                        "vietnamese": ex.get("vi", ""),
                        "lesson": "Bài 2",
                        "category": f"Ví dụ vận mẫu {item.get('chu', '')}",
                        "example_han": "",
                        "example_py": "",
                        "example_vi": ""
                    })

    # --- BÀI 3 ---
    lesson3_path = os.path.join(lessons_dir, "lesson3.py")
    b3_vocab = extract_variable_from_file(lesson3_path, "vocab_data", "show_lesson3_vocab")
    if b3_vocab:
        for item in b3_vocab:
            all_vocab.append({
                "word": item.get("Chữ Hán", ""),
                "pinyin": item.get("Pinyin", ""),
                "vietnamese": item.get("Nghĩa tiếng Việt", ""),
                "lesson": "Bài 3",
                "category": "Từ vựng",
                "example_han": "",
                "example_py": "",
                "example_vi": ""
            })
    b3_names = extract_variable_from_file(lesson3_path, "names_data", "show_lesson3_vocab")
    if b3_names:
        for item in b3_names:
            all_vocab.append({
                "word": item.get("Chữ Hán", ""),
                "pinyin": item.get("Pinyin", ""),
                "vietnamese": item.get("Nghĩa tiếng Việt", ""),
                "lesson": "Bài 3",
                "category": "Tên riêng",
                "example_han": "",
                "example_py": "",
                "example_vi": ""
            })

    # --- BÀI 4 ---
    lesson4_path = os.path.join(lessons_dir, "lesson4.py")
    b4_vocab = extract_variable_from_file(lesson4_path, "VOCAB_LIST", "show_lesson4_vocab")
    if b4_vocab:
        for item in b4_vocab:
            all_vocab.append({
                "word": item.get("word", ""),
                "pinyin": item.get("pinyin", ""),
                "vietnamese": item.get("vietnamese", ""),
                "lesson": "Bài 4",
                "category": item.get("group", "Từ vựng"),
                "example_han": item.get("example_han", ""),
                "example_py": item.get("example_py", ""),
                "example_vi": item.get("example_vi", "")
            })

    # --- BÀI 5 ---
    lesson5_path = os.path.join(lessons_dir, "lesson5.py")
    b5_vocab = extract_variable_from_file(lesson5_path, "B5_VOCAB", "show_lesson5_vocab")
    if b5_vocab:
        for item in b5_vocab:
            all_vocab.append({
                "word": item.get("word", ""),
                "pinyin": item.get("pinyin", ""),
                "vietnamese": item.get("vietnamese", ""),
                "lesson": "Bài 5",
                "category": "Từ vựng",
                "example_han": item.get("example_han", ""),
                "example_py": item.get("example_py", ""),
                "example_vi": item.get("example_vi", "")
            })

    # --- BÀI 6 ---
    lesson6_path = os.path.join(lessons_dir, "lesson6.py")
    b6_groups = extract_variable_from_file(lesson6_path, "groups", "show_lesson6_vocab")
    if b6_groups:
        for group in b6_groups:
            cat_name = group.get("name", "Từ vựng")
            for item in group.get("items", []):
                all_vocab.append({
                    "word": item.get("word", ""),
                    "pinyin": item.get("pinyin", ""),
                    "vietnamese": item.get("vietnamese", ""),
                    "lesson": "Bài 6",
                    "category": cat_name,
                    "example_han": item.get("example_han", ""),
                    "example_py": item.get("example_py", ""),
                    "example_vi": item.get("example_vi", "")
                })

    # --- BÀI 7 ---
    lesson7_path = os.path.join(lessons_dir, "lesson7.py")
    b7_groups = extract_variable_from_file(lesson7_path, "groups", "show_lesson7_vocab")
    if b7_groups:
        for group in b7_groups:
            cat_name = group.get("name", "Từ vựng")
            for item in group.get("items", []):
                all_vocab.append({
                    "word": item.get("word", ""),
                    "pinyin": item.get("pinyin", ""),
                    "vietnamese": item.get("vietnamese", ""),
                    "lesson": "Bài 7",
                    "category": cat_name,
                    "example_han": item.get("example_han", ""),
                    "example_py": item.get("example_py", ""),
                    "example_vi": item.get("example_vi", "")
                })

    # --- XUẤT RA CÁC FILE ĐẦU RA ---
    os.makedirs("assets", exist_ok=True)
    
    # 1. File JSON
    json_path = os.path.join("assets", "vocabulary.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_vocab, f, ensure_ascii=False, indent=4)
    print(f"Saved {len(all_vocab)} vocabulary items to {json_path}")
    
    # 2. File CSV (Flashcard format)
    csv_path = os.path.join("assets", "vocabulary.csv")
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["word", "pinyin", "vietnamese", "lesson", "category", "example_han", "example_py", "example_vi"])
        writer.writeheader()
        writer.writerows(all_vocab)
    print(f"Saved vocabulary to CSV {csv_path}")

    # 3. File HTML In Ấn (Print friendly layout)
    html_path = os.path.join("assets", "vocabulary_print.html")
    generate_print_html(all_vocab, html_path)
    
    return all_vocab

def generate_print_html(vocab_list, filepath):
    # Group vocabulary by Lesson
    by_lesson = {}
    for item in vocab_list:
        lesson = item["lesson"]
        if lesson not in by_lesson:
            by_lesson[lesson] = []
        by_lesson[lesson].append(item)
        
    html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Bảng Tổng Hợp Từ Vựng Tiếng Trung</title>
    <style>
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            margin: 40px;
            color: #333;
            background-color: #fff;
        }
        h1 {
            text-align: center;
            color: #e11d48;
            font-size: 2.2rem;
            margin-bottom: 5px;
        }
        .subtitle {
            text-align: center;
            color: #64748b;
            font-size: 1rem;
            margin-bottom: 40px;
        }
        .lesson-section {
            page-break-inside: avoid;
            margin-bottom: 40px;
        }
        .lesson-title {
            color: #1e3a8a;
            font-size: 1.5rem;
            border-bottom: 3px solid #e11d48;
            padding-bottom: 8px;
            margin-bottom: 15px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        th, td {
            border: 1px solid #cbd5e1;
            padding: 10px 12px;
            text-align: left;
        }
        th {
            background-color: #f1f5f9;
            color: #1e293b;
            font-weight: bold;
        }
        .word-cell {
            font-size: 1.3rem;
            font-weight: bold;
            color: #e11d48;
            width: 15%;
        }
        .pinyin-cell {
            font-family: 'Courier New', monospace;
            font-weight: bold;
            color: #2563eb;
            width: 18%;
        }
        .viet-cell {
            font-weight: 600;
            color: #334155;
            width: 20%;
        }
        .category-cell {
            font-size: 0.85rem;
            color: #64748b;
            width: 15%;
        }
        .ex-cell {
            font-size: 0.9rem;
            color: #475569;
        }
        .ex-han {
            font-weight: 500;
            color: #0f172a;
        }
        .ex-py {
            font-family: 'Courier New', monospace;
            color: #059669;
            font-size: 0.85rem;
        }
        .ex-vi {
            font-style: italic;
        }
        @media print {
            body {
                margin: 20px;
            }
            .no-print {
                display: none;
            }
            button {
                display: none;
            }
        }
        .print-btn-container {
            text-align: right;
            margin-bottom: 20px;
        }
        .print-btn {
            background-color: #e11d48;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 6px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .print-btn:hover {
            background-color: #be123c;
        }
    </style>
</head>
<body>
    <div class="print-btn-container no-print">
        <button class="print-btn" onclick="window.print()">🖨️ In Bảng Từ Vựng</button>
    </div>
    
    <h1>Bảng Tổng Hợp Từ Vựng Tiếng Trung</h1>
    <div class="subtitle">Đầy đủ từ vựng từ Bài 1 đến Bài 7 (Kèm phiên âm, nghĩa tiếng Việt và ví dụ minh họa)</div>
"""

    for lesson in sorted(by_lesson.keys()):
        html_content += f"""
    <div class="lesson-section">
        <h2 class="lesson-title">{lesson}</h2>
        <table>
            <thead>
                <tr>
                    <th>Chữ Hán</th>
                    <th>Pinyin</th>
                    <th>Nghĩa tiếng Việt</th>
                    <th>Phân loại</th>
                    <th>Ví dụ minh họa</th>
                </tr>
            </thead>
            <tbody>"""
        
        for item in by_lesson[lesson]:
            ex_html = ""
            if item["example_han"]:
                ex_html = f"""<div class="ex-han">{item['example_han']}</div>
<div class="ex-py">{item['example_py']}</div>
<div class="ex-vi">{item['example_vi']}</div>"""
            else:
                ex_html = "<span style='color: #94a3b8; font-style: italic;'>Không có ví dụ</span>"
                
            html_content += f"""
                <tr>
                    <td class="word-cell">{item['word']}</td>
                    <td class="pinyin-cell">{item['pinyin']}</td>
                    <td class="viet-cell">{item['vietnamese']}</td>
                    <td class="category-cell">{item['category']}</td>
                    <td class="ex-cell">{ex_html}</td>
                </tr>"""
                
        html_content += """
            </tbody>
        </table>
    </div>"""
        
    html_content += """
</body>
</html>"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated print HTML at {filepath}")

if __name__ == "__main__":
    generate_vocabulary()
