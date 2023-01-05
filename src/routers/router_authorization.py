from fastapi import Depends, status, APIRouter, HTTPException
from fastapi_limiter.depends import RateLimiter
from src.resources.utils import add_create_at_timestamp

from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.resources.auth_utils import get_user_logged
from src.resources.utils import check_authorization

from src.schemas import schemas_authorization
from src.infra.sqlalchemy.repository.repo_authorization import RepositoryAuthorization



router = APIRouter()

@router.post('/authorization', status_code=status.HTTP_201_CREATED, response_model=schemas_authorization.Authorization, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["authorizations"])
def register_auth(auth_data: schemas_authorization.Authorization, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    auth_data = add_create_at_timestamp(auth_data)

    exist = RepositoryAuthorization(db).searchByDescription(auth_data.description)

    if exist:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Already existing authorizarion!")

    authorization_created = RepositoryAuthorization(db).register_authorization(auth_data)

    return authorization_created
