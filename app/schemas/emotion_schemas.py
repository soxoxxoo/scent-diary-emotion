from pydantic import BaseModel
from typing import List

class EmotionAnalysisRequest(BaseModel):
    sentence: str

class EmotionTaggingResponse(BaseModel):
    emotion: str
    tags: List[str]
