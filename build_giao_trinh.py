# -*- coding: utf-8 -*-
import os
import re

# 1. DANH SÁCH BÀI HỌC (Bạn có thể dễ dàng thêm Bài 7, Bài 8... vào đây)
LESSONS = [
    {
        "title": "Bài 1: Nhập môn Bính âm (Pinyin) & Hệ thống Thanh điệu",
        "toc_desc": "Thanh mẫu b-h, Vận mẫu đơn, 4 Thanh điệu, Biến điệu thanh 3",
        "content_html": """
        <h2 class="section-title">1. Khái quát về hệ thống chữ viết Pinyin</h2>
        <p>Hệ thống phiên âm tiếng Trung tiêu chuẩn (Bính âm - Pinyin) cấu tạo bởi 3 thành phần chính:</p>
        <div style="text-align: center; margin: 15px 0; font-weight: bold; font-size: 16px; letter-spacing: 2px;">
            Thanh mẫu (Phụ âm đầu) + Vận mẫu (Nguyên âm) + Thanh điệu (Dấu)
        </div>
        
        <h2 class="section-title">2. Thanh mẫu cơ bản (11 Phụ âm đầu)</h2>
        <p>Học phát âm chuẩn xác các thanh mẫu nhóm môi, đầu lưỡi và cuống lưỡi:</p>
        <table>
            <thead>
                <tr>
                    <th style="width: 15%;">Thanh mẫu</th>
                    <th style="width: 45%;">Hướng dẫn khẩu hình &amp; Cách phát âm</th>
                    <th style="width: 40%;">Ví dụ từ khóa (Chữ Hán - Pinyin - Việt)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>b</strong></td>
                    <td>Âm hai môi, không bật hơi. Đọc gần giống chữ "p" nhẹ trong tiếng Việt. Mím hai môi rồi mở ra nhẹ nhàng.</td>
                    <td>爸爸 <span class="pinyin">bàba</span> (bố)</td>
                </tr>
                <tr>
                    <td><strong>p</strong></td>
                    <td>Âm hai môi, bật hơi mạnh. Mím môi chặt rồi đẩy một luồng hơi mạnh từ khoang miệng ra ngoài. Giống âm "ph" bật môi.</td>
                    <td>跑步 <span class="pinyin">pǎobù</span> (chạy bộ)</td>
                </tr>
                <tr>
                    <td><strong>m</strong></td>
                    <td>Âm hai môi, âm mũi. Phát âm giống hệt chữ "m" trong tiếng Việt.</td>
                    <td>妈妈 <span class="pinyin">māma</span> (mẹ)</td>
                </tr>
                <tr>
                    <td><strong>f</strong></td>
                    <td>Âm răng môi. Răng trên chạm nhẹ vào môi dưới, đẩy hơi ra ngoài. Phát âm giống chữ "ph" trong tiếng Việt.</td>
                    <td>饭 <span class="pinyin">fàn</span> (cơm)</td>
                </tr>
                <tr>
                    <td><strong>d</strong></td>
                    <td>Âm đầu lưỡi, không bật hơi. Đọc gần giống chữ "t" trong tiếng Việt (đầu lưỡi chạm răng trên rồi hạ xuống).</td>
                    <td>弟弟 <span class="pinyin">dìdi</span> (em trai)</td>
                </tr>
                <tr>
                    <td><strong>t</strong></td>
                    <td>Âm đầu lưỡi, bật hơi mạnh. Đọc gần giống chữ "th" trong tiếng Việt nhưng hơi đẩy ra dứt khoát và mạnh hơn.</td>
                    <td>他 <span class="pinyin">tā</span> (anh ấy)</td>
                </tr>
                <tr>
                    <td><strong>n</strong></td>
                    <td>Âm đầu lưỡi, âm mũi. Phát âm giống hệt chữ "n" trong tiếng Việt.</td>
                    <td>你 <span class="pinyin">nǐ</span> (bạn)</td>
                </tr>
                <tr>
                    <td><strong>l</strong></td>
                    <td>Âm bên đầu lưỡi. Phát âm giống hệt chữ "l" trong tiếng Việt.</td>
                    <td>老师 <span class="pinyin">lǎoshī</span> (giáo viên)</td>
                </tr>
                <tr>
                    <td><strong>g</strong></td>
                    <td>Âm cuống lưỡi, không bật hơi. Đọc gần giống chữ "c" hoặc "k" trong tiếng Việt. Luồng hơi bị chặn lại ở cuống họng.</td>
                    <td>哥哥 <span class="pinyin">gēge</span> (anh trai)</td>
                </tr>
                <tr>
                    <td><strong>k</strong></td>
                    <td>Âm cuống lưỡi, bật hơi mạnh. Đọc gần giống chữ "kh" tiếng Việt nhưng cần đẩy luồng hơi mạnh từ cuống họng ra ngoài.</td>
                    <td>渴 <span class="pinyin">kě</span> (khát)</td>
                </tr>
                <tr>
                    <td><strong>h</strong></td>
                    <td>Âm cuống lưỡi, âm xát. Phát âm hơi nhẹ hơn chữ "h" tiếng Việt một chút, giống như tiếng thở phào nhẹ nhõm.</td>
                    <td>好 <span class="pinyin">hǎo</span> (tốt)</td>
                </tr>
            </tbody>
        </table>

        <h2 class="section-title">3. Vận mẫu đơn cơ bản (6 Nguyên âm đơn)</h2>
        <p>Cách đặt khẩu hình miệng quyết định độ chuẩn xác của nguyên âm:</p>
        <table>
            <thead>
                <tr>
                    <th style="width: 15%;">Vận mẫu</th>
                    <th style="width: 50%;">Hướng dẫn khẩu hình &amp; Cách đọc</th>
                    <th style="width: 35%;">Ví dụ cụ thể</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>a</strong></td>
                    <td>Miệng mở rộng tối đa, lưỡi hạ thấp. Đọc giống chữ "a" trong tiếng Việt.</td>
                    <td>爸 <span class="pinyin">bà</span> (bố)</td>
                </tr>
                <tr>
                    <td><strong>o</strong></td>
                    <td>Môi tròn, miệng hơi khép lại, lưỡi rút về sau. Đọc giống chữ "ô" tiếng Việt.</td>
                    <td>我 <span class="pinyin">wǒ</span> (tôi)</td>
                </tr>
                <tr>
                    <td><strong>e</strong></td>
                    <td>Miệng mở vừa, dẹt sang hai bên. Đọc giống chữ "ơ" hoặc "ưa" trong tiếng Việt.</td>
                    <td>鹅 <span class="pinyin">é</span> (con ngỗng)</td>
                </tr>
                <tr>
                    <td><strong>i</strong></td>
                    <td>Hai môi dẹt, răng khép hờ, lưỡi nâng cao. Đọc giống chữ "i" tiếng Việt.</td>
                    <td>一 <span class="pinyin">yī</span> (số một)</td>
                </tr>
                <tr>
                    <td><strong>u</strong></td>
                    <td>Môi tròn và nhô ra phía trước tối đa. Đọc giống chữ "u" tiếng Việt.</td>
                    <td>五 <span class="pinyin">wǔ</span> (số năm)</td>
                </tr>
                <tr>
                    <td><strong>ü</strong></td>
                    <td>Môi tròn (giống u), lưỡi nâng cao (giống i). Đọc giống âm "uy" nhưng giữ nguyên hình dáng môi tròn suốt quá trình phát âm.</td>
                    <td>绿 <span class="pinyin">lǜ</span> (màu xanh lá)</td>
                </tr>
            </tbody>
        </table>

        <h2 class="section-title">4. Hệ thống Thanh điệu (4 Thanh chính &amp; Thanh nhẹ)</h2>
        <p>Tiếng Trung là ngôn ngữ có thanh điệu. Một âm tiết mang thanh điệu khác nhau sẽ biểu thị ý nghĩa hoàn toàn khác nhau:</p>
        <ul>
            <li><strong>Thanh 1 (Thanh ngang):</strong> Giọng cao, giữ thăng bằng từ đầu đến cuối (ký hiệu: <span class="pinyin">ā</span>). Đọc kéo dài hơi.</li>
            <li><strong>Thanh 2 (Thanh sắc):</strong> Giọng đi từ mức trung bình lên mức cao nhất (ký hiệu: <span class="pinyin">á</span>). Đọc giống dấu sắc tiếng Việt nhưng nhẹ hơn.</li>
            <li><strong>Thanh 3 (Thanh hỏi):</strong> Giọng đi từ thấp xuống cực thấp rồi đi lên trung bình (ký hiệu: <span class="pinyin">ǎ</span>). Đọc giống dấu hỏi kéo dài hơi hoặc đi xuống sâu.</li>
            <li><strong>Thanh 4 (Thanh huyền):</strong> Giọng đi từ mức cao nhất rơi thẳng xuống mức thấp nhất (ký hiệu: <span class="pinyin">à</span>). Đọc dứt khoát, mạnh mẽ, không kéo dài.</li>
            <li><strong>Thanh nhẹ (Neutral Tone):</strong> Không có ký hiệu dấu trên đầu nguyên âm. Đọc cực kỳ nhẹ và ngắn. Ví dụ: <span class="pinyin">māma</span>, <span class="pinyin">bàba</span>.</li>
        </ul>

        <div class="info-box">
            <strong>💡 Quy tắc Biến điệu của Thanh 3 (Sandhi Rule):</strong><br>
            • Khi <strong>hai âm tiết mang thanh 3</strong> đi liền nhau, thanh 3 thứ nhất sẽ biến âm đọc thành thanh 2 (thanh sắc), nhưng cách viết chữ Pinyin vẫn giữ nguyên dấu thanh 3.<br>
            <em>Ví dụ:</em> 你好 <span class="pinyin">nǐ hǎo</span> đọc thực tế là <span class="pinyin">ní hǎo</span>.<br>
            • Khi <strong>ba âm tiết mang thanh 3</strong> đi liền nhau, tùy cấu trúc ngữ nghĩa để biến điệu: biến âm tiết thứ 2 (3-3-3 → 3-2-3) hoặc biến cả hai âm tiết đầu (3-3-3 → 2-2-3).
        </div>

        <h2 class="section-title">5. Từ vựng cốt lõi Bài 1</h2>
        <table>
            <thead>
                <tr>
                    <th style="width: 25%;">Chữ Hán</th>
                    <th style="width: 25%;">Phiên âm Pinyin</th>
                    <th style="width: 30%;">Nghĩa tiếng Việt</th>
                    <th style="width: 20%;">Loại từ</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="hanzi">爸爸</td>
                    <td class="pinyin">bàba</td>
                    <td>bố / ba</td>
                    <td>Danh từ</td>
                </tr>
                <tr>
                    <td class="hanzi">妈妈</td>
                    <td class="pinyin">māma</td>
                    <td>mẹ / má</td>
                    <td>Danh từ</td>
                </tr>
                <tr>
                    <td class="hanzi">哥哥</td>
                    <td class="pinyin">gēge</td>
                    <td>anh trai</td>
                    <td>Danh từ</td>
                </tr>
                <tr>
                    <td class="hanzi">姐姐</td>
                    <td class="pinyin">jiějie</td>
                    <td>chị gái</td>
                    <td>Danh từ</td>
                </tr>
                <tr>
                    <td class="hanzi">弟弟</td>
                    <td class="pinyin">dìdi</td>
                    <td>em trai</td>
                    <td>Danh từ</td>
                </tr>
                <tr>
                    <td class="hanzi">妹妹</td>
                    <td class="pinyin">mèimei</td>
                    <td>em gái</td>
                    <td>Danh từ</td>
                </tr>
                <tr>
                    <td class="hanzi">我</td>
                    <td class="pinyin">wǒ</td>
                    <td>tôi / tớ / mình</td>
                    <td>Đại từ</td>
                </tr>
                <tr>
                    <td class="hanzi">你</td>
                    <td class="pinyin">nǐ</td>
                    <td>bạn / cậu / mày</td>
                    <td>Đại từ</td>
                </tr>
                <tr>
                    <td class="hanzi">他</td>
                    <td class="pinyin">tā</td>
                    <td>anh ấy / ông ấy</td>
                    <td>Đại từ</td>
                </tr>
                <tr>
                    <td class="hanzi">她</td>
                    <td class="pinyin">tā</td>
                    <td>cô ấy / chị ấy</td>
                    <td>Đại từ</td>
                </tr>
                <tr>
                    <td class="hanzi">老师</td>
                    <td class="pinyin">lǎoshī</td>
                    <td>thầy giáo / cô giáo</td>
                    <td>Danh từ</td>
                </tr>
                <tr>
                    <td class="hanzi">学生</td>
                    <td class="pinyin">xuéshēng</td>
                    <td>học sinh / sinh viên</td>
                    <td>Danh từ</td>
                </tr>
                <tr>
                    <td class="hanzi">很</td>
                    <td class="pinyin">hěn</td>
                    <td>rất</td>
                    <td>Phó từ</td>
                </tr>
                <tr>
                    <td class="hanzi">忙</td>
                    <td class="pinyin">máng</td>
                    <td>bạn rộn</td>
                    <td>Tính từ</td>
                </tr>
                <tr>
                    <td class="hanzi">不</td>
                    <td class="pinyin">bù</td>
                    <td>không</td>
                    <td>Phó từ</td>
                </tr>
            </tbody>
        </table>


        """,
        "content_md": """
### 1. Khái quát về hệ thống chữ viết Pinyin
Hệ thống phiên âm tiếng Trung tiêu chuẩn (Bính âm - Pinyin) cấu tạo bởi 3 thành phần chính:
$$\\text{Thanh mẫu (Phụ âm đầu)} + \\text{Vận mẫu (Nguyên âm)} + \\text{Thanh điệu (Dấu)}$$

### 2. Thanh mẫu cơ bản (11 Phụ âm đầu)
*   **b**: Âm hai môi, không bật hơi. Đọc gần giống chữ "p" nhẹ trong tiếng Việt. Mím hai môi rồi mở ra nhẹ nhàng. (Ví dụ: 爸爸 **bàba** - bố)
*   **p**: Âm hai môi, bật hơi mạnh. Mím môi chặt rồi đẩy một luồng hơi mạnh từ khoang miệng ra ngoài. Giống âm "ph" bật môi. (Ví dụ: 跑步 **pǎobù** - chạy bộ)
*   **m**: Âm hai môi, âm mũi. Phát âm giống hệt chữ "m" trong tiếng Việt. (Ví dụ: 妈妈 **māma** - mẹ)
*   **f**: Âm răng môi. Răng trên chạm nhẹ vào môi dưới, đẩy hơi ra ngoài. Phát âm giống chữ "ph" trong tiếng Việt. (Ví dụ: 饭 **fàn** - cơm)
*   **d**: Âm đầu lưỡi, không bật hơi. Đọc gần giống chữ "t" trong tiếng Việt. (Ví dụ: 弟弟 **dìdi** - em trai)
*   **t**: Âm đầu lưỡi, bật hơi mạnh. Đọc gần giống chữ "th" trong tiếng Việt nhưng hơi đẩy ra dứt khoát và mạnh hơn. (Ví dụ: 他 **tā** - anh ấy)
*   **n**: Âm đầu lưỡi, âm mũi. Phát âm giống hệt chữ "n" trong tiếng Việt. (Ví dụ: 你 **nǐ** - bạn)
*   **l**: Âm bên đầu lưỡi. Phát âm giống hệt chữ "l" trong tiếng Việt. (Ví dụ: 老师 **lǎoshī** - giáo viên)
*   **g**: Âm cuống lưỡi, không bật hơi. Đọc gần giống chữ "c" hoặc "k" trong tiếng Việt. (Ví dụ: 哥哥 **gēge** - anh trai)
*   **k**: Âm cuống lưỡi, bật hơi mạnh. Đọc gần giống chữ "kh" tiếng Việt nhưng cần đẩy luồng hơi mạnh từ cuống họng ra ngoài. (Ví dụ: 渴 **kě** - khát)
*   **h**: Âm cuống lưỡi, âm xát. Phát âm hơi nhẹ hơn chữ "h" tiếng Việt một chút, giống như tiếng thở phào nhẹ nhõm. (Ví dụ: 好 **hǎo** - tốt)

### 3. Vận mẫu đơn cơ bản (6 Nguyên âm đơn)
*   **a**: Miệng mở rộng tối đa, lưỡi hạ thấp. Đọc giống chữ "a" trong tiếng Việt. (Ví dụ: 爸 **bà** - bố)
*   **o**: Môi tròn, miệng hơi khép lại, lưỡi rút về sau. Đọc giống chữ "ô" tiếng Việt. (Ví dụ: 我 **wǒ** - tôi)
*   **e**: Miệng mở vừa, dẹt sang hai bên. Đọc giống chữ "ơ" hoặc "ưa" trong tiếng Việt. (Ví dụ: 鹅 **é** - con ngỗng)
*   **i**: Hai môi dẹt, răng khép hờ, lưỡi nâng cao. Đọc giống chữ "i" tiếng Việt. (Ví dụ: 一 **yī** - số một)
*   **u**: Môi tròn và nhô ra phía trước tối đa. Đọc giống chữ "u" tiếng Việt. (Ví dụ: 五 **wǔ** - số năm)
*   **ü**: Môi tròn (giống u), lưỡi nâng cao (giống i). Đọc giống âm "uy" nhưng giữ nguyên hình dáng môi tròn suốt quá trình phát âm. (Ví dụ: 绿 **lǜ** - màu xanh lá)

### 4. Hệ thống Thanh điệu
Tiếng Trung có 4 thanh điệu chính và 1 thanh nhẹ:
*   **Thanh 1 (Thanh ngang - $\\bar{a}$):** Giọng cao, giữ thăng bằng từ đầu đến cuối. Đọc kéo dài hơi.
*   **Thanh 2 (Thanh sắc - $\\acute{a}$):** Giọng đi từ mức trung bình lên mức cao nhất. Đọc giống dấu sắc tiếng Việt nhưng nhẹ hơn.
*   **Thanh 3 (Thanh hỏi - $\\check{a}$):** Giọng đi từ thấp xuống cực thấp rồi đi lên trung bình. Đọc giống dấu hỏi kéo dài.
*   **Thanh 4 (Thanh huyền - $\\grave{a}$):** Giọng đi từ mức cao nhất rơi thẳng xuống mức thấp nhất. Đọc dứt khoát, mạnh mẽ.
*   **Thanh nhẹ (Neutral Tone):** Không có ký hiệu dấu. Đọc cực kỳ nhẹ và ngắn. Thường xuất hiện ở âm tiết thứ hai của từ láy (Ví dụ: **bàba**, **māma**).

> [!NOTE]
> **Quy tắc Biến điệu của Thanh 3:**
> Khi hai âm tiết mang thanh 3 đi liền nhau, thanh 3 thứ nhất sẽ biến âm đọc thành thanh 2 (thanh sắc), nhưng cách viết chữ Pinyin vẫn giữ nguyên dấu thanh 3.
> *Ví dụ:* 你好 **nǐ hǎo** đọc thực tế là **ní hǎo**.

### 5. Từ vựng cốt lõi Bài 1
*   **爸爸 (bàba):** bố / ba (Danh từ)
*   **妈妈 (māma):** mẹ / má (Danh từ)
*   **哥哥 (gēge):** anh trai (Danh từ)
*   **姐姐 (jiějie):** chị gái (Danh từ)
*   **弟弟 (dìdi):** em trai (Danh từ)
*   **妹妹 (mèimei):** em gái (Danh từ)
*   **我 (wǒ):** tôi / tớ / mình (Đại từ)
*   **你 (nǐ):** bạn / cậu / mày (Đại từ)
*   **他 (tā):** anh ấy / ông ấy (Đại từ)
*   **她 (tā):** cô ấy / chị ấy (Đại từ)
*   **老师 (lǎoshī):** thầy giáo / cô giáo (Danh từ)
*   **学生 (xuéshēng):** học sinh / sinh viên (Danh từ)
*   **很 (hěn):** rất (Phó từ)
*   **忙 (máng):** bận rộn (Tính từ)
*   **不 (bù):** không (Phó từ)


        """
    },
    {
        "title": "Bài 2: Vận mẫu kép & Bảng Ghép âm cơ bản",
        "toc_desc": "Vận mẫu kép (ai, ei, ao, ou), Bảng ghép âm tổng hợp",
        "content_html": """
        <h2 class="section-title">1. Vận mẫu kép cơ bản (ai, ei, ao, ou)</h2>
        <p>Vận mẫu kép là sự kết hợp của nhiều nguyên âm đơn. Khi phát âm, khẩu hình trượt mượt mà từ âm thứ nhất sang âm thứ hai:</p>
        <table>
            <thead>
                <tr>
                    <th style="width: 15%;">Vận mẫu</th>
                    <th style="width: 50%;">Hướng dẫn khẩu hình &amp; Cách đọc</th>
                    <th style="width: 35%;">Ví dụ cụ thể</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>ai</strong></td>
                    <td>Miệng mở rộng phát âm nguyên âm /a/, sau đó chuyển nhanh khẩu hình sang dẹt và khép nhẹ ở /i/. Phát âm giống chữ "ai" tiếng Việt.</td>
                    <td>来 <span class="pinyin">lái</span> (đến/lại)</td>
                </tr>
                <tr>
                    <td><strong>ei</strong></td>
                    <td>Miệng mở hé phát âm nguyên âm /e/, sau đó trượt nhanh sang âm /i/. Đọc gần giống chữ "ây" trong tiếng Việt.</td>
                    <td>内 <span class="pinyin">nèi</span> (ở trong)</td>
                </tr>
                <tr>
                    <td><strong>ao</strong></td>
                    <td>Miệng mở rộng bắt đầu từ /a/, trượt mượt mà thu tròn môi lại kết thúc ở âm /o/. Đọc giống chữ "ao" tiếng Việt.</td>
                    <td>宝贝 <span class="pinyin">bǎobèi</span> (bảo bối)</td>
                </tr>
                <tr>
                    <td><strong>ou</strong></td>
                    <td>Môi tròn vừa phát âm /o/, nhanh chóng thu tròn môi nhỏ lại kết thúc ở âm /u/. Đọc giống chữ "âu" trong tiếng Việt.</td>
                    <td>狗 <span class="pinyin">gǒu</span> (con chó)</td>
                </tr>
            </tbody>
        </table>

        <h2 class="section-title">2. Bảng Ghép âm cơ bản (Thanh mẫu + Vận mẫu đơn &amp; kép)</h2>
        <p>Học viên hãy dùng bút luyện tập đánh vần từng ô giao nhau của thanh mẫu và vận mẫu bên dưới. Những ô trống biểu thị sự kết hợp âm không tồn tại trong tiếng Trung tiêu chuẩn.</p>
        <table style="text-align: center;">
            <thead>
                <tr style="background-color: #f1f5f9;">
                    <th style="text-align: center;">Pinyin</th>
                    <th style="text-align: center;">a</th>
                    <th style="text-align: center;">o</th>
                    <th style="text-align: center;">e</th>
                    <th style="text-align: center;">i</th>
                    <th style="text-align: center;">u</th>
                    <th style="text-align: center;">ü</th>
                    <th style="text-align: center;">ai</th>
                    <th style="text-align: center;">ei</th>
                    <th style="text-align: center;">ao</th>
                    <th style="text-align: center;">ou</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>b</strong></td>
                    <td>ba</td>
                    <td>bo</td>
                    <td>-</td>
                    <td>bi</td>
                    <td>bu</td>
                    <td>-</td>
                    <td>bai</td>
                    <td>bei</td>
                    <td>bao</td>
                    <td>-</td>
                </tr>
                <tr>
                    <td><strong>p</strong></td>
                    <td>pa</td>
                    <td>po</td>
                    <td>-</td>
                    <td>pi</td>
                    <td>pu</td>
                    <td>-</td>
                    <td>pai</td>
                    <td>pei</td>
                    <td>pao</td>
                    <td>pou</td>
                </tr>
                <tr>
                    <td><strong>m</strong></td>
                    <td>ma</td>
                    <td>mo</td>
                    <td>me</td>
                    <td>mi</td>
                    <td>mu</td>
                    <td>-</td>
                    <td>mai</td>
                    <td>mei</td>
                    <td>mao</td>
                    <td>mou</td>
                </tr>
                <tr>
                    <td><strong>f</strong></td>
                    <td>fa</td>
                    <td>fo</td>
                    <td>-</td>
                    <td>-</td>
                    <td>fu</td>
                    <td>-</td>
                    <td>-</td>
                    <td>fei</td>
                    <td>-</td>
                    <td>fou</td>
                </tr>
                <tr>
                    <td><strong>d</strong></td>
                    <td>da</td>
                    <td>-</td>
                    <td>de</td>
                    <td>di</td>
                    <td>du</td>
                    <td>-</td>
                    <td>dai</td>
                    <td>dei</td>
                    <td>dao</td>
                    <td>dou</td>
                </tr>
                <tr>
                    <td><strong>t</strong></td>
                    <td>ta</td>
                    <td>-</td>
                    <td>te</td>
                    <td>ti</td>
                    <td>tu</td>
                    <td>-</td>
                    <td>tai</td>
                    <td>-</td>
                    <td>tao</td>
                    <td>tou</td>
                </tr>
                <tr>
                    <td><strong>n</strong></td>
                    <td>na</td>
                    <td>-</td>
                    <td>ne</td>
                    <td>ni</td>
                    <td>nu</td>
                    <td>nü</td>
                    <td>nai</td>
                    <td>nei</td>
                    <td>nao</td>
                    <td>nou</td>
                </tr>
                <tr>
                    <td><strong>l</strong></td>
                    <td>la</td>
                    <td>-</td>
                    <td>le</td>
                    <td>li</td>
                    <td>lu</td>
                    <td>lü</td>
                    <td>lai</td>
                    <td>lei</td>
                    <td>lao</td>
                    <td>lou</td>
                </tr>
                <tr>
                    <td><strong>g</strong></td>
                    <td>ga</td>
                    <td>-</td>
                    <td>ge</td>
                    <td>-</td>
                    <td>gu</td>
                    <td>-</td>
                    <td>gai</td>
                    <td>gei</td>
                    <td>gao</td>
                    <td>gou</td>
                </tr>
                <tr>
                    <td><strong>k</strong></td>
                    <td>ka</td>
                    <td>-</td>
                    <td>ke</td>
                    <td>-</td>
                    <td>ku</td>
                    <td>-</td>
                    <td>kai</td>
                    <td>kei</td>
                    <td>kao</td>
                    <td>kou</td>
                </tr>
                <tr>
                    <td><strong>h</strong></td>
                    <td>ha</td>
                    <td>-</td>
                    <td>he</td>
                    <td>-</td>
                    <td>hu</td>
                    <td>-</td>
                    <td>hai</td>
                    <td>hei</td>
                    <td>hao</td>
                    <td>hou</td>
                </tr>
            </tbody>
        </table>


        """,
        "content_md": """
### 1. Vận mẫu kép cơ bản (ai, ei, ao, ou)
*   **ai**: Miệng mở rộng phát âm nguyên âm /a/, sau đó chuyển nhanh khẩu hình sang dẹt và khép nhẹ ở /i/. Phát âm giống chữ "ai" tiếng Việt. (Ví dụ: 来 **lái** - đến)
*   **ei**: Miệng mở hé phát âm nguyên âm /e/, sau đó trượt nhanh sang âm /i/. Đọc gần giống chữ "ây" trong tiếng Việt. (Ví dụ: 内 **nèi** - ở trong)
*   **ao**: Miệng mở rộng bắt đầu từ /a/, trượt mượt mà thu tròn môi lại kết thúc ở âm /o/. Đọc giống chữ "ao" tiếng Việt. (Ví dụ: 宝贝 **bǎobèi** - bảo bối)
*   **ou**: Môi tròn vừa phát âm /o/, nhanh chóng thu tròn môi nhỏ lại kết thúc ở âm /u/. Đọc giống chữ "âu" trong tiếng Việt. (Ví dụ: 狗 **gǒu** - con chó)

### 2. Bảng Ghép âm cơ bản (Thanh mẫu + Vận mẫu đơn & kép)

| Pinyin | a | o | e | i | u | ü | ai | ei | ao | ou |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **b** | ba | bo | - | bi | bu | - | bai | bei | bao | - |
| **p** | pa | po | - | pi | pu | - | pai | pei | pao | pou |
| **m** | ma | mo | me | mi | mu | - | mai | mei | mao | mou |
| **f** | fa | fo | - | - | fu | - | - | fei | - | fou |
| **d** | da | - | de | di | du | - | dai | dei | dao | dou |
| **t** | ta | - | te | ti | tu | - | tai | - | tao | tou |
| **n** | na | - | ne | ni | nu | nü | nai | nei | nao | nou |
| **l** | la | - | le | li | lu | lü | lai | lei | lao | lou |
| **g** | ga | - | ge | - | gu | - | gai | gei | gao | gou |
| **k** | ka | - | ke | - | ku | - | kai | kei | kao | kou |
| **h** | ha | - | he | - | hu | - | hai | hei | hao | hou |


        """
    },
    {
        "title": "Bài 3: Thanh mẫu Nâng cao & Cấu trúc Ngữ pháp Cốt lõi",
        "toc_desc": "j-x, zh-r, z-s, Biến điệu \"Bù\", Động từ \"Shì\" & \"Yǒu\", Cách gọi tên",
        "content_html": """
        <h2 class="section-title">1. Hệ thống Thanh mẫu Nâng cao (10 Phụ âm &amp; 2 Âm đệm)</h2>
        <table>
            <thead>
                <tr>
                    <th style="width: 25%;">Nhóm thanh mẫu</th>
                    <th style="width: 15%;">Ký hiệu</th>
                    <th style="width: 60%;">Đặc điểm cấu âm &amp; Hướng dẫn phát âm</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td rowspan="3"><strong>Nhóm mặt lưỡi</strong><br>(Không đi với u, o)</td>
                    <td><strong>j</strong></td>
                    <td>Không bật hơi. Mặt lưỡi áp sát ngạc cứng, đẩy hơi nhẹ ra ngoài. Đọc giống chữ "ch" tiếng Việt nhưng dẹt môi sang hai bên.</td>
                </tr>
                <tr>
                    <td><strong>q</strong></td>
                    <td>Bật hơi mạnh. Vị trí đặt lưỡi giống hệt "j" nhưng cần nén hơi lại và đẩy ra một luồng hơi cực mạnh làm rung giấy.</td>
                </tr>
                <tr>
                    <td><strong>x</strong></td>
                    <td>Âm xát. Mặt lưỡi gần sát ngạc cứng, để hơi thoát ra ngoài tự nhiên qua khe lưỡi. Phát âm nhẹ giống chữ "x" tiếng Việt.</td>
                </tr>
                <tr>
                    <td rowspan="4"><strong>Nhóm uốn lưỡi</strong><br>(Uốn đầu lưỡi ngược lên ngạc cứng)</td>
                    <td><strong>zh</strong></td>
                    <td>Không bật hơi. Đầu lưỡi uốn ngược chạm ngạc cứng, chặn hơi rồi thả nhẹ cho hơi thoát ra. Đọc giống chữ "tr" uốn lưỡi nặng.</td>
                </tr>
                <tr>
                    <td><strong>ch</strong></td>
                    <td>Bật hơi mạnh. Vị trí giống "zh" nhưng bật hơi mạnh từ cuống họng.</td>
                </tr>
                <tr>
                    <td><strong>sh</strong></td>
                    <td>Âm xát uốn lưỡi. Uốn lưỡi lên sát ngạc trên (không chạm hẳn), để hơi xát đi ra ngoài. Đọc giống chữ "s" uốn lưỡi rất nặng.</td>
                </tr>
                <tr>
                    <td><strong>r</strong></td>
                    <td>Âm uốn lưỡi có rung dây thanh. Khẩu hình giống "sh" nhưng có độ rung của cổ họng. Phát âm gần giống chữ "r" tiếng Việt.</td>
                </tr>
                <tr>
                    <td rowspan="3"><strong>Nhóm đầu lưỡi - răng</strong><br>(Lưỡi thẳng chạm mặt sau răng trên)</td>
                    <td><strong>z</strong></td>
                    <td>Không bật hơi. Đầu lưỡi thẳng chạm mặt sau răng trên, chặn hơi rồi hé nhẹ ra. Đọc gần giống chữ "ch" tiếng Việt nhưng lưỡi thẳng.</td>
                </tr>
                <tr>
                    <td><strong>c</strong></td>
                    <td>Bật hơi mạnh. Khẩu hình và vị trí lưỡi giống "z" nhưng đẩy hơi bật thật mạnh ra ngoài qua khe răng khép hờ.</td>
                </tr>
                <tr>
                    <td><strong>s</strong></td>
                    <td>Âm xát đầu lưỡi. Lưỡi thẳng để hở khe nhỏ với răng trên, đẩy hơi xát nhẹ ra ngoài. Đọc giống chữ "s" thẳng lưỡi (xì nhẹ).</td>
                </tr>
                <tr>
                    <td rowspan="2"><strong>Ký hiệu bán nguyên âm</strong></td>
                    <td><strong>y</strong></td>
                    <td>Biểu diễn cho nguyên âm đệm <strong>i</strong> khi âm tiết không có phụ âm đầu đi kèm.</td>
                </tr>
                <tr>
                    <td><strong>w</strong></td>
                    <td>Biểu diễn cho nguyên âm đệm <strong>u</strong> khi âm tiết không có phụ âm đầu đi kèm.</td>
                </tr>
            </tbody>
        </table>

        <div class="warn-box">
            <strong>⚠️ Quy tắc Phát âm Vận mẫu "i" đặc biệt:</strong><br>
            • Khi nguyên âm <strong>i</strong> đi sau các thanh mẫu uốn lưỡi và đầu lưỡi răng (<strong>zh, ch, sh, r, z, c, s</strong>), nó bắt buộc phải đọc biến thành âm <strong>"ư"</strong> của tiếng Việt. Ví dụ: 是 <span class="pinyin">shì</span> (đọc là "sư"), 四 <span class="pinyin">sì</span> (đọc là "sư"), 吃 <span class="pinyin">chī</span> (đọc là "chư").<br>
            • Khi <strong>i</strong> đi sau các thanh mẫu khác (như <strong>b, p, m, d, t, n, l, j, q, x</strong>), nó vẫn đọc là âm <strong>"i"</strong> như tiếng Việt. Ví dụ: 你 <span class="pinyin">nǐ</span> (ni), 七 <span class="pinyin">qī</span> (chi).
        </div>

        <h2 class="section-title">2. Quy tắc chính tả đối với i, u, ü khi đứng độc lập</h2>
        <p>Khi các vận mẫu đứng một mình tạo thành âm tiết độc lập, dạng viết Bính âm của chúng phải thay đổi như sau:</p>
        <ul>
            <li><strong>Nhóm i:</strong> i → <span class="spelling-highlight">yi</span>, ia → <span class="spelling-highlight">ya</span>, ie → <span class="spelling-highlight">ye</span>, iu → <span class="spelling-highlight">you</span>.</li>
            <li><strong>Nhóm u:</strong> u → <span class="spelling-highlight">wu</span>, ua → <span class="spelling-highlight">wa</span>, uo → <span class="spelling-highlight">wo</span>, ui → <span class="spelling-highlight">wei</span>.</li>
            <li><strong>Nhóm ü:</strong> ü → <span class="spelling-highlight">yu</span>, üe → <span class="spelling-highlight">yue</span>, üan → <span class="spelling-highlight">yuan</span>, ün → <span class="spelling-highlight">yun</span> (Lược bỏ hai dấu chấm trên đầu chữ ü).</li>
        </ul>

        <div class="info-box">
            <strong>💡 Quy tắc Lược bỏ Dấu hai chấm trên đầu chữ "ü":</strong><br>
            • Khi <strong>ü</strong> đi sau các thanh mẫu mặt lưỡi <strong>j, q, x</strong> và bán nguyên âm <strong>y</strong>, ta bỏ hai dấu chấm trên đầu, viết là <strong>ju, qu, xu, yu</strong> nhưng vẫn giữ nguyên cách đọc tròn môi là <strong>jü, qü, xü, yü</strong>.<br>
            • Khi <strong>ü</strong> đi sau hai thanh mẫu đầu lưỡi <strong>n, l</strong>, ta <strong>bắt buộc phải giữ nguyên hai dấu chấm</strong> (viết là <strong>nü, lü</strong>) để phân biệt rõ với âm đi với u thường (<strong>nu, lu</strong>).
        </div>

        <h2 class="section-title">3. Quy tắc Biến điệu của phó từ phủ định "不" (bù)</h2>
        <p>Phó từ phủ định <strong>不 (bù)</strong> mang thanh 4 gốc. Tuy nhiên cách đọc thay đổi tùy theo thanh điệu của từ tiếp sau nó:</p>
        <ol>
            <li><strong>Giữ nguyên thanh 4 (bù):</strong> Khi đứng trước các từ mang <strong>Thanh 1, Thanh 2, Thanh 3</strong>.<br>
                <em>Ví dụ:</em> 不忙 <span class="pinyin">bù máng</span> (không bận), 不好 <span class="pinyin">bù hǎo</span> (không tốt), 不吃 <span class="pinyin">bù chī</span> (không ăn).
            </li>
            <li><strong>Biến âm đọc thành thanh 2 (bú):</strong> Khi đứng trước các từ mang <strong>Thanh 4</strong>.<br>
                <em>Ví dụ:</em> 不是 <span class="pinyin">bù shì</span> → đọc là <span class="pinyin">bú shì</span> (không phải); 不累 <span class="pinyin">bù lèi</span> → đọc là <span class="pinyin">bú lèi</span> (không mệt).
            </li>
        </ol>

        <h2 class="section-title">4. Cấu trúc Ngữ pháp Cốt lõi: So sánh Động từ "是" (shì) &amp; "有" (yǒu)</h2>
        <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
            <thead>
                <tr style="background-color: #f1f5f9;">
                    <th style="width: 50%; font-size: 15px; text-align: center; padding: 12px; font-weight: bold; color: var(--primary-color);">Động từ "是" (shì - Là)</th>
                    <th style="width: 50%; font-size: 15px; text-align: center; padding: 12px; font-weight: bold; color: var(--primary-color);">Động từ "有" (yǒu - Có)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="vertical-align: top; padding: 15px;">
                        <p style="margin-bottom: 8px;"><strong>Ý nghĩa:</strong> Biểu thị quan hệ tương đương giữa chủ ngữ và vị ngữ danh từ (định danh, giới thiệu).</p>
                        <ul style="margin-left: 20px;">
                            <li><strong>Khẳng định:</strong> <code style="color: #1e3a8a; font-weight: bold;">S + 是 + O</code><br><em>Ví dụ:</em> 我是老师。<span class="pinyin">(Wǒ shì lǎoshī.)</span> - Tôi là giáo viên.</li>
                            <li><strong>Phủ định:</strong> <code style="color: #b91c1c; font-weight: bold;">S + 不是 + O</code><br><em>Ví dụ:</em> 他不是学生。<span class="pinyin">(Tā bú shì xuéshēng.)</span> - Anh ấy không phải học sinh.</li>
                            <li><strong>Nghi vấn:</strong> <code style="color: #0f766e; font-weight: bold;">S + 是 + O + 吗？</code><br><em>Ví dụ:</em> 你是学生吗？<span class="pinyin">(Nǐ shì xuéshēng ma?)</span> - Bạn là học sinh phải không?</li>
                        </ul>
                    </td>
                    <td style="vertical-align: top; padding: 15px;">
                        <p style="margin-bottom: 8px;"><strong>Ý nghĩa:</strong> Biểu thị sự sở hữu vật chất, mối quan hệ xã hội hoặc sự tồn tại.</p>
                        <ul style="margin-left: 20px;">
                            <li><strong>Khẳng định:</strong> <code style="color: #1e3a8a; font-weight: bold;">S + 有 + O</code><br><em>Ví dụ:</em> 我有朋友。<span class="pinyin">(Wǒ yǒu péngyou.)</span> - Tôi có bạn bè.</li>
                            <li><strong>Phủ định:</strong> <code style="color: #b91c1c; font-weight: bold;">S + 没有 + O</code><br><em>Ví dụ:</em> 他没有女朋友。<span class="pinyin">(Tā méiyǒu nǚpéngyou.)</span> - Anh ấy không có bạn gái.</li>
                            <li><strong>Nghi vấn:</strong> <code style="color: #0f766e; font-weight: bold;">S + 有 + O + 吗？</code><br><em>Ví dụ:</em> 你有男朋友吗？<span class="pinyin">(Nǐ yǒu nánpéngyou ma?)</span> - Bạn có bạn trai không?</li>
                        </ul>
                    </td>
                </tr>
            </tbody>
        </table>

        <h2 class="section-title">5. Từ vựng cốt lõi Bài 3 &amp; Văn hóa gọi tên</h2>
        <table>
            <thead>
                <tr>
                    <th style="width: 25%;">Chữ Hán / Phiên âm</th>
                    <th style="width: 30%;">Nghĩa tiếng Việt</th>
                    <th style="width: 20%;">Chữ Hán / Phiên âm</th>
                    <th style="width: 25%;">Nghĩa tiếng Việt</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="hanzi">律师 <span class="pinyin">lǜshī</span></td>
                    <td>luật sư</td>
                    <td class="hanzi">名字 <span class="pinyin">míngzi</span></td>
                    <td>tên</td>
                </tr>
                <tr>
                    <td class="hanzi">朋友 <span class="pinyin">péngyou</span></td>
                    <td>bạn bè</td>
                    <td class="hanzi">高兴 <span class="pinyin">gāoxìng</span></td>
                    <td>vui mừng / vui vẻ</td>
                </tr>
                <tr>
                    <td class="hanzi">男朋友 <span class="pinyin">nánpéngyou</span></td>
                    <td>bạn trai</td>
                    <td class="hanzi">认识 <span class="pinyin">rènshi</span></td>
                    <td>quen biết / nhận biết</td>
                </tr>
                <tr>
                    <td class="hanzi">女朋友 <span class="pinyin">nǚpéngyou</span></td>
                    <td>bạn gái</td>
                    <td class="hanzi">叫 <span class="pinyin">jiào</span></td>
                    <td>gọi / gọi là</td>
                </tr>
            </tbody>
        </table>
        
        <p style="margin-top: 10px;"><strong>💡 Văn hóa gọi tên trong giao tiếp đời thường:</strong><br>
        Người Trung Quốc thường gọi nhau bằng các cách thân mật: ghép tiền tố <strong>阿 (ā)</strong> hoặc <strong>小 (xiǎo)</strong> trước tên (Ví dụ: 小薇 Xiǎo Wēi - Tiểu Vy, ...). Khi gọi người lớn tuổi hoặc cấp trên thân mật, ghép tiền tố <strong>老 (lǎo)</strong> trước họ (Ví dụ: 老张 Lǎo Zhāng - Lão Trương).</p>


        """,
        "content_md": """
### 1. Hệ thống Thanh mẫu Nâng cao
*   **Nhóm mặt lưỡi (j, q, x):** Không bật hơi ở **j** (đọc giống "ch" dẹt môi); bật hơi cực mạnh ở **q**; âm xát nhẹ ở **x** (giống "x" tiếng Việt).
*   **Nhóm uốn lưỡi (zh, ch, sh, r):** Uốn đầu lưỡi chạm ngạc cứng. Không bật hơi ở **zh** (đọc "tr" uốn lưỡi nặng); bật hơi cực mạnh ở **ch**; âm xát uốn lưỡi ở **sh** (giống "s" uốn lưỡi); âm rung uốn lưỡi ở **r** (giống "r" tiếng Việt).
*   **Nhóm đầu lưỡi - răng (z, c, s):** Lưỡi thẳng chạm mặt sau răng trên. Không bật hơi ở **z** (đọc giống "ch" lưỡi thẳng); bật hơi cực mạnh ở **c** (đẩy hơi mạnh qua khe răng); âm xát đầu lưỡi ở **s** (xì nhẹ thẳng lưỡi).

> [!WARNING]
> **Quy tắc Phát âm Vận mẫu "i" đặc biệt:**
> *   Khi nguyên âm **i** đi sau các thanh mẫu **zh, ch, sh, r, z, c, s**, nó bắt buộc phải phát âm biến thành âm **"ư"** (Ví dụ: 是 **shì** đọc là "sư", 四 **sì** đọc là "sư").
> *   Khi **i** đi sau các thanh mẫu khác, nó vẫn phát âm là âm **"i"** (Ví dụ: 你 **nǐ** đọc là "ni").

### 2. Quy tắc chính tả đứng độc lập và lược dấu chấm ü
*   **Đứng độc lập:** i → **yi**, ia → **ya**, ie → **ye**, iu → **you**, u → **wu**, ua → **wa**, uo → **wo**, ui → **wei**, ü → **yu**, üe → **yue**, üan → **yuan**, ün → **yun**.
*   **Lược dấu hai chấm của ü:** Khi **ü** đi sau **j, q, x, y**, ta bỏ hai dấu chấm trên đầu, viết là **ju, qu, xu, yu** nhưng vẫn đọc tròn môi là **jü, qü, xü, yü**. Đi sau **n, l** phải giữ nguyên dấu chấm để phân biệt (nü, lü).

### 3. Quy tắc Biến điệu của phó từ "不" (bù)
*   **Giữ nguyên thanh 4 (bù):** Khi đi trước từ mang Thanh 1, Thanh 2, Thanh 3. (Ví dụ: 不忙 **bù máng**)
*   **Đổi thành thanh 2 (bú):** Khi đi trước từ mang Thanh 4. (Ví dụ: 不是 **bú shì**)

### 4. So sánh Động từ "是" (shì - Là) & "有" (yǒu - Có)

| Động từ "是" (shì - Là) | Động từ "有" (yǒu - Có) |
| :--- | :--- |
| **Ý nghĩa:** Định danh, biểu thị quan hệ tương đương.<br>**Khẳng định:** S + 是 + O<br>*Ví dụ:* 我是老师 (Tôi là giáo viên).<br>**Phủ định:** S + 不是 + O<br>*Ví dụ:* 他tên不是学生 (Anh ấy không phải học sinh).<br>**Nghi vấn:** S + 是 + O + 吗？<br>*Ví dụ:* 你sẽ学生吗？ (Bạn là học sinh phải không?) | **Ý nghĩa:** Biểu thị sự sở hữu hoặc mối quan hệ.<br>**Khẳng định:** S + 有 + O<br>*Ví dụ:* 我有朋友 (Tôi có bạn bè).<br>**Phủ định:** S + 没有 + O<br>*Ví dụ:* 他没有女朋友 (Anh ấy không có bạn gái).<br>**Nghi vấn:** S + 有 + O + 吗？<br>*Ví dụ:* 你有男朋友吗？ (Bạn có bạn trai không?) |

### 5. Từ vựng cốt lõi Bài 3
*   **律师 (lǜshī):** luật sư (Danh từ)
*   **朋友 (péngyou):** bạn bè (Danh từ)
*   **男朋友 (nánpéngyou):** bạn trai (Danh từ)
*   **女朋友 (nǚpéngyou):** bạn gái (Danh từ)
*   **名字 (míngzi):** tên (Danh từ)
*   **高兴 (gāoxìng):** vui mừng, vui vẻ (Tính từ)
*   **认识 (rènshi):** quen biết (Động từ)
*   **叫 (jiào):** gọi là (Động từ)
        """
    },
    {
        "title": "Bài 4: Vận mẫu kép Mở rộng & Từ vựng chỉ Nữ giới",
        "toc_desc": "9 Vận mẫu kép mới, Viết gọn iu/ui, Chuyên đề 7 từ vựng chỉ Nữ giới",
        "content_html": """
        <h2 class="section-title">1. Vận mẫu kép mở rộng (9 Nguyên âm phức)</h2>
        <p>Chi tiết cách phát âm và quy tắc biến đổi chính tả của 9 vận mẫu kép phức hợp:</p>
        <table>
            <thead>
                <tr>
                    <th style="width: 12%;">Vận mẫu</th>
                    <th style="width: 48%;">Hướng dẫn cấu âm chi tiết</th>
                    <th style="width: 20%;">Viết độc lập</th>
                    <th style="width: 20%;">Ví dụ cụ thể</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>ia</strong></td>
                    <td>Đọc nguyên âm /i/ làm âm đệm rồi mở rộng miệng phát âm /a/ thật nhanh. Giống âm "ia" tiếng Việt.</td>
                    <td><strong>ya</strong></td>
                    <td>家 <span class="pinyin">jiā</span> (nhà)</td>
                </tr>
                <tr>
                    <td><strong>ie</strong></td>
                    <td>Đọc âm /i/ rồi trượt nhanh hạ lưỡi phát âm âm /ê/. Giống âm "iê" tiếng Việt.</td>
                    <td><strong>ye</strong></td>
                    <td>姐姐 <span class="pinyin">jiějie</span> (chị)</td>
                </tr>
                <tr>
                    <td><strong>iao</strong></td>
                    <td>Bắt đầu từ /i/, trượt mượt sang /a/ rộng rồi thu tròn môi ở /o/. Giống âm "i-ao" viết lướt.</td>
                    <td><strong>yao</strong></td>
                    <td>小 <span class="pinyin">xiǎo</span> (nhỏ)</td>
                </tr>
                <tr>
                    <td><strong>iu</strong></td>
                    <td>Cách viết rút gọn của <strong>iou</strong>. Đọc âm /i/ trượt nhanh sang âm /ou/ (âu). Giống âm "yêu" tiếng Việt.</td>
                    <td><strong>you</strong></td>
                    <td>六 <span class="pinyin">liù</span> (sáu)</td>
                </tr>
                <tr>
                    <td><strong>ua</strong></td>
                    <td>Tròn môi phát âm /u/ làm đệm, mở nhanh sang /a/. Giống âm "oa" tiếng Việt.</td>
                    <td><strong>wa</strong></td>
                    <td>花 <span class="pinyin">huā</span> (hoa)</td>
                </tr>
                <tr>
                    <td><strong>uo</strong></td>
                    <td>Tròn môi phát âm /u/ làm đệm, chuyển nhanh sang /o/ (ô). Giống âm "uô" tiếng Việt.</td>
                    <td><strong>wo</strong></td>
                    <td>我 <span class="pinyin">wǒ</span> (tôi)</td>
                </tr>
                <tr>
                    <td><strong>uai</strong></td>
                    <td>Tròn môi phát âm /u/ làm đệm, trượt sang /a/ rồi kết thúc ở /i/. Giống âm "oai" tiếng Việt.</td>
                    <td><strong>wai</strong></td>
                    <td>外 <span class="pinyin">wài</span> (bên ngoài)</td>
                </tr>
                <tr>
                    <td><strong>ui</strong></td>
                    <td>Cách viết rút gọn của <strong>uei</strong>. Đọc âm /u/ làm đệm trượt nhanh sang /ei/. Giống âm "uây" tiếng Việt.</td>
                    <td><strong>wei</strong></td>
                    <td>水 <span class="pinyin">shuǐ</span> (nước)</td>
                </tr>
                <tr>
                    <td><strong>üe</strong></td>
                    <td>Giữ tròn môi của âm /ü/, trượt nhanh mở miệng sang âm /e/ (ê). Giống âm "uyê" tiếng Việt.</td>
                    <td><strong>yue</strong></td>
                    <td>月 <span class="pinyin">yuè</span> (tháng)</td>
                </tr>
            </tbody>
        </table>

        <div class="info-box">
            <strong>💡 Quy tắc Rút gọn Chính tả cực kỳ quan trọng:</strong><br>
            • Vận mẫu <strong>iou</strong> khi đi kèm với thanh mẫu phía trước bắt buộc phải viết rút gọn thành <strong>iu</strong> (ví dụ: <span class="pinyin">jiǔ</span> - số 9). Khi đứng độc lập, viết đầy đủ dạng gốc là <span class="pinyin">you</span>.<br>
            • Vận mẫu <strong>uei</strong> khi đi kèm với thanh mẫu phía trước bắt buộc viết rút gọn thành <strong>ui</strong> (ví dụ: <span class="pinyin">shuǐ</span> - nước). Khi đứng độc lập, viết đầy đủ dạng gốc là <span class="pinyin">wei</span>.
        </div>

        <h2 class="section-title">2. Chuyên đề từ vựng: Phân biệt 7 từ vựng chỉ Nữ giới</h2>
        <p>Trong tiếng Trung có nhiều từ cùng dịch là "phụ nữ, con gái, nữ giới" nhưng có sắc thái và hoàn cảnh sử dụng khác nhau:</p>
        <table>
            <thead>
                <tr>
                    <th style="width: 15%;">Từ vựng</th>
                    <th style="width: 12%;">Pinyin</th>
                    <th style="width: 18%;">Độ tuổi gợi ý</th>
                    <th style="width: 18%;">Sắc thái / Ngữ cảnh</th>
                    <th style="width: 37%;">Đặc điểm và Ví dụ cụ thể</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="hanzi">女人</td>
                    <td class="pinyin">nǚrén</td>
                    <td>Trên 18 tuổi</td>
                    <td>Khẩu ngữ đời sống</td>
                    <td>Chỉ phụ nữ trưởng thành nói chung. Đối lập với 男人.<br><em>Ví dụ:</em> 她是一个好女人 (Cô ấy là một người phụ nữ tốt).</td>
                </tr>
                <tr>
                    <td class="hanzi">女孩</td>
                    <td class="pinyin">nǚhái</td>
                    <td>Dưới 20 tuổi</td>
                    <td>Thân mật, trẻ trung</td>
                    <td>Bé gái hoặc thiếu nữ chưa chồng. Đối lập với 男孩.<br><em>Ví dụ:</em> 那个女孩很可爱 (Cô bé đó rất đáng yêu).</td>
                </tr>
                <tr>
                    <td class="hanzi">女儿</td>
                    <td class="pinyin">nǚ'ér</td>
                    <td>Mọi lứa tuổi</td>
                    <td>Quan hệ gia đình</td>
                    <td>Con gái ruột (trong mối quan hệ với bố mẹ). Đối lập với 儿子.<br><em>Ví dụ:</em> 她是 my 女儿 (Cô ấy là con gái tôi).</td>
                </tr>
                <tr>
                    <td class="hanzi">女生</td>
                    <td class="pinyin">nǚshēng</td>
                    <td>12 - 30 tuổi</td>
                    <td>Giới trẻ, học đường</td>
                    <td>Nguyên gốc là nữ sinh. Nay dùng rộng rãi chỉ các cô gái trẻ tuổi.<br><em>Ví dụ:</em> 那个女生很漂亮 (Bạn nữ kia rất xinh đẹp).</td>
                </tr>
                <tr>
                    <td class="hanzi">女性</td>
                    <td class="pinyin">nǚxìng</td>
                    <td>Mọi lứa tuổi</td>
                    <td>Trang trọng, báo chí</td>
                    <td>Chỉ giới tính sinh học (nữ giới) trong văn bản khoa học, pháp lý.<br><em>Ví dụ:</em> 这里的女性 很多 (Nữ giới ở đây rất nhiều).</td>
                </tr>
                <tr>
                    <td class="hanzi">女子</td>
                    <td class="pinyin">nǚzǐ</td>
                    <td>Mọi lứa tuổi</td>
                    <td>Trang trọng, thể thao</td>
                    <td>Xuất hiện trong các giải đấu thể thao hoặc tiêu đề trang trọng.<br><em>Ví dụ:</em> 女子单打 (Đơn nữ quần vợt).</td>
                </tr>
                <tr>
                    <td class="hanzi">妇女</td>
                    <td class="pinyin">fùnǚ</td>
                    <td>Trên 25-30 tuổi</td>
                    <td>Chính trị, pháp luật</td>
                    <td>Phụ nữ trưởng thành, đã kết hôn hoặc trung niên.<br><em>Ví dụ:</em> 三八妇女节 (Ngày quốc tế phụ nữ 8/3).</td>
                </tr>
            </tbody>
        </table>


        """,
        "content_md": """
### 1. Vận mẫu kép mở rộng (9 Nguyên âm phức)
*   **ia (ya)**: Đọc i đệm rồi mở miệng sang a. (Ví dụ: 家 **jiā** - nhà)
*   **ie (ye)**: Đọc i đệm rồi trượt sang ê. (Ví dụ: 姐姐 **jiějie** - chị)
*   **iao (yao)**: Đọc i-a-o liền mạch. (Ví dụ: 小 **xiǎo** - nhỏ)
*   **iu (you)**: Viết gọn của *iou*. Đọc i sang ou. (Ví dụ: 六 **liù** - số sáu)
*   **ua (wa)**: Tròn môi u đệm mở sang a. (Ví dụ: 花 **huā** - hoa)
*   **uo (wo)**: Tròn môi u đệm mở sang o. (Ví dụ: 我 **wǒ** - tôi)
*   **uai (wai)**: Tròn môi u đệm trượt sang ai. (Ví dụ: 外 **wài** - bên ngoài)
*   **ui (wei)**: Viết gọn của *uei*. Đọc u đệm sang ei. (Ví dụ: 水 **shuǐ** - nước)
*   **üe (yue)**: Tròn môi ü đệm trượt sang ê. (Ví dụ: 月 **yuè** - tháng)

### 2. Chuyên đề phân biệt 7 từ vựng chỉ Nữ giới
1.  **女人 (nǚrén - Phụ nữ/Đàn bà):** Chỉ phụ nữ trưởng thành chung chung trong khẩu ngữ đời sống. (Trái nghĩa: 男人)
2.  **女孩 (nǚhái - Cô bé/Thiếu nữ):** Bé gái hoặc cô gái trẻ chưa chồng, mang sắc thái đáng yêu, trẻ trung. (Trái nghĩa: 男孩)
3.  **女儿 (nǚ'ér - Con gái ruột):** Dùng duy nhất biểu thị quan hệ huyết thống gia đình với bố mẹ. (Trái nghĩa: 儿子)
4.  **女生 (nǚshēng - Bạn nữ/Cô gái trẻ):** Học sinh/sinh viên nữ hoặc dùng gọi lịch sự các cô gái trẻ tuổi. (Trái nghĩa: 男生)
5.  **女性 (nǚxìng - Nữ giới/Phái nữ):** Từ trang trọng chỉ giới tính trong nghiên cứu, y khoa, báo chí. (Trái nghĩa: 男性)
6.  **女子 (nǚzǐ - Nữ/Nữ tử):** Mang sắc thái trang trọng, văn viết, phổ biến trong các hạng mục thể thao.
7.  **妇女 (fùnǚ - Phụ nữ trung niên):** Phụ nữ đã kết hôn hoặc trung niên (25-30 tuổi trở lên), dùng trong văn bản pháp luật, chính trị.
        """
    },
    {
        "title": "Bài 5: Số đếm, Vận mẫu mũi trước/sau & Ngữ pháp Mức độ",
        "toc_desc": "Số đếm 0-10, Biến điệu \"Yī\", Phân biệt èr/liǎng, Âm mũi, Tết Đoan Ngọ",
        "content_html": """
        <h2 class="section-title">1. Số đếm tiếng Trung cơ bản &amp; Ký hiệu số lớn</h2>
        <p>Học đếm số từ 0 đến 10 kèm các đơn vị số lớn:</p>
        <table>
            <thead>
                <tr>
                    <th style="width: 10%;">Số</th>
                    <th style="width: 15%;">Chữ Hán</th>
                    <th style="width: 15%;">Pinyin</th>
                    <th style="width: 20%;">Số lớn</th>
                    <th style="width: 15%;">Chữ Hán</th>
                    <th style="width: 25%;">Nghĩa Việt</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>0</td>
                    <td class="hanzi">零</td>
                    <td class="pinyin">líng</td>
                    <td>100</td>
                    <td class="hanzi">一百</td>
                    <td class="pinyin">yī bǎi (Một trăm)</td>
                </tr>
                <tr>
                    <td>1</td>
                    <td class="hanzi">一</td>
                    <td class="pinyin">yī</td>
                    <td>1.000</td>
                    <td class="hanzi">一千</td>
                    <td class="pinyin">yī qiān (Một nghìn)</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td class="hanzi">二 / 两</td>
                    <td class="pinyin">èr / liǎng</td>
                    <td>10.000</td>
                    <td class="hanzi">一万</td>
                    <td class="pinyin">yī wàn (Mười nghìn/1 vạn)</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td class="hanzi">三</td>
                    <td class="pinyin">sān</td>
                    <td>100.000</td>
                    <td class="hanzi">十万</td>
                    <td class="pinyin">shí wàn (Một trăm nghìn)</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td class="hanzi">四</td>
                    <td class="pinyin">sì</td>
                    <td>1.000.000</td>
                    <td class="hanzi">一百万</td>
                    <td class="pinyin">yī bǎi wàn (Một triệu)</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td class="hanzi">五</td>
                    <td class="pinyin">wǔ</td>
                    <td>10.000.000</td>
                    <td class="hanzi">一千万</td>
                    <td class="pinyin">yī qiān wàn (Mười triệu)</td>
                </tr>
                <tr>
                    <td>6</td>
                    <td class="hanzi">六</td>
                    <td class="pinyin">liù</td>
                    <td>100.000.000</td>
                    <td class="hanzi">一亿</td>
                    <td class="pinyin">yī yì (Một trăm triệu)</td>
                </tr>
                <tr>
                    <td>7</td>
                    <td class="hanzi">七</td>
                    <td class="pinyin">qī</td>
                    <td>1.000.000.000</td>
                    <td class="hanzi">十亿</td>
                    <td class="pinyin">shí yì (Một tỷ)</td>
                </tr>
                <tr>
                    <td>8</td>
                    <td class="hanzi">八</td>
                    <td class="pinyin">bā</td>
                    <td colspan="3" rowspan="3" style="background-color:#f1f5f9; text-align:center; font-weight:bold; font-size:12px;">
                        💡 Biến điệu của "一" (yī):<br>
                        • Đọc <span class="pinyin">yī</span> khi đứng lẻ, đọc số thứ tự.<br>
                        • Đọc <span class="pinyin">yì</span> trước thanh 1, 2, 3 (yì bǎi, yì qiān).<br>
                        • Đọc <span class="pinyin">yí</span> trước thanh 4 (yí wàn, yí yì).
                    </td>
                </tr>
                <tr>
                    <td>9</td>
                    <td class="hanzi">九</td>
                    <td class="pinyin">jiǔ</td>
                </tr>
                <tr>
                    <td>10</td>
                    <td class="hanzi">十</td>
                    <td class="pinyin">shí</td>
                </tr>
            </tbody>
        </table>

        <div class="info-box">
            <strong>⚖️ Phân biệt cách dùng số 2: 二 (èr) và 两 (liǎng):</strong><br>
            • Dùng <strong>二 (èr)</strong> khi: đếm số thuần túy (yī, èr, sān...), đọc số thứ tự (第二), số phòng, số điện thoại, số đứng ở hàng chục và hàng đơn vị (十二).<br>
            • Dùng <strong>两 (liǎng)</strong> khi: đứng trực tiếp trước <strong>lượng từ</strong> để chỉ số lượng người/vật (2 người, 2 bánh ú). Hoặc đứng trước các đơn vị số lớn từ hàng trăm trở lên (两百 - 200, 两千 - 2000).
        </div>

        <h2 class="section-title">2. Vận mẫu mũi trước (-n) và mũi sau (-ng)</h2>
        <p>Vận mẫu mũi được chia làm 2 nhóm chính dựa vào vị trí kết thúc luồng hơi:</p>
        <ul>
            <li><strong>Nhóm mũi trước (-n): an, en, in.</strong> Khi kết thúc âm, đầu lưỡi bắt buộc nâng lên chạm nhẹ vào nướu răng cửa hàm trên (khép âm lại bằng âm /n/).</li>
            <li><strong>Nhóm mũi sau (-ng): ang, eng, ing, ong.</strong> Khi kết thúc âm, gốc lưỡi hạ thấp tự do, cuống lưỡi thụt về sau chạm ngạc mềm chặn hơi. Âm vang lên ở hốc mũi.</li>
        </ul>

        <h2 class="section-title">3. Ngữ pháp: Phó từ chỉ mức độ trong câu vị ngữ tính từ</h2>
        <p>Trong tiếng Trung, câu khẳng định có tính từ làm vị ngữ có cấu trúc đặc trưng:</p>
        <div style="text-align: center; font-size: 16px; font-weight: bold; margin: 10px 0;">
            Chủ ngữ (S) + Phó từ mức độ + Tính từ (Adj)
        </div>

        <p><strong>Bảng phân cấp các phó từ chỉ mức độ thường gặp:</strong></p>
        <table>
            <thead>
                <tr>
                    <th style="width: 25%;">Cấp độ mức độ</th>
                    <th style="width: 20%;">Phó từ / Cấu trúc</th>
                    <th style="width: 25%;">Công thức câu</th>
                    <th style="width: 30%;">Ví dụ cụ thể</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Tương đối / Khá</td>
                    <td>比较 <span class="pinyin">bǐjiào</span></td>
                    <td>S + 比较 + Adj</td>
                    <td>汉语比较难 (Tiếng Trung tương đối khó)</td>
                </tr>
                <tr>
                    <td>Khá là (Văn nói)</td>
                    <td>挺...的 <span class="pinyin">tǐng...de</span></td>
                    <td>S + 挺 + Adj + 的</td>
                    <td>他挺好的 (Anh ấy khá là tốt)</td>
                </tr>
                <tr>
                    <td>Bình thường / Rất</td>
                    <td>很 <span class="pinyin">hěn</span></td>
                    <td>S + 很 + Adj</td>
                    <td>我很忙 (Tôi bận / Tôi rất bận)</td>
                </tr>
                <tr>
                    <td>Đặc biệt</td>
                    <td>特别 <span class="pinyin">tèbié</span></td>
                    <td>S + 特别 + Adj</td>
                    <td>汉语特别有趣 (Tiếng Trung đặc biệt thú vị)</td>
                </tr>
                <tr>
                    <td>Vô cùng / Cực kỳ</td>
                    <td>非常 <span class="pinyin">fēicháng</span></td>
                    <td>S + 非常 + Adj</td>
                    <td>她非常漂亮 (Cô ấy vô cùng xinh đẹp)</td>
                </tr>
                <tr>
                    <td>Quá / Lắm (Cảm thán)</td>
                    <td>太...了 <span class="pinyin">tài...le</span></td>
                    <td>S + 太 + Adj + 了</td>
                    <td>今天太热了 (Hôm nay nóng quá rồi!)</td>
                </tr>
                <tr>
                    <td>Cực kỳ (Đứng sau)</td>
                    <td>极了 <span class="pinyin">jí le</span></td>
                    <td>S + Adj + 极了</td>
                    <td>累极了 (Mệt cực kỳ)</td>
                </tr>
            </tbody>
        </table>

        <h2 class="section-title">4. Chuyên đề Văn hóa: Tết Đoan Ngọ (端午节 - Duānwǔ Jié)</h2>
        <p>Tết Đoan Ngọ diễn ra vào ngày mùng 5 tháng 5 Âm lịch. Tại Trung Quốc, ngày lễ này mang tính tưởng niệm sâu sắc đối với nhà thơ yêu nước vĩ đại <strong>Khuất Nguyên (屈原)</strong> nước Sở thời Chiến Quốc.</p>


        """,
        "content_md": """
### 1. Số đếm và Biến điệu của "一" (yī)
*   **Số đếm 0 - 10:** 0 **零 líng**, 1 **一 yī**, 2 **二 èr / 两 liǎng**, 3 **三 sān**, 4 **四 sì**, 5 **五 wǔ**, 6 **六 liù**, 7 **七 qī**, 8 **八 bā**, 9 **九 jiǔ**, 10 **十 shí**.
*   **Đơn vị số lớn:** 100 **一百 yī bǎi**, 1000 **一千 yī qiān**, 10.000 **一万 yī wàn**, 100.000.000 **一亿 yī yì**.
*   **Biến điệu của "一" (yī):**
    *   Giữ nguyên thanh 1 (yī): Khi đứng lẻ, đọc số thứ tự.
    *   Đổi thành thanh 4 (yì): Khi đi trước từ mang Thanh 1, 2, 3 (Ví dụ: **yì bǎi**, **yì qiān**).
    *   Đổi thành thanh 2 (yí): Khi đi trước từ mang Thanh 4 (Ví dụ: **yí wàn**, **yí yì**).

> [!IMPORTANT]
> **Phân biệt 二 (èr) và 两 (liǎng):**
> *   Dùng **二 (èr)** khi đếm số, số thứ tự, số nhà, số phòng.
> *   Dùng **两 (liǎng)** khi đứng trước lượng từ chỉ số lượng người/vật (Ví dụ: 两个人 - hai người) hoặc đơn vị số lớn (两百).

### 2. Vận mẫu mũi trước (-n) và mũi sau (-ng)
*   **Mũi trước (-n): an, en, in.** Đầu lưỡi chạm ngạc trên khép âm lại. (Ví dụ: **fàn** - cơm, **hěn** - rất)
*   **Mũi sau (-ng): ang, eng, ing, ong.** Gốc lưỡi hạ thấp chặn hơi ở sau, hơi đi ra mũi. (Ví dụ: **máng** - bận, **péng** - bạn bè)

### 3. Ngữ pháp: Phó từ chỉ mức độ
Trong câu khẳng định vị ngữ tính từ (S + Adj), bắt buộc phải có phó từ mức độ **很 (hěn)** đi kèm làm liên kết ngữ pháp.
*   **Các phó từ mức độ theo cấp độ:**
    *   Tương đối, khá: 比较 **bǐjiào**, 挺...de **tǐng...de**
    *   Rất: 很 **hěn**
    *   Đặc biệt: 特別 **tèbié**
    *   Vô cùng: 非常 **fēicháng**
    *   Quá, lắm: 太...了 **tài...le**
    *   Cực kỳ: 极了 **jí le**

### 4. Chuyên đề Văn hóa: Tết Đoan Ngọ (端午节 - Duānwǔ Jié)
Tết Đoan Ngọ diễn ra vào ngày mùng 5 tháng 5 Âm lịch. Tại Trung Quốc, ngày lễ này mang tính tưởng niệm sâu sắc đối với nhà thơ yêu nước vĩ đại Khuất Nguyên (屈原) nước Sở thời Chiến Quốc. Khi nước Sở mất nước, ông ôm đá tự vẫn dưới sông Mịch La. Người dân đi thuyền ra cứu và ném bánh tro (bánh ú - 粽子) xuống sông để cá không ăn xác ông. Đây cũng là nguồn gốc phong tục Đua thuyền rồng (赛龙舟).


"""
    },
    {
        "title": "Bài 6: Vận mẫu mũi phức hợp & Bảng quy tắc biến đổi chính tả",
        "toc_desc": "8 Vận mẫu mũi mới, Quy tắc viết đứng độc lập y/w, Lược dấu chấm ü",
        "content_html": """
        <h2 class="section-title">1. Vận mẫu mũi phức hợp (8 Nguyên âm mũi phức)</h2>
        <p>Các vận mẫu mũi phức hợp bắt đầu bằng âm đệm nguyên âm hẹp (i, u, ü) kết thúc bằng phụ âm mũi (-n hoặc -ng):</p>
        <table>
            <thead>
                <tr>
                    <th style="width: 15%;">Vận mẫu</th>
                    <th style="width: 45%;">Hướng dẫn khẩu hình &amp; Cách đọc</th>
                    <th style="width: 20%;">Viết độc lập</th>
                    <th style="width: 20%;">Ví dụ cụ thể</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>ian</strong></td>
                    <td>Đọc âm /i/ rồi trượt nhanh sang âm /an/. Đọc giống âm "yên" tiếng Việt.</td>
                    <td><strong>yan</strong></td>
                    <td>烟 <span class="pinyin">yān</span> (khói)</td>
                </tr>
                <tr>
                    <td><strong>iang</strong></td>
                    <td>Đọc âm /i/ rồi trượt nhanh sang âm /ang/. Đọc giống âm "yang" tiếng Việt.</td>
                    <td><strong>yang</strong></td>
                    <td>羊 <span class="pinyin">yáng</span> (con dê)</td>
                </tr>
                <tr>
                    <td><strong>iong</strong></td>
                    <td>Đọc âm /i/ rồi trượt nhanh sang âm /ong/. Đọc giống âm "y-ông" tiếng Việt.</td>
                    <td><strong>yong</strong></td>
                    <td>用 <span class="pinyin">yòng</span> (dùng)</td>
                </tr>
                <tr>
                    <td><strong>uan</strong></td>
                    <td>Tròn môi phát âm /u/ làm đệm, chuyển nhanh sang /an/. Đọc giống âm "oan" tiếng Việt.</td>
                    <td><strong>wan</strong></td>
                    <td>玩 <span class="pinyin">wán</span> (chơi)</td>
                </tr>
                <tr>
                    <td><strong>uang</strong></td>
                    <td>Tròn môi phát âm /u/ làm đệm, chuyển nhanh sang /ang/. Đọc giống âm "oang" tiếng Việt.</td>
                    <td><strong>wang</strong></td>
                    <td>王 <span class="pinyin">wáng</span> (vua)</td>
                </tr>
                <tr>
                    <td><strong>un</strong></td>
                    <td>Cách viết rút gọn của <strong>uen</strong>. Đọc âm /u/ trượt sang /ên/. Đọc giống âm "uân" tiếng Việt.</td>
                    <td><strong>wen</strong></td>
                    <td>问 <span class="pinyin">wèn</span> (hỏi)</td>
                </tr>
                <tr>
                    <td><strong>ün</strong></td>
                    <td>Tròn môi phát âm /ü/, kết thúc ở âm /n/ (lưỡi chạm răng trên). Đọc giống âm "uyn".</td>
                    <td><strong>yun</strong></td>
                    <td>云 <span class="pinyin">yún</span> (mây)</td>
                </tr>
                <tr>
                    <td><strong>üan</strong></td>
                    <td>Tròn môi phát âm /ü/, kết thúc ở âm /an/. Đọc giống âm "uyên" tiếng Việt.</td>
                    <td><strong>yuan</strong></td>
                    <td>元 <span class="pinyin">yuán</span> (đồng tệ)</td>
                </tr>
            </tbody>
        </table>

        <h2 class="section-title">2. Quy tắc chính tả Pinyin tối quan trọng (Tổng ôn toàn khóa)</h2>
        <div class="warn-box">
            <strong>🌟 Quy tắc 1: Khi nguyên âm đứng một mình làm thành âm tiết (Không đi với thanh mẫu)</strong><br>
            • Các vận mẫu bắt đầu bằng <strong>i</strong> sẽ chuyển chữ <strong>i</strong> thành <strong>y</strong> (hoặc thêm y ở trước đối với i, in, ing).<br>
            • Các vận mẫu bắt đầu bằng <strong>u</strong> sẽ chuyển chữ <strong>u</strong> thành <strong>w</strong> (hoặc thêm w ở trước đối với u).<br>
            • Các vận mẫu bắt đầu bằng <strong>ü</strong> sẽ thêm chữ <strong>y</strong> đứng trước và lược bỏ hai dấu chấm trên đầu chữ ü.
        </div>

        <h3 style="margin-top: 15px; font-size: 14.5px; color: var(--primary-color);">📌 Nhóm 1: Các vận mẫu bắt đầu bằng 'i'</h3>
        <table>
            <thead>
                <tr>
                    <th style="width: 25%;">Vận mẫu gốc</th>
                    <th style="width: 25%;">Khi viết độc lập</th>
                    <th style="width: 25%;">Ví dụ cụ thể</th>
                    <th style="width: 25%;">Nghĩa tiếng Việt</th>
                </tr>
            </thead>
            <tbody>
                <tr><td><strong>i</strong></td><td><span class="pinyin">yi</span></td><td>一 <span class="pinyin">yī</span></td><td>số một</td></tr>
                <tr><td><strong>ia</strong></td><td><span class="pinyin">ya</span></td><td>鸭 <span class="pinyin">yā</span></td><td>con vịt</td></tr>
                <tr><td><strong>iao</strong></td><td><span class="pinyin">yao</span></td><td>药 <span class="pinyin">yào</span></td><td>thuốc</td></tr>
                <tr><td><strong>ian</strong></td><td><span class="pinyin">yan</span></td><td>言 <span class="pinyin">yán</span></td><td>ngôn ngữ / lời nói</td></tr>
                <tr><td><strong>iang</strong></td><td><span class="pinyin">yang</span></td><td>羊 <span class="pinyin">yáng</span></td><td>con dê</td></tr>
                <tr><td><strong>ie</strong></td><td><span class="pinyin">ye</span></td><td>爷 <span class="pinyin">yé</span></td><td>ông nội</td></tr>
                <tr><td><strong>iou</strong></td><td><span class="pinyin">you</span></td><td>有 <span class="pinyin">yǒu</span></td><td>có</td></tr>
                <tr><td><strong>iong</strong></td><td><span class="pinyin">yong</span></td><td>用 <span class="pinyin">yòng</span></td><td>sử dụng / dùng</td></tr>
                <tr><td><strong>in</strong></td><td><span class="pinyin">yin</span></td><td>音 <span class="pinyin">yīn</span></td><td>âm thanh</td></tr>
                <tr><td><strong>ing</strong></td><td><span class="pinyin">ying</span></td><td>影 <span class="pinyin">yǐng</span></td><td>ảnh / phim</td></tr>
            </tbody>
        </table>

        <h3 style="margin-top: 15px; font-size: 14.5px; color: var(--primary-color);">📌 Nhóm 2: Các vận mẫu bắt đầu bằng 'u'</h3>
        <table>
            <thead>
                <tr>
                    <th style="width: 25%;">Vận mẫu gốc</th>
                    <th style="width: 25%;">Khi viết độc lập</th>
                    <th style="width: 25%;">Ví dụ cụ thể</th>
                    <th style="width: 25%;">Nghĩa tiếng Việt</th>
                </tr>
            </thead>
            <tbody>
                <tr><td><strong>u</strong></td><td><span class="pinyin">wu</span></td><td>五 <span class="pinyin">wǔ</span></td><td>số năm</td></tr>
                <tr><td><strong>ua</strong></td><td><span class="pinyin">wa</span></td><td>娃 <span class="pinyin">wá</span></td><td>em bé / búp bê</td></tr>
                <tr><td><strong>uai</strong></td><td><span class="pinyin">wai</span></td><td>外 <span class="pinyin">wài</span></td><td>bên ngoài</td></tr>
                <tr><td><strong>uan</strong></td><td><span class="pinyin">wan</span></td><td>玩 <span class="pinyin">wán</span></td><td>chơi / đùa</td></tr>
                <tr><td><strong>uang</strong></td><td><span class="pinyin">wang</span></td><td>王 <span class="pinyin">wáng</span></td><td>vua / họ Vương</td></tr>
                <tr><td><strong>uo</strong></td><td><span class="pinyin">wo</span></td><td>我 <span class="pinyin">wǒ</span></td><td>tôi / ta</td></tr>
                <tr><td><strong>uei</strong></td><td><span class="pinyin">wei</span></td><td>喂 <span class="pinyin">wèi</span></td><td>alo (nghe điện thoại)</td></tr>
                <tr><td><strong>uen</strong></td><td><span class="pinyin">wen</span></td><td>问 <span class="pinyin">wèn</span></td><td>hỏi</td></tr>
                <tr><td><strong>ueng</strong></td><td><span class="pinyin">weng</span></td><td>翁 <span class="pinyin">wēng</span></td><td>ông già</td></tr>
            </tbody>
        </table>

        <h3 style="margin-top: 15px; font-size: 14.5px; color: var(--primary-color);">📌 Nhóm 3: Các vận mẫu bắt đầu bằng 'ü'</h3>
        <table>
            <thead>
                <tr>
                    <th style="width: 25%;">Vận mẫu gốc</th>
                    <th style="width: 25%;">Khi viết độc lập</th>
                    <th style="width: 25%;">Ví dụ cụ thể</th>
                    <th style="width: 25%;">Nghĩa tiếng Việt</th>
                </tr>
            </thead>
            <tbody>
                <tr><td><strong>ü</strong></td><td><span class="pinyin">yu</span></td><td>鱼 <span class="pinyin">yú</span></td><td>con cá (đọc tròn môi 'uy')</td></tr>
                <tr><td><strong>üe</strong></td><td><span class="pinyin">yue</span></td><td>月 <span class="pinyin">yuè</span></td><td>mặt trăng / tháng (đọc tròn môi 'uyê')</td></tr>
                <tr><td><strong>üan</strong></td><td><span class="pinyin">yuan</span></td><td>元 <span class="pinyin">yuán</span></td><td>đồng tệ (đọc tròn môi 'uyên')</td></tr>
                <tr><td><strong>ün</strong></td><td><span class="pinyin">yun</span></td><td>云 <span class="pinyin">yún</span></td><td>mây / đám mây (đọc tròn môi 'uyn')</td></tr>
            </tbody>
        </table>

        <div class="info-box">
            <strong>🌟 Quy tắc 2: Lược bỏ hai dấu chấm của nguyên âm "ü" sau j, q, x</strong><br>
            Khi các vận mẫu tròn môi như <strong>ün</strong> và <strong>üan</strong> kết hợp với thanh mẫu mặt lưỡi <strong>j, q, x</strong>, chúng ta bắt buộc lược bỏ hai dấu chấm trên đầu chữ ü.<br>
            • j + ün → <strong>jun</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • q + ün → <strong>qun</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • x + ün → <strong>xun</strong><br>
            • j + üan → <strong>juan</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • q + üan → <strong>quan</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • x + üan → <strong>xuan</strong>
        </div>


        """,
        "content_md": """
### 1. Vận mẫu mũi phức hợp (8 Nguyên âm mũi phức)
*   **ian (yan)**: Đọc i đệm trượt sang an (đọc giống "yên").
*   **iang (yang)**: Đọc i đệm trượt sang ang (đọc giống "yang").
*   **iong (yong)**: Đọc i đệm trượt sang ong.
*   **uan (wan)**: Tròn môi u đệm trượt sang an.
*   **uang (wang)**: Tròn môi u đệm trượt sang ang.
*   **un (wen)**: Viết gọn của *uen*. Đọc u đệm sang ên (đọc giống "uân").
*   **ün (yun)**: Tròn môi ü đệm kết thúc ở n (đọc giống "uyn").
*   **üan (yuan)**: Tròn môi ü đệm trượt sang an (đọc giống "uyên").

### 2. Tổng hợp 2 Quy tắc chính tả Pinyin cuối khóa
*   **Quy tắc 1: Khi nguyên âm đứng một mình tạo thành âm tiết độc lập**
    *   **Nhóm bắt đầu bằng 'i':**
        *   i ➔ **yi**, in ➔ **yin**, ing ➔ **ying**
        *   ia ➔ **ya**, iao ➔ **yao**, ian ➔ **yan**, iang ➔ **yang**, ie ➔ **ye**, iou ➔ **you**, iong ➔ **yong**
    *   **Nhóm bắt đầu bằng 'u':**
        *   u ➔ **wu**
        *   ua ➔ **wa**, uai ➔ **wai**, uan ➔ **wan**, uang ➔ **wang**, uo ➔ **wo**, uei ➔ **wei**, uen ➔ **wen**, ueng ➔ **weng**
    *   **Nhóm bắt đầu bằng 'ü' (Thêm 'y' và bỏ dấu hai chấm):**
        *   ü ➔ **yu**, üe ➔ **yue**, üan ➔ **yuan**, ün ➔ **yun**
*   **Quy tắc 2: Lược bỏ hai dấu chấm trên đầu chữ ü sau j, q, x**
    *   Khi **ün** và **üan** đi sau **j, q, x**, ta viết lược bỏ hai dấu chấm trên đầu ü thành **jun, qun, xun, juan, quan, xuan** nhưng vẫn giữ nguyên cách phát âm tròn môi.
        """
    },
    {
        "title": "Bài 7.1: Các từ để hỏi",
        "toc_desc": "Hỏi về người, vật, địa điểm, số lượng, cách thức và trợ từ nghi vấn",
        "content_html": """
        <h2 class="section-title">1. Hệ thống đại từ nghi vấn (Từ để hỏi) cốt lõi</h2>
        <p>Bảng tổng hợp các đại từ nghi vấn quan trọng nhất trong cấp độ HSK 1:</p>
        <table>
            <thead>
                <tr>
                    <th style="width: 15%;">Từ để hỏi</th>
                    <th style="width: 25%;">Phiên âm / Nghĩa</th>
                    <th style="width: 30%;">Cách sử dụng chính</th>
                    <th style="width: 30%;">Ví dụ cụ thể (Chữ Hán - Pinyin - Việt)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>谁</strong></td>
                    <td><span class="pinyin">shéi / shuí</span><br>Ai (Who)</td>
                    <td>Hỏi danh tính người. Thay thế trực tiếp vào vị trí của người trong câu.</td>
                    <td>他是谁？ <span class="pinyin">Tā shì shéi?</span> (Anh ấy là ai?)</td>
                </tr>
                <tr>
                    <td><strong>什么</strong></td>
                    <td><span class="pinyin">shénme</span><br>Cái gì / Gì (What)</td>
                    <td>Hỏi đồ vật, tên gọi, nghề nghiệp... Có thể đi kèm danh từ ở sau (什么 + N).</td>
                    <td>你叫什么名字？ <span class="pinyin">Nǐ jiào shénme míngzi?</span> (Bạn tên là gì?)</td>
                </tr>
                <tr>
                    <td><strong>哪</strong></td>
                    <td><span class="pinyin">nǎ</span><br>Nào (Which)</td>
                    <td>Hỏi về sự lựa chọn. Thường đi kèm lượng từ và danh từ phía sau.</td>
                    <td>你是哪国人？ <span class="pinyin">Nǐ shì nǎ guó rén?</span> (Bạn là người nước nào?)</td>
                </tr>
                <tr>
                    <td><strong>哪儿 / 哪里</strong></td>
                    <td><span class="pinyin">nǎr / nǎlǐ</span><br>Ở đâu / Đâu (Where)</td>
                    <td>Hỏi về vị trí địa điểm. Thường đi sau động từ 在 (ở) hoặc 去 (đi).</td>
                    <td>我的书在哪儿？ <span class="pinyin">Wǒ de shū zài nǎr?</span> (Sách của tôi ở đâu?)</td>
                </tr>
                <tr>
                    <td><strong>几</strong></td>
                    <td><span class="pinyin">jǐ</span><br>Mấy (How many)</td>
                    <td>Hỏi số lượng nhỏ (&lt; 10). Bắt buộc đi kèm lượng từ (几 + Lượng từ + N).</td>
                    <td>你家有几口人？ <span class="pinyin">Nǐ jiā yǒu jǐ kǒu rén?</span> (Nhà bạn có mấy người?)</td>
                </tr>
                <tr>
                    <td><strong>多少</strong></td>
                    <td><span class="pinyin">duōshao</span><br>Bao nhiêu (How many/much)</td>
                    <td>Hỏi số lượng lớn hoặc không giới hạn. Lượng từ đi kèm không bắt buộc.</td>
                    <td>这个杯子多少钱？ <span class="pinyin">Zhège bēizi duōshao qián?</span> (Cái cốc này bao nhiêu tiền?)</td>
                </tr>
                <tr>
                    <td><strong>怎么</strong></td>
                    <td><span class="pinyin">zěnme</span><br>Thế nào / Sao (How/Why)</td>
                    <td>Hỏi cách thức thực hiện hành động (怎么 + V), hoặc hỏi lý do đầy ngạc nhiên.</td>
                    <td>这个字怎么写？ <span class="pinyin">Zhège zì zěnme xiě?</span> (Chữ này viết thế nào?)</td>
                </tr>
                <tr>
                    <td><strong>怎么样</strong></td>
                    <td><span class="pinyin">zěnmeyàng</span><br>Thế nào / Ra sao (How about)</td>
                    <td>Hỏi tình trạng tính chất (đứng cuối câu) hoặc thăm hỏi ý kiến đề xuất.</td>
                    <td>今天天气怎么样？ <span class="pinyin">Jīntiān tiānqì zěnmeyàng?</span> (Thời tiết hôm nay thế nào?)</td>
                </tr>
                <tr>
                    <td><strong>什么时候</strong></td>
                    <td><span class="pinyin">shénme shíhou</span><br>Khi nào / Lúc nào / Bao giờ (When)</td>
                    <td>Hỏi thời điểm xảy ra hành động. Đứng trước hoặc sau chủ ngữ (trước động từ).</td>
                    <td>你什么时候去中国？ <span class="pinyin">Nǐ shénme shíhou qù Zhōngguó?</span> (Khi nào bạn đi Trung Quốc?)</td>
                </tr>
                <tr>
                    <td><strong>为什么</strong></td>
                    <td><span class="pinyin">wèishénme</span><br>Tại sao / Vì sao (Why)</td>
                    <td>Hỏi lý do, nguyên nhân thực hiện hành động, sự việc.</td>
                    <td>你为什么不喝茶？ <span class="pinyin">Nǐ wèishénme bù hē chá?</span> (Tại sao bạn không uống trà?)</td>
                </tr>
            </tbody>
        </table>

        <h2 class="section-title">2. Trợ từ nghi vấn đặc biệt ở cuối câu</h2>
        <p>Các trợ từ không dùng để thay thế từ ngữ mà đứng cuối câu để biến câu trần thuật thành câu hỏi:</p>
        <table>
            <thead>
                <tr>
                    <th style="width: 20%;">Trợ từ nghi vấn</th>
                    <th style="width: 20%;">Phiên âm / Nghĩa</th>
                    <th style="width: 30%;">Vị trí &amp; Tác dụng</th>
                    <th style="width: 30%;">Ví dụ cụ thể</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>吗</strong></td>
                    <td><span class="pinyin">ma</span><br>...không? / ...phải không?</td>
                    <td>Đứng cuối câu trần thuật để tạo câu hỏi nghi vấn Đúng/Sai (Yes/No).</td>
                    <td>你是学生吗？ <span class="pinyin">Nǐ shì xuésheng ma?</span> (Bạn là học sinh phải không?)</td>
                </tr>
                <tr>
                    <td><strong>呢</strong></td>
                    <td><span class="pinyin">ne</span><br>...thì sao? / ...đâu?</td>
                    <td>Đứng sau danh từ/đại từ để hỏi tỉnh lược ("còn bạn thì sao?") hoặc hỏi vị trí nhanh.</td>
                    <td>我的杯子呢？ <span class="pinyin">Wǒ de bēizi ne?</span> (Cái cốc của tôi đâu rồi?)</td>
                </tr>
            </tbody>
        </table>

        <h2 class="section-title">3. So sánh mở rộng và lưu ý sử dụng</h2>
        <div class="info-box">
            <strong>💡 Phân biệt 几 (jǐ) và 多少 (duōshao):</strong><br>
            • <strong>几 (jǐ):</strong> Thường dùng khi ước lượng số lượng nhỏ (&lt; 10) và <strong>bắt buộc phải có lượng từ</strong> đi kèm phía sau (Ví dụ: 几本书, 几个人). Thường dùng hỏi giờ, ngày tháng, thứ, gia đình.<br>
            • <strong>多少 (duōshao):</strong> Dùng khi ước lượng số lượng lớn hoặc không giới hạn số lượng, <strong>lượng từ phía sau có thể có hoặc không</strong> (Ví dụ: 多少(个)人, 多少钱).
        </div>
        <div class="info-box">
            <strong>💡 Phân biệt 怎么 (zěnme) và 怎么样 (zěnmeyàng):</strong><br>
            • <strong>怎么 (zěnme):</strong> Luôn đứng trước động từ để hỏi về cách thức thực hiện hành động (怎么写 - viết thế nào, 怎么去 - đi thế nào).<br>
            • <strong>怎么样 (zěnmeyàng):</strong> Đứng ở cuối câu để hỏi về tính chất, trạng thái (天气怎么样 - thời tiết thế nào) hoặc đề xuất lấy ý kiến (Chúng ta đi ăn cơm nhé, thấy thế nào?).
        </div>
        <div class="info-box">
            <strong>💡 Bản sắc địa phương: 哪儿 (nǎr) và 哪里 (nǎlǐ):</strong><br>
            • Cả hai đều dùng hỏi địa điểm "ở đâu". <strong>哪儿</strong> phổ biến ở miền Bắc với âm cuốn lưỡi, còn <strong>哪里</strong> phổ biến hơn ở miền Nam, Đài Loan.<br>
            • Ngoài ra, <strong>哪里，哪里！</strong> (Nǎlǐ, nǎlǐ!) còn là câu phản hồi khiêm tốn khi nhận lời khen (Đâu có, đâu có!). Không dùng "哪儿，哪儿" cho mục đích này.
        </div>
        """,
        "content_md": """
### 1. Hệ thống đại từ nghi vấn (Từ để hỏi) HSK 1
*   **谁 (shéi / shuí) - Ai:** Hỏi về danh tính (Ví dụ: 他是谁？ - Anh ấy là ai?).
*   **什么 (shénme) - Cái gì / Gì:** Hỏi đồ vật, tên gọi (Ví dụ: 这是什么？ - Đây là cái gì?).
*   **哪 (nǎ) - Nào:** Hỏi lựa chọn (Ví dụ: 你是 nǎ guó rén? - Bạn là người nước nào?).
*   **哪儿 / 哪里 (nǎr / nǎlǐ) - Ở đâu:** Hỏi vị trí (Ví dụ: 我的书在哪儿？ - Sách của tôi ở đâu?).
*   **几 (jǐ) - Mấy:** Hỏi số lượng nhỏ < 10, yêu cầu lượng từ (Ví dụ: 你家有几口人？ - Nhà bạn có mấy người?).
*   **多少 (duōshao) - Bao nhiêu:** Hỏi số lượng không giới hạn, lượng từ không bắt buộc (Ví dụ: 这个杯子多少钱？ - Cái cốc này bao nhiêu tiền?).
*   **怎么 (zěnme) - Thế nào / Sao:** Hỏi cách thức (怎么写 - viết thế nào) hoặc lý do ngạc nhiên.
*   **怎么样 (zěnmeyàng) - Ra sao / Thế nào:** Hỏi trạng thái hoặc lấy ý kiến (Ví dụ: 今天天气怎么样？ - Thời tiết hôm nay thế nào?).
*   **什么时候 (shénme shíhou) - Khi nào / Lúc nào:** Hỏi về thời gian, thời điểm (Ví dụ: 你什么时候去中国？ - Khi nào bạn đi Trung Quốc?).
*   **为什么 (wèishénme) - Tại sao:** Hỏi về nguyên nhân, lý do (Ví dụ: 你为什么不喝茶？ - Tại sao bạn không uống trà?).

### 2. Trợ từ nghi vấn cuối câu
*   **吗 (ma) - ...không?:** Biến câu trần thuật thành câu hỏi Yes/No (Ví dụ: 你是老师吗？ - Bạn là giáo viên phải không?).
*   **呢 (ne) - ...thì sao?:** Dùng trong câu hỏi tỉnh lược (Ví dụ: 我很好，你呢？ - Tôi rất tốt, còn bạn?) hoặc hỏi vị trí nhanh (我的杯子呢？ - Cái cốc của tôi đâu?).

### 3. Điểm ngữ pháp cốt lõi
1.  **Cấu trúc 几 (jǐ) và 多少 (duōshao):** 几 bắt buộc đi với lượng từ, 多少 không bắt buộc.
2.  **Cấu trúc 怎么 (zěnme) và 怎么样 (zěnmeyàng):** 怎么 + Động từ; 怎么样 đứng ở cuối câu.
3.  **Hỏi vị trí:** Dùng 哪儿 hoặc 哪里 đứng sau động từ 在 (ở) hoặc 去 (đi).
4.  **Cấu trúc 什么时候 (shénme shíhou) và 为什么 (wèishénme):** Thường đứng trước động từ (sau chủ ngữ) để hỏi về thời điểm và nguyên nhân thực hiện hành động.
        """
    },
    {
        "title": "Bài 7.2: Cách dùng chữ 的",
        "toc_desc": "Sở hữu, tính chất đặc điểm, cấu trúc chữ 的 và quy tắc lược bỏ",
        "content_html": """
        <h2 class="section-title">1. Ba cấu trúc ngữ pháp cơ bản của chữ 的</h2>
        <p>Quy tắc cốt lõi: Cái chính yếu, quan trọng đứng sau; cái phụ trợ, bổ nghĩa đứng trước.</p>
        <table>
            <thead>
                <tr>
                    <th style="width: 25%;">Cấu trúc sử dụng</th>
                    <th style="width: 35%;">Giải thích chi tiết</th>
                    <th style="width: 40%;">Ví dụ cụ thể (Chữ Hán - Pinyin - Việt)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Sở hữu (Của...)</strong></td>
                    <td>Đảo ngược so với tiếng Việt.<br>Cấu trúc: <strong>Người sở hữu + 的 + Vật sở hữu</strong></td>
                    <td>我的书 <span class="pinyin">wǒ de shū</span> (Sách của tôi)<br>老师的电脑 <span class="pinyin">lǎoshī de diànnǎo</span> (Máy tính của thầy giáo)</td>
                </tr>
                <tr>
                    <td><strong>Đặc điểm, tính chất</strong></td>
                    <td>Nối tính từ với danh từ để miêu tả đặc điểm.<br>Cấu trúc: <strong>Tính từ + 的 + Danh từ</strong></td>
                    <td>很好的朋友 <span class="pinyin">hěn hǎo de péngyou</span> (Người bạn rất tốt)<br>很大的苹果 <span class="pinyin">hěn dà de píngguǒ</span> (Quả táo rất to)</td>
                </tr>
                <tr>
                    <td><strong>Cấu trúc chữ "de" lược bỏ</strong></td>
                    <td>Lược bỏ danh từ phía sau chữ 的 khi ngữ cảnh đã rõ ràng để tránh lặp từ.</td>
                    <td>我要大的。 <span class="pinyin">Wǒ yào dà de.</span> (Tôi muốn cái to.)<br>这本书是我的。 <span class="pinyin">Zhè běn shū shì wǒ de.</span> (Cuốn sách này là của tôi.)</td>
                </tr>
            </tbody>
        </table>

        <h2 class="section-title">2. Quy tắc lược bỏ chữ 的 khi biểu thị sở hữu</h2>
        <p>Bạn có thể lược bỏ chữ <strong>的</strong> khi giữa người sở hữu và đối tượng sở hữu có mối quan hệ gắn bó khăng khít:</p>
        <table>
            <thead>
                <tr>
                    <th style="width: 30%;">Trường hợp</th>
                    <th style="width: 35%;">Cách dùng đúng (Nên dùng)</th>
                    <th style="width: 35%;">Giải thích ngữ cảnh</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Người thân gia đình</strong></td>
                    <td>我爸爸 <span class="pinyin">wǒ bàba</span> (Bố tôi)<br>我妈妈 <span class="pinyin">wǒ māma</span> (Mẹ tôi)</td>
                    <td>Mối quan hệ huyết thống ruột thịt gần gũi.</td>
                </tr>
                <tr>
                    <td><strong>Mối quan hệ xã hội quen thuộc</strong></td>
                    <td>我朋友 <span class="pinyin">wǒ péngyou</span> (Bạn tôi)<br>Chúng tôi 老师 / 我们老师 <span class="pinyin">wǒmen lǎoshī</span> (Thầy giáo của chúng tôi)</td>
                    <td>Giao tế xã hội, bạn bè học tập thân cận.</td>
                </tr>
                <tr>
                    <td><strong>Nơi chốn, cơ quan gắn liền</strong></td>
                    <td>我家 <span class="pinyin">wǒ jiā</span> (Nhà tôi)<br>我学校 <span class="pinyin">wǒ xuéxiào</span> (Trường tôi)</td>
                    <td>Nơi thuộc về hoặc sinh sống hàng ngày.</td>
                </tr>
            </tbody>
        </table>

        <div class="warn-box">
            <strong>⚠️ LƯU Ý BẮT BUỘC GIỮ LẠI "Đ":</strong><br>
            Đối với <strong>đồ vật cá nhân, tài sản độc lập</strong> (quần áo, sách vở, tiền bạc, máy tính...), mối quan hệ này không phải là "tự nhiên gắn liền" mà là sở hữu tài sản. Bạn bắt buộc phải giữ chữ 的:<br>
            • Đúng: <strong>我的书</strong> (Sách của tôi) &nbsp;&nbsp; ❌ Sai: <i>我书</i><br>
            • Đúng: <strong>他的电脑</strong> (Máy tính của anh ấy) &nbsp;&nbsp; ❌ Sai: <i>他电脑</i><br>
            • Đúng: <strong>我的衣服</strong> (Quần áo của tôi) &nbsp;&nbsp; ❌ Sai: <i>我衣服</i>
        </div>
        """,
        "content_md": """
### 1. Ba cấu trúc cơ bản
1.  **Biểu thị sở hữu:** Người sở hữu + 的 + Đồ vật (Ví dụ: 我的书 - Sách của tôi).
2.  **Biểu thị đặc điểm:** Tính từ + 的 + Danh từ (Ví dụ: 很好的朋友 - Người bạn rất tốt).
3.  **Cấu trúc chữ 的 rút gọn:** Bỏ danh từ phía sau (Ví dụ: 我要大的 - Tôi lấy cái to; 这本书是我的 - Sách này là của tôi).

### 2. Quy tắc lược bỏ "de" (Sở hữu thân thiết)
*   **Có thể lược bỏ:**
    *   Người thân (...爸爸, 我妈妈)
    *   Quan hệ xã hội thân cận (我朋友, 我们老师)
    *   Nơi chốn/Cơ quan thuộc về (我家, 我学校)
*   **Bắt buộc giữ 的:** Tài sản cá nhân, đồ vật (我的书, 他的电脑).
        """
    },
        {
        "title": "Bài 8.1: Tổng quan Chữ Hán",
        "toc_desc": "Bản chất chữ Hán, so sánh Phồn thể & Giản thể, 4 cách cấu tạo chữ Hán theo Lục thư",
        "content_html": """
        <h2 class="section-title">1. Bản chất Chữ Hán</h2>
        <p>Chữ Hán (汉字) là hệ chữ <strong>biểu ý</strong> (ghi lại ý nghĩa), khác với chữ Quốc ngữ hay tiếng Anh là hệ chữ <strong>biểu âm</strong> (ghép chữ cái phát âm).</p>
        <div class="info-box">
            • <strong>Chữ Phồn thể (繁体字):</strong> Kiểu chữ truyền thống nhiều nét, mang tính tạo hình cao. Ví dụ: <strong>馬</strong> (mã - con ngựa) gồm 10 nét.<br>
            • <strong>Chữ Giản thể (简体字):</strong> Bản rút gọn lược bớt nét để viết nhanh, dễ nhớ hơn. Ví dụ: <strong>马</strong> gồm 3 nét.
        </div>
        <div style="text-align: center; margin: 15px 0;">
            <img src="{ASSETS_PATH}/horse_evolution.png" alt="Sự tiến hóa chữ Mã" style="max-width: 100%; height: auto; border: 1.5px solid var(--border-color); border-radius: 8px; padding: 5px;">
            <p style="font-size: 11px; color: #475569; margin-top: 5px;">Sự tiến hóa của chữ Mã (Ngựa) qua các thời kỳ</p>
        </div>
        
        <h2 class="section-title">2. Cấu tạo Chữ Hán theo Lục thư (4 cách cơ bản)</h2>
        <table>
            <thead>
                <tr>
                    <th style="width: 25%;">Phương thức tạo chữ</th>
                    <th style="width: 35%;">Định nghĩa &amp; Đặc điểm</th>
                    <th style="width: 40%;">Ví dụ biểu diễn</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Chữ Tượng hình</strong><br>(象形)</td>
                    <td>Phác họa lại hình dáng thực tế của sự vật ngoài đời.</td>
                    <td><strong>日</strong> (Mặt trời), <strong>月</strong> (Mặt trăng), <strong>木</strong> (Cây), <strong>山</strong> (Núi), <strong>人</strong> (Người).</td>
                </tr>
                <tr>
                    <td><strong>Chữ Chỉ sự</strong><br>(指 sự)</td>
                    <td>Dùng ký hiệu ước lệ để chỉ các khái niệm trừu tượng hoặc chỉ vị trí.</td>
                    <td><strong>上</strong> (Trên), <strong>下</strong> (Dưới), <strong>本</strong> (Gốc rễ - thêm nét ngang dưới chữ 木).</td>
                </tr>
                <tr>
                    <td><strong>Chữ Hội ý</strong><br>(会意)</td>
                    <td>Ghép hai hoặc nhiều chữ đơn lẻ để biểu thị ý nghĩa mới kết hợp.</td>
                    <td><strong>休</strong> (Nghỉ ngơi = Người 人 tựa cây 木), <strong>明</strong> (Sáng = Nhật 日 + Nguyệt 月), <strong>好</strong> (Tốt = Nữ 女 + Tử 子).</td>
                </tr>
                <tr>
                    <td><strong>Chữ Hình thanh</strong><br>(形声)</td>
                    <td>Ghép phần chỉ ý nghĩa (bộ thủ) và phần chỉ cách đọc (biểu âm). Chiếm hơn 80% chữ Hán.</td>
                    <td><strong>妈</strong> (Mẹ = Nữ 女 chỉ nghĩa + Mã 马 chỉ âm 'mā'), <strong>爸</strong> (Bố = Phụ 父 chỉ nghĩa + Ba Ba chỉ âm 'bà').</td>
                </tr>
            </tbody>
        </table>
        """,
        "content_md": """
### 1. Bản chất Chữ Hán
* Chữ Hán là chữ biểu ý.
* Gồm 2 dạng viết: Phồn thể (馬 - 10 nét) và Giản thể (马 - 3 nét).

### 2. Cấu tạo Chữ Hán theo Lục thư
* **Tượng hình (象形):** Vẽ hình sự vật (Ví dụ: 日, 月, 木, 山, 人).
* **Chỉ sự (指事):** Biểu diễn khái niệm trừu tượng (Ví dụ: 上, 下, 本).
* **Hội ý (会意):** Ghép nghĩa các chữ đơn (Ví dụ: 休 = 人 + 木; 明 = 日 + 月; 好 = 女 + Tử).
* **Hình thanh (形声):** Ghép phần chỉ nghĩa + phần chỉ âm (Ví dụ: 妈, 爸).
        """
    },
    {
        "title": "Bài 8.2: Hệ thống Nét viết",
        "toc_desc": "8 nét viết cơ bản (Vĩnh tự bát pháp), Giải nghĩa cấu tạo chữ 永 và 4 nét biến thể ghép",
        "content_html": """
        <h2 class="section-title">1. 8 Nét viết cơ bản (Vĩnh tự bát pháp)</h2>
        <p>Hệ thống nét viết trong chữ Hán bắt đầu bằng 8 nét cốt lõi:</p>
        <table>
            <thead>
                <tr>
                    <th style="width: 25%;">Tên nét tiếng Việt</th>
                    <th style="width: 25%;">Ký hiệu minh họa</th>
                    <th style="width: 50%;">Mô tả cách viết</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Chấm (点)</strong></td>
                    <td style="font-size: 20px; text-align: center; font-weight: bold;">丶</td>
                    <td>Dấu chấm từ trên xuống, hơi chếch sang phải.</td>
                </tr>
                <tr>
                    <td><strong>Ngang (横)</strong></td>
                    <td style="font-size: 20px; text-align: center; font-weight: bold;">一</td>
                    <td>Thẳng ngang từ trái sang phải.</td>
                </tr>
                <tr>
                    <td><strong>Sổ (竖)</strong></td>
                    <td style="font-size: 20px; text-align: center; font-weight: bold;">丨</td>
                    <td>Thẳng đứng dọc từ trên xuống dưới.</td>
                </tr>
                <tr>
                    <td><strong>Phẩy (撇)</strong></td>
                    <td style="font-size: 20px; text-align: center; font-weight: bold;">丿</td>
                    <td>Nét cong từ trên xuống, vắt chéo sang trái.</td>
                </tr>
                <tr>
                    <td><strong>Mác (捺)</strong></td>
                    <td style="font-size: 20px; text-align: center; font-weight: bold;">乀</td>
                    <td>Nét thẳng xiên từ trên xuống, kéo sang phải.</td>
                </tr>
                <tr>
                    <td><strong>Hất (提)</strong></td>
                    <td style="font-size: 20px; text-align: center; font-weight: bold;">㇀</td>
                    <td>Nét thẳng đi chéo từ dưới lên trên, sang phải.</td>
                </tr>
                <tr>
                    <td><strong>Gập (折)</strong></td>
                    <td style="font-size: 20px; text-align: center; font-weight: bold;">𠃍</td>
                    <td>Gập khúc chuyển hướng đột ngột của đầu bút.</td>
                </tr>
                <tr>
                    <td><strong>Móc (钩)</strong></td>
                    <td style="font-size: 20px; text-align: center; font-weight: bold;">亅</td>
                    <td>Nét móc nhỏ ngược lên ở cuối nét sổ hoặc nét nghiêng.</td>
                </tr>
            </tbody>
        </table>

        <h2 class="section-title">2. Ý nghĩa chữ 永 (Vĩnh) trong thư pháp</h2>
        <div class="info-box">
            Chữ <strong>永</strong> (yǒng - vĩnh viễn/mãi mãi) là chữ kinh điển chứa đầy đủ cả 8 nét viết cơ bản trên:<br>
            • Nét Chấm (点): Đỉnh trên cùng.<br>
            • Nét Ngang (横): Giữa thân trái.<br>
            • Nét Sổ (竖): Dọc trục chính đứng.<br>
            • Nét Móc (钩): Móc đáy sổ dọc.<br>
            • Nét Hất (提): Chéo xiên bên trái lên.<br>
            • Nét Phẩy (撇): Cong bên trái.<br>
            • Nét Gập (折): Khung gập bên phải.<br>
            • Nét Mác (捺): Kéo xiên dài bên phải.
        </div>

        <h2 class="section-title">3. Các nét biến thể ghép</h2>
        <ul>
            <li><strong>横折 (héngzhé - Ngang gập):</strong> Ngang rồi gập vuông góc đi xuống (Ví dụ: 口, 日).</li>
            <li><strong>竖折 (shùzhé - Sổ gập):</strong> Sổ rồi gập vuông góc sang phải (Ví dụ: 山).</li>
            <li><strong>竖钩 (shùgōu - Sổ móc):</strong> Sổ thẳng rồi móc nhọn lên bên trái (Ví dụ: 小, 水).</li>
            <li><strong>斜钩 (xiégōu - Nghiêng móc):</strong> Nghiêng cong kéo từ trên xuống rồi móc chéo lên (Ví dụ: 我).</li>
        </ul>
        """,
        "content_md": """
### 1. 8 Nét Cơ Bản
* Chấm (点): 丶
* Ngang (横): 一
* Sổ (竖): 丨
* Phẩy (撇): 丿
* Mác (捺): 乀
* Hất (提): ㇀
* Gập (折): 𠃍
* Móc (钩): 亅

### 2. Ý nghĩa chữ 永
Chữ 永 chứa đủ 8 nét viết cơ bản của chữ Hán.

### 3. Nét biến thể ghép
* Ngang gập (横折) - chữ 口
* Sổ gập (竖折) - chữ 山
* Sổ móc (竖钩) - chữ 小
* Nghiêng móc (斜钩) - chữ 我
        """
    },
    {
        "title": "Bài 8.3: Quy tắc Bút thuận",
        "toc_desc": "7 quy tắc viết bút thuận chữ Hán từ trước ra sau, từ trên xuống dưới",
        "content_html": """
        <h2 class="section-title">7 Quy tắc Bút thuận cơ bản</h2>
        <p>Bút thuận là quy định thứ tự viết trước - sau của các nét để chữ Hán viết nhanh, cân đối và đẹp mắt:</p>
        <table>
            <thead>
                <tr>
                    <th style="width: 10%;">STT</th>
                    <th style="width: 30%;">Quy tắc bút thuận</th>
                    <th style="width: 45%;">Hướng dẫn chi tiết</th>
                    <th style="width: 15%;">Ví dụ chữ</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td><strong>Ngang trước sổ sau</strong></td>
                    <td>Nét ngang viết trước, nét sổ cắt qua viết sau.</td>
                    <td><strong>十</strong> (Mười)</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td><strong>Phẩy trước mác sau</strong></td>
                    <td>Nét phẩy bên trái viết trước, nét mác bên phải viết sau.</td>
                    <td><strong>人</strong> (Người)</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td><strong>Trên trước dưới sau</strong></td>
                    <td>Viết các nét ở phía trên trước, nét ở dưới viết sau.</td>
                    <td><strong>三</strong> (Ba)</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td><strong>Trái trước phải sau</strong></td>
                    <td>Phần bên trái chữ viết trước, phần bên phải viết sau.</td>
                    <td><strong>你</strong> (Bạn)</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td><strong>Ngoài trước trong sau</strong></td>
                    <td>Khung bao vây ngoài viết trước, bộ phận trong viết sau.</td>
                    <td><strong>月</strong> (Mặt trăng)</td>
                </tr>
                <tr>
                    <td>6</td>
                    <td><strong>Vào trước đóng sau</strong></td>
                    <td>Viết khung ngoài (hở đáy) ➔ viết ruột ➔ đóng cửa đáy.</td>
                    <td><strong>国</strong> (Quốc gia)</td>
                </tr>
                <tr>
                    <td>7</td>
                    <td><strong>Giữa trước hai bên sau</strong></td>
                    <td>Nét thẳng đứng ở giữa viết trước, hai bên viết sau.</td>
                    <td><strong>小</strong> (Nhỏ)</td>
                </tr>
            </tbody>
        </table>
        """,
        "content_md": """
### 7 Quy tắc viết bút thuận
1. Ngang trước sổ sau: 十
2. Phẩy trước mác sau: 人
3. Trên trước dưới sau: 三
4. Trái trước phải sau: 你
5. Ngoài trước trong sau: 月
6. Vào trước đóng sau: 国
7. Giữa trước hai bên sau: 小
        """
    },
    {
        "title": "Bài 8.4: Hệ thống Bộ thủ",
        "toc_desc": "Vai trò bộ thủ biểu nghĩa và 8 bộ thủ cốt lõi của trình độ HSK 1",
        "content_html": """
        <h2 class="section-title">1. Khái niệm Bộ thủ (部首)</h2>
        <p>Bộ thủ là bộ phận biểu ý chính của chữ Hán, giúp chúng ta nhận diện ý nghĩa khái quát của từ mặc dù chưa biết cách đọc.</p>
        
        <h2 class="section-title">2. 8 Bộ thủ cốt lõi trình độ HSK 1</h2>
        <table>
            <thead>
                <tr>
                    <th style="width: 15%;">Bộ thủ</th>
                    <th style="width: 25%;">Ý nghĩa gốc</th>
                    <th style="width: 40%;">Mô tả ngữ nghĩa liên quan</th>
                    <th style="width: 20%;">Ví dụ chữ Hán</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>亻(人)</strong></td>
                    <td>Nhân (Con người)</td>
                    <td>Liên quan đến con người, danh xưng, hoạt động của người.</td>
                    <td><strong>他</strong> (anh ấy), <strong>ni</strong> (bạn)</td>
                </tr>
                <tr>
                    <td><strong>女</strong></td>
                    <td>Nữ (Phụ nữ)</td>
                    <td>Liên quan đến phái đẹp, người nữ, gia đình.</td>
                    <td><strong>她</strong> (cô ấy), <strong>妈</strong> (mẹ)</td>
                </tr>
                <tr>
                    <td><strong>口</strong></td>
                    <td>Khẩu (Miệng)</td>
                    <td>Liên quan đến ăn uống, kêu gọi, bộ phận ở miệng.</td>
                    <td><strong>吃</strong> (ăn), <strong>喝</strong> (uống)</td>
                </tr>
                <tr>
                    <td><strong>氵(水)</strong></td>
                    <td>Thủy (Nước)</td>
                    <td>Liên quan đến chất lỏng, sông ngòi, nước nói chung.</td>
                    <td><strong>没</strong> (không có), <strong>汉</strong> (Hán)</td>
                </tr>
                <tr>
                    <td><strong>木</strong></td>
                    <td>Mộc (Cây, Gỗ)</td>
                    <td>Liên quan đến cây cối, rừng rậm hoặc đồ dùng bằng gỗ.</td>
                    <td><strong>杯</strong> (cốc), <strong>桌</strong> (bàn)</td>
                </tr>
                <tr>
                    <td><strong>火 (灬)</strong></td>
                    <td>Hỏa (Lửa)</td>
                    <td>Liên quan đến nhiệt độ, sức nóng, nấu nướng.</td>
                    <td><strong>热</strong> (nóng), <strong>点</strong> (giờ)</td>
                </tr>
                <tr>
                    <td><strong>讠(言)</strong></td>
                    <td>Ngôn (Lời nói)</td>
                    <td>Liên quan đến giao tiếp, đối thoại, phát ngôn.</td>
                    <td><strong>说</strong> (nói), <strong>语</strong> (ngôn ngữ)</td>
                </tr>
                <tr>
                    <td><strong>忄(心)</strong></td>
                    <td>Tâm (Cảm xúc)</td>
                    <td>Liên quan đến suy nghĩ, tâm trạng, tình cảm tâm lý.</td>
                    <td><strong>忙</strong> (bận), <strong>想</strong> (muốn/nhớ)</td>
                </tr>
            </tbody>
        </table>
        """,
        "content_md": """
### 1. Khái niệm Bộ thủ
Bộ thủ là thành phần quy định nghĩa của chữ.

### 2. 8 Bộ thủ cơ bản HSK 1
* **亻(人) - Nhân:** 他, 你
* **女 - Nữ:** 她, 妈
* **口 - Khẩu:** 吃, 喝
* **氵(水) - Thủy:** 没, 汉
* **木 - Mộc:** 杯, 桌
* **火 (灬) - Hỏa:** 热, 点
* **讠(言) - Ngôn:** 说, 语
* **忄(心) - Tâm:** 忙, 想
        """
    },
    {
        "title": "Bài 8.5: Đơn thể & Hợp thể",
        "toc_desc": "Phân loại chữ Đơn thể độc lập và Chữ Hợp thể ghép theo cấu trúc",
        "content_html": """
        <h2 class="section-title">1. Chữ Đơn thể (独体字)</h2>
        <p>Là kiểu chữ độc lập cấu thành trực tiếp từ các nét vẽ gốc, không thể bóc tách nhỏ hơn thành các bộ phận có nghĩa lẻ. Đóng vai trò làm bộ thủ hoặc khối gốc xây dựng các chữ khác.</p>
        <div class="info-box">
            <strong>Ví dụ tiêu biểu:</strong> <strong>人</strong> (Người), <strong>木</strong> (Cây), <strong>日</strong> (Mặt trời), <strong>月</strong> (Mặt trăng), <strong>山</strong> (Núi), <strong>水</strong> (Nước), <strong>口</strong> (Miệng), <strong>女</strong> (Phụ nữ).
        </div>

        <h2 class="section-title">2. Chữ Hợp thể (合体字)</h2>
        <p>Là kiểu chữ phức hợp ghép từ hai hay nhiều bộ phận nhỏ hơn (các bộ thủ kết hợp với chữ đơn thể). Có 3 kiểu cấu trúc ghép phổ biến nhất:</p>
        <table>
            <thead>
                <tr>
                    <th style="width: 30%;">Cấu trúc ghép</th>
                    <th style="width: 40%;">Hướng dẫn nhận diện</th>
                    <th style="width: 30%;">Ví dụ chữ Hán</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Kết cấu Trái - Phải</strong></td>
                    <td>Hai bộ phận xếp song hành từ trái qua phải.</td>
                    <td><strong>好</strong> (Nữ 女 + Tử 子)<br><strong>你</strong> (Nhân 亻 + Nhĩ 尔)</td>
                </tr>
                <tr>
                    <td><strong>Kết cấu Trên - Dưới</strong></td>
                    <td>Hai bộ phận xếp chồng lên nhau từ trên xuống dưới.</td>
                    <td><strong>爸</strong> (Phụ 父 + Ba Ba)<br><strong>字</strong> (Miên 宀 + Tử 子)</td>
                </tr>
                <tr>
                    <td><strong>Kết cấu Bao vây</strong></td>
                    <td>Khung ngoài ôm bao bọc bộ phận nhỏ hơn ở trong.</td>
                    <td><strong>国</strong> (Vi 囗 + Ngọc 玉)<br><strong>回</strong> (Vi 囗 + Khẩu 口)</td>
                </tr>
            </tbody>
        </table>
        """,
        "content_md": """
### 1. Chữ Đơn thể
* Chữ độc lập tạo từ nét vẽ gốc.
* Ví dụ: 人, 木, 日, 月, 山, 水, 口, 女.

### 2. Chữ Hợp thể
* Chữ ghép từ các thành phần chữ đơn thể khác.
* **Trái - Phải:** 好 (女+子), 你 (亻+尔).
* **Trên - Dưới:** 爸 (父+巴), 字 (宀+子).
* **Bao vây:** 国 (囗+玉), 回 (囗+口).
        """
    }
]

def make_filename(title):
    match = re.search(r"Bài\s+([\d\.]+)", title, re.IGNORECASE)
    if match:
        val = match.group(1).replace(".", "_")
        return f"bai_{val}.html"
    return "bai_hoc.html"

def build_individual_lessons():
    output_dir = "giao_trinh_in_an"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    css_content = """
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap');
        :root { --primary-color: #000000; --secondary-color: #000000; --dark-color: #000000; --light-bg: #f1f5f9; --border-color: #000000; --highlight-bg: #ffffff; --highlight-border: #000000; }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Inter', 'Noto Sans SC', sans-serif; font-weight: 700; color: var(--dark-color); line-height: 1.6; background-color: #ffffff; font-size: 14px; }
        .container { max-width: 900px; margin: 0 auto; padding: 30px; }
        h1.lesson-title { font-size: 24px; color: var(--primary-color); border-bottom: 3px solid var(--primary-color); padding-bottom: 10px; margin-bottom: 20px; text-transform: uppercase; }
        h2.section-title { font-size: 18px; color: var(--secondary-color); border-left: 5px solid var(--secondary-color); padding-left: 10px; margin-top: 25px; margin-bottom: 15px; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 13.5px; }
        table, th, td { border: 1.5px solid var(--border-color); padding: 10px; }
        th { background-color: #f1f5f9; color: var(--primary-color); }
        .info-box { background-color: var(--light-bg); border-left: 5px solid var(--primary-color); padding: 15px; margin: 15px 0; border: 1.5px solid var(--border-color); }
        .warn-box { background-color: var(--highlight-bg); border-left: 5px solid var(--primary-color); padding: 15px; margin: 15px 0; border: 1.5px solid var(--border-color); }
        .exercise-section { border: 2px dashed var(--border-color); border-radius: 12px; padding: 20px; margin: 30px 0; }
        .pinyin { font-family: inherit; font-weight: inherit; color: var(--primary-color); }
        .write-line { display: inline-block; width: 150px; border-bottom: 1.5px solid var(--border-color); }
        .print-btn-container { display: flex; justify-content: flex-end; margin-bottom: 20px; }
        .print-btn { background-color: var(--primary-color); color: white; border: none; padding: 10px 20px; font-size: 14px; font-weight: bold; border-radius: 6px; cursor: pointer; transition: background-color 0.2s; }
        .print-btn:hover { background-color: var(--secondary-color); }

        /* Cover Page Styling */
        .cover-page {
            height: 90vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            border: 4px double var(--primary-color);
            padding: 40px;
            background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 100%);
            margin-top: 2vh;
            page-break-after: always;
            break-after: page;
        }
        .cover-badge {
            background-color: var(--primary-color);
            color: white;
            padding: 6px 16px;
            font-size: 14px;
            font-weight: 700;
            letter-spacing: 2px;
            border-radius: 40px;
            margin-bottom: 24px;
        }
        .cover-title {
            font-size: 32px;
            color: var(--primary-color);
            text-align: center;
            font-weight: 800;
            line-height: 1.3;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        @media print {
            .no-print { display: none !important; }
            body { font-size: 11.5px !important; line-height: 1.25 !important; font-weight: 700 !important; -webkit-print-color-adjust: exact; print-color-adjust: exact; background-color: #ffffff; }
            .container { width: 100% !important; max-width: 100% !important; padding: 0 !important; margin: 0 auto !important; }
            
            /* Cover Page - Precise A4 Print size to prevent trailing blank space */
            .cover-page {
                height: 270mm !important;
                margin: 0 auto !important;
                padding: 25px !important;
                border: 4px double var(--primary-color) !important;
                box-sizing: border-box !important;
                display: flex !important;
                flex-direction: column !important;
                justify-content: center !important;
                align-items: center !important;
                page-break-after: always !important;
                break-after: page !important;
                page-break-inside: avoid !important;
                break-inside: avoid !important;
            }
            .cover-title {
                font-size: 25px !important;
            }

            /* Compact spacing for paragraphs, lists, and headings */
            p { margin-top: 2px !important; margin-bottom: 2px !important; line-height: 1.25 !important; }
            ul, ol { margin-top: 2px !important; margin-bottom: 2px !important; padding-left: 15px !important; }
            li { margin-bottom: 0.8px !important; }

            /* Tables & rows */
            table { page-break-inside: avoid !important; margin: 5px 0 !important; line-height: 1.2 !important; }
            tr { page-break-inside: avoid !important; break-inside: avoid !important; }
            th, td { padding: 3.5px 5px !important; font-size: 10.5px !important; }
            
            /* Allow blocks to break across pages if needed, but try to avoid */
            .info-box, .warn-box {
                page-break-inside: avoid !important;
                break-inside: avoid !important;
                padding: 5px 8px !important;
                margin: 5px 0 !important;
                font-size: 10.5px !important;
            }
            .exercise-section {
                margin: 5px 0 !important;
                padding: 5px !important;
                page-break-inside: avoid !important;
                break-inside: avoid !important;
            }

            h1.lesson-title { font-size: 15px !important; margin-top: 0 !important; margin-bottom: 4px !important; padding-bottom: 2px !important; }
            h2.section-title { font-size: 12px !important; margin-top: 5px !important; margin-bottom: 2.5px !important; padding-left: 4px !important; }
            
            /* Keep headings with their subsequent paragraph / table */
            h1, h2, h3, h4, h5, h6 { page-break-after: avoid; break-after: avoid; }
            
            p, li, tr {
                orphans: 2;
                widows: 2;
            }

            /* Lesson-specific fine tuning to fill page beautifully without overflow */
            /* Lesson 1 (Longest): squeeze slightly to fit on 1 page */
            .lesson-1 {
                font-size: 10.2px !important;
                line-height: 1.2 !important;
            }
            .lesson-1 p {
                margin-top: 1.5px !important;
                margin-bottom: 1.5px !important;
            }
            .lesson-1 table {
                margin: 4px 0 !important;
            }
            .lesson-1 th, .lesson-1 td {
                padding: 2.2px 4px !important;
                font-size: 9.2px !important;
            }
            .lesson-1 .info-box, .lesson-1 .warn-box {
                padding: 4px 6px !important;
                margin: 4px 0 !important;
                font-size: 9.2px !important;
            }

            /* Lesson 2 (Short): expand to fill page */
            .lesson-2 {
                font-size: 13.5px !important;
                line-height: 1.35 !important;
            }
            .lesson-2 p {
                margin-top: 5px !important;
                margin-bottom: 5px !important;
            }
            .lesson-2 table {
                margin: 10px 0 !important;
            }
            .lesson-2 th, .lesson-2 td {
                padding: 6px 8px !important;
                font-size: 12.5px !important;
            }

            /* Lesson 3 (Medium-long): squeeze slightly to fit on 1 page */
            .lesson-3 {
                font-size: 10.3px !important;
                line-height: 1.2 !important;
            }
            .lesson-3 th, .lesson-3 td {
                padding: 2.5px 4px !important;
                font-size: 9.3px !important;
            }
            .lesson-3 .info-box, .lesson-3 .warn-box {
                padding: 4px 6px !important;
                margin: 4px 0 !important;
                font-size: 9.3px !important;
            }

            /* Lesson 4 (Short): expand but keep safe from overflow */
            .lesson-4 {
                font-size: 12px !important;
                line-height: 1.25 !important;
            }
            .lesson-4 p {
                margin-top: 4px !important;
                margin-bottom: 4px !important;
            }
            .lesson-4 table {
                margin: 8px 0 !important;
            }
            .lesson-4 th, .lesson-4 td {
                padding: 4px 6px !important;
                font-size: 11px !important;
            }

            /* Lesson 5 (Medium-long): scale slightly */
            .lesson-5 {
                font-size: 11.2px !important;
                line-height: 1.22 !important;
            }
            .lesson-5 th, .lesson-5 td {
                padding: 3px 5px !important;
                font-size: 10.2px !important;
            }

            /* Lesson 6 (Long): squeeze slightly to fit on 1 page */
            .lesson-6 {
                font-size: 10px !important;
                line-height: 1.18 !important;
            }
            .lesson-6 p {
                margin-top: 1.5px !important;
                margin-bottom: 1.5px !important;
            }
            .lesson-6 table {
                margin: 4px 0 !important;
            }
            .lesson-6 th, .lesson-6 td {
                padding: 2.2px 4px !important;
                font-size: 9px !important;
            }
            .lesson-6 .info-box, .lesson-6 .warn-box {
                padding: 4px 6px !important;
                margin: 4px 0 !important;
                font-size: 9px !important;
            }

            /* Lesson 7.1 (Medium-long): squeeze slightly to fit on 1 page */
            .lesson-7 {
                font-size: 11px !important;
                line-height: 1.22 !important;
            }
            .lesson-7 p {
                margin-top: 2px !important;
                margin-bottom: 2px !important;
            }
            .lesson-7 table {
                margin: 6px 0 !important;
            }
            .lesson-7 th, .lesson-7 td {
                padding: 3px 5px !important;
                font-size: 9.8px !important;
            }
            .lesson-7 .info-box, .lesson-7 .warn-box {
                padding: 4px 6px !important;
                margin: 4.5px 0 !important;
                font-size: 9.8px !important;
            }

            /* Lesson 7.2 (Medium-long): squeeze slightly to fit on 1 page */
            .lesson-8 {
                font-size: 11.2px !important;
                line-height: 1.22 !important;
            }
            .lesson-8 p {
                margin-top: 2px !important;
                margin-bottom: 2px !important;
            }
            .lesson-8 table {
                margin: 6px 0 !important;
            }
            .lesson-8 th, .lesson-8 td {
                padding: 3.5px 5px !important;
                font-size: 10px !important;
            }
            .lesson-8 .info-box, .lesson-8 .warn-box {
                padding: 4px 6px !important;
                margin: 4.5px 0 !important;
                font-size: 10px !important;
            }

            /* Lesson 8.1 (Medium-long): squeeze slightly to fit on 1 page */
            .lesson-9 {
                font-size: 11px !important;
                line-height: 1.22 !important;
            }
            .lesson-9 p {
                margin-top: 2px !important;
                margin-bottom: 2px !important;
            }
            .lesson-9 table {
                margin: 6px 0 !important;
            }
            .lesson-9 th, .lesson-9 td {
                padding: 3.5px 5px !important;
                font-size: 10px !important;
            }
            .lesson-9 .info-box, .lesson-9 .warn-box {
                padding: 4px 6px !important;
                margin: 4.5px 0 !important;
                font-size: 10px !important;
            }

            @page {
                size: A4 portrait;
                margin: 6mm 8mm 6mm 8mm;
            }
        }
    """
    
    # 1. Tạo trang bìa và mục lục
    toc_rows = ""
    for idx, lesson in enumerate(LESSONS, 1):
        filename = make_filename(lesson['title'])
        toc_rows += f"""
        <tr>
            <td style="font-weight: 700; padding: 12px 0; border: none;"><a href="./{filename}" style="color: var(--primary-color); text-decoration: none;">{lesson['title']}</a></td>
            <td style="color: var(--dark-color); padding: 12px 0; text-align: right; border: none;">{lesson['toc_desc']}</td>
        </tr>"""
        
    cover_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trang Bìa & Mục Lục - Giáo Trình Tiếng Trung</title>
    <style>{css_content}</style>
</head>
<body>
    <div class="container">
        <div class="no-print print-btn-container">
            <button class="print-btn" onclick="window.print()">🖨️ In trang bìa & mục lục</button>
        </div>
        
        <!-- COVER PAGE -->
        <div class="cover-page">
            <div class="cover-badge">TÀI LIỆU HỌC VIÊN</div>
            <h1 class="cover-title">Phát Âm & Giao Tiếp Tiếng Trung Cơ Bản</h1>
        </div>
        
        <!-- TABLE OF CONTENTS -->
        <div style="page-break-before: always; padding-top: 20px;">
            <h1 class="lesson-title" style="border-bottom: 2px solid #000; margin-top: 0;">Mục Lục Giáo Trình</h1>
            <table style="border: none; width: 100%;">
                <thead>
                    <tr style="background-color: transparent; border-bottom: 2px solid #000;">
                        <th style="background: transparent; color: #000; padding: 12px 0; font-size: 16px; border: none;">Bài học</th>
                        <th style="background: transparent; color: #000; padding: 12px 0; text-align: right; font-size: 16px; border: none;">Nội dung chính</th>
                    </tr>
                </thead>
                <tbody>
                    {toc_rows}
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>"""

    with open(os.path.join(output_dir, "trang_bia_va_muc_luc.html"), "w", encoding="utf-8") as f:
        f.write(cover_html)
        
    # 2. Tạo từng bài học riêng biệt
    for idx, lesson in enumerate(LESSONS, 1):
        filename = make_filename(lesson['title'])
        lesson_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{lesson['title']}</title>
    <style>{css_content}</style>
</head>
<body>
    <div class="container lesson-{idx}">
        <div class="no-print print-btn-container">
            <button class="print-btn" onclick="window.print()">🖨️ In bài học này</button>
        </div>
        <h1 class="lesson-title">{lesson['title']}</h1>
        {lesson['content_html'].replace("{ASSETS_PATH}", "../assets")}
    </div>
</body>
</html>"""
        with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
            f.write(lesson_html)
            
    # 3. Tạo file tổng hợp giao_trinh_in_an.html ở thư mục gốc
    lessons_content = ""
    for idx, lesson in enumerate(LESSONS, 1):
        lessons_content += f"""
    <!-- PAGE BREAK FOR NEW LESSON -->
    <div class="page-break lesson-{idx}" style="page-break-before: always; padding-top: 20px;">
        <h1 class="lesson-title">{lesson['title']}</h1>
        {lesson['content_html'].replace("{ASSETS_PATH}", "assets")}
    </div>"""

    combined_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Giáo Trình Tiếng Trung Cơ Bản (Tổng Hợp)</title>
    <style>
        {css_content}
    </style>
</head>
<body>
    <div class="container">
        <div class="no-print print-btn-container">
            <button class="print-btn" onclick="window.print()">🖨️ In toàn bộ giáo trình</button>
        </div>
        
        <!-- COVER PAGE -->
        <div class="cover-page">
            <div class="cover-badge">TÀI LIỆU HỌC VIÊN</div>
            <h1 class="cover-title">Phát Âm & Giao Tiếp Tiếng Trung Cơ Bản</h1>
        </div>
        
        <!-- TABLE OF CONTENTS -->
        <div style="page-break-before: always; padding-top: 20px; page-break-after: always;">
            <h1 class="lesson-title" style="border-bottom: 2px solid #000; margin-top: 0;">Mục Lục Giáo Trình</h1>
            <table style="border: none; width: 100%;">
                <thead>
                    <tr style="background-color: transparent; border-bottom: 2px solid #000;">
                        <th style="background: transparent; color: #000; padding: 12px 0; font-size: 16px; border: none;">Bài học</th>
                        <th style="background: transparent; color: #000; padding: 12px 0; text-align: right; font-size: 16px; border: none;">Nội dung chính</th>
                    </tr>
                </thead>
                <tbody>
                    {toc_rows}
                </tbody>
            </table>
        </div>
        
        <!-- LESSONS -->
        {lessons_content}
    </div>
</body>
</html>"""

    with open("giao_trinh_in_an.html", "w", encoding="utf-8") as f:
        f.write(combined_html)
            
    print(f"Successfully generated {len(LESSONS)} individual lessons in folder '{output_dir}/' and combined file 'giao_trinh_in_an.html'.")

if __name__ == "__main__":
    build_individual_lessons()
    print("=== SYNC SUCCESSFUL ===")
