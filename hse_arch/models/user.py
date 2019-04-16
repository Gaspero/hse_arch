import datetime
from flask_peewee.auth import BaseUser
from peewee import *
from hse_arch import db


class User(db.Model, BaseUser):
    username = CharField()
    password = CharField()
    email = CharField()
    active = BooleanField(default=True)
    admin = BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        table_name = 'user'
