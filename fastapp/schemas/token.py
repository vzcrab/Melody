#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from datetime import timedelta

from pydantic import BaseModel

"""
token 模型

@File    :   token.py
@Time    :   2021/04/22 11:06:16
@Author  :   snc 
"""


class Token(BaseModel):
    type: str = "bearer"
    token: str


class TokenPayload(BaseModel):
    """[summary]

    Args:
        sub (str): 用户id
        exp: 过期时间
    """
    sub: str
    exp: timedelta = None
