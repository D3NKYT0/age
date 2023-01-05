from fastapi import Depends, status, APIRouter, HTTPException

from sqlalchemy.orm import Session
from typing import List

from src.resources.auth_utils import get_user_logged
from src.resources.utils import check_authorization
from src.resources.utils import add_create_at_timestamp

from src.schemas import schemas_classifier_user
from src.infra.sqlalchemy.repository.repo_classifier_user import RepositoryClassifierUser
from src.infra.sqlalchemy.config.database import get_db


router = APIRouter()


@router.get('/get/{id}', status_code=status.HTTP_200_OK, response_model=schemas_classifier_user.ClassifierUser, tags=["classifier_users"])
def show_classifier_user(id: int, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    classifier_user_located = add_create_at_timestamp(classifier_user_located)

    classifier_user_located = RepositoryClassifierUser(db).searchById(id)

    if not classifier_user_located:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Classifier user not exist!")

    return classifier_user_located

@router.get('/get/all', status_code=status.HTTP_200_OK, response_model=List[schemas_classifier_user.ClassifierUser], tags=["classifier_users"])
def show_all_classifier_users( _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    all_classifier_users = RepositoryClassifierUser(db).show_all_classifier_users()

    if not  all_classifier_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There are no classifier user located!")

    return  all_classifier_users

@router.post('/register/', status_code=status.HTTP_201_CREATED, response_model=schemas_classifier_user.ClassifierUser, tags=["classifier_users"])
def create_classifier_user(classifier_user: schemas_classifier_user.ClassifierUser, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    classifier_user_created = add_create_at_timestamp(classifier_user)

    classifier_user_created = RepositoryClassifierUser(db).register(classifier_user)
    return classifier_user_created

@router.put('/update/{id}', status_code=status.HTTP_200_OK, response_model=schemas_classifier_user.ClassifierUser, tags=["classifier_users"])
def update_classifier_user(id: int, classifier_user: schemas_classifier_user.ClassifierUser, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    classifier_user = add_create_at_timestamp(classifier_user, True)

    # -- register log here --
    # --
    # -- end --

    classifier_user_updated = RepositoryClassifierUser(db).edit(id, classifier_user)
    classifier_user_updated.id = id

    return classifier_user_updated

@router.delete('/delete/{id}', status_code=status.HTTP_200_OK, response_model=schemas_classifier_user.ClassifierUser, tags=["classifier_users"])
def delete_classifier_user(classifier_user_id: int, _ = Depends(get_user_logged) ,db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    classifier_user = add_create_at_timestamp(classifier_user_id, True)

    classifier_user = RepositoryClassifierUser(db).remove(classifier_user_id)
    return classifier_user
