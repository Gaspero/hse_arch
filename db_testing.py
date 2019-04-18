#вариант -- через админку добавляем в БД товары, ингредиенты и прочие радости жизни
from peewee import *
from hse_arch.models.product import Product, ProductIngredient, Ingredient
from run import app

db = SqliteDatabase('testing.db')
db.get_columns("customers")


for i in Ingredient:
    print(i.name)

for i in ProductIngredient:
    print(i.ingredient_id, i.product_id)

#найти список продуктов по игредиенту
def filter_ingredient(ingredient_list):
    result = Product.select().join(ProductIngredient).join(Ingredient).where(Ingredient.name.in_(ingredient_list))
    return result

for prod in filter_ingredient(["mushrooms"]):
    print(prod)
