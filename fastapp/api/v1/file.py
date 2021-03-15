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
    # TODO 配置
    # TODO 类型验证

    logger.info(f"用户->上传文件:{file.filename}")

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
