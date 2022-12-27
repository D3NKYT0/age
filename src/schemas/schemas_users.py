from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[int] = None
    create_at: str
    name: str
    login: str
    password: str
    email: str
    classified_as: int

    class Config:
        orm_mode = True


class SimpleUser(BaseModel):
    id: Optional[int] = None
    create_at: str
    name: str

    class Config:
        orm_mode = True
