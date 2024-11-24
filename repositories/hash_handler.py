import hashlib
from fastapi import APIRouter, HTTPException

router = APIRouter()

csv_file = 'files/reservas.csv'  # Caminho do arquivo CSV

def calcular_hash_csv():
    """
    Calcula o hash SHA256 do arquivo CSV.
    """
    try:
        sha256_hash = hashlib.sha256()
        with open(csv_file, mode='rb') as file:
            for chunk in iter(lambda: file.read(4096), b""):  # Lê o arquivo em blocos de 4 KB pra prevenir possiveis erros
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Arquivo CSV não encontrado.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao calcular hash: {str(e)}")


@router.get('/reserva/hash')
def obter_hash_csv():
    """
    Endpoint para retornar o hash SHA256 do arquivo CSV.
    """
    hash_csv = calcular_hash_csv()
    return {"hash_sha256": hash_csv}