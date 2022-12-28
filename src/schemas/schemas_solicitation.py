from pydantic import BaseModel
from typing import Optional

class Solicitation(BaseModel):
    id: Optional[int] = None
    description: str
    create_at: str
    
    class Config:
        orm_mode = True