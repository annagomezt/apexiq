from fastapi import APIRouter

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.get("/")
def documents():
    return {
        "message": "Coming soon..."
    }