from fastapi import Depends, status, APIRouter, HTTPException
from fastapi_limiter.depends import RateLimiter

from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import hash_provider as hp
from src.infra.providers import token_provider as tp

from src.schemas import schemas_users, schemas_auth
from src.infra.sqlalchemy.repository.repo_user import RepositoryUser
from src.infra.sqlalchemy.repository.repo_classifier_user import RepositoryClassifierUser

from src.resources.utils import add_create_at_timestamp, check_authorization
from src.resources.auth_utils import get_user_logged


router = APIRouter()


@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=schemas_users.User, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["auth"])
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
