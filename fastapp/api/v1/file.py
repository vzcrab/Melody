#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Union

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status

from fastapp.api import deps
from fastapp.common.logger import logger
from fastapp.middle.app_info import AppInfo
from fastapp import schemas
from fastapp.api.session import session

"""
文件操作路由

@File    :   file.py
@Time    :   2021/03/14 10:35:26
@Author  :   snc 
"""

router = APIRouter()


@router.post('/uploadfile', summary='上传文件', response_model=Union[schemas.ApkInfo, schemas.IpaInfo], responses={415: {}})
async def create_upload_file(file: UploadFile = File(...), id: int = Depends(deps.get_user_id)):
    # TODO 前端做hash, 将值上传, 判断

    file_ext = Path(file.filename).suffix
    if file_ext not in ['.apk', '.ipa']:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail='不支持该媒体类型')

    tmp_path = __save_upload_file_tmp(file)  # 保存到临时目录

    logger.info(f"用户 {id} -> 上传文件:{file.filename} 保存至 {tmp_path}")

    app_info = __parser_app(file_ext, tmp_path)

    Path.unlink(tmp_path)

    return app_info


def __parser_app(file_ext: str, file_path: str):
    appf = AppInfo(file_path)

    # TODO 错误捕获, 解析失败, 返回错误
    if file_ext == '.apk':
        app_info = appf.apk_parser()
    elif file_ext == '.ipa':
        app_info = appf.ipa_parser()

    return app_info


def __save_upload_file_tmp(upload_file: UploadFile) -> Path:
    try:
        suffix = Path(upload_file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(upload_file.file, tmp)  # TODO 保存到MASAP临时目录
            tmp_path = Path(tmp.name)
    finally:
        upload_file.file.close()
    return tmp_path
