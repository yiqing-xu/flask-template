# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 22:36
# @Author  : xuyiqing
# @File    : __init__.py.py


from flask import Flask

from backend.config import config_mapping


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config_mapping['decelop'])
    from app.swagger import swagger_bp
    app.register_blueprint(swagger_bp)
    return app
