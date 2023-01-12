from fastapi import Depends, status, APIRouter, BackgroundTasks, HTTPException
from fastapi_limiter.depends import RateLimiter

from src.infra.sqlalchemy.repository.repo_user import RepositoryUser
from src.infra.sqlalchemy.repository.repo_super_user import RepositorySuperUser
from src.infra.sqlalchemy.repository.repo_super_user_logs import RepositorySuperUserLogs
from src.infra.sqlalchemy.repository.repo_logs import RepositoryLogs
from src.infra.sqlalchemy.config.database import get_db
from sqlalchemy.orm import Session

from src.schemas import schemas_custom, schemas_users, schemas_super_user, schemas_super_user_logs, schemas_logs
from src.jobs import cog
from src.infra.providers import hash_provider as hp

from src.resources.auth_utils import get_user_logged, get_super_user_logged
from src.resources.utils import check_authorization
from src.resources.utils import add_create_at_timestamp


router = APIRouter()


@router.post('/email', status_code=status.HTTP_202_ACCEPTED, response_model=schemas_custom.Email, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["ti"])
def send_email(email_data: schemas_custom.Email, background: BackgroundTasks, _ = Depends(get_super_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["system"], True):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    log_data = {"description": f"O usuario {_.SuperUser.name} enviou um email para \"{email_data.destination_email}\"", "create_at": None, "super_user_id": _.SuperUser.id}
    log_data = add_create_at_timestamp(schemas_super_user_logs.SuperUserLogs(**log_data))
    RepositorySuperUserLogs(db).register(log_data)

    background.add_task(cog.send_email_task, email_data)
    return email_data

@router.get('/user/{login}', status_code=status.HTTP_200_OK, response_model=schemas_users.SimpleUser, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["ti"])
def me(login: str, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root", "admin", "manager", "user", "system"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    user = RepositoryUser(db).searchByLogin(login)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")

    # rotas get nao geram registros de logs

    return user.User


@router.post('/super_user/register/', status_code=status.HTTP_201_CREATED, response_model=schemas_super_user.SimpleSuperUser, dependencies=[Depends(RateLimiter(times=2, seconds=5))], tags=["ti"])
def create_super_users(super_user: schemas_super_user.SuperUser, _ = Depends(get_user_logged), db: Session = Depends(get_db)):

    if not check_authorization(db, _, ["root"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have authorization to access!")

    super_user = add_create_at_timestamp(super_user)

    exist = RepositorySuperUser(db).searchByLogin(super_user.login)

    if exist:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Already existing this super user!")

    log_data = {"description": f"O usuario {_.User.name} registrou um super usuario", "create_at": None, "user_id": _.User.id}
    log_data = add_create_at_timestamp(schemas_logs.Logs(**log_data))
    RepositoryLogs(db).register(log_data)

    super_user.password = hp.gerar_hash(super_user.password)
    super_user_created = RepositorySuperUser(db).register(super_user)
    return super_user_created
