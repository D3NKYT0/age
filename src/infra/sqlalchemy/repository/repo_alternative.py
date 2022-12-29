from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session

from src.schemas import schemas_alternative
from src.infra.sqlalchemy.models import models_alternative


class RepositoryAlternative():
    
    def __init__(self, db: Session):
        self.db = db

    def searchById(self, id: int):
        query = select(schemas_alternative.Alternative).where(schemas_alternative.Alternative.id == id)
        alternative = self.db.execute(query).first()
        return alternative

    def register_alternative(self, alternative: schemas_alternative.Alternative):

        # conversao do schema em model
        db_alternative = models_alternative.Alternative(
            id = alternative.id,
            description = alternative.description,
            weight = alternative.weight,
            is_available = alternative.is_available,
            create_at = alternative.create_at,
        )

        # operações no banco de dados
        self.db.add(db_alternative)
        self.db.commit()
        self.db.refresh(db_alternative)

        return db_alternative

    def edit_alternative(self, alternative_id: int, alternative: schemas_alternative.Alternative):
            update_statement = update(models_alternative.Alternative).where(
                models_alternative.Alternative.id == alternative_id
            ).values(
                description = alternative.description,
                weight = alternative.weight,
                is_available = alternative.is_available,
            )

            self.db.execute(update_statement)
            self.db.commit()
            return alternative

    def show_all_alternatives(self):
        alternative = self.db.query(schemas_alternative.Alternative).all()
        return alternative

    def remove_alternative(self, alternative_id: int):
        statement = select(schemas_alternative.Alternative).filter_by(id=alternative_id)
        alternative = self.db.execute(statement).first()

        statement = delete(schemas_alternative.Alternative).where(schemas_alternative.Alternative.id == alternative_id)
        self.db.execute(statement)
        self.db.commit()

        return alternative
