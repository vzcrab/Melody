#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from fastapi import HTTPException, status

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

    def apk_parser(self) -> AppInfoModel:
        # TODO 类型声明
        apkf = APK(self.file)
        if not apkf.is_valid_APK():
            raise HTTPException(
                status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail='不支持该媒体类型')
        # TODO 判断是否是apk文件
        app_info = AppInfoModel()
        app_info.package = apkf.package
        app_info.file_md5 = apkf.file_md5
        app_info.cert_md5 = apkf.get_cert_md5()
        app_info.file_size = apkf.file_size
        app_info.androidversion = apkf.androidversion
        app_info.sdk_version = apkf.get_target_sdk_version()
        app_info.libraries = apkf.get_libraries()
        app_info.files = apkf.get_files()
        app_info.files_types = apkf.get_files_types()
        app_info.main_activity = apkf.get_main_activity()
        app_info.activities = apkf.get_activities()
        app_info.services = apkf.get_services()
        app_info.receivers = apkf.get_receivers()
        app_info.providers = apkf.get_providers()
        app_info.permissions = apkf.get_permissions()
        # app_info = apkf.get_file(apkf.get_app_icon())
        # app_info=apkf.get_certificate()

        return app_info
