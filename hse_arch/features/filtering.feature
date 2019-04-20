# Created by alina at 17.04.2019
Feature: filtering

  Scenario: Sort products by ProductIngredients
    Given a set of products in the menu
      | product_id | name      | price | description         |
      | 1          | Pen       | 30    | nice pen            |
      | 2          | Pineapple | 10    | nice pineapple      |
      | 3          | Apple     | 10    | also nice pineapple |
    And a set of ingredients
      | ingredient_id | name       |
      | 1             | mushrooms  |
      | 2             | cheese     |
      | 3             | tomato     |
    And products have the following ingredients
      | ingredient_id | product_id |
      | 1             | 1          |
      | 2             | 1          |
      | 3             | 1          |
      | 3             | 2          |
      | 1             | 3          |
   When I select mushrooms in the ingredients
   Then System returns the following set of products
      | product_id | name      | price | description         |
      | 1          | Pen       | 30    | nice pen            |
      | 3          | Apple     | 10    | also nice pineapple |

#  Scenario: # Enter scenario name here
    # Enter steps here