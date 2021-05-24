#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os

import json

"""
app_parser 解析(go) -> 可执行文件 -> python

@File    :   parser_helper.py
@Time    :   2021/04/22 20:53:50
@Author  :   snc 
"""

parser_exe = 'app_parser.exe'


def get_info(path: str):
    parser_path = os.path.join(
        os.getcwd(), 'plugins', parser_exe)

    info = os.popen(parser_path+' '+path)
    a = info.buffer.read().decode(encoding='utf8')
    print(a)
    b = json.loads(a)
    print(b)
    info.close()


if __name__ == "__main__":
    file_path = os.path.join(
        os.getcwd(), 'plugins', 'anro.apk')
    get_info(file_path)
