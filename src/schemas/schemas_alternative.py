from pydantic import BaseModel
from typing import Optional
from datetime import datetime as dt

class Alternative(BaseModel):
    id: Optional[int] = None
    description: str
    weight: float
    is_available: bool
    create_at: Optional[dt]
    question_id: int

    class Config:
        orm_mode = True


class SimpleAlternative(BaseModel):
    id: Optional[int] = None
    description: str
    
    class Config:
        orm_mode = True
