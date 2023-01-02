from fastapi import Depends, status, APIRouter, HTTPException

from sqlalchemy.orm import Session
from typing import List

from src.resources.auth_utils import get_user_logged
from src.resources.utils import check_authorization
from src.resources.utils import add_create_at_timestamp

from src.schemas import schemas_alternative
from src.infra.sqlalchemy.repository.repo_alternative import RepositoryAlternative
from src.infra.sqlalchemy.config.database import get_db


router = APIRouter()


@router.get('/alternative/{id}', status_code=status.HTTP_200_OK, response_model=schemas_alternative.SimpleAlternative, tags=["alternative"])
def show_alternative(id: int, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    alternative_located = add_create_at_timestamp(alternative_located)

    alternative_located = RepositoryAlternative(db).searchById(id)

    if not alternative_located:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alternative not exist!")

    return alternative_located

@router.get('/alternative/all', status_code=status.HTTP_200_OK, response_model=List[schemas_alternative.SimpleAlternative], tags=["alternatives"])
def show_all_alternative( _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    all_alternative = RepositoryAlternative(db).show_all_alternatives()

    if not all_alternative:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alternatives not found!")

    return all_alternative

@router.post('/alternative', status_code=status.HTTP_201_CREATED, response_model=schemas_alternative.SimpleAlternative, tags=["alternative"])
def create_alternative(alternative: schemas_alternative.Alternative, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    alternative = add_create_at_timestamp(alternative)

    alternative_created = RepositoryAlternative(db).register(alternative)
    return alternative_created

@router.put('/alternative/{id}', status_code=status.HTTP_200_OK, response_model=schemas_alternative.SimpleAlternative, tags=["alternative"])
def update_question(id: int, alternative: schemas_alternative.Alternative, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    alternative = add_create_at_timestamp(alternative, True)

    # -- register log here --
    # --
    # -- end --

    alternative_updated = RepositoryAlternative(db).edit(id, alternative)
    alternative_updated.id = id

    return alternative_updated

@router.delete('/alternative/{id}', status_code=status.HTTP_200_OK, response_model=schemas_alternative.SimpleAlternative, tags=["alternative"])
def delete_alternative(alternative_id: int, _ = Depends(get_user_logged) ,db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    alternative = add_create_at_timestamp(alternative, True)

    alternative = RepositoryAlternative(db).remove(alternative_id)
    return alternative
