import os

from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from src.schemas import schemas_produtos, schemas_usuarios
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db, criar_db


# version
__version__ = "0.0.5.1"


# criação do banco de dados (so acontece uma vez)
if not os.path.exists("app_age.db"):
    criar_db()

# criação do aplicativo principal da API (age)
app = FastAPI()


# origins
origins = [
    'http://localhost:3000'  # teste local
]


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# ============== definições de rotas =================

@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=schemas_produtos.ProdutoSimples)
def criar_produto(produto: schemas_produtos.Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@app.put('/produtos/{id}', status_code=status.HTTP_200_OK, response_model=schemas_produtos.ProdutoSimples)
def atualizar_produto(id: int, produto: schemas_produtos.Produto, db: Session = Depends(get_db)):
    produto_atualizado = RepositorioProduto(db).editar(id, produto)
    produto_atualizado.id = id
    return produto_atualizado

@app.get('/produtos', status_code=status.HTTP_200_OK, response_model=list[schemas_produtos.ProdutoSimples])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@app.get('/produtos/{produto_id}', status_code=status.HTTP_200_OK, response_model=schemas_produtos.ProdutoRetorno)
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = RepositorioProduto(db).obter(produto_id)
    try:
        retorno = produto.__dict__
    except AttributeError:
        produto['usuario_id'] = -1
        retorno = produto
    usuario_id = retorno['usuario_id']
    user = RepositorioUsuario(db).obter(usuario_id)
    if user is not None:
        try:
            retorno['usuario'] = user.__dict__
        except AttributeError:
            retorno['usuario'] = user
    else:
        retorno['usuario'] = {"nome": "Usuario nao encontrado", "telefone": "", "senha": ""}
    return retorno

@app.delete('/produtos/{produto_id}', status_code=status.HTTP_200_OK, response_model=schemas_produtos.ProdutoSimples)
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = RepositorioProduto(db).remover(produto_id)
    return produto


# ========================== USUARIOS ==========================

@app.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=schemas_usuarios.Usuario)
def criar_usuario(usuario: schemas_usuarios.Usuario, db: Session = Depends(get_db)):
    produto_criado = RepositorioUsuario(db).criar(usuario)
    return produto_criado

@app.get('/usuarios', status_code=status.HTTP_200_OK, response_model=list[schemas_usuarios.Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios

@app.get('/usuarios/{usuario_id}', status_code=status.HTTP_200_OK, response_model=schemas_usuarios.UsuarioSimples)
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = RepositorioUsuario(db).obter(usuario_id)
    return usuario

@app.delete('/usuarios/{usuario_id}', status_code=status.HTTP_200_OK, response_model=schemas_usuarios.UsuarioSimples)
def remover_usuario(usuario_id: int, db: Session = Depends(get_db)):
    user = RepositorioUsuario(db).remover(usuario_id)
    return user
