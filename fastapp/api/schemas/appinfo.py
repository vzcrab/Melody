#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pydantic import BaseModel

"""
应用信息模型

@File    :   appinfo.py
@Time    :   2021/04/22 11:08:32
@Author  :   snc 
"""


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
