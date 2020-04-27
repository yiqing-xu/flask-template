# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 22:37
# @Author  : xuyiqing
# @File    : __init__.py.py


from flask import Blueprint
from flask_restful import Api

swagger_bp = Blueprint('swagger', __name__)

api = Api(swagger_bp)

from app.swagger import routes
