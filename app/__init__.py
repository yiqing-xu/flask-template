# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 22:36
# @Author  : xuyiqing
# @File    : __init__.py.py


from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_session import Session

from backend.config import config_mapping
from app.users.models import Account


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config_mapping['develop'])

    from app.swagger import swagger_bp
    from app.users import users_bp
    app.register_blueprint(swagger_bp)
    app.register_blueprint(users_bp)

    from backend.dbs.mysql import db
    db.init_app(app)

    migrate = Migrate()
    migrate.init_app(app, db)

    session = Session()
    session.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Account.query.get(user_id)

    return app
