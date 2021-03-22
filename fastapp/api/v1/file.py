#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import shutil
import os

from fastapi import APIRouter, File, UploadFile

from fastapp.common.logger import logger
from fastapp.core.config import settings
from fastapp.api.schemas.response import response_code

"""
文件操作路由

@File    :   file.py
@Time    :   2021/03/14 10:35:26
@Author  :   snc 
"""

router = APIRouter()


@router.post('/uploadfile', summary='上传文件')
async def create_upload_file(file: UploadFile = File(...)):
    # TODO 前端做hash, 将值上传, 判断
    # TODO 权限, 用户上传
    # TODO 类型验证
    # 类型验证, 可以用content_tpye 文件问类型, mime, 这种前端发包改不就行了, 没有什么意义
    # 第二种, 由工具判别就行, 功能不能读肯定就会报错, 这个时候返回错误信息就行了
    # 第三种, 使用第三方库判断
    # 第四种, os库获取文件后缀, 进行判断

    logger.info(f"用户->上传文件:{file.filename}")

    file_ext = os.path.splitext(file.filename)[-1]
    if file_ext != 'apk' or file_ext != 'ipa':
        return response_code.resp_415()

    uploadfile_path = os.path.join(settings.BASE_PATH, 'data', 'uploadfile')
    if not os.path.exists(uploadfile_path):
        os.makedirs(uploadfile_path)

    file_path = os.path.join(uploadfile_path, file.filename)

    try:
        with open(file_path, 'wb') as f:
            c_path = shutil.copyfileobj(file.file, f)
    except Exception as e:
        logger.error(e)
        return response_code.resp_500()

    return response_code.resp_200()
