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
        "🧩 Bài 10.2 - Các loại từ",
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
