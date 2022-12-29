from pydantic import BaseModel
from typing import Optional

class ClassifierUser(BaseModel):
    id: Optional[int] = None
    description: str
    create_at: Optional[str]
    authorization_id: int

    class Config:
        orm_mode = True