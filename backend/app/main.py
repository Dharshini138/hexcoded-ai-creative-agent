from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.creative import router as creative_router


app = FastAPI(
    title="HexCoded Creative Director API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "HexCoded Creative Director"
    }


app.include_router(
    creative_router,
    prefix="/api/creative",
    tags=["Creative Director"]
)