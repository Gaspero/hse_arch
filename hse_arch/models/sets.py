# -*- coding: utf-8 -*-

from datetime import datetime
from peewee import *
from hse_arch import db
from hse_arch.models.product import Product

class Set(db.Model):
    set_id = PrimaryKeyField()
    name = CharField(unique=True, null=False)
    price = FloatField(default=0, null=False)
    people = IntegerField(default=1, null=False)
    create_time = DateTimeField(default=datetime.now, null=False)
    description = CharField(null=False)

    @classmethod
    def sort_by_price(cls, direction):
        if direction == 'asc' or direction is None:
            result = cls.select().order_by(cls.price.asc())
        if direction == 'desc':
            result = cls.select().order_by(cls.price.desc())
        return result

    @classmethod
    def sort_by_people(cls, direction):
        if direction == 'asc' or direction is None:
            result = cls.select().order_by(cls.people.asc())
        if direction == 'desc':
            result = cls.select().order_by(cls.people.desc())
        return result

    class Meta:
        table_name = 'sets'

    def __str__(self):
        return self.name

class SetProduct(db.Model):
    set_id = ForeignKeyField(Set, backref='set_product')
    product_id = ForeignKeyField(Product, backref='set_product')

    class Meta:
        table_name = 'set product'

    def __str__(self):
        return self.name