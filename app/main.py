from fastapi import FastAPI
from routers import appointments
from config.generate_credentials import generate_credentials
app = FastAPI()

generate_credentials()

app.include_router(appointments.router)
@app.get("/")
async def root():
    return {"status": "ok"}
