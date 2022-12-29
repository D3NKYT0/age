from pydantic import BaseModel
from src.schemas.schemas_users import SimpleUser


class LoginSuccess(BaseModel):
    user: SimpleUser
    access_token: str


class LoginData(BaseModel):
    login: str
    password: str
