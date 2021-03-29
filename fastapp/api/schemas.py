#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pydantic import BaseModel

"""
响应模型

@File    :   schemas.py
@Time    :   2021/03/29 10:30:48
@Author  :   snc 
"""


class Msg(BaseModel):
    code: int = 2000
    msg: str


class AppInfoModel(BaseModel):
    """ 
    应用信息模型
    """
    package: str
    file_md5: str
    cert_md5: str
    file_size: int
    androidversion: dict
    sdk_version: int
    libraries: list
    files: list
    files_types: dict
    main_activity: str
    avtivities: list
    services: list
    receivers: list
    providers: list
    permissions: list
    # icon: # 图片
    # cert_text
