import os
import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import criar_db

from src.routers import router_auth, super_router, router_client
from src.routers import router_alternative, router_lse, router_questions, router_user
from src.routers import router_response, router_solicitation, router_authorization
from src.routers import router_classifier_user, router_status_client, router_super_user, router_super_user_logs

from starlette.middleware.base import BaseHTTPMiddleware
from src.middlewares import timer as md_timer

import redis.asyncio as redis
from fastapi_limiter import FastAPILimiter
from src.resources.rate_limit import default_callback as limiter_default_callback
from src.data import default


# CONFIGS
__version__ = "0.0.16.1"
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
app.include_router(router_auth.router, prefix='/auth')
app.include_router(super_router.router, prefix='/ti')
app.include_router(router_client.router, prefix='/client')
app.include_router(router_questions.router, prefix='/question')
app.include_router(router_lse.router, prefix='/lse')
app.include_router(router_alternative.router, prefix='/alternative')
app.include_router(router_response.router, prefix='/response')
app.include_router(router_solicitation.router, prefix='/solicitation')
app.include_router(router_authorization.router, prefix='/authorization')
app.include_router(router_status_client.router, prefix='/status_client')
app.include_router(router_super_user.router, prefix='/super_user')
app.include_router(router_super_user_logs.router, prefix='/super_user_logs')
app.include_router(router_classifier_user.router, prefix='/classifier_user')
app.include_router(router_user.router, prefix='/user')