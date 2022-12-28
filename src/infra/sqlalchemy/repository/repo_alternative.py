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

    def register(self, alternative: schemas_alternative.Alternative):

        # conversao do schema em model
        db_user = models_alternative.Alternative(
            id = alternative.id,
            description = alternative.description,
            weight = alternative.weight,
            is_available = alternative.is_available,
            create_at = alternative.create_at,
        )

        # operações no banco de dados
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return db_user

    def edit(self, user_id: int, user: schemas_users.User):
            update_statement = update(models_user.User).where(
                models_user.User.id == user_id
            ).values(
                name = user.name,
                login = user.login,
                password = user.password,
                email = user.email,
                classified_as = user.classified_as
            )

            self.db.execute(update_statement)
            self.db.commit()
            return user

    def show_all_alternative(self):
        users = self.db.query(schemas_users.User).all()
        return users

    def remove_alternative(self, user_id: int):
        statement = select(schemas_users.User).filter_by(id=user_id)
        user = self.db.execute(statement).first()

        statement = delete(schemas_users.User).where(schemas_users.User.id == user_id)
        self.db.execute(statement)
        self.db.commit()

        return user
