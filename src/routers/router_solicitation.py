from fastapi import Depends, status, APIRouter, HTTPException
from fastapi_limiter.depends import RateLimiter

from sqlalchemy.orm import Session
from typing import List

from src.resources.auth_utils import get_user_logged
from src.resources.utils import check_authorization
from src.resources.utils import add_create_at_timestamp

from src.schemas import schemas_solicitation
from src.infra.sqlalchemy.repository.repo_solicitation import RepositorySolicitation
from src.infra.sqlalchemy.config.database import get_db


router = APIRouter()


@router.get('/get/{id}', status_code=status.HTTP_200_OK, response_model=schemas_solicitation.Solicitation, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["solicitations"])
def show_solicitation(id: int, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    solicitation_located = add_create_at_timestamp(solicitation_located)

    solicitation_located = RepositorySolicitation(db).searchById(id)

    if not solicitation_located:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Solicitation not exist!")

    return solicitation_located

@router.get('/get/all/', status_code=status.HTTP_200_OK, response_model=List[schemas_solicitation.Solicitation], dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["solicitations"])
def show_all_solicitations( _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    all_solicitations = RepositorySolicitation(db).show_all_solicitations()

    if not all_solicitations:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Solicitation not found!")

    return all_solicitations

@router.post('/register/', status_code=status.HTTP_201_CREATED, response_model=schemas_solicitation.Solicitation, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["solicitations"])
def create_solicitation(solicitation: schemas_solicitation.Solicitation, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    solicitation_created = add_create_at_timestamp(solicitation)

    solicitation_created = RepositorySolicitation(db).register(solicitation)
    return solicitation_created

@router.put('/update/{id}', status_code=status.HTTP_200_OK, response_model=schemas_solicitation.Solicitation, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["solicitations"])
def update_solicitation(id: int, solicitation: schemas_solicitation.Solicitation, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    solicitation = add_create_at_timestamp(solicitation, True)

    # -- register log here --
    # --
    # -- end --

    solicitation_updated = RepositorySolicitation(db).edit(id, solicitation)
    solicitation_updated.id = id

    return solicitation_updated

@router.delete('/delete/{id}', status_code=status.HTTP_200_OK, response_model=schemas_solicitation.Solicitation, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["solicitations"])
def delete_solicitation(solicitation_id: int, _ = Depends(get_user_logged) ,db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    solicitation = add_create_at_timestamp(solicitation, True)

    solicitation = RepositorySolicitation(db).remove(solicitation_id)
    return solicitation