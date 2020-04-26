# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 21:50
# @Author  : xuyiqing
# @File    : apis.py


import os
import uuid
from datetime import datetime

import jieba
import numpy as np
from PIL import Image
from flask import current_app, send_from_directory
from flask_restful import reqparse
from wordcloud import WordCloud, STOPWORDS
from werkzeug.datastructures import FileStorage

from app.apis import Resource


class WordCloudGenApi(Resource):

    def __init__(self):
        self.path = os.path.join(current_app.root_path, 'tools/resource')
        self.stopwords = set(STOPWORDS)
        with open(os.path.join(self.path, 'stopwords.txt'), 'r', encoding='utf-8') as f:
            content = f.readlines()
        for word in content:
            self.stopwords.add(word.strip())

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('bg_img', type=FileStorage, required=True, location='files')
        self.parser.add_argument('text', type=str, required=True, location='form')
        self.args = self.parser.parse_args()

    def post(self):
        img = self.args.bg_img
        bg = np.array(Image.open(img))
        words_list = jieba.cut(self.args.text, cut_all=True)
        words = ' '.join(words_list)
        wc = WordCloud(
            background_color='white',
            mask=bg,
            stopwords=self.stopwords,
            font_path=os.path.join(self.path, 'simsun.ttc')
        )
        wc.generate(words)

        # timg = wc.to_image()
        # f = BytesIO()
        # timg.save(f, 'png')
        # data = f.getvalue()
        # import base64
        # data = base64.b64decode(data)
        # import mimetypes
        # mime_type = mimetypes.guess_type('testtest.png')[0]
        # response.headers['Content-Type'] = mime_type
        # response.headers['Content-Disposition'] = 'attachment; filename={}'.format('testtest.png')
        # resp = make_response(data)
        # resp.headers['Content-Type'] = 'image/png'
        # return send_file(img.stream, as_attachment=True, attachment_filename="filename.jpg")

        img_name = '{}.png'.format(uuid.uuid4())
        img_path = os.path.join(os.path.join(current_app.config['MEDIA_ROOT'], 'wordcloudimgs'),
                                f"{datetime.strftime(datetime.today(), '%Y/%m/%d')}")
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        wc.to_file(os.path.join(img_path, img_name))
        return send_from_directory(img_path, img_name, as_attachment=True)
