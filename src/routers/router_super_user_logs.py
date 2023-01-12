from fastapi import Depends, status, APIRouter, HTTPException

from sqlalchemy.orm import Session
from typing import List

from src.resources.auth_utils import get_user_logged
from src.resources.utils import check_authorization
from src.resources.utils import add_create_at_timestamp

from src.schemas import schemas_super_user_logs
from src.infra.sqlalchemy.repository.repo_super_user_logs import RepositorySuperUserLogs
from src.infra.sqlalchemy.config.database import get_db


router = APIRouter()


@router.get('/get/{id}', status_code=status.HTTP_200_OK, response_model=schemas_super_user_logs.SuperUserLogs, tags=["super_users_logs"])
def show_super_user_logs(id: int, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    logs_super_user_located = add_create_at_timestamp(logs_super_user_located)

    logs_super_user_located = RepositorySuperUserLogs(db).searchById(id)

    if not logs_super_user_located:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Logs super user not exist!")

    return logs_super_user_located

@router.get('/get/all/', status_code=status.HTTP_200_OK, response_model=List[schemas_super_user_logs.SuperUserLogs], tags=["super_users_logs"])
def show_super_user_logs( _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    all_logs_super_users = RepositorySuperUserLogs(db).show_all_super_users()

    if not all_logs_super_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There are no logs super user located!")

    return all_logs_super_users

@router.post('/register/', status_code=status.HTTP_201_CREATED, response_model=schemas_super_user_logs.SuperUserLogs, tags=["super_users_logs"])
def create_Logs_super_user(logs_super_user: schemas_super_user_logs.SuperUserLogs, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    logs_super_user_created = add_create_at_timestamp(logs_super_user)

    logs_super_user_created = RepositorySuperUserLogs(db).register(logs_super_user)
    return logs_super_user_created

@router.put('/update/{id}', status_code=status.HTTP_200_OK, response_model=schemas_super_user_logs.SuperUserLogs, tags=["super_users_logs"])
def update_super_users_logs(id: int, super_user_logs: schemas_super_user_logs.SuperUserLogs, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    logs_super_user = add_create_at_timestamp(super_user_logs, True)

    # -- register log here --
    # --
    # -- end --

    logs_super_user_updated = RepositorySuperUserLogs(db).edit(id, super_user_logs)
    logs_super_user_updated.id = id

    return logs_super_user_updated

@router.delete('/delete/{id}', status_code=status.HTTP_200_OK, response_model=schemas_super_user_logs.SuperUserLogs, tags=["super_users_logs"])
def delete_logs_super_users(logs_super_user_id: int, _ = Depends(get_user_logged) ,db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    logs_super_user = add_create_at_timestamp(logs_super_user, True)

    logs_super_user = RepositorySuperUserLogs(db).remove(logs_super_user_id)
    return logs_super_user
