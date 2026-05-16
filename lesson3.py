import streamlit as st
from lessons_data import *
from ui_utils import *

def show_lesson3_pinyin():
    render_lesson_intro("🔒 Bài 3: Thanh mẫu nâng cao & Biến điệu", "Học các thanh mẫu khó (Âm mặt lưỡi, đầu lưỡi) và quy tắc biến điệu của 不.")
    for g in B2_THANH_MAU_DATA:
        st.markdown(f"#### {g['ten']}")
        cols = st.columns(4)
        for i, item in enumerate(g["items"]):
            with cols[i%4]: render_pronunciation_card(item, "b3_tm")
    
    st.markdown("---")
    st.info("""
    📌 **Mối liên quan giữa cặp y-i và w-u**

    **y** và **w** không phải là thanh mẫu thực sự. Chúng là ký hiệu viết xuất hiện khi vận mẫu bắt đầu bằng **i** hoặc **u** mà đứng một mình (không có thanh mẫu đi trước):

    - i → **y**: yī (一: số 1), yě (也: cũng), yuè (月: trăng)
    - u → **w**: wǔ (五: số 5), wǒ (我: tôi), wén (文: văn)

    🔑 y và w là "áo khoác" của i và u khi chúng đứng đầu âm tiết. Phát âm hoàn toàn giống nhau!
    """)
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
    **Cấu trúc:** Chủ ngữ + **是** + Danh từ

    - ✅ Dùng với **danh từ**: Wǒ shì xuéshēng. (Tôi là học sinh.)
    - ❌ **Không** dùng với tính từ: ~~Wǒ shì máng~~ → Phải dùng **很**: Wǒ hěn máng.
    """)

    col_shi1, col_shi2 = st.columns(2)
    with col_shi1:
        st.success("**Câu khẳng định (是):**")
        st.write("- Wǒ shì xuéshēng. (我是学生: Tôi là học sinh.)")
        st.write("- Nǐ shì lǎoshī. (你是老师: Bạn là giáo viên.)")
        st.write("- Tā shì wǒ māma. (她是我妈妈: Cô ấy là mẹ tôi.)")
    with col_shi2:
        st.error("**Câu phủ định (不是 → bú shì):**")
        st.write("- Wǒ bú shì lǎoshī. (我不是老师: Tôi không phải giáo viên.)")
        st.write("- Tā bú shì xuéshēng. (他不是学生: Anh ấy không phải học sinh.)")

    st.warning("**Câu hỏi (是...吗?):**")
    st.write("- Nǐ shì xuéshēng **ma**? (你是学生吗？: Bạn có phải học sinh không?)")
    st.write("  → Trả lời đúng: **Shì de**, wǒ shì xuéshēng. (是的，我是学生。)")
    st.write("  → Trả lời sai: **Bú shì**, wǒ shì lǎoshī. (不是，我是老师。)")

    with st.expander("💬 Hội thoại mẫu", expanded=False):
        st.code("""
A: 你好！你是老师吗？
   Nǐ hǎo! Nǐ shì lǎoshī ma?
   (Xin chào! Bạn có phải giáo viên không?)

B: 不是，我是学生。你呢？
   Bú shì, wǒ shì xuéshēng. Nǐ ne?
   (Không phải, tôi là học sinh. Còn bạn?)

A: 我是老师。很高兴认识你！
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
    st.write("- bù shì → **bú shì** (不是: không phải)")
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
        st.write("- Tā **bú shì** lǎoshī. (他不是老师: Anh ấy không phải thầy giáo.)")
        st.write("- Wǒ **bù máng**. (我不忙: Tôi không bận.)")
        st.write("- Nǐ hǎo **bù hǎo**? (你好不好: Bạn khỏe không?)")
        st.write("- Chī **bù chī**? (吃不吃: Ăn không?)")

def show_lesson3_pinyin_rules():
    render_lesson_intro("🔒 Bài 3: Quy tắc viết Pinyin", "Nắm vững các quy tắc biến đổi chữ viết của i, u, ü trong bính âm.")
    
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
    
    tab1, tab2, tab3 = st.tabs(["Quy tắc của i", "Quy tắc của u", "Quy tắc của ü"])
    with tab1:
        st.markdown("**i → thêm y** (*Nhớ: i đầu câu → đổi thành y*)")
        st.write("- **i** → **yi** (yī 一)")
        st.write("- **ia** → **ya** (yā 压)")
        st.write("- **iao** → **yao** (yào 要)")
        st.write("- **ie** → **ye** (yě 也)")
        st.write("- **iu** → **you** (yǒu 有)")
        st.write("- **ian** → **yan** (yán 言)")
        st.write("- **in** → **yin** (yīn 音)")
        st.write("- **ing** → **ying** (yīng 英)")
    with tab2:
        st.markdown("**u → thêm w** (*Nhớ: u đầu câu → đổi thành w*)")
        st.write("- **u** → **wu** (wú 五)")
        st.write("- **ua** → **wa** (wá 娃)")
        st.write("- **uo** → **wo** (wǒ 我)")
        st.write("- **uai** → **wai** (wài 外)")
        st.write("- **ui** → **wei** (wèi 为)")
        st.write("- **uan** → **wan** (wán 完)")
        st.write("- **un** → **wen** (wén 文)")
    with tab3:
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
