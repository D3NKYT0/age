from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session

from src.schemas import schemas_pedidos
from src.infra.sqlalchemy.models import models


class RepositorioPedido():
    
    def __init__(self, db: Session):
        self.db = db

    def criar(self, pedido: schemas_pedidos.Pedido):
        pass

    def listar(self):
        pass

    def obter(self, id: int):
        pass
