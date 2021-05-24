#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from fastapp.schemas import session
from typing import Any, Dict, Optional

from fastapp import schemas

"""
会话管理（服务端）

存储用户数据

@File    :   session.py
@Time    :   2021/05/24 19:41:52
@Author  :   snc 
"""


class InMemorySession(object):
    """在 `dict` 存储会话数据
    """

    def __init__(self) -> None:
        self.data: dict = dict()

    async def read(
        self,
        session_id: str
    ) -> schemas.SessionData:
        result = self.data.get(session_id)
        if not result:
            return None
        print(result)
        return result.copy()

    async def write(self, session_data: schemas.SessionData) -> bool:
        session_id = session_data.session_id
        session_dict = session_data.dict()
        del session_dict['session_id']
        self.data[session_id] = session_dict
        return True

    async def remove(self, session_id: str) -> None:
        del self.data[session_id]

    async def exists(self, session_id: str) -> bool:
        return session_id in self.data


session = InMemorySession()  # TODO 最佳实现
