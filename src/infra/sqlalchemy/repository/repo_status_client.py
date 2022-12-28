from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session

from src.schemas import schemas_status_client
from src.infra.sqlalchemy.models import models_status_client


class RepositoryStatusClient():
    
    def __init__(self, db: Session):
        self.db = db

    def searchById(self, id: int):
        query = select(schemas_status_client.StatusClient).where(schemas_status_client.Client.id == id)
        status = self.db.execute(query).first()
        return status

    def register(self, client: schemas_status_client.StatusClient):

        # conversao do schema em model
        db_status = models_status_client.StatusClient(
            description = client.description,
            create_at = client.create_at
        )

        # operações no banco de dados
        self.db.add(db_status)
        self.db.commit()
        self.db.refresh(db_status)

        return db_status

    def edit(self, status_id: int, status: schemas_status_client.StatusClient):
            update_statement = update(models_status_client.StatusClient).where(
                models_status_client.StatusClient.id == status_id
            ).values(
                description = status.description
            )

            self.db.execute(update_statement)
            self.db.commit()
            return status

    def show_all_status(self):
        status = self.db.query(schemas_status_client.StatusClient).all()
        return status

    def remove(self, status_id: int):
        statement = select(schemas_status_client.StatusClient).filter_by(id=status_id)
        status = self.db.execute(statement).first()

        statement = delete(schemas_status_client.StatusClient).where(schemas_status_client.StatusClient.id == status_id)
        self.db.execute(statement)
        self.db.commit()

        return status
