# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 12:41
# @Author  : xuyiqing
# @File    : mysql.py


from flask_sqlalchemy import SQLAlchemy

from backend.utils.snowflake import gen_uid


db = SQLAlchemy()


class BaseModel(db.Model):

    __abstract__ = True

    id = db.Column(db.BigInteger, primary_key=True)

    def __init__(self, **kwargs):
        for field, val in kwargs.items():
            setattr(self, field, val)

    @classmethod
    def commit(cls):
        db.session.commit()

    def save(self):
        if not self.id:
            self.id = gen_uid()
        db.session.add(self)
        db.session.commit()

    @classmethod
    def patch(cls):
        db.session.commit()

    @classmethod
    def add_all(cls, objs):
        for obj in objs:
            if not obj.id:
                obj.id = gen_uid()
        db.session.add_all(objs)
        db.session.commit()

    @classmethod
    def bulk_from_iter(cls, objs):
        for obj in objs:
            if not obj.id:
                obj.id = gen_uid()
            db.session.add(obj)
            db.session.commit()

    @classmethod
    def bulk_save_objects(cls, objs):
        for obj in objs:
            if not obj.id:
                obj.id = gen_uid()
        db.session.bulk_save_objects(objs)

    @classmethod
    def bulk_insert_mappings(cls, dicts):
        for item in dicts:
            if not item.get('id'):
                item.update(dicts(id=gen_uid()))
        db.session.bulk_insert_mappings(dicts)
        db.session.commit()

    def bulk_execute_insert(self, dicts):
        for item in dicts:
            if not item.get('id'):
                item.update(dicts(id=gen_uid()))
        db.session.execute(
            self.__table__.insert(),
            dicts
        )
        db.session.commit()
