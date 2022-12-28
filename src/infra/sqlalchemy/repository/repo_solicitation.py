from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session

from src.schemas import schemas_solicitation
from src.infra.sqlalchemy.models import models_solicitation


class RepositorySolicitation():
    
    def __init__(self, db: Session):
        self.db = db

    def searchById(self, id: int):
        query = select(schemas_solicitation.Solicitation).where(schemas_solicitation.Solicitation.id == id)
        solicitation = self.db.execute(query).first()
        return solicitation

    def register(self, solicitation: schemas_solicitation.Solicitation):

        # conversao do schema em model
        db_solicitation = models_solicitation.Solicitation(
            description = solicitation.description,
            create_at = solicitation.create_at
        )

        # operações no banco de dados
        self.db.add(db_solicitation)
        self.db.commit()
        self.db.refresh(db_solicitation)

        return db_solicitation

    def edit(self, solicitation_id: int, solicitation: schemas_solicitation.Solicitation):
            update_statement = update(models_solicitation.Solicitation).where(
                models_solicitation.Solicitation.id == solicitation_id
            ).values(
                description = solicitation.description
            )

            self.db.execute(update_statement)
            self.db.commit()
            return solicitation

    def show_all_solicitations(self):
        solicitations = self.db.query(schemas_solicitation.Solicitation).all()
        return solicitations

    def remove(self, solicitation_id: int):
        statement = select(schemas_solicitation.Solicitation).filter_by(id=solicitation_id)
        solicitation = self.db.execute(statement).first()

        statement = delete(schemas_solicitation.Solicitation).where(schemas_solicitation.Solicitation.id == solicitation_id)
        self.db.execute(statement)
        self.db.commit()

        return solicitation
