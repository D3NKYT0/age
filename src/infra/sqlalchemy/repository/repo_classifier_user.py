from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session

from src.schemas import schemas_classifier_user
from src.infra.sqlalchemy.models import models_classifier_user


class RepositoryClassifierUser():
    
    def __init__(self, db: Session):
        self.db = db

    def searchById(self, id: int):
        query = select(models_classifier_user.ClassifierUser).where(models_classifier_user.ClassifierUser.id == id)
        classifieruser = self.db.execute(query).first()
        return classifieruser

    def searchByDescription(self, description: str):
        query = select(models_classifier_user.ClassifierUser).where(models_classifier_user.ClassifierUser.description == description)
        authorization = self.db.execute(query).first()
        return authorization

    def register_classifier_user(self, classifieruser: schemas_classifier_user.ClassifierUser):

        # conversao do schema em model
        db_classifier = models_classifier_user.ClassifierUser(
            description = classifieruser.description,
            create_at = classifieruser.create_at
        )

        # operações no banco de dados
        self.db.add(db_classifier)
        self.db.commit()
        self.db.refresh(db_classifier)

        return db_classifier

    def edit_classifier_user(self, classifier_user_id: int, classifier_user: schemas_classifier_user.ClassifierUser):
        
            update_statement = update(models_classifier_user.ClassifierUser).where(
                models_classifier_user.ClassifierUser.id == classifier_user_id
            ).values(
                description = classifier_user.description
            )

            self.db.execute(update_statement)
            self.db.commit()
            return classifier_user

    def show_all_classifier_users(self):
        classifier_user = self.db.query(models_classifier_user.ClassifierUser).all()
        return classifier_user

    def remove_classifier_user(self, classifier_user_id: int):
        statement = select(models_classifier_user.ClassifierUser).filter_by(id=classifier_user_id)
        classifier_user_id= self.db.execute(statement).first()

        statement = delete(models_classifier_user.ClassifierUser).where(models_classifier_user.ClassifierUser.id == classifier_user_id)
        self.db.execute(statement)
        self.db.commit()

        return classifier_user_id
