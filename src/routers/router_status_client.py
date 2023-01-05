from fastapi import Depends, status, APIRouter, HTTPException

from sqlalchemy.orm import Session
from typing import List

from src.resources.auth_utils import get_user_logged
from src.resources.utils import check_authorization
from src.resources.utils import add_create_at_timestamp

from src.schemas import schemas_status_client
from src.infra.sqlalchemy.repository.repo_status_client import RepositoryStatusClient
from src.infra.sqlalchemy.config.database import get_db


router = APIRouter()


@router.get('/get/{id}', status_code=status.HTTP_200_OK, response_model=schemas_status_client.StatusClient, tags=["status_clients"])
def show_status_client(id: int, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    status_client_located = add_create_at_timestamp(status_client_located)

    status_client_located = RepositoryStatusClient(db).searchById(id)

    if not status_client_located:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Status client not exist!")

    return status_client_located

@router.get('/get/all', status_code=status.HTTP_200_OK, response_model=List[schemas_status_client.StatusClient], tags=["status_clients"])
def show_all_status_client( _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    all_status_client = RepositoryStatusClient(db).show_all_status_client()

    if not  all_status_client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There are no status client located!")

    return  all_status_client

@router.post('/register/', status_code=status.HTTP_201_CREATED, response_model=schemas_status_client.StatusClient, tags=["status_clients"])
def create_status_client(status_client: schemas_status_client.StatusClient, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    status_client_created = add_create_at_timestamp(status_client)

    status_client_created = RepositoryStatusClient(db).register(status_client)
    return status_client_created 

@router.put('/update/{id}', status_code=status.HTTP_200_OK, response_model=schemas_status_client.StatusClient, tags=["status_clients"])
def update_status_client(id: int, status_client: schemas_status_client.StatusClient, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    status_client = add_create_at_timestamp(status_client, True)

    # -- register log here --
    # --
    # -- end --

    status_client_updated = RepositoryStatusClient(db).edit(id, status_client)
    status_client_updated.id = id

    return status_client_updated

@router.delete('/delete/{id}', status_code=status.HTTP_200_OK, response_model=schemas_status_client.StatusClient, tags=["status_clients"])
def delete_status_client(status_client_id: int, _ = Depends(get_user_logged) ,db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    status_client = add_create_at_timestamp(status_client, True)

    status_client = RepositoryStatusClient(db).remove(status_client_id)
    return status_client

