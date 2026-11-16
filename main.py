
from fastapi import FastAPI
from health import router as health_router

app = FastAPI(
    title="PolyGen AI",
    description="AI-powered 3D model generation and optimization platform",
    version="0.1.0"
)

app.include_router(health_router, prefix="/api/v1", tags=["Health"])


@app.get("/")
async def root():
    return {
        "message": "Welcome to PolyGen AI",
        "version": "0.1.0"
    }
