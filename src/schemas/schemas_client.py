from pydantic import BaseModel
from typing import Optional
import datetime


class Client(BaseModel):
    id: Optional[int] = None
    create_at: Optional[datetime.datetime]
    birth_date: str
    name: str
    cep: str
    UF: str
    city: str
    address: str
    number: int
    complement: str
    phone: str
    line_of_credit: str
    line_of_business = str
    start_of_business = str
    status_id: int
    lse_id: int
    user_id: int

    class Config:
        orm_mode = True


class SimpleClient(BaseModel):
    id: Optional[int] = None
    create_at: Optional[datetime.datetime]
    name: str
    city: str
    line_of_credit: str

    class Config:
        orm_mode = True
