from pydantic import BaseModel
from typing import Optional
from datetime import datetime as dt


class Logs(BaseModel):
    id: Optional[int] = None
    description: str
    create_at: Optional[dt]
    id_user: Optional[int] = None

    class Config:
        orm_mode = True
