from fastapi import Depends, status, APIRouter, HTTPException
from fastapi_limiter.depends import RateLimiter

from sqlalchemy.orm import Session
from typing import List

from src.resources.auth_utils import get_user_logged
from src.resources.utils import check_authorization
from src.resources.utils import add_create_at_timestamp

from src.schemas import schemas_response
from src.infra.sqlalchemy.repository.repo_response import RepositoryResponse
from src.infra.sqlalchemy.config.database import get_db


router = APIRouter()


@router.get('/get/{id}', status_code=status.HTTP_200_OK, response_model=schemas_response.SimpleResponse, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["responses"])
def show_response(id: int, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    response_located = add_create_at_timestamp(response_located)

    response_located = RepositoryResponse(db).searchById(id)

    if not response_located:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Response not exist!")

    return response_located

@router.get('/get/all/', status_code=status.HTTP_200_OK, response_model=List[schemas_response.SimpleResponse], dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["responses"])
def show_all_responses( _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    all_responses = RepositoryResponse(db).show_all_responses()

    if not all_responses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Response not found!")

    return all_responses

@router.post('/register/', status_code=status.HTTP_201_CREATED, response_model=schemas_response.SimpleResponse, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["responses"])
def create_response(response: schemas_response.SimpleResponse, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    response_created = add_create_at_timestamp(response)

    response_created = RepositoryResponse(db).register(response)
    return response_created

@router.put('/update/{id}', status_code=status.HTTP_200_OK, response_model=schemas_response.SimpleResponse, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["responses"])
def update_response(id: int, response: schemas_response.Response, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    response = add_create_at_timestamp(response, True)

    # -- register log here --
    # --
    # -- end --

    response_updated = RepositoryResponse(db).edit(id, response)
    response_updated.id = id

    return response_updated

@router.delete('/delete/{id}', status_code=status.HTTP_200_OK, response_model=schemas_response.SimpleResponse, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["responses"])
def delete_response(response_id: int, _ = Depends(get_user_logged) ,db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    response = add_create_at_timestamp(response, True)

    response = RepositoryResponse(db).remove(response_id)
    return response