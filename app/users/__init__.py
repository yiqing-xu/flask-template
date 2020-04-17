# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 12:18
# @Author  : xuyiqing
# @File    : users.py

from flask import Blueprint
from flask_restful import Api
from app.users.models import Account


users_bp = Blueprint('users',
                     __name__)

api = Api(users_bp, prefix='/api')

import app.users.routes
