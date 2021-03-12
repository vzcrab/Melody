#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from fastapi import FastAPI

"""
fastapi主程序

@File    :   main.py
@Time    :   2021/03/12 20:58:45
@Author  :   snc 
"""

app = FastAPI()


@app.get('/')
def root():
    return {'message': '欢迎,这里是Melody!'}
