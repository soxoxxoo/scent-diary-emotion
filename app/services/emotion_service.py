emotion_to_tags = {
    "기쁨": ["#joyful", "#bright", "#citrus"],
    "불안": ["#nervous", "#sharp", "#spicy"],
    "당황": ["#confused", "#mild", "#powdery"],
    "분노": ["#angry", "#hot", "#burntwood"],
    "상처": ["#hurt", "#cool", "#woody"],
    "슬픔": ["#sad", "#deep", "#musk"],
    "우울": ["#depressed", "#dark", "#leather"],
    "흥분": ["#excited", "#fresh", "#green"]
}

def analyze_emotion(sentence: str) -> str:
    if "기뻐" in sentence or "행복" in sentence:
        return "기쁨"
    elif "우울" in sentence or "지쳐" in sentence:
        return "우울"
    elif "슬퍼" in sentence:
        return "슬픔"
    elif "화나" in sentence or "짜증" in sentence:
        return "분노"
    else:
        return "불안"  # 기본 감정

def get_tags(emotion: str):
    return emotion_to_tags.get(emotion, [])
