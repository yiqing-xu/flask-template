# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 22:22
# @Author  : xuyiqing
# @File    : manage.py


from flask import Flask, render_template, views
from flask_script import Manager


app = Flask(__name__)


class ApiDocView(views.MethodView):

    @staticmethod
    def get():
        return render_template('swagger/index.html')


app.add_url_rule('/api/docs', view_func=ApiDocView.as_view('swagger'))


if __name__ == '__main__':
    manage = Manager(app)
    manage.run()


if __name__ != '__main__':
    pass
