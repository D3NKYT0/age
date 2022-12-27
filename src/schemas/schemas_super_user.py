from pydantic import BaseModel
from typing import Optional

class SuperUser(BaseModel):
    id: Optional[int] = None
    create_at: str
    name: str
    login: str
    password: str
    email: str
    classified_as: int
    

    class Config:
        orm_mode = True


class SimpleSuperUser(BaseModel):
    id: Optional[int] = None
    create_at: str
    name: str


    class Config:
        orm_mode = True