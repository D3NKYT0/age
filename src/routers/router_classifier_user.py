from fastapi import Depends, status, APIRouter, HTTPException
from fastapi_limiter.depends import RateLimiter
from src.resources.utils import add_create_at_timestamp

from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.resources.auth_utils import get_user_logged
from src.resources.utils import check_authorization

from src.schemas import schemas_classifier_user
from src.infra.sqlalchemy.repository.repo_classifier_user import RepositoryClassifierUser


router = APIRouter()


@router.post('/classifier', status_code=status.HTTP_201_CREATED, response_model=schemas_classifier_user.ClassifierUser, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["classifier_users"])
def register_classifier(classifier_data: schemas_classifier_user.ClassifierUser, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    classifier_data = add_create_at_timestamp(classifier_data)

    exist_auth = RepositoryAuthorization(db).searchById(classifier_data.authorization_id)

    if not exist_auth:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Althorization not found!")

    exist = RepositoryClassifierUser(db).searchByDescription(classifier_data.description)

    if exist:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Already existing classification!")

    classifier_created = RepositoryClassifierUser(db).register_classifier_user(classifier_data)

    return classifier_created