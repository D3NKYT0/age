from fastapi import Depends, status, APIRouter, HTTPException
from fastapi_limiter.depends import RateLimiter

from sqlalchemy.orm import Session
from typing import List

from src.resources.auth_utils import get_user_logged
from src.resources.utils import check_authorization
from src.resources.utils import add_create_at_timestamp

from src.schemas import schemas_client
from src.infra.sqlalchemy.repository.repo_client import RepositoryClient
from src.infra.sqlalchemy.config.database import get_db


router = APIRouter()


@router.get('/get/{id}', status_code=status.HTTP_200_OK, response_model=schemas_client.SimpleClient, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["clients"])
def show_client(id: int, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    client = add_create_at_timestamp(client)

    client_located = RepositoryClient(db).searchById(id)

    if not client_located:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not exist!")

    return client_located

@router.get('/get/all/', status_code=status.HTTP_200_OK, response_model=List[schemas_client.SimpleClient], dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["clients"])
def show_all_clients( _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    all_client = RepositoryClient(db).show_all_clients()

    if not all_client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There are no registered clients!")

    return all_client

@router.post('/register/', status_code=status.HTTP_201_CREATED, response_model=schemas_client.SimpleClient, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["clients"])
def create_client(client: schemas_client.Client, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    client = add_create_at_timestamp(client)

    client_created = RepositoryClient(db).register_client(client)
    return client_created

@router.put('/update/{id}', status_code=status.HTTP_200_OK, response_model=schemas_client.SimpleClient, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["clients"])
def update_client(id: int, client: schemas_client.Client, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    client = add_create_at_timestamp(client, True)

    # -- register log here --
    # --
    # -- end --

    client_updated = RepositoryClient(db).edit_client(id, client)
    client_updated.id = id

    return client_updated

@router.delete('/delete/{id}', status_code=status.HTTP_200_OK, response_model=schemas_client.SimpleClient, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["clients"])
def delete_client(client_id: int, _ = Depends(get_user_logged) ,db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    client = add_create_at_timestamp(client, True)

    client = RepositoryClient(db).remove(client_id)
    return client
