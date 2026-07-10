# -*- coding: utf-8 -*-
import streamlit as st
import streamlit.components.v1 as components
from ui_utils import render_lesson_intro, render_play_button

def render_hanzi_anim(char, width=120, height=120, key=None):
    import uuid
    if key is None:
        key = str(uuid.uuid4())[:8]
    div_id = f"hanzi_writer_{key}"
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <script src="https://cdn.jsdelivr.net/npm/hanzi-writer@2.2/dist/hanzi-writer.min.js"></script>
      <style>
        body {{
          margin: 0;
          padding: 0;
          display: flex;
          justify-content: center;
          align-items: center;
          background-color: transparent;
        }}
        #container {{
          width: {width}px;
          height: {height}px;
          border: 2px solid #e2e8f0;
          border-radius: 12px;
          background: #ffffff;
          box-shadow: 0 4px 12px rgba(0,0,0,0.05);
          display: flex;
          justify-content: center;
          align-items: center;
          cursor: pointer;
          transition: transform 0.2s, box-shadow 0.2s;
        }}
        #container:hover {{
          transform: translateY(-2px);
          box-shadow: 0 6px 16px rgba(0,0,0,0.1);
        }}
      </style>
    </head>
    <body>
      <div id="container">
        <div id="{div_id}"></div>
      </div>
      <script>
        var writer = HanziWriter.create('{div_id}', '{char}', {{
          width: {width - 24},
          height: {height - 24},
          padding: 5,
          showOutline: true,
          strokeColor: '#e11d48',
          outlineColor: '#f8fafc',
          strokeAnimationSpeed: 1.5
        }});
        document.getElementById('container').addEventListener('click', function() {{
          writer.animateCharacter();
        }});
      </script>
    </body>
    </html>
    """
    components.html(html_code, height=height+10, width=width+10)

def render_stroke_anim(d_path, width=120, height=120, key=None):
    import uuid
    if key is None:
        key = str(uuid.uuid4())[:8]
    path_id = f"stroke_path_{key}"
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        body {{
          margin: 0;
          padding: 0;
          display: flex;
          justify-content: center;
          align-items: center;
          background-color: transparent;
        }}
        #container {{
          width: {width}px;
          height: {height}px;
          border: 2px solid #e2e8f0;
          border-radius: 12px;
          background: #ffffff;
          box-shadow: 0 4px 12px rgba(0,0,0,0.05);
          display: flex;
          justify-content: center;
          align-items: center;
          cursor: pointer;
          transition: transform 0.2s, box-shadow 0.2s;
        }}
        #container:hover {{
          transform: translateY(-2px);
          box-shadow: 0 6px 16px rgba(0,0,0,0.1);
        }}
        .animated-path {{
          stroke-dasharray: 300;
          stroke-dashoffset: 0;
        }}
        .animated-path.draw-active {{
          animation: draw 1.5s ease-in-out forwards;
        }}
        @keyframes draw {{
          0% {{
            stroke-dashoffset: 300;
          }}
          100% {{
            stroke-dashoffset: 0;
          }}
        }}
      </style>
    </head>
    <body>
      <div id="container" onclick="startAnim()">
        <svg width="{width - 16}" height="{height - 16}" viewBox="0 0 100 100">
          <line x1="0" y1="50" x2="100" y2="50" stroke="#cbd5e1" stroke-dasharray="4 4" stroke-width="1" />
          <line x1="50" y1="0" x2="50" y2="100" stroke="#cbd5e1" stroke-dasharray="4 4" stroke-width="1" />
          <line x1="0" y1="0" x2="100" y2="100" stroke="#f1f5f9" stroke-dasharray="4 4" stroke-width="1" />
          <line x1="100" y1="0" x2="0" y2="100" stroke="#f1f5f9" stroke-dasharray="4 4" stroke-width="1" />
          <rect x="1" y="1" width="98" height="98" fill="none" stroke="#e2e8f0" stroke-width="2" rx="10" />
          <path d="{d_path}" stroke="#f1f5f9" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" fill="none" />
          <path d="{d_path}" stroke="#cbd5e1" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none" style="opacity: 0.4;" />
          <path id="{path_id}" d="{d_path}" stroke="#e11d48" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none" class="animated-path" />
        </svg>
      </div>
      <script>
        function startAnim() {{
          var path = document.getElementById('{path_id}');
          path.classList.remove('draw-active');
          void path.offsetWidth;
          path.classList.add('draw-active');
        }}
      </script>
    </body>
    </html>
    """
    components.html(html_code, height=height+10, width=width+10)

def inject_lesson8_css():
    st.markdown("""
    <style>
    .hanzi-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 18px;
        margin-bottom: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.02);
    }
    .rule-item {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 12px;
        margin-bottom: 10px;
    }
    .rule-header {
        font-weight: bold;
        color: #1e3a8a;
        font-size: 1.05rem;
        margin-bottom: 4px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .rule-badge {
        background-color: #dbeafe;
        color: #1e40af;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.8rem;
    }
    </style>
    """, unsafe_allow_html=True)

def show_lesson8_1_overview():
    inject_lesson8_css()
    render_lesson_intro(
        "📚 Bài 8.1 - Tổng quan Chữ Hán",
        "Tìm hiểu bản chất chữ biểu ý và các phương thức cấu tạo chữ Hán cơ bản."
    )
    st.subheader("1. Bản chất chữ Hán")
    st.write("Chữ Hán là chữ **biểu ý** (chỉ ý nghĩa), khác với chữ tiếng Việt/tiếng Anh là chữ **biểu âm** (ghép vần phát âm).")
    
    st.write("💡 **So sánh Phồn thể (nhiều nét) vs Giản thể (ít nét, dễ viết hơn):**")
    col1, col2 = st.columns(2)
    with col1:
        st.info("🐴 **Chữ Mã (Ngựa) - Phồn thể (10 nét)**")
        render_hanzi_anim("馬", key="ma_phonthe")
    with col2:
        st.success("🐴 **Chữ Mã (Ngựa) - Giản thể (3 nét)**")
        render_hanzi_anim("马", key="ma_gianthe")

    st.subheader("2. Cấu tạo Chữ Hán (4 loại cơ bản)")
    
    st.write("① **Tượng hình** (Vẽ lại hình dạng vật thực tế):")
    cols = st.columns(5)
    chars_th = [("日", "Mặt trời"), ("月", "Mặt trăng"), ("木", "Cây cối"), ("山", "Núi non"), ("人", "Con người")]
    for idx, (char, meaning) in enumerate(chars_th):
        with cols[idx]:
            st.caption(f"**{char}** ({meaning})")
            render_hanzi_anim(char, key=f"th_{char}")

    st.write("② **Chỉ sự** (Dùng nét ký hiệu để chỉ khái niệm trừu tượng):")
    cols = st.columns(3)
    chars_cs = [("上", "Ở trên"), ("下", "Ở dưới"), ("本", "Gốc rễ (gạch dưới gốc cây)")]
    for idx, (char, meaning) in enumerate(chars_cs):
        with cols[idx]:
            st.caption(f"**{char}** ({meaning})")
            render_hanzi_anim(char, key=f"cs_{char}")

    st.write("③ **Hội ý** (Ghép nhiều chữ đơn lẻ để tạo ra nghĩa mới):")
    cols = st.columns(3)
    chars_hy = [
        ("休", "Nghỉ ngơi (Người 人 dựa gốc cây 木)"),
        ("明", "Sáng sủa (Mặt trời 日 + Mặt trăng 月)"),
        ("好", "Tốt đẹp (Mẹ 女 + Con 子)")
    ]
    for idx, (char, meaning) in enumerate(chars_hy):
        with cols[idx]:
            st.caption(f"**{char}**")
            st.write(f"<small>{meaning}</small>", unsafe_allow_html=True)
            render_hanzi_anim(char, key=f"hy_{char}")

    st.write("④ **Hình thanh** (Phần chỉ ý nghĩa ghép với phần chỉ âm đọc):")
    cols = st.columns(2)
    chars_ht = [
        ("妈", "Mẹ (Nữ 女 chỉ nghĩa + Mã 马 chỉ âm đọc 'mā')"),
        ("爸", "Bố (Phụ 父 chỉ nghĩa + Ba 巴 chỉ âm đọc 'bà')")
    ]
    for idx, (char, meaning) in enumerate(chars_ht):
        with cols[idx]:
            st.caption(f"**{char}**")
            st.write(f"<small>{meaning}</small>", unsafe_allow_html=True)
            render_hanzi_anim(char, key=f"ht_{char}")

def show_lesson8_2_strokes():
    inject_lesson8_css()
    render_lesson_intro(
        "✍️ Bài 8.2 - Hệ thống Nét viết",
        "Luyện tập 8 nét cơ bản cấu tạo nên chữ Hán."
    )
    st.subheader("1. 8 Nét Cơ Bản Trong Chữ Hán (Vĩnh Tự Bát Pháp)")
    st.write("Nhấp vào các ô bên dưới để xem cách viết nét đơn độc lập:")

    basic_strokes = [
        {"stroke": "点 (diǎn)", "name": "Nét Chấm", "path": "M 45 40 Q 55 45 60 55", "desc": "Chấm từ trên xuống dưới"},
        {"stroke": "横 (héng)", "name": "Nét Ngang", "path": "M 25 50 L 75 50", "desc": "Ngang từ trái sang phải"},
        {"stroke": "竖 (shù)", "name": "Nét Sổ", "path": "M 50 25 L 50 75", "desc": "Sổ thẳng từ trên xuống"},
        {"stroke": "撇 (piě)", "name": "Nét Phẩy", "path": "M 65 30 Q 50 60 25 75", "desc": "Phẩy cong xuống sang trái"},
        {"stroke": "捺 (nà)", "name": "Nét Mác", "path": "M 35 30 Q 50 60 75 75", "desc": "Mác xiên xuống sang phải"},
        {"stroke": "提 (tí)", "name": "Nét Hất", "path": "M 30 70 L 70 45", "desc": "Hất chéo từ dưới lên phải"},
        {"stroke": "折 (zhé)", "name": "Nét Gập", "path": "M 30 35 L 70 35 L 70 75", "desc": "Gập góc đột ngột"},
        {"stroke": "钩 (gōu)", "name": "Nét Móc", "path": "M 50 25 L 50 75 L 35 60", "desc": "Móc ngược ở cuối nét"}
    ]

    cols = st.columns(4)
    for idx, s in enumerate(basic_strokes):
        with cols[idx % 4]:
            st.write(f"✍️ **{s['name']}**")
            st.write(f"<small>{s['stroke']}: {s['desc']}</small>", unsafe_allow_html=True)
            render_stroke_anim(s['path'], key=f"stroke_char_{idx}")
            st.markdown("<br/>", unsafe_allow_html=True)

    st.subheader("2. Giải nghĩa chữ 永 (Vĩnh) trong thư pháp")
    st.write("Chữ **永** (yǒng - vĩnh viễn/mãi mãi) là chữ kinh điển chứa đầy đủ cả 8 nét viết cơ bản:")

    col_desc, col_char = st.columns([6, 4])
    with col_desc:
        st.markdown("""
        - ❶ **Nét Chấm (点):** Nét chấm nằm trên cùng đầu chữ.
        - ❷ **Nét Ngang (横):** Nét đi ngang ngắn ở giữa.
        - ❸ **Nét Sổ (竖):** Nét dọc đứng trục chính ở giữa.
        - ❹ **Nét Móc (钩):** Nét móc nhọn ngược lên ở cuối nét sổ.
        - ❺ **Nét Hất (提):** Nét chéo đi từ dưới lên trên ở bên trái.
        - ❻ **Nét Phẩy (撇):** Nét cong dài từ giữa vuốt sang trái.
        - ❼ **Nét Gập (折):** Nét gấp góc ở phía trên bên phải.
        - ❽ **Nét Mác (捺):** Nét xiên dài vuốt xuống bên phải.
        """, unsafe_allow_html=True)
    with col_char:
        render_hanzi_anim("永", width=160, height=160, key="yong_explain")

    st.subheader("3. Các nét biến thể ghép")
    st.write("Nhấp vào các ô bên dưới để xem cách viết các nét biến thể ghép:")
    compound_strokes = [
        {"stroke": "横折 (héng zhé)", "name": "Ngang Gập", "path": "M 25 40 L 75 40 L 75 75", "desc": "Ngang rồi gập dọc (Ví dụ: 口, 日)"},
        {"stroke": "竖折 (shù zhé)", "name": "Sổ Gập", "path": "M 35 30 L 35 70 L 75 70", "desc": "Sổ rồi gập ngang (Ví dụ: 山)"},
        {"stroke": "竖钩 (shù gōu)", "name": "Sổ Móc", "path": "M 50 20 L 50 75 L 35 60", "desc": "Sổ rồi móc lên trái (Ví dụ: 小, 水)"},
        {"stroke": "斜钩 (xié gōu)", "name": "Nghiêng Móc", "path": "M 35 25 Q 55 60 65 75 L 53 65", "desc": "Cong nghiêng rồi móc lên (Ví dụ: 我)"}
    ]
    cols = st.columns(4)
    for idx, cs in enumerate(compound_strokes):
        with cols[idx]:
            st.write(f"✍️ **{cs['name']}**")
            st.write(f"<small>{cs['stroke']}: {cs['desc']}</small>", unsafe_allow_html=True)
            render_stroke_anim(cs['path'], key=f"compound_char_{idx}")
            st.markdown("<br/>", unsafe_allow_html=True)

def show_lesson8_3_rules():
    inject_lesson8_css()
    render_lesson_intro(
        "📐 Bài 8.3 - Quy tắc Bút thuận",
        "Quy tắc thứ tự viết các nét trong chữ Hán từ trước ra sau."
    )
    st.subheader("7 Quy tắc viết chữ Hán (Bút thuận)")
    st.write("Quan sát thứ tự các nét vẽ động tương ứng với mỗi quy tắc:")

    rules_list = [
        {"num": "1", "title": "Ngang trước sổ sau", "char": "十", "desc": "Nét ngang viết trước, nét sổ dọc viết sau."},
        {"num": "2", "title": "Phẩy trước mác sau", "char": "人", "desc": "Nét phẩy trái viết trước, nét mác phải viết sau."},
        {"num": "3", "title": "Trên trước dưới sau", "char": "三", "desc": "Viết bộ phận trên trước, dưới sau."},
        {"num": "4", "title": "Trái trước phải sau", "char": "你", "desc": "Viết bộ phận bên trái trước, bên phải sau."},
        {"num": "5", "title": "Ngoài trước trong sau", "char": "月", "desc": "Viết khung ngoài trước, viết phần trong sau."},
        {"num": "6", "title": "Vào trước đóng sau", "char": "国", "desc": "Khung ngoài ➔ viết chữ trong ➔ đóng cửa đáy."},
        {"num": "7", "title": "Giữa trước hai bên sau", "char": "小", "desc": "Nét chính giữa viết trước, 2 nét hai bên viết sau."}
    ]

    for idx, r in enumerate(rules_list):
        col_txt, col_anim = st.columns([6, 4])
        with col_txt:
            st.markdown(f"""
            <div class="rule-item">
                <div class="rule-header">
                    <span class="rule-badge">Quy tắc {r['num']}</span>
                    <span>{r['title']}</span>
                </div>
                <p style="color:#475569; font-size:0.95rem;">{r['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            render_play_button(r['char'], f"🔊 Phát âm chữ mẫu", key=f"play_rule_{idx}")
        with col_anim:
            render_hanzi_anim(r['char'], width=100, height=100, key=f"anim_rule_{idx}")
        st.markdown("<hr style='margin:10px 0; border:0; border-top:1px dashed #cbd5e1;'/>", unsafe_allow_html=True)

def show_lesson8_4_radicals():
    inject_lesson8_css()
    render_lesson_intro(
        "🧩 Bài 8.4 - Hệ thống Bộ thủ",
        "Học 8 bộ thủ cơ bản HSK 1 qua thẻ ghi nhớ (Flashcards) tương tác."
    )

    radicals_data = [
        {"bo": "亻 (人)", "name": "Bộ Nhân", "meaning": "Người", "char": "..."},
        {"bo": "亻 (人)", "name": "Bộ Nhân", "meaning": "Người", "char": "他", "desc": "Liên quan đến con người, danh xưng, hoạt động của người."},
        {"bo": "女", "name": "Bộ Nữ", "meaning": "Phụ nữ", "char": "她", "desc": "Liên quan đến phái đẹp, người nữ, quan hệ gia đình."},
        {"bo": "口", "name": "Bộ Khẩu", "meaning": "Miệng", "char": "吃", "desc": "Liên quan đến ăn uống, kêu gọi, bộ phận ở miệng."},
        {"bo": "氵 (水)", "name": "Bộ Thủy", "meaning": "Nước", "char": "没", "desc": "Liên quan đến chất lỏng, sông ngòi, nước nói chung."},
        {"bo": "木", "name": "Bộ Mộc", "meaning": "Cây/Gỗ", "char": "杯", "desc": "Liên quan đến cây cối, rừng rậm hoặc đồ dùng bằng gỗ."},
        {"bo": "火 (灬)", "name": "Bộ Hỏa", "meaning": "Lửa", "char": "热", "desc": "Liên quan đến nhiệt độ, sức nóng, nấu nướng."},
        {"bo": "讠 (言)", "name": "Bộ Ngôn", "meaning": "Lời nói", "char": "说", "desc": "Liên quan đến giao tiếp, đối thoại, phát ngôn."},
        {"bo": "忄 (心)", "name": "Bộ Tâm", "meaning": "Cảm xúc", "char": "忙", "desc": "Liên quan đến suy nghĩ, tâm trạng, tình cảm tâm lý."}
    ]
    # Remove dummy item
    radicals_data = radicals_data[1:]

    if "radical_idx" not in st.session_state:
        st.session_state.radical_idx = 0

    col_prev, col_info, col_next = st.columns([2, 6, 2])
    
    with col_prev:
        st.write("<div style='height: 100px;'></div>", unsafe_allow_html=True)
        if st.button("◀ Thẻ trước", key="btn_prev_rad", use_container_width=True):
            st.session_state.radical_idx = (st.session_state.radical_idx - 1) % len(radicals_data)
            st.rerun()

    with col_next:
        st.write("<div style='height: 100px;'></div>", unsafe_allow_html=True)
        if st.button("Thẻ sau ▶", key="btn_next_rad", use_container_width=True):
            st.session_state.radical_idx = (st.session_state.radical_idx + 1) % len(radicals_data)
            st.rerun()

    current_idx = st.session_state.radical_idx
    r = radicals_data[current_idx]

    with col_info:
        st.markdown(f"""
        <div style="background: linear-gradient(145deg, #ffffff 0%, #fff1f2 100%); 
                    border: 2px solid #fecdd3; 
                    border-radius: 20px; 
                    padding: 25px; 
                    box-shadow: 0 10px 25px rgba(225, 29, 72, 0.08); 
                    text-align: center; 
                    margin-top: 10px;">
            <span style="background-color: #ffe4e6; color: #e11d48; padding: 4px 14px; border-radius: 12px; font-weight: bold; font-size: 0.9rem;">
                BỘ THỦ {current_idx + 1} / {len(radicals_data)}
            </span>
            <div style="font-size: 5rem; font-weight: bold; color: #e11d48; margin: 15px 0 5px 0; line-height: 1;">
                {r['bo']}
            </div>
            <h3 style="color: #1e293b; margin: 0 0 10px 0; font-size: 1.5rem;">{r['name']} ({r['meaning']})</h3>
            <p style="color: #475569; font-size: 1rem; line-height: 1.6; max-width: 500px; margin: 0 auto 20px auto;">
                {r['desc']}
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='text-align: center; font-weight: bold; margin-top: 20px; color: #1e3a8a;'>Ví dụ chữ Hán chứa bộ thủ:</div>", unsafe_allow_html=True)
        col_char, col_btn = st.columns([1, 1])
        with col_char:
            render_hanzi_anim(r['char'], width=120, height=120, key=f"flash_rad_char_{current_idx}")
        with col_btn:
            st.write("<div style='height: 35px;'></div>", unsafe_allow_html=True)
            render_play_button(r['char'], f"🔊 Phát âm chữ: {r['char']}", key=f"play_flash_{current_idx}")

def show_lesson8_5_structures():
    inject_lesson8_css()
    render_lesson_intro(
        "🧱 Bài 8.5 - Đơn thể & Hợp thể",
        "Phân loại cấu trúc chữ Hán thành chữ độc lập (đơn thể) và chữ ghép (hợp thể)."
    )
    st.subheader("1. Chữ Đơn thể")
    st.write("Chữ độc lập, cấu tạo trực tiếp từ nét bút, không tách nhỏ hơn được:")
    cols = st.columns(4)
    chars_dt = [("人", "Người"), ("木", "Cây"), ("日", "Mặt trời"), ("月", "Mặt trăng")]
    for idx, (c, m) in enumerate(chars_dt):
        with cols[idx]:
            st.caption(f"**{c}** ({m})")
            render_hanzi_anim(c, key=f"dt_anim_{idx}")

    st.subheader("2. Chữ Hợp thể")
    st.write("Chữ ghép từ 2 bộ phận trở lên. Gồm các cấu trúc ghép chính:")
    
    col_left, col_mid, col_right = st.columns(3)
    with col_left:
        st.info("⬅️➡️ **Trái - Phải**")
        st.write("好 (Tốt) = 女 + Tử")
        render_hanzi_anim("好", key="struct_lr")
    with col_mid:
        st.success("⬆️⬇️ **Trên - Dưới**")
        st.write("爸 (Bố) = Phụ + Ba")
        render_hanzi_anim("爸", key="struct_ud")
    with col_right:
        st.warning("🔄 **Bao vây**")
        st.write("国 (Nước) = Vi + Ngọc")
        render_hanzi_anim("国", key="struct_enc")
