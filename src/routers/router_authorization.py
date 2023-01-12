from fastapi import Depends, status, APIRouter, HTTPException
from fastapi_limiter.depends import RateLimiter
from src.resources.utils import add_create_at_timestamp

from typing import List

from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.resources.auth_utils import get_user_logged
from src.resources.utils import check_authorization

from src.schemas import schemas_authorization, schemas_logs
from src.infra.sqlalchemy.repository.repo_authorization import RepositoryAuthorization
from src.infra.sqlalchemy.repository.repo_logs import RepositoryLogs



router = APIRouter()

@router.get('/get/{id}', status_code=status.HTTP_200_OK, response_model=schemas_authorization.Authorization, tags=["authorizations"])
def show_authorization(id: int, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    authorization_located = add_create_at_timestamp(authorization_located)

    authorization_located = RepositoryAuthorization(db).searchById(id)

    if not authorization_located:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Authorization not exist!")

    return authorization_located

@router.get('/get/all', status_code=status.HTTP_200_OK, response_model=List[schemas_authorization.Authorization], tags=["authorizations"])
def show_all_authorization( _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    all_authorization = RepositoryAuthorization(db).show_all_authorization()

    if not all_authorization:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There are no authorizations located!")

    return all_authorization

@router.post('/register', status_code=status.HTTP_201_CREATED, response_model=schemas_authorization.Authorization, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["authorizations"])
def register_auth(auth_data: schemas_authorization.Authorization, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    auth_data = add_create_at_timestamp(auth_data)

    exist = RepositoryAuthorization(db).searchByDescription(auth_data.description)

    if exist:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Already existing authorizarion!")

    log_data = {"description": f"O usuario {_.User.name} criou uma autorização", "create_at": None, "user_id": _.User.id}
    log_data = add_create_at_timestamp(schemas_logs.Logs(**log_data))
    RepositoryLogs(db).register(log_data)

    authorization_created = RepositoryAuthorization(db).register_authorization(auth_data)

    return authorization_created

@router.put('/update/{id}', status_code=status.HTTP_200_OK, response_model=schemas_authorization.Authorization, tags=["authorizations"])
def update_authorization(id: int, authorization: schemas_authorization.Authorization, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    authorization = add_create_at_timestamp(authorization, True)

    log_data = {"description": f"O usuario {_.User.name} criou uma autorização", "create_at": None, "user_id": _.User.id}
    log_data = add_create_at_timestamp(schemas_logs.Logs(**log_data))
    RepositoryLogs(db).register(log_data)

    authorization_updated = RepositoryAuthorization(db).edit_authorization(id, authorization)
    authorization_updated.id = id

    return authorization_updated

@router.delete('/delete/{id}', status_code=status.HTTP_200_OK, response_model=schemas_authorization.Authorization, tags=["authorizations"])
def delete_authorization(authorization_id: int, _ = Depends(get_user_logged) ,db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    authorization = add_create_at_timestamp(authorization, True)

    log_data = {"description": f"O usuario {_.User.name} criou uma autorização", "create_at": None, "user_id": _.User.id}
    log_data = add_create_at_timestamp(schemas_logs.Logs(**log_data))
    RepositoryLogs(db).register(log_data)

    authorization = RepositoryAuthorization(db).remove_authorization(authorization_id)
    return authorization
