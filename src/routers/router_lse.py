from fastapi import Depends, status, APIRouter, HTTPException

from sqlalchemy.orm import Session
from typing import List

from src.resources.auth_utils import get_user_logged
from src.resources.utils import check_authorization
from src.resources.utils import add_create_at_timestamp

from src.schemas import schemas_lse
from src.infra.sqlalchemy.repository.repo_lse import RepositoryLse
from src.infra.sqlalchemy.config.database import get_db


router = APIRouter()


@router.get('/get/{id}', status_code=status.HTTP_200_OK, response_model=schemas_lse.SimpleLse, tags=["lse"])
def show_lse(id: int, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    lse_located = add_create_at_timestamp(lse_located)

    lse_located = RepositoryLse(db).searchById(id)

    if not lse_located:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lse not exist!")

    return lse_located

@router.get('/get/all', status_code=status.HTTP_200_OK, response_model=List[schemas_lse.SimpleLse], tags=["lse"])
def show_all_lse( _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    all_lse = RepositoryLse(db).show_all_lse()

    if not all_lse:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There are no lse located!")

    return all_lse

@router.post('/register/', status_code=status.HTTP_201_CREATED, response_model=schemas_lse.SimpleLse, tags=["lse"])
def create_lse(lse: schemas_lse.Lse, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    lse = add_create_at_timestamp(lse)

    lse_created = RepositoryLse(db).register(lse)
    return lse_created

@router.put('/update/{id}', status_code=status.HTTP_200_OK, response_model=schemas_lse.SimpleLse, tags=["lse"])
def update_lse(id: int, lse: schemas_lse.Lse, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    lse = add_create_at_timestamp(lse, True)

    # -- register log here --
    # --
    # -- end --

    lse_updated = RepositoryLse(db).edit(id, lse)
    lse_updated.id = id

    return lse_updated

@router.delete('/delete/{id}', status_code=status.HTTP_200_OK, response_model=schemas_lse.SimpleLse, tags=["lse"])
def delete_lse(lse_id: int, _ = Depends(get_user_logged) ,db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    lse = add_create_at_timestamp(lse, True)

    lse = RepositoryLse(db).remove(lse_id)
    return lse
