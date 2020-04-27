# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 12:10
# @Author  : xuyiqing
# @File    : websocket.py


from flask_socketio import SocketIO

from app.socketios.apis import CustomSocketNamespace

socketio = SocketIO()
socketio.on_namespace(CustomSocketNamespace('/ws'))
