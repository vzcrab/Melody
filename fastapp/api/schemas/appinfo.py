#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from typing import Union

from pydantic import BaseModel

"""
应用信息模型

@File    :   appinfo.py
@Time    :   2021/04/22 11:08:32
@Author  :   snc 
"""


class AppInfoBase(BaseModel):
    type: str  # 限定 apk 与 ipa


class ApkInfo(AppInfoBase):
    type = 'apk'
    package: str
    file_md5: str
    cert_md5: list
    file_size: str
    androidversion: dict
    sdk_version: str
    libraries: list
    files: list
    files_types: dict

    main_activity: str
    activities: list
    services: list
    receivers: list
    providers: list
    permissions: list


class IpaInfo(AppInfoBase):
    type = 'ipa'
    ipa_name: str
    bundle_id: str
    version_num: str
    build_num: str
