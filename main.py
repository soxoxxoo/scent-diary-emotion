from fastapi import FastAPI
from app.routers import emotion_router

app = FastAPI()
app.include_router(emotion_router.router)
