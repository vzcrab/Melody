#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pydantic import BaseModel

"""
响应模型-消息

@File    :   msg.py
@Time    :   2021/03/23 12:04:56
@Author  :   snc 
"""


class Msg(BaseModel):
    code: int = 2000
    msg: str
