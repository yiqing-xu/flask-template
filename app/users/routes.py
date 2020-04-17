# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 13:33
# @Author  : xuyiqing
# @File    : routes.py


from app.users.apis import LoginApi, RegisterApi, LogoutApi
from app.users import api

api.add_resource(LoginApi, '/login')
api.add_resource(RegisterApi, '/register')
api.add_resource(LogoutApi, '/logout')
