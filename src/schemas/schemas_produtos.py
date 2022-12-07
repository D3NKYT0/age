from pydantic import BaseModel
from typing import Optional, List


class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str

    class Config:
        orm_mode = True


class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: int

    class Config:
        orm_mode = True

class ProdutoRetorno(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: int
    usuario: Optional[UsuarioSimples]

    class Config:
        orm_mode = True


class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float

    class Config:
        orm_mode = True
