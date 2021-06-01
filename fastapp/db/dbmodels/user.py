#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from fastapp.db.dbmodels.base import Base

"""
SQLAlchemy User Model

@File    :   user.py
@Time    :   2021/05/07 10:58:14
@Author  :   snc 
"""


class User(Base):
    __tablename__ = "local_userinfo"

    uid = Column(Integer, primary_key=True,
                 autoincrement=True, nullable=False)
    username = Column(String(40), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    github_auth = Column(Boolean, default=False, nullable=False)


class GithubUser(Base):
    __tablename__ = "github_userinfo"

    id = Column(Integer, primary_key=True)
    username = Column(String(40), nullable=False)
    nickname = Column(String(255))
    profile_photo = Column(String(255))
    email = Column(String(255), ForeignKey(
        'local_userinfo.email'), unique=True, nullable=False)

    user = relationship('User', backref='github_user')
