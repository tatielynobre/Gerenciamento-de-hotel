from fastapi import APIRouter, HTTPException
from http import HTTPStatus
from models import Reserva
from repositories.csv_manager import carregar_reservas, salvar_reserva_csv, apagar_reserva_csv, atualizar_reserva_csv

router = APIRouter()

@router.post('/reserva/')
def criar_reserva(reserva: Reserva):
    reservas = carregar_reservas()
    id_reserva = max(reservas.keys(), default=0) + 1  # Garante o ID único
    reservas[id_reserva] = reserva
    salvar_reserva_csv(id_reserva, reserva)  # Salva no CSV
    return {
        "message": "Reserva criada",
        "id_reserva": id_reserva,
        "dados": reserva
    }

@router.get("/reserva/")
def lista_total():
    return carregar_reservas()

@router.get("/reserva/{reserva_id}")
def exibir_reserva(reserva_id: int):
    reservas = carregar_reservas()
    if reserva_id not in reservas:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")
    return reservas[reserva_id]

@router.delete("/reserva/{reserva_id}")
def apagar_reserva(reserva_id: int):
    reservas = carregar_reservas()
    if reserva_id not in reservas:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Reserva não encontrada.")
    
    del reservas[reserva_id]
    apagar_reserva_csv(reservas)  # Atualiza o CSV após remoção
    return {"message": "Reserva removida com sucesso!"}

@router.put("/reserva/{reserva_id}")
def atualizar_reserva(reserva_id: int, reserva_atualizada: Reserva):
    reservas = carregar_reservas()
    if reserva_id not in reservas:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Reserva não encontrada.")
    
    reservas[reserva_id] = reserva_atualizada
    atualizar_reserva_csv(reservas)  # Atualiza o CSV após atualização
    return {
        "message": "Reserva atualizada com sucesso!",
        "id_reserva": reserva_id,
        "dados": reserva_atualizada
    }