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
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(39))
    email = Column(String(255))
    id_github = Column(Integer, ForeignKey('oauth_github_user'))
    github_user = relationship('oauth_github_user', backref='github_id')


class GithubUser(Base):
    __tablename__ = "oauth_github_user"

    id = Column(Integer, primary_key=True)
