# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 22:40
# @Author  : xuyiqing
# @File    : routes.py


from app.swagger import api
from app.swagger.apis import ApiDocView


api.add_resource(ApiDocView, '/api/docs')
