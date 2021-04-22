#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import shutil
import os

from fastapi import APIRouter, File, UploadFile, HTTPException, status, Depends

from fastapp.common.logger import logger
from fastapp.core.config import settings
from fastapp.api import schemas, deps
from fastapp.models.app_info import AppInfo

"""
文件操作路由

@File    :   file.py
@Time    :   2021/03/14 10:35:26
@Author  :   snc 
"""

router = APIRouter()


@router.post('/uploadfile', summary='上传文件', response_model=schemas.AppInfoModel, responses={415: {}})
async def create_upload_file(file: UploadFile = File(...), user: schemas.User = Depends(deps.get_current_user)):
    # TODO 前端做hash, 将值上传, 判断

    logger.info(f"用户 {user} ->上传文件:{file.filename}")

    file_ext = os.path.splitext(file.filename)[-1]
    if file_ext not in ['.apk', '.ipa']:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail='不支持该媒体类型')

    uploadfile_path = os.path.join(settings.BASE_PATH, 'data', 'uploadfile')
    if not os.path.exists(uploadfile_path):
        os.makedirs(uploadfile_path)

    file_path = os.path.join(uploadfile_path, file.filename)

    with open(file_path, 'wb') as f:
        c_path = shutil.copyfileobj(file.file, f)

    app_info = AppInfo(file_path).apk_parser()  # TODO 分离出来

    return app_info

# TODO 建立一个全局的websocket
