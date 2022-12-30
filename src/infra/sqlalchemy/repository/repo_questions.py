from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session

from src.schemas import schemas_questions
from src.infra.sqlalchemy.models import models_questions


class RepositoryQuestions():
    
    def __init__(self, db: Session):
        self.db = db

    def searchById(self, id: int):
        query = select(models_questions.Question).where(models_questions.Question.id == id)
        question = self.db.execute(query).first()
        return question

    def register(self, question: schemas_questions.Question):

        # conversao do schema em model
        db_question = models_questions.Question(
            description = question.description,
            create_at = question.create_at,
            is_available = question.is_available,
            is_alternative = question.is_alternative,
            lse_id = question.lse_id
        )

        # operações no banco de dados
        self.db.add(db_question)
        self.db.commit()
        self.db.refresh(db_question)

        return db_question

    def edit(self, question_id: int, question: schemas_questions.Question):
            update_statement = update(models_questions.Question).where(
                models_questions.Question.id == question_id
            ).values(
                description = question.description,
                is_available = question.is_available,
                is_alternative = question.is_alternative,
                lse_id = question.lse_id
            )

            self.db.execute(update_statement)
            self.db.commit()
            return question

    def show_all_questions(self):
        questions = self.db.query(models_questions.Question).all()
        return questions

    def remove(self, question_id: int):
        statement = select(models_questions.Question).filter_by(id=question_id)
        question = self.db.execute(statement).first()

        statement = delete(models_questions.Question).where(models_questions.Question.id == question_id)
        self.db.execute(statement)
        self.db.commit()

        return question
