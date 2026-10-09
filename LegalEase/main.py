from fastapi import FastAPI
from routes import router

app = FastAPI(title="LegalEase API")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "LegalEase backend is running"}
