import sqlite3
from flask_restful import Resource
# Resource what the api asks for, can use....external representation of entity
# Model internal representation of entity
from db import db


class UserModel(db.Model):
    TABLE_NAME = 'users'
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        # must match columns above
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()  # returning user model object

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()  # returning user model object

