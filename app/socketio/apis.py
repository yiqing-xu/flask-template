# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 12:10
# @Author  : xuyiqing
# @File    : apis.py


import json

from flask import request, current_app, session
from flask_login import current_user
from flask_socketio import Namespace
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from .models import RoomModel, MessageModel


class CustomSocketNamespace(Namespace):
    """
    Class-Based Namespaces
    基于类的事件监听命名，事件名以${on_event}形式定义
    调用emit方法实现消息发送
        1 - 指向性发送至指定用户，emit(evet, data, room, namespace)
            import json
            from flask_socketio import emit
            from app.socketio.models import RoomModel

            room = RoomModel.query.filter_by(user_id=user_id).first()
            if room:
                roomsid = room.room
                emit('receive_message', json.dumps({'data': 'ok'}), room=room, namespace='/ws')

        2 - 广播发送指定命名空间的所有在线用户
            emit('receive_message', json.dumps({'data': 'ok'}), namespace='/ws', broadcast=True)
    """

    def on_connect(self):
        """
        建立连接
        :return:
        """
        if not current_user.is_authenticated:
            return
        sid = getattr(request, 'sid')
        try:
            room = RoomModel.query.filter_by(user_id=current_user.id).one()
        except NoResultFound:
            room = RoomModel(user_id=current_user.id, room=sid)
            room.save()
        except MultipleResultsFound:
            RoomModel.query.filter_by(user_id=current_user.id).delete()
            RoomModel.commit()
            room = RoomModel(user_id=current_user.id, room=sid)
            room.save()
        else:
            room.room = sid
            room.commit()
        finally:
            self.emit('receive_message',
                      data=self.init_data(dict(code=200,
                                               msg='连接成功',
                                               data=dict(user_id=current_user.id,
                                                         username=current_user.username)
                                               )),
                      room=sid)

    def on_disconnect(self):
        """
        断开连接
        :return:
        """
        # self.close_room(room=getattr(request, 'sid'))
        RoomModel.query.filter_by(user_id=current_user.id).delete()
        RoomModel.commit()

    def on_message(self, data):
        """
        event事件
        :param data:
        :return:
        """
        print(data)
        self.emit('receive_message', self.init_data(data))

    @staticmethod
    def init_data(data: dict):
        return json.dumps(data, ensure_ascii=False)


def need_authenticated(func):
    import functools

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            from flask_socketio import disconnect
            disconnect()
        else:
            return func(*args, **kwargs)
    return wrapped
