#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from datetime import timedelta, datetime
from typing import Any, Union

from authlib.jose import jwt

from fastapp.core.config import settings
from fastapp.api.schemas.token import TokenPayload

"""
# 描述

@File    :   security.py
@Time    :   2021/04/20 16:16:12
@Author  :   snc 
"""


def create_access_token(
    payload: TokenPayload
) -> str:
    """创建访问JWT

    Args:
        subject (Union[str, Any]): JWT subject
        expires_delta (timedelta, optional): 过期时间. Defaults to None.

    Returns:
        str: jwt
    """

    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    header = {'alg': settings.ALGORITHM}
    payload.exp = expire
    encoded_jwt = jwt.encode(header,
                             payload, settings.SECRET_KEY)  # 返回类型
    return encoded_jwt
