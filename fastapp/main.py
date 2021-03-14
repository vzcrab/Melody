#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from fastapp.core.server import create_app

"""
fastapi主程序

@File    :   main.py
@Time    :   2021/03/12 20:58:45
@Author  :   snc 
"""

app = create_app()

if __name__ == "__main__":
    import uvicorn

    # 输出所有的路由
    for route in app.routes:
        if hasattr(route, "methods"):
            print({'path': route.path, 'name': route.name, 'methods': route.methods})

    uvicorn.run(app='main:app', host="127.0.0.1",
                port=8010, reload=True, debug=True)
