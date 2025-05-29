from fastapi import APIRouter
from app.schemas.emotion_schemas import EmotionAnalysisRequest, EmotionTaggingResponse
from app.services.emotion_service import analyze_emotion, get_tags

router = APIRouter()

@router.post("/emotion-tagging", response_model=EmotionTaggingResponse)
def emotion_tagging(request: EmotionAnalysisRequest):
    emotion = analyze_emotion(request.sentence)
    tags = get_tags(emotion)
    return EmotionTaggingResponse(emotion=emotion, tags=tags)
