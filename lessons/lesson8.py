# -*- coding: utf-8 -*-
import streamlit as st
from ui_utils import render_lesson_intro, render_play_button

def show_lesson8_1_hanzi_strokes():
    # CSS Styles sang trọng cho Bài 8.1
    st.markdown("""
    <style>
    .hanzi-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .hanzi-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
    }
    .hanzi-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1e3a8a;
        margin-right: 15px;
    }
    .pinyin-badge {
        background-color: #eff6ff;
        color: #1d4ed8;
        padding: 4px 10px;
        border-radius: 20px;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        font-size: 1.1rem;
        border: 1px solid #bfdbfe;
    }
    .meaning-badge {
        background-color: #f0fdf4;
        color: #15803d;
        padding: 4px 10px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.95rem;
        border: 1px solid #bbf7d0;
    }
    .rule-box {
        background-color: #f8fafc;
        border-left: 5px solid #3b82f6;
        border-radius: 8px;
        padding: 15px;
        margin: 15px 0;
        border-top: 1px solid #e2e8f0;
        border-right: 1px solid #e2e8f0;
        border-bottom: 1px solid #e2e8f0;
    }
    .info-box-premium {
        background: linear-gradient(135deg, #f8fafc 0%, #eff6ff 100%);
        border-left: 5px solid #2563eb;
        border-radius: 8px;
        padding: 18px;
        margin: 18px 0;
        border-top: 1px solid #e2e8f0;
        border-right: 1px solid #e2e8f0;
        border-bottom: 1px solid #e2e8f0;
    }
    .comparison-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 1px solid #e2e8f0;
        border-left: 6px solid #8b5cf6;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.02);
    }
    .comparison-title {
        font-weight: 700;
        color: #7c3aed;
        font-size: 1.2rem;
        margin-bottom: 8px;
    }
    .stroke-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
        gap: 16px;
        margin-top: 15px;
    }
    .stroke-card {
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 15px;
        background-color: #ffffff;
        box-shadow: 0 2px 8px rgba(0,0,0,0.02);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .stroke-char {
        font-size: 2.2rem;
        font-weight: bold;
        color: #e11d48;
        text-align: center;
        background: #fff1f2;
        border-radius: 8px;
        padding: 5px 0;
        margin-bottom: 10px;
        border: 1px dashed #fecdd3;
    }
    .stroke-name {
        font-weight: bold;
        color: #0f172a;
        font-size: 1.1rem;
        margin-bottom: 5px;
    }
    .stroke-desc {
        color: #475569;
        font-size: 0.9rem;
        line-height: 1.4;
        margin-bottom: 8px;
    }
    .rule-item {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 16px;
        margin-bottom: 12px;
    }
    .rule-header {
        font-weight: bold;
        color: #1e3a8a;
        font-size: 1.05rem;
        margin-bottom: 6px;
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
    .radical-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
    }
    .radical-table th, .radical-table td {
        border: 1px solid #e2e8f0;
        padding: 12px;
        text-align: left;
    }
    .radical-table th {
        background-color: #f1f5f9;
        color: #1e293b;
        font-weight: bold;
    }
    .radical-table tr:hover {
        background-color: #f8fafc;
    }
    .hanzi-font {
        font-size: 1.6rem;
        font-family: 'Noto Sans SC', sans-serif;
        font-weight: bold;
        color: #0f172a;
    }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "📚 Bài 8.1 - Chữ Hán: Nét viết, Bút thuận & Cấu tạo chữ",
        "Học phần lý thuyết chuyên sâu về nguồn gốc chữ Hán, hệ thống nét viết cơ bản, quy tắc viết chữ (bút thuận), khái niệm bộ thủ và phân loại cấu trúc chữ đơn thể & hợp thể."
    )

    tab_overview, tab_strokes, tab_rules, tab_radicals, tab_structures = st.tabs([
        "📚 1. Tổng quan chữ Hán",
        "✍️ 2. Hệ thống Nét viết",
        "📐 3. Quy tắc Bút thuận",
        "🧩 4. Hệ thống Bộ thủ",
        "🧱 5. Đơn thể & Hợp thể"
    ])

    # ================= TAB 1: TỔNG QUAN CHỮ HÁN =================
    with tab_overview:
        st.subheader("1. Nguồn gốc & Bản chất Chữ Hán")
        st.write("""
        Chữ Hán (汉字 - Hànzì) là hệ chữ biểu ý (logographic) lâu đời nhất thế giới còn sử dụng rộng rãi đến ngày nay. 
        Không giống như các hệ chữ biểu âm (như tiếng Việt, tiếng Anh sử dụng các chữ cái Latinh ghép lại để biểu diễn âm thanh), 
        chữ Hán biểu diễn trực tiếp **ý nghĩa** hoặc **hình ảnh tượng trưng** của sự vật, hiện tượng.
        """)

        st.markdown("""
        <div class="info-box-premium">
            <strong>💡 Quá trình phát triển của chữ Hán qua các thời kỳ:</strong><br/>
            • <b>Giáp cốt văn (甲骨文):</b> Chữ khắc trên mai rùa, xương thú thời nhà Thương (khoảng 3000 năm trước), mang tính tượng hình rất đậm nét.<br/>
            &nbsp;&nbsp; <i>Ví dụ:</i> Chữ <b>日</b> (mặt trời) thuở sơ khai được khắc là một hình tròn có một dấu chấm tròn ở giữa biểu thị tâm mặt trời; chữ <b>马</b> (ngựa) vẽ rõ nét con ngựa đứng có đầu, bờm và bốn chân.<br/>
            • <b>Kim văn (金文):</b> Chữ khắc trên chuông, đỉnh và đồ dùng bằng đồng thời nhà Chu. Nét chữ dày dặn hơn, bớt đi các góc nhọn sắc của nét khắc xương.<br/>
            &nbsp;&nbsp; <i>Ví dụ:</i> Chữ <b>日</b> trong Kim văn được viết tròn hơn, dấu chấm ở giữa to rõ; chữ <b>马</b> được làm thon gọn lại, chú trọng nét vẽ bờm và đầu ngựa.<br/>
            • <b>Tiểu triện (小篆):</b> Kiểu chữ thống nhất thời Tần Thủy Hoàng. Nét vẽ uốn lượn tròn trịa, dài và thanh mảnh, mang tính thẩm mỹ cao.<br/>
            &nbsp;&nbsp; <i>Ví dụ:</i> Chữ <b>日</b> kéo dài thành hình chữ nhật đứng bo tròn góc với nét ngang ở giữa; chữ <b>马</b> được chuẩn hóa thành các nét cong dài xếp dọc đối xứng.<br/>
            • <b>Lệ thư (隶书):</b> Bước ngoặt lớn nhất, biến các nét cong uốn lượn của Tiểu triện thành các nét thẳng, gập vuông vắn để thuận tiện viết nhanh bằng bút lông.<br/>
            &nbsp;&nbsp; <i>Ví dụ:</i> Chữ <b>日</b> trở nên vuông vắn hoàn toàn; chữ <b>马</b> biến đổi các nét vẽ bờm thành các nét ngang dọc thẳng đứng, 4 chân ngựa biến thành 4 dấu chấm ở đáy (<b>馬</b>).<br/>
            • <b>Khải thư (楷书):</b> Kiểu chữ chuẩn mực, vuông vức, cân đối và sắc nét nhất, kế thừa Lệ thư và ổn định cấu trúc chữ từ thời Đông Hán cho đến nay.<br/>
            &nbsp;&nbsp; <i>Ví dụ:</i> Chữ <b>日</b> và chữ <b>馬</b> đạt độ cân đối thẩm mỹ tối đa, là kiểu chữ in sách chuẩn ngày nay.<br/>
            • <b>Chữ Giản thể (简体字) & Phồn thể (繁体字):</b><br/>
            &nbsp;&nbsp; - <b>Phồn thể:</b> Giữ nguyên các nét của Khải thư truyền thống (dùng ở Đài Loan, Hồng Kông). <i>Ví dụ:</i> Chữ <b>馬</b> (ngựa) có 10 nét.<br/>
            &nbsp;&nbsp; - <b>Giản thể:</b> Phiên bản rút gọn nét của chữ Phồn thể để giúp người dân học và viết nhanh hơn (dùng ở Trung Quốc đại lục, Singapore). <i>Ví dụ:</i> Chữ <b>馬</b> được giản lược thành <b>马</b> (chỉ còn 3 nét, 4 dấu chấm chân ngựa bên dưới biến thành 1 nét ngang dài).
        </div>
        """, unsafe_allow_html=True)

        st.subheader("2. Cấu tạo Chữ Hán theo Lục thư (六书)")
        st.write("Theo truyền thống học thuật Trung Hoa, chữ Hán được cấu tạo theo 6 phương thức (Lục thư). Ở trình độ cơ bản, chúng ta tập trung vào 4 phương thức chính:")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="comparison-card">
                <div class="comparison-title">① Chữ Tượng hình (象形 - xiàngxíng)</div>
                <p>Là kiểu chữ vẽ lại phác họa hình dáng của sự vật ngoài đời thực.</p>
                <ul>
                    <li><b>日</b> (rì - mặt trời): vẽ hình tròn có dấu chấm giữa.</li>
                    <li><b>月</b> (yuè - mặt trăng): vẽ hình trăng khuyết.</li>
                    <li><b>木</b> (mù - cây): vẽ hình thân cây có cành và rễ.</li>
                    <li><b>山</b> (shān - núi): vẽ ba ngọn núi nhấp nhô.</li>
                    <li><b>人</b> (rén - người): vẽ dáng người đang đi.</li>
                </ul>
            </div>
            <div class="comparison-card">
                <div class="comparison-title">② Chữ Chỉ sự (指事 - zhǐshì)</div>
                <p>Dùng nét vẽ ước lệ để biểu thị các khái niệm trừu tượng hoặc chỉ định vị trí.</p>
                <ul>
                    <li><b>上</b> (shàng - trên) & <b>下</b> (xià - dưới).</li>
                    <li><b>本</b> (běn - gốc, cội nguồn): thêm một nét ngang dưới bộ <b>木</b> để chỉ phần gốc rễ của cây.</li>
                    <li><b>刃</b> (rèn - lưỡi dao): thêm một dấu chấm trên bộ <b>刀</b> (dao) để chỉ phần lưỡi sắc.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="comparison-card">
                <div class="comparison-title">③ Chữ Hội ý (会意 - huìyì)</div>
                <p>Ghép hai hoặc nhiều chữ tượng hình lại với nhau để tạo ra một ý nghĩa mới hợp thành.</p>
                <ul>
                    <li><b>休</b> (xiū - nghỉ ngơi): ghép từ bộ <b>人</b> (người) đứng cạnh bộ <b>木</b> (gây gốc cây). Người tựa vào cây là để nghỉ ngơi.</li>
                    <li><b>明</b> (míng - sáng sủa): ghép từ <b>日</b> (mặt trời) và <b>月</b> (mặt trăng). Cả hai nguồn sáng tụ lại tạo nên sự sáng sủa.</li>
                    <li><b>好</b> (hǎo - tốt đẹp): ghép từ bộ <b>女</b> (phụ nữ) và chữ <b>子</b> (con cái). Người phụ nữ có con là điều tốt đẹp nhất.</li>
                </ul>
            </div>
            <div class="comparison-card">
                <div class="comparison-title">④ Chữ Hình thanh (形声 - xíngshēng)</div>
                <p>Ghép từ một phần biểu ý (chỉ nghĩa) và một phần biểu âm (chỉ cách đọc). Phương thức này tạo nên hơn 80% chữ Hán.</p>
                <ul>
                    <li><b>妈</b> (mā - mẹ): bộ <b>女</b> (nữ - chỉ giới tính nữ) ghép với chữ <b>马</b> (mǎ - ngựa - mượn âm đọc).</li>
                    <li><b>爸</b> (bà - bố): bộ <b>父</b> (phụ - cha, chỉ nghĩa) ghép với chữ <b>巴</b> (bā - mượn âm đọc).</li>
                    <li><b>谁</b> (shéi - ai): bộ <b>讠</b> (ngôn - nói năng, chỉ nghĩa) ghép với chữ <b>隹</b> (zhuī - mượn âm đọc).</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    # ================= TAB 2: HỆ THỐNG NÉT VIẾT =================
    with tab_strokes:
        st.subheader("1. 8 Nét Cơ Bản Trong Chữ Hán (永字八法)")
        st.write("""
        Chữ Hán được cấu tạo từ các đường nét. Trong thư pháp Trung Hoa có quy tắc **Vĩnh tự bát pháp (永字八法)**: 
        Chữ **永** (yǒng - vĩnh viễn) chứa toàn bộ 8 nét cơ bản nhất của chữ Hán.
        """)

        # Danh sách 8 nét cơ bản
        basic_strokes = [
            {"stroke": "点", "name": "Nét Chấm (diǎn)", "desc": "Dấu chấm từ trên xuống dưới, hơi chếch về bên phải.", "eg": "主, 六, 门, 头", "sound_txt": "点"},
            {"stroke": "横", "name": "Nét Ngang (héng)", "desc": "Nét thẳng nằm ngang, viết từ trái sang phải.", "eg": "一, 二, 三, 十", "sound_txt": "横"},
            {"stroke": "竖", "name": "Nét Sổ (shù)", "desc": "Nét thẳng đứng, viết từ trên xuống dưới.", "eg": "十, 中, 工, 干", "sound_txt": "竖"},
            {"stroke": "撇", "name": "Nét Phẩy (piě)", "desc": "Nét cong từ trên xuống, vắt xiên về phía trái.", "eg": "人, 八, 禾, 千", "sound_txt": "撇"},
            {"stroke": "捺", "name": "Nét Mác (nà)", "desc": "Nét thẳng xiên từ trên xuống, kéo dài chếch về phía phải.", "eg": "人, 八, 木, 大", "sound_txt": "捺"},
            {"stroke": "提", "name": "Nét Hất (tí)", "desc": "Nét chéo thẳng đi từ dưới lên trên và chếch sang phải.", "eg": "我, 打, 习, 冰", "sound_txt": "提"},
            {"stroke": "折", "name": "Nét Gập (zhé)", "desc": "Nét đang đi thẳng thì gập góc sang hướng khác (ngang gập, sổ gập...).", "eg": "口, 门, 日, 四", "sound_txt": "折"},
            {"stroke": "钩", "name": "Nét Móc (gōu)", "desc": "Nét móc ngược lên ở cuối các nét khác (sổ móc, cong móc, nghiêng móc).", "eg": "小, 水, 手, 我", "sound_txt": "钩"},
        ]

        st.markdown('<div class="stroke-grid">', unsafe_allow_html=True)
        for s in basic_strokes:
            st.markdown(f"""
            <div class="stroke-card">
                <div>
                    <div class="stroke-char">{s['stroke']}</div>
                    <div class="stroke-name">{s['name']}</div>
                    <div class="stroke-desc">{s['desc']}</div>
                    <div style="font-size: 0.88rem; color: #64748b;"><b>Ví dụ chữ:</b> {s['eg']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            # Render play button inside Streamlit columns under the card
            render_play_button(s['sound_txt'], f"🔊 Nghe đọc nét {s['stroke']}", key=f"snd_{s['stroke']}")
            st.markdown('<div style="margin-bottom:12px;"></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.subheader("2. Một số nét biến thể / phức hợp thường gặp")
        st.write("Các nét phức hợp là sự kết hợp liền mạch không nhấc bút của các nét cơ bản trên:")
        
        compound_strokes = [
            {"stroke": "横折 (héng zhé)", "desc": "Ngang gập (Ví dụ: nét thứ hai của chữ <b>口</b>, <b>日</b>)"},
            {"stroke": "竖折 (shù zhé)", "desc": "Sổ gập (Ví dụ: nét thứ hai của chữ <b>山</b>, <b>画</b>)"},
            {"stroke": "竖钩 (shù gōu)", "desc": "Sổ móc (Ví dụ: nét thẳng giữa của chữ <b>小</b>, <b>水</b>)"},
            {"stroke": "弯钩 (wān gōu)", "desc": "Cong móc (Ví dụ: nét móc bên phải chữ <b>家</b>, <b>狗</b>)"},
            {"stroke": "斜钩 (xié gōu)", "desc": "Nghiêng móc (Ví dụ: nét móc nghiêng trong chữ <b>我</b>, <b>钱</b>)"},
            {"stroke": "横折钩 (héng zhé gōu)", "desc": "Ngang gập móc (Ví dụ: nét bao ngoài chữ <b>月</b>, <b>门</b>)"}
        ]

        cols = st.columns(2)
        for i, cs in enumerate(compound_strokes):
            col_target = cols[i % 2]
            with col_target:
                st.markdown(f"""
                <div style="background-color:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:12px; margin-bottom:10px;">
                    <span style="font-weight:bold; color:#e11d48;">{cs['stroke']}</span>: {cs['desc']}
                </div>
                """, unsafe_allow_html=True)

    # ================= TAB 3: QUY TẮC BÚT THUẬN =================
    with tab_rules:
        st.subheader("Quy tắc Bút Thuận (笔顺 - Bǐshùn)")
        st.write("""
        Bút thuận là quy tắc quy định thứ tự viết trước sau của các nét trong một chữ Hán. 
        Viết đúng bút thuận giúp chữ viết cân đối, đẹp mắt, nhanh hơn và giúp bạn dễ dàng đếm số nét để tra cứu từ điển.
        """)

        rules_list = [
            {"num": "1", "title": "Ngang trước sổ sau (先横后竖)", "desc": "Khi có nét ngang và nét sổ giao nhau, viết nét ngang trước, sổ sau.", "eg_han": "十", "eg_py": "shí", "order": "一 ➔ 十"},
            {"num": "2", "title": "Phẩy trước mác sau (先撇后捺)", "desc": "Khi nét phẩy (chếch trái) và nét mác (chếch phải) giao nhau, viết phẩy trước, mác sau.", "eg_han": "人", "eg_py": "rén", "order": "丿 ➔ 人"},
            {"num": "3", "title": "Trên trước dưới sau (从上到下)", "desc": "Các nét hoặc bộ phận ở trên viết trước, ở dưới viết sau.", "eg_han": "三", "eg_py": "sān", "order": "Ngang trên ➔ Ngang giữa ➔ Ngang dưới"},
            {"num": "4", "title": "Trái trước phải sau (从左到右)", "desc": "Các nét hoặc bộ phận bên trái viết trước, bên phải viết sau.", "eg_han": "你", "eg_py": "nǐ", "order": "Bộ 亻 (trái) ➔ Chữ 尔 (phải)"},
            {"num": "5", "title": "Ngoài trước trong sau (从外到内)", "desc": "Với chữ có khung bao quanh (nhưng không đóng đáy), viết khung ngoài trước, phần bên trong sau.", "eg_han": "月", "eg_py": "yuè", "order": "Khung ngoài ➔ Hai nét ngang bên trong"},
            {"num": "6", "title": "Vào trước đóng sau (先进入后关门)", "desc": "Với chữ có khung bao khép kín hoàn toàn, viết khung ngoài (chừa đáy) ➔ viết ruột ➔ đóng nét đáy cuối cùng.", "eg_han": "国", "eg_py": "guó", "order": "Viết khung 冂 ➔ Viết chữ 玉 bên trong ➔ Viết nét ngang đóng đáy _"},
            {"num": "7", "title": "Giữa trước hai bên sau (先中间后两边)", "desc": "Với chữ có nét chính ở giữa đối xứng hai bên, viết nét ở giữa trước, nét trái và phải sau.", "eg_han": "小", "eg_py": "xiǎo", "order": "Nét sổ móc ở giữa ➔ Nét chấm trái ➔ Nét chấm phải"}
        ]

        for r in rules_list:
            st.markdown(f"""
            <div class="rule-item">
                <div class="rule-header">
                    <span class="rule-badge">Quy tắc {r['num']}</span>
                    <span>{r['title']}</span>
                </div>
                <p style="color:#475569; font-size:0.95rem; margin-bottom:8px;">{r['desc']}</p>
                <div style="background:#f1f5f9; border-radius:6px; padding:10px; font-size:0.9rem; display:flex; align-items:center; gap:15px; flex-wrap:wrap;">
                    <span><b>Ví dụ chữ:</b> <span class="hanzi-font">{r['eg_han']}</span> ({r['eg_py']})</span>
                    <span><b>Trình tự viết:</b> <code style="color:#e11d48;font-weight:bold;">{r['order']}</code></span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            render_play_button(r['eg_han'], f"🔊 Nghe đọc chữ {r['eg_han']}", key=f"rule_snd_{r['num']}")
            st.markdown('<div style="margin-bottom:8px;"></div>', unsafe_allow_html=True)

    # ================= TAB 4: HỆ THỐNG BỘ THỦ =================
    with tab_radicals:
        st.subheader("1. Khái niệm Bộ thủ (部首 - Bùshǒu)")
        st.write("""
        **Bộ thủ** là thành phần cơ bản cấu tạo nên chữ Hán. Hầu như mọi chữ Hán đều chứa ít nhất một bộ thủ. 
        • Bộ thủ giúp **biểu thị ý nghĩa khái quát** của chữ Hán (ví dụ: chữ có bộ Thủy thường liên quan đến nước).
        • Bộ thủ là công cụ chính để **tra cứu chữ Hán** trong từ điển giấy truyền thống.
        • Có tổng cộng **214 bộ thủ Khang Hy** trong tiếng Trung.
        """)

        st.subheader("2. Các Bộ thủ cực kỳ quan trọng trong HSK 1")
        st.write("Lớp học Pinyin và giao tiếp cơ bản cần nắm vững các bộ thủ quen thuộc sau:")

        radicals_data = [
            {"bo": "亻(人)", "pinyin": "rén", "meaning": "Bộ Nhân (Người)", "desc": "Liên quan đến con người, hành vi của con người.", "eg": "你 (nǐ - bạn), 他 (tā - anh ấy), 们 (men - số nhiều)"},
            {"bo": "女", "pinyin": "nǚ", "meaning": "Bộ Nữ (Phụ nữ)", "desc": "Liên quan đến phụ nữ, phái đẹp, quan hệ họ hàng.", "eg": "她 (tā - cô ấy), 妈 (mā - mẹ), 好 (hǎo - tốt)"},
            {"bo": "口", "pinyin": "kǒu", "meaning": "Bộ Khẩu (Miệng)", "desc": "Liên quan đến ăn uống, phát ngôn, âm thanh.", "eg": "吃 (chī - ăn), 喝 (hē - uống), 叫 (jiào - gọi), 吗 (ma - trợ từ)"},
            {"bo": "氵(水)", "pinyin": "shuǐ", "meaning": "Bộ Thủy (Nước)", "desc": "Liên quan đến nước, sông ngòi, chất lỏng.", "eg": "水 (shuǐ - nước), 汉 (hàn - Hán, sông Hán), 没 (méi - không có)"},
            {"bo": "木", "pinyin": "mù", "meaning": "Bộ Mộc (Gỗ, Cây)", "desc": "Liên quan đến thực vật, cây cối, đồ làm bằng gỗ.", "eg": "木 (mù - gỗ), 林 (lín - rừng), 桌 (zhuō - bàn), 杯 (bēi - cốc)"},
            {"bo": "火 (灬)", "pinyin": "huǒ", "meaning": "Bộ Hỏa (Lửa)", "desc": "Liên quan đến lửa, nhiệt độ, nấu nướng.", "eg": "火 (huǒ - lửa), 热 (rè - nóng), 点 (diǎn - giờ/chấm)"},
            {"bo": "讠(言)", "pinyin": "yán", "meaning": "Bộ Ngôn (Lời nói)", "desc": "Liên quan đến ngôn ngữ, lời nói, giao tiếp.", "eg": "说 (shuō - nói), 语 (yǔ - ngôn ngữ), 谁 (shéi - ai), 请 (qǐng - xin mời)"},
            {"bo": "忄(心)", "pinyin": "xīn", "meaning": "Bộ Tâm (Tim, Lòng)", "desc": "Liên quan đến tâm lý, tư duy, cảm xúc con người.", "eg": "忙 (máng - bận), 想 (xiǎng - nhớ, muốn), 怕 (pà - sợ)"}
        ]

        # RENDER RADICAL TABLE
        table_html = """
        <table class="radical-table">
            <thead>
                <tr>
                    <th style="width:15%;">Bộ thủ</th>
                    <th style="width:15%;">Phiên âm</th>
                    <th style="width:25%;">Tên gọi (Nghĩa)</th>
                    <th style="width:20%;">Ý nghĩa cốt lõi</th>
                    <th style="width:25%;">Ví dụ Hán tự</th>
                </tr>
            </thead>
            <tbody>
        """
        for r in radicals_data:
            table_html += f"""
                <tr>
                    <td class="hanzi-font" style="color:#e11d48; text-align:center;">{r['bo']}</td>
                    <td style="font-family:monospace; font-weight:bold; color:#2563eb;">{r['pinyin']}</td>
                    <td><b>{r['meaning']}</b></td>
                    <td style="font-size:0.9rem; color:#475569;">{r['desc']}</td>
                    <td style="font-size:0.92rem;">{r['eg']}</td>
                </tr>
            """
        table_html += "</tbody></table>"
        st.markdown(table_html, unsafe_allow_html=True)

    # ================= TAB 5: ĐƠN THỂ & HỢP THỂ =================
    with tab_structures:
        st.subheader("Phân Loại Chữ Đơn Thể & Chữ Hợp Thể")
        st.write("""
        Dựa vào cấu trúc hình thể, chữ Hán được chia làm hai nhóm chính: **Chữ đơn thể** (chữ độc lập) và **Chữ hợp thể** (chữ ghép).
        """)

        col_left, col_right = st.columns(2)

        with col_left:
            st.markdown("""
            <div class="hanzi-card">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
                    <span class="hanzi-title" style="color:#10b981;">Đơn thể</span>
                    <span class="meaning-badge" style="background-color:#ecfdf5; color:#047857; border:1px solid #a7f3d0;">独体字 dútǐzì</span>
                </div>
                <p><b>Khái niệm:</b> Là những chữ Hán đơn lẻ, được cấu thành trực tiếp từ các nét bút viết cơ bản độc lập. 
                Chúng không thể chia cắt hay phân tách thành các chữ nhỏ hơn có nghĩa.</p>
                <p><b>Đặc điểm:</b> Chiếm số lượng ít nhưng cực kỳ quan trọng, đa số là chữ tượng hình hoặc chỉ sự nguyên bản, và thường làm bộ thủ để cấu tạo nên chữ hợp thể.</p>
                <div style="background:#f0fdf4; border-radius:8px; padding:12px; margin-top:10px; border:1px solid #a7f3d0;">
                    <b>Ví dụ chữ đơn thể tiêu biểu:</b><br/>
                    • <b>人</b> (rén) - Người<br/>
                    • <b>木</b> (mù) - Cây/Gỗ<br/>
                    • <b>日</b> (rì) - Mặt trời / Ngày<br/>
                    • <b>月</b> (yuè) - Mặt trăng / Tháng<br/>
                    • <b>山</b> (shān) - Núi<br/>
                    • <b>水</b> (shuǐ) - Nước<br/>
                    • <b>口</b> (kǒu) - Miệng<br/>
                    • <b>女</b> (nǚ) - Phụ nữ
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col_right:
            st.markdown("""
            <div class="hanzi-card">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
                    <span class="hanzi-title" style="color:#3b82f6;">Hợp thể</span>
                    <span class="pinyin-badge" style="background-color:#eff6ff; color:#1d4ed8; border:1px solid #bfdbfe;">合体字 hétǐzì</span>
                </div>
                <p><b>Khái niệm:</b> Là những chữ Hán được ghép từ hai hoặc nhiều chữ đơn thể (hoặc bộ thủ) lại với nhau để biểu thị ý nghĩa hoặc âm đọc phức hợp.</p>
                <p><b>Đặc điểm:</b> Chiếm hơn 90% lượng chữ Hán hiện đại. Thường có cấu trúc đối xứng hoặc ghép phần rất rõ ràng.</p>
                <div style="background:#eff6ff; border-radius:8px; padding:12px; margin-top:10px; border:1px solid #bfdbfe;">
                    <b>Các dạng cấu trúc ghép phổ biến:</b><br/>
                    • <b>Ghép Trái - Phải (左右):</b><br/>
                    &nbsp;&nbsp; <i>好</i> (Tốt) = 女 (nữ) + 子 (tử)<br/>
                    &nbsp;&nbsp; <i>你</i> (Bạn) = 亻 (nhân) + 尔 (nhĩ)<br/>
                    &nbsp;&nbsp; <i>明</i> (Sáng) = 日 (nhật) + 月 (nguyệt)<br/>
                    • <b>Ghép Trên - Dưới (上下):</b><br/>
                    &nbsp;&nbsp; <i>爸</i> (Bố) = 父 (phụ) + 巴 (ba)<br/>
                    &nbsp;&nbsp; <i>字</i> (Chữ) = 宀 (miên) + 子 (tử)<br/>
                    • <b>Ghép Bao vây (包围):</b><br/>
                    &nbsp;&nbsp; <i>国</i> (Nước) = 囗 (vi) + 玉 (ngọc)<br/>
                    &nbsp;&nbsp; <i>回</i> (Về) = 囗 (vi) + 口 (khẩu)
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.subheader("💡 Mẹo ghi nhớ cấu trúc chữ Hán")
        st.write("""
        Khi học một chữ Hán mới:
        1. Hãy xác định xem đó là chữ **Đơn thể** hay **Hợp thể**.
        2. Nếu là chữ hợp thể, hãy tách nó ra thành các phần (bộ thủ biểu nghĩa + phần biểu âm).
        3. Liên tưởng câu chuyện thú vị từ nghĩa của các bộ thủ cấu thành để ghi nhớ chữ Hán lâu hơn mà không bị nhầm lẫn nét viết!
        """)
