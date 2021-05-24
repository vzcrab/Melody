#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status

from fastapp.api import deps
from fastapp.middle.vuln_detection import VulnDetection
from fastapp.api.session import session


"""
漏洞扫描API

@File    :   scan.py
@Time    :   2021/05/24 16:40:27
@Author  :   snc 
"""

router = APIRouter()


@router.get('/url', summary='扫描APK中URL')
async def scan_url(id: str = Depends(deps.get_user_id)):
    user_sd = await session.read(id)
    vd = VulnDetection(str(user_sd['app_path']))
    url_res = vd.scan_url()
    return url_res
