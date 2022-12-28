from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session

from src.schemas import schemas_super_user_logs
from src.infra.sqlalchemy.models import models_super_user_logs


class RepositoryUser():
    
    def __init__(self, db: Session):
        self.db = db

    def searchById(self, id: int):
        query = select(schemas_super_user_logs.SuperUserLogs).where(schemas_super_user_logs.SuperUserLogs.id == id)
        log = self.db.execute(query).first()
        return log

    def register(self, log: schemas_super_user_logs.SuperUserLogs):

        # conversao do schema em model
        db_user = models_super_user_logs.SuperLog(
            description = log.description,
            create_at = log.create_at,
        )

        # operações no banco de dados
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return db_user

    def edit(self, log_id: int, log: schemas_super_user_logs.SuperUserLogs):
            update_statement = update(models_super_user_logs.SuperLog).where(
                models_super_user_logs.SuperLog.id == log_id
            ).values(
                description = log.description,
            )

            self.db.execute(update_statement)
            self.db.commit()
            return log

    def show_all_users(self):
        users = self.db.query(schemas_users.User).all()
        return users

    def remove(self, user_id: int):
        statement = select(schemas_users.User).filter_by(id=user_id)
        user = self.db.execute(statement).first()

        statement = delete(schemas_users.User).where(schemas_users.User.id == user_id)
        self.db.execute(statement)
        self.db.commit()

        return user
