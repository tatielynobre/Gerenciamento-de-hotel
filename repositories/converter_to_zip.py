import os
import zipfile
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter()

csv_file = "files/reservas.csv"
zip_file = "files/reservas.zip"

def compactar_csv():
    """
    Compacta o arquivo CSV em um arquivo ZIP.
    """
    try:
        if not os.path.exists(csv_file):
            raise FileNotFoundError("Arquivo CSV não encontrado.")
        
        # Cria o arquivo ZIP
        with zipfile.ZipFile(zip_file, mode="w", compression=zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(csv_file, os.path.basename(csv_file))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao compactar arquivo: {str(e)}")


@router.get("/reserva/compactar", response_class=FileResponse)
def baixar_csv_compactado():
    """
    Endpoint para compactar o arquivo CSV e retornar o ZIP.
    """
    compactar_csv()
    
    # Verifica se o ZIP foi criado corretamente
    if not os.path.exists(zip_file):
        raise HTTPException(status_code=500, detail="Erro ao criar o arquivo ZIP.")
    
    return FileResponse(
        path=zip_file,
        media_type="application/zip",
        filename=os.path.basename(zip_file)
    )
