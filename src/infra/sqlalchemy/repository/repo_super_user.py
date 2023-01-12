from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session

from src.schemas import schemas_super_user
from src.infra.sqlalchemy.models import models_super_user


class RepositorySuperUser():
    
    def __init__(self, db: Session):
        self.db = db

    def searchById(self, id: int):
        query = select(models_super_user.SuperUser).where(models_super_user.SuperUser.id == id)
        super_user = self.db.execute(query).first()
        return super_user

    def searchByLogin(self, login: str):
        query = select(models_super_user.SuperUser).where(models_super_user.SuperUser.login == login)
        super_user = self.db.execute(query).first()
        return super_user

    def register(self, super_user: schemas_super_user.SuperUser):

        # conversao do schema em model
        db_super_user = models_super_user.SuperUser(
            name = super_user.name,
            create_at = super_user.create_at,
            login = super_user.login,
            password = super_user.password,
            email = super_user.email,
            classified_as = super_user.classified_as
        )

        # operações no banco de dados
        self.db.add(db_super_user)
        self.db.commit()
        self.db.refresh(db_super_user)

        return db_super_user

    def edit(self, super_user_id: int, super_user: schemas_super_user.SuperUser):
            update_statement = update(models_super_user.SuperUser).where(
                models_super_user.SuperUser.id == super_user_id
            ).values(
                name = super_user.name,
                login = super_user.login,
                password = super_user.password,
                email = super_user.email,
                classified_as = super_user.classified_as
            )

            self.db.execute(update_statement)
            self.db.commit()
            return super_user

    def show_all_users(self):
        super_user = self.db.query(models_super_user.SuperUser).all()
        return super_user

    def remove(self, super_user_id: int):
        statement = select(models_super_user.SuperUser).filter_by(id=super_user_id)
        super_user = self.db.execute(statement).first()

        statement = delete(models_super_user.SuperUser).where(models_super_user.SuperUser.id == super_user_id)
        self.db.execute(statement)
        self.db.commit()

        return super_user
