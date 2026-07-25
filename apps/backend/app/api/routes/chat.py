from fastapi import APIRouter

from app.models.chat import ChatRequest, ChatResponse
from app.services.ai_engine import AIEngine

router = APIRouter(tags=["Chat"])

engine = AIEngine()


@router.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(request: ChatRequest):

    result = engine.ask(request.question)

    return ChatResponse(
        question=result["question"],
        answer=result["answer"],
        sources=result["sources"],
    )