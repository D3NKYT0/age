from pydantic import BaseModel
from typing import Optional
from datetime import datetime as dt


class SuperUserLogs(BaseModel):
    id: Optional[int] = None
    description: str
    create_at: Optional[dt]
    super_user_id: int

    class Config:
        orm_mode = True
