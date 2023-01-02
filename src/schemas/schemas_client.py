from pydantic import BaseModel
from typing import Optional
from datetime import datetime as dt


class Client(BaseModel):
    id: Optional[int] = None
    create_at: Optional[dt]
    birth_date: Optional[dt]
    name: str
    cep: str
    UF: str
    city: str
    address: str
    number: int
    complement: str
    phone: str
    line_of_credit: str
    line_of_business: str
    start_of_business: Optional[dt]
    status_id: int
    lse_id: int
    user_id: int

    class Config:
        orm_mode = True


class SimpleClient(BaseModel):
    id: Optional[int] = None
    create_at: Optional[dt]
    name: str
    city: str
    line_of_credit: str

    class Config:
        orm_mode = True
