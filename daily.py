import schedule
import time
from main import main
from datetime import datetime 

def job():
    # Ejecuta tu función principal
    main()
now = datetime.now()

# Programa la tarea para que se ejecute una vez al día
job()
schedule.every().day.at(now.strftime("%H:%M:%S")).do(job)

while True:
    # Ejecuta las tareas programadas
    schedule.run_pending()
    time.sleep(1)
