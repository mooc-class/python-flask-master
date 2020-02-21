# coding: utf-8
from application import db


class User(db.Model):
    __tablename__ = 'user'

    Host = db.Column(db.String(60, 'utf8_bin'), primary_key=True, nullable=False, server_default=db.FetchedValue())
    User = db.Column(db.String(32, 'utf8_bin'), primary_key=True, nullable=False, server_default=db.FetchedValue())
    password_last_changed = db.Column(db.DateTime)
    password_lifetime = db.Column(db.SmallInteger)
