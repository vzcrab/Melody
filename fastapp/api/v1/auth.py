#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from authlib.integrations.starlette_client import OAuth
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from fastapp import schemas
from fastapp.api import deps
from fastapp.common.logger import logger
from fastapp.core import security
from fastapp.core.config import settings
from fastapp.db import crud, dbmodels

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
    try:
        token = await oauth.github.authorize_access_token(request)
    except Exception as e:
        logger.error(repr(e))
        # 重复请求，导致github code与state过期出现错误
        raise HTTPException(
            status_code=status.HTTP_425_TOO_EARLY, detail="重复请求!")
    resp = await oauth.github.get('user', token=token)
    github_user = resp.json()

    email = await oauth.github.get('user/emails', token=token)
    email = email.json()[0]['email']

    user = crud.user.get_by_email(db, email=email)
    if not user:
        user_in = schemas.user.GithubUserCreate(
            github_id=github_user['id'], username=github_user['login'], nickname=github_user['name'], profile_photo=github_user['avatar_url'], email=email)
        user = crud.user.create_github(db, obj_in=user_in)

    payload = schemas.token.TokenPayload(sub=user.uid)

    access_token = security.create_access_token(
        payload)

    return {'type': 'bearer', 'token': access_token}


@router.get('/user/info', response_model=schemas.UserInfo)
def get_userinfo(user: dbmodels.User = Depends(deps.get_current_user)):
    user_info = schemas.UserInfo(id=user.uid, username=user.username, email=user.email,
                                 nickname=user.github_user[0].nickname, avatars=user.github_user[0].profile_photo)
    return user_info
