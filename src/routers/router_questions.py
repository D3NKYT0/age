from fastapi import Depends, status, APIRouter, HTTPException

from sqlalchemy.orm import Session
from typing import List

from src.resources.auth_utils import get_user_logged
from src.resources.utils import check_authorization
from src.resources.utils import add_create_at_timestamp

from src.schemas import schemas_questions
from src.infra.sqlalchemy.repository.repo_questions import RepositoryQuestions
from src.infra.sqlalchemy.config.database import get_db


router = APIRouter()


@router.get('/question/{id}', status_code=status.HTTP_200_OK, response_model=schemas_questions.SimpleQuestion, tags=["question"])
def show_question(id: int, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    question_located = add_create_at_timestamp(question_located)

    question_located = RepositoryQuestions(db).searchById(id)

    if not question_located:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not exist!")

    return question_located

@router.get('/questions/all', status_code=status.HTTP_200_OK, response_model=List[schemas_questions.SimpleQuestion], tags=["questions"])
def show_all_questions( _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    all_questions = RepositoryQuestions(db).show_all_questions()

    if not all_questions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="questions not found!")

    return all_questions

@router.post('/question', status_code=status.HTTP_201_CREATED, response_model=schemas_questions.SimpleQuestion, tags=["question"])
def create_question(question: schemas_questions.Question, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    question = add_create_at_timestamp(question)

    question_created = RepositoryQuestions(db).register(question)
    return question_created

@router.put('/question/{id}', status_code=status.HTTP_200_OK, response_model=schemas_questions.SimpleQuestion, tags=["question"])
def update_question(id: int, question: schemas_questions.Question, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    question = add_create_at_timestamp(question, True)

    # -- register log here --
    # --
    # -- end --

    question_updated = RepositoryQuestions(db).edit(id, question)
    question_updated.id = id

    return question_updated

@router.delete('/question/{id}', status_code=status.HTTP_200_OK, response_model=schemas_questions.SimpleQuestion, tags=["question"])
def delete_question(question_id: int, _ = Depends(get_user_logged) ,db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    question = add_create_at_timestamp(question, True)

    question = RepositoryQuestions(db).remove(question_id)
    return question
