from fastapi import Depends, status, APIRouter, BackgroundTasks
from fastapi_limiter.depends import RateLimiter
from src.resources.auth_utils import get_user_logged

# from src.infra.sqlalchemy.config.database import get_db
# from sqlalchemy.orm import Session

from src.schemas import schemas_authorization, schemas_classifier_user
from src.jobs import cog


router = APIRouter()


@router.post('/classifier', status_code=status.HTTP_202_ACCEPTED, response_model=schemas_classifier_user.ClassifierUser, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["god"])
def register_classifier(classifier_data: schemas_classifier_user.ClassifierUser):
    return classifier_data

@router.get('/authorization', status_code=status.HTTP_200_OK, response_model=schemas_authorization.Authorization, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["god"])
def register_auth(auth_data: schemas_authorization.Authorization):
    return auth_data
