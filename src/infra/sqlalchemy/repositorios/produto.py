from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from src.schemas import schemas_produtos
from src.infra.sqlalchemy.models import models


class RepositorioProduto():
    
    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: schemas_produtos.Produto):

        # conversao do schema em model
        db_produto = models.Produto(
            nome = produto.nome,
            detalhes = produto.detalhes,
            preco = produto.preco,
            disponivel = produto.disponivel,
            usuario_id = produto.usuario_id
        )

        # operações no banco de dados
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)

        return db_produto

    def editar(self, produto_id: int, produto: schemas_produtos.Produto):
            update_statement = update(models.Produto).where(
                models.Produto.id == produto_id
            ).values(
                nome = produto.nome,
                detalhes = produto.detalhes,
                preco = produto.preco,
                disponivel = produto.disponivel
            )

            self.db.execute(update_statement)
            self.db.commit()
            return produto

    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos

    def obter(self, produto_id: int):
        statement = select(models.Produto).filter_by(id=produto_id)
        produto = self.db.execute(statement).first()
        return produto.Produto if produto is not None else {"nome": "Produto nao encontrado", "detalhes": "", "preco": 0.0}

    def remover(self, produto_id: int):
        statement = select(models.Produto).filter_by(id=produto_id)
        produto = self.db.execute(statement).first()

        statement = delete(models.Produto).where(models.Produto.id == produto_id)
        self.db.execute(statement)
        self.db.commit()

        return produto.Produto if produto is not None else {"nome": "Produto nao encontrado", "detalhes": "", "preco": 0.0}
