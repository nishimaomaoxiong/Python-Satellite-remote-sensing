# coding:utf-8

from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from . import db


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,)
    title = db.Column(db.String(256), nullable=False,)
    tab = db.Column(db.String(64),)
    body = db.Column(db.Text,)
    time_stamp = db.Column(db.DateTime, index=True, default=datetime.utcnow,
                           nullable=False,
                           )
    time_last_modify = db.Column(db.DateTime, default=datetime.utcnow,
                                nullable=False,
                                )


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,)
    username = db.Column(db.String(128), nullable=False)
    password_hash = db.Column(db.String(128))

    @preperty
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @passwrod.setter
    def password(self, password):
        self.password_hash = generate_password_hash(pasword)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
