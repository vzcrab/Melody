#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from plugins.vuln_detection.matching import MATCH

from fastapp.core.config import settings

"""
中间层-漏洞检测

@File    :   vuln_detection.py
@Time    :   2021/05/24 16:27:19
@Author  :   snc 
"""


class VulnDetection(object):
    """对APK文件漏洞扫描
    """

    def __init__(self, file, output=settings.DATA_PATH) -> None:
        """
        Args:
            file (str): 应用路径
            output (str, optional): 输出路径. Defaults to settings.DATA_PATH.
        """
        super().__init__()
        self.file = file
        self.output = output

    def scan_url(self):
        """检测APK中URL

        Returns:
            [type]: [description]
        """
        result = MATCH(settings.BASE_PATH, self.file, self.output).match_url()

        return result
