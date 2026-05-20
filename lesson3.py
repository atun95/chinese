import streamlit as st
from lessons_data import *
from ui_utils import *

def show_lesson3_pinyin():
    render_lesson_intro("📚 Bài 3: Thanh mẫu nâng cao & Biến điệu", "Học các thanh mẫu khó (Âm mặt lưỡi, đầu lưỡi) và quy tắc biến điệu của 不.")
    for g in B2_THANH_MAU_DATA:
        st.markdown(f"#### {g['ten']}")
        cols = st.columns(4)
        for i, item in enumerate(g["items"]):
            with cols[i%4]: render_pronunciation_card(item, "b3_tm")
    
    st.markdown("---")
    st.subheader("2. Luyện tập đọc Thanh mẫu nâng cao")
    col_lt1, col_lt2 = st.columns(2)
    with col_lt1:
        st.write("**Nhóm mặt lưỡi (j, q, x):**")
        st.write("- **jī** (鸡: con gà)")
        st.write("- **qī** (七: số 7)")
        st.write("- **xǐ** (洗: rửa/giặt)")
        st.write("- **jiā** (家: nhà/gia đình)")
        
        st.write("**Nhóm đầu lưỡi (z, c, s):**")
        st.write("- **zì** (字: chữ)")
        st.write("- **cí** (词: từ/từ vựng)")
        st.write("- **sì** (四: số 4)")
        st.write("- **sān** (三: số 3)")

    with col_lt2:
        st.write("**Nhóm uốn lưỡi (zh, ch, sh, r):**")
        st.write("- **zhè** (这: đây/này)")
        st.write("- **chī** (吃: ăn)")
        st.write("- **shì** (是: là/phải)")
        st.write("- **rì** (日: ngày/mặt trời)")
        st.write("- **rén** (人: người)")
        
        st.write("**Âm đệm (y, w):**")
        st.write("- **yī** (一: số 1)")
        st.write("- **wǔ** (五: số 5)")
        st.write("- **yú** (鱼: con cá)")
    
    st.markdown("---")
    st.subheader("3. Ngữ pháp: Động từ 是 (shì) — \"là\"")

    st.info("""
    **Cấu trúc:** Chủ ngữ + **...** + Danh từ
    
    - ✅ Dùng với **danh từ**: Wǒ shì xuéshēng. (Tôi là học sinh.)
    - ❌ **Không** dùng với tính từ: ~~Wǒ shì máng~~ → Phải dùng **hěn** (很): Wǒ hěn máng.
    """)

    col_shi1, col_shi2 = st.columns(2)
    with col_shi1:
        st.success("**Câu khẳng định (是):**")
        st.write("- Wǒ shì xuéshēng. (我是学生: Tôi là học sinh.)")
        st.write("- Nǐ shì lǎoshī. (你是老师: Bạn là giáo viên.)")
        st.write("- Tā shì wǒ māma. (她是我妈妈: Cô ấy là mẹ tôi.)")
    with col_shi2:
        st.error("**Câu phủ định (不是 → bú shì):**")
        st.write("- Wǒ bú shì lǎoshī. (我...: Tôi không phải giáo viên.)")
        st.write("- Tā bú ... (他...: Anh ấy không phải học sinh.)")

    st.warning("**Câu hỏi (是...吗?):**")
    st.write("- Nǐ shì xuéshēng **ma**? (你是学生吗？: Bạn có phải học sinh không?)")
    st.write("  → Trả lời đúng: **Shì de**, wǒ shì xuéshēng. (是的，我是....)")
    st.write("  → Trả lời sai: **Bú shì**, wǒ shì lǎoshī. (不是，我是...)")

    with st.expander("💬 Hội thoại mẫu", expanded=False):
        st.code("""
A: 你好！你是老师吗？
   Nǐ hǎo! Nǐ...
   (Xin chào! Bạn có phải giáo viên không?)

B: 不是，我是学生。你呢？
   Bú shì, wǒ shì xuéshēng. Nǐ ne?
   (Không phải, tôi là học sinh. Còn bạn?)

A: 我是老师. 很高兴认识你！
   Wǒ shì lǎoshī. Hěn gāoxìng rènshi nǐ!
   (Tôi là giáo viên. Rất vui được gặp bạn!)
        """, language="text")

    st.markdown("---")
    st.subheader("4. Biến điệu của '不' (bù)")
    st.info("""
    **Quy tắc:**
    
    1. **Giữ nguyên thanh 4 (bù):**
    Khi đứng một mình hoặc đứng trước âm tiết mang **thanh 1, thanh 2, thanh 3**.
    
    2. **Biến thành thanh 2 (bú):**
    Khi đứng trước âm tiết mang **thanh 4**.
    """)
    
    st.success("**Ví dụ biến thành thanh 2 (bú):**")
    st.write("- bù qù → **bú qù** (不去: không đi)")
    st.write("- bù shì → **bú shì** (Không phải / 不是: không phải)")
    st.write("- bù è → **bú è** (不饿: không đói)")
    st.write("- bù lèi → **bú lèi** (不累: không mệt)")
    st.write("- bù duì → **bú duì** (不对: không đúng)")
    
    st.warning("**Ví dụ giữ nguyên thanh 4 (bù):**")
    st.write("- bù hē (不喝: không uống) - *Thanh 1*")
    st.write("- bù lái (不来: không đến) - *Thanh 2*")
    st.write("- bù nán (不难: không khó) - *Thanh 2*")
    st.write("- bù hǎo (不好: không tốt) - *Thanh 3*")
    st.write("- bù xiǎo (不小: không nhỏ) - *Thanh 3*")
    
    st.markdown("---")
    st.markdown("#### Luyện tập thêm & Câu ngắn:")
    col_ex3, col_ex4 = st.columns(2)
    with col_ex3:
        st.write("**Từ vựng:**")
        st.write("- bù gāo (不高: không cao)")
        st.write("- bù máng (不忙: không bận)")
        st.write("- bù lěng (不冷: không lạnh)")
        st.write("- bù tīng (不听: không nghe)")
    with col_ex4:
        st.write("**Câu ngắn:**")
        st.write("- Wǒ **bú qù**. (我不去: Tôi không đi.)")
        st.write("- Tā **bú ...** (他...: Anh ấy không phải thầy giáo.)")
        st.write("- Wǒ **bù máng**. (我不忙: Tôi không bận.)")
        st.write("- Nǐ hǎo **bù hǎo**? (你好不好: Bạn khỏe không?)")
        st.write("- Chī **bù chī**? (吃不吃: Ăn không?)")

def show_lesson3_pinyin_rules():
    render_lesson_intro("📚 Bài 3: Quy tắc viết Pinyin", "Nắm vững các quy tắc biến đổi chữ viết của i, u, ü trong bính âm.")
    
    st.subheader("1. Quy tắc phát âm chữ 'i'")
    st.info("Chữ 'i' có 2 cách đọc chính tùy thuộc vào chữ cái đi trước nó.")
    col_i1, col_i2 = st.columns(2)
    with col_i1:
        st.success("**Đọc là 'i' như tiếng Việt**")
        st.write("- **Khi nào đọc:** Khi 'i' đứng một mình (viết thành **yi**) hoặc đi sau các phụ âm: **b, p, m, f, d, t, n, l, j, q, x, y**.")
        st.write("- **Cách phát âm:** Khóe môi hơi dẹt, bè sang hai bên. Giống hệt âm 'i' tiếng Việt.")
        st.write("- **Ví dụ:**\n  - **yī** (一 - số một) đọc là 'i'\n  - **nǐ** (你 - bạn) đọc là 'ni'")
    with col_i2:
        st.warning("**Đọc là 'ư'**")
        st.write("- **Khi nào đọc:** Khi 'i' đứng sau 7 phụ âm uốn lưỡi và đầu lưỡi: **zh, ch, sh, r, z, c, s**.")
        st.write("- **Cách phát âm:** Đọc kéo dài âm 'ư' của tiếng Việt.")
        st.write("- **Ví dụ:**\n  - **shī** (师 - giáo viên) đọc là 'sư'\n  - **sī** (私 - riêng tư) đọc là 'sư'")
        
    st.markdown("---")
    st.subheader("2. Quy tắc viết i, u, ü khi không có thanh mẫu")
    st.write("Khi một âm tiết không có phụ âm đầu (thanh mẫu), ta cần thêm hoặc đổi chữ cái đầu thành **y** hoặc **w**.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**i → thêm y** (*Nhớ: i đầu câu → đổi thành y*)")
        st.write("- **i** → **yi** (yī 一)")
        st.write("- **ia** → **ya** (yā 压)")
        st.write("- **iao** → **yao** (yào 要)")
        st.write("- **ie** → **ye** (yě 也)")
        st.write("- **iu** → **you** (yǒu 有)")
        st.write("- **ian** → **yan** (yán 言)")
        st.write("- **in** → **yin** (yīn 音)")
        st.write("- **ing** → **ying** (yīng 英)")
    with col2:
        st.markdown("**u → thêm w** (*Nhớ: u đầu câu → đổi thành w*)")
        st.write("- **u** → **wu** (wú 五)")
        st.write("- **ua** → **wa** (wá 娃)")
        st.write("- **uo** → **wo** (wǒ 我)")
        st.write("- **uai** → **wai** (wài 外)")
        st.write("- **ui** → **wei** (wèi 为)")
        st.write("- **uan** → **wan** (wán 完)")
        st.write("- **un** → **wen** (wén 文)")
    with col3:
        st.markdown("**ü → thêm y** (*Nhớ: ü đầu câu → viết y + phần còn lại*)")
        st.write("- **ü** → **yu** (yú 鱼)")
        st.write("- **üe** → **yue** (yuè 月)")
        st.write("- **üan** → **yuan** (yuán 元)")
        st.write("- **ün** → **yun** (yún 云)")

    st.markdown("---")
    st.subheader("3. Các thanh mẫu kết hợp với ü và quy tắc bỏ dấu chấm")
    st.write("Nguyên âm **ü** không kết hợp với tất cả thanh mẫu. Nó chủ yếu đi với: **j, q, x, n, l, y**.")
    
    col_u1, col_u2 = st.columns(2)
    with col_u1:
        st.success("**Nhóm 1: Dấu ü BỊ BỎ CHẤM (j, q, x, y)**")
        st.write("Sau 4 âm này, viết là **u** nhưng vẫn đọc là **ü**:")
        st.write("- j + ü = **ju** (jū)")
        st.write("- q + ü = **qu** (qù)")
        st.write("- x + ü = **xue** (xué)")
        st.write("- y + ü = **yue** (yuè)")
    with col_u2:
        st.error("**Nhóm 2: Phải GIỮ DẤU CHẤM (n, l)**")
        st.write("Vì n, l còn ghép được với u thường, nên phải viết rõ dấu hai chấm để phân biệt:")
        st.write("- **nǔ** (n + u) ≠ **nǚ** (n + ü)")
        st.write("- **lù** (l + u) ≠ **lǜ** (l + ü)")

    st.markdown("#### Bảng ghép âm ü với 4 thanh điệu")
    st.markdown("""
    <table class="chinese-table" style="width:100%; text-align:center;">
        <thead>
            <tr>
                <th class="tm-header" style="text-align:center;">Thanh mẫu</th>
                <th class="tm-header" style="text-align:center;">Ghép với ü</th>
                <th class="tm-header" style="text-align:center;">Thanh 1</th>
                <th class="tm-header" style="text-align:center;">Thanh 2</th>
                <th class="tm-header" style="text-align:center;">Thanh 3</th>
                <th class="tm-header" style="text-align:center;">Thanh 4</th>
            </tr>
        </thead>
        <tbody>
            <tr><td><b>j</b></td><td class="pinyin-text">ju</td><td class="pinyin-text">jū</td><td class="pinyin-text">jú</td><td class="pinyin-text">jǔ</td><td class="pinyin-text">jù</td></tr>
            <tr><td><b>q</b></td><td class="pinyin-text">qu</td><td class="pinyin-text">qū</td><td class="pinyin-text">qú</td><td class="pinyin-text">qǔ</td><td class="pinyin-text">qù</td></tr>
            <tr><td><b>x</b></td><td class="pinyin-text">xu</td><td class="pinyin-text">xū</td><td class="pinyin-text">xú</td><td class="pinyin-text">xǔ</td><td class="pinyin-text">xù</td></tr>
            <tr><td><b>y</b></td><td class="pinyin-text">yu</td><td class="pinyin-text">yū</td><td class="pinyin-text">yú</td><td class="pinyin-text">yǔ</td><td class="pinyin-text">yù</td></tr>
            <tr><td><b>n</b></td><td class="pinyin-text">nü</td><td class="pinyin-text">nǖ</td><td class="pinyin-text">nǘ</td><td class="pinyin-text">nǚ</td><td class="pinyin-text">nǜ</td></tr>
            <tr><td><b>l</b></td><td class="pinyin-text">lü</td><td class="pinyin-text">lǖ</td><td class="pinyin-text">lǘ</td><td class="pinyin-text">lǚ</td><td class="pinyin-text">lǜ</td></tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)

def show_lesson3_vocab():
    render_lesson_intro("📚 Bài 3: Từ vựng & Cấu trúc câu", "Học từ vựng mới, tên riêng và cách đặt câu cơ bản.")
    
    st.subheader("1. Từ vựng & Tên riêng")
    vocab_data = [
        {"han": "律师", "pinyin": "lǜshī", "mean": "luật sư"},
        {"han": "朋友", "pinyin": "péngyou", "mean": "bạn, bạn bè"},
        {"han": "男", "pinyin": "nán", "mean": "nam"},
        {"han": "女", "pinyin": "nǚ", "mean": "nữ"},
        {"han": "男朋友", "pinyin": "nánpéngyou", "mean": "bạn trai"},
        {"han": "女朋友", "pinyin": "nǚpéngyou", "mean": "bạn gái"},
        {"han": "叫", "pinyin": "jiào", "mean": "gọi, tên là"},
        {"han": "名字", "pinyin": "míngzi", "mean": "tên"},
        {"han": "高兴", "pinyin": "gāoxìng", "mean": "vui vẻ"},
        {"han": "认识", "pinyin": "rènshi", "mean": "quen biết"},
        {"han": "你叫什么名字？", "pinyin": "Nǐ jiào shénme míngzi?", "mean": "Bạn tên là gì?"},
        {"han": "青", "pinyin": "Qīng", "mean": "tên Thanh"},
        {"han": "薇", "pinyin": "Wēi", "mean": "tên Vy"},
        {"han": "珍", "pinyin": "Zhēn", "mean": "tên Trân"},
        {"han": "仙", "pinyin": "Xiān", "mean": "tên Tiên"},
    ]
    
    html = '<table class="chinese-table"><thead><tr><th style="text-align:center;">Chữ Hán</th><th style="text-align:center;">Phiên âm</th><th>Nghĩa tiếng Việt</th></tr></thead><tbody>'
    for v in vocab_data:
        html += f'<tr><td style="text-align:center; font-size: 1.2em;"><b>{v["han"]}</b></td><td class="pinyin-text" style="text-align:center;">{v["pinyin"]}</td><td>{v["mean"]}</td></tr>'
    html += '</tbody></table>'
    st.markdown(html, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("2. Văn hóa & Cách gọi tên thân mật (阿, 小, 老...)")
    
    st.markdown("""
<div style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); border-left: 6px solid #3b82f6; border-radius: 12px; padding: 20px; margin: 15px 0; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
<div style="background-color: #3b82f6; color: white; padding: 4px 10px; border-radius: 6px; font-size: 0.85em; font-weight: bold; display: inline-block; margin-bottom: 12px;">🏮 GÓC VĂN HÓA & NGÔN NGỮ</div>
<h4 style="color: #1e3a8a; margin-top: 0; margin-bottom: 10px; font-weight: bold;">Chữ 阿 (ā) trước tên trong tiếng Trung</h4>
<p style="color: #334155; line-height: 1.6; margin-bottom: 15px;">
Chữ <b>阿 (ā)</b> đặt trước tên trong tiếng Trung là cách gọi <b>thân mật, gần gũi</b> — hơi tương đương với cách xưng hô <i>“anh/chị/em”</i> hoặc các kiểu gọi nickname thân quen trong tiếng Việt.
</p>
<div style="display: flex; gap: 15px; margin-bottom: 20px; flex-wrap: wrap;">
<div style="flex: 1; min-width: 220px; background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); border: 1px solid #e2e8f0;">
<div style="font-weight: bold; color: #0f172a; margin-bottom: 8px; border-bottom: 2px solid #e2e8f0; padding-bottom: 4px;">Ví dụ tiêu biểu:</div>
<ul style="margin: 0; padding-left: 20px; color: #475569; line-height: 1.8;">
<li><span class="pinyin-text" style="font-size:1.1em; color:#2563eb;">阿俊</span> (ā jùn) = “A Tuấn”</li>
<li><span class="pinyin-text" style="font-size:1.1em; color:#2563eb;">阿恒</span> (ā héng) = “A Hằng”</li>
<li><span class="pinyin-text" style="font-size:1.1em; color:#2563eb;">阿明</span> (ā míng) = “A Minh”</li>
</ul>
</div>
<div style="flex: 1; min-width: 220px; background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); border: 1px solid #e2e8f0;">
<div style="font-weight: bold; color: #0f172a; margin-bottom: 8px; border-bottom: 2px solid #e2e8f0; padding-bottom: 4px;">Sắc thái biểu đạt:</div>
<span style="color: #475569;">Không mang nghĩa thực tế mạnh, chủ yếu tạo cảm giác:</span>
<div style="margin-top: 8px; display: flex; flex-wrap: wrap; gap: 6px;">
<span style="background:#f1f5f9; padding:2px 8px; border-radius:4px; font-size:0.9em; color:#0f172a; border: 1px solid #cbd5e1; font-weight: 500;">Thân quen</span>
<span style="background:#f1f5f9; padding:2px 8px; border-radius:4px; font-size:0.9em; color:#0f172a; border: 1px solid #cbd5e1; font-weight: 500;">Bình dân</span>
<span style="background:#f1f5f9; padding:2px 8px; border-radius:4px; font-size:0.9em; color:#0f172a; border: 1px solid #cbd5e1; font-weight: 500;">Gần gũi</span>
</div>
<div style="margin-top: 10px; font-size: 0.9em; color: #64748b;">
👉 Dùng gọi trong: <i>Gia đình, bạn bè thân thiết, hàng xóm, hoặc... giang hồ xã hội đen</i> 😄
</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)
 
    col_og1, col_og2 = st.columns(2)
    with col_og1:
        st.markdown("""
<div style="background-color: #f0fdf4; border-left: 4px solid #16a34a; padding: 15px; border-radius: 8px; height: 100%;">
<h5 style="color: #14532d; margin-top:0; font-weight: bold;">❓ Vì sao lại dùng "阿"?</h5>
<p style="font-size: 0.95em; color: #166534; line-height: 1.5; margin-bottom: 8px;">
Ngày xưa trong nhiều phương ngữ Trung Quốc (đặc biệt là <b>miền Nam</b> như: <i>Quảng Đông, Mân Nam, Triều Châu, Ngô/Thượng Hải</i>), người ta hay thêm âm đệm <b>"阿"</b> trước tên để gọi cho thuận miệng. Sau này, nó đã trở thành một thói quen văn hóa ăn sâu vào đời sống hàng ngày.
</p>
<div style="background: white; padding: 10px; border-radius: 6px; border: 1px solid #bbf7d0; margin-top: 10px;">
<b>Ví dụ phổ biến:</b><br/>
- <b>阿强</b> (ā qiáng) ~ "thằng Cường"<br/>
- <b>阿玲</b> (ā líng) ~ "con Linh"<br/>
- <b>阿华</b> (ā huá) ~ "anh Hoa"<br/>
<span style="font-size: 0.85em; color: #666;">(Mang sắc thái thân mật giống tiếng Việt nhưng lịch sự, nhẹ nhàng hơn)</span>
</div>
</div>
""", unsafe_allow_html=True)
 
    with col_og2:
        st.markdown("""
<div style="background-color: #fffaf0; border-left: 4px solid #dd6b20; padding: 15px; border-radius: 8px; height: 100%;">
<h5 style="color: #7b341e; margin-top:0; font-weight: bold;">👥 Đối tượng sử dụng & Lưu ý</h5>
<ul style="font-size: 0.95em; color: #7b341e; line-height: 1.5; padding-left: 20px; margin-bottom: 10px;">
<li><b>Hay dùng với:</b> Bạn bè thân thiết, người yêu, người trong nhà, người lớn gọi trẻ con, hoặc các nhân vật trong phim ảnh Hong Kong.</li>
<li><b>Không dùng:</b> Trong các hoàn cảnh trang trọng, công sở lịch sự.</li>
</ul>
<div style="background: white; padding: 10px; border-radius: 6px; border: 1px solid #fed7aa; margin-top: 5px;">
<b>⚠️ Cực kỳ quan trọng:</b> Bạn sẽ không tự giới thiệu bản thân bằng "阿"!<br/>
- ❌ Không nói: <span style="color:#e53e3e; font-weight:bold;">我叫阿俊</span> (Wǒ jiào Ā Jùn)<br/>
- ✔️ Nên nói: <span style="color:#38a169; font-weight:bold;">我叫... (tên đầy đủ)</span> (Ví dụ: 我叫<b>俊杰</b>)
</div>
</div>
""", unsafe_allow_html=True)
 
    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown("#### 💡 Các cách gọi thân mật phổ biến khác")
    
    col_alt1, col_alt2, col_alt3 = st.columns(3)
    with col_alt1:
        st.markdown("""
<div style="background-color: #fdf2f8; border-top: 4px solid #db2777; padding: 15px; border-radius: 8px; height: 260px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);">
<div>
<h5 style="color: #831843; margin-top:0; font-weight: bold;">1. 小 (xiǎo) - "Tiểu / Nhỏ"</h5>
<p style="font-size: 0.9em; color: #9d174d; line-height: 1.4;">
Thường dùng để gọi những người <b>trẻ tuổi hơn</b> hoặc có dáng người nhỏ nhắn, thể hiện sự dễ thương, thân thiết.
</p>
</div>
<div style="background: white; padding: 8px; border-radius: 6px; border: 1px solid #fbcfe8;">
<b>Ví dụ:</b><br/>
- <b>小王</b> (Xiǎo Wáng): Tiểu Vương<br/>
- <b>小李</b> (Xiǎo Lǐ): Tiểu Lý
</div>
</div>
""", unsafe_allow_html=True)
 
    with col_alt2:
        st.markdown("""
<div style="background-color: #f0fdfa; border-top: 4px solid #0d9488; padding: 15px; border-radius: 8px; height: 260px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);">
<div>
<h5 style="color: #115e59; margin-top:0; font-weight: bold;">2. 老 (lǎo) - "Lão"</h5>
<p style="font-size: 0.9em; color: #134e4a; line-height: 1.4;">
Dành cho người <b>lớn tuổi hơn</b> hoặc bạn bè chơi thân lâu năm. Không mang nghĩa là "già cỗi", mà thể hiện sự tôn trọng, xu hướng dân dã.
</p>
</div>
<div style="background: white; padding: 8px; border-radius: 6px; border: 1px solid #99f6e4;">
<b>Ví dụ:</b><br/>
- <b>老张</b> (Lǎo Zhāng): Lão Trương / Ông Trương<br/>
- <b>老陈</b> (Lǎo Chén): Lão Trần / Ông Trần
</div>
</div>
""", unsafe_allow_html=True)
 
    with col_alt3:
        st.markdown("""
<div style="background-color: #f5f3ff; border-top: 4px solid #7c3aed; padding: 15px; border-radius: 8px; height: 260px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);">
<div>
<h5 style="color: #4c1d95; margin-top:0; font-weight: bold;">3. Tên lặp đôi</h5>
<p style="font-size: 0.9em; color: #5b21b6; line-height: 1.4;">
Lặp lại từ cuối cùng trong tên riêng. Cách gọi này cực kỳ ngọt ngào, phổ biến để gọi <b>trẻ con, con gái, hoặc người yêu</b>.
</p>
</div>
<div style="background: white; padding: 8px; border-radius: 6px; border: 1px solid #ddd6fe;">
<b>Ví dụ:</b><br/>
- <b>明明</b> (Míngmíng): Minh Minh<br/>
- <b>婷婷</b> (Tíngting): Đình Đình<br/>
- <b>乐乐</b> (Lèlè): Nhạc Nhạc
</div>
</div>
""", unsafe_allow_html=True)
 
    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown("""
<div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border-radius: 10px; padding: 15px; color: #f8fafc; border: 1px solid #334155;">
<span style="color:#38bdf8; font-weight:bold; font-size:0.9em; text-transform:uppercase; letter-spacing:1px;">💡 Tóm lại nhanh:</span>
<ul style="margin: 8px 0 0 0; padding-left: 20px; font-size: 0.95em; color: #cbd5e1; line-height: 1.6;">
<li><b>阿 (ā) + Tên</b>: Cách gọi thân mật đậm chất phương ngữ miền Nam Trung Quốc (không dịch sát nghĩa, tương đương "A + tên" hoặc nickname thân quen).</li>
<li><b>Không</b> dùng khi tự giới thiệu bản thân trong tình huống trang trọng!</li>
</ul>
</div>
""", unsafe_allow_html=True)
 
    st.markdown("---")
    st.subheader("3. Cấu trúc câu & Từ để hỏi")
    st.info("Các từ dùng để cấu tạo câu khẳng định, phủ định và câu hỏi.")
    
    grammar_data = [
        {"han": "是", "pinyin": "shì", "mean": "là"},
        {"han": "不是", "pinyin": "bú shì", "mean": "không phải (là)"},
        {"han": "有", "pinyin": "yǒu", "mean": "có"},
        {"han": "没有", "pinyin": "méiyǒu", "mean": "không có"},
        {"han": "你呢", "pinyin": "nǐ ne", "mean": "còn bạn thì sao?"},
        {"han": "吗", "pinyin": "ma", "mean": "không? (đặt ở cuối câu hỏi)"},
    ]
    html_gr = '<table class="chinese-table"><thead><tr><th style="text-align:center;">Chữ Hán</th><th style="text-align:center;">Phiên âm</th><th>Cách dùng / Nghĩa</th></tr></thead><tbody>'
    for g in grammar_data:
        html_gr += f'<tr><td style="text-align:center; font-size: 1.2em;"><b>{g["han"]}</b></td><td class="pinyin-text" style="text-align:center;">{g["pinyin"]}</td><td>{g["mean"]}</td></tr>'
    html_gr += '</tbody></table>'
    st.markdown(html_gr, unsafe_allow_html=True)
 
    st.markdown("#### 💡 Cách đặt câu hỏi với 是 và 有")
    col_q1, col_q2 = st.columns(2)
    with col_q1:
        st.success("**Động từ 是 (shì - là)**")
        st.write("Có 2 cách để hỏi 'có phải là... không?':")
        st.write("1. Dùng trợ từ **吗 (ma)** ở cuối câu:")
        st.write("👉 Chủ ngữ + **是** + [Danh từ] + **吗**？")
        st.write("*(Ví dụ: 你**是**青**吗**？ - Bạn là Thanh phải không?)*")
        st.write("2. Dùng mẫu câu chính phản **chính phản**:")
        st.write("👉 Chủ ngữ + **是不是** + [Danh từ]？")
        st.write("*(Ví dụ: 你**是不是**青？ - Bạn có phải là Thanh không?)*")
        
    with col_q2:
        st.warning("**Động từ 有 (yǒu - có)**")
        st.write("Có 2 cách để hỏi 'có... không?':")
        st.write("1. Dùng trợ từ **吗 (ma)** ở cuối câu:")
        st.write("👉 Chủ ngữ + **有** + [Danh từ] + **吗**？")
        st.write("*(Ví dụ: 你**有**男朋友**吗**？ - Bạn có bạn trai không?)*")
        st.write("2. Dùng mẫu câu chính phản **有没有 (yǒu méiyǒu)**:")
        st.write("👉 Chủ ngữ + **有没有** + [Danh từ]？")
        st.write("*(Ví dụ: 你**有没有**男朋友？ - Bạn có bạn trai không?)*")
    
    st.info("📌 **Mẹo nhỏ:** Khi đã dùng **是不是** hoặc **有没有** thì tuyệt đối KHÔNG dùng thêm **吗** ở cuối câu nữa nhé!")
    st.markdown("---")
    st.subheader("4. Hội thoại giao tiếp mẫu")
    st.info("Luyện tập các mẫu câu chào hỏi và ứng dụng từ vựng vừa học.")
    
    with st.expander("💬 Hội thoại 1: Chào hỏi & Tên tuổi", expanded=True):
        st.code("""
A: 你好！
   Xin chào!

B: 你好！我叫青。你呢？
   Xin chào! Tôi tên Thanh. Còn bạn?

A: 我叫薇。很高兴认识你。
   Tôi tên Vy. Rất vui được gặp bạn.
""", language="text")
        st.markdown("""
<div style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); 
            border-left: 5px solid #10b981; 
            border-radius: 8px; 
            padding: 15px; 
            margin-top: 15px; 
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); 
            max-width: 650px;">
    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px;">
        <span style="font-size: 1.2em;">💡</span>
        <strong style="color: #0f172a; font-size: 1.05em;">So sánh: 我叫青 (Wǒ jiào Qīng) và 我是青 (Wǒ shì Qīng)</strong>
    </div>
    <div style="font-size: 0.95em; line-height: 1.5; color: #334155;">
        <div style="margin-bottom: 10px; padding-left: 8px; border-left: 3px solid #3b82f6;">
            <strong style="color: #2563eb;">我叫青</strong> <span class="pinyin-text" style="color: #475569;">(Wǒ jiào Qīng)</span>: <i>"Tôi tên là Thanh"</i><br/>
            👉 Dùng để <b>giới thiệu tên tự nhiên và phổ biến nhất</b> khi gặp mặt. Từ <b>叫 (jiào)</b> mang nghĩa là "gọi là, tên là".
        </div>
        <div style="padding-left: 8px; border-left: 3px solid #f59e0b;">
            <strong style="color: #d97706;">我是青</strong> <span class="pinyin-text" style="color: #475569;">(Wǒ shì Qīng)</span>: <i>"Tôi là Thanh"</i><br/>
            👉 Nhấn mạnh <b>xác nhận thân phận</b>. Thường dùng khi ai đó đang tìm bạn và bạn lên tiếng xác nhận <i>"Tôi chính là Thanh đây"</i>.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
 
    with st.expander("💬 Hội thoại 2: Hỏi thăm sức khỏe", expanded=True):
        st.code("""
A: 你好吗？
   Bạn khỏe không?

B: 我很好。你忙吗？
   Tôi khỏe. Bạn bận không?

A: 我不忙。
   Tôi không bận.
""", language="text")
 
    with st.expander("💬 Hội thoại 3: Sử dụng 是, 不是, 有, 没有", expanded=True):
        st.code("""
A: 你是律师吗？
   Bạn là luật sư phải không?

B: 不是，我不是律师。
   Không phải, tôi không phải luật sư.

A: 你有男朋友吗？
   Bạn có bạn trai không?

B: 我没有男朋友。你呢？
   Tôi không có bạn trai. Còn bạn?

A: 我有女朋友。
   Tôi có bạn gái.
""", language="text")


def show_lesson3_practice(add_tones):
    from lessons_data import B3_LUYEN_TAP_FINALS, B3_LUYEN_TAP_ROWS
    render_lesson_intro("📚 Bài 3: Luyện tập ghép âm", "Luyện ghép các thanh mẫu nâng cao (z, c, s, zh, ch, sh, r, j, q, x) với các vận mẫu cơ bản và vận mẫu kép.")
    st.subheader("Bảng luyện tập ghép âm nâng cao")
    
    h_cols = st.columns([1.5] + [1] * len(B3_LUYEN_TAP_FINALS))
    h_cols[0].markdown("**T/V**")
    for i, f in enumerate(B3_LUYEN_TAP_FINALS): h_cols[i+1].markdown(f"**{f}**")
    for init in B3_LUYEN_TAP_ROWS.keys():
        r_cols = st.columns([1.5] + [1] * len(B3_LUYEN_TAP_FINALS))
        r_cols[0].markdown(f"**{init}**")
        for i, combo in enumerate(B3_LUYEN_TAP_ROWS[init]):
            if combo:
                with r_cols[i+1]:
                    with st.popover(combo, use_container_width=True):
                        for t in add_tones(combo): st.write(f"- {t}")
            else:
                r_cols[i+1].write("")





def show_lesson3_dialogues():
    render_lesson_intro("📚 Bài 3: Hội thoại thực hành", "Ứng dụng các thanh mẫu nâng cao, quy tắc viết bính âm và từ vựng đã học vào các ngữ cảnh hội thoại giao tiếp 2 người, 3 người và 4 người.")
    
    # Helper to render a compact dialogue row
    def dialogue_row(speaker_name, speaker_color, hanzi, pinyin, translation):
        return f"""
        <div style="display: flex; align-items: flex-start; padding: 6px 0; border-bottom: 1px solid #f1f5f9; font-size: 0.95em;">
            <div style="width: 140px; min-width: 140px; font-weight: 700; color: {speaker_color}; font-size: 0.9em; padding-top: 4px;">👤 {speaker_name}</div>
            <div style="flex-grow: 1; display: flex; flex-wrap: wrap; align-items: center; gap: 8px 12px; margin-left: 10px;">
                <span style="font-size: 1.15em; font-weight: 700; color: #0f172a; min-width: 180px; display: inline-block;">{hanzi}</span>
                <span style="font-family: 'Courier New', monospace; font-weight: 700; color: #2563eb; font-size: 0.95em; background-color: #eff6ff; padding: 2px 8px; border-radius: 4px;">{pinyin}</span>
                <span style="color: #64748b; font-size: 0.92em; font-style: italic;">{translation}</span>
            </div>
        </div>
        """

    tab1, tab2, tab3 = st.tabs(["👥 Hội thoại 2 người", "👥 Hội thoại 3 người", "👥 Hội thoại 4 người"])

    with tab1:
        st.markdown(f"""
        <div style="background-color: #f8fafc; border-left: 4px solid #3b82f6; padding: 10px 12px; border-radius: 6px; margin-bottom: 12px; font-size: 0.92em;">
            <strong>🗣️ Ngữ cảnh:</strong> A Thanh (Ā Qīng - Học sinh) gặp A Vy (Ā Wēi - Luật sư). Họ chào nhau, giới thiệu tên, nghề nghiệp và rủ nhau đi ăn.
        </div>
        <div style="background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 6px 16px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.01);">
            {dialogue_row("A Thanh (阿青)", "#2563eb", "你好！", "Nǐ hǎo!", "Xin chào!")}
            {dialogue_row("A Vy (阿薇)", "#10b981", "你好！力叫什么名字？", "Nǐ hǎo! Nǐ jiào shénme míngzi?", "Xin chào! Bạn tên là gì vậy?")}
            {dialogue_row("A Thanh (阿青)", "#2563eb", "我叫阿青。你呢？", "Wǒ jiào Ā Qīng. Nǐ ne?", "Tôi tên là A Thanh. Còn bạn?")}
            {dialogue_row("A Vy (阿薇)", "#10b981", "我叫阿薇。", "Wǒ jiào Ā Wēi.", "Tôi tên là A Vy.")}
            {dialogue_row("A Thanh (阿青)", "#2563eb", "很高兴认识你，阿薇。你是老师吗？", "Hěn gāoxìng rènshi nǐ, Ā Wēi. Nǐ shì lǎoshī ma?", "Rất vui được gặp bạn, A Vy. Bạn là giáo viên phải không?")}
            {dialogue_row("A Vy (阿薇)", "#10b981", "不是，我不是老师。我是律师。你呢？你是律师吗？", "Bú shì, wǒ bú shì lǎoshī. Wǒ shì lǜshī. Nǐ ne? Nǐ shì lǜshī ma?", "Không phải, tôi không phải giáo viên. Tôi là luật sư. Còn bạn? Bạn cũng là luật sư à?")}
            {dialogue_row("A Thanh (阿青)", "#2563eb", "不是，我是学生。你忙吗？", "Bú shì, wǒ shì xuéshēng. Nǐ máng ma?", "Không phải, tôi là học sinh. Tôi không bận. Bạn có bận không?")}
            {dialogue_row("A Vy (阿薇)", "#10b981", "我很忙。", "Wǒ hěn máng.", "Tôi rất bận.")}
            {dialogue_row("A Thanh (阿青)", "#2563eb", "你有男朋友吗？", "Nǐ yǒu nánpéngyou ma?", "Bạn có bạn trai chưa?")}
            {dialogue_row("A Vy (阿薇)", "#10b981", "我没有男朋友。你呢？", "Wǒ méiyǒu nánpéngyou. Nǐ ne?", "Tôi không có bạn trai. Còn bạn?")}
            {dialogue_row("A Thanh (阿青)", "#2563eb", "我有女朋友。她很好。", "Wǒ yǒu nǚpéngyou. Tā hěn hǎo.", "Tôi có bạn gái rồi. Cô ấy rất tốt.")}
            {dialogue_row("A Vy (阿薇)", "#10b981", "你饿吗？去吃吗？", "Nǐ è ma? Qù chī ma?", "Bạn có đói không? Có đi ăn không?")}
            {dialogue_row("A Thanh (阿青)", "#2563eb", "我很饿。去吧，去吃鸡！", "Wǒ hěn è. Qù ba, qù chī jī!", "Tôi rất đói. Đi thôi, đi ăn thịt gà nào!")}
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown(f"""
        <div style="background-color: #f8fafc; border-left: 4px solid #8b5cf6; padding: 10px 12px; border-radius: 6px; margin-bottom: 12px; font-size: 0.92em;">
            <strong>🗣️ Ngữ cảnh:</strong> A Trân (Ā Zhēn) tình cờ gặp A Tiên (Ā Xiān) trên đường và giới thiệu người bạn đi cùng mình là A Thanh (Ā Qīng) cho A Tiên làm quen.
        </div>
        <div style="background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 6px 16px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.01);">
            {dialogue_row("A Trân (阿珍)", "#8b5cf6", "阿仙，你好吗？", "Ā Xiān, nǐ hǎo ma?", "A Tiên, bạn khỏe không?")}
            {dialogue_row("A Tiên (阿仙)", "#f59e0b", "我很好！你呢，阿珍？", "Wǒ hěn hǎo! Nǐ ne, Ā Zhēn?", "Tôi rất khỏe! Còn bạn thì sao, A Trân?")}
            {dialogue_row("A Trân (阿珍)", "#8b5cf6", "我也很好。这是我朋友，他叫阿青。", "Wǒ yě hěn hǎo. Zhè shì wǒ péngyou, tā jiào Ā Qīng.", "Tôi cũng rất khỏe. Đây là bạn của tôi, cậu ấy tên là A Thanh.")}
            {dialogue_row("A Tiên (阿仙)", "#f59e0b", "你好，阿青！很高兴认识你！", "Nǐ hǎo, Ā Qīng! Hěn gāoxìng rènshi nǐ!", "Chào cậu, A Thanh! Rất vui được quen biết cậu!")}
            {dialogue_row("A Thanh (阿青)", "#2563eb", "你好，阿仙！我也很高兴认识你。你是学生吗？", "Nǐ hǎo, Ā Xiān! Wǒ yě hěn gāoxìng rènshi nǐ. Nǐ shì xuéshēng ma?", "Chào cậu, A Tiên! Tớ cũng rất vui được quen biết cậu. Cậu là học sinh à?")}
            {dialogue_row("A Tiên (阿仙)", "#f59e0b", "不是，我是律师。阿青，你是老师吗？", "Bùshì, wǒ shì lǜshī。. Ā Qīng, nǐ shì lǎoshī ma?", "Đúng vậy, tớ là học sinh. A Thanh, cậu là giáo viên phải không?")}
            {dialogue_row("A Thanh (阿青)", "#2563eb", "不是，我不是老师。我是律师。", "Bú ... wǒ bú ... lǎoshī. Wǒ shì lǜshī.", "Không phải, tớ không phải giáo viên. Tớ là luật sư.")}
            {dialogue_row("A Tiên (阿仙)", "#f59e0b", "哇，你是律师！那你忙吗？", "Wa, nǐ shì lǜshī! Nà nǐ máng ma?", "Oa, cậu là luật sư cơ à! Thế cậu có bận không?")}
            {dialogue_row("A Thanh (阿青)", "#2563eb", "我不忙。今天我不忙。", "Wǒ bù máng. Jīntiān wǒ bù máng.", "Tớ không bận. Hôm nay tớ không bận.")}
            {dialogue_row("A Trân (阿珍)", "#8b5cf6", "你们累吗？去喝奶茶吧？", "Nǐmen lèi ma? Qù hē nǎichá ba?", "Các cậu có mệt không? Chúng ta đi uống nước nhé?")}
            {dialogue_row("A Tiên (阿仙)", "#f59e0b", "我不累。去吧！", "Wǒ bú lèi. Qù ba!", "Tớ không mệt. Đi thôi nào!")}
            {dialogue_row("A Thanh (阿青)", "#2563eb", "去吧！", "Qù ba!", "Đi thôi!")}
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown(f"""
        <div style="background-color: #f8fafc; border-left: 4px solid #f59e0b; padding: 10px 12px; border-radius: 6px; margin-bottom: 12px; font-size: 0.92em;">
            <strong>🗣️ Ngữ cảnh:</strong> Cuộc tụ họp cuối tuần vui vẻ giữa 4 người bạn: A Vy, A Thanh, A Trân và A Tiên. Họ trao đổi về công việc, đời sống và cùng bàn bạc xem hôm nay ăn gì.
        </div>
        <div style="background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 6px 16px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.01);">
            {dialogue_row("A Vy (阿薇)", "#10b981", "你们好！", "Nǐmen hǎo!", "Chào các bạn!")}
            {dialogue_row("A Thanh (阿青)", "#2563eb", "阿薇，你好！你忙吗？", "Ā Wēi, nǐ hǎo! Nǐ máng ma?", "A Vy, chào bạn! Bạn bận không?")}
            {dialogue_row("A Vy (阿薇)", "#10b981", "我很忙。你们呢？", "Wǒ hěn máng. Nǐmen ne?", "Tôi rất bận. Còn các bạn thì sao?")}
            {dialogue_row("A Trân (阿珍)", "#8b5cf6", "我们不忙。这是阿仙，她是我的好朋友。", "Wǒmen bù máng. Zhè ... Ā Xiān, tā shì wǒ de hǎo péngyou.", "Chúng tôi không bận. Đây là A Tiên, cô ấy là bạn thân của tôi.")}
            {dialogue_row("A Tiên (阿仙)", "#f59e0b", "阿薇，你好！很高兴认识你。", "Ā Wēi, nǐ hǎo! Hěn gāoxìng rènshi nǐ.", "Chào A Vy! Rất vui được quen biết bạn.")}
            {dialogue_row("A Vy (阿薇)", "#10b981", "你好，阿仙！我也很高兴认识你。你是学生吗？", "Nǐ hǎo, Ā Xiān! Wǒ yě ... gāoxìng rènshi nǐ. Nǐ shì xuéshēng ma?", "Chào A Tiên! Tôi cũng rất vui được quen biết bạn. Bạn là học sinh à?")}
            {dialogue_row("A Tiên (阿仙)", "#f59e0b", "不是，我不是学生。我是律师。", "Bú ... wǒ bú ... xuéshēng. Wǒ shì lǜshī.", "Không phải, tôi không phải học sinh. Tôi là luật sư.")}
            {dialogue_row("A Vy (阿薇)", "#10b981", "太好了！你有男朋友吗？", "Tài hǎo le! Nǐ yǒu nánpéngyou ma?", "Tuyệt vời quá! Bạn có bạn trai chưa?")}
            {dialogue_row("A Tiên (阿仙)", "#f59e0b", "我没有男朋友。你呢？", "Wǒ méiyǒu nánpéngyou. Nǐ ne?", "Tôi không có bạn trai. Còn bạn?")}
            {dialogue_row("A Vy (阿薇)", "#10b981", "我也没有。阿青，你呢？你有女朋友吗？", "Wǒ yě ... Ā Qīng, nǐ ne? Nǐ yǒu nǚpéngyou ma?", "Tôi cũng không có. A Thanh, còn bạn? Bạn có bạn gái chưa?")}
            {dialogue_row("A Thanh (阿青)", "#2563eb", "我有。她叫青，她很好。", "Wǒ yǒu. Tā jiào Qīng, tā hěn hǎo.", "Tôi có rồi. Cô ấy tên là Thanh, cô ấy tốt lắm.")}
            {dialogue_row("A Trân (阿珍)", "#8b5cf6", "好了好了，你们累吗？你们饿吗？", "Hǎo le hǎo le, nǐmen lèi ma? Nǐmen è ma?", "Được rồi được rồi, các bạn có mệt không? Có đói không?")}
            {dialogue_row("A Vy (阿薇)", "#10b981", "我不累，但我很饿。", "Wǒ bú lèi, dàn wǒ hěn è.", "Tôi không mệt, nhưng tôi rất đói rồi.")}
            {dialogue_row("A Tiên (阿仙)", "#f59e0b", "我也很饿。我们吃什么？", "Wǒ yě hěn è. Wǒmen chī shénme?", "Tôi cũng rất đói. Chúng ta ăn gì đây?")}
            {dialogue_row("A Thanh (阿青)", "#2563eb", "吃鸡还是吃鱼？", "Chī jī hái shì chī yú?", "Ăn thịt gà hay ăn cá đây?")}
            {dialogue_row("A Trân (阿珍)", "#8b5cf6", "吃鱼吧！鱼很好。", "Chī yú ba! Yú hěn hǎo.", "Ăn cá đi! Cá ngon lắm đấy.")}
            {dialogue_row("A Tiên (阿仙)", "#f59e0b", "好！去吃鱼吧！", "Hǎo! Qù chī yú ba!", "Được! Đi ăn cá thôi nào!")}
            {dialogue_row("A Vy (阿薇)", "#10b981", "去吧！", "Qù ba!", "Đi thôi!")}
        </div>
        """, unsafe_allow_html=True)
