# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 23:42
# @Author  : xuyiqing
# @File    : config.py


class Config(object):

    DEBUG = True

    SECRET_KEY = "\x9d\xc7JM'R\x03\xc9\x9bGv\xe6\xfd\xb92\x03\xf4\x88\x02\xf5 \xa4(?"

    # SQLALCHEMY_DATABASE_URI = ''  # 'mysql+pymysql://user:password@host:port/db'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    pass


config_mapping = {
    'config': Config,
    'decelop': DevelopConfig
}
