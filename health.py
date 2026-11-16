
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "application": "PolyGen AI",
        "version": "0.1.0"
    }
