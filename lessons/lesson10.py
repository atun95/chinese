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
        "💬 Bài 10.1 - Cách dùng 吧 (ba)",
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
