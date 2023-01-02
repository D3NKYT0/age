from pydantic import BaseModel
from typing import Optional
from datetime import datetime as dt


class Response(BaseModel):
    id: Optional[int] = None
    description: str
    create_at: Optional[dt]
    question_id: int
    client_id: int

    class Config:
        orm_mode = True


class SimpleResponse(BaseModel):
    id: Optional[int] = None
    description: str
    
    class Config:
        orm_mode = True
