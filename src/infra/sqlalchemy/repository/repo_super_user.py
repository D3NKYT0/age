from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session

from src.schemas import schemas_super_user
from src.infra.sqlalchemy.models import models_super_user


class RepositorySuperUser():
    
    def __init__(self, db: Session):
        self.db = db

    def searchById(self, id: int):
        query = select(schemas_super_user.SuperUser).where(schemas_super_user.SuperUser.id == id)
        user = self.db.execute(query).first()
        return user

    def register(self, user: schemas_super_user.SuperUser):

        # conversao do schema em model
        db_user = models_super_user.SuperUser(
            name = user.name,
            create_at = user.create_at,
            login = user.login,
            password = user.password,
            email = user.email,
            classified_as = user.classified_as
        )

        # operações no banco de dados
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return db_user

    def edit(self, user_id: int, user: schemas_super_user.SuperUser):
            update_statement = update(models_super_user.SuperUser).where(
                models_super_user.SuperUser.id == user_id
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

    def show_all_users(self):
        users = self.db.query(schemas_super_user.SuperUser).all()
        return users

    def remove(self, user_id: int):
        statement = select(schemas_super_user.SuperUser).filter_by(id=user_id)
        user = self.db.execute(statement).first()

        statement = delete(schemas_super_user.SuperUser).where(schemas_super_user.SuperUser.id == user_id)
        self.db.execute(statement)
        self.db.commit()

        return user
