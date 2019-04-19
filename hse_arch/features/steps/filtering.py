# -*- coding: utf-8 -*-
from hse_arch.models.product import Product, ProductIngredient, Ingredient
from behave import *

@given('a set of products in the menu')
def step_1(context):
    context.my_table1 = context.table
    for row in context.my_table1:
        try:
            Product.get(Product.name == row['name'])
        except Product.DoesNotExist:
            Product.create(#product_id = row['product_id'],
                           name=row['name'],
                           price=row['price'],
                           description=row['description'])

@given('a set of ingredients')
def also_step_1(context):
    context.my_table3 = context.table
    for row in context.my_table3:
        try:
            Ingredient.get(Ingredient.ingredient_id == row['ingredient_id'])
        except Ingredient.DoesNotExist:
            Ingredient.create(#ingredient_id=row['ingredient_id'],
                              name=row['name'])

@given('products have the following ingredients')
def also_step_12(context):
    context.my_table2 = context.table
    for row in context.my_table2:
        try:
            ProductIngredient.get(ProductIngredient.ingredient_id == row['ingredient_id'])
        except ProductIngredient.DoesNotExist:
            ProductIngredient.create(ingredient_id=row['ingredient_id'],
                                     product_id=row['product_id'])

@when('I select mushrooms in the ingredients')
def step_2(context):
    pass
    #context.result = Product.filter_products(["mushrooms"])
   #assert context.result

@then('System returns the following set of products')
def step3(context):
    pass

#    for index, row in enumerate(context.result):
#        print("---", index, row)
        #assert row['name'] == context.my_table1[index].name
