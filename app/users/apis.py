# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 13:31
# @Author  : xuyiqing
# @File    : apis.py
import time

from flask import request
from flask_login import login_user, logout_user, login_required
from flask_restful import reqparse, abort

from app.apis import Resource
from app.users.models import Account


class LoginApi(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str, location='json')
        self.parser.add_argument('password', type=str, location='json')
        self.args = self.parser.parse_args()

    def post(self):
        response = self.gen_response()
        username = self.args.get('username')
        password = self.args.get('password')
        start = time.time()
        user = Account.query.filter_by(username=username).first()
        if user:
            if user.check_password(password):
                login_user(user)
                data = dict(
                    id=user.id,
                    username=user.username,
                    name=user.name
                )
                response.update(dict(data=data))
                print(time.time() - start)
                return response
            else:
                response.update(dict(msg='密码错误'))
                abort(403, **response)
        else:
            response.update(dict(msg='用户名不存在'))
            abort(404, **response)


class RegisterApi(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str, required=True, location='json')
        self.parser.add_argument('password', type=str, required=True,  location='json')
        self.parser.add_argument('email', type=str, location='json')
        self.parser.add_argument('name', type=str, location='json')
        self.args = self.parser.parse_args()

    def post(self):
        response = self.gen_response()
        user = Account(username=self.args['username'],
                       password=self.args['password'],
                       name=self.args.get('name'),
                       email=self.args['email'])
        user.save()
        response.update(dict(msg='注册成功'))
        return response


class LogoutApi(Resource):

    @login_required
    def post(self):
        response = self.gen_response()
        logout_user()
        response.update(dict(msg='退出成功'))
        return response
