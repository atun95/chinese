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
    st.subheader("3. Biến điệu của '不' (bù)")
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

def show_lesson3_hanzi():
    render_lesson_intro("🔒 Bài 3: Nét chữ Hán cơ bản", "Rèn nét cơ bản và quy tắc thứ tự nét.")
    st.table(NET_CO_BAN)
