from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session

from src.schemas import schemas_response
from src.infra.sqlalchemy.models import models_response


class RepositoryResponse():
    
    def __init__(self, db: Session):
        self.db = db

    def searchById(self, id: int):
        query = select(models_response.Response).where(models_response.Response.id == id)
        response = self.db.execute(query).first()
        return response

    def register(self, response: schemas_response.Response):

        # conversao do schema em model
        db_response = models_response.Response(
            description = response.description,
            create_at = response.create_at,
            question_id = response.question_id,
            client_id = response.client_id
        )

        # operações no banco de dados
        self.db.add(db_response)
        self.db.commit()
        self.db.refresh(db_response)

        return db_response

    def edit(self, response_id: int, response: schemas_response.Response):
            update_statement = update(models_response.Response).where(
                models_response.Response.id == response_id
            ).values(
            description = response.description,
            question_id = response.question_id,
            client_id = response.client_id
            )

            self.db.execute(update_statement)
            self.db.commit()
            return response

    def show_all_responses(self):
        responses = self.db.query(models_response.Response).all()
        return responses

    def remove(self, response_id: int):
        statement = select(models_response.Response).filter_by(id=response_id)
        response = self.db.execute(statement).first()

        statement = delete(models_response.Response).where(models_response.Response.id == response_id)
        self.db.execute(statement)
        self.db.commit()

        return response
