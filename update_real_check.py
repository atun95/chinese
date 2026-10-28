# -*- coding: utf-8 -*-
with open("a.py", "r", encoding="utf-8") as f:
    text = f.read()

old_block = '''# Trạng thái kết nối Supabase ở bên trái màn hình
if supabase_client.is_supabase_configured():
    st.sidebar.markdown("""
    <div style="background-color: #f0fdf4; border: 1.5px solid #22c55e; border-radius: 12px; padding: 8px 12px; margin-bottom: 15px; color: #15803d; font-size: 0.85rem; font-weight: 700; display: flex; align-items: center; gap: 8px;">
        <span style="font-size: 0.95rem;">🟢</span>
        <span>Supabase: Đã kết nối</span>
    </div>
    """, unsafe_allow_html=True)
else:
    st.sidebar.markdown("""
    <div style="background-color: #fef2f2; border: 1.5px solid #ef4444; border-radius: 12px; padding: 8px 12px; margin-bottom: 15px; color: #991b1b; font-size: 0.85rem; font-weight: 700; display: flex; align-items: center; gap: 8px;">
        <span style="font-size: 0.95rem;">🔴</span>
        <span>Supabase: Chưa kết nối</span>
    </div>
    """, unsafe_allow_html=True)'''

new_block = '''# Kiểm tra kết nối THỰC TẾ với Supabase (Live database ping)
is_live_ok, live_conn_msg = supabase_client.check_real_connection()

if is_live_ok:
    st.sidebar.markdown("""
    <div style="background-color: #f0fdf4; border: 1.5px solid #22c55e; border-radius: 12px; padding: 8px 12px; margin-bottom: 15px; color: #15803d; font-size: 0.85rem; font-weight: 700; display: flex; align-items: center; gap: 8px;">
        <span style="font-size: 0.95rem;">🟢</span>
        <span>Supabase: Đã kết nối</span>
    </div>
    """, unsafe_allow_html=True)
else:
    st.sidebar.markdown(f"""
    <div style="background-color: #fef2f2; border: 1.5px solid #ef4444; border-radius: 12px; padding: 8px 12px; margin-bottom: 15px; color: #991b1b; font-size: 0.85rem; font-weight: 700; display: flex; align-items: center; gap: 8px;" title="{live_conn_msg}">
        <span style="font-size: 0.95rem;">🔴</span>
        <span>Supabase: Chưa kết nối</span>
    </div>
    """, unsafe_allow_html=True)'''

old_block_crlf = old_block.replace('\n', '\r\n')
new_block_crlf = new_block.replace('\n', '\r\n')

if old_block_crlf in text:
    text = text.replace(old_block_crlf, new_block_crlf)
    print("Replaced CRLF")
elif old_block in text:
    text = text.replace(old_block, new_block)
    print("Replaced LF")
else:
    print("Direct replace failed, using index find")
    idx = text.find('# Trạng thái kết nối Supabase ở bên trái màn hình')
    end_idx = text.find('mode = st.sidebar.selectbox', idx)
    text = text[:idx] + new_block + '\n\n' + text[end_idx:]
    print("Index replaced!")

with open("a.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated a.py successfully!")
