#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapp.core.config import settings

"""
SQLAlchemy Session 交互

SessionLocal 每个实例是一个数据库会话

https://fastapi.tiangolo.com/zh/tutorial/sql-databases/

@File    :   session.py
@Time    :   2021/05/06 21:50:09
@Author  :   snc 
"""

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
