from jose import JWTError
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException

from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider


oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')
token_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token Invalido')


def get_user_logged(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    try:
        phone = token_provider.verify_access_token(token)
    except JWTError:
        raise token_exception

    if not phone:
        raise token_exception
    user = RepositorioUsuario(db).get_by_phone(phone)

    if not user:
        raise token_exception

    return user
    