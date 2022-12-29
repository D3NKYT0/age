from pydantic import BaseModel
from typing import Optional

class Logs(BaseModel):
    id: Optional[int] = None
    description: str
    create_at: Optional[str]

    class Config:
        orm_mode = True