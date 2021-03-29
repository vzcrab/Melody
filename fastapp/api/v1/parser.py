#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from fastapi import APIRouter

from fastapp.api import schemas
from fastapp.models.app_info import AppInfo
"""
应用解析

@File    :   parser.py
@Time    :   2021/03/29 10:51:01
@Author  :   snc 
"""

router = APIRouter(prefix='/parser')


@router.get('/info', summary='应用信息', response_model=schemas.AppInfoModel)
def get_apk_info(file):
    # TODO file类型与如何传参

    app_info = AppInfo(file).apk_parser()

    return app_info
