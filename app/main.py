from fastapi import FastAPI

from app.config.generate_credentials import generate_credentials
from app.routers import appointments

app = FastAPI()

generate_credentials()

app.include_router(appointments.router)
@app.get("/")
async def root():
    return {"status": "ok"}
