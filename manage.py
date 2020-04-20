# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 22:22
# @Author  : xuyiqing
# @File    : manage.py


from flask_script import Manager
from flask_migrate import MigrateCommand

if __name__ == '__main__':
    from app import create_app
    app = create_app()
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.run()


if __name__ != '__main__':
    pass
