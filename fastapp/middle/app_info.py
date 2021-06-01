#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import json
import os

from fastapi import HTTPException, status

from fastapp.schemas.appinfo import ApkInfo, IpaInfo
from fastapp.core.config import settings

from plugins.apk_parse3.apk_parse3.apk import APK
from plugins.ipa_parser import IosIpa as IpaParser

"""
解析apk文件

@File    :   app_info.py
@Time    :   2021/03/25 15:26:30
@Author  :   snc 
"""


class AppInfo(object):
    def __init__(self, file: str):
        self.file = file

    def apk_parser(self) -> ApkInfo:

        apkf = APK(self.file)
        if not apkf.is_valid_APK():
            raise HTTPException(
                status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail='不支持该媒体类型')

        app_info = ApkInfo(
            package=apkf.package,
            file_md5=apkf.file_md5,
            cert_md5=apkf.get_cert_md5(),
            file_size=apkf.file_size,
            androidversion=apkf.androidversion,
            sdk_version=apkf.get_target_sdk_version(),
            libraries=apkf.get_libraries(),
            files=apkf.get_files(),
            files_types=apkf.get_files_types(),
            main_activity=apkf.get_main_activity(),
            activities=apkf.get_activities(),
            services=apkf.get_services(),
            receivers=apkf.get_receivers(),
            providers=apkf.get_providers(),
            permissions=apkf.get_permissions()
        )

        # app_info = apkf.get_file(apkf.get_app_icon())
        # app_info=apkf.get_certificate()

        return app_info

    def ipa_parser(self) -> IpaInfo:
        ipaf = IpaParser(self.file)
        app_info = ipaf.get_info()
        app_info = IpaInfo(**app_info)

        return app_info

    def apk_parser_go(self):
        parser_path = os.path.join(
            settings.BASE_PATH, 'plugins', 'app_parser.exe')

        run = os.popen(parser_path+' '+self.file)
        info = run.buffer.read().decode(encoding='utf8')
        run.close()

        info = json.loads(info)

        return info
