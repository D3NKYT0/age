from pydantic import BaseModel
from typing import Optional, List

from src.schemas.schemas_produtos import ProdutoSimples
from src.schemas.schemas_usuarios import UsuarioSimples


class Pedido(BaseModel):
    id: Optional[int] = None
    quantidade: int
    local_entrega: Optional[str]
    tipo_entrega: str
    obsercacao: Optional[str] = "Sem observações"

    usuario_id: Optional[int]
    produto_id: Optional[int]

    usuario: Optional[UsuarioSimples]
    produto: Optional[ProdutoSimples]

    class Config:
        orm_mode = True
