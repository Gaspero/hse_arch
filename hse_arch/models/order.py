# -*- coding: utf-8 -*-

from datetime import datetime
from peewee import *
from hse_arch import db
from hse_arch.models.customer import Customer
from hse_arch.models.product import Product
from hse_arch.models.producers import Producer

"""
STATUSES = ((1, 'Pre-Order'),
            (2, 'Payment'),
            (3, 'Paid'),
            (4, 'Formation'),
            (5, 'Delivery'),
            (6, 'Performed'))
"""


class Order(db.Model):
    order_id = PrimaryKeyField()
    customer_id = ForeignKeyField(Customer, to_field='customer_id', null=False)
    order_status = CharField(default="Pre-Order", null=False)
    create_time = DateTimeField(default=datetime.now, null=False)
    district = CharField(50, null=True)
    producer_id = ForeignKeyField(Producer, to_field='producer_id', null=True)  # TODO: сделать присвоение на опр. этапе

    class Meta:
        table_name = 'orders'

    # метод для получения продюсеров, подходящих заказу по району
    def find_producers(self):
        query = Producer.select().where(Producer.district == self.district)
        return query if query else None  # else 'No producers available'


class OrderItem(db.Model):
    item_id = PrimaryKeyField()
    order_id = ForeignKeyField(Order, backref='items')
    product_id = ForeignKeyField(Product, to_field='product_id', null=False)
    # list_price = FloatField(default=0, null=False) ???
    quantity = IntegerField(default=0, null=False)

    # метод для получения количества айтемов в заказе
    @classmethod
    def get_order_item_number(cls, order_id):
        query = cls.select().where(cls.order_id == order_id)  # делаем запрос к БД, чтобы получить Order по id
        return len(query)  # возращаем количество аттрибутов OrderItem у данного Order

    class Meta:
        table_name = 'order_items'

    # метод для получения стоимости заказов в корзине
    @classmethod
    def get_order_amount(cls, order_id):
        subquery = (cls
                    .select(fn.SUM(Product.price * cls.quantity).alias('sum'))  # получаем сумму цена*количество
                    .join(Product, on=(cls.product_id == Product.product_id))  # добавляем продукт чтобы получить цену
                    .where(cls.order_id == order_id))  # результат только для items в указанном ордере
        return subquery[0].sum
