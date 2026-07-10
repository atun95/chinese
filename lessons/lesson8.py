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
          strokeAnimationSpeed: 1.5,
          delayBetweenLoops: 2000
        }});
        writer.loopCharacterAnimation();
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
        }}
        .animated-path {{
          stroke-dasharray: 300;
          stroke-dashoffset: 300;
          animation: draw 2.5s infinite ease-in-out;
        }}
        @keyframes draw {{
          0% {{
            stroke-dashoffset: 300;
          }}
          50% {{
            stroke-dashoffset: 0;
          }}
          100% {{
            stroke-dashoffset: 0;
          }}
        }}
      </style>
    </head>
    <body>
      <div id="container">
        <svg width="{width - 16}" height="{height - 16}" viewBox="0 0 100 100">
          <line x1="0" y1="50" x2="100" y2="50" stroke="#cbd5e1" stroke-dasharray="4 4" stroke-width="1" />
          <line x1="50" y1="0" x2="50" y2="100" stroke="#cbd5e1" stroke-dasharray="4 4" stroke-width="1" />
          <line x1="0" y1="0" x2="100" y2="100" stroke="#f1f5f9" stroke-dasharray="4 4" stroke-width="1" />
          <line x1="100" y1="0" x2="0" y2="100" stroke="#f1f5f9" stroke-dasharray="4 4" stroke-width="1" />
          <rect x="1" y="1" width="98" height="98" fill="none" stroke="#e2e8f0" stroke-width="2" rx="10" />
          <path d="{d_path}" stroke="#e11d48" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none" class="animated-path" />
        </svg>
      </div>
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
    compound_strokes = [
        {"stroke": "横折 (héng zhé)", "desc": "Ngang gập (ví dụ trong chữ <b>口</b>, <b>日</b>)"},
        {"stroke": "竖折 (shù zhé)", "desc": "Sổ gập (ví dụ trong chữ <b>山</b>)"},
        {"stroke": "竖钩 (shù gōu)", "desc": "Sổ móc (ví dụ trong chữ <b>小</b>, <b>水</b>)"},
        {"stroke": "斜钩 (xié gōu)", "desc": "Nghiêng móc (ví dụ trong chữ <b>我</b>)"}
    ]
    cols = st.columns(2)
    for i, cs in enumerate(compound_strokes):
        with cols[i % 2]:
            st.markdown(f"""
            <div style="background-color:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:8px 12px; margin-bottom:8px;">
                <span style="font-weight:bold; color:#e11d48;">{cs['stroke']}</span>: {cs['desc']}
            </div>
            """, unsafe_allow_html=True)

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
        "Nhận diện 8 bộ thủ cơ bản đại diện cho nhóm ý nghĩa trong chữ Hán."
    )
    st.subheader("1. Khái niệm Bộ thủ")
    st.write("Bộ thủ biểu thị nhóm ý nghĩa khái quát của chữ Hán. HSK 1 cần nhớ 8 bộ thủ sau:")

    radicals_data = [
        {"bo": "亻(人)", "name": "Bộ Nhân (Người)", "char": "他", "desc": "Chỉ người, hành động của người"},
        {"bo": "女", "name": "Bộ Nữ (Phụ nữ)", "char": " she", "char": "彼女", "char": "彼女", "char": "她", "desc": "Chỉ phụ nữ, quan hệ gia đình"},
        {"bo": "口", "name": "Bộ Khẩu (Miệng)", "char": "吃", "desc": "Liên quan đến ăn uống, lời nói"},
        {"bo": "氵(水)", "name": "Bộ Thủy (Nước)", "char": "没", "desc": "Liên quan đến nước, chất lỏng"},
        {"bo": "木", "name": "Bộ Mộc (Cây/Gỗ)", "char": "杯", "desc": "Liên quan đến thực vật, bàn ghế, cốc gỗ"},
        {"bo": "火 (灬)", "name": "Bộ Hỏa (Lửa)", "char": "热", "desc": "Liên quan đến lửa, nhiệt độ"},
        {"bo": "讠(言)", "name": "Bộ Ngôn (Lời nói)", "char": "说", "desc": "Liên quan đến giao tiếp, ngôn ngữ"},
        {"bo": "忄(心)", "name": "Bộ Tâm (Cảm xúc)", "char": "忙", "desc": "Liên quan đến tâm lý, tâm trạng"}
    ]

    cols = st.columns(4)
    for idx, r in enumerate(radicals_data):
        with cols[idx % 4]:
            st.markdown(f"""
            <div style="background-color:#fff1f2; border:1px solid #fecdd3; border-radius:8px; padding:10px; text-align:center; margin-bottom:5px;">
                <span style="font-size:1.5rem; font-weight:bold; color:#e11d48;">{r['bo']}</span><br/>
                <b>{r['name']}</b><br/>
                <small style="color:#475569;">{r['desc']}</small>
            </div>
            """, unsafe_allow_html=True)
            render_hanzi_anim(r['char'], width=100, height=100, key=f"rad_anim_{idx}")
            st.markdown("<br/>", unsafe_allow_html=True)

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
