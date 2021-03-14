#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import time

from loguru import logger

from fastapp.core.config import settings

"""
日志记录程序

@File    :   logger.py
@Time    :   2021/03/14 14:49:53
@Author  :   snc 
"""

# 日志文件
log_path = os.path.join(settings.BASE_PATH, 'logs')

if not os.path.exists(log_path):
    os.mkdir(log_path)

log_path_error = os.path.join(
    log_path, f'{time.strftime("%Y-%m-%d")}_error.log')


# 日志简单配置
logger.add(log_path_error, rotation="12:00", retention="5 days", enqueue=True)

__all__ = ["logger"]
