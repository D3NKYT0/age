from pydantic import BaseModel
from typing import Optional, List

from src.schemas.schemas_produtos import ProdutoSimples


class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str
    produtos: List[ProdutoSimples] = []

    class Config:
        orm_mode = True


class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str

    class Config:
        orm_mode = True


class LoginData(BaseModel):
    telefone: str
    senha: str


class LoginSucesso(BaseModel):
    usuario: UsuarioSimples
    access_token: str
