#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from apk_parse3.apk import APK

from fastapp.api.schemas import AppInfoModel

"""
解析apk文件

@File    :   app_info.py
@Time    :   2021/03/25 15:26:30
@Author  :   snc 
"""


class AppInfo(object):
    def __init__(self, file):
        self.file = file

    def apk_parser(self) -> AppInfo:
        # TODO 类型声明
        apkf = APK(self.file)
        apkf.is_valid_APK()
        # TODO 判断是否是apk文件
        app_info = AppInfoModel()
        app_info.package = apkf.package
        app_info.file_md5 = apkf.file_md5
        # app_info.cert_md5=apkf.get_cert_md5()

        return app_info
