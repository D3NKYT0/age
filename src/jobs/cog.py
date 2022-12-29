from src.email.smtp import send_email
from src.schemas import schemas_custom


def send_email_task(email_data: schemas_custom.Email):
    send_email(email_data.content, email_data.subject, email_data.destination_email)
