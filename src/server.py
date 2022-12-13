import os

from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import criar_db

from src.routers import produtos as router_produtos
from src.routers import usuarios as router_usuarios
from src.routers import pedidos as router_pedidos

from starlette.middleware.base import BaseHTTPMiddleware
from src.middlewares import timer as md_timer

from src.jobs import write_notification


# version
__version__ = "0.0.6.1"
__postgressql__ = True

# criação do banco de dados (so acontece uma vez)
if not os.path.exists("app_age.db") and not __postgressql__:
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


# MIDDLEWARES CUSTOM
app.add_middleware(
    BaseHTTPMiddleware,
    dispatch=md_timer.add_process_time_header
)


# Router
app.include_router(router_produtos.router)
app.include_router(router_usuarios.router)
app.include_router(router_pedidos.router)


@app.post('/send_email')
def send_email(email: str, background: BackgroundTasks):
    background.add_task(write_notification.write, email, 'a vida é bela')
    return {"msg": 'mensagem enviada'}
