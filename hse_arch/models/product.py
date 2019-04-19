# -*- coding: utf-8 -*-

from datetime import datetime
from peewee import *
from hse_arch import db
from hse_arch.models.category import Category

class Product(db.Model):
    product_id = PrimaryKeyField()
    name = CharField(unique=True, null=False)
    price = FloatField(default=0, null=False)
    create_time = DateTimeField(default=datetime.now, null=False)
    description = CharField(null=False)
    size = CharField(null=True)
    weight = FloatField(null=True)
    energy = FloatField(null=True)
    proteins = FloatField(null=True)
    fat = FloatField(null=True)
    carbons = FloatField(null=True)
    category_id = ForeignKeyField(Category, to_field='category_id', null=True)
#    ingredient_id = ManyToManyField(ProductIngredient, to_field='ingredient_id', null=True, backref="product")

    @classmethod
    def sort_by_price(cls, direction):
        if direction == 'asc' or direction is None:
            result = cls.select().order_by(cls.price.asc())
        if direction == 'desc':
            result = cls.select().order_by(cls.price.desc())
        return result

    @classmethod
    def filter_ingredient(cls, ingr):
        result = cls\
            .select()\
            .join(ProductIngredient, on=(cls.product_id == ProductIngredient.product_id))\
            .join(Ingredient, on=(ProductIngredient.ingredient_id == Ingredient.ingredient_id))\
            .where(Ingredient.name.in_(ingr))
        return result

    class Meta:
        table_name = 'products'

    def __str__(self):
        return self.name

class Ingredient(db.Model):
    ingredient_id = PrimaryKeyField()
    name = CharField(null=False)

    class Meta:
        table_name = 'ingredients'

    def __str__(self):
        return self.name

class ProductIngredient(db.Model):
    ingredient_id = ForeignKeyField(Ingredient, backref='product_ingredients')
    product_id = ForeignKeyField(Product, backref='product_ingredients')

    class Meta:
        table_name = 'product ingredients'

    def __str__(self):
        return f'{self.ingredient_id} : {self.product_id}'
