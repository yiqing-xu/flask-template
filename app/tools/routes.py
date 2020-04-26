# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 21:57
# @Author  : xuyiqing
# @File    : routes.py


from app.tools import api

from app.tools.apis import WordCloudGenApi


api.add_resource(WordCloudGenApi, '/word_cloud')

