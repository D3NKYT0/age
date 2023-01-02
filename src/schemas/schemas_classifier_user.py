from pydantic import BaseModel
from typing import Optional
from datetime import datetime as dt


class ClassifierUser(BaseModel):
    id: Optional[int] = None
    description: str
    create_at: Optional[dt]
    authorization_id: int

    class Config:
        orm_mode = True
