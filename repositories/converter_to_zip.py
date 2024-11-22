#Convertendo o csv para arquivo zip
import zipfile ##precisa especificar qual o arquivo csv que ele vai compactar

def Compact_csv(csv_file):
    zip_file = f"{csv_file}.zip"
    with zipfile.ZipFile(csv_file, 'w') as zip:
            zip.write(csv_file)
    return zip_file
