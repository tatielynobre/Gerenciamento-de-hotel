from pydantic import BaseModel

##formato esperado
class Reserva(BaseModel):
        id_quarto: int
        id_cliente: int
        data_inicio: str
        data_fim: str
        nivel_quarto: str # Standard, Master, Deluxe
