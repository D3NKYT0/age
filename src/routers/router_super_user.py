from fastapi import Depends, status, APIRouter, HTTPException

from sqlalchemy.orm import Session
from typing import List

from src.resources.auth_utils import get_user_logged
from src.resources.utils import check_authorization
from src.resources.utils import add_create_at_timestamp

from src.schemas import schemas_super_user
from src.infra.sqlalchemy.repository.repo_super_user import RepositorySuperUser
from src.infra.sqlalchemy.config.database import get_db


router = APIRouter()


@router.get('/get/{id}', status_code=status.HTTP_200_OK, response_model=schemas_super_user.SimpleSuperUser, tags=["super_users"])
def show_super_user(id: int, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    super_user_located = add_create_at_timestamp(super_user_located)

    super_user_located = RepositorySuperUser(db).searchById(id)

    if not super_user_located:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Super user not exist!")

    return super_user_located

@router.get('/get/all', status_code=status.HTTP_200_OK, response_model=List[schemas_super_user.SimpleSuperUser], tags=["super_users"])
def show_all_super_users( _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    all_super_users = RepositorySuperUser(db).show_all_super_users()

    if not all_super_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There are no super user located!")

    return all_super_users

@router.post('/register/', status_code=status.HTTP_201_CREATED, response_model=schemas_super_user.SimpleSuperUser, tags=["super_users"])
def create_super_user(super_user: schemas_super_user.SuperUser, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    super_user_created = add_create_at_timestamp(super_user)

    super_user_created = RepositorySuperUser(db).register(super_user)
    return super_user_created

@router.put('/update/{id}', status_code=status.HTTP_200_OK, response_model=schemas_super_user.SimpleSuperUser, tags=["super_users"])
def update_super_users(id: int, super_user: schemas_super_user.SuperUser, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    super_user = add_create_at_timestamp(super_user, True)

    # -- register log here --
    # --
    # -- end --

    super_user_updated = RepositorySuperUser(db).edit(id, super_user)
    super_user_updated.id = id

    return super_user_updated

@router.delete('/delete/{id}', status_code=status.HTTP_200_OK, response_model=schemas_super_user.SimpleSuperUser, tags=["super_users"])
def delete_super_users(super_user_id: int, _ = Depends(get_user_logged) ,db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    super_user = add_create_at_timestamp(super_user, True)

    super_user = RepositorySuperUser(db).remove(super_user_id)
    return super_user
