#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from typing import Generator

from authlib.jose import JsonWebToken, errors
from fastapi import Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2AuthorizationCodeBearer
from sqlalchemy.orm import Session

from fastapp.common.logger import logger
from fastapp.core.config import settings
from fastapp.db.session import SessionLocal
from fastapp import schemas
from fastapp.db import crud

"""
FastAPI 依赖

@File    :   deps.py
@Time    :   2021/04/19 14:06:08
@Author  :   snc 
"""

jwt = JsonWebToken([settings.ALGORITHM])

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="/login/github", tokenUrl="/auth/github")  # 应该不是最佳的方案


def get_db() -> Generator:
    """获得数据库会话（SQLAlchemy Session）

    创建数据库会话并在使用结束后关闭

    `yield` 数据库会话 https://fastapi.tiangolo.com/zh/tutorial/dependencies/dependencies-with-yield/

    Yields:
        Generator:  
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def __jwt_decode(token: str):
    try:
        claims = jwt.decode(
            token, settings.SECRET_KEY
        )
        claims.validate()
        token_data = schemas.token.TokenPayload(**claims)
    except (errors.InvalidClaimError, errors.DecodeError, errors.BadSignatureError, errors.ExpiredTokenError) as e:
        logger.error(repr(e))
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    return token_data


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    """从token获得当前用户id,查询数据库返回用户

    Args:
        token (str, optional): jwt. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: 403 token验证失败
        HTTPException: 404

    Returns:
        user(schemas.User)
    """
    token_data = __jwt_decode(token)

    user = crud.user.get(db, token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_user_id(token: str = Depends(oauth2_scheme)):
    token_data = __jwt_decode(token)

    return token_data.sub
