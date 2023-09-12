import pandas as pd
from fetch_data import fetch_data
from metrics import metrics
from email_send import send_email

def main():
    # Obtiene y procesa los datos
    countries = fetch_data()

    # Crea un DataFrame con los datos de los países
    df = pd.DataFrame(countries)

    # Guarda el DataFrame en un archivo Excel
    with pd.ExcelWriter('countries.xlsx') as writer:
        df.to_excel(writer, sheet_name='Paises')
    # Agrego las estadisticas en el Archivo Excel
    metrics()
    # Envía el correo electrónico con el archivo Excel adjunto
    send_email()

    

if __name__ == "__main__":
    main()
