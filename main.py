from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Scent Diary Emotion API (Backend Only)",
    description="향수 앱 백엔드 전용 API",
    version="1.0.0"
)

class DiaryInput(BaseModel):
    text: str

@app.post("/analyze", summary="감정 분석 API (백엔드 테스트용)", description="감정 분석 모델 제거 후 더미 응답 반환")
def analyze(diary: DiaryInput):
    return {
        "sentiment": "중립",
        "tags": ["clean", "mild", "musky"]
    }

from app.routers import emotion_router

app = FastAPI()
app.include_router(emotion_router.router)

