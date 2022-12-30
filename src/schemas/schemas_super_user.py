from pydantic import BaseModel
from typing import Optional


class SuperUser(BaseModel):
    id: Optional[int] = None
    create_at: Optional[str]
    name: str
    login: str
    password: str
    email: str
    classified_as: Optional[int] = 1

    class Config:
        orm_mode = True


class SimpleSuperUser(BaseModel):
    id: Optional[int] = None
    create_at: Optional[str]
    name: str

    class Config:
        orm_mode = True
