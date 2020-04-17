# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 16:25
# @Author  : xuyiqing
# @File    : api.py


from typing import Union

from flask_restful import Resource as BaseResource


class Resource(BaseResource):

    # method_decorators = [login_required]

    @classmethod
    def gen_response(cls, code: int = 200, msg: str = '返回成功', data: Union[dict, list] = None):
        if data:
            return dict(code=code, msg=msg, data=data)
        return dict(code=code, msg=msg)
