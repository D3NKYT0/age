from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session

from src.schemas import schemas_authorization
from src.infra.sqlalchemy.models import models_authorization


class RepositoryAuthorization():
    
    def __init__(self, db: Session):
        self.db = db

    def searchById(self, id: int):
        query = select(schemas_authorization.Authorization).where(schemas_authorization.Authorization.id == id)
        authorization = self.db.execute(query).first()
        return authorization

    def register_authorization(self, authorization: schemas_authorization.Authorization):

        # conversao do schema em model
        db_user = models_authorization.Authorization(
            description = authorization.description,
        )

        # operações no banco de dados
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return db_user

    def edit_authorization(self, authorization_id: int, authorization: schemas_authorization.Authorization):
            update_statement = update(models_authorization.Authorization).where(
                models_authorization.Authorization.id == authorization_id
            ).values(
                description = authorization.description,
            )

            self.db.execute(update_statement)
            self.db.commit()
            return authorization

    def show_all_authorization(self):
        authorization = self.db.query(schemas_authorization.Authorization).all()
        return authorization

    def remove_authorization(self, authorization_id: int):
        statement = select(schemas_authorization.Authorization).filter_by(id=authorization_id)
        authorization = self.db.execute(statement).first()

        statement = delete(schemas_authorization.Authorization).where(schemas_authorization.Authorization.id == authorization_id)
        self.db.execute(statement)
        self.db.commit()

        return authorization
