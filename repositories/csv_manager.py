#Cod de manipulações do csv
import csv

csv_file ="reservas.csv"
campos=['id_quarto','id_cliente','data_inicio','data_fim','nivel_quarto']

#teste csv
def iniciar_csv():
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()

def add_reserva_csv(reserva):
    with open(csv_file, mode="a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writerow(reserva)
##fim
