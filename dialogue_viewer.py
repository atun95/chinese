"""Simple Streamlit app to display the sample dialogues for learners.
It loads 'sample_dialogues.md', splits into separate dialogue blocks, and lets the user select which dialogue to view.
"""
import pathlib
import streamlit as st

# Page configuration with larger fonts via CSS
st.set_page_config(page_title="Dialogue Viewer", layout="wide")
st.markdown(
    """
    <style>
    .title {font-size: 2.5rem; font-weight: bold; margin-bottom: 1rem;}
    .instruction {font-size: 1.3rem; margin-bottom: 1.5rem;}
    .dialogue {font-size: 1.2rem; line-height: 1.6;}
    .stSelectbox label {font-size: 1.3rem;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='title'>📚 Xem các đoạn hội thoại</div>", unsafe_allow_html=True)
st.write("<div class='instruction'>Chọn một đoạn hội thoại từ menu bên dưới để xem nội dung.</div>", unsafe_allow_html=True)

# Load dialogues markdown
dlg_path = pathlib.Path(__file__).parent / "lessons" / "sample_dialogues.md"
if not dlg_path.exists():
    st.error(f"Dialogue file not found: {dlg_path}")
    st.stop()
content = dlg_path.read_text(encoding="utf-8")
# Split blocks by separator '---'
raw_blocks = [b.strip() for b in content.split('---') if b.strip()]
# Clean up block headings (remove top-level title line if present)
blocks = []
for block in raw_blocks:
    lines = block.splitlines()
    # Remove lines that start with '# Sample' (the global title line)
    lines = [ln for ln in lines if not ln.startswith('# Sample')]
    blocks.append('\n'.join(lines))
# Extract titles for the selectbox (use the first "##" heading in each block)
options = []
for i, block in enumerate(blocks, 1):
    title = f"Dialogue {i}"
    for line in block.splitlines():
        if line.startswith('##'):
            title = line.lstrip('#').strip()
            break
    options.append(title)

selected = st.selectbox("Chọn đoạn hội thoại", options, key="dialogue_select")
idx = options.index(selected)
# Show selected dialogue
st.markdown(f"<div class='dialogue'>### {selected}</div>", unsafe_allow_html=True)
st.markdown(blocks[idx], unsafe_allow_html=False)
