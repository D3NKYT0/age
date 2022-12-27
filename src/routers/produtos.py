from fastapi import Depends, status, APIRouter, HTTPException

from sqlalchemy.orm import Session
from typing import List

from src.schemas import schemas_produtos
from src.infra.sqlalchemy.repository.produto import RepositorioProduto
from src.infra.sqlalchemy.repository.usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db


router = APIRouter()


@router.get('/produtos/{id}', tags=["produtos"])
def exibir_produto(id: int, db: Session = Depends(get_db)):
    produto_localizado = RepositorioProduto(db).buscarPorId(id)

    if not produto_localizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")

    return produto_localizado

@router.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=schemas_produtos.ProdutoSimples, tags=["produtos"])
def criar_produto(produto: schemas_produtos.Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@router.put('/produtos/{id}', status_code=status.HTTP_200_OK, response_model=schemas_produtos.ProdutoSimples, tags=["produtos"])
def atualizar_produto(id: int, produto: schemas_produtos.Produto, db: Session = Depends(get_db)):
    produto_atualizado = RepositorioProduto(db).editar(id, produto)
    produto_atualizado.id = id
    return produto_atualizado

@router.get('/produtos', status_code=status.HTTP_200_OK, response_model=list[schemas_produtos.ProdutoSimples], tags=["produtos"])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@router.get('/produtos/{produto_id}', status_code=status.HTTP_200_OK, response_model=schemas_produtos.ProdutoRetorno, tags=["produtos"])
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

@router.delete('/produtos/{produto_id}', status_code=status.HTTP_200_OK, response_model=schemas_produtos.ProdutoSimples, tags=["produtos"])
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = RepositorioProduto(db).remover(produto_id)
    return produto
