from datetime import datetime
from peewee import *
from hse_arch import db


class Producer(db.Model):

    producer_id = PrimaryKeyField()
    name = CharField(50, null=False)
    district = CharField(50, null=False)
    address = CharField(50, null=False)
    workers = IntegerField(100, default=0)
    working_hours = CharField(100, null=False)

    class Meta:
        table_name = 'producers'

# TODO: добавить время работы
