from fastapi import Depends, status, APIRouter, HTTPException
from fastapi_limiter.depends import RateLimiter
from src.resources.utils import add_create_at_timestamp

from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db

from src.schemas import schemas_authorization, schemas_classifier_user
from src.infra.sqlalchemy.repository.repo_authorization import RepositoryAuthorization
from src.infra.sqlalchemy.repository.repo_classifier_user import RepositoryClassifierUser


router = APIRouter()


@router.post('/classifier', status_code=status.HTTP_201_CREATED, response_model=schemas_classifier_user.ClassifierUser, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["god"])
def register_classifier(classifier_data: schemas_classifier_user.ClassifierUser, db: Session = Depends(get_db)):

    classifier_data = add_create_at_timestamp(classifier_data)

    exist_auth = RepositoryAuthorization(db).searchById(classifier_data.authorization_id)

    if not exist_auth:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Althorization not found!")

    exist = RepositoryClassifierUser(db).searchByDescription(classifier_data.description)

    if exist:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Already existing classification!")

    classifier_created = RepositoryClassifierUser(db).register_classifier_user(classifier_data)

    return classifier_created

@router.get('/authorization', status_code=status.HTTP_201_CREATED, response_model=schemas_authorization.Authorization, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["god"])
def register_auth(auth_data: schemas_authorization.Authorization, db: Session = Depends(get_db)):

    auth_data = add_create_at_timestamp(auth_data)

    exist = RepositoryAuthorization(db).searchByDescription(auth_data.description)

    if exist:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Already existing authorizarion!")

    authorization_created = RepositoryAuthorization(db).register_authorization(auth_data)

    return authorization_created
