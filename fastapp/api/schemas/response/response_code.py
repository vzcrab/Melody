#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from typing import Union

from fastapi import status
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder

"""
统一响应状态码

@File    :   response_code.py
@Time    :   2021/03/14 19:51:48
@Author  :   snc 
"""


def resp_200(*, data: Union[list, dict, str] = None, message: str = "Success") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            'code': 2000,
            'message': message,
            'data': data,
        })
    )


def resp_415(*, data: Union[list, dict, str] = None, message: str = "媒体类型不支持") -> Response:
    """媒体类型不支持
    """
    return JSONResponse(
        status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        content=jsonable_encoder({
            'code': 2000,
            'message': message,
            'data': data,
        })
    )


def resp_500(*, data: Union[list, dict, str] = None, message: str = "Internal Server Error") -> Response:
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder({
            'code': 500,
            'message': message,
            'data': data,
        })
    )


# 请求参数格式错误
def resp_4001(*, data: Union[list, dict, str] = None,
              message: Union[list, dict, str] = "Request Validation Error") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            'code': 4001,
            'data': data,
            'message': message,
        })
    )


# 用户token过期
def resp_4002(*, data: Union[list, dict, str] = None, message: str = "Request Fail") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            'code': 4002,
            'data': data,
            'message': message,
        })
    )


# token认证失败
def resp_4003(*, data: Union[list, dict, str] = None, message: str = "Request Fail") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            'code': 4003,
            'data': data,
            'message': message,
        })
    )


# 内部验证数据错误
def resp_5002(*, data: Union[list, dict, str] = None, message: Union[list, dict, str] = "Request Fail") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            'code': 5002,
            'data': data,
            'message': message,
        })
    )
