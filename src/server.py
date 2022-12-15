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


# CONFIGS
__version__ = "0.0.9.1"
__postgressql__ = True
__title__ = "Conecta Age"
__terms_of_service__ = "https://github.com/D3NKYT0/age/blob/master/LICENSE"


with open("auth/data/auth.json", encoding="utf-8") as auth_data:
    _auth_data = json.load(auth_data)


# criação do banco de dados (so acontece uma vez) {only sqlite}
if not os.path.exists("app_age.db") and not __postgressql__:
    criar_db()


__description__ = """
A ConectaAGE é uma api em desenvolvimento (atualmente) para AGE-PE afim de intercomunicar suas aplicações WEB/MOBILE com a agencia. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

__tags_metadata__ = [
    {
        "name": "usuarios",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "produtos",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "pedidos",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "email",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "auth",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

__contact__ = {
        "name": "Daniel Amaral",
        "url": "https://github.com/D3NKYT0",
        "email": "danielamaral.f@age.pe.gov.br",
    }

__license_info__ = {
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }


# criação do aplicativo principal da API (age)
app = FastAPI(
    title=__title__,
    description=__description__,
    version=__version__,
    terms_of_service=__terms_of_service__,
    contact=__contact__,
    license_info=__license_info__,
    openapi_tags=__tags_metadata__
)


@app.on_event("startup")
async def startup():
    _redis = redis.from_url(_auth_data['REDIS_URI'], encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(_redis, http_callback=limiter_default_callback)


@app.on_event("shutdown")
async def shutdown():
    await FastAPILimiter.close()


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
app.include_router(router_custom.router)
