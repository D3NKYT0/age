import json
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


with open("auth/data/auth.json", encoding="utf-8") as auth_data:
    _auth_data = json.load(auth_data)


# Configuração
host = _auth_data['SMTP_HOST']
port = 587
user = _auth_data['SMTP_EMAIL']
password = _auth_data['SMTP_PASSWORD']


def send_email(message: str, subject: str, to_email: str):
    """Envio de email

    Entendendo os parametros:
    message -- corpo do email
    subject -- assunto do email
    to_email -- email de destino
    """

    # Criando objeto
    server = smtplib.SMTP(host, port)

    # Login com servidor
    server.ehlo()
    server.starttls()
    server.login(user, password)

    # Criando mensagem
    email_msg = MIMEMultipart()
    email_msg['From'] = user
    email_msg['To'] = to_email
    email_msg['Subject'] = subject
    email_msg.attach(MIMEText(message, 'plain'))

    # Enviando mensagem
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
    server.quit()
