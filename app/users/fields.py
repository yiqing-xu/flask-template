# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 15:35
# @Author  : xuyiqing
# @File    : fields.py


from flask_restful import fields

user_fields = dict(
    id=fields.Integer,
    username=fields.String,
    name=fields.String
)

users_fields_data = dict(
    code=fields.Integer,
    message=fields.String,
    data=fields.Nested(user_fields)
)

users_fields_datas = dict(
    code=fields.Integer,
    message=fields.String,
    data=fields.List(fields.Nested(user_fields))
)
