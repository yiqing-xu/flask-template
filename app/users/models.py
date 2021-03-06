# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 12:19
# @Author  : xuyiqing
# @File    : models.py


from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from backend.dbs.mysql import BaseModel, db
from app.aborter import abort


class Account(UserMixin, BaseModel):

    __tablename__ = 'users_account'

    username = db.Column(db.String(20), unique=True, comment='用户名')
    _password = db.Column(db.String(255), comment='密码')
    email = db.Column(db.String(30), comment='邮箱')
    name = db.Column(db.String(10), comment='姓名')

    def __init__(self, **kwargs):
        super(Account, self).__init__(**kwargs)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def check_password(self, user_pwd):
        return check_password_hash(self._password, user_pwd)

    def is_valid(self, username):
        if not self.query.filter_by(username=username).count():
            return True
        else:
            abort(409, '用户名重复')


# class Permission(BaseModel):
#
#     __tablename__ = 'users_permission'
#
#     user = db.Column(db.BigInteger, db.ForeignKey('users_account.id', ondelete='CASCADE'), )
