# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 21:18
# @Author  : xuyiqing
# @File    : __init__.py.py


from flask import Blueprint
from flask_restful import Api


tools_bp = Blueprint('wordcloud', __name__)

api = Api(tools_bp, prefix='/api')

import app.tools.routes
