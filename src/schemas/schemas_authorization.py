from pydantic import BaseModel
from typing import Optional

class Authorization(BaseModel):
    id: Optional[int] = None
    description: str

    class Config:
        orm_mode = True
