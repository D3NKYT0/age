from fastapi import Depends, status, APIRouter, HTTPException, BackgroundTasks

from sqlalchemy.orm import Session

from src.schemas import schemas_custom
from src.infra.sqlalchemy.config.database import get_db
from src.jobs import cog
from src.email.smtp import send_email


router = APIRouter()


@router.post('/email', status_code=status.HTTP_202_ACCEPTED, response_model=schemas_custom.Email, tags=["email"])
def enviar_email(email_data: schemas_custom.Email, background: BackgroundTasks):
    background.add_task(cog.send_email_task, email_data)
    return email_data
