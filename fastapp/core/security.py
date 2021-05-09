#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from datetime import timedelta, datetime
from typing import Any, Union

from authlib.jose import jwt

from fastapp.core.config import settings
from fastapp.schemas.token import TokenPayload

"""
# 描述

@File    :   security.py
@Time    :   2021/04/20 16:16:12
@Author  :   snc 
"""


def create_access_token(
    payload: TokenPayload
) -> str:
    """生成JWT

    Args:
        payload (TokenPayload): 

    Returns:
        str: jwt
    """

    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    header = {'alg': settings.ALGORITHM}
    payload.exp = expire
    encoded_jwt = jwt.encode(header,
                             payload.dict(), settings.SECRET_KEY)
    return encoded_jwt
