from math import ceil

from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_429_TOO_MANY_REQUESTS


async def default_callback(request: Request, response: Response, pexpire: int):
    """
    default callback when too many requests
    :param request:
    :param pexpire: The remaining milliseconds
    :param response:
    :return:
    """
    expire = ceil(pexpire / 1000)

    __headers__ = {
        "Retry-After": str(expire)
    }

    raise HTTPException(HTTP_429_TOO_MANY_REQUESTS, "Too Many Requests", headers=__headers__)
