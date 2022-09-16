from fastapi import FastAPI

from app.config.generate_credentials import generate_credentials
from app.routers import appointments
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

generate_credentials()

app.include_router(appointments.router)
@app.get("/")
async def root():
    return {"status": "ok"}
