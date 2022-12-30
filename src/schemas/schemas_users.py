from pydantic import BaseModel
from typing import Optional
import datetime


class User(BaseModel):
    id: Optional[int] = None
    create_at: Optional[datetime.datetime]
    name: str
    login: str
    password: str
    email: str
    classified_as: int

    class Config:
        orm_mode = True


class SimpleUser(BaseModel):
    id: Optional[int] = None
    create_at: Optional[datetime.datetime]
    name: str

    class Config:
        orm_mode = True
