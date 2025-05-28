from fastapi import FastAPI
from pydantic import BaseModel
from tagger import analyze_sentiment_and_tags

app = FastAPI(
    title="Scent Diary Emotion API",
    description="시향 일기 감정 분석 및 향수 태그 자동 추천 API",
    version="1.0.0"
)

class DiaryInput(BaseModel):
    text: str

@app.post("/analyze", summary="시향 일기 감정 분석", description="입력된 일기 내용을 기반으로 감정을 분류하고, 관련 향수 해시태그를 반환합니다.")
def analyze(diary: DiaryInput):
    sentiment, tags = analyze_sentiment_and_tags(diary.text)
    return {
        "sentiment": sentiment,
        "tags": tags
    }
