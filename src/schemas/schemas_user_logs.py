from pydantic import BaseModel
from typing import Optional
from datetime import datetime as dt


class UserLogs(BaseModel):
    id: Optional[int] = None
    description: str
    create_at: Optional[dt]

    class Config:
        orm_mode = True
