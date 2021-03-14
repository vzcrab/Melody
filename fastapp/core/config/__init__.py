#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os

"""
配置

区分生产环境与开发环境

@File    :   __init__.py
@Time    :   2021/03/14 14:13:04
@Author  :   snc 
"""

# 获取环境变量
env = os.getenv("ENV", "")
if env:
    # 如果有虚拟环境 则是 生产环境
    print("----------生产环境启动------------")
    from .production_config import settings
else:
    # 没有则是开发环境
    print("----------开发环境启动------------")
    from .development_config import settings
