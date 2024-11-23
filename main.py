from fastapi import FastAPI, HTTPException
from http import HTTPStatus
from routes.crud import router as reservas_router

app = FastAPI()

app.include_router(reservas_router, prefix="/api/v1", tags=["Reservas"])

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao sistema de reservas!"}