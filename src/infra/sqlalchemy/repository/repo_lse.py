from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session

from src.schemas import schemas_lse
from src.infra.sqlalchemy.models import models_lse


class RepositoryLse():
    
    def __init__(self, db: Session):
        self.db = db

    def searchById(self, id: int):
        query = select(schemas_lse.Lse).where(schemas_lse.Lse.id == id)
        lse = self.db.execute(query).first()
        return lse

    def register(self, lse: schemas_lse.Lse):

        # conversao do schema em model
        db_lse = models_lse.Lse(
            quiz = lse.quiz,
            create_at = lse.create_at,
            is_available = lse.is_available
        )

        # operações no banco de dados
        self.db.add(db_lse)
        self.db.commit()
        self.db.refresh(db_lse)

        return db_lse

    def edit(self, lse_id: int, lse: schemas_lse.Lse):
            update_statement = update(models_lse.Lse).where(
                models_lse.Lse.id == lse_id
            ).values(
                quiz = lse.quiz,
                create_at = lse.create_at,
                is_available = lse.is_available
            )

            self.db.execute(update_statement)
            self.db.commit()
            return lse

    def show_all_lse(self):
        lse = self.db.query(schemas_lse.Lse).all()
        return lse

    def remove(self, lse_id: int):
        statement = select(schemas_lse.Lse).filter_by(id=lse_id)
        lse = self.db.execute(statement).first()

        statement = delete(schemas_lse.Lse).where(schemas_lse.Lse.id == lse_id)
        self.db.execute(statement)
        self.db.commit()

        return lse
