from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from src.schemas import schemas_usuarios
from src.infra.sqlalchemy.models import models


class RepositorioUsuario():
    
    def __init__(self, db: Session):
        self.db = db

    def criar(self, usuario: schemas_usuarios.Usuario):

        # conversao do schema em model
        db_usuario = models.Usuario(
            nome = usuario.nome,
            senha = usuario.senha,
            telefone = usuario.telefone
        )

        # operações no banco de dados
        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)

        return db_usuario

    def listar(self):
        usuarios = self.db.query(models.Usuario).all()
        return usuarios

    def obter(self, usuario_id: int):
        statement = select(models.Usuario).filter_by(id=usuario_id)
        usuario = self.db.execute(statement).first()
        return usuario.Usuario if usuario is not None else {"nome": "Usuario nao encontrado", "telefone": "", "senha": ""}

    def remover(self, usuario_id: int):
        statement = select(models.Usuario).filter_by(id=usuario_id)
        usuario = self.db.execute(statement).first()

        statement = delete(models.Usuario).where(models.Usuario.id == usuario_id)
        self.db.execute(statement)
        self.db.commit()
        return usuario.Usuario if usuario is not None else {"nome": "Usuario nao encontrado", "telefone": "", "senha": ""}
