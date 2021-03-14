#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import shutil

from fastapi import APIRouter, File, UploadFile

from fastapp.common.logger import logger
from fastapp.core.config import settings

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

    file_path = './data/uploadfiles/'+file.filename

    try:
        with open(file_path, 'wb') as f:
            c_path = shutil.copyfileobj(file.file, f)
    except Exception as e:
        logger.error(e)
        return {'message': 'failed'}

    return {'status': 200, 'message': 'success'}
