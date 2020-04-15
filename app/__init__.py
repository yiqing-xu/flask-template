# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 22:36
# @Author  : xuyiqing
# @File    : __init__.py.py


from flask import Flask


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    from app.swagger import swagger_bp
    app.register_blueprint(swagger_bp)
    return app
