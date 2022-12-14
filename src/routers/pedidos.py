from fastapi import Depends, status, APIRouter, HTTPException

from sqlalchemy.orm import Session
from typing import List

from src.schemas import schemas_pedidos
from src.infra.sqlalchemy.repositorios.pedido import RepositorioPedido
from src.infra.sqlalchemy.config.database import get_db


router = APIRouter()

@router.post('/pedidos', status_code=status.HTTP_201_CREATED, response_model=schemas_pedidos.Pedido, tags=["pedidos"])
def fazer_pedido(pedido: schemas_pedidos.Pedido, db: Session = Depends(get_db)):
    pedido_criado = RepositorioPedido(db).criar(pedido)
    return pedido_criado

@router.get('/pedidos/{id}', status_code=status.HTTP_200_OK, response_model=schemas_pedidos.Pedido, tags=["pedidos"])
def exibir_pedido(id: int, db: Session = Depends(get_db)):
    pedido = RepositorioPedido(db).obter(id)
    return pedido

@router.get('/pedidos/', status_code=status.HTTP_200_OK, response_model=List[schemas_pedidos.Pedido], tags=["pedidos"])
def listar_pedidos(db: Session = Depends(get_db)):
    pedidos = RepositorioPedido(db).listar()
    return pedidos
