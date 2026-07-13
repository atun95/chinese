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

    # 4. File App Offline Tương Tác
    app_offline_path = "Flashcard_Offline.html"
    generate_offline_app(all_vocab, app_offline_path)
    
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

def generate_offline_app(vocab_list, filepath):
    import json
    embedded_json = json.dumps(vocab_list, ensure_ascii=False, indent=4)
    
    html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thẻ từ Ôn tập Từ vựng HSK 1 (Offline)</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/hanzi-writer@2.2/dist/hanzi-writer.min.js"></script>
    <style>
        :root {{
            --primary: #e11d48;
            --primary-hover: #be123c;
            --bg-body: #f8fafc;
            --bg-card: #ffffff;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --border-color: #e2e8f0;
        }}
        
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Inter', sans-serif;
        }}

        body {{
            background-color: var(--bg-body);
            color: var(--text-main);
            display: flex;
            min-height: 100vh;
            flex-direction: column;
        }}

        header {{
            background-color: var(--bg-card);
            border-bottom: 1px solid var(--border-color);
            padding: 16px 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);
            position: sticky;
            top: 0;
            z-index: 100;
        }}

        .header-title {{
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 1.25rem;
            font-weight: 800;
            color: var(--primary);
        }}

        .header-subtitle {{
            font-size: 0.875rem;
            color: var(--text-muted);
            margin-left: auto;
            margin-right: 20px;
        }}

        .main-container {{
            display: flex;
            flex: 1;
            max-width: 1400px;
            width: 100%;
            margin: 0 auto;
            padding: 24px;
            gap: 24px;
        }}

        .sidebar {{
            width: 320px;
            background-color: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 24px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            align-self: flex-start;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);
        }}

        .content-area {{
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 20px;
            align-items: center;
        }}

        .form-group {{
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}

        .form-group label {{
            font-size: 0.85rem;
            font-weight: 700;
            color: var(--text-main);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        .form-control {{
            width: 100%;
            padding: 10px 14px;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            font-size: 0.95rem;
            background-color: #f8fafc;
            color: var(--text-main);
            transition: all 0.2s;
        }}

        .form-control:focus {{
            outline: none;
            border-color: var(--primary);
            background-color: #fff;
            box-shadow: 0 0 0 3px rgba(225, 29, 72, 0.15);
        }}

        /* 3D Card Container */
        .card-scene {{
            width: 100%;
            max-width: 650px;
            height: 400px;
            perspective: 1000px;
            cursor: pointer;
        }}

        .flashcard {{
            width: 100%;
            height: 100%;
            position: relative;
            transform-style: preserve-3d;
            transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
            border-radius: 24px;
            box-shadow: 0 20px 25px -5px rgba(0,0,0,0.08);
        }}

        .flashcard.flipped {{
            transform: rotateY(180deg);
        }}

        .card-face {{
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            border-radius: 24px;
            padding: 30px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            border: 2px solid var(--border-color);
            background-color: var(--bg-card);
        }}

        .card-front {{
            background: linear-gradient(135deg, #ffffff 0%, #fcfdfd 100%);
        }}

        .card-back {{
            transform: rotateY(180deg);
            background: linear-gradient(135deg, #ffffff 0%, #fafbfc 100%);
        }}

        .word-chinese {{
            font-size: 3.5rem;
            font-weight: 800;
            color: var(--primary);
            margin-bottom: 20px;
            letter-spacing: 2px;
        }}

        .word-pinyin {{
            font-family: monospace;
            font-size: 1.6rem;
            font-weight: 700;
            color: #2563eb;
            background-color: #eff6ff;
            padding: 4px 18px;
            border-radius: 30px;
            border: 1px solid #dbeafe;
            margin-bottom: 12px;
        }}

        .word-translation {{
            font-size: 1.5rem;
            font-weight: 700;
            color: #1e293b;
            margin-bottom: 20px;
            text-align: center;
        }}

        /* Stroke anim container */
        .stroke-container {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            justify-content: center;
            margin-top: 10px;
            margin-bottom: 15px;
        }}

        .hanzi-char-box {{
            width: 90px;
            height: 90px;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            background: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);
            transition: transform 0.2s;
        }}

        .hanzi-char-box:hover {{
            transform: scale(1.03);
            border-color: var(--primary);
        }}

        .card-example {{
            width: 100%;
            background-color: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 16px;
            margin-top: auto;
            text-align: left;
        }}

        .example-title {{
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            color: var(--text-muted);
            margin-bottom: 4px;
        }}

        .example-han {{
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 2px;
        }}

        .example-py {{
            font-family: monospace;
            font-size: 0.85rem;
            color: #059669;
            margin-bottom: 4px;
        }}

        .example-vi {{
            font-size: 0.82rem;
            font-style: italic;
            color: var(--text-muted);
        }}

        /* Learn Card styling (No Flip) */
        .learn-card {{
            width: 100%;
            max-width: 650px;
            background: #ffffff;
            border-radius: 24px;
            padding: 30px;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.08);
            border: 1px solid var(--border-color);
            margin-bottom: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}

        .learn-card-body {{
            display: flex;
            width: 100%;
            justify-content: space-around;
            align-items: center;
            flex-wrap: wrap;
            gap: 20px;
        }}

        .learn-word-section {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-width: 180px;
        }}

        .learn-details-section {{
            flex: 1;
            min-width: 250px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}

        .detail-item {{
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}

        .detail-label {{
            font-size: 0.85rem;
            color: var(--text-muted);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        /* Audio buttons */
        .btn-audio {{
            border: 1px solid var(--border-color);
            background-color: #fff;
            color: var(--text-main);
            padding: 6px 12px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s;
            margin-top: 6px;
            font-size: 0.85rem;
        }}

        .btn-audio:hover {{
            background-color: #eff6ff;
            border-color: #3b82f6;
            color: #2563eb;
        }}

        /* Controls */
        .controls {{
            display: flex;
            gap: 16px;
            width: 100%;
            max-width: 650px;
            margin-top: 10px;
        }}

        .btn {{
            flex: 1;
            padding: 12px 20px;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            font-size: 0.95rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            display: inline-flex;
            justify-content: center;
            align-items: center;
            gap: 8px;
        }}

        .btn-primary {{
            background-color: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
        }}

        .btn-primary:hover {{
            background-color: var(--primary-hover);
        }}

        .btn-secondary {{
            background-color: #ffffff;
            color: var(--text-main);
        }}

        .btn-secondary:hover {{
            background-color: #f1f5f9;
        }}

        /* Progress */
        .progress-container {{
            width: 100%;
            max-width: 650px;
            display: flex;
            flex-direction: column;
            gap: 6px;
            margin-top: 20px;
        }}

        .progress-bar-bg {{
            width: 100%;
            height: 8px;
            background-color: var(--border-color);
            border-radius: 10px;
            overflow: hidden;
        }}

        .progress-bar-fill {{
            height: 100%;
            width: 0%;
            background-color: var(--primary);
            transition: width 0.3s ease;
        }}

        .progress-text {{
            display: flex;
            justify-content: space-between;
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--text-muted);
        }}

        /* Mode Selector */
        .mode-selector {{
            display: flex;
            background-color: #e2e8f0;
            padding: 4px;
            border-radius: 10px;
            margin-bottom: 20px;
        }}

        .mode-btn {{
            flex: 1;
            padding: 8px 12px;
            border: none;
            background: none;
            font-size: 0.85rem;
            font-weight: 700;
            cursor: pointer;
            border-radius: 8px;
            transition: all 0.2s;
        }}

        .mode-btn.active {{
            background-color: #ffffff;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            color: var(--primary);
        }}

        /* Table view */
        .table-view {{
            width: 100%;
            max-width: 900px;
            background-color: #fff;
            border: 1px solid var(--border-color);
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);
            display: none;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
        }}

        th, td {{
            padding: 12px 16px;
            border-bottom: 1px solid var(--border-color);
        }}

        th {{
            background-color: #f8fafc;
            font-weight: 700;
            color: var(--text-muted);
            font-size: 0.85rem;
            text-transform: uppercase;
        }}

        tr:last-child td {{
            border-bottom: none;
        }}

        .badge {{
            display: inline-block;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 600;
            background-color: #f1f5f9;
            color: #475569;
        }}

        /* Mobile Responsive */
        @media (max-width: 768px) {{
            .main-container {{
                flex-direction: column;
                padding: 16px;
            }}
            .sidebar {{
                width: 100%;
            }}
            .card-scene {{
                height: 340px;
            }}
            .word-chinese {{
                font-size: 3rem;
            }}
            .word-pinyin {{
                font-size: 1.4rem;
            }}
            .word-translation {{
                font-size: 1.3rem;
            }}
            .learn-card-body {{
                flex-direction: column;
                text-align: center;
                gap: 15px;
            }}
            .learn-details-section {{
                width: 100%;
                align-items: center;
                text-align: center;
            }}
        }}
    </style>
</head>
<body>
    <header>
        <div class="header-title">
            <span>🇨🇳</span> HSK 1 - THẺ TỪ ÔN TẬP TỰ VỰNG
        </div>
    </header>

    <div class="main-container">
        <div class="sidebar">
            <div class="form-group">
                <label>Chế độ hiển thị</label>
                <div class="mode-selector">
                    <button class="mode-btn active" onclick="switchView('learn')">📖 Học tập</button>
                    <button class="mode-btn" onclick="switchView('card')">🎴 Luyện tập</button>
                    <button class="mode-btn" onclick="switchView('table')">📋 Danh sách</button>
                </div>
            </div>

            <div class="form-group">
                <label for="sel-lesson">Chọn Bài học</label>
                <select id="sel-lesson" class="form-control" onchange="applyFilters()">
                    <option value="Tất cả">Tất cả bài học</option>
                </select>
            </div>



            <div class="form-group">
                <label for="search-input">Tìm kiếm</label>
                <input type="text" id="search-input" class="form-control" placeholder="Tìm Hán tự, Pinyin, nghĩa..." oninput="applyFilters()">
            </div>


        </div>

        <div class="content-area">
            <!-- Learn View Mode (No Flip) -->
            <div id="learn-view-mode" style="width: 100%; display: flex; flex-direction: column; align-items: center;">
                <div class="learn-card">
                    <div class="learn-card-body">
                        <div class="learn-word-section">
                            <div id="learn-word" class="word-chinese"></div>
                            <button id="learn-speak-btn" class="btn-audio" style="margin-top: 15px;" onclick="speakCurrentWord()">🔊 Phát âm</button>
                        </div>
                        <div class="learn-details-section">
                            <div class="detail-item">
                                <span class="detail-label">Pinyin:</span>
                                <span id="learn-pinyin" class="word-pinyin"></span>
                            </div>
                            <div class="detail-item">
                                <span class="detail-label">Nghĩa tiếng Việt:</span>
                                <span id="learn-viet" class="word-translation" style="text-align: left; margin-bottom: 0;"></span>
                            </div>
                            
                            <!-- Example sentences -->
                            <div id="learn-example" class="card-example" style="margin-top: 10px; display: none;"></div>
                        </div>
                    </div>
                    
                    <!-- Stroke animation for characters -->
                    <div class="stroke-section" style="margin-top: 25px; border-top: 1px solid var(--border-color); padding-top: 20px; width: 100%; text-align: center;">
                        <h4 style="font-size: 0.85rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); margin-bottom: 15px; letter-spacing: 0.05em;">Hướng dẫn viết nét chữ Hán (Bấm vào chữ để vẽ nét):</h4>
                        <div id="learn-stroke-area" class="stroke-container"></div>
                    </div>
                </div>

                <div class="controls">
                    <button class="btn btn-secondary" onclick="prevCard()">⬅️ Từ trước</button>
                    <button class="btn btn-secondary" onclick="nextCard()">Từ sau ➡️</button>
                </div>

                <div class="progress-container">
                    <div class="progress-text">
                        <span id="learn-progress-info">Từ 0 / 0</span>
                        <span id="learn-percent-info">0%</span>
                    </div>
                    <div class="progress-bar-bg">
                        <div id="learn-progress-fill" class="progress-bar-fill"></div>
                    </div>
                </div>
            </div>

            <!-- Card View Mode -->
            <div id="card-view-mode" style="width: 100%; display: none; flex-direction: column; align-items: center;">
                <div class="card-scene" onclick="flipCard()">
                    <div id="flashcard" class="flashcard">
                        <!-- Front Face -->
                        <div class="card-face card-front">
                            <div id="front-word" class="word-chinese"></div>
                            <div id="front-stroke-area" class="stroke-container" onclick="event.stopPropagation()"></div>
                            <div style="font-size: 0.85rem; color: var(--text-muted); font-style: italic; margin-top: 10px;">
                                (Bấm vào chữ để xem viết nét, nhấp vào nền để lật thẻ)
                            </div>
                        </div>
                        
                        <!-- Back Face -->
                        <div class="card-face card-back">
                            <div id="back-word" class="word-chinese" style="font-size: 2.2rem; margin-bottom: 4px;"></div>
                            <div id="back-pinyin" class="word-pinyin"></div>
                            <div id="back-viet" class="word-translation"></div>
                            
                            <!-- Stroke animation for characters -->
                            <div id="stroke-area" class="stroke-container" onclick="event.stopPropagation()"></div>
                            
                            <!-- Example sentences -->
                            <div id="back-example" class="card-example"></div>
                        </div>
                    </div>
                </div>

                <div class="controls">
                    <button class="btn btn-secondary" onclick="prevCard()">⬅️ Từ trước</button>
                    <button class="btn btn-primary" onclick="flipCard()">👁️ Lật thẻ</button>
                    <button class="btn btn-secondary" onclick="nextCard()">Từ sau ➡️</button>
                </div>

                <div class="progress-container">
                    <div class="progress-text">
                        <span id="progress-info">Từ 0 / 0</span>
                        <span id="percent-info">0%</span>
                    </div>
                    <div class="progress-bar-bg">
                        <div id="progress-fill" class="progress-bar-fill"></div>
                    </div>
                </div>
            </div>

            <!-- Table View Mode -->
            <div id="table-view-mode" class="table-view">
                <table>
                    <thead>
                        <tr>
                            <th>STT</th>
                            <th>Bài</th>
                            <th>Hán tự</th>
                            <th>Pinyin</th>
                            <th>Nghĩa tiếng Việt</th>
                            <th>Nhóm từ</th>
                            <th>Phát âm</th>
                        </tr>
                    </thead>
                    <tbody id="table-body">
                        <!-- Filled by JS -->
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <script>
        const VOCABULARY = {embedded_json};
        
        let activeVocab = [...VOCABULARY];
        let currentIndex = 0;
        let activeWritersFront = [];
        let activeWritersBack = [];
        let activeWritersLearn = [];

        window.addEventListener('DOMContentLoaded', () => {{
            populateFilters();
            applyFilters();
        }});

        function populateFilters() {{
            const lessons = new Set();
            const categories = new Set();
            VOCABULARY.forEach(item => {{
                if (item.lesson) lessons.add(item.lesson);
                if (item.category) categories.add(item.category);
            }});

            const selLesson = document.getElementById('sel-lesson');
            Array.from(lessons).sort().forEach(les => {{
                const opt = document.createElement('option');
                opt.value = les;
                opt.textContent = les;
                selLesson.appendChild(opt);
            }});
        }}

        function applyFilters() {{
            const selectedLesson = document.getElementById('sel-lesson').value;
            const searchQuery = document.getElementById('search-input').value.toLowerCase().trim();

            activeVocab = VOCABULARY.filter(item => {{
                const matchesLesson = selectedLesson === 'Tất cả' || item.lesson === selectedLesson;
                const matchesSearch = !searchQuery || 
                    item.word.toLowerCase().includes(searchQuery) ||
                    item.pinyin.toLowerCase().includes(searchQuery) ||
                    item.vietnamese.toLowerCase().includes(searchQuery);
                return matchesLesson && matchesSearch;
            }});

            currentIndex = 0;
            updateUI();
            updateTable();
        }}

        function shuffleVocabulary() {{
            for (let i = activeVocab.length - 1; i > 0; i--) {{
                const j = Math.floor(Math.random() * (i + 1));
                [activeVocab[i], activeVocab[j]] = [activeVocab[j], activeVocab[i]];
            }}
            currentIndex = 0;
            updateUI();
            updateTable();
        }}

        function switchView(view) {{
            const learnMode = document.getElementById('learn-view-mode');
            const cardMode = document.getElementById('card-view-mode');
            const tableMode = document.getElementById('table-view-mode');
            const buttons = document.querySelectorAll('.mode-btn');

            buttons.forEach(btn => btn.classList.remove('active'));

            if (view === 'learn') {{
                learnMode.style.display = 'flex';
                cardMode.style.display = 'none';
                tableMode.style.display = 'none';
                buttons[0].classList.add('active');
                updateUI();
            }} else if (view === 'card') {{
                learnMode.style.display = 'none';
                cardMode.style.display = 'flex';
                tableMode.style.display = 'none';
                buttons[1].classList.add('active');
                updateUI();
            }} else {{
                learnMode.style.display = 'none';
                cardMode.style.display = 'none';
                tableMode.style.display = 'block';
                buttons[2].classList.add('active');
                updateTable();
            }}
        }}

        function flipCard() {{
            const card = document.getElementById('flashcard');
            card.classList.toggle('flipped');
            
            if (card.classList.contains('flipped')) {{
                initStrokeWritersBack();
            }} else {{
                initStrokeWritersFront();
            }}
        }}

        function updateUI() {{
            const card = document.getElementById('flashcard');
            card.classList.remove('flipped');

            // Learn mode elements
            const learnWord = document.getElementById('learn-word');
            const learnPinyin = document.getElementById('learn-pinyin');
            const learnViet = document.getElementById('learn-viet');
            const learnExBox = document.getElementById('learn-example');

            if (activeVocab.length === 0) {{
                document.getElementById('front-word').textContent = '⚠️ Trống';
                document.getElementById('back-word').textContent = '⚠️ Trống';
                document.getElementById('back-pinyin').textContent = '';
                document.getElementById('back-viet').textContent = 'Vui lòng chọn bộ lọc khác';
                document.getElementById('back-example').style.display = 'none';
                document.getElementById('progress-info').textContent = 'Từ 0 / 0';
                document.getElementById('percent-info').textContent = '0%';
                document.getElementById('progress-fill').style.width = '0%';

                if (learnWord) {{
                    learnWord.textContent = '⚠️ Trống';
                    learnPinyin.textContent = '';
                    learnViet.textContent = 'Vui lòng chọn bộ lọc khác';
                    learnExBox.style.display = 'none';
                    document.getElementById('learn-progress-info').textContent = 'Từ 0 / 0';
                    document.getElementById('learn-percent-info').textContent = '0%';
                    document.getElementById('learn-progress-fill').style.width = '0%';
                }}
                return;
            }}

            const item = activeVocab[currentIndex];
            document.getElementById('front-word').textContent = item.word;
            document.getElementById('back-word').textContent = item.word;
            document.getElementById('back-pinyin').textContent = item.pinyin;
            document.getElementById('back-viet').textContent = item.vietnamese;

            const exBox = document.getElementById('back-example');
            if (item.example_han) {{
                exBox.style.display = 'block';
                exBox.innerHTML = `
                    <div class="example-title">Ví dụ minh họa:</div>
                    <div class="example-han">${{item.example_han}}</div>
                    <div class="example-py">${{item.example_py}}</div>
                    <div class="example-vi">${{item.example_vi}}</div>
                    <button class="btn-audio" onclick="speak('${{item.example_han}}')">🔊 Nghe câu ví dụ</button>
                `;
            }} else {{
                exBox.style.display = 'none';
            }}

            const total = activeVocab.length;
            const currentNum = currentIndex + 1;
            const percent = Math.round((currentNum / total) * 100);
            
            document.getElementById('progress-info').textContent = `Từ ${{currentNum}} / ${{total}}`;
            document.getElementById('percent-info').textContent = `${{percent}}%`;
            document.getElementById('progress-fill').style.width = `${{percent}}%`;

            // Update learn view UI
            if (learnWord) {{
                learnWord.textContent = item.word;
                learnPinyin.textContent = item.pinyin;
                learnViet.textContent = item.vietnamese;

                if (item.example_han) {{
                    learnExBox.style.display = 'block';
                    learnExBox.innerHTML = `
                        <div class="example-title">Ví dụ minh họa:</div>
                        <div class="example-han">${{item.example_han}}</div>
                        <div class="example-py">${{item.example_py}}</div>
                        <div class="example-vi">${{item.example_vi}}</div>
                        <button class="btn-audio" onclick="speak('${{item.example_han}}')">🔊 Nghe câu ví dụ</button>
                    `;
                }} else {{
                    learnExBox.style.display = 'none';
                }}

                document.getElementById('learn-progress-info').textContent = `Từ ${{currentNum}} / ${{total}}`;
                document.getElementById('learn-percent-info').textContent = `${{percent}}%`;
                document.getElementById('learn-progress-fill').style.width = `${{percent}}%`;
            }}

            initStrokeWritersFront();
            initStrokeWritersLearn();
            speak(item.word);
        }}

        function initStrokeWritersFront() {{
            const item = activeVocab[currentIndex];
            const container = document.getElementById('front-stroke-area');
            container.innerHTML = '';
            activeWritersFront = [];

            if (!item) return;
            const chars = item.word.split('').filter(c => /[\\u4e00-\\u9fa5]/.test(c));

            chars.forEach((char, idx) => {{
                const charBox = document.createElement('div');
                charBox.className = 'hanzi-char-box';
                charBox.id = `front-char-box-${{idx}}`;
                container.appendChild(charBox);

                try {{
                    const writer = HanziWriter.create(charBox.id, char, {{
                        width: 80,
                        height: 80,
                        padding: 5,
                        showOutline: true,
                        strokeColor: '#e11d48',
                        outlineColor: '#f8fafc',
                        strokeAnimationSpeed: 1.5
                    }});
                    activeWritersFront.push(writer);
                    charBox.addEventListener('click', (e) => {{
                        e.stopPropagation();
                        writer.animateCharacter();
                    }});
                    setTimeout(() => writer.animateCharacter(), idx * 400);
                }} catch (e) {{
                    charBox.textContent = char;
                }}
            }});
        }}

        function initStrokeWritersLearn() {{
            const item = activeVocab[currentIndex];
            const container = document.getElementById('learn-stroke-area');
            container.innerHTML = '';
            activeWritersLearn = [];

            if (!item) return;
            const chars = item.word.split('').filter(c => /[\\u4e00-\\u9fa5]/.test(c));

            chars.forEach((char, idx) => {{
                const charBox = document.createElement('div');
                charBox.className = 'hanzi-char-box';
                charBox.id = `learn-char-box-${{idx}}`;
                container.appendChild(charBox);

                try {{
                    const writer = HanziWriter.create(charBox.id, char, {{
                        width: 80,
                        height: 80,
                        padding: 5,
                        showOutline: true,
                        strokeColor: '#e11d48',
                        outlineColor: '#f8fafc',
                        strokeAnimationSpeed: 1.5
                    }});
                    activeWritersLearn.push(writer);
                    charBox.addEventListener('click', (e) => {{
                        e.stopPropagation();
                        writer.animateCharacter();
                    }});
                    setTimeout(() => writer.animateCharacter(), idx * 400);
                }} catch (e) {{
                    charBox.textContent = char;
                }}
            }});
        }}

        function speakCurrentWord() {{
            const item = activeVocab[currentIndex];
            if (item) {{
                speak(item.word);
            }}
        }}

        function initStrokeWritersBack() {{
            const item = activeVocab[currentIndex];
            const container = document.getElementById('stroke-area');
            container.innerHTML = '';
            activeWritersBack = [];

            if (!item) return;
            const chars = item.word.split('').filter(c => /[\\u4e00-\\u9fa5]/.test(c));

            chars.forEach((char, idx) => {{
                const charBox = document.createElement('div');
                charBox.className = 'hanzi-char-box';
                charBox.id = `back-char-box-${{idx}}`;
                container.appendChild(charBox);

                try {{
                    const writer = HanziWriter.create(charBox.id, char, {{
                        width: 70,
                        height: 70,
                        padding: 5,
                        showOutline: true,
                        strokeColor: '#2563eb',
                        outlineColor: '#f8fafc',
                        strokeAnimationSpeed: 1.5
                    }});
                    activeWritersBack.push(writer);
                    charBox.addEventListener('click', (e) => {{
                        e.stopPropagation();
                        writer.animateCharacter();
                    }});
                    setTimeout(() => writer.animateCharacter(), idx * 400);
                }} catch (e) {{
                    charBox.textContent = char;
                }}
            }});
        }}

        function prevCard() {{
            if (activeVocab.length === 0) return;
            currentIndex = (currentIndex - 1 + activeVocab.length) % activeVocab.length;
            updateUI();
        }}

        function nextCard() {{
            if (activeVocab.length === 0) return;
            currentIndex = (currentIndex + 1) % activeVocab.length;
            updateUI();
        }}

        function speak(text) {{
            if ('speechSynthesis' in window) {{
                window.speechSynthesis.cancel();
                const utterance = new SpeechSynthesisUtterance(text);
                utterance.lang = 'zh-CN';
                utterance.rate = 0.8;
                window.speechSynthesis.speak(utterance);
            }}
        }}

        function updateTable() {{
            const tbody = document.getElementById('table-body');
            tbody.innerHTML = '';

            activeVocab.forEach((item, idx) => {{
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${{idx + 1}}</td>
                    <td><span class="badge">${{item.lesson}}</span></td>
                    <td style="font-size: 1.5rem; font-weight: bold; color: var(--primary);">${{item.word}}</td>
                    <td style="font-family: monospace; font-size: 1.1rem; color: #2563eb;">${{item.pinyin}}</td>
                    <td style="font-weight: 600;">${{item.vietnamese}}</td>
                    <td><span class="badge" style="background-color:#eff6ff; color:#1e40af;">${{item.category}}</span></td>
                    <td>
                        <button class="btn-audio" style="margin-top:0;" onclick="speak('${{item.word}}')">🔊 Phát âm</button>
                    </td>
                `;
                tbody.appendChild(tr);
            }});
        }}
    </script>
</body>
</html>"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated standalone interactive offline flashcards app at {filepath}")

if __name__ == "__main__":
    generate_vocabulary()
