#Convertendo o csv para arquivo zip
import zipfile
import os

csv_file = 'files/reservas.csv'

def Compact_csv(csv_file):
        if not os.path.isfile(csv_file):
                raise FileNotFoundError(f"O arquivo '{csv_file}' não foi encontrado.")
        zip_file = f"{csv_file}.zip"
        with zipfile.ZipFile(csv_file, 'w') as zip:
            zip.write(csv_file)
        return zip_file