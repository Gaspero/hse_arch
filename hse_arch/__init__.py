import logging
from flask import Flask
from playhouse.flask_utils import FlaskDB
from flask_admin import Admin
from hse_arch.admin import init_admin
from config import Config, DevelopmentConfig
# from hse_arch.api import init_app

db = FlaskDB()  # Создаем обертку над БД
admin = Admin()  # Создаем обертку над админкой
# restful_api = Api()  # не уверен, что это делается здесь
# auth = Auth()  # не уверен, что это делается здесь
# peewee_api = RestAPI()  # не уверен, что это делается здесь


def create_app(config_class):
    from hse_arch.models.category import Category
    from hse_arch.models.customer import Customer
    from hse_arch.models.order import Order, OrderItem
    from hse_arch.models.product import Product, ProductIngredient
    from hse_arch.models.producers import Producer
    from hse_arch.models.user import User
    app = Flask(__name__)  # Создаем экземпляр класса Flask-приложения
    ms = [Product, Customer, Order, OrderItem, Producer, ProductIngredient, Category, User]
    app.config.from_object(config_class)  # Настраиваем приложение из конфиг-файла
    app.url_map.strict_slashes = False  # Указываем игнорирововать слеша в конце url
    db.init_app(app)  # Инициируем БД
    db.database.create_tables(ms)  # Создаем таблицы в БД, но это не точно
    init_admin(app, db)
    return app

# TODO: определиться, куда в подобном конфиге совать api.add_resource в create_app или в другое место
# TODO: разобраться с тем, как передавать в Application Factory объект конфига, если запускать через flask run
