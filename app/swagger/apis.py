# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 22:38
# @Author  : xuyiqing
# @File    : views.py
import yaml
from urllib.parse import urlparse

from werkzeug.datastructures import FileStorage
from flask import render_template, request, make_response
from flask_restful import Resource, reqparse
from app.swagger import api


class ApiDocView(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('doc', type=str, location='args')
        self.parser.add_argument('file', type=FileStorage, location='files')
        self.args = self.parser.parse_args()

    @api.representation("text/html")
    def get(self):
        """
        进入swagger渲染页面，doc为预览接口文档文件名
        :return:
        """
        port = urlparse(request.url).netloc.split(':')[1]
        doc = self.args.get('doc')
        return make_response(render_template('swagger/index.html',
                                             port=port,
                                             doc=doc if doc else 'swagger.yaml'))

    def post(self):
        """
        转换yaml文件为json
        :return:
        """
        file = self.args.get('file')
        if file:
            jsondata = yaml.load(file.read())
            return jsondata
        else:
            return {}
