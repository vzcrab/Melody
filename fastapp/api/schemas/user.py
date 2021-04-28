#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from typing import Optional

from pydantic import BaseModel

"""
用户模型

@File    :   user.py
@Time    :   2021/04/22 11:05:46
@Author  :   snc 
"""


class User(BaseModel):
    username: str
    email: Optional[str] = None
    disabled: Optional[bool] = None
