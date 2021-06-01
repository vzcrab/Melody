#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pathlib import Path
from typing import Any, Optional, Union

from pydantic import BaseModel
from fastapi import WebSocket

"""
Session 会话（服务端）数据模型

@File    :   session.py
@Time    :   2021/05/24 19:47:04
@Author  :   snc 
"""


class SessionData(BaseModel):
    session_id: str
    app_path: Union[str, Path]
    ws: Optional[Any]  # WebSocket
