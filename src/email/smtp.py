import ssl
import json
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


with open("auth/data/auth.json", encoding="utf-8") as auth_data:
    _auth_data = json.load(auth_data)


# Configuração
_host = _auth_data['SMTP_HOST']
_port = _auth_data['SMTP_PORT']
_user = _auth_data['SMTP_USER']
_pass = _auth_data['SMTP_PASS']
_mail = _auth_data['SMTP_MAIL']

# SSL contexto
_context = ssl.create_default_context()


def send_email(content: str, subject: str, destination_email: str):

    # Criando mensagem
    email_msg = MIMEMultipart()
    email_msg['From'] = _mail
    email_msg['To'] = destination_email
    email_msg['Subject'] = subject
    email_msg.attach(MIMEText(content, 'plain'))

    with smtplib.SMTP(_host, _port) as server:
        server.ehlo()
        server.starttls(context=_context)
        server.login(_user, _pass)

        # Enviando mensagem
        server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
