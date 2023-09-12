import smtplib
import re
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def get_smtp_server(email):
    # Define una lista de servidores SMTP
    smtp_servers = {
        "gmail.com": "smtp.gmail.com",
        "outlook.com": "smtp-mail.outlook.com",
        "hotmail.com": "smtp-mail.outlook.com",
        "live.com": "smtp-mail.outlook.com",
        "yahoo.com": "smtp.mail.yahoo.com"
    }

    # Usa una expresión regular para extraer el dominio del correo electrónico
    domain = re.search("@[\w.]+", email)

    # Busca el servidor SMTP en la lista usando el dominio del correo electrónico
    smtp_server = smtp_servers.get(domain.group().replace("@",""))

    return smtp_server

def send_email():
    # Intenta leer los datos del archivo
    try:
        with open('email_data.txt', 'r') as f:
            sender_email = f.readline().strip()
            password = f.readline().strip()
            recipient_email = f.readline().strip()
    except FileNotFoundError:
        # Si el archivo no existe, solicita los datos al usuario y los guarda en el archivo
        sender_email = input("Por favor, ingresa tu correo electrónico: ")
        password = input("Por favor, ingresa tu contraseña: ")
        recipient_email = input("Por favor, ingresa el correo electrónico del destinatario: ")

        with open('email_data.txt', 'w') as f:
            f.write(sender_email + '\n')
            f.write(password + '\n')
            f.write(recipient_email + '\n')

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'Reporte diario de países'

    attachment = open('countries.xlsx', 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % 'countries.xlsx')

    msg.attach(part)

    smtp_server = get_smtp_server(sender_email)
    
    server = smtplib.SMTP(smtp_server, 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)
    server.quit()
