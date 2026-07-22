from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ApexIQ API",
    description="AI-powered Motorsport Knowledge Assistant",
    version="1.0.0",
)

# Permite comunicação com o frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Depois restringiremos isso
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
def root():
    return {
        "project": "ApexIQ",
        "message": "Welcome to ApexIQ API!"
    }


@app.get("/health", tags=["Health"])
def health():
    return {
        "status": "ok",
        "project": "ApexIQ",
        "version": "1.0.0"
    }