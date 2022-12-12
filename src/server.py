import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import criar_db
from src.routers import produtos as router_produtos
from src.routers import usuarios as router_usuarios
from src.routers import pedidos as router_pedidos


# version
__version__ = "0.0.6.1"


# criação do banco de dados (so acontece uma vez)
if not os.path.exists("app_age.db"):
    criar_db()

# criação do aplicativo principal da API (age)
app = FastAPI()


# origins
origins = [
    'http://localhost:3000'  # teste local
]


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Router
app.include_router(router_produtos.router)
app.include_router(router_usuarios.router, prefix='/auth')
app.include_router(router_pedidos.router)
