from pydantic import BaseModel
from typing import Optional


class Question(BaseModel):
    id: Optional[int] = None
    description: str
    create_at: Optional[str]
    is_available: bool
    is_alternative: bool
    lse_id: int

    class Config:
        orm_mode = True


class SimpleQuestion(BaseModel):
    id: Optional[int] = None
    description: str
    
    class Config:
        orm_mode = True
