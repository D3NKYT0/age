from pydantic import BaseModel
from typing import Optional


class Email(BaseModel):
    id: Optional[int] = None
    email_destino: str
    assunto: str
    conteudo: str
    n: Optional[int] = None

    class Config:
        orm_mode = True
