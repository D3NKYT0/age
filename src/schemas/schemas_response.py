from pydantic import BaseModel
from typing import Optional
import datetime


class Response(BaseModel):
    id: Optional[int] = None
    description: str
    create_at: Optional[datetime.datetime]
    question_id: int
    client_id: int

    class Config:
        orm_mode = True


class SimpleResponse(BaseModel):
    id: Optional[int] = None
    description: str
    
    class Config:
        orm_mode = True
