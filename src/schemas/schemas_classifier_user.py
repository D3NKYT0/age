from pydantic import BaseModel
from typing import Optional
import datetime


class ClassifierUser(BaseModel):
    id: Optional[int] = None
    description: str
    create_at: Optional[datetime.datetime]
    authorization_id: int

    class Config:
        orm_mode = True
