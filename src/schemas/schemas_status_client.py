from pydantic import BaseModel
from typing import Optional
import datetime


class StatusClient(BaseModel):
    id: Optional[int] = None
    description: str
    create_at: Optional[datetime.datetime]
    
    class Config:
        orm_mode = True
