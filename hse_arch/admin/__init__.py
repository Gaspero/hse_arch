# -*- coding: utf-8 -*-

from flask_peewee.admin import Admin, ModelAdmin
from flask_peewee.auth import Auth


class CustomerAdmin(ModelAdmin):
    columns = ('last_name', 'first_name', 'email', 'is_active',)


def init_admin(app, db):

    auth_admin = Auth(app, db)

    User = auth_admin.User
    User.create_table(fail_silently=True)

    if not User.select().where(User.username == 'admin').exists():
        admin = User(username='admin', email='', admin=True, active=True)
        admin.set_password('admin')
        admin.save()

    admin = Admin(app, auth_admin)

    from hse_arch.models.customer import Customer
    from hse_arch.models.order import Order, OrderItem
    from hse_arch.models.product import Product, ProductIngredient, Ingredient
    from hse_arch.models.producers import Producer
    from hse_arch.models.category import Category
    from hse_arch.models.user import User

    admin.register(Customer, CustomerAdmin)
    admin.register(Order)
    admin.register(OrderItem)
    admin.register(Product)
    admin.register(Ingredient)
    admin.register(Producer)
    admin.register(Category)
    admin.register(ProductIngredient)
    admin.register(User)
    admin.setup()

    return admin
