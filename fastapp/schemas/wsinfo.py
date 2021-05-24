#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pydantic import BaseModel

"""
websocket 前端通信模型

@File    :   wsinfo.py
@Time    :   2021/05/18 20:33:28
@Author  :   snc 
"""


class WSResponse(BaseModel):
    code: int
    status: str
