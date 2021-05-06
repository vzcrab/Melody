#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String

"""
# 描述

@File    :   base.py
@Time    :   2021/05/06 10:37:10
@Author  :   snc 
"""

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(39))
    email = Column(String(255))


class GithubUser(Base):
    __tablename__ = ""
