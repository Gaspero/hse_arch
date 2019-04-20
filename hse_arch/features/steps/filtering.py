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
            Product.create(name=row['name'],
                           price=row['price'],
                           description=row['description'])


@given('a set of ingredients')
def also_step_1(context):
    context.my_table3 = context.table
    for row in context.my_table3:
        try:
            Ingredient.get(Ingredient.ingredient_id == row['ingredient_id'])
        except Ingredient.DoesNotExist:
            Ingredient.create(name=row['name'])


@given('products have the following ingredients')
def also_step_12(context):
    context.my_table2 = context.table
    for row in context.my_table2:
        try:
            ProductIngredient.get(ProductIngredient.ingredient_id == row['ingredient_id'] &
                                  ProductIngredient.product_id == row['product_id'])
        except ProductIngredient.DoesNotExist:
            ProductIngredient.create(ingredient_id=row['ingredient_id'],
                                     product_id=row['product_id'])


@when('I select mushrooms in the ingredients')
def step_2(context):
    context.result = Product.filter_ingredient(["mushrooms"])
    assert context.result


@then('System returns the following set of products')
def step3(context):
    context.my_table3 = context.table
    for row, result in zip(context.my_table3, context.result):
        assert row['name'] == result.name
