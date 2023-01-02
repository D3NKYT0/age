from pydantic import BaseModel
from typing import Optional
from datetime import datetime as dt


class User(BaseModel):
    id: Optional[int] = None
    create_at: Optional[dt]
    name: str
    login: str
    password: str
    email: str
    classified_as: int

    class Config:
        orm_mode = True


class SimpleUser(BaseModel):
    id: Optional[int] = None
    create_at: Optional[dt]
    name: str

    class Config:
        orm_mode = True
