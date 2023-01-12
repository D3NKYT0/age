from fastapi import Depends, status, APIRouter, HTTPException
from fastapi_limiter.depends import RateLimiter

from sqlalchemy.orm import Session
from typing import List
from src.infra.providers import hash_provider as hp

from src.resources.auth_utils import get_user_logged
from src.resources.utils import check_authorization
from src.resources.utils import add_create_at_timestamp

from src.schemas import schemas_users
from src.infra.sqlalchemy.repository.repo_user import RepositoryUser
from src.infra.sqlalchemy.repository.repo_classifier_user import RepositoryClassifierUser
from src.infra.sqlalchemy.config.database import get_db


router = APIRouter()


@router.get('/get/{id}', status_code=status.HTTP_200_OK, response_model=schemas_users.SimpleUser, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["users"])
def show_user(id: int, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    user_located = add_create_at_timestamp(user_located)

    user_located = RepositoryUser(db).searchById(id)

    if not user_located:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not exist!")

    return user_located

@router.get('/get/all/', status_code=status.HTTP_200_OK, response_model=List[schemas_users.SimpleUser], dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["users"])
def show_all_users( _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    all_users = RepositoryUser(db).show_all_users()

    if not all_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There are no users located!")

    return all_users

@router.post('/register/', status_code=status.HTTP_201_CREATED, response_model=schemas_users.User, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["auth"])
def create_user(user: schemas_users.User, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    user = add_create_at_timestamp(user)

    data_user = RepositoryUser(db).searchByLogin(user.login)

    if data_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")

    exist_auth = RepositoryClassifierUser(db).searchById(user.classified_as)

    if not exist_auth:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Classifier not found!")

    user.password = hp.gerar_hash(user.password)
    created_user = RepositoryUser(db).register(user)
    return created_user

@router.put('/update/{id}', status_code=status.HTTP_200_OK, response_model=schemas_users.SimpleUser, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["users"])
def update_users(id: int, user: schemas_users.User, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    user = add_create_at_timestamp(user, True)

    # -- register log here --
    # --
    # -- end --

    user_updated = RepositoryUser(db).edit(id, user)
    user_updated.id = id

    return user_updated

@router.delete('/delete/{id}', status_code=status.HTTP_200_OK, response_model=schemas_users.SimpleUser, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["users"])
def delete_users(user_id: int, _ = Depends(get_user_logged) ,db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    user = add_create_at_timestamp(user, True)

    user = RepositoryUser(db).remove(user_id)
    return user
