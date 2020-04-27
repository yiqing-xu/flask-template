# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 13:31
# @Author  : xuyiqing
# @File    : apis.py


from flask import request, session, sessions
from flask_login import login_user, logout_user, login_required
from flask_restful import reqparse, marshal_with

from app.apis import Resource
from app.users.models import Account
from app.users.fields import users_fields_data, users_fields_datas
from app.aborter import abort


class LoginApi(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str, location='args')
        self.parser.add_argument('password', type=str, location='args')
        self.args = self.parser.parse_args()

    @marshal_with(users_fields_data)
    def post(self):
        username = self.args.username
        password = self.args.password
        user = Account.query.filter_by(username=username).first()
        if user:
            if user.check_password(password):
                login_user(user)
                response = self.gen_response(data=user)
                return response
            else:
                abort(403, '用户名/密码错误')
        else:
            abort(404, '该用户不存在')

    @marshal_with(users_fields_datas)
    def get(self):
        users = Account.query.all()
        data = self.gen_response(data=users)
        return data


class RegisterApi(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str, required=True, location='json')
        self.parser.add_argument('password', type=str, required=True,  location='json')
        self.parser.add_argument('email', type=str, location='json')
        self.parser.add_argument('name', type=str, location='json')
        self.args = self.parser.parse_args()

    @marshal_with(users_fields_data)
    def post(self):
        user = Account(username=self.args.username,
                       password=self.args.password,
                       name=self.args.name,
                       email=self.args.email)
        if user.is_valid(user.username):
            user.save()
        response = self.gen_response(data=user)
        return response


class LogoutApi(Resource):

    @login_required
    def post(self):
        logout_user()
        response = self.gen_response(message='退出成功')
        return response
