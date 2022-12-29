from fastapi import Depends, status, APIRouter, BackgroundTasks
from fastapi_limiter.depends import RateLimiter
from src.resources.auth_utils import get_user_logged

# from src.infra.sqlalchemy.config.database import get_db
# from sqlalchemy.orm import Session

from src.schemas import schemas_custom, schemas_users
from src.jobs import cog


router = APIRouter()


@router.post('/email', status_code=status.HTTP_202_ACCEPTED, response_model=schemas_custom.Email, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["ti"])
def send_email(email_data: schemas_custom.Email, background: BackgroundTasks = Depends(get_user_logged)):
    background.add_task(cog.send_email_task, email_data)
    return email_data

@router.get('/me', status_code=status.HTTP_200_OK, response_model=schemas_users.SimpleUser, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["ti"])
def me(user: schemas_users.User = Depends(get_user_logged)):
    return user
    