#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from fastapi import APIRouter

from fastapp.api.v1 import file, auth, ws, scan

"""
版本路由区分与管理路由

@File    :   router_v1.py
@Time    :   2021/03/14 14:29:00
@Author  :   snc 
"""

api_v1_router = APIRouter()

api_v1_router.include_router(file.router)
api_v1_router.include_router(ws.router)
api_v1_router.include_router(auth.router)
api_v1_router.include_router(scan.router)
