#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from fastapi import FastAPI, Request, Response

from fastapp.core.config import settings
from fastapp.routers.router_v1 import api_v1_router

"""
服务器

@File    :   server.py
@Time    :   2021/03/14 14:23:03
@Author  :   snc 
"""


def create_app() -> FastAPI:
    """
    生成FatAPI对象
    :return:
    """
    app = FastAPI(
        debug=settings.DEBUG,
        title=settings.TITLE,
        description=settings.DESCRIPTION,
        docs_url=settings.DOCS_URL,
        openapi_url=settings.OPENAPI_URL,
        redoc_url=settings.REDOC_URL
    )

    # 其余的一些全局配置可以写在这里 多了可以考虑拆分到其他文件夹

    # 跨域设置
    # register_cors(app)

    # 注册路由
    register_router(app)

    # 注册捕获全局异常
    # register_exception(app)

    # 请求拦截
    # register_hook(app)

    # 取消挂载在 request对象上面的操作，感觉特别麻烦，直接使用全局的
    # register_init(app)

    """ 
    if settings.DEBUG:
        # 注册静态文件
        register_static_file(app) 
    """

    return app


def register_router(app: FastAPI) -> None:
    """注册路由

    Args:
        app (FastAPI): FastAPI
    """
    app.include_router(api_v1_router)
