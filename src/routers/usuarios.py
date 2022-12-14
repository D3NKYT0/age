from fastapi import Depends, status, APIRouter, HTTPException
from fastapi_limiter.depends import RateLimiter

from sqlalchemy.orm import Session
from typing import List

from src.schemas import schemas_usuarios
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.routers.auth_utils import get_user_logged
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import hash_provider as hp
from src.infra.providers import token_provider as tp


router = APIRouter()


@router.post('/auth/signup', status_code=status.HTTP_201_CREATED, response_model=schemas_usuarios.UsuarioNovo, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["auth"])
def criar_usuario(usuario: schemas_usuarios.UsuarioNovo, db: Session = Depends(get_db)):
    user = RepositorioUsuario(db).get_by_phone(usuario.telefone)

    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario ja existe")

    usuario.senha = hp.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado

@router.post('/token', response_model=schemas_usuarios.LoginSucesso, status_code=status.HTTP_200_OK, tags=["auth"])
def login(login_data: schemas_usuarios.LoginData, db: Session = Depends(get_db)):
    senha = login_data.senha
    telefone = login_data.telefone

    user = RepositorioUsuario(db).get_by_phone(telefone)

    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='o telefone ou senha estao incorretos')

    senha_valida = hp.verificar_hash(senha, user.senha)

    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='o telefone ou senha estao incorretos')

    # gerar JWT
    token = tp.generate_access_token({'sub': user.telefone})
    return schemas_usuarios.LoginSucesso(usuario=user, access_token=token)

@router.get('/me', status_code=status.HTTP_200_OK, response_model=schemas_usuarios.UsuarioSimples, tags=["auth"])
def me(usuario: schemas_usuarios.Usuario = Depends(get_user_logged)):
    return usuario

@router.get('/usuarios', status_code=status.HTTP_200_OK, response_model=list[schemas_usuarios.Usuario], tags=["usuarios"])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios

@router.get('/usuarios/{usuario_id}', status_code=status.HTTP_200_OK, response_model=schemas_usuarios.UsuarioSimples, tags=["usuarios"])
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = RepositorioUsuario(db).obter(usuario_id)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuário nao encontrado')

    return usuario

@router.delete('/usuarios/{usuario_id}', status_code=status.HTTP_200_OK, response_model=schemas_usuarios.UsuarioSimples, tags=["usuarios"])
def remover_usuario(usuario_id: int, db: Session = Depends(get_db)):
    user = RepositorioUsuario(db).remover(usuario_id)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuário nao encontrado')

    return user
