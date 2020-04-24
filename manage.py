# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 22:22
# @Author  : xuyiqing
# @File    : manage.py


from flask_script import Manager
from flask_migrate import MigrateCommand


if __name__ == '__main__':
    from app import create_app
    app, socketio = create_app()
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    @manager.option('-h', '--host', dest='host', default='0.0.0.0')
    @manager.option('-p', '--port', dest='port', default=6888)
    def socketserver(host, port):
        socketio.run(app, host=host, port=port)

    manager.run()


if __name__ != '__main__':
    from app import create_app
    app, _ = create_app('develop')
