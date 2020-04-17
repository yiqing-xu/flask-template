# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 23:42
# @Author  : xuyiqing
# @File    : config.py

# 'mysql+pymysql://user:password@host:port/db'

import os
import configparser

import redis

from backend.dbs.mysql import db


parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'conf.cfg'))
sqlconf = parser['mysql_38']
redisconf = parser['redis_88']


class Config(object):

    DEBUG = True

    SECRET_KEY = "\x9d\xc7JM'R\x03\xc9\x9bGv\xe6\xfd\xb92\x03\xf4\x88\x02\xf5 \xa4(?"

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{sqlconf['user']}:{sqlconf['password']}" \
                              f"@{sqlconf['user']}:{sqlconf['password']}/{sqlconf['db']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    SESSION_TYPE = 'sqlalchemy'
    SESSION_SQLALCHEMY_TABLE = 'session'
    SESSION_SQLALCHEMY = db


class DevelopConfig(Config):

    DEBUG = True

    SECRET_KEY = "\x9d\xc7JM'R\x03\xc9\x9bGv\xe6\xfd\xb92\x03\xf4\x88\x02\xf5 \xa4(?"

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{sqlconf['user']}:{sqlconf['password']}" \
                              f"@{sqlconf['user']}:{sqlconf['password']}/{sqlconf['db']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.Redis(host=redisconf['host'], port=redisconf['port'],
                                password=redisconf['password'], db=redisconf['db'])


config_mapping = {
    'config': Config,
    'develop': DevelopConfig
}
