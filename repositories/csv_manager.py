import csv
from fastapi import HTTPException
from models import Reserva

# Definindo os campos que vão para o CSV
csv_file = 'files/reservas.csv'
campos = ['id_reserva', 'id_cliente', 'id_quarto', 'data_inicio', 'data_fim', 'nivel_quarto']

# Função para carregar reservas do CSV
def carregar_reservas():
    reservas = {}
    try:
        with open(csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                reservas[int(row['id_reserva'])] = row
    except FileNotFoundError:
        pass  # Se o arquivo não existir, retornar um dicionário vazio
    return reservas


# Função para salvar uma nova reserva no CSV
def salvar_reserva_csv(reserva_id, reserva: Reserva):
    try:
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=campos)
            if file.tell() == 0:  # Escreve o cabeçalho apenas se o arquivo estiver vazio
                writer.writeheader()
            
            # Convertendo o objeto 'Reserva' para dicionário e adicionando o 'id_reserva'
            reserva_dict = reserva.model_dump()  # Pydantic converte para dict
            reserva_dict['id_reserva'] = reserva_id  # Adiciona o ID gerado
            writer.writerow(reserva_dict)  # Escreve a linha no CSV
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao salvar reserva no CSV: {str(e)}")
    
# Função para apagar uma reserva do CSV
def apagar_reserva_csv(reservas):
    try:
        with open('files/reservas.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=campos)
            writer.writeheader()
            for id_, reserva in reservas.items():
                writer.writerow({'id_quarto': id_, **reserva})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar o CSV: {str(e)}")

# Função para atualizar as reservas no CSV
def atualizar_reserva_csv(reservas):
    try:
        with open('files/reservas.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=campos)
            writer.writeheader()
            for id_, reserva in reservas.items():
                writer.writerow({'id_quarto': id_, **reserva})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar o CSV: {str(e)}")