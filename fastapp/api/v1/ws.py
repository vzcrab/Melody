#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from typing import List

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

"""
# 描述

@File    :   ws.py
@Time    :   2021/04/13 11:22:39
@Author  :   snc 
"""

router = APIRouter()


class ConnectionManager(object):
    """ 
    WebSocket连接管理
    """

    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, ws: WebSocket):
        # 等待连接
        await ws.accept()
        # 存储ws连接对象
        self.active_connections.append(ws)

    def disconnect(self, ws: WebSocket):
        # 关闭时 移除ws对象
        self.active_connections.remove(ws)

    async def send_personal_message(self, message: str, ws: WebSocket):
        # 发送个人消息
        await ws.send_text(message)


manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"你说了: {data}", websocket)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
