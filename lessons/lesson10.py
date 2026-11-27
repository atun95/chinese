import streamlit as st
from ui_utils import render_lesson_intro


def show_lesson10_1_ba():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');

    .b101-hero {
        background: linear-gradient(145deg, #fffbeb, #fef3c7);
        border: 2px solid #fcd34d;
        border-radius: 18px;
        padding: 28px 24px;
        text-align: center;
        box-shadow: 0 8px 28px rgba(0,0,0,0.06);
        margin-bottom: 8px;
    }
    .b101-char { font-size: 5rem; font-weight: 900; color: #b45309; line-height: 1; }
    .b101-py { font-family: monospace; font-size: 1.6rem; font-weight: 800; color: #92400e; margin-top: 6px; }
    .b101-tag {
        display: inline-block;
        margin-top: 10px;
        background: #fcd34d;
        color: #78350f;
        font-weight: 800;
        padding: 4px 14px;
        border-radius: 999px;
    }

    .b101-rule {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 18px 20px;
        margin-bottom: 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    .b101-rule h4 { margin: 0 0 6px 0; }
    .b101-desc { color: #334155; font-size: 0.95rem; line-height: 1.6; margin: 0 0 12px 0; }
    .b101-formula {
        background: #1e293b;
        border-radius: 10px;
        padding: 12px 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        gap: 6px;
        margin-bottom: 12px;
    }
    .b101-table { width: 100%; border-collapse: collapse; font-size: 0.92rem; }
    .b101-table th { text-align: left; padding: 8px 10px; font-weight: 800; }
    .b101-table td { padding: 8px 10px; border-top: 1px solid #e2e8f0; vertical-align: top; }
    .b101-han { font-size: 1.12rem; font-weight: 800; color: #0f172a; }
    .b101-py2 { font-family: monospace; font-weight: 700; }
    .b101-vi { font-style: italic; color: #475569; }
    .b101-note { color: #64748b; font-size: 0.85rem; }

    .b101-pair {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 18px 20px;
        margin-bottom: 14px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }
    .b101-pair-title { font-weight: 800; color: #0f172a; margin-bottom: 10px; }
    .b101-line { border-radius: 10px; padding: 10px 14px; margin-bottom: 8px; }
    .b101-line .han { font-size: 1.2rem; font-weight: 800; color: #0f172a; }
    .b101-line .meta { font-size: 0.88rem; color: #64748b; }

    .b101-dlg {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 18px 20px;
        margin-top: 8px;
    }
    .b101-turn { margin-bottom: 12px; }
    .b101-who {
        display: inline-block;
        font-weight: 800;
        font-size: 0.8rem;
        padding: 2px 8px;
        border-radius: 8px;
        margin-bottom: 4px;
    }
    .b101-who.a { background: #fef3c7; color: #92400e; }
    .b101-who.b { background: #dbeafe; color: #1e3a8a; }

    .b101-tip {
        background: linear-gradient(135deg, #fefce8, #fef9c3);
        border: 2px solid #fde047;
        border-radius: 16px;
        padding: 20px 22px;
        margin-bottom: 14px;
    }
    .b101-trap {
        background: #fff1f2;
        border: 2px solid #fda4af;
        border-radius: 14px;
        padding: 14px 16px;
        margin-bottom: 10px;
    }
    .b101-key {
        background: linear-gradient(135deg, #0f172a, #92400e);
        color: white;
        border-radius: 16px;
        padding: 20px 22px;
        margin-top: 16px;
    }
    .b101-key table { width: 100%; border-collapse: collapse; margin-top: 10px; }
    .b101-key td { padding: 8px 10px; border-top: 1px solid rgba(255,255,255,0.15); vertical-align: top; }
    .b101-bad { color: #be123c; text-decoration: line-through; }
    .b101-ok { color: #166534; font-weight: 700; }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "💬 Bài 28 - Cách dùng 吧 (ba)",
        "吧 đứng cuối câu, thanh nhẹ. Nó không có nghĩa riêng: thêm vào để rủ, chịu, hoặc đoán."
    )

    tab_theory, tab_examples, tab_tips, tab_quiz = st.tabs([
        "📚 Lý thuyết",
        "📝 Ví dụ đối chiếu",
        "⚠️ Lưu ý & Mẹo nhớ",
        "🎮 Luyện tập"
    ])

    cases = [
        {
            "color": "#d97706",
            "bg": "#fffbeb",
            "title": "1. Rủ, đề nghị",
            "desc": "Người nói đưa ra một việc và mời người kia cùng làm, hoặc khuyên người kia làm. Giọng mềm hơn câu ra lệnh trần.",
            "formula": [
                ("Câu", "#fbbf24"),
                ("+", "#94a3b8"),
                ("吧", "#fbbf24", True),
                ("。", "#e2e8f0"),
            ],
            "rows": [
                ("我们去吃饭吧。", "Wǒmen qù chīfàn ba.", "Mình đi ăn thôi.", "Rủ cùng đi"),
                ("你喝茶吧。", "Nǐ hē chá ba.", "Bạn uống trà đi.", "Khuyên một người"),
                ("我们一起去吧。", "Wǒmen yìqǐ qù ba.", "Chúng ta cùng đi nhé.", "Rủ, có 一起"),
                ("我们买橘子吧。", "Wǒmen mǎi júzi ba.", "Mình mua quýt đi.", "Đề nghị lựa chọn"),
            ],
        },
        {
            "color": "#ea580c",
            "bg": "#fff7ed",
            "title": "2. Thương lượng",
            "desc": "Dùng khi trả giá hoặc chốt một cách làm. 吧 biến con số, cách trả tiền thành một lời đề nghị, không phải câu thông báo.",
            "formula": [
                ("Ý đề nghị", "#fdba74"),
                ("+", "#94a3b8"),
                ("吧", "#fdba74", True),
                ("。", "#e2e8f0"),
            ],
            "rows": [
                ("太贵了，三块五吧。", "Tài guì le, sān kuài wǔ ba.", "Đắt quá, ba đồng rưỡi nhé.", "Chào giá"),
                ("买两个吧。", "Mǎi liǎng gè ba.", "Lấy hai cái đi.", "Chốt số lượng"),
                ("我们三个人一起给吧。", "Wǒmen sān gè rén yìqǐ gěi ba.", "Ba người mình trả cùng đi.", "Đề nghị cách trả"),
            ],
        },
        {
            "color": "#15803d",
            "bg": "#f0fdf4",
            "title": "3. Đồng ý, chấp nhận",
            "desc": "Câu rất ngắn. Người nói nhận lời, thường là nhận cho xong việc, không nhiệt tình bằng 好的.",
            "formula": [
                ("好", "#86efac"),
                ("+", "#94a3b8"),
                ("吧", "#86efac", True),
                ("。", "#e2e8f0"),
            ],
            "rows": [
                ("好吧。", "Hǎo ba.", "Thôi được. / Được rồi.", "Chịu, hơi miễn cưỡng"),
                ("那好吧。", "Nà hǎo ba.", "Thế thì được.", "Nhận sau khi đã nghe đề nghị"),
                ("行吧。", "Xíng ba.", "Cũng được.", "行 = được, ổn"),
            ],
        },
        {
            "color": "#1d4ed8",
            "bg": "#eff6ff",
            "title": "4. Đoán, xin xác nhận",
            "desc": "Người nói đã có một đoán và khá chắc. 吧？ xin người kia gật hoặc lắc. Đây là câu hỏi, nhưng không phải câu hỏi mở.",
            "formula": [
                ("Câu trần thuật", "#93c5fd"),
                ("+", "#94a3b8"),
                ("吧？", "#93c5fd", True),
            ],
            "rows": [
                ("你是老师吧？", "Nǐ shì lǎoshī ba?", "Bạn là giáo viên phải không?", "Đoán nghề"),
                ("他是中国人吧？", "Tā shì Zhōngguó rén ba?", "Anh ấy là người Trung Quốc đúng không?", "Đoán quốc tịch"),
                ("你是越南人吧？", "Nǐ shì Yuènán rén ba?", "Bạn là người Việt Nam phải không?", "Đoán quốc tịch"),
            ],
        },
    ]

    with tab_theory:
        st.markdown("""
        <div class="b101-hero">
            <div class="b101-char">吧</div>
            <div class="b101-py">ba · thanh nhẹ</div>
            <div class="b101-tag">Trợ từ cuối câu</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br/>", unsafe_allow_html=True)
       
        for case in cases:
            spans = ""
            for part in case["formula"]:
                text, color = part[0], part[1]
                big = len(part) > 2 and part[2]
                size = "2rem" if big else "1.05rem"
                spans += (
                    f'<span style="color:{color};font-size:{size};font-weight:800;margin:0 4px;">{text}</span>'
                )
            rows = ""
            for han, py, vi, note in case["rows"]:
                rows += f"""
                <tr>
                    <td class="b101-han">{han}</td>
                    <td class="b101-py2" style="color:{case['color']};">{py}</td>
                    <td class="b101-vi">{vi}</td>
                    <td class="b101-note">{note}</td>
                </tr>"""
            st.markdown(f"""
            <div class="b101-rule" style="border-left:5px solid {case['color']};background:{case['bg']};">
                <h4 style="color:{case['color']};">{case['title']}</h4>
                <p class="b101-desc">{case['desc']}</p>
                <div class="b101-formula">{spans}</div>
                <table class="b101-table">
                    <thead>
                        <tr style="color:{case['color']};">
                            <th>Chữ Hán</th><th>Pinyin</th><th>Nghĩa</th><th>Vì sao có 吧</th>
                        </tr>
                    </thead>
                    <tbody>{rows}</tbody>
                </table>
            </div>
            """, unsafe_allow_html=True)

    with tab_examples:
        st.markdown("### Ba câu cùng một việc, ba giọng khác nhau")
        st.markdown("""
        <div class="b101-pair">
            <div class="b101-pair-title">Đi ăn cơm</div>
            <div class="b101-line" style="background:#f8fafc;border-left:4px solid #64748b;">
                <div class="han">我们去吃饭。</div>
                <div class="meta">Wǒmen qù chīfàn. — Chúng tôi đi ăn. <b>Kể một việc.</b></div>
            </div>
            <div class="b101-line" style="background:#fffbeb;border-left:4px solid #d97706;">
                <div class="han">我们去吃饭吧。</div>
                <div class="meta">Wǒmen qù chīfàn ba. — Mình đi ăn thôi. <b>Rủ.</b></div>
            </div>
            <div class="b101-line" style="background:#eff6ff;border-left:4px solid #1d4ed8;">
                <div class="han">我们去吃饭吗？</div>
                <div class="meta">Wǒmen qù chīfàn ma? — Chúng ta đi ăn không? <b>Hỏi, chưa quyết.</b></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 吗 hỏi vì chưa biết · 吧 hỏi vì đã đoán")
        st.markdown("""
        <div class="b101-pair">
            <div class="b101-pair-title">Bạn có phải học sinh không?</div>
            <div class="b101-line" style="background:#eff6ff;border-left:4px solid #1d4ed8;">
                <div class="han">你是学生吗？</div>
                <div class="meta">Nǐ shì xuéshēng ma? — Chưa có đoán. Câu trả lời có thể là 是 hoặc 不是.</div>
            </div>
            <div class="b101-line" style="background:#fffbeb;border-left:4px solid #d97706;">
                <div class="han">你是学生吧？</div>
                <div class="meta">Nǐ shì xuéshēng ba? — Người nói nghĩ “chắc là học sinh”, chỉ xin xác nhận.</div>
            </div>
        </div>
        <div class="b101-pair">
            <div class="b101-pair-title">Nhận lời</div>
            <div class="b101-line" style="background:#f0fdf4;border-left:4px solid #15803d;">
                <div class="han">好的。</div>
                <div class="meta">Hǎo de. — Được, đồng ý rõ và vui vẻ.</div>
            </div>
            <div class="b101-line" style="background:#fffbeb;border-left:4px solid #d97706;">
                <div class="han">好吧。</div>
                <div class="meta">Hǎo ba. — Thôi được. Đồng ý, nhưng giọng chịu hơn là vui.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Hội thoại ngắn — ở quán")
        st.caption("Ba cách dùng 吧 trong một đoạn: đoán, chào giá, rồi rủ.")
        st.markdown("""
        <div class="b101-dlg">
            <div class="b101-turn">
                <div class="b101-who a">A</div>
                <div class="han" style="font-size:1.15rem;font-weight:800;">你是中国人吧？</div>
                <div class="meta" style="color:#64748b;">Nǐ shì Zhōngguó rén ba? — Bạn là người Trung Quốc phải không?</div>
            </div>
            <div class="b101-turn">
                <div class="b101-who b">B</div>
                <div class="han" style="font-size:1.15rem;font-weight:800;">不是，我是越南人。</div>
                <div class="meta" style="color:#64748b;">Bú shì, wǒ shì Yuènán rén. — Không, tôi là người Việt Nam.</div>
            </div>
            <div class="b101-turn">
                <div class="b101-who a">A</div>
                <div class="han" style="font-size:1.15rem;font-weight:800;">苹果太贵了，三块五吧。</div>
                <div class="meta" style="color:#64748b;">Píngguǒ tài guì le, sān kuài wǔ ba. — Táo đắt quá, ba đồng rưỡi nhé.</div>
            </div>
            <div class="b101-turn">
                <div class="b101-who b">B</div>
                <div class="han" style="font-size:1.15rem;font-weight:800;">好吧。我们买橘子吧。</div>
                <div class="meta" style="color:#64748b;">Hǎo ba. Wǒmen mǎi júzi ba. — Thôi được. Mình mua quýt đi.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_tips:
        st.markdown("""
        <div class="b101-tip">
            <div style="font-weight:800;font-size:1.05rem;color:#713f12;margin-bottom:8px;">Một câu để nhớ</div>
            <div style="font-size:1.15rem;font-weight:800;color:#0f172a;">Muốn rủ → thêm 吧。 &nbsp;·&nbsp; Chưa biết → hỏi bằng 吗？ &nbsp;·&nbsp; Đã đoán → hỏi bằng 吧？</div>
        </div>
        """, unsafe_allow_html=True)

        traps = [
            (
                "吧 đọc thanh nhẹ",
                "Viết <b>ba</b>, không dấu. Không đọc bā, bá hay bà. Trong câu, 吧 không nhấn.",
            ),
            (
                "吧 đứng cuối câu",
                "我们<b>吧</b>去吃饭 là sai. Đúng: <b>我们去吃饭吧。</b>",
            ),
            (
                "Câu đã có từ để hỏi thì không thêm 吧",
                "什么, 谁, 哪儿, 几, 多少 đã biến câu thành câu hỏi. <span class='b101-bad'>你去哪儿吧？</span> &nbsp; <span class='b101-ok'>你去哪儿？</span>",
            ),
            (
                "吧 và 吗 không thay nhau",
                "你是学生<b>吗</b>？ = tôi chưa biết. 你是学生<b>吧</b>？ = tôi đoán bạn là học sinh.",
            ),
            (
                "吧 không phải 把",
                "吧 (ba) là trợ từ cuối câu, bộ 口. 把 (bǎ) là chữ khác, chưa học ở bài này.",
            ),
        ]
        for title, body in traps:
            st.markdown(f"""
            <div class="b101-trap">
                <div style="font-weight:800;color:#9f1239;margin-bottom:4px;">⚠️ {title}</div>
                <div style="color:#334155;line-height:1.55;">{body}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class="b101-key">
            <div style="font-weight:800;font-size:1.05rem;">Bảng chọn nhanh</div>
            <table>
                <tr><td style="width:34%;font-weight:700;">Việc người nói muốn</td><td>Câu</td></tr>
                <tr><td>Kể một việc</td><td>我们去吃饭。</td></tr>
                <tr><td>Rủ, khuyên, chào giá</td><td>我们去吃饭吧。 / 三块五吧。</td></tr>
                <tr><td>Chịu, nhận lời</td><td>好吧。</td></tr>
                <tr><td>Hỏi vì chưa biết</td><td>你是学生吗？</td></tr>
                <tr><td>Hỏi vì đã đoán</td><td>你是学生吧？</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    with tab_quiz:
        st.markdown("Chọn câu hoặc chữ đúng. Nộp bài để xem giải thích.")
        quiz_data = [
            {
                "q": "Muốn rủ: “Mình đi ăn thôi.”",
                "options": ["我们去吃饭。", "我们去吃饭吧。", "我们去吃饭吗？"],
                "answer": "我们去吃饭吧。",
                "explain": "Rủ thì thêm 吧. Câu không có 吧 chỉ kể việc. Câu có 吗 là đang hỏi."
            },
            {
                "q": "Chưa biết người kia có phải học sinh không. Hỏi thế nào?",
                "options": ["你是学生吧？", "你是学生吗？", "你是学生。"],
                "answer": "你是学生吗？",
                "explain": "Chưa có đoán thì dùng 吗. 吧？ chỉ dùng khi người nói đã nghĩ sẵn đáp án."
            },
            {
                "q": "Nhìn cách ăn mặc, bạn đoán anh ấy là giáo viên và muốn xin xác nhận.",
                "options": ["他是老师吗？", "他是老师吧？", "他是老师。"],
                "answer": "他是老师吧？",
                "explain": "Đã đoán khá chắc → câu trần thuật + 吧？"
            },
            {
                "q": "Táo đắt. Bạn muốn trả ba đồng rưỡi.",
                "options": ["太贵了，三块五。", "太贵了，三块五吧。", "太贵了，三块五吗？"],
                "answer": "太贵了，三块五吧。",
                "explain": "Chào giá là một lời thương lượng, thêm 吧."
            },
            {
                "q": "Bạn nhận lời, nhưng giọng hơi miễn cưỡng: “Thôi được.”",
                "options": ["好的。", "好吧。", "好吗？"],
                "answer": "好吧。",
                "explain": "好吧 là chịu, nhận cho xong. 好的 vui và dứt khoát hơn. 好吗 là đang hỏi lại."
            },
            {
                "q": "Điền vào chỗ trống: 苹果太贵了。我们买橘子___。",
                "options": ["吧", "吗", "的"],
                "answer": "吧",
                "explain": "我们买橘子吧 = mình mua quýt đi. Đây là lời rủ sau khi chê táo đắt."
            },
            {
                "q": "Điền vào chỗ trống: 你去哪儿___？",
                "options": ["吧", "吗", "Không thêm gì"],
                "answer": "Không thêm gì",
                "explain": "哪儿 đã là từ để hỏi. Câu đúng là 你去哪儿？ Không thêm 吧, cũng không thêm 吗."
            },
            {
                "q": "Câu nào là lời khuyên “Bạn uống trà đi”?",
                "options": ["你喝茶。", "你喝茶吧。", "你喝茶吗？"],
                "answer": "你喝茶吧。",
                "explain": "Khuyên, rủ một người làm việc gì → động từ + 吧."
            },
        ]

        if "b101_submitted" not in st.session_state:
            st.session_state.b101_submitted = False
        if "b101_answers" not in st.session_state:
            st.session_state.b101_answers = {}

        for i, q in enumerate(quiz_data):
            st.markdown(f"""
            <div style="background:white;border:1px solid #e2e8f0;border-radius:14px;padding:18px 22px;margin-bottom:4px;">
                <div style="font-size:1.15rem;font-weight:800;color:#0f172a;">Câu {i+1}. {q['q']}</div>
            </div>
            """, unsafe_allow_html=True)
            key = f"b101_a{i}"
            st.radio(
                f"Chọn đáp án câu {i+1}:",
                q["options"],
                key=key,
                horizontal=True,
                disabled=st.session_state.b101_submitted,
                label_visibility="collapsed",
            )
            if st.session_state.b101_submitted:
                user_ans = st.session_state.b101_answers.get(key)
                if user_ans == q["answer"]:
                    st.success(f"Đúng. {q['explain']}")
                else:
                    st.error(f"Đáp án đúng: **{q['answer']}**. {q['explain']}")
            st.markdown("<br/>", unsafe_allow_html=True)

        col_submit, col_reset = st.columns([1, 1])
        with col_submit:
            if not st.session_state.b101_submitted:
                if st.button("Nộp bài", use_container_width=True, key="b101_submit", type="primary"):
                    st.session_state.b101_answers = {
                        f"b101_a{i}": st.session_state.get(f"b101_a{i}") for i in range(len(quiz_data))
                    }
                    st.session_state.b101_submitted = True
                    st.rerun()
        with col_reset:
            if st.session_state.b101_submitted:
                if st.button("Làm lại", use_container_width=True, key="b101_reset"):
                    st.session_state.b101_submitted = False
                    st.session_state.b101_answers = {}
                    for i in range(len(quiz_data)):
                        key = f"b101_a{i}"
                        if key in st.session_state:
                            del st.session_state[key]
                    st.rerun()

        if st.session_state.b101_submitted:
            correct = sum(
                1 for i, q in enumerate(quiz_data)
                if st.session_state.b101_answers.get(f"b101_a{i}") == q["answer"]
            )
            total = len(quiz_data)
            pct = int(correct / total * 100)
            if pct == 100:
                msg = "Đủ bốn cách dùng 吧."
            elif pct >= 70:
                msg = "Xem lại các câu sai, nhất là chỗ 吧 khác 吗."
            else:
                msg = "Đọc lại phần Lý thuyết rồi làm lại."
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#1e3a8a,#b45309);color:white;border-radius:16px;padding:28px;text-align:center;margin-top:12px;">
                <div style="font-size:3.2rem;font-weight:900;">{correct}/{total}</div>
                <div>{pct}% đúng</div>
                <div style="margin-top:8px;font-weight:700;">{msg}</div>
            </div>
            """, unsafe_allow_html=True)


def show_lesson10_2_constituents():
    st.markdown("""
    <style>
    .b102-stack { display: flex; flex-direction: column; align-items: center; gap: 10px; margin-bottom: 8px; }
    .b102-rung { border-radius: 16px; padding: 16px 18px; border: 2px solid; box-sizing: border-box; }
    .b102-rung h3 { margin: 0 0 4px 0; }
    .b102-rung .sub { margin: 0 0 8px 0; color: #334155; line-height: 1.5; }
    .b102-w1 { width: 100%; background: #dbeafe; border-color: #2563eb; }
    .b102-w2 { width: 93%; background: #ecfdf5; border-color: #059669; }
    .b102-w3 { width: 86%; background: #fef3c7; border-color: #d97706; }
    .b102-w4 { width: 79%; background: #fdf2f8; border-color: #db2777; }
    .b102-w5 { width: 72%; background: #f3e8ff; border-color: #9333ea; }
    .b102-arrow { color: #94a3b8; font-weight: 800; font-size: 0.85rem; }
    .b102-ex { font-size: 1.35rem; font-weight: 900; color: #0f172a; }
    .b102-py { font-family: monospace; color: #c2410c; font-weight: 700; }
    .b102-vi { color: #475569; font-style: italic; }
    .b102-chip { display: inline-block; margin: 4px 6px 0 0; padding: 4px 8px; border-radius: 8px; font-weight: 800; background: rgba(255,255,255,.75); border: 1px solid rgba(15,23,42,.08); }
    .b102-card { background: #fff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 16px 18px; margin-bottom: 12px; }
    .b102-card h4 { margin: 0 0 6px 0; }
    .b102-num { display: inline-block; background: #0f172a; color: #fff; border-radius: 8px; padding: 2px 8px; margin-right: 8px; font-size: 0.85rem; }
    .b102-han { font-size: 1.2rem; font-weight: 800; color: #0f172a; }
    .b102-sent { display: flex; flex-wrap: wrap; gap: 8px; margin: 10px 0; }
    .b102-tok { border-radius: 10px; padding: 8px 10px; min-width: 72px; }
    .b102-tok .hz { font-size: 1.25rem; font-weight: 900; }
    .b102-tok .role { font-size: 0.75rem; font-weight: 800; }
    .b102-formula { background: #0f172a; color: #fff; border-radius: 12px; padding: 14px 16px; font-weight: 700; line-height: 1.7; margin-bottom: 12px; }
    .b102-map { width: 100%; border-collapse: collapse; font-size: 0.95rem; }
    .b102-map th, .b102-map td { text-align: left; padding: 8px 10px; border-top: 1px solid #e2e8f0; vertical-align: top; }
    .b102-map th { color: #64748b; font-size: 0.78rem; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "🧩 Bài 21 - Các loại từ",
        "Câu bắt đầu bằng chủ ngữ và vị ngữ. Các phần còn lại gắn dần vào hai phần này, càng xuống càng nhỏ."
    )

    tab_map, tab_parts, tab_words, tab_quiz = st.tabs([
        "Các loại từ",
        "📘 Thành phần câu",
        "🔤 Phó từ",
        "🎮 Luyện tập",
    ])

    with tab_map:
        st.markdown("""
        <div class="b102-stack">
          <div class="b102-rung b102-w1">
            <h3>1 · 主语 (zhǔyǔ) - chủ ngữ + 谓语 (wèiyǔ) - vị ngữ</h3>
            <div class="b102-ex">老师 / 来了。</div>
            <div class="b102-py">Lǎoshī / lái le.</div>
            <div class="b102-vi">老师 là chủ ngữ, 来了 là vị ngữ. (Thầy giáo đến rồi)</div>
          </div>
          <div class="b102-rung b102-w2">
            <h3>2 · 宾语 (bīnyǔ) - tân ngữ</h3>
            <div class="b102-ex">老师 / 喜欢 / 菜。</div>
            <div class="b102-py">Lǎoshī / xǐhuan / cài.</div>
            <div class="b102-vi">老师 là chủ ngữ, 喜欢 là vị ngữ, 菜 là tân ngữ đứng sau động từ. (Thầy giáo thích món ăn)</div>
          </div>
          <div class="b102-rung b102-w3">
            <h3>3 · 状语 (zhuàngyǔ) - trạng ngữ · 补语 (bǔyǔ) - bổ ngữ</h3>
            <div class="b102-ex">老师 / 很 / 喜欢 / 菜。</div>
            <div class="b102-py">Lǎoshī / hěn / xǐhuan / cài.</div>
            <div class="b102-vi">很 là trạng ngữ (đứng trước vị ngữ 喜欢).</div>
            <div class="b102-ex" style="margin-top:10px;">他 / 说 / 得 / 很好。</div>
            <div class="b102-py">Tā / shuō / de / hěn hǎo.</div>
            <div class="b102-vi">很好 là bổ ngữ (đứng sau vị ngữ 说 qua 得).</div>
          </div>
          <div class="b102-rung b102-w4">
            <h3>4 · 定语 (dìngyǔ) - định ngữ</h3>
            <div class="b102-ex">我的 / 老师 / 很 / 喜欢 / 中国 / 菜。</div>
            <div class="b102-py">Wǒ de / lǎoshī / hěn / xǐhuan / Zhōngguó / cài.</div>
            <div class="b102-vi">我的 là định ngữ bổ nghĩa cho 老师, 中国 là định ngữ bổ nghĩa cho 菜. (Thầy giáo của tôi rất thích món ăn Trung Quốc)</div>
          </div>
          <div class="b102-rung b102-w5">
            <h3>5 · 副词 (fùcí) - phó từ</h3>
            <div class="b102-ex">他 / 不 / 吃 / 米饭。</div>
            <div class="b102-py">Tā / bù / chī / mǐfàn.</div>
            <div class="b102-vi">不 là phó từ (đứng trước động từ 吃, làm trạng ngữ).</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_parts:
        st.markdown("""
        <div class="b102-card">
          <h4><span class="b102-num">1</span>主语 và 谓语 (Chủ ngữ & Vị ngữ)</h4>
          <div class="b102-han">老师来了。</div>
          <div class="b102-py">Lǎoshī lái le.</div>
          <div class="b102-vi">Thầy giáo đến rồi. (老师 là chủ ngữ, 来了 là vị ngữ)</div>
        </div>
        <div class="b102-card">
          <h4><span class="b102-num">2</span>宾语 (bīnyǔ) - Tân ngữ</h4>
          <p><b>Vị trí:</b> Đứng <b>sau động từ vị ngữ</b>, là đối tượng tiếp nhận hoặc chịu tác động của hành động.</p>
          <div class="b102-sent">
            <div class="b102-tok" style="background:#dbeafe;"><div class="role">主语</div><div class="hz">老师</div></div>
            <div class="b102-tok" style="background:#bbf7d0;"><div class="role">谓语</div><div class="hz">喜欢</div></div>
            <div class="b102-tok" style="background:#fecaca;"><div class="role">宾语</div><div class="hz">菜</div></div>
          </div>
          <div class="b102-han">老师喜欢菜。</div>
          <div class="b102-py">Lǎoshī xǐhuan cài.</div>
          <div class="b102-vi">Thầy giáo thích món ăn. (菜 là tân ngữ của 喜欢)</div>
        </div>
        <div class="b102-card">
          <h4><span class="b102-num">3</span>状语 (zhuàngyǔ) - Trạng ngữ</h4>
          <p><b>1. Đứng ở đâu (Cấu trúc)?</b>
            <br>• Luôn đứng <b>trước Vị ngữ</b> (Động từ / Tính từ):
            <br><code style="background:#f1f5f9;padding:3px 8px;border-radius:6px;font-weight:700;color:#0f172a;">Chủ ngữ + [ Trạng ngữ ] + Vị ngữ (Động từ / Tính từ) + Tân ngữ</code>
            <br>• <i>Trạng ngữ chỉ thời gian / địa điểm cũng có thể đứng ở đầu câu (trước Chủ ngữ).</i>
          </p>
          <p><b>2. Thường là loại từ gì?</b>
            <br>• <b>Phó từ</b> (mức độ, phủ định, phạm vi...): 很, 太, 非常, 不, 没, 也, 都
            <br>• <b>Danh từ / Cụm thời gian, nơi chốn</b>: 今天, 明天, 现在, 在学校, 在家
            <br>• <b>Tính từ / Cụm tính từ</b> (thường có trợ từ 地): 认真地 (chăm chỉ), 慢慢地 (từ từ)
          </p>
          <div class="b102-sent">
            <div class="b102-tok" style="background:#dbeafe;"><div class="role">主语</div><div class="hz">老师</div></div>
            <div class="b102-tok" style="background:#fde68a;"><div class="role">状语</div><div class="hz">很</div></div>
            <div class="b102-tok" style="background:#bbf7d0;"><div class="role">谓语</div><div class="hz">喜欢</div></div>
            <div class="b102-tok" style="background:#fecaca;"><div class="role">宾语</div><div class="hz">菜</div></div>
          </div>
          <div class="b102-han">老师很喜欢菜。</div>
          <div class="b102-py">Lǎoshī hěn xǐhuan cài.</div>
          <div class="b102-vi">很 là trạng ngữ (phó từ) đứng trước vị ngữ 喜欢. (Thầy giáo rất thích món ăn)</div>
        </div>
        <div class="b102-card">
          <h4><span class="b102-num">4</span>补语 (bǔyǔ) - Bổ ngữ</h4>
          <p><b>1. Đứng ở đâu (Cấu trúc)?</b>
            <br>• Luôn đứng <b>ngay sau Vị ngữ</b> (Động từ / Tính từ):
            <br><code style="background:#f1f5f9;padding:3px 8px;border-radius:6px;font-weight:700;color:#0f172a;">Động từ + 得 + [ Bổ ngữ ]</code> <i>(Bổ ngữ trạng thái / trình độ)</i>
            <br><code style="background:#f1f5f9;padding:3px 8px;border-radius:6px;font-weight:700;color:#0f172a;">Động từ + [ Bổ ngữ ]</code> <i>(Bổ ngữ kết quả, số lượng)</i>
          </p>
          <p><b>2. Thường là loại từ gì?</b>
            <br>• <b>Tính từ / Cụm tính từ</b> (đứng sau 得, đánh giá trình độ, mức độ): 好, 快, 很好, 很快 (说得很好 - nói rất hay)
            <br>• <b>Động từ / Tính từ kết quả</b> (đứng sát sau động từ): 懂 (hiểu), 见 (thấy), 完 (xong), 饱 (no) (听懂 - nghe hiểu, 做完 - làm xong)
            <br>• <b>Số từ + Lượng từ</b> (thời lượng, số lần): 一次 (1 lần), 两年 (2 năm) (学了两年 - học hai năm)
          </p>
          <div class="b102-sent">
            <div class="b102-tok" style="background:#dbeafe;"><div class="role">主语</div><div class="hz">他</div></div>
            <div class="b102-tok" style="background:#bbf7d0;"><div class="role">谓语</div><div class="hz">说</div></div>
            <div class="b102-tok" style="background:#fef9c3;"><div class="role">助词</div><div class="hz">得</div></div>
            <div class="b102-tok" style="background:#e9d5ff;"><div class="role">补语</div><div class="hz">很好</div></div>
          </div>
          <div class="b102-han">他说得很好。</div>
          <div class="b102-py">Tā shuō de hěn hǎo.</div>
          <div class="b102-vi">很好 là bổ ngữ (cụm tính từ) đứng sau vị ngữ 说 (qua 得), nói rõ mức độ nói tốt.</div>
        </div>
        <div class="b102-card">
          <h4><span class="b102-num">5</span>定语 (dìngyǔ) - Định ngữ</h4>
          <p><b>1. Đứng ở đâu (Cấu trúc)?</b>
            <br>• Luôn đứng <b>trước Danh từ (Trung tâm ngữ)</b>:
            <br><code style="background:#f1f5f9;padding:3px 8px;border-radius:6px;font-weight:700;color:#0f172a;">[ Định ngữ ] + (的) + Danh từ (Chủ ngữ hoặc Tân ngữ)</code>
            <br>• <i>⚡ Lưu ý: Thứ tự ngược hoàn toàn với tiếng Việt (Tiếng Việt: "Sách của tôi" → Tiếng Trung: "Tôi của sách" 我的书).</i>
          </p>
          <p><b>2. Thường là loại từ gì?</b>
            <br>• <b>Đại từ / Danh từ</b> (sở hữu, phân loại, nguồn gốc): 我的 (của tôi), 老师的 (của thầy cô), 中国 (Trung Quốc)
            <br>• <b>Tính từ / Cụm tính từ</b> (miêu tả đặc điểm, tính chất): 好 (tốt), 漂亮的 (đẹp)
            <br>• <b>Số từ + Lượng từ</b> (chỉ số lượng): 一位 (một vị), 三本 (ba quyển)
          </p>
          <div class="b102-sent">
            <div class="b102-tok" style="background:#fde68a;"><div class="role">定语</div><div class="hz">我的</div></div>
            <div class="b102-tok" style="background:#dbeafe;"><div class="role">主语</div><div class="hz">老师</div></div>
            <div class="b102-tok" style="background:#fde68a;"><div class="role">状语</div><div class="hz">很</div></div>
            <div class="b102-tok" style="background:#bbf7d0;"><div class="role">谓语</div><div class="hz">喜欢</div></div>
            <div class="b102-tok" style="background:#fecaca;"><div class="role">定语</div><div class="hz">中国</div></div>
            <div class="b102-tok" style="background:#fca5a5;"><div class="role">宾语</div><div class="hz">菜</div></div>
          </div>
          <div class="b102-han">我的老师很喜欢中国菜。</div>
          <div class="b102-py">Wǒ de lǎoshī hěn xǐhuan Zhōngguó cài.</div>
          <div class="b102-vi">我的 (định ngữ) bổ nghĩa cho 老师 (chủ ngữ) &nbsp;|&nbsp; 中国 (định ngữ) bổ nghĩa cho 菜 (tân ngữ). (Thầy giáo của tôi rất thích món ăn Trung Quốc)</div>
        </div>

        """, unsafe_allow_html=True)

    with tab_words:
        st.markdown("""
        <div class="b102-card">
          <h4><span class="b102-num">★</span>副词 (fùcí) · Phó từ</h4>
          <p><b>Đặc điểm & Vị trí:</b> Phó từ dùng để bổ nghĩa cho động từ hoặc tính từ. Phó từ <b>luôn đứng trước Động từ / Tính từ</b> và giữ vai trò làm <b>Trạng ngữ</b> trong câu.</p>
          <div class="b102-formula">📌 Cấu trúc: Phó từ + Động từ / Tính từ &nbsp;&nbsp;(Không đứng độc lập làm chủ ngữ hay tân ngữ)</div>
        </div>

        <div class="b102-card">
          <h4 style="color:#2563eb;">1. Phó từ chỉ mức độ (程度副词)</h4>
          <table class="b102-map">
            <tr><th style="width:130px;">Phó từ</th><th>Pinyin & Nghĩa</th><th>Ví dụ</th><th>Dịch nghĩa</th></tr>
            <tr><td><b>很</b></td><td>hěn · rất</td><td><b>很</b>好 / <b>很</b>喜欢</td><td>rất tốt / rất thích</td></tr>
            <tr><td><b>太</b></td><td>tài · quá, lắm</td><td><b>太</b>大 / <b>太</b>累了</td><td>quá to / quá mệt rồi</td></tr>
            <tr><td><b>非常</b></td><td>fēicháng · vô cùng, cực kỳ</td><td><b>非常</b>高兴</td><td>vô cùng vui mừng</td></tr>
            <tr><td><b>最</b></td><td>zuì · nhất</td><td><b>最</b>喜欢 / <b>最</b>大</td><td>thích nhất / to nhất</td></tr>
            <tr><td><b>比较</b></td><td>bǐjiào · khá, tương đối</td><td><b>比较</b>好</td><td>tương đối tốt / khá tốt</td></tr>
            <tr><td><b>真</b></td><td>zhēn · thật là</td><td><b>真</b>好吃</td><td>thật là ngon</td></tr>
          </table>
        </div>

        <div class="b102-card">
          <h4 style="color:#dc2626;">2. Phó từ phủ định (否定副词)</h4>
          <table class="b102-map">
            <tr><th style="width:130px;">Phó từ</th><th>Pinyin & Nghĩa</th><th>Ví dụ</th><th>Dịch nghĩa</th></tr>
            <tr><td><b>不</b></td><td>bù · không (thói quen, hiện tại, tương lai)</td><td><b>不</b>吃 / <b>不</b>去</td><td>không ăn / không đi</td></tr>
            <tr><td><b>没 / 没有</b></td><td>méi / méiyǒu · chưa, không (hành động đã/chưa xảy ra)</td><td><b>没</b>来 / <b>没</b>做</td><td>chưa đến / chưa làm</td></tr>
            <tr><td><b>别</b></td><td>bié · đừng (khuyên ngăn, cấm đoán)</td><td><b>别</b>说 / <b>别</b>走</td><td>đừng nói / đừng đi</td></tr>
          </table>
        </div>

        <div class="b102-card">
          <h4 style="color:#059669;">3. Phó từ chỉ phạm vi (范围副词)</h4>
          <table class="b102-map">
            <tr><th style="width:130px;">Phó từ</th><th>Pinyin & Nghĩa</th><th>Ví dụ</th><th>Dịch nghĩa</th></tr>
            <tr><td><b>都</b></td><td>dōu · đều</td><td>我们<b>都</b>去</td><td>chúng tôi đều đi</td></tr>
            <tr><td><b>只</b></td><td>zhǐ · chỉ</td><td><b>只</b>买一个</td><td>chỉ mua một cái</td></tr>
            <tr><td><b>一共</b></td><td>yígòng · tổng cộng</td><td><b>一共</b>多少钱</td><td>tổng cộng bao nhiêu tiền</td></tr>
            <tr><td><b>一起</b></td><td>yìqǐ · cùng nhau</td><td><b>一起</b>学</td><td>cùng nhau học</td></tr>
          </table>
        </div>

        <div class="b102-card">
          <h4 style="color:#d97706;">4. Phó từ chỉ thời gian & tần suất (时间/频率副词)</h4>
          <table class="b102-map">
            <tr><th style="width:130px;">Phó từ</th><th>Pinyin & Nghĩa</th><th>Ví dụ</th><th>Dịch nghĩa</th></tr>
            <tr><td><b>正在 / 在</b></td><td>zhèngzài / zài · đang</td><td><b>正在</b>看书</td><td>đang đọc sách</td></tr>
            <tr><td><b>已经</b></td><td>yǐjīng · đã (rồi)</td><td><b>已经</b>走了</td><td>đã đi rồi</td></tr>
            <tr><td><b>常常 / 常</b></td><td>chángcháng · thường, thường xuyên</td><td><b>常常</b>去</td><td>thường xuyên đi</td></tr>
            <tr><td><b>又</b></td><td>yòu · lại (hành động lặp lại đã xảy ra)</td><td>他<b>又</b>来了</td><td>anh ấy lại đến rồi</td></tr>
            <tr><td><b>再</b></td><td>zài · lại, nữa (hành động lặp lại chưa xảy ra)</td><td><b>再</b>见 / <b>再</b>吃一个</td><td>hẹn gặp lại / ăn thêm một cái nữa</td></tr>
          </table>
        </div>

        <div class="b102-card">
          <h4 style="color:#7c3aed;">5. Phó từ chỉ ngữ khí & liên kết (语气/关联副词)</h4>
          <table class="b102-map">
            <tr><th style="width:130px;">Phó từ</th><th>Pinyin & Nghĩa</th><th>Ví dụ</th><th>Dịch nghĩa</th></tr>
            <tr><td><b>也</b></td><td>yě · cũng</td><td>我<b>也</b>喜欢</td><td>tôi cũng thích</td></tr>
            <tr><td><b>就</b></td><td>jiù · thì, ngay, liền</td><td>我<b>就</b>去</td><td>tôi đi ngay đây</td></tr>
            <tr><td><b>才</b></td><td>cái · mới (muộn, khó khăn)</td><td>他<b>才</b>来</td><td>anh ấy mới đến</td></tr>
            <tr><td><b>一定</b></td><td>yídìng · nhất định</td><td><b>一定</b>要来</td><td>nhất định phải đến</td></tr>
            <tr><td><b>真的</b></td><td>zhēnde · thật sự</td><td><b>真的</b>很好</td><td>thật sự rất tốt</td></tr>
          </table>
        </div>
        """, unsafe_allow_html=True)

    with tab_quiz:
        quiz = [
            {
                "q": "Phần lớn nhất của câu là cặp nào?",
                "options": ["主语 + 谓语", "定语 + 助词", "副词 + 补语"],
                "answer": "主语 + 谓语",
                "explain": "Khung câu là chủ ngữ và vị ngữ. Các phần khác gắn vào sau."
            },
            {
                "q": "宾语 đứng ở đâu?",
                "options": ["Sau động từ vị ngữ", "Trước chủ ngữ", "Cuối câu, sau 吧"],
                "answer": "Sau động từ vị ngữ",
                "explain": "老师喜欢菜. 菜 là tân ngữ, đứng sau 喜欢."
            },
            {
                "q": "状语 và 补语 nằm thế nào so với vị ngữ?",
                "options": ["Trạng ngữ phía trước, bổ ngữ phía sau", "Cả hai đứng trước chủ ngữ", "Cả hai là tân ngữ"],
                "answer": "Trạng ngữ phía trước, bổ ngữ phía sau",
                "explain": "很喜欢: 很 ở trước. 说得很好: 很好 ở sau."
            },
            {
                "q": "定语 gắn vào tiếng nào?",
                "options": ["Danh từ của chủ ngữ hoặc tân ngữ", "Trợ từ ngữ khí cuối câu", "Chỉ gắn vào phó từ"],
                "answer": "Danh từ của chủ ngữ hoặc tân ngữ",
                "explain": "我的 đứng trước 老师. 中国 đứng trước 菜."
            },
            {
                "q": "Trong 很喜欢, 很 là gì?",
                "options": ["Phó từ, làm trạng ngữ", "Tân ngữ", "Trợ từ ngữ khí"],
                "answer": "Phó từ, làm trạng ngữ",
                "explain": "很 là 副词, ngồi trước vị ngữ 喜欢."
            },
            {
                "q": "的, 地, 得 lần lượt bám vào đâu?",
                "options": ["Định ngữ, trạng ngữ, bổ ngữ", "Chủ ngữ, vị ngữ, tân ngữ", "Cả ba đứng cuối câu"],
                "answer": "Định ngữ, trạng ngữ, bổ ngữ",
                "explain": "我的老师, 慢慢地走, 说得很好."
            },
            {
                "q": "吧 trong 我们去吧 thuộc nhóm nào?",
                "options": ["Trợ từ ngữ khí, cuối câu", "Định ngữ", "Vị ngữ"],
                "answer": "Trợ từ ngữ khí, cuối câu",
                "explain": "吧 cùng nhóm 吗, 呢. Nó đứng ngoài sáu thành phần lớn."
            },
            {
                "q": "Trong 他说得很好, 很好 là gì?",
                "options": ["补语", "主语", "定语"],
                "answer": "补语",
                "explain": "说 là vị ngữ, 得 là trợ từ, 很好 là bổ ngữ."
            },
        ]

        if "b102_submitted" not in st.session_state:
            st.session_state.b102_submitted = False
        if "b102_answers" not in st.session_state:
            st.session_state.b102_answers = {}

        for i, q in enumerate(quiz):
            st.markdown(f"""
            <div style="background:white;border:1px solid #e2e8f0;border-radius:14px;padding:18px 22px;margin-bottom:4px;">
                <div style="font-size:1.05rem;font-weight:800;color:#0f172a;">Câu {i+1}. {q['q']}</div>
            </div>
            """, unsafe_allow_html=True)
            key = f"b102_a{i}"
            st.radio(
                f"Chọn đáp án câu {i+1}:",
                q["options"],
                key=key,
                horizontal=False,
                disabled=st.session_state.b102_submitted,
                label_visibility="collapsed",
            )
            if st.session_state.b102_submitted:
                user_ans = st.session_state.b102_answers.get(key)
                if user_ans == q["answer"]:
                    st.success(f"Đúng. {q['explain']}")
                else:
                    st.error(f"Đáp án đúng: **{q['answer']}**. {q['explain']}")

        c1, c2 = st.columns(2)
        with c1:
            if not st.session_state.b102_submitted:
                if st.button("Nộp bài", use_container_width=True, key="b102_submit", type="primary"):
                    st.session_state.b102_answers = {
                        f"b102_a{i}": st.session_state.get(f"b102_a{i}") for i in range(len(quiz))
                    }
                    st.session_state.b102_submitted = True
                    st.rerun()
        with c2:
            if st.session_state.b102_submitted:
                if st.button("Làm lại", use_container_width=True, key="b102_reset"):
                    st.session_state.b102_submitted = False
                    st.session_state.b102_answers = {}
                    for i in range(len(quiz)):
                        key = f"b102_a{i}"
                        if key in st.session_state:
                            del st.session_state[key]
                    st.rerun()

        if st.session_state.b102_submitted:
            correct = sum(
                1 for i, q in enumerate(quiz)
                if st.session_state.b102_answers.get(f"b102_a{i}") == q["answer"]
            )
            total = len(quiz)
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#1e3a8a,#a16207);color:white;border-radius:16px;padding:28px;text-align:center;margin-top:12px;">
                <div style="font-size:3rem;font-weight:900;">{correct}/{total}</div>
                <div>{int(correct / total * 100)}% đúng</div>
            </div>
            """, unsafe_allow_html=True)


def show_lesson10_3_ne():
    st.markdown("""
    <style>
    .b103-hero {
        background: linear-gradient(135deg, #0f172a, #065f46);
        color: white;
        border-radius: 18px;
        padding: 28px 24px;
        text-align: center;
        margin-bottom: 18px;
    }
    .b103-char { font-size: 4rem; font-weight: 900; line-height: 1; }
    .b103-py { font-size: 1.2rem; opacity: .9; margin-top: 8px; }
    .b103-tag { display: inline-block; margin-top: 10px; background: rgba(255,255,255,.15); border-radius: 999px; padding: 4px 14px; font-size: .85rem; font-weight: 700; }
    .b103-rule {
        background: white;
        border: 2px solid #e2e8f0;
        border-left: 6px solid #059669;
        border-radius: 14px;
        padding: 16px 18px;
        margin-bottom: 14px;
    }
    .b103-rule h4 { margin: 0 0 6px 0; }
    .b103-desc { color: #475569; line-height: 1.6; margin-bottom: 10px; }
    .b103-formula {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: center;
        gap: 6px;
        background: #f8fafc;
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 12px;
    }
    .b103-table { width: 100%; border-collapse: collapse; font-size: .95rem; }
    .b103-table th { text-align: left; color: #64748b; font-size: .78rem; text-transform: uppercase; padding: 6px 8px; border-bottom: 2px solid #e2e8f0; }
    .b103-table td { padding: 8px; border-top: 1px solid #e2e8f0; vertical-align: top; }
    .b103-han { font-size: 1.15rem; font-weight: 800; color: #0f172a; }
    .b103-py2 { font-family: monospace; font-weight: 700; }
    .b103-vi { color: #475569; }
    .b103-note { color: #64748b; font-style: italic; font-size: .88rem; }
    .b103-pair { background: white; border: 1px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; margin-bottom: 12px; }
    .b103-pair-title { font-weight: 800; color: #0f172a; margin-bottom: 8px; }
    .b103-line { border-radius: 10px; padding: 10px 14px; margin-bottom: 8px; }
    .b103-line .han { font-size: 1.25rem; font-weight: 900; color: #0f172a; }
    .b103-line .meta { color: #475569; font-size: .9rem; }
    .b103-dlg { background: white; border: 1px solid #e2e8f0; border-radius: 14px; padding: 16px 18px; }
    .b103-turn { display: flex; gap: 12px; align-items: flex-start; margin-bottom: 12px; }
    .b103-turn:last-child { margin-bottom: 0; }
    .b103-who { width: 34px; height: 34px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 900; color: white; flex-shrink: 0; }
    .b103-who.a { background: #2563eb; }
    .b103-who.b { background: #059669; }
    .b103-tip { background: #fefce8; border: 2px solid #fde047; border-radius: 14px; padding: 16px 18px; margin-bottom: 12px; }
    .b103-trap { background: #fff1f2; border: 2px solid #fda4af; border-radius: 14px; padding: 14px 16px; margin-bottom: 10px; }
    .b103-bad { color: #be123c; text-decoration: line-through; }
    .b103-ok { color: #166534; font-weight: 700; }
    .b103-key { background: linear-gradient(135deg, #0f172a, #064e3b); color: white; border-radius: 16px; padding: 20px 22px; margin-top: 16px; }
    .b103-key table { width: 100%; border-collapse: collapse; margin-top: 10px; }
    .b103-key td { padding: 8px 10px; border-top: 1px solid rgba(255,255,255,0.15); vertical-align: top; }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "💬 Bài 29 - Cách dùng 呢 (ne)",
        "呢 đọc ngang thanh, đứng cuối câu hoặc sau chủ ngữ. Nó hỏi ngược lại, hỏi thân mật, hoặc nhấn mạnh “đang... đấy”."
    )

    tab_theory, tab_examples, tab_tips, tab_quiz = st.tabs([
        "📚 Lý thuyết",
        "📝 Ví dụ đối chiếu",
        "⚠️ Lưu ý & Mẹo nhớ",
        "🎮 Luyện tập"
    ])

    cases = [
        {
            "color": "#059669",
            "bg": "#ecfdf5",
            "title": "1. Hỏi ngược lại — “còn ... thì sao?”",
            "desc": "Khi câu trước đã nêu một người hoặc một việc, 呢？ dùng để hỏi về phần còn lại. Giống “thì sao?” trong tiếng Việt.",
            "formula": [
                ("Câu", "#6ee7b7"),
                (",", "#94a3b8"),
                ("呢？", "#6ee7b7", True),
            ],
            "rows": [
                ("你呢？", "Nǐ ne?", "Còn bạn thì sao?", "Hỏi lại người vừa nói"),
                ("我很好，你呢？", "Wǒ hěn hǎo, nǐ ne?", "Tôi khỏe, còn bạn?", "Trả lời xong rồi hỏi lại"),
                ("今天很热，明天呢？", "Jīntiān hěn rè, míngtiān ne?", "Hôm nay nóng, còn ngày mai?", "Hỏi về khả năng còn lại"),
                ("苹果五块，香蕉呢？", "Píngguǒ wǔ kuài, xiāngjiāo ne?", "Táo năm nghìn, còn chuối?", "Hỏi giá món khác"),
            ],
        },
        {
            "color": "#2563eb",
            "bg": "#eff6ff",
            "title": "2. Hỏi thông tin — nhẹ nhàng, thân mật",
            "desc": "Đặt 呢 cuối câu hỏi có từ để hỏi (什么, 谁, 哪儿...) hoặc sau chủ ngữ để hỏi “còn A thì...?”. 呢 khiến câu hỏi nghe tò mò, thân mật hơn.",
            "formula": [
                ("Chủ ngữ", "#93c5fd"),
                ("+", "#94a3b8"),
                ("呢", "#93c5fd", True),
                (",", "#e2e8f0"),
                ("... ?", "#93c5fd"),
            ],
            "rows": [
                ("你在哪儿呢？", "Nǐ zài nǎr ne?", "Bạn đang ở đâu đấy?", "Thân mật hơn 你在哪儿？"),
                ("你喜欢吃什么呢？", "Nǐ xǐhuan chī shénme ne?", "Bạn thích ăn gì thế?", "Hỏi thăm, kỳ vọng được chia sẻ"),
                ("他呢，会不会说中文？", "Tā ne, huì bu huì shuō Zhōngwén?", "Còn anh ấy thì có biết tiếng Trung không?", "呢 sau chủ ngữ = còn... thì"),
                ("这家店呢，贵不贵？", "Zhè jiā diàn ne, guì bu guì?", "Còn cửa hàng này thì đắt không?", "Chuyển sang đối tượng mới để hỏi"),
            ],
        },
        {
            "color": "#d97706",
            "bg": "#fffbeb",
            "title": "3. “Đang ... đấy” — hành động tiếp diễn",
            "desc": "Với động từ hành động (吃, 做, 写, 睡, 等...), thêm 在/正/正在 + 呢 cuối câu để nhấn mạnh việc đang xảy ra ngay lúc nói. Đây là cách nói “thì hiện tại tiếp diễn” của tiếng Trung.",
            "formula": [
                ("Chủ ngữ", "#fcd34d"),
                ("+ 在/正/正在", "#fcd34d", True),
                ("+ Động từ + (Tân ngữ)", "#fcd34d"),
                ("+ 呢", "#fcd34d", True),
                ("。", "#e2e8f0"),
            ],
            "rows": [
                ("我在做饭呢，你等一下。", "Wǒ zài zuòfàn ne, nǐ děng yíxià.", "Tôi đang nấu cơm, bạn đợi chút.", "在 + 做饭 + 呢"),
                ("她正在睡觉呢。", "Tā zhèngzài shuìjiào ne.", "Cô ấy đang ngủ đấy.", "正在 nhấn mạnh hơn 在"),
                ("别吵，我在写作业呢。", "Bié chǎo, wǒ zài xiě zuòyè ne.", "Đừng ồn, tôi đang làm bài tập.", "Ngụ ý: đừng làm phiền"),
                ("我们正等你呢！", "Wǒmen zhèng děng nǐ ne!", "Chúng tôi đang đợi bạn đấy!", "正 = ngay lúc này"),
            ],
        },
        {
            "color": "#be123c",
            "bg": "#fff1f2",
            "title": "4. Nhấn mạnh — “rồi đấy, mà”",
            "desc": "呢 cuối câu trần thuật nhấn mạnh điều người nói khẳng định: đã xong rồi, biết từ lâu, hoặc tôi nói thật đấy. Hay đi với 已经/早就/都.",
            "formula": [
                ("Câu trần thuật", "#fda4af"),
                ("+ 呢", "#fda4af", True),
                ("。", "#e2e8f0"),
            ],
            "rows": [
                ("钱我已经付了呢。", "Qián wǒ yǐjīng fù le ne.", "Tiền tôi trả rồi đấy.", "Ngụ ý: đừng đòi nữa"),
                ("我早就知道呢。", "Wǒ zǎo jiù zhīdào ne.", "Tôi biết từ lâu rồi mà.", "早就 + 呢"),
                ("事情都解决了呢。", "Shìqing dōu jiějué le ne.", "Mọi việc đã giải quyết xong rồi.", "都 ... 了 + 呢"),
                ("他在家呢。", "Tā zài jiā ne.", "Anh ấy đang ở nhà đấy.", "Nhấn mạnh, ngụ ý rõ ràng"),
            ],
        },
    ]

    with tab_theory:
        st.markdown("""
        <div class="b103-hero">
            <div class="b103-char">呢</div>
            <div class="b103-py">ne · thanh ngang</div>
            <div class="b103-tag">Trợ từ cuối câu / sau chủ ngữ</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br/>", unsafe_allow_html=True)

        for case in cases:
            spans = ""
            for part in case["formula"]:
                text, color = part[0], part[1]
                big = len(part) > 2 and part[2]
                size = "2rem" if big else "1.05rem"
                spans += (
                    f'<span style="color:{color};font-size:{size};font-weight:800;margin:0 4px;">{text}</span>'
                )
            rows = ""
            for han, py, vi, note in case["rows"]:
                rows += f"""
                <tr>
                    <td class="b103-han">{han}</td>
                    <td class="b103-py2" style="color:{case['color']};">{py}</td>
                    <td class="b103-vi">{vi}</td>
                    <td class="b103-note">{note}</td>
                </tr>"""
            st.markdown(f"""
            <div class="b103-rule" style="border-left:5px solid {case['color']};background:{case['bg']};">
                <h4 style="color:{case['color']};">{case['title']}</h4>
                <p class="b103-desc">{case['desc']}</p>
                <div class="b103-formula">{spans}</div>
                <table class="b103-table">
                    <thead>
                        <tr style="color:{case['color']};">
                            <th>Chữ Hán</th><th>Pinyin</th><th>Nghĩa</th><th>Vì sao có 呢</th>
                        </tr>
                    </thead>
                    <tbody>{rows}</tbody>
                </table>
            </div>
            """, unsafe_allow_html=True)

    with tab_examples:
        st.markdown("### 吗 hỏi có/không · 呢 hỏi ngược lại và “đang”")
        st.markdown("""
        <div class="b103-pair">
            <div class="b103-pair-title">Bạn có phải học sinh không? — vs — Còn bạn thì sao?</div>
            <div class="b103-line" style="background:#eff6ff;border-left:4px solid #2563eb;">
                <div class="han">你是学生吗？</div>
                <div class="meta">Nǐ shì xuéshēng ma? — Chưa biết, hỏi có/không.</div>
            </div>
            <div class="b103-line" style="background:#ecfdf5;border-left:4px solid #059669;">
                <div class="han">你呢？你是学生吗？</div>
                <div class="meta">Nǐ ne? Nǐ shì xuéshēng ma? — Còn bạn thì sao? Bạn là học sinh không?</div>
            </div>
        </div>
        <div class="b103-pair">
            <div class="b103-pair-title">“Đang làm gì?” — ba cách nói</div>
            <div class="b103-line" style="background:#f8fafc;border-left:4px solid #64748b;">
                <div class="han">你做什么？</div>
                <div class="meta">Nǐ zuò shénme? — Bạn làm gì? (trung lập, có thể hỏi thói quen)</div>
            </div>
            <div class="b103-line" style="background:#fffbeb;border-left:4px solid #d97706;">
                <div class="han">你在做什么？</div>
                <div class="meta">Nǐ zài zuò shénme? — Bạn đang làm gì? (nhấn mạnh lúc này)</div>
            </div>
            <div class="b103-line" style="background:#fffbeb;border-left:4px solid #d97706;">
                <div class="han">你在做什么呢？</div>
                <div class="meta">Nǐ zài zuò shénme ne? — Bạn đang làm gì đấy? (thân mật, tò mò)</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Hội thoại ngắn — hỏi thăm bạn bè")
        st.caption("呢 xuất hiện ba lần: hỏi lại, hỏi thông tin, và “đang... đấy”.")
        st.markdown("""
        <div class="b103-dlg">
            <div class="b103-turn">
                <div class="b103-who a">A</div>
                <div class="han" style="font-size:1.15rem;font-weight:800;">你好吗？</div>
                <div class="meta" style="color:#64748b;">Nǐ hǎo ma? — Bạn khỏe không?</div>
            </div>
            <div class="b103-turn">
                <div class="b103-who b">B</div>
                <div class="han" style="font-size:1.15rem;font-weight:800;">我很好，你呢？</div>
                <div class="meta" style="color:#64748b;">Wǒ hěn hǎo, nǐ ne? — Tôi khỏe, còn bạn?</div>
            </div>
            <div class="b103-turn">
                <div class="b103-who a">A</div>
                <div class="han" style="font-size:1.15rem;font-weight:800;">我也很好。你在做什么呢？</div>
                <div class="meta" style="color:#64748b;">Wǒ yě hěn hǎo. Nǐ zài zuò shénme ne? — Tôi cũng khỏe. Bạn đang làm gì đấy?</div>
            </div>
            <div class="b103-turn">
                <div class="b103-who b">B</div>
                <div class="han" style="font-size:1.15rem;font-weight:800;">我在看书呢。你呢？</div>
                <div class="meta" style="color:#64748b;">Wǒ zài kàn shū ne. Nǐ ne? — Tôi đang đọc sách đấy. Còn bạn?</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_tips:
        st.markdown("""
        <div class="b103-tip">
            <div style="font-weight:800;font-size:1.05rem;color:#713f12;margin-bottom:8px;">Một câu để nhớ</div>
            <div style="font-size:1.15rem;font-weight:800;color:#0f172a;">Hỏi lại → 呢？ &nbsp;·&nbsp; “Đang... đấy” → 在/正 + V + 呢 &nbsp;·&nbsp; Nhấn mạnh → ...了/都 + 呢</div>
        </div>
        """, unsafe_allow_html=True)

        traps = [
            (
                "呢 đọc thanh ngang",
                "Viết <b>ne</b>, không dấu. Không đọc né, nē hay nè. Trong câu, 呢 không nhấn.",
            ),
            (
                "呢 không thay 吗 trong câu hỏi có/không",
                "你是学生<b>吗</b>？ = chưa biết. <span class='b103-bad'>你是学生呢？</span> nghe không tự nhiên. Dùng 呢 khi hỏi lại, hỏi thông tin, hoặc “đang”.",
            ),
            (
                "呢 chỉ mang nghĩa “đang” với động từ hành động",
                "吃饭, 做作业, 看书, 等 → được: 我在吃饭<b>呢</b>. Nhưng 是, 喜欢, 知道 là trạng thái → không diễn tả tiếp diễn.",
            ),
            (
                "呢 đứng cuối câu hoặc sau chủ ngữ",
                "我在看书<b>呢</b> ✓ &nbsp; 他<b>呢</b>，会说中文 ✓ &nbsp; <span class='b103-bad'>我呢在看书。</span> ✗",
            ),
            (
                "呢 và 吧 khác nhau",
                "我们去吃饭<b>吧</b> = rủ đi ăn. 我们去吃饭<b>呢</b> = chúng tôi đang đi ăn đấy. 吧 rủ/kêu, 呢 thông báo đang làm.",
            ),
        ]
        for title, body in traps:
            st.markdown(f"""
            <div class="b103-trap">
                <div style="font-weight:800;color:#9f1239;margin-bottom:4px;">⚠️ {title}</div>
                <div style="color:#334155;line-height:1.55;">{body}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class="b103-key">
            <div style="font-weight:800;font-size:1.05rem;">Bảng chọn nhanh</div>
            <table>
                <tr><td style="width:34%;font-weight:700;">Việc người nói muốn</td><td>Câu</td></tr>
                <tr><td>Hỏi lại “còn... thì sao?”</td><td>你呢？ / 明天呢？</td></tr>
                <tr><td>Hỏi thông tin, thân mật</td><td>你在哪儿呢？ / 你喜欢什么呢？</td></tr>
                <tr><td>Nói “đang... đấy”</td><td>我在做饭呢。 / 她正在睡觉呢。</td></tr>
                <tr><td>Nhấn mạnh “rồi đấy, mà”</td><td>钱我已经付了呢。 / 我早就知道呢。</td></tr>
                <tr><td>Hỏi có/không (không dùng 呢)</td><td>你是学生吗？</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    with tab_quiz:
        st.markdown("Chọn câu hoặc chữ đúng. Nộp bài để xem giải thích.")
        quiz_data = [
            {
                "q": "“Tôi khỏe, còn bạn thì sao?”",
                "options": ["我很好，你吗？", "我很好，你呢？", "我很好，你吧？"],
                "answer": "我很好，你呢？",
                "explain": "Hỏi ngược lại “còn... thì sao?” dùng 呢, không dùng 吗 hay 吧."
            },
            {
                "q": "“Bạn đang làm gì đấy?” (thân mật, tò mò)",
                "options": ["你做什么呢？", "你做什么吗？", "你做什么吧？"],
                "answer": "你做什么呢？",
                "explain": "什么 đã là từ để hỏi. Thêm 呢 cuối câu cho sắc thái thân mật. 吗/吧 không đứng sau từ để hỏi."
            },
            {
                "q": "“Tôi đang nấu cơm, bạn đợi chút.”",
                "options": ["我做饭呢，你等一下。", "我在做饭呢，你等一下。", "我做饭吗，你等一下。"],
                "answer": "我在做饭呢，你等一下。",
                "explain": "Diễn tả “đang” cần 在/正/正在 trước động từ + 呢 cuối câu."
            },
            {
                "q": "Điền vào chỗ trống: 你___，会不会说中文？ (Còn bạn thì có biết tiếng Trung không?)",
                "options": ["呢", "吗", "吧"],
                "answer": "呢",
                "explain": "呢 sau chủ ngữ = “còn... thì...?”. 吗 chỉ hỏi có/không, 吧 là đoán/rủ."
            },
            {
                "q": "Câu nào đúng?",
                "options": ["他在家呢。", "他呢在家。", "他在家吗呢。"],
                "answer": "他在家呢。",
                "explain": "呢 đứng cuối câu khi nhấn mạnh “đang ở nhà đấy”. 呢 không đứng giữa câu."
            },
            {
                "q": "“Tiền tôi trả rồi đấy.” (ngụ ý: đừng đòi nữa)",
                "options": ["钱我付了呢。", "钱我呢付了。", "钱付了吗呢。"],
                "answer": "钱我付了呢。",
                "explain": "已/了 + 呢 cuối câu = nhấn mạnh đã xong, “rồi đấy”."
            },
            {
                "q": "Hôm nay nóng, còn ngày mai thì sao?",
                "options": ["今天很热，明天呢？", "今天很热，明天吗？", "今天很热，明天吧？"],
                "answer": "今天很热，明天呢？",
                "explain": "Hỏi về khả năng còn lại trong so sánh dùng 呢. 吗 là hỏi có/không, 吧 là đoán."
            },
            {
                "q": "Câu nào sai?",
                "options": ["我在看书呢。", "你是学生呢？", "你在哪儿呢？"],
                "answer": "你是学生呢？",
                "explain": "是 là động từ trạng thái, câu hỏi có/không phải dùng 吗: 你是学生吗？ 呢 chỉ dùng hỏi lại/thông tin/đang."
            },
        ]

        if "b103_submitted" not in st.session_state:
            st.session_state.b103_submitted = False
        if "b103_answers" not in st.session_state:
            st.session_state.b103_answers = {}

        for i, q in enumerate(quiz_data):
            st.markdown(f"""
            <div style="background:white;border:1px solid #e2e8f0;border-radius:14px;padding:18px 22px;margin-bottom:4px;">
                <div style="font-size:1.15rem;font-weight:800;color:#0f172a;">Câu {i+1}. {q['q']}</div>
            </div>
            """, unsafe_allow_html=True)
            key = f"b103_a{i}"
            st.radio(
                f"Chọn đáp án câu {i+1}:",
                q["options"],
                key=key,
                horizontal=True,
                disabled=st.session_state.b103_submitted,
                label_visibility="collapsed",
            )
            if st.session_state.b103_submitted:
                user_ans = st.session_state.b103_answers.get(key)
                if user_ans == q["answer"]:
                    st.success(f"Đúng. {q['explain']}")
                else:
                    st.error(f"Đáp án đúng: **{q['answer']}**. {q['explain']}")
            st.markdown("<br/>", unsafe_allow_html=True)

        col_submit, col_reset = st.columns([1, 1])
        with col_submit:
            if not st.session_state.b103_submitted:
                if st.button("Nộp bài", use_container_width=True, key="b103_submit", type="primary"):
                    st.session_state.b103_answers = {
                        f"b103_a{i}": st.session_state.get(f"b103_a{i}") for i in range(len(quiz_data))
                    }
                    st.session_state.b103_submitted = True
                    st.rerun()
        with col_reset:
            if st.session_state.b103_submitted:
                if st.button("Làm lại", use_container_width=True, key="b103_reset"):
                    st.session_state.b103_submitted = False
                    st.session_state.b103_answers = {}
                    for i in range(len(quiz_data)):
                        key = f"b103_a{i}"
                        if key in st.session_state:
                            del st.session_state[key]
                    st.rerun()

        if st.session_state.b103_submitted:
            correct = sum(
                1 for i, q in enumerate(quiz_data)
                if st.session_state.b103_answers.get(f"b103_a{i}") == q["answer"]
            )
            total = len(quiz_data)
            pct = int(correct / total * 100)
            if pct == 100:
                msg = "Nắm vững cả bốn cách dùng 呢."
            elif pct >= 70:
                msg = "Xem lại các câu sai, nhất là chỗ 呢 khác 吗 và 吧."
            else:
                msg = "Đọc lại phần Lý thuyết rồi làm lại."
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#1e3a8a,#065f46);color:white;border-radius:16px;padding:28px;text-align:center;margin-top:12px;">
                <div style="font-size:3.2rem;font-weight:900;">{correct}/{total}</div>
                <div>{pct}% đúng</div>
                <div style="margin-top:8px;font-weight:700;">{msg}</div>
            </div>
            """, unsafe_allow_html=True)


def show_lesson10_4_yixia():
    st.markdown("""
    <style>
    .b104-hero {
        background: linear-gradient(145deg, #ecfdf5, #d1fae5);
        border: 2px solid #6ee7b7;
        border-radius: 18px;
        padding: 28px 24px;
        text-align: center;
        box-shadow: 0 8px 28px rgba(0,0,0,0.06);
        margin-bottom: 8px;
    }
    .b104-char { font-size: 4.2rem; font-weight: 900; color: #047857; line-height: 1.15; }
    .b104-py { font-family: monospace; font-size: 1.6rem; font-weight: 800; color: #065f46; margin-top: 6px; }
    .b104-tag {
        display: inline-block; margin-top: 10px; background: #6ee7b7; color: #064e3b;
        font-weight: 800; padding: 4px 14px; border-radius: 999px;
    }
    .b104-rule {
        background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px;
        padding: 18px 20px; margin-bottom: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    .b104-rule h4 { margin: 0 0 6px 0; }
    .b104-use, .b104-mean { color: #334155; font-size: 0.95rem; line-height: 1.65; margin: 0 0 8px 0; }
    .b104-use b, .b104-mean b { color: #0f172a; }
    .b104-formula {
        background: #1e293b; border-radius: 10px; padding: 12px 18px;
        display: flex; align-items: center; justify-content: center; flex-wrap: wrap; gap: 6px; margin-bottom: 12px;
    }
    .b104-table { width: 100%; border-collapse: collapse; font-size: 0.92rem; }
    .b104-table th { text-align: left; padding: 8px 10px; font-weight: 800; }
    .b104-table td { padding: 8px 10px; border-top: 1px solid #e2e8f0; vertical-align: top; }
    .b104-han { font-size: 1.12rem; font-weight: 800; color: #0f172a; }
    .b104-py2 { font-family: monospace; font-weight: 700; }
    .b104-vi { font-style: italic; color: #475569; }
    .b104-note { color: #64748b; font-size: 0.85rem; }
    .b104-pair { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px; padding: 18px 20px; margin-bottom: 14px; }
    .b104-pair-title { font-weight: 800; color: #0f172a; margin-bottom: 10px; }
    .b104-line { border-radius: 10px; padding: 10px 14px; margin-bottom: 8px; }
    .b104-line .han { font-size: 1.2rem; font-weight: 800; color: #0f172a; }
    .b104-line .meta { font-size: 0.88rem; color: #64748b; }
    .b104-dlg { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px; padding: 18px 20px; margin-top: 8px; }
    .b104-turn { margin-bottom: 12px; }
    .b104-who { display: inline-block; font-weight: 800; font-size: 0.8rem; padding: 2px 8px; border-radius: 8px; margin-bottom: 4px; }
    .b104-who.a { background: #d1fae5; color: #065f46; }
    .b104-who.b { background: #dbeafe; color: #1e3a8a; }
    .b104-tip { background: linear-gradient(135deg, #fefce8, #fef9c3); border: 2px solid #fde047; border-radius: 16px; padding: 20px 22px; margin-bottom: 14px; }
    .b104-trap { background: #fff1f2; border: 2px solid #fda4af; border-radius: 14px; padding: 14px 16px; margin-bottom: 10px; }
    .b104-key { background: linear-gradient(135deg, #0f172a, #065f46); color: white; border-radius: 16px; padding: 20px 22px; margin-top: 16px; }
    .b104-key table { width: 100%; border-collapse: collapse; margin-top: 10px; }
    .b104-key td { padding: 8px 10px; border-top: 1px solid rgba(255,255,255,0.15); vertical-align: top; }
    .b104-bad { color: #be123c; text-decoration: line-through; }
    .b104-ok { color: #166534; font-weight: 700; }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "💬 Bài 30 - Cách dùng 一下 (yíxià)",
        "一下 đứng sau động từ. Có khi là làm một lát, có khi làm câu nhờ nhẹ hơn, có khi là lượng từ để đếm số lần."
    )

    tab_theory, tab_examples, tab_tips, tab_quiz = st.tabs([
        "📚 Lý thuyết",
        "📝 Ví dụ đối chiếu",
        "⚠️ Lưu ý & Mẹo nhớ",
        "🎮 Luyện tập"
    ])

    cases = [
        {
            "color": "#059669",
            "bg": "#ecfdf5",
            "title": "1. Làm rất ngắn, chỉ một lát",
            "use": "Lấy động từ chỉ hành động, thêm <b>一下</b> ngay phía sau. Câu không cần tân ngữ.",
            "mean": "Việc chỉ xảy ra một chốc rồi thôi, không kéo dài. Nghĩa là “một chút”, “một lát”, “làm qua một lần”.",
            "formula": [("Động từ", "#6ee7b7"), ("+", "#94a3b8"), ("一下", "#6ee7b7", True)],
            "rows": [
                ("等一下。", "Děng yíxià.", "Đợi một lát.", "Đợi trong chốc lát, không đợi lâu"),
                ("看一下。", "Kàn yíxià.", "Xem một chút.", "Xem qua, không xem kỹ"),
                ("听一下。", "Tīng yíxià.", "Nghe một chút.", "Nghe thoáng qua"),
                ("试一下。", "Shì yíxià.", "Thử một lần.", "Làm thử cho biết kết quả"),
                ("说一下。", "Shuō yíxià.", "Nói một chút.", "Nói ngắn, nói qua việc đó"),
                ("想一下。", "Xiǎng yíxià.", "Nghĩ một lát.", "Suy nghĩ trong chốc lát"),
            ],
        },
        {
            "color": "#2563eb",
            "bg": "#eff6ff",
            "title": "2. Có tân ngữ thì 一下 đứng trước tân ngữ",
            "use": "Viết <b>động từ + 一下 + tân ngữ</b>. Tân ngữ là người hoặc vật mà hành động hướng tới. Không đưa 一下 ra sau tân ngữ.",
            "mean": "Vẫn là làm một lát hoặc làm một lần, và nói rõ làm với ai, với cái gì.",
            "formula": [("Động từ", "#93c5fd"), ("+", "#94a3b8"), ("一下", "#93c5fd", True), ("+", "#94a3b8"), ("Tân ngữ", "#93c5fd")],
            "rows": [
                ("你看一下这本书。", "Nǐ kàn yíxià zhè běn shū.", "Bạn xem qua quyển sách này.", "这本书 là vật được xem"),
                ("我问一下老师。", "Wǒ wèn yíxià lǎoshī.", "Tôi hỏi thầy một câu.", "老师 là người được hỏi"),
                ("请你介绍一下你的老师。", "Qǐng nǐ jièshào yíxià nǐ de lǎoshī.", "Bạn giới thiệu một chút về thầy của bạn.", "你的老师 là người được giới thiệu"),
                ("我们听一下这首歌。", "Wǒmen tīng yíxià zhè shǒu gē.", "Chúng ta nghe qua bài hát này.", "这首歌 là vật được nghe"),
            ],
        },
        {
            "color": "#d97706",
            "bg": "#fffbeb",
            "title": "3. Làm lời nhờ nhẹ hơn",
            "use": "Giữ nguyên động từ, thêm <b>一下</b> phía sau. Muốn nhờ lịch sự hơn thì thêm <b>请你</b> ở đầu câu.",
            "mean": "Việc cần làm không đổi. 一下 chỉ làm câu bớt khô, bớt giống ra lệnh. Có 请你 thì thành lời nhờ.",
            "formula": [("请你", "#fcd34d"), ("+", "#94a3b8"), ("Động từ", "#fcd34d"), ("+", "#94a3b8"), ("一下", "#fcd34d", True)],
            "rows": [
                ("你看。", "Nǐ kàn.", "Bạn xem.", "Khô, giống ra lệnh"),
                ("你看一下。", "Nǐ kàn yíxià.", "Bạn xem một chút.", "Cùng một việc, giọng đã nhẹ hơn"),
                ("请你看一下。", "Qǐng nǐ kàn yíxià.", "Bạn xem giúp một chút.", "Lời nhờ lịch sự"),
            ],
        },
        {
            "color": "#7c3aed",
            "bg": "#f5f3ff",
            "title": "4. Làm lượng từ: đếm số lần",
            "use": "Chỉ dùng với <b>động từ chỉ động tác ngắn</b>: động tác xảy ra một cái rồi kết thúc ngay, nên đếm từng cái được. Gồm <b>拍</b> vỗ, <b>敲</b> gõ, <b>打</b> đánh, <b>踢</b> đá, <b>点</b> gật, <b>摇</b> lắc, <b>响</b> kêu. Công thức: động từ chỉ động tác ngắn + 一下 / 两下 / 三下.",
            "mean": "Đếm động tác đó xảy ra mấy cái, mấy tiếng. 一下 = một cái. 等, 想, 看, 听, 说, 休息 là động từ chỉ việc làm một lát, chỉ dùng ở trường hợp 1, không đếm thành 两下, 三下.",
            "formula": [("Động từ chỉ động tác ngắn", "#c4b5fd"), ("+", "#94a3b8"), ("一下 / 两下 / 三下", "#c4b5fd", True)],
            "rows": [
                ("拍一下。", "Pāi yíxià.", "Vỗ một cái.", "拍 là động từ chỉ động tác ngắn: vỗ"),
                ("敲一下门。", "Qiāo yíxià mén.", "Gõ cửa một cái.", "敲 là động từ chỉ động tác ngắn: gõ"),
                ("响两下。", "Xiǎng liǎng xià.", "Kêu hai tiếng.", "响 là động từ chỉ động tác ngắn: kêu"),
                ("打三下。", "Dǎ sān xià.", "Đánh ba cái.", "打 là động từ chỉ động tác ngắn: đánh"),
            ],
        },
    ]

    with tab_theory:
        st.markdown("""
        <div class="b104-hero">
            <div class="b104-char">一下</div>
            <div class="b104-py">yíxià · thanh 2 + thanh 4</div>
            <div class="b104-tag">Đứng sau động từ · bốn cách dùng</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br/>", unsafe_allow_html=True)
        st.info("**一** trong **一下** đọc **yí**, không đọc yī. Vì **下** là thanh 4, **一** đổi thành thanh 2.")

        for case in cases:
            spans = ""
            for part in case["formula"]:
                text, color = part[0], part[1]
                big = len(part) > 2 and part[2]
                size = "2rem" if big else "1.05rem"
                spans += f'<span style="color:{color};font-size:{size};font-weight:800;margin:0 4px;">{text}</span>'
            rows = ""
            for han, py, vi, note in case["rows"]:
                rows += f"""
                <tr>
                    <td class="b104-han">{han}</td>
                    <td class="b104-py2" style="color:{case['color']};">{py}</td>
                    <td class="b104-vi">{vi}</td>
                    <td class="b104-note">{note}</td>
                </tr>"""
            st.markdown(f"""
            <div class="b104-rule" style="border-left:5px solid {case['color']};background:{case['bg']};">
                <h4 style="color:{case['color']};">{case['title']}</h4>
                <p class="b104-use"><b>Cách dùng:</b> {case['use']}</p>
                <p class="b104-mean"><b>Nghĩa:</b> {case['mean']}</p>
                <div class="b104-formula">{spans}</div>
                <table class="b104-table">
                    <thead>
                        <tr style="color:{case['color']};">
                            <th>Chữ Hán</th><th>Pinyin</th><th>Nghĩa</th><th>Ghi chú</th>
                        </tr>
                    </thead>
                    <tbody>{rows}</tbody>
                </table>
            </div>
            """, unsafe_allow_html=True)

    with tab_examples:
        st.markdown("### Ba câu cùng một việc, ba giọng khác nhau")
        st.markdown("""
        <div class="b104-pair">
            <div class="b104-pair-title">Nhờ người xem</div>
            <div class="b104-line" style="background:#f8fafc;border-left:4px solid #64748b;">
                <div class="han">你看。</div>
                <div class="meta">Nǐ kàn. — Bạn xem. <b>Khô, giống ra lệnh.</b></div>
            </div>
            <div class="b104-line" style="background:#ecfdf5;border-left:4px solid #059669;">
                <div class="han">你看一下。</div>
                <div class="meta">Nǐ kàn yíxià. — Bạn xem một chút. <b>Nhẹ hơn.</b></div>
            </div>
            <div class="b104-line" style="background:#fffbeb;border-left:4px solid #d97706;">
                <div class="han">请你看一下。</div>
                <div class="meta">Qǐng nǐ kàn yíxià. — Bạn xem giúp một chút. <b>Nhờ lịch sự.</b></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 一下 đi với việc làm · 一点 đi với lượng hoặc mức độ")
        st.markdown("""
        <div class="b104-pair">
            <div class="b104-pair-title">Cả hai đều có thể dịch là “một chút”, nhưng không thay nhau</div>
            <div class="b104-line" style="background:#ecfdf5;border-left:4px solid #059669;">
                <div class="han">等一下。 / 看一下。 / 说一下。</div>
                <div class="meta">Děng yíxià. / Kàn yíxià. / Shuō yíxià. — <b>一下</b> đi với việc làm.</div>
            </div>
            <div class="b104-line" style="background:#eff6ff;border-left:4px solid #2563eb;">
                <div class="han">一点水。 / 好一点。 / 快一点。</div>
                <div class="meta">Yìdiǎn shuǐ. / Hǎo yìdiǎn. / Kuài yìdiǎn. — <b>一点</b> đi với lượng hoặc mức độ.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.caption("Muốn bảo “đợi một chút” thì nói **等一下**, không nói 等一点.")

        st.markdown("### 一下 “một lát” khác 一下 “một cái”")
        st.markdown("""
        <div class="b104-pair">
            <div class="b104-pair-title">Cùng viết 一下, nhưng một bên là thời gian ngắn, một bên là lượng từ đếm lần</div>
            <div class="b104-line" style="background:#ecfdf5;border-left:4px solid #059669;">
                <div class="han">休息一下。 / 想一下。</div>
                <div class="meta">Xiūxi yíxià. / Xiǎng yíxià. — Nghỉ một lát, nghĩ một lát. <b>Không đếm.</b> Không nói 休息三下 để bảo nghỉ ba lần.</div>
            </div>
            <div class="b104-line" style="background:#f5f3ff;border-left:4px solid #7c3aed;">
                <div class="han">拍一下。 / 拍两下。 / 敲三下。</div>
                <div class="meta">Pāi yíxià. / Pāi liǎng xià. / Qiāo sān xià. — Vỗ một cái, vỗ hai cái, gõ ba cái. <b>拍, 敲 là động từ chỉ động tác ngắn</b>, nên đếm được bằng 下.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Hội thoại ngắn")
        st.markdown("""
        <div class="b104-dlg">
            <div class="b104-turn">
                <div class="b104-who a">A</div>
                <div class="han">你等一下。我买水。</div>
                <div class="meta">Nǐ děng yíxià. Wǒ mǎi shuǐ. — Bạn đợi một chút. Tôi mua nước.</div>
            </div>
            <div class="b104-turn">
                <div class="b104-who b">B</div>
                <div class="han">好的。</div>
                <div class="meta">Hǎo de. — Được.</div>
            </div>
        </div>
        <div class="b104-dlg" style="margin-top:12px;">
            <div class="b104-turn">
                <div class="b104-who a">A</div>
                <div class="han">请你介绍一下你的老师。</div>
                <div class="meta">Qǐng nǐ jièshào yíxià nǐ de lǎoshī. — Bạn giới thiệu một chút về thầy của bạn.</div>
            </div>
            <div class="b104-turn">
                <div class="b104-who b">B</div>
                <div class="han">她是中国人，她教汉语。</div>
                <div class="meta">Tā shì Zhōngguó rén, tā jiāo Hànyǔ. — Cô ấy là người Trung Quốc, cô dạy tiếng Hán.</div>
            </div>
        </div>
        <div class="b104-dlg" style="margin-top:12px;">
            <div class="b104-turn">
                <div class="b104-who a">A</div>
                <div class="han">你听，门响了两下。</div>
                <div class="meta">Nǐ tīng, mén xiǎng le liǎng xià. — Bạn nghe này, cửa kêu hai tiếng. <b>两下</b> đếm số lần.</div>
            </div>
            <div class="b104-turn">
                <div class="b104-who b">B</div>
                <div class="han">我去看一下。</div>
                <div class="meta">Wǒ qù kàn yíxià. — Tôi đi xem một chút. <b>一下</b> ở đây là làm một lát, không phải đếm.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_tips:
        st.markdown("""
        <div class="b104-tip">
            <div style="font-weight:800;font-size:1.05rem;color:#713f12;margin-bottom:8px;">Một câu để nhớ</div>
            <div style="font-size:1.15rem;font-weight:800;color:#0f172a;">Làm một lát hoặc nhờ nhẹ → 一下 &nbsp;·&nbsp; Đếm một cái, hai cái → 下 là lượng từ &nbsp;·&nbsp; Lượng hoặc mức độ → 一点</div>
        </div>
        """, unsafe_allow_html=True)
        traps = [
            ("一 đổi thanh khi đứng trước 下", "下 là thanh 4, nên 一 đọc <b>yí</b>. Viết yíxià. Không đọc yīxià."),
            ("一下 đứng sau động từ, trước tân ngữ", "Đúng: <span class='b104-ok'>看一下这本书</span>. Không nói <span class='b104-bad'>看这本书一下</span>."),
            ("一下 không thay 一点", "等<b>一下</b> = đợi một chút. 一点水 = một chút nước. <span class='b104-bad'>等一点</span> không dùng để bảo người khác đợi."),
            ("Đếm nhiều lần thì Số + 下", "Một lần: <b>一下</b>. Hai lần: <b>两下</b>. Ba lần: <b>三下</b>. Không viết <span class='b104-bad'>两一下</span>, <span class='b104-bad'>三一下</span>."),
            ("Trường hợp 4 chỉ dùng động từ chỉ động tác ngắn", "<b>拍</b> vỗ, <b>敲</b> gõ, <b>打</b> đánh, <b>踢</b> đá, <b>点</b> gật, <b>摇</b> lắc, <b>响</b> kêu. 等, 想, 休息 là làm một lát. Không nói <span class='b104-bad'>等三下</span>, <span class='b104-bad'>想两下</span>, <span class='b104-bad'>休息三下</span>."),
            ("Chỉ dùng với động từ chỉ hành động", "看, 听, 拍, 敲, 说, 等 thì được. Không nói <span class='b104-bad'>高一下</span>, <span class='b104-bad'>是一下</span>, <span class='b104-bad'>很一下</span>."),
        ]
        for title, body in traps:
            st.markdown(f"""
            <div class="b104-trap">
                <div style="font-weight:800;color:#9f1239;margin-bottom:4px;">⚠️ {title}</div>
                <div style="color:#334155;line-height:1.55;">{body}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("""
        <div class="b104-key">
            <div style="font-weight:800;font-size:1.05rem;">Bảng chọn nhanh</div>
            <table>
                <tr><td style="width:38%;font-weight:700;">Muốn nói</td><td>Câu</td></tr>
                <tr><td>Làm một lần, rất ngắn</td><td>看一下。 / 听一下。 / 试一下。</td></tr>
                <tr><td>Có người hoặc vật đi kèm</td><td>看一下这本书。 / 问一下老师。</td></tr>
                <tr><td>Nhờ cho lịch sự</td><td>请你看一下。 / 请你介绍一下。</td></tr>
                <tr><td>Động từ chỉ động tác ngắn: đếm một cái, hai cái, ba cái</td><td>拍一下。 / 响两下。 / 敲三下。</td></tr>
                <tr><td>Một chút nước, tốt hơn, nhanh hơn</td><td>一点水。 / 好一点。 / 快一点。</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    with tab_quiz:
        st.markdown("Chọn câu hoặc chữ đúng. Nộp bài để xem giải thích.")
        quiz_data = [
            {"q": "“Đợi một chút.”", "options": ["等一下。", "等一点。", "一下等。"], "answer": "等一下。", "explain": "Đợi là một việc làm, dùng 一下 sau động từ. 一点 không dùng trong câu này."},
            {"q": "“Bạn xem qua quyển sách này.”", "options": ["你看一下这本书。", "你看这本书一下。", "你一下看这本书。"], "answer": "你看一下这本书。", "explain": "一下 đứng ngay sau động từ, trước tân ngữ 这本书."},
            {"q": "Câu nào là lời nhờ lịch sự?", "options": ["你看。", "你看一下。", "请你看一下。"], "answer": "请你看一下。", "explain": "请你 + động từ + 一下 là câu nhờ. 你看 khô hơn. 你看一下 đã nhẹ, nhưng chưa có 请."},
            {"q": "一下 đọc thế nào?", "options": ["yīxià", "yíxià", "yìxià"], "answer": "yíxià", "explain": "下 là thanh 4, nên 一 đổi thành thanh 2: yí."},
            {"q": "Câu nào đúng khi muốn nói “một chút nước”?", "options": ["一下水", "一点水", "水一下"], "answer": "一点水", "explain": "Nước là lượng, dùng 一点. 一下 không đứng trước danh từ để chỉ “một chút nước”."},
            {"q": "Câu nào sai?", "options": ["听一下。", "吃一下。", "是一下。"], "answer": "是一下。", "explain": "是 không phải động từ chỉ hành động, không thêm 一下. 听 và 吃 thì được."},
            {"q": "Câu nào dùng 下 làm lượng từ, để đếm số lần?", "options": ["休息一下。", "他拍了一下桌子。", "好一点。"], "answer": "他拍了一下桌子。", "explain": "拍了一下 = vỗ một cái. 下 đếm số lần. 休息一下 là nghỉ một lát, không đếm. 好一点 dùng 一点."},
            {"q": "“Chuông gõ ba tiếng.”", "options": ["钟敲了三下。", "钟敲了三一下。", "钟三下敲了。"], "answer": "钟敲了三下。", "explain": "Đếm ba lần thì viết 三下, đứng sau động từ. Không viết 三一下, cũng không đưa 三下 lên trước động từ."},
        ]
        if "b104_submitted" not in st.session_state:
            st.session_state.b104_submitted = False
        if "b104_answers" not in st.session_state:
            st.session_state.b104_answers = {}
        for i, q in enumerate(quiz_data):
            st.markdown(f"""
            <div style="background:white;border:1px solid #e2e8f0;border-radius:14px;padding:18px 22px;margin-bottom:4px;">
                <div style="font-size:1.15rem;font-weight:800;color:#0f172a;">Câu {i+1}. {q['q']}</div>
            </div>
            """, unsafe_allow_html=True)
            key = f"b104_a{i}"
            st.radio(f"Chọn đáp án câu {i+1}:", q["options"], key=key, horizontal=True, disabled=st.session_state.b104_submitted, label_visibility="collapsed")
            if st.session_state.b104_submitted:
                user_ans = st.session_state.b104_answers.get(key)
                if user_ans == q["answer"]:
                    st.success(f"Đúng. {q['explain']}")
                else:
                    st.error(f"Đáp án đúng: **{q['answer']}**. {q['explain']}")
            st.markdown("<br/>", unsafe_allow_html=True)
        col_submit, col_reset = st.columns([1, 1])
        with col_submit:
            if not st.session_state.b104_submitted:
                if st.button("Nộp bài", use_container_width=True, key="b104_submit", type="primary"):
                    st.session_state.b104_answers = {f"b104_a{i}": st.session_state.get(f"b104_a{i}") for i in range(len(quiz_data))}
                    st.session_state.b104_submitted = True
                    st.rerun()
        with col_reset:
            if st.session_state.b104_submitted:
                if st.button("Làm lại", use_container_width=True, key="b104_reset"):
                    st.session_state.b104_submitted = False
                    st.session_state.b104_answers = {}
                    for i in range(len(quiz_data)):
                        key = f"b104_a{i}"
                        if key in st.session_state:
                            del st.session_state[key]
                    st.rerun()
        if st.session_state.b104_submitted:
            correct = sum(1 for i, q in enumerate(quiz_data) if st.session_state.b104_answers.get(f"b104_a{i}") == q["answer"])
            total = len(quiz_data)
            pct = int(correct / total * 100)
            if pct == 100:
                msg = "Nắm vững cách dùng 一下."
            elif pct >= 70:
                msg = "Xem lại chỗ 一下 khác 一点, vị trí của 一下, và lúc 下 là lượng từ đếm lần."
            else:
                msg = "Đọc lại phần Lý thuyết rồi làm lại."
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#064e3b,#1e3a8a);color:white;border-radius:16px;padding:28px;text-align:center;margin-top:12px;">
                <div style="font-size:3.2rem;font-weight:900;">{correct}/{total}</div>
                <div>{pct}% đúng</div>
                <div style="margin-top:8px;font-weight:700;">{msg}</div>
            </div>
            """, unsafe_allow_html=True)


def show_lesson10_5_hao_verb():
    st.markdown("""
    <style>
    .b105-hero {
        background: linear-gradient(145deg, #ecfdf5, #d1fae5);
        border: 2px solid #6ee7b7;
        border-radius: 18px;
        padding: 28px 24px;
        text-align: center;
        box-shadow: 0 8px 28px rgba(0,0,0,0.06);
        margin-bottom: 8px;
    }
    .b105-char { font-size: 3.4rem; font-weight: 900; color: #047857; line-height: 1.15; }
    .b105-py { font-family: monospace; font-size: 1.35rem; font-weight: 800; color: #065f46; margin-top: 6px; }
    .b105-tag {
        display: inline-block; margin-top: 10px; background: #6ee7b7; color: #064e3b;
        font-weight: 800; padding: 4px 14px; border-radius: 999px;
    }
    .b105-rule {
        background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px;
        padding: 18px 20px; margin-bottom: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    .b105-rule h4 { margin: 0 0 6px 0; }
    .b105-use, .b105-mean { color: #334155; font-size: 0.95rem; line-height: 1.65; margin: 0 0 8px 0; }
    .b105-use b, .b105-mean b { color: #0f172a; }
    .b105-formula {
        background: #1e293b; border-radius: 10px; padding: 12px 18px;
        display: flex; align-items: center; justify-content: center; flex-wrap: wrap; gap: 6px; margin-bottom: 12px;
    }
    .b105-table { width: 100%; border-collapse: collapse; font-size: 0.92rem; }
    .b105-table th { text-align: left; padding: 8px 10px; font-weight: 800; }
    .b105-table td { padding: 8px 10px; border-top: 1px solid #e2e8f0; vertical-align: top; }
    .b105-han { font-size: 1.12rem; font-weight: 800; color: #0f172a; }
    .b105-py2 { font-family: monospace; font-weight: 700; }
    .b105-vi { font-style: italic; color: #475569; }
    .b105-note { color: #64748b; font-size: 0.85rem; }
    .b105-pair { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px; padding: 18px 20px; margin-bottom: 14px; }
    .b105-pair-title { font-weight: 800; color: #0f172a; margin-bottom: 10px; }
    .b105-line { border-radius: 10px; padding: 10px 14px; margin-bottom: 8px; }
    .b105-line .han { font-size: 1.15rem; font-weight: 800; color: #0f172a; }
    .b105-line .meta { font-size: 0.88rem; color: #64748b; }
    .b105-tip { background: linear-gradient(135deg, #fefce8, #fef9c3); border: 2px solid #fde047; border-radius: 16px; padding: 20px 22px; margin-bottom: 14px; }
    .b105-trap { background: #fff1f2; border: 2px solid #fda4af; border-radius: 14px; padding: 14px 16px; margin-bottom: 10px; }
    .b105-key { background: linear-gradient(135deg, #0f172a, #065f46); color: white; border-radius: 16px; padding: 20px 22px; margin-top: 16px; }
    .b105-key table { width: 100%; border-collapse: collapse; margin-top: 10px; }
    .b105-key td { padding: 8px 10px; border-top: 1px solid rgba(255,255,255,0.15); vertical-align: top; }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "💬 Bài 35 - Cách dùng 好 / 难 + động từ",
        "好 và 难 đứng trước động từ. Cả cụm dùng như tính từ: nhận xét vật đẹp hay xấu, ngon hay dở, dễ làm hay khó làm."
    )

    tab_theory, tab_examples, tab_tips, tab_quiz = st.tabs([
        "📚 Lý thuyết",
        "📝 Ví dụ đối chiếu",
        "⚠️ Lưu ý & Mẹo nhớ",
        "🎮 Luyện tập"
    ])

    cases = [
        {
            "color": "#059669",
            "bg": "#ecfdf5",
            "title": "1. Động từ giác quan và trải nghiệm",
            "use": "<b>好</b> hoặc <b>难</b> đứng trước động từ gắn với giác quan hoặc một hoạt động có thể đánh giá cảm giác: <b>看</b> nhìn, xem, đọc; <b>吃</b> ăn; <b>喝</b> uống; <b>听</b> nghe; <b>闻</b> ngửi; <b>玩</b> chơi.",
            "mean": "<b>好</b> là đẹp, ngon, hay, vui. <b>难</b> là xấu, dở, khó nghe, hôi.",
            "formula": [("Chủ ngữ", "#6ee7b7"), ("+", "#94a3b8"), ("很", "#6ee7b7"), ("+", "#94a3b8"), ("好 / 难", "#6ee7b7", True), ("+", "#94a3b8"), ("Động từ", "#6ee7b7")],
            "rows": [
                ("好看 / 难看", "hǎokàn / nánkàn", "đẹp, hay / xấu", "看 nhìn, xem, đọc"),
                ("好吃 / 难吃", "hǎochī / nánchī", "ngon / dở", "吃 ăn"),
                ("好喝 / 难喝", "hǎohē / nánhē", "ngon / dở (đồ uống)", "喝 uống"),
                ("好听 / 难听", "hǎotīng / nántīng", "hay, êm tai / khó nghe", "听 nghe"),
                ("好闻 / 难闻", "hǎowén / nánwén", "thơm, dễ chịu / hôi, khó ngửi", "闻 ngửi"),
                ("好玩 / 难玩", "hǎowán / nánwán", "vui, thú vị / khó chơi", "玩 chơi"),
            ],
        },
        {
            "color": "#2563eb",
            "bg": "#eff6ff",
            "title": "2. Động từ thao tác và nhận thức",
            "use": "<b>好</b> hoặc <b>难</b> đứng trước động từ chỉ một hành động có thể đánh giá mức độ dễ hay khó: <b>学</b> học, <b>用</b> dùng, <b>写</b> viết, <b>懂</b> hiểu, <b>记</b> nhớ, <b>找</b> tìm, <b>做</b> làm.",
            "mean": "<b>好</b> là dễ làm việc đó. <b>难</b> là khó làm việc đó.",
            "formula": [("Chủ ngữ", "#93c5fd"), ("+", "#94a3b8"), ("很", "#93c5fd"), ("+", "#94a3b8"), ("好 / 难", "#93c5fd", True), ("+", "#94a3b8"), ("Động từ", "#93c5fd")],
            "rows": [
                ("好学 / 难学", "hǎoxué / nánxué", "dễ học / khó học", "学 học"),
                ("好用 / 难用", "hǎoyòng / nányòng", "dễ dùng / khó dùng", "用 dùng"),
                ("好写 / 难写", "hǎoxiě / nánxiě", "dễ viết / khó viết", "写 viết"),
                ("好懂 / 难懂", "hǎodǒng / nándǒng", "dễ hiểu / khó hiểu", "懂 hiểu"),
                ("好记 / 难记", "hǎojì / nánjì", "dễ nhớ / khó nhớ", "记 nhớ"),
                ("好找 / 难找", "hǎozhǎo / nánzhǎo", "dễ tìm / khó tìm", "找 tìm"),
                ("好做 / 难做", "hǎozuò / nánzuò", "dễ làm / khó làm", "做 làm"),
            ],
        },
        {
            "color": "#d97706",
            "bg": "#fffbeb",
            "title": "3. Phủ định với 不",
            "use": "Phủ định của <b>好</b> chỉ dùng <b>不</b>. <b>不</b> đứng trước cả cụm <b>好 + động từ</b>.",
            "mean": "<b>不好吃</b> là không ngon, <b>不好看</b> là không đẹp, <b>不好写</b> là không dễ viết.",
            "formula": [("Chủ ngữ", "#fcd34d"), ("+", "#94a3b8"), ("不", "#fcd34d", True), ("+", "#94a3b8"), ("好", "#fcd34d"), ("+", "#94a3b8"), ("Động từ", "#fcd34d")],
            "rows": [
                ("这个菜不好吃。", "Zhège cài bù hǎochī.", "Món này không ngon.", "不 đứng trước 好吃"),
                ("这件衣服不好看。", "Zhè jiàn yīfu bù hǎokàn.", "Áo này không đẹp.", "不 đứng trước 好看"),
                ("这首歌不好听。", "Zhè shǒu gē bù hǎotīng.", "Bài hát này không hay.", "不 đứng trước 好听"),
                ("这个字不好写。", "Zhège zì bù hǎoxiě.", "Chữ này không dễ viết.", "不 đứng trước 好写"),
                ("这句话不好懂。", "Zhè jù huà bù hǎodǒng.", "Câu này không dễ hiểu.", "不 đứng trước 好懂"),
            ],
        },
    ]

    with tab_theory:
        st.markdown("""
        <div class="b105-hero">
            <div class="b105-char">好 / 难 + động từ</div>
            <div class="b105-py">hǎo / nán · đứng trước động từ</div>
            <div class="b105-tag">Cả cụm dùng như một tính từ</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br/>", unsafe_allow_html=True)

        for case in cases:
            spans = ""
            for part in case["formula"]:
                text, color = part[0], part[1]
                big = len(part) > 2 and part[2]
                size = "1.7rem" if big else "1.02rem"
                spans += f'<span style="color:{color};font-size:{size};font-weight:800;margin:0 4px;">{text}</span>'
            rows = ""
            for han, py, vi, note in case["rows"]:
                rows += f"""
                <tr>
                    <td class="b105-han">{han}</td>
                    <td class="b105-py2" style="color:{case['color']};">{py}</td>
                    <td class="b105-vi">{vi}</td>
                    <td class="b105-note">{note}</td>
                </tr>"""
            st.markdown(f"""
            <div class="b105-rule" style="border-left:5px solid {case['color']};background:{case['bg']};">
                <h4 style="color:{case['color']};">{case['title']}</h4>
                <p class="b105-use"><b>Cách dùng:</b> {case['use']}</p>
                <p class="b105-mean"><b>Nghĩa:</b> {case['mean']}</p>
                <div class="b105-formula">{spans}</div>
                <table class="b105-table">
                    <thead>
                        <tr style="color:{case['color']};">
                            <th>Chữ Hán</th><th>Pinyin</th><th>Nghĩa</th><th>Ghi chú</th>
                        </tr>
                    </thead>
                    <tbody>{rows}</tbody>
                </table>
            </div>
            """, unsafe_allow_html=True)

    with tab_examples:
        st.markdown("### Nhóm giác quan: đẹp, ngon, hay — và ngược lại")
        st.markdown("""
        <div class="b105-pair">
            <div class="b105-pair-title">好 là cảm giác dễ chịu · 难 là cảm giác ngược lại</div>
            <div class="b105-line" style="background:#ecfdf5;border-left:4px solid #059669;">
                <div class="han">这件衣服很好看。</div>
                <div class="meta">Zhè jiàn yīfu hěn hǎokàn. — Áo này rất đẹp.</div>
            </div>
            <div class="b105-line" style="background:#fff1f2;border-left:4px solid #e11d48;">
                <div class="han">这件衣服很难看。</div>
                <div class="meta">Zhè jiàn yīfu hěn nánkàn. — Áo này rất xấu.</div>
            </div>
            <div class="b105-line" style="background:#ecfdf5;border-left:4px solid #059669;">
                <div class="han">这个菜很好吃。</div>
                <div class="meta">Zhège cài hěn hǎochī. — Món này rất ngon.</div>
            </div>
            <div class="b105-line" style="background:#fff1f2;border-left:4px solid #e11d48;">
                <div class="han">这个菜很难吃。</div>
                <div class="meta">Zhège cài hěn nánchī. — Món này rất dở.</div>
            </div>
            <div class="b105-line" style="background:#ecfdf5;border-left:4px solid #059669;">
                <div class="han">绿茶很好喝。</div>
                <div class="meta">Lǜchá hěn hǎohē. — Trà xanh rất ngon.</div>
            </div>
            <div class="b105-line" style="background:#fff1f2;border-left:4px solid #e11d48;">
                <div class="han">这杯水很难喝。</div>
                <div class="meta">Zhè bēi shuǐ hěn nánhē. — Cốc nước này rất dở.</div>
            </div>
            <div class="b105-line" style="background:#ecfdf5;border-left:4px solid #059669;">
                <div class="han">这首歌很好听。</div>
                <div class="meta">Zhè shǒu gē hěn hǎotīng. — Bài hát này rất hay.</div>
            </div>
            <div class="b105-line" style="background:#fff1f2;border-left:4px solid #e11d48;">
                <div class="han">这句话很难听。</div>
                <div class="meta">Zhè jù huà hěn nántīng. — Câu này rất khó nghe.</div>
            </div>
            <div class="b105-line" style="background:#ecfdf5;border-left:4px solid #059669;">
                <div class="han">这朵花很好闻。</div>
                <div class="meta">Zhè duǒ huā hěn hǎowén. — Hoa này rất thơm.</div>
            </div>
            <div class="b105-line" style="background:#fff1f2;border-left:4px solid #e11d48;">
                <div class="han">这个味道很难闻。</div>
                <div class="meta">Zhège wèidào hěn nánwén. — Mùi này rất hôi.</div>
            </div>
            <div class="b105-line" style="background:#ecfdf5;border-left:4px solid #059669;">
                <div class="han">这个游戏很好玩。</div>
                <div class="meta">Zhège yóuxì hěn hǎowán. — Trò này rất vui.</div>
            </div>
            <div class="b105-line" style="background:#fff1f2;border-left:4px solid #e11d48;">
                <div class="han">这个游戏很难玩。</div>
                <div class="meta">Zhège yóuxì hěn nánwán. — Trò này khó chơi.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Nhóm thao tác: dễ làm và khó làm")
        st.markdown("""
        <div class="b105-pair">
            <div class="b105-pair-title">好 là dễ · 难 là khó</div>
            <div class="b105-line" style="background:#eff6ff;border-left:4px solid #2563eb;">
                <div class="han">汉语很好学。</div>
                <div class="meta">Hànyǔ hěn hǎoxué. — Tiếng Hán dễ học.</div>
            </div>
            <div class="b105-line" style="background:#fff7ed;border-left:4px solid #ea580c;">
                <div class="han">这个汉字很难写。</div>
                <div class="meta">Zhège Hànzì hěn nánxiě. — Chữ Hán này khó viết.</div>
            </div>
            <div class="b105-line" style="background:#eff6ff;border-left:4px solid #2563eb;">
                <div class="han">这个手机很好用。</div>
                <div class="meta">Zhège shǒujī hěn hǎoyòng. — Điện thoại này dễ dùng.</div>
            </div>
            <div class="b105-line" style="background:#fff7ed;border-left:4px solid #ea580c;">
                <div class="han">这句话很难懂。</div>
                <div class="meta">Zhè jù huà hěn nándǒng. — Câu này khó hiểu.</div>
            </div>
            <div class="b105-line" style="background:#eff6ff;border-left:4px solid #2563eb;">
                <div class="han">这个名字好记。</div>
                <div class="meta">Zhège míngzi hǎojì. — Tên này dễ nhớ.</div>
            </div>
            <div class="b105-line" style="background:#fff7ed;border-left:4px solid #ea580c;">
                <div class="han">他家很难找。</div>
                <div class="meta">Tā jiā hěn nánzhǎo. — Nhà cậu ấy khó tìm.</div>
            </div>
            <div class="b105-line" style="background:#eff6ff;border-left:4px solid #2563eb;">
                <div class="han">这个字很好写。</div>
                <div class="meta">Zhège zì hěn hǎoxiě. — Chữ này dễ viết.</div>
            </div>
            <div class="b105-line" style="background:#fff7ed;border-left:4px solid #ea580c;">
                <div class="han">这个菜很难做。</div>
                <div class="meta">Zhège cài hěn nánzuò. — Món này khó làm.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_tips:
        st.markdown("""
        <div class="b105-tip">
            <div style="font-weight:800;font-size:1.05rem;color:#713f12;margin-bottom:8px;">Một câu để nhớ</div>
            <div style="font-size:1.15rem;font-weight:800;color:#0f172a;">Nhìn, ăn, nghe → 好 là ngon, đẹp, hay · Làm một việc → 好 là dễ, 难 là khó</div>
        </div>
        """, unsafe_allow_html=True)
        traps = [
            ("Chủ ngữ là vật được nhận xét", "这个菜很好吃。 Món đứng trước. Người ăn không đứng vào chỗ chủ ngữ của mẫu này."),
            ("是, 有, 在, 死 không đi vào mẫu này", "Những động từ này không có mức độ dễ hay khó, cũng không phải cảm nhận khi nhìn, ăn, nghe."),
            ("Phủ định của 好 là 不", "不好吃, 不好看, 不好写. 不 đứng trước cả cụm 好 + động từ."),
        ]
        for title, body in traps:
            st.markdown(f"""
            <div class="b105-trap">
                <div style="font-weight:800;color:#9f1239;margin-bottom:4px;">⚠️ {title}</div>
                <div style="color:#334155;line-height:1.55;">{body}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("""
        <div class="b105-key">
            <div style="font-weight:800;font-size:1.05rem;">Bảng chọn nhanh</div>
            <table>
                <tr><td style="width:42%;font-weight:700;">Muốn nói</td><td>Câu</td></tr>
                <tr><td>Ngon, đẹp, hay, vui</td><td>好吃 · 好看 · 好听 · 好玩</td></tr>
                <tr><td>Dở, xấu, khó nghe, hôi</td><td>难吃 · 难看 · 难听 · 难闻</td></tr>
                <tr><td>Dễ học, dễ viết, dễ tìm</td><td>好学 · 好写 · 好找</td></tr>
                <tr><td>Khó viết, khó hiểu, khó làm</td><td>难写 · 难懂 · 难做</td></tr>
                <tr><td>Không ngon, không đẹp, không dễ viết</td><td>不好吃 · 不好看 · 不好写</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    with tab_quiz:
        st.markdown("Chọn câu hoặc chữ đúng. Nộp bài để xem giải thích.")
        quiz_data = [
            {"q": "“Món này rất ngon.”", "options": ["这个菜很好吃。", "这个菜吃很好。", "这个菜好很吃。"], "answer": "这个菜很好吃。", "explain": "好吃 là ngon. 很 đứng trước cả cụm 好吃."},
            {"q": "“Chữ này khó viết.”", "options": ["这个字很难写。", "这个字写很难。", "这个字难很写。"], "answer": "这个字很难写。", "explain": "Nhóm thao tác: 难 + 写 = khó viết. 难 đứng trước động từ."},
            {"q": "“Áo này không đẹp.”", "options": ["这件衣服不好看。", "这件衣服看不好。", "这件衣服不看好。"], "answer": "这件衣服不好看。", "explain": "Phủ định dùng 不 đứng trước 好看."},
            {"q": "“Áo này rất xấu.”", "options": ["这件衣服很难看。", "这件衣服看很难。", "这件衣服好难看不。"], "answer": "这件衣服很难看。", "explain": "Nhóm giác quan: 难看 là xấu. 难 đứng trước 看."},
            {"q": "“Câu này khó hiểu.”", "options": ["这句话很难懂。", "这句话懂很难。", "这句话好难懂不。"], "answer": "这句话很难懂。", "explain": "难懂 là khó hiểu. 懂 là động từ nhận thức, đứng sau 难."},
            {"q": "Câu nào là phủ định của “ngon”?", "options": ["这个菜不好吃。", "这个菜没好吃。", "这个菜好吃不。"], "answer": "这个菜不好吃。", "explain": "Phủ định của 好 dùng 不: 不好吃."},
            {"q": "Động từ nào không đứng sau 好 theo mẫu này?", "options": ["写", "吃", "是"], "answer": "是", "explain": "是 không có mức độ dễ hay khó, cũng không phải cảm nhận. 写 và 吃 thì dùng được: 好写, 好吃."},
            {"q": "“Chữ này không dễ viết.”", "options": ["这个字不好写。", "这个字好不写。", "这个字不字好写。"], "answer": "这个字不好写。", "explain": "不 đứng trước 好写."},
        ]
        if "b105_submitted" not in st.session_state:
            st.session_state.b105_submitted = False
        if "b105_answers" not in st.session_state:
            st.session_state.b105_answers = {}
        for i, q in enumerate(quiz_data):
            st.markdown(f"""
            <div style="background:white;border:1px solid #e2e8f0;border-radius:14px;padding:18px 22px;margin-bottom:4px;">
                <div style="font-size:1.15rem;font-weight:800;color:#0f172a;">Câu {i+1}. {q['q']}</div>
            </div>
            """, unsafe_allow_html=True)
            key = f"b105_a{i}"
            st.radio(f"Chọn đáp án câu {i+1}:", q["options"], key=key, horizontal=True, disabled=st.session_state.b105_submitted, label_visibility="collapsed")
            if st.session_state.b105_submitted:
                user_ans = st.session_state.b105_answers.get(key)
                if user_ans == q["answer"]:
                    st.success(f"Đúng. {q['explain']}")
                else:
                    st.error(f"Đáp án đúng: **{q['answer']}**. {q['explain']}")
            st.markdown("<br/>", unsafe_allow_html=True)
        col_submit, col_reset = st.columns([1, 1])
        with col_submit:
            if not st.session_state.b105_submitted:
                if st.button("Nộp bài", width="stretch", key="b105_submit", type="primary"):
                    st.session_state.b105_answers = {f"b105_a{i}": st.session_state.get(f"b105_a{i}") for i in range(len(quiz_data))}
                    st.session_state.b105_submitted = True
                    st.rerun()
        with col_reset:
            if st.session_state.b105_submitted:
                if st.button("Làm lại", width="stretch", key="b105_reset"):
                    st.session_state.b105_submitted = False
                    st.session_state.b105_answers = {}
                    for i in range(len(quiz_data)):
                        key = f"b105_a{i}"
                        if key in st.session_state:
                            del st.session_state[key]
                    st.rerun()
        if st.session_state.b105_submitted:
            correct = sum(1 for i, q in enumerate(quiz_data) if st.session_state.b105_answers.get(f"b105_a{i}") == q["answer"])
            total = len(quiz_data)
            pct = int(correct / total * 100)
            if pct == 100:
                msg = "Nắm vững cách dùng 好 và 难 đứng trước động từ."
            elif pct >= 70:
                msg = "Xem lại nhóm giác quan và nhóm dễ hay khó."
            else:
                msg = "Đọc lại phần Lý thuyết rồi làm lại."
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#064e3b,#1e3a8a);color:white;border-radius:16px;padding:28px;text-align:center;margin-top:12px;">
                <div style="font-size:3.2rem;font-weight:900;">{correct}/{total}</div>
                <div>{pct}% đúng</div>
                <div style="margin-top:8px;font-weight:700;">{msg}</div>
            </div>
            """, unsafe_allow_html=True)


def show_lesson10_6_lia():
    st.markdown("""
    <style>
    .b106-hero {
        background: linear-gradient(145deg, #fff7ed, #ffedd5);
        border: 2px solid #fdba74;
        border-radius: 18px;
        padding: 28px 24px;
        text-align: center;
        box-shadow: 0 8px 28px rgba(0,0,0,0.06);
        margin-bottom: 8px;
    }
    .b106-char { font-size: 4.2rem; font-weight: 900; color: #c2410c; line-height: 1.15; }
    .b106-py { font-family: monospace; font-size: 1.45rem; font-weight: 800; color: #9a3412; margin-top: 6px; }
    .b106-tag {
        display: inline-block; margin-top: 10px; background: #fdba74; color: #7c2d12;
        font-weight: 800; padding: 4px 14px; border-radius: 999px;
    }
    .b106-rule {
        background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px;
        padding: 18px 20px; margin-bottom: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    .b106-rule h4 { margin: 0 0 6px 0; }
    .b106-use, .b106-mean { color: #334155; font-size: 0.95rem; line-height: 1.65; margin: 0 0 8px 0; }
    .b106-use b, .b106-mean b { color: #0f172a; }
    .b106-formula {
        background: #1e293b; border-radius: 10px; padding: 12px 18px;
        display: flex; align-items: center; justify-content: center; flex-wrap: wrap; gap: 6px; margin-bottom: 12px;
    }
    .b106-table { width: 100%; border-collapse: collapse; font-size: 0.92rem; }
    .b106-table th { text-align: left; padding: 8px 10px; font-weight: 800; }
    .b106-table td { padding: 8px 10px; border-top: 1px solid #e2e8f0; vertical-align: top; }
    .b106-han { font-size: 1.12rem; font-weight: 800; color: #0f172a; }
    .b106-py2 { font-family: monospace; font-weight: 700; }
    .b106-vi { font-style: italic; color: #475569; }
    .b106-note { color: #64748b; font-size: 0.85rem; }
    .b106-pair { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px; padding: 18px 20px; margin-bottom: 14px; }
    .b106-pair-title { font-weight: 800; color: #0f172a; margin-bottom: 10px; }
    .b106-line { border-radius: 10px; padding: 10px 14px; margin-bottom: 8px; }
    .b106-line .han { font-size: 1.15rem; font-weight: 800; color: #0f172a; }
    .b106-line .meta { font-size: 0.88rem; color: #64748b; }
    .b106-tip { background: linear-gradient(135deg, #fefce8, #fef9c3); border: 2px solid #fde047; border-radius: 16px; padding: 20px 22px; margin-bottom: 14px; }
    .b106-trap { background: #fff1f2; border: 2px solid #fda4af; border-radius: 14px; padding: 14px 16px; margin-bottom: 10px; }
    .b106-key { background: linear-gradient(135deg, #7c2d12, #c2410c); color: white; border-radius: 16px; padding: 20px 22px; margin-top: 16px; }
    .b106-key table { width: 100%; border-collapse: collapse; margin-top: 10px; }
    .b106-key td { padding: 8px 10px; border-top: 1px solid rgba(255,255,255,0.18); vertical-align: top; }
    </style>
    """, unsafe_allow_html=True)

    render_lesson_intro(
        "💬 Bài 36 - Cách dùng 俩 (liǎ)",
        "俩 là cách nói gọn của 两个, dùng cho người. Trong 俩 đã có sẵn 个, nên phía sau không thêm lượng từ."
    )

    tab_theory, tab_examples, tab_tips, tab_quiz = st.tabs([
        "📚 Lý thuyết",
        "📝 Ví dụ đối chiếu",
        "⚠️ Lưu ý & Mẹo nhớ",
        "🎮 Luyện tập"
    ])

    cases = [
        {
            "color": "#c2410c",
            "bg": "#fff7ed",
            "title": "1. Đứng sau đại từ",
            "use": "Đại từ số nhiều chỉ người, rồi thêm <b>俩</b>.",
            "mean": "Đúng hai người trong nhóm đó. <b>我们俩</b> là hai chúng tôi, bằng <b>我们两个人</b>.",
            "formula": [("我们 / 你们 / 他们 / 咱们", "#fdba74"), ("+", "#94a3b8"), ("俩", "#fdba74", True)],
            "rows": [
                ("我们俩。", "Wǒmen liǎ.", "Hai chúng tôi.", "我们两个人"),
                ("你们俩。", "Nǐmen liǎ.", "Hai bạn.", "你们两个人"),
                ("他们俩。", "Tāmen liǎ.", "Hai người họ.", "他们两个人"),
                ("咱们俩。", "Zánmen liǎ.", "Hai chúng ta.", "咱们两个人"),
            ],
        },
        {
            "color": "#2563eb",
            "bg": "#eff6ff",
            "title": "2a. Danh từ chỉ người thường",
            "use": "Danh từ chỉ loại người bình thường, đếm được. <b>俩</b> là <b>两个</b> đã gộp, nên đứng trước danh từ. Không viết <b>个</b> ở giữa. <b>口子</b> cũng đi theo kiểu này: <b>俩口子</b>.",
            "mean": "Hai người thuộc loại đó.",
            "formula": [("俩", "#93c5fd", True), ("+", "#94a3b8"), ("Danh từ chỉ người", "#93c5fd")],
            "rows": [
                ("俩人。", "Liǎ rén.", "Hai người.", "两个人"),
                ("俩学生。", "Liǎ xuésheng.", "Hai học sinh.", "两个学生"),
                ("俩孩子。", "Liǎ háizi.", "Hai đứa trẻ.", "两个孩子"),
                ("俩口子。", "Liǎ kǒuzi.", "Hai vợ chồng.", "Khi nói: liá kǒuzi. Không nói 口子俩"),
            ],
        },
        {
            "color": "#0f766e",
            "bg": "#f0fdfa",
            "title": "2b. Cặp người thân",
            "use": "Danh từ đã là một cặp thân thuộc cố định. <b>俩</b> đứng sau, cùng kiểu với <b>我们俩</b>. Không áp dụng cho người thường: không nói <b>学生俩</b>, <b>孩子俩</b>.",
            "mean": "Đúng hai người trong cặp đó.",
            "formula": [("Cặp người thân", "#5eead4"), ("+", "#94a3b8"), ("俩", "#5eead4", True)],
            "rows": [
                ("兄弟俩。", "Xiōngdì liǎ.", "Hai anh em.", "Cặp thân thuộc + 俩"),
                ("姐妹俩。", "Jiěmèi liǎ.", "Hai chị em.", "俩 đứng sau"),
                ("夫妻俩。", "Fūqī liǎ.", "Hai vợ chồng.", "俩 đứng sau"),
                ("父子俩。", "Fùzǐ liǎ.", "Hai bố con.", "俩 đứng sau"),
                ("母女俩。", "Mǔnǚ liǎ.", "Hai mẹ con.", "俩 đứng sau"),
            ],
        },
    ]

    with tab_theory:
        st.markdown("""
        <div class="b106-hero">
            <div class="b106-char">俩</div>
            <div class="b106-py">liǎ · thanh 3</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br/>", unsafe_allow_html=True)

        for case in cases:
            spans = ""
            for part in case["formula"]:
                text, color = part[0], part[1]
                big = len(part) > 2 and part[2]
                size = "1.7rem" if big else "1.02rem"
                spans += f'<span style="color:{color};font-size:{size};font-weight:800;margin:0 4px;">{text}</span>'
            rows = ""
            for han, py, vi, note in case["rows"]:
                rows += f"""
                <tr>
                    <td class="b106-han">{han}</td>
                    <td class="b106-py2" style="color:{case['color']};">{py}</td>
                    <td class="b106-vi">{vi}</td>
                    <td class="b106-note">{note}</td>
                </tr>"""
            st.markdown(f"""
            <div class="b106-rule" style="border-left:5px solid {case['color']};background:{case['bg']};">
                <h4 style="color:{case['color']};">{case['title']}</h4>
                <p class="b106-use"><b>Cách dùng:</b> {case['use']}</p>
                <p class="b106-mean"><b>Nghĩa:</b> {case['mean']}</p>
                <div class="b106-formula">{spans}</div>
                <table class="b106-table">
                    <thead>
                        <tr style="color:{case['color']};">
                            <th>Chữ Hán</th><th>Pinyin</th><th>Nghĩa</th><th>Ghi chú</th>
                        </tr>
                    </thead>
                    <tbody>{rows}</tbody>
                </table>
            </div>
            """, unsafe_allow_html=True)

    with tab_examples:
        st.markdown("### Cùng một nghĩa, hai cách nói")
        st.markdown("""
        <div class="b106-pair">
            <div class="b106-pair-title">Nói đủ bằng 两个 · nói gọn bằng 俩</div>
            <div class="b106-line" style="background:#f8fafc;border-left:4px solid #64748b;">
                <div class="han">我们两个人。</div>
                <div class="meta">Wǒmen liǎng gè rén. — Hai chúng tôi. <b>Nói đủ.</b></div>
            </div>
            <div class="b106-line" style="background:#fff7ed;border-left:4px solid #c2410c;">
                <div class="han">我们俩。</div>
                <div class="meta">Wǒmen liǎ. — Hai chúng tôi. <b>Nói gọn.</b></div>
            </div>
            <div class="b106-line" style="background:#f8fafc;border-left:4px solid #64748b;">
                <div class="han">两个人。</div>
                <div class="meta">Liǎng gè rén. — Hai người.</div>
            </div>
            <div class="b106-line" style="background:#fff7ed;border-left:4px solid #c2410c;">
                <div class="han">俩人。</div>
                <div class="meta">Liǎ rén. — Hai người.</div>
            </div>
            <div class="b106-line" style="background:#f8fafc;border-left:4px solid #64748b;">
                <div class="han">两个孩子。</div>
                <div class="meta">Liǎng gè háizi. — Hai đứa trẻ.</div>
            </div>
            <div class="b106-line" style="background:#fff7ed;border-left:4px solid #c2410c;">
                <div class="han">俩孩子。</div>
                <div class="meta">Liǎ háizi. — Hai đứa trẻ.</div>
            </div>
            <div class="b106-line" style="background:#f8fafc;border-left:4px solid #64748b;">
                <div class="han">夫妻两个人。</div>
                <div class="meta">Fūqī liǎng gè rén. — Hai vợ chồng.</div>
            </div>
            <div class="b106-line" style="background:#fff7ed;border-left:4px solid #c2410c;">
                <div class="han">夫妻俩。</div>
                <div class="meta">Fūqī liǎ. — Hai vợ chồng.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Đồ vật vẫn dùng 两")
        st.markdown("""
        <div class="b106-pair">
            <div class="b106-pair-title">俩 chỉ người · đồ vật dùng 两 + lượng từ</div>
            <div class="b106-line" style="background:#eff6ff;border-left:4px solid #2563eb;">
                <div class="han">两本书。 · 两个苹果。 · 两杯茶。</div>
                <div class="meta">Liǎng běn shū. · Liǎng gè píngguǒ. · Liǎng bēi chá. — Hai quyển sách, hai quả táo, hai chén trà.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_tips:
        st.markdown("""
        <div class="b106-tip">
            <div style="font-weight:800;font-size:1.05rem;color:#713f12;margin-bottom:8px;">Một câu để nhớ</div>
            <div style="font-size:1.15rem;font-weight:800;color:#0f172a;">俩 = 两个, chỉ người, và 个 đã nằm trong chữ 俩</div>
        </div>
        """, unsafe_allow_html=True)
        traps = [
            ("俩 chỉ người", "Đồ vật vẫn dùng <b>两 + lượng từ</b>: 两本书, 两个苹果, 两杯茶."),
            ("Chọn đúng chỗ của 俩", "Người thường, đang đếm: <b>俩</b> đứng trước — 俩人, 俩学生, 俩孩子, 俩口子. Cặp thân thuộc: <b>俩</b> đứng sau — 兄弟俩, 姐妹俩, 夫妻俩. Không nói 学生俩, không nói 口子俩."),
            ("Không thêm lượng từ sau 俩", "Hai người viết <b>俩人</b> hoặc <b>两个人</b>."),
            ("二, 两, 俩 mỗi chữ một chỗ", "<b>二</b> là chữ số: 十二, 第二. <b>两</b> là số lượng trước lượng từ: 两个人. <b>俩</b> là 两个 đã gộp lại, chỉ người: 我们俩."),
            ("俩口子 khi nói đổi thanh", "口 là thanh 3, nên 俩 nói thành thanh 2: liá kǒuzi. Chữ vẫn viết liǎ."),
            ("Còn một âm liǎng", "Trong từ <b>伎俩</b> (jìliǎng, thủ đoạn), 俩 đọc liǎng. Bài này chỉ học âm liǎ."),
        ]
        for title, body in traps:
            st.markdown(f"""
            <div class="b106-trap">
                <div style="font-weight:800;color:#9f1239;margin-bottom:4px;">⚠️ {title}</div>
                <div style="color:#334155;line-height:1.55;">{body}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("""
        <div class="b106-key">
            <div style="font-weight:800;font-size:1.05rem;">Bảng chọn nhanh</div>
            <table>
                <tr><td style="width:42%;font-weight:700;">Muốn nói</td><td>Câu</td></tr>
                <tr><td>Hai chúng tôi, hai bạn, hai người họ</td><td>我们俩 · 你们俩 · 他们俩</td></tr>
                <tr><td>Hai người, hai học sinh, hai đứa trẻ</td><td>俩人 · 俩学生 · 俩孩子</td></tr>
                <tr><td>Hai anh em, hai chị em, hai vợ chồng</td><td>兄弟俩 · 姐妹俩 · 夫妻俩</td></tr>
                <tr><td>Hai quyển sách, hai quả táo</td><td>两本书 · 两个苹果</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    with tab_quiz:
        st.markdown("Chọn câu hoặc chữ đúng. Nộp bài để xem giải thích.")
        quiz_data = [
            {"q": "“Hai chúng tôi.”", "options": ["我们俩。", "我们两个俩。", "我们二俩。"], "answer": "我们俩。", "explain": "Đại từ số nhiều rồi thêm 俩. 我们俩 = 我们两个人."},
            {"q": "“Hai người.”", "options": ["俩个人。", "俩人。", "二人个。"], "answer": "俩人。", "explain": "俩 đã gồm 个, nên viết 俩人. Muốn nói đủ thì dùng 两个人."},
            {"q": "“Hai quyển sách.”", "options": ["俩书。", "俩本书。", "两本书。"], "answer": "两本书。", "explain": "Sách là đồ vật. Dùng 两 + lượng từ: 两本书."},
            {"q": "兄弟俩 nghĩa là", "options": ["anh em thứ hai", "hai anh em", "hai quyển sách"], "answer": "hai anh em", "explain": "兄弟 là anh em. 俩 đứng sau, nghĩa là hai người trong cặp đó."},
            {"q": "俩口子 khi nói đọc thế nào?", "options": ["liǎ kǒuzi", "liá kǒuzi", "liǎng kǒuzi"], "answer": "liá kǒuzi", "explain": "口 là thanh 3, nên 俩 khi nói đổi thành thanh 2. Chữ vẫn viết liǎ."},
        ]
        if "b106_submitted" not in st.session_state:
            st.session_state.b106_submitted = False
        if "b106_answers" not in st.session_state:
            st.session_state.b106_answers = {}
        for i, q in enumerate(quiz_data):
            st.markdown(f"""
            <div style="background:white;border:1px solid #e2e8f0;border-radius:14px;padding:18px 22px;margin-bottom:4px;">
                <div style="font-size:1.15rem;font-weight:800;color:#0f172a;">Câu {i+1}. {q['q']}</div>
            </div>
            """, unsafe_allow_html=True)
            key = f"b106_a{i}"
            st.radio(f"Chọn đáp án câu {i+1}:", q["options"], key=key, horizontal=True, disabled=st.session_state.b106_submitted, label_visibility="collapsed")
            if st.session_state.b106_submitted:
                user_ans = st.session_state.b106_answers.get(key)
                if user_ans == q["answer"]:
                    st.success(f"Đúng. {q['explain']}")
                else:
                    st.error(f"Đáp án đúng: **{q['answer']}**. {q['explain']}")
            st.markdown("<br/>", unsafe_allow_html=True)
        col_submit, col_reset = st.columns([1, 1])
        with col_submit:
            if not st.session_state.b106_submitted:
                if st.button("Nộp bài", width="stretch", key="b106_submit", type="primary"):
                    st.session_state.b106_answers = {f"b106_a{i}": st.session_state.get(f"b106_a{i}") for i in range(len(quiz_data))}
                    st.session_state.b106_submitted = True
                    st.rerun()
        with col_reset:
            if st.session_state.b106_submitted:
                if st.button("Làm lại", width="stretch", key="b106_reset"):
                    st.session_state.b106_submitted = False
                    st.session_state.b106_answers = {}
                    for i in range(len(quiz_data)):
                        key = f"b106_a{i}"
                        if key in st.session_state:
                            del st.session_state[key]
                    st.rerun()
        if st.session_state.b106_submitted:
            correct = sum(1 for i, q in enumerate(quiz_data) if st.session_state.b106_answers.get(f"b106_a{i}") == q["answer"])
            total = len(quiz_data)
            pct = int(correct / total * 100)
            if pct == 100:
                msg = "Nắm vững cách dùng 俩."
            elif pct >= 70:
                msg = "Xem lại chỗ 俩 chỉ người và không thêm 个."
            else:
                msg = "Đọc lại phần Lý thuyết rồi làm lại."
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#7c2d12,#1e3a8a);color:white;border-radius:16px;padding:28px;text-align:center;margin-top:12px;">
                <div style="font-size:3.2rem;font-weight:900;">{correct}/{total}</div>
                <div>{pct}% đúng</div>
                <div style="margin-top:8px;font-weight:700;">{msg}</div>
            </div>
            """, unsafe_allow_html=True)
