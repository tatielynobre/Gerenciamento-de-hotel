#Convertendo o csv para arquivo zip
import zipfile

def Compact_csv(csv_file):
    zip_file = f"{csv_file}.zip"
    with zipfile.ZipFile('csv_file', 'w') as zip:
            zip.write(csv_file)
    return zip_file