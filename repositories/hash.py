import hashlib

csv_file = 'files/reservas.csv'
def return_hash():
    with open(csv_file, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()