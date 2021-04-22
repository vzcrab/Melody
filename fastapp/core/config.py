#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import (AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn,
                      validator)

"""
# 描述

@File    :   config.py
@Time    :   2021/04/20 14:32:44
@Author  :   snc 
"""


class AuthGithub(object):
    CLIENT_ID: str = ''  # FIXME 设置密钥
    CLIENT_SECRET: str = ''


class Settings(BaseSettings):
    # 开发模式配置
    DEBUG: bool = True
    # 项目文档
    TITLE: str = "Melody"
    DESCRIPTION: str = "Web后端API"
    # 文档地址 默认为docs
    DOCS_URL: str = "/api/docs"
    # 文档关联请求数据接口
    OPENAPI_URL: str = "/api/openapi.json"
    # redoc 文档
    REDOC_URL: Optional[str] = "/api/redoc"

    # token过期时间 分钟
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # 生成token的加密算法
    ALGORITHM: str = "HS256"

    # 项目根路径
    BASE_PATH: str = os.getcwd()

    # Oauth2 github
    OAUTH2_GITHUB: AuthGithub = AuthGithub()

    SECRET_KEY: str = secrets.token_urlsafe(32)

    class Config:
        case_sensitive = True
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
