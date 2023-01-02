from pydantic import BaseModel
from typing import Optional
from datetime import datetime as dt


class SuperUser(BaseModel):
    id: Optional[int] = None
    create_at: Optional[dt]
    name: str
    login: str
    password: str
    email: str
    classified_as: Optional[int] = 1

    class Config:
        orm_mode = True


class SimpleSuperUser(BaseModel):
    id: Optional[int] = None
    create_at: Optional[dt]
    name: str

    class Config:
        orm_mode = True
