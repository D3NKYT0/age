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
        db_log = models_super_user_logs.SuperLog(
            description = log.description,
            create_at = log.create_at
        )

        # operações no banco de dados
        self.db.add(db_log)
        self.db.commit()
        self.db.refresh(db_log)

        return db_log

    def edit(self, log_id: int, log: schemas_super_user_logs.SuperUserLogs):
            update_statement = update(models_super_user_logs.SuperLog).where(
                models_super_user_logs.SuperLog.id == log_id
            ).values(
                description = log.description,
            )

            self.db.execute(update_statement)
            self.db.commit()
            return log

    def show_all_logs(self):
        logs = self.db.query(schemas_super_user_logs.SuperUserLogs).all()
        return logs

    def remove(self, log_id: int):
        statement = select(schemas_super_user_logs.SuperUserLogs).filter_by(id=log_id)
        log = self.db.execute(statement).first()

        statement = delete(schemas_super_user_logs.SuperUserLogs).where(schemas_super_user_logs.SuperUserLogs.id == log_id)
        self.db.execute(statement)
        self.db.commit()

        return log
