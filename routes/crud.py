from basemodel import Reserva
from fastapi import APIRouter, HTTPException
from http import HTTPStatus


router = APIRouter()

@router.post('/reserva/')
def criar_reserva(reserva: Reserva):
    id_reserva = max(reservas.keys()) + 1 if reservas else 1 # precisa arrumar essa parte das reservas pra ele ir atualizando diretamente no csv
    reservas[id_reserva] = reserva
    return {
        "message": "Reserva criada",
        "id_reserva": id_reserva,
        "dados": reserva
    }

@router.get("/reserva/")
def lista_total():
    return reservas

@router.get("/reserva/{reserva_id}")
def exibir_reserva(reserva_id: int):
    if reserva_id in reservas:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")
    return reservas[reserva_id]  

@router.delete("/reserva/{reserva_id}")  # noqa: F821
def apagar_reserva(reserva_id: int):
    if reserva_id not in reservas:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Reserva não encontrada.")
    
    del reservas[reserva_id]
    return {"message": "Reserva removida com sucesso!"}


@router.put("/reserva/{reserva_id}")
def atualizar_reserva(reserva_id: int, reserva_atualizada: Reserva):
    if reserva_id not in reservas:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Reserva não encontrada.")
    
    reservas[reserva_id] = reserva_atualizada
    return {
        "message": "Reserva atualizada com sucesso!",
        "id_reserva": reserva_id,
        "dados": reserva_atualizada
    }