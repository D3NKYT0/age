from fastapi import Depends, status, APIRouter, HTTPException
from fastapi_limiter.depends import RateLimiter

from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import hash_provider as hp
from src.infra.providers import token_provider as tp

from src.schemas import schemas_auth
from src.infra.sqlalchemy.repository.repo_user import RepositoryUser
from src.infra.sqlalchemy.repository.repo_super_user import RepositorySuperUser


router = APIRouter()


@router.post('/token', response_model=schemas_auth.LoginSuccess, status_code=status.HTTP_200_OK, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["auth"])
def login(login_data: schemas_auth.LoginData, db: Session = Depends(get_db)):

    password, login = login_data.password, login_data.login

    user = RepositoryUser(db).searchByLogin(login)

    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Login or password is incorrect')

    user = user.User  # recebendo a classe principal

    invalid_password = hp.verificar_hash(password, user.password)

    if not invalid_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Login or password is incorrect')

    # gerar JWT
    token = tp.generate_access_token({'sub': user.login})
    return schemas_auth.LoginSuccess(user=user, access_token=token)

@router.post('/su', response_model=schemas_auth.LoginSuccess, status_code=status.HTTP_200_OK, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["auth"])
def login(login_data: schemas_auth.LoginData, db: Session = Depends(get_db)):

    password, login = login_data.password, login_data.login

    super_user = RepositorySuperUser(db).searchByLogin(login)

    if super_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Login or password is incorrect')

    super_user = super_user.SuperUser  # recebendo a classe principal

    invalid_password = hp.verificar_hash(password, super_user.password)

    if not invalid_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Login or password is incorrect')

    # gerar JWT
    token = tp.generate_access_token({'sub': super_user.login})
    return schemas_auth.LoginSuccess(user=super_user, access_token=token)
