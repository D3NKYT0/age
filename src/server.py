import os
import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import criar_db

from src.routers import produtos as router_produtos
from src.routers import usuarios as router_usuarios
from src.routers import pedidos as router_pedidos
from src.routers import custom as router_custom

from starlette.middleware.base import BaseHTTPMiddleware
from src.middlewares import timer as md_timer

import redis.asyncio as redis
from fastapi_limiter import FastAPILimiter
from src.resources.rate_limit import default_callback as limiter_default_callback
from src.data import default


# CONFIGS
__version__ = "0.0.11.1"
__postgressql__ = True


with open("auth/data/auth.json", encoding="utf-8") as auth_data:
    _auth_data = json.load(auth_data)


# criação do banco de dados (so acontece uma vez) {only sqlite}
if not os.path.exists("app_age.db") and not __postgressql__:
    criar_db()


# criação do aplicativo principal da API (age)
app = FastAPI(
    title=default.__title__,
    description=default.__description__,
    version=__version__,
    terms_of_service=default.__terms_of_service__,
    contact=default.__contact__,
    license_info=default.__license_info__,
    openapi_tags=default.__tags_metadata__
)


@app.on_event("startup")
async def startup():
    _redis = redis.from_url(_auth_data['REDIS_URI'], encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(_redis, http_callback=limiter_default_callback)


@app.on_event("shutdown")
async def shutdown():
    await FastAPILimiter.close()


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=default.origins,
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
app.include_router(router_custom.router)
