# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 12:41
# @Author  : xuyiqing
# @File    : mysql.py


from flask_sqlalchemy import SQLAlchemy

from backend.utils.snowflake import gen_uid


db = SQLAlchemy()


class BaseModel(db.Model):

    __abstract__ = True

    id = db.Column(db.BigInteger, primary_key=True)

    def __init__(self, **kwargs):
        for field, val in kwargs.items():
            setattr(self, field, val)

    def save(self):
        if not self.id:
            self.id = gen_uid()
        db.session.add(self)
        db.session.commit()
