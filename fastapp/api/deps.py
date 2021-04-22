#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from authlib.jose import jwt, errors
from fastapi import Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2AuthorizationCodeBearer

from fastapp.core.config import settings
from fastapp.api import schemas

"""
FastAPI 依赖

@File    :   deps.py
@Time    :   2021/04/19 14:06:08
@Author  :   snc 
"""


oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="/login/github", tokenUrl="/auth/github")  # 应该不是最佳的方案


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        claims = jwt.decode(
            token, settings.SECRET_KEY  # FIXME 固定使用一个算法
        )
        claims.validate()
    except (errors.InvalidClaimError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = claims.sub  # TODO 数据模型
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
