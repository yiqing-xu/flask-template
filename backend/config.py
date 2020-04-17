# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 23:42
# @Author  : xuyiqing
# @File    : config.py

# 'mysql+pymysql://user:password@host:port/db'

import redis

from backend.dbs.mysql import db


class Config(object):

    DEBUG = True

    SECRET_KEY = "\x9d\xc7JM'R\x03\xc9\x9bGv\xe6\xfd\xb92\x03\xf4\x88\x02\xf5 \xa4(?"

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:shield@49.4.14.38:3306/backend'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    SESSION_TYPE = 'sqlalchemy'
    SESSION_SQLALCHEMY_TABLE = 'session'
    SESSION_SQLALCHEMY = db


class DevelopConfig(Config):

    DEBUG = True

    SECRET_KEY = "\x9d\xc7JM'R\x03\xc9\x9bGv\xe6\xfd\xb92\x03\xf4\x88\x02\xf5 \xa4(?"

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:shield@49.4.14.38:3306/backend'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.Redis('192.168.11.88', port='6379', password='Aegis@2018!', db=15)


config_mapping = {
    'config': Config,
    'develop': DevelopConfig
}
