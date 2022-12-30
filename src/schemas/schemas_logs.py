from pydantic import BaseModel
from typing import Optional
import datetime


class Logs(BaseModel):
    id: Optional[int] = None
    description: str
    create_at: Optional[datetime.datetime]
    id_user: Optional[int] = None

    class Config:
        orm_mode = True
