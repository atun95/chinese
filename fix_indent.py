import re

path = r'c:\Users\lyquo\OneDrive\Desktop\chinese\lesson5.py'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Dedent lines 1116-1204 (0-indexed 1115-1203) - the HTML inside st.markdown
for i in range(1115, 1204):
    stripped = lines[i].lstrip()
    if stripped:
        lines[i] = stripped

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Done - HTML lines 1116-1204 dedented to column 0')
