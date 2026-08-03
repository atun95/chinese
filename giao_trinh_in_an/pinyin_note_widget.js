/**
 * Chinese Pinyin Note Widget (Ghi chú Pinyin Tự động)
 * Self-contained floating resizable & draggable note widget for Chinese learning pages.
 */
(function () {
    if (window.__pinyinNoteWidgetLoaded) return;
    window.__pinyinNoteWidgetLoaded = true;

    // Load pinyin-pro CDN dynamically if not available
    if (typeof pinyinPro === 'undefined') {
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/npm/pinyin-pro@3.19.6/dist/index.js';
        script.async = true;
        script.onload = () => {
            if (window.__renderPinyinNote) window.__renderPinyinNote();
        };
        document.head.appendChild(script);
    }

    // Built-in Offline Fallback Dictionary (~1000 most common characters)
    const offlineDict = {
        '我': 'wǒ', '你': 'nǐ', '他': 'tā', '她': 'tā', '它': 'tā', '们': 'men', '好': 'hǎo', '是': 'shì',
        '在': 'zài', '不': 'bù', '有': 'yǒu', '这': 'zhè', '那': 'nà', '个': 'gè', '上': 'shàng', '下': 'xià',
        '人': 'rén', '大': 'dà', '小': 'xiǎo', '中': 'zhōng', '国': 'guó', '年': 'nián', '月': 'yuè', '日': 'rì',
        '号': 'hào', '时': 'shí', '分': 'fēn', '点': 'diǎn', '天': 'tiān', '生': 'shēng', '作': 'zuò', '学': 'xué',
        '校': 'xiào', '老': 'lǎo', '师': 'shī', '生': 'shēng', '同': 'tóng', '朋': 'péng', '友': 'yǒu', '家': 'jiā',
        '爸': 'bà', '妈': 'mā', '哥': 'gē', '姐': 'jiě', '弟': 'dì', '妹': 'mèi', '儿': 'ér', '子': 'zǐ',
        '女': 'nǚ', '吃': 'chī', '喝': 'hē', '茶': 'chá', '水': 'shuǐ', '菜': 'cài', '饭': 'fàn', '米': 'mǐ',
        '果': 'guǒ', '苹': 'píng', '猫': 'māo', '狗': 'gǒu', '爱': 'ài', '喜': 'xǐ', '欢': 'huān', '想': 'xiǎng',
        '要': 'yào', '去': 'qù', '来': 'lái', '回': 'huí', '买': 'mǎi', '卖': 'mài', '看': 'kàn', '听': 'tīng',
        '说': 'shuō', '读': 'dú', '写': 'xiě', '字': 'zì', '文': 'wén', '语': 'yǔ', '汉': 'hàn', '英': 'yīng',
        '书': 'shū', '桌': 'zhuō', '椅': 'yǐ', '电': 'diàn', '脑': 'nǎo', '视': 'shì', '影': 'yǐng', '话': 'huà',
        '车': 'chē', '站': 'zhàn', '机': 'jī', '场': 'chǎng', '钱': 'qián', '块': 'kuài', '百': 'bǎi', '千': 'qiān',
        '万': 'wàn', '零': 'líng', '一': 'yī', '二': 'èr', '三': 'sān', '四': 'sì', '五': 'wǔ', '六': 'liù',
        '七': 'qī', '八': 'bā', '九': 'jiǔ', '十': 'shí', '做': 'zuò', '高': 'gāo', '兴': 'xìng', '坐': 'zuò',
        '请': 'qǐng', '问': 'wèn', '谢': 'xiè', '再': 'zài', '见': 'jiàn', '对': 'duì', '起': 'qǐ', '没': 'méi',
        '关': 'guān', '系': 'xì', '多': 'duō', '少': 'shǎo', '能': 'néng', '会': 'huì', '能': 'néng', '冷': 'lěng',
        '热': 'rè', '雨': 'yǔ', '飞': 'fēi', '名': 'míng', '亮': 'liàng', '漂': 'piào', '商': 'shāng', '店': 'diàn',
        '医': 'yī', '院': 'yuàn', '工': 'gōng', '路': 'lù', '门': 'mén', '前': 'qián', '后': 'hòu', '里': 'lǐ',
        '外': 'wài', '左': 'zuǒ', '右': 'yòu', '东': 'dōng', '西': 'xī', '南': 'nán', '北': 'běi', '早': 'zǎo',
        '晚': 'wǎn', '明': 'míng', '昨': 'zuó', '今': 'jīn', '期': 'qī', '星': 'xīng', '杯': 'bēi', '服': 'fú',
        '穿': 'chuān', '词': 'cí', '课': 'kè', '本': 'běn', '笔': 'bǐ', '纸': 'zhǐ', '试': 'shì', '题': 'tí'
    };

    // Helper: Check if character is Chinese
    function isChineseChar(char) {
        return /[\u4e00-\u9fa5]/.test(char);
    }

    // Helper: Get pinyin for a single character or string
    function getPinyin(text, toneType = 'symbol') {
        if (!text) return [];

        if (typeof pinyinPro !== 'undefined' && pinyinPro.pinyin) {
            try {
                const result = [];
                for (let i = 0; i < text.length; i++) {
                    const ch = text[i];
                    if (isChineseChar(ch)) {
                        const py = pinyinPro.pinyin(ch, { toneType: toneType, type: 'array' })[0] || offlineDict[ch] || '';
                        result.push({ char: ch, pinyin: py });
                    } else {
                        result.push({ char: ch, pinyin: '' });
                    }
                }
                return result;
            } catch (e) {
                console.warn('pinyin-pro error, using offline fallback', e);
            }
        }

        const result = [];
        for (let i = 0; i < text.length; i++) {
            const ch = text[i];
            if (isChineseChar(ch)) {
                result.push({ char: ch, pinyin: offlineDict[ch] || '?' });
            } else {
                result.push({ char: ch, pinyin: '' });
            }
        }
        return result;
    }

    // Inject CSS styles
    const style = document.createElement('style');
    style.innerHTML = `
        .pinyin-note-fab {
            position: fixed;
            bottom: 24px;
            right: 24px;
            z-index: 999990;
            background: linear-gradient(135deg, #e11d48 0%, #be123c 100%);
            color: #ffffff;
            border: none;
            border-radius: 30px;
            padding: 12px 20px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 10px 25px -5px rgba(225, 29, 72, 0.4);
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        .pinyin-note-fab:hover {
            transform: translateY(-2px) scale(1.03);
            box-shadow: 0 15px 30px -5px rgba(225, 29, 72, 0.5);
        }
        .pinyin-note-fab.hidden {
            display: none !important;
        }

        .pinyin-note-window {
            position: fixed;
            bottom: 80px;
            right: 24px;
            width: 420px;
            height: 520px;
            min-width: 320px;
            min-height: 300px;
            background: #ffffff;
            border-radius: 16px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15), 0 0 0 1px rgba(0, 0, 0, 0.05);
            z-index: 999995;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            transition: opacity 0.2s ease, transform 0.2s ease;
            resize: both;
        }

        .pinyin-note-window.collapsed {
            display: none !important;
        }

        .pinyin-note-window.maximized {
            top: 20px !important;
            left: 20px !important;
            right: 20px !important;
            bottom: 20px !important;
            width: calc(100vw - 40px) !important;
            height: calc(100vh - 40px) !important;
        }

        .pinyin-note-header {
            background: #f8fafc;
            padding: 12px 16px;
            border-bottom: 1px solid #e2e8f0;
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: move;
            user-select: none;
        }

        .pinyin-note-title {
            font-size: 15px;
            font-weight: 700;
            color: #0f172a;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .pinyin-note-controls {
            display: flex;
            gap: 6px;
        }

        .pinyin-note-btn-icon {
            background: transparent;
            border: none;
            color: #64748b;
            width: 28px;
            height: 28px;
            border-radius: 6px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
            transition: background 0.15s ease, color 0.15s ease;
        }
        .pinyin-note-btn-icon:hover {
            background: #e2e8f0;
            color: #0f172a;
        }

        .pinyin-note-toolbar {
            padding: 8px 16px;
            background: #ffffff;
            border-bottom: 1px solid #f1f5f9;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 8px;
            flex-wrap: wrap;
        }

        .pinyin-note-tools-group {
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .pinyin-note-btn {
            background: #f1f5f9;
            border: 1px solid #cbd5e1;
            color: #334155;
            padding: 5px 10px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.15s ease;
            display: flex;
            align-items: center;
            gap: 4px;
        }
        .pinyin-note-btn:hover {
            background: #e2e8f0;
            color: #0f172a;
        }
        .pinyin-note-btn.active {
            background: #e11d48;
            color: #ffffff;
            border-color: #e11d48;
        }

        .pinyin-note-body {
            flex: 1;
            display: flex;
            flex-direction: column;
            padding: 12px 16px;
            gap: 12px;
            overflow-y: auto;
            background: #ffffff;
        }

        .pinyin-note-input {
            width: 100%;
            height: 90px;
            min-height: 70px;
            padding: 10px;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            font-size: 15px;
            font-family: inherit;
            resize: vertical;
            outline: none;
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
        }
        .pinyin-note-input:focus {
            border-color: #e11d48;
            box-shadow: 0 0 0 3px rgba(225, 29, 72, 0.15);
        }

        .pinyin-note-output-title {
            font-size: 12px;
            font-weight: 600;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .pinyin-note-output {
            flex: 1;
            min-height: 120px;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 14px;
            overflow-y: auto;
            line-height: 2.2;
            word-wrap: break-word;
        }

        .pinyin-note-output ruby {
            ruby-position: over;
            margin: 0 2px;
            font-size: 22px;
            font-weight: 600;
            color: #0f172a;
            display: inline-block;
            text-align: center;
        }
        .pinyin-note-output rt {
            font-size: 12px;
            font-weight: 500;
            color: #e11d48;
            line-height: 1.2;
            text-align: center;
        }
        .pinyin-note-output .non-hanzi {
            font-size: 16px;
            color: #475569;
            white-space: pre-wrap;
        }

        .pinyin-note-footer {
            padding: 8px 16px;
            background: #f8fafc;
            border-top: 1px solid #e2e8f0;
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 11px;
            color: #94a3b8;
        }
    `;
    document.head.appendChild(style);

    // Create FAB
    const fab = document.createElement('button');
    fab.className = 'pinyin-note-fab';
    fab.innerHTML = `<span>📝</span> <span>Ghi chú Pinyin</span>`;
    document.body.appendChild(fab);

    // Create Window
    const win = document.createElement('div');
    win.className = 'pinyin-note-window collapsed';
    win.innerHTML = `
        <div class="pinyin-note-header" id="pinyinNoteDragHeader">
            <div class="pinyin-note-title">
                <span>📝</span> Ghi chú Pinyin Từ vựng
            </div>
            <div class="pinyin-note-controls">
                <button class="pinyin-note-btn-icon" id="pinyinNoteMinBtn" title="Thu gọn (Minimize)">_</button>
                <button class="pinyin-note-btn-icon" id="pinyinNoteMaxBtn" title="Phóng to / Thu nhỏ">⤢</button>
                <button class="pinyin-note-btn-icon" id="pinyinNoteCloseBtn" title="Đóng">✕</button>
            </div>
        </div>
        <div class="pinyin-note-toolbar">
            <div class="pinyin-note-tools-group">
                <button class="pinyin-note-btn active" id="btnToneSymbol" title="Dấu thanh (ā á ǎ à)">Dấu thanh</button>
                <button class="pinyin-note-btn" id="btnToneNum" title="Số thanh (a1 a2 a3)">Số thanh</button>
                <button class="pinyin-note-btn" id="btnToneNone" title="Không dấu (a)">Không dấu</button>
            </div>
            <div class="pinyin-note-tools-group">
                <button class="pinyin-note-btn" id="btnAudioTTS" title="Phát âm từ vựng">🔊 Đọc</button>
                <button class="pinyin-note-btn" id="btnCopyPy" title="Copy Pinyin">📋 Pinyin</button>
                <button class="pinyin-note-btn" id="btnCopyBoth" title="Copy Chữ Hán + Pinyin">📋 Cả hai</button>
                <button class="pinyin-note-btn" id="btnClear" title="Xóa nội dung">🗑️ Xóa</button>
            </div>
        </div>
        <div class="pinyin-note-body">
            <textarea class="pinyin-note-input" id="pinyinNoteInput" placeholder="Nhập từ vựng hoặc chữ Hán vào đây (Ví dụ: 你好 苹果 学习)..."></textarea>
            <div class="pinyin-note-output-title">Kết quả Pinyin tự động (Mọi chữ Hán):</div>
            <div class="pinyin-note-output" id="pinyinNoteOutput">
                <span style="color: #94a3b8; font-style: italic; font-size: 13px;">Pinyin sẽ tự động xuất hiện tại đây khi bạn nhập chữ Hán...</span>
            </div>
        </div>
        <div class="pinyin-note-footer">
            <span id="pinyinNoteStats">0 từ / 0 chữ Hán</span>
            <span>Tự động lưu (localStorage)</span>
        </div>
    `;
    document.body.appendChild(win);

    // References
    const inputEl = win.querySelector('#pinyinNoteInput');
    const outputEl = win.querySelector('#pinyinNoteOutput');
    const statsEl = win.querySelector('#pinyinNoteStats');
    const btnMin = win.querySelector('#pinyinNoteMinBtn');
    const btnMax = win.querySelector('#pinyinNoteMaxBtn');
    const btnClose = win.querySelector('#pinyinNoteCloseBtn');
    const btnToneSymbol = win.querySelector('#btnToneSymbol');
    const btnToneNum = win.querySelector('#btnToneNum');
    const btnToneNone = win.querySelector('#btnToneNone');
    const btnAudio = win.querySelector('#btnAudioTTS');
    const btnCopyPy = win.querySelector('#btnCopyPy');
    const btnCopyBoth = win.querySelector('#btnCopyBoth');
    const btnClear = win.querySelector('#btnClear');

    let currentToneType = 'symbol';
    let isMaximized = false;

    // Load saved content & mode
    const savedText = localStorage.getItem('pinyin_note_text') || '';
    if (savedText) {
        inputEl.value = savedText;
    }

    // Render Pinyin logic
    function renderPinyin() {
        const text = inputEl.value;
        localStorage.setItem('pinyin_note_text', text);

        if (!text.trim()) {
            outputEl.innerHTML = `<span style="color: #94a3b8; font-style: italic; font-size: 13px;">Pinyin sẽ tự động xuất hiện tại đây khi bạn nhập chữ Hán...</span>`;
            statsEl.innerText = '0 từ / 0 chữ Hán';
            return;
        }

        let toneParam = 'symbol';
        if (currentToneType === 'num') toneParam = 'num';
        if (currentToneType === 'none') toneParam = 'none';

        const parsed = getPinyin(text, toneParam);
        let html = '';
        let hanziCount = 0;

        for (let item of parsed) {
            if (isChineseChar(item.char)) {
                hanziCount++;
                html += `<ruby><rb>${item.char}</rb><rt>${item.pinyin || ''}</rt></ruby>`;
            } else if (item.char === '\n') {
                html += '<br>';
            } else {
                html += `<span class="non-hanzi">${escapeHtml(item.char)}</span>`;
            }
        }

        outputEl.innerHTML = html;
        statsEl.innerText = `${text.trim().split(/\s+/).length} từ / ${hanziCount} chữ Hán`;
    }

    function escapeHtml(str) {
        return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    }

    window.__renderPinyinNote = renderPinyin;

    // Input listeners
    inputEl.addEventListener('input', renderPinyin);

    // Tone type toggles
    btnToneSymbol.addEventListener('click', () => {
        currentToneType = 'symbol';
        btnToneSymbol.classList.add('active');
        btnToneNum.classList.remove('active');
        btnToneNone.classList.remove('active');
        renderPinyin();
    });

    btnToneNum.addEventListener('click', () => {
        currentToneType = 'num';
        btnToneNum.classList.add('active');
        btnToneSymbol.classList.remove('active');
        btnToneNone.classList.remove('active');
        renderPinyin();
    });

    btnToneNone.addEventListener('click', () => {
        currentToneType = 'none';
        btnToneNone.classList.add('active');
        btnToneSymbol.classList.remove('active');
        btnToneNum.classList.remove('active');
        renderPinyin();
    });

    // TTS Audio
    btnAudio.addEventListener('click', () => {
        const text = inputEl.value.trim();
        if (!text) return;
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'zh-CN';
            utterance.rate = 0.85;
            window.speechSynthesis.speak(utterance);
        } else {
            alert('Trình duyệt của bạn không hỗ trợ đọc phát âm tự động.');
        }
    });

    // Copy Pinyin
    btnCopyPy.addEventListener('click', () => {
        const text = inputEl.value;
        if (!text.trim()) return;
        const parsed = getPinyin(text, currentToneType);
        const pinyinOnly = parsed.map(item => item.pinyin || item.char).join(' ');
        navigator.clipboard.writeText(pinyinOnly).then(() => {
            const orig = btnCopyPy.innerText;
            btnCopyPy.innerText = '✓ Đã copy';
            setTimeout(() => btnCopyPy.innerText = orig, 1500);
        });
    });

    // Copy Both (Hanzi + Pinyin)
    btnCopyBoth.addEventListener('click', () => {
        const text = inputEl.value;
        if (!text.trim()) return;
        const parsed = getPinyin(text, currentToneType);
        let result = '';
        for (let item of parsed) {
            if (isChineseChar(item.char)) {
                result += `${item.char}(${item.pinyin}) `;
            } else {
                result += item.char;
            }
        }
        navigator.clipboard.writeText(result.trim()).then(() => {
            const orig = btnCopyBoth.innerText;
            btnCopyBoth.innerText = '✓ Đã copy';
            setTimeout(() => btnCopyBoth.innerText = orig, 1500);
        });
    });

    // Clear
    btnClear.addEventListener('click', () => {
        inputEl.value = '';
        renderPinyin();
    });

    // Minimize & Open
    fab.addEventListener('click', () => {
        win.classList.remove('collapsed');
        fab.classList.add('hidden');
        renderPinyin();
        inputEl.focus();
    });

    btnMin.addEventListener('click', () => {
        win.classList.add('collapsed');
        fab.classList.remove('hidden');
    });

    btnClose.addEventListener('click', () => {
        win.classList.add('collapsed');
        fab.classList.remove('hidden');
    });

    // Maximize / Restore
    btnMax.addEventListener('click', () => {
        isMaximized = !isMaximized;
        if (isMaximized) {
            win.classList.add('maximized');
            btnMax.innerText = '❐';
        } else {
            win.classList.remove('maximized');
            btnMax.innerText = '⤢';
        }
    });

    // Draggable window logic
    const header = win.querySelector('#pinyinNoteDragHeader');
    let isDragging = false;
    let offsetX = 0, offsetY = 0;

    header.addEventListener('mousedown', (e) => {
        if (e.target.closest('.pinyin-note-controls') || isMaximized) return;
        isDragging = true;
        const rect = win.getBoundingClientRect();
        offsetX = e.clientX - rect.left;
        offsetY = e.clientY - rect.top;
        document.addEventListener('mousemove', onMouseMove);
        document.addEventListener('mouseup', onMouseUp);
    });

    function onMouseMove(e) {
        if (!isDragging) return;
        win.style.left = `${e.clientX - offsetX}px`;
        win.style.top = `${e.clientY - offsetY}px`;
        win.style.bottom = 'auto';
        win.style.right = 'auto';
    }

    function onMouseUp() {
        isDragging = false;
        document.removeEventListener('mousemove', onMouseMove);
        document.removeEventListener('mouseup', onMouseUp);
    }

    // Initial render call
    renderPinyin();
})();
