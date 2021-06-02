#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from fastapi import APIRouter, Depends, status

from fastapp import schemas
from fastapp.api import deps
from fastapp.api.session import session
from fastapp.middle.vuln_detection import VulnDetection
from .ws import manager

"""
漏洞扫描API

@File    :   scan.py
@Time    :   2021/05/24 16:40:27
@Author  :   snc 
"""

router = APIRouter()

# TODO 过程改为ws通信


@router.get('/url', summary='扫描APK中URL')
async def scan_url(id: str = Depends(deps.get_user_id)):
    user_sd = await session.read(id)
    vd = VulnDetection(str(user_sd.app_path))

    wsrsp = schemas.WSResponse(code=2001, status='反编译开始...')
    await manager.send_personal_message(wsrsp, user_sd.ws)
    if vd.decompile():
        # ws 通知
        url_res = vd.scan_url()
        return url_res
    else:
        # ws 失败通知
        pass
