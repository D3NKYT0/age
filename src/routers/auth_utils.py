import json

from jose import JWTError
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException

from src.infra.sqlalchemy.repository.repo_user import RepositoryUser
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider


with open("auth/data/auth.json", encoding="utf-8") as auth_data:
    _auth_data = json.load(auth_data)


oauth2_schema = OAuth2PasswordBearer(tokenUrl=_auth_data['tokenUrl'])
token_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token Invalido')


def get_user_logged(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    try:
        phone = token_provider.verify_access_token(token)
    except JWTError:
        raise token_exception

    if not phone:
        raise token_exception
    user = RepositoryUser(db).searchById(phone)

    if not user:
        raise token_exception

    return user
    