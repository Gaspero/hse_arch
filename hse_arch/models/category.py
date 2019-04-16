# -*- coding: utf-8 -*-

from peewee import *
from hse_arch import db


class Category(db.Model):

    category_id = PrimaryKeyField()
    name = CharField(unique=True, null=False)

    class Meta:
        table_name = 'categories'

    def __unicode__(self):
        return '%s: %s' % (self.category_id, self.name)

    def __str__(self):
        return self.name
