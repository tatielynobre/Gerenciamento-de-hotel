from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from http import HTTPStatus

app = FastAPI()

##formato esperado
class Reserva(BaseModel):
        id_quarto: int
        id_cliente: int
        data_inicio: str
        data_fim: str
        nivel_quarto: str # Standard, Master, Deluxe

##apenas cod teste
@app.post('/reserva')
def criar_reserva(reserva: Reserva):
    id_reserva = max(reservas.keys()) + 1 if reservas else 1
    reservas[id_reserva] = reserva
    return {
        "message": "Reserva criada",
        "id_reserva": id_reserva,
        "dados": reserva
    }

reservas = {
    1: Reserva(id_quarto=101, id_cliente=202, data_inicio="2024-12-01", data_fim="2024-12-10", nivel_quarto="Deluxe"),
    2: Reserva(id_quarto=102, id_cliente=203, data_inicio="2024-12-05", data_fim="2024-12-12", nivel_quarto="Master")
}

@app.get("/reserva/{reserva_id}")
def exibir_reserva(reserva_id: int):
    if reserva_id in reservas:
         return reservas[reserva_id]  
    return {"message": "Reserva não encontrada"}

@app.delete("/reserva/{reserva_id}")
def apagar_reserva(reserva_id: int):
    if reserva_id not in reservas:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Reserva não encontrada.")
    
    del reservas[reserva_id]
    return {"message": "Reserva removida com sucesso!"}


@app.put("/reserva/{reserva_id}")
def atualizar_reserva(reserva_id: int, reserva_atualizada: Reserva):
    if reserva_id not in reservas:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Reserva não encontrada.")
    
    reservas[reserva_id] = reserva_atualizada
    return {
        "message": "Reserva atualizada com sucesso!",
        "id_reserva": reserva_id,
        "dados": reserva_atualizada
    }