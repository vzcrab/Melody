#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from os import access
from typing import Optional

from pydantic import BaseModel

from fastapp.api.schemas.token import Token

"""
用户模型

@File    :   user.py
@Time    :   2021/04/22 11:05:46
@Author  :   snc 
"""


class User(BaseModel):
    username: str
    email: Optional[str]
    disabled: Optional[bool]
    nickname: str
    avatars: str
    access_token: Token

class UserCreate(BaseModel):
    """CURD 专用
    """
    pass