# -*- coding: utf-8 -*-
from hse_arch.models.product import Product
from hse_arch.models.order import Order, OrderItem
from hse_arch.models.customer import Customer

from behave import *


@given('a customer with email {email}')
def step_9(context, email):
    try:
        Customer.get(Customer.email == email)
    except Customer.DoesNotExist:
        Customer.create(email=email)


@given('an empty order for current customer')
def step_10(context):
    try:
        Order.get(Order.customer_id == 1)
    except Order.DoesNotExist:
        Order.create(customer_id=1)


@given('a set of OrderItems in the Order')
def step_11(context):
    for row in context.table:
        try:
            OrderItem.get(OrderItem.order_id == row['order_id'],
                          OrderItem.product_id == row['product_id'],
                          OrderItem.quantity == row['quantity'])
        except OrderItem.DoesNotExist:
            OrderItem.create(order_id=row['order_id'],
                             product_id=row['product_id'],
                             quantity=row['quantity'])


@when('i check order total price')
def step_12(context):
    context.result = OrderItem.get_order_amount(1)
    assert context.result


@then('i see {amount}')
def step_13(context, amount):
    assert float(amount) == context.result
