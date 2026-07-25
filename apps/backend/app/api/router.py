from fastapi import APIRouter

from app.api.routes import health
from app.api.routes import documents
from app.api.routes import chat

api_router = APIRouter()

api_router.include_router(health.router)
api_router.include_router(documents.router)
api_router.include_router(chat.router)