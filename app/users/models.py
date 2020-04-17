# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 12:19
# @Author  : xuyiqing
# @File    : models.py


from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from backend.dbs.mysql import BaseModel, db


class Account(UserMixin, BaseModel):

    __tablename__ = 'users_account'

    username = db.Column(db.String(20), unique=True)
    _password = db.Column(db.String(255))
    email = db.Column(db.String(30), nullable=True)
    name = db.Column(db.String(10), nullable=True)

    def __init__(self, username=None, password=None, name=None, email=None):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def check_password(self, user_pwd):
        return check_password_hash(self._password, user_pwd)
