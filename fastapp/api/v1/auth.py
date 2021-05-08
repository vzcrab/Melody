#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from authlib.integrations.starlette_client import OAuth
from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from fastapp.core import security
from fastapp.core.config import settings
from fastapp.api import deps, schemas
from fastapp.db import crud

"""
# 描述

@File    :   auth.py
@Time    :   2021/04/19 15:31:44
@Author  :   snc 
"""

router = APIRouter()

oauth = OAuth()

oauth.register(
    name='github',
    client_id=settings.OAUTH2_GITHUB.CLIENT_ID,
    client_secret=settings.OAUTH2_GITHUB.CLIENT_SECRET,
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)


@router.get("/login/github")
async def login_via_github(request: Request):
    redirect_uri = 'http://localhost:8080/login'
    return await oauth.github.authorize_redirect(request, redirect_uri)


@router.get("/auth/github", response_model=schemas.Token)
async def auth_via_github(request: Request, db: Session = Depends(deps.get_db)):
    """获取github授权，验证是否已在本地注册
    """
    # TODO httpx.ConnectTimeout 连接github超时
    token = await oauth.github.authorize_access_token(request)
    resp = await oauth.github.get('user', token=token)
    github_user = resp.json()

    email = await oauth.github.get('user/emails', token=token)

    user = crud.user.get_by_email(db, email=email)
    if not user:
        user_in = schemas.user.UserCreate()
        user = crud.user.create(db, obj_in=user_in)

    access_token = security.create_access_token(
        user.id)  # TODO id

    return {'type': 'bearer', 'access_token': access_token}
