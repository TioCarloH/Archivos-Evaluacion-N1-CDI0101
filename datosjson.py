import json
from datetime import datetime, timedelta

def main():
    ruta_archivo = "/home/devasc/labs/devnet-src/parsing/myfile.json"
    with open(ruta_archivo) as archivo:
        json_file = json.load(archivo)

    token = json_file["access_token"]
    tiempo_expiracion = json_file["expires_in"]
    tiempo_restante_segundos = tiempo_expiracion
    
    print("Token:", token)
    print("Tiempo de expiración del token en segundos:", tiempo_restante_segundos)
if __name__ == "__main__":
    main()
