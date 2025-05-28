import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# ✅ 모델 로드
model_name = "beomi/KcELECTRA-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# ✅ 감정 → 해시태그 매핑
label_to_tags = {
    "부정": ["bright", "citrus", "fresh"],
    "중립": ["clean", "mild", "musky"],
    "긍정": ["deep", "woody", "mysterious"]
}
labels = ["부정", "중립", "긍정"]

# ✅ 분석 함수
def analyze_sentiment_and_tags(text: str):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=1)
        predicted = torch.argmax(probs, dim=1).item()
    sentiment = labels[predicted]
    tags = label_to_tags.get(sentiment, ["neutral"])
    return sentiment, tags
