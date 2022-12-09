from fastapi import APIRouter
from fastapi import Depends, status

from sqlalchemy.orm import Session
from typing import List

from src.schemas import schemas_usuarios
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db


router = APIRouter()


@router.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=schemas_usuarios.Usuario)
def criar_usuario(usuario: schemas_usuarios.Usuario, db: Session = Depends(get_db)):
    produto_criado = RepositorioUsuario(db).criar(usuario)
    return produto_criado

@router.get('/usuarios', status_code=status.HTTP_200_OK, response_model=list[schemas_usuarios.Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios

@router.get('/usuarios/{usuario_id}', status_code=status.HTTP_200_OK, response_model=schemas_usuarios.UsuarioSimples)
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = RepositorioUsuario(db).obter(usuario_id)
    return usuario

@router.delete('/usuarios/{usuario_id}', status_code=status.HTTP_200_OK, response_model=schemas_usuarios.UsuarioSimples)
def remover_usuario(usuario_id: int, db: Session = Depends(get_db)):
    user = RepositorioUsuario(db).remover(usuario_id)
    return user
