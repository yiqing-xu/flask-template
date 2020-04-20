# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 16:25
# @Author  : xuyiqing
# @File    : api.py


from flask_restful import Resource as BaseResource

from app.aborter import exception_handler


class Resource(BaseResource):

    method_decorators = [exception_handler]

    def dispatch_request(self, *args, **kwargs):
        response = super(Resource, self).dispatch_request(*args, **kwargs)
        return response

    @classmethod
    def gen_response(cls, code: int = 200, message: str = '返回成功', data=None) -> dict:
        if data:
            return dict(code=code, message=message, data=data)
        return dict(code=code, message=message)
