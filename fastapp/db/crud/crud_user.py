#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from fastapp.db.crud.base import CRUDBase
from fastapp.db import dbmodels as models
from fastapp import schemas

"""
CRUD-用户表

@File    :   crud_user.py
@Time    :   2021/05/07 10:42:38
@Author  :   snc 
"""


class CRUDUser(CRUDBase[models.User]):
    def get_by_email(self, db: Session, *, email: str):
        return db.query(models.User).filter(models.User.email == email).first()

    def create_github(self, db: Session, *, obj_in: schemas.user.GithubUserCreate):
        db_obj_u = models.User(email=obj_in.email,
                               username=obj_in.username, github_auth=True)

        db_obj_g = models.GithubUser(id=obj_in.github_id, username=obj_in.username,
                                     nickname=obj_in.nickname, profile_photo=obj_in.profile_photo, email=obj_in.email)
        db.add(db_obj_u)
        db.add(db_obj_g)
        db.commit()
        db.refresh(db_obj_u)

        return db_obj_u


user = CRUDUser(models.User)
