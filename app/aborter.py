# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 17:03
# @Author  : xuyiqing
# @File    : aborter.py
"""
为了统一http状态码为200，具体状态码在data的code字段中体现
重写flask的Aborter类，使flask_restrul的abort能抛出状态码为200的HTTPException
"""

import traceback

from werkzeug.exceptions import Aborter as BaseAborter, HTTPException


class Success(HTTPException):

    code = 200
    description = (
        "Success"
    )


class Aborter(BaseAborter):

    def __init__(self):
        super(Aborter, self).__init__()
        self.mapping.update({Success.code: Success})


def abort(code=400, message=None, http_status_code=200, **kwargs):
    # 默认http状态码为200，抛出code=400, abort(404, 'Not Found')
    try:
        Aborter()(http_status_code)
    except HTTPException as e:
        kwargs.update(dict(
            code=code,
            message=message
        ))
        e.data = kwargs
        raise


def exception_handler(func):
    # 捕获接口报错信息
    def handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            if isinstance(err, HTTPException):
                return getattr(err, 'data')
            info = traceback.format_exc()
            abort(500, str(info))
    return handler
