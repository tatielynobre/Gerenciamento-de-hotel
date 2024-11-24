from fastapi import FastAPI, HTTPException
from http import HTTPStatus
from routes.crud import router as reservas_router
from repositories.hash_handler import router as hash_router
from repositories.converter_to_zip import router as zip_router

app = FastAPI()

app.include_router(reservas_router, prefix="/api/v1", tags=["Reservas"])
app.include_router(hash_router, prefix="/hash", tags=["Hash"])
app.include_router(zip_router, prefix="/zip", tags=["Compactação"])

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao sistema de reservas!"}