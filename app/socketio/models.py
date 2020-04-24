# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 9:16
# @Author  : xuyiqing
# @File    : models.py


from datetime import datetime

from backend.dbs.mysql import BaseModel, db


class RoomModel(BaseModel):
    """
    用户个人房间
    """

    __tablename__ = 'socketio_room'

    room = db.Column(db.String(100), unique=True, comment='用户连接socketio的sid')
    user_id = db.Column(db.BigInteger, db.ForeignKey('users_account.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('Account', backref=db.backref('scoketio_room'))

    def __repr__(self):
        return '{}-{}'.format(self.user, self.room)


class MessageModel(BaseModel):
    """
    消息
    """

    __tablenmae__ = 'socketio_message'

    sender_id = db.Column(db.BigInteger, db.ForeignKey('users_account.id', ondelete='CASCADE'),
                          nullable=False, comment='发送者')
    sender = db.relationship('Account', backref=db.backref('message_sender'), foreign_keys=sender_id)
    receiver_id = db.Column(db.BigInteger, db.ForeignKey('users_account.id', ondelete='CASCADE'),
                            nullable=False, comment='接收者')
    reveiver = db.relationship('Account', backref=db.backref('mesasge_reveiver'), foreign_keys=receiver_id)
    message = db.Column(db.Text, comment='消息内容')
    create_time = db.Column(db.DateTime, default=datetime.now, comment='创建时间')

    def __repr__(self):
        return '{}-send2-{}-{}'.format(self.sender, self.receiver, self.message)
