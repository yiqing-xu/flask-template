# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 23:42
# @Author  : xuyiqing
# @File    : config.py

# 'mysql+pymysql://user:password@host:port/db'

import os
import configparser

import redis

from backend.dbs.mysql import db


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)

parser = configparser.ConfigParser()
parser.read(os.path.join(BASE_DIR, 'backend/conf.cfg'))


class Config(object):

    DEBUG = True

    BASE_DIR = BASE_DIR
    MEDIA_ROOT = MEDIA_ROOT

    SECRET_KEY = '\xc9\xe5\x02\xe3\xbe\xcf\x08\xc5\x1c\xf1\xef\x10cf\xf7\xcf'  # os.urandom(16)

    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_URL = "redis://"

    SESSION_TYPE = 'sqlalchemy'
    SESSION_SQLALCHEMY_TABLE = 'session'
    SESSION_SQLALCHEMY = db


class DevelopConfig(Config):

    DEBUG = True

    SECRET_KEY = '\xc9\xe5\x02\xe3\xbe\xcf\x08\xc5\x1c\xf1\xef\x10cf\xf7\xcf'

    sqlconf = parser['mysql_38']
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{sqlconf['user']}:{sqlconf['password']}" \
                              f"@{sqlconf['host']}:{sqlconf['port']}/{sqlconf['db']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    redisconf = parser['redis_88']
    REDIS_URL = f"redis://:{redisconf['password']}@{redisconf['host']}/{redisconf['db']}"
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.Redis(host=redisconf['host'], port=redisconf['port'],
                                password=redisconf['password'], db=redisconf['db'])


class ProductConfig(Config):

    DEBUG = False


config_mapping = {
    'config': Config,
    'develop': DevelopConfig,
    'product': ProductConfig
}
