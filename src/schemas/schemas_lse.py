from pydantic import BaseModel
from typing import Optional
from datetime import datetime as dt


class Lse(BaseModel):
    id: Optional[int] = None
    quiz: str
    create_at: Optional[dt]
    is_available: bool

    class Config:
        orm_mode = True


class SimpleLse(BaseModel):
    id: Optional[int] = None
    description: str
    
    class Config:
        orm_mode = True
