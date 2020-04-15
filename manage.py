# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 22:22
# @Author  : xuyiqing
# @File    : manage.py


from flask_script import Manager


if __name__ == '__main__':
    from app import create_app
    app = create_app()
    manage = Manager(app)
    manage.run()


if __name__ != '__main__':
    pass
