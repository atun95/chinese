# -*- coding: utf-8 -*-
"""
Dialogue practice scenarios for classroom activities.
Each scenario contains:
- title: short description
- context: brief situation description
- characters: list of participant roles
- prompts: list of prompts for each participant to start the conversation
- example: optional example dialogue (Chinese characters, pinyin, translation)
"""

SCENARIOS = [
    {
        "title": "Mua đồ ăn ở chợ",
        "context": "Bạn và một người bán hàng đang ở chợ thực tế. Thực hành cách đặt giá và trả tiền.",
        "characters": ["Học viên", "Người bán"],
        "prompts": [
            "Bạn muốn mua một bó cải xanh, hỏi giá bao nhiêu?",
            "Bạn muốn hỏi có giảm giá không?",
        ],
        "example": {
            "Chinese": "请问，这束青菜多少钱？\n还有没有折扣？",
            "Pinyin": "Qǐngwèn, zhè shù qīngcài duōshǎo qián?\nHái yǒu méiyǒu zhékòu?",
            "Translation": "Excuse me, how much is this bunch of greens?\nIs there any discount?"
        }
    },
    {
        "title": "Đặt phòng khách sạn",
        "context": "Bạn đang gọi điện đặt phòng cho kỳ nghỉ.",
        "characters": ["Học viên", "Nhân viên lễ tân"],
        "prompts": [
            "Bạn muốn hỏi có phòng đôi có wifi miễn phí không?",
            "詢問入住和退房時間。"
        ],
        "example": {
            "Chinese": "您好，我想预订一个双人间，请问有免费WiFi吗？\n入住时间是几点，退房时间是几点？",
            "Pinyin": "Nín hǎo, wǒ xiǎng yùdìng yí gè shuāngrén jiān, qǐngwèn yǒu miǎnfèi WiFi ma?\nRùzhù shíjiān shì jǐ diǎn, tuìfáng shíjiān shì jǐ diǎn?",
            "Translation": "Hello, I'd like to book a double room, is there free WiFi?\nWhat are the check‑in and check‑out times?"
        }
    },
    {
        "title": "Hỏi đường đến thư viện",
        "context": "Bạn đang trên đường và cần hỏi người địa phương đường tới thư viện.",
        "characters": ["Học viên", "Người dân địa phương"],
        "prompts": [
            "请问，去图书馆怎么走？",
            "请问，最近的地铁站在哪里？"
        ],
        "example": {
            "Chinese": "请问，去图书馆怎么走？\n从这里坐地铁到最近的站要多久？",
            "Pinyin": "Qǐngwèn, qù túshūguǎn zěnme zǒu?\nCóng zhèlǐ zuò dìtiě dào zuìjìn de zhàn yào duōjiǔ?",
            "Translation": "Excuse me, how do I get to the library?\nHow long does it take by subway from here to the nearest station?"
        }
    }
]

def get_random_scenario():
    """Return a random scenario dictionary from SCENARIOS."""
    import random
    return random.choice(SCENARIOS)
