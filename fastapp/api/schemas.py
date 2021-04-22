#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from typing import Optional

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
    package: str = ''
    file_md5: str = ''
    cert_md5: list = []
    file_size: str = ''
    androidversion: dict = {}
    sdk_version: str = ''
    libraries: list = []
    files: list = []
    files_types: dict = {}

    main_activity: str = ''

    activities: list = []
    services: list = []
    receivers: list = []
    providers: list = []
    permissions: list = []
    # icon: # 图片
    # cert_text
    # TODO 前端显示名, title字段提示, 列表...

 # 继承一个模型, 然后指定显示字段与数据类型


class User(BaseModel):
    username: str
    email: Optional[str] = None
    disabled: Optional[bool] = None


class TokenPayload(BaseModel):
    username: str
