import datetime

from src.data.default import authotizations
from src.infra.sqlalchemy.repository.repo_classifier_user import RepositoryClassifierUser


def add_create_at_timestamp(data: object, is_log: bool = False) -> object:
    if is_log:
        data.log = datetime.datetime.now().astimezone().isoformat()
    else:
        data.create_at = datetime.datetime.now().astimezone().isoformat()
    return data


def check_authorization(db, user, authorization_list):
    classifier_id = user.User.classified_as
    classifier_obj = RepositoryClassifierUser(db).searchById(classifier_id)
    authorization_id = classifier_obj.ClassifierUser.authorization_id
    for k, v in authotizations.items():
        if authorization_id == int(k):
            if v in authorization_list:
                return True
    return False
