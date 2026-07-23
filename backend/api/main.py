from fastapi import FastAPI
from backend.api.routers import generate
from backend.api.routers import upload
from backend.api.routers import auth
from backend.api.routers import evaluation
from backend.api.routers import voice
from fastapi.staticfiles import StaticFiles
app = FastAPI(
    title="Mirror AI API",
    description="Backend API for Mirror AI",
    version="1.0.0"
)

app.include_router(generate.router)
app.include_router(upload.router)
app.include_router(auth.router)
app.include_router(evaluation.router)
app.include_router(voice.router)

@app.get("/")
def root():
    return {"message": "Mirror AI Backend Running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads",
)