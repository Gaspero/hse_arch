# Created by ivanshadrin at 2019-04-19
Feature: Get order total price

  Scenario: Get order total price
    Given a customer with email test-user@test.com
      And a set of products in the menu
        | product_id | name      | price | description         |
        | 1          | Pen       | 30    | nice pen            |
        | 2          | Pineapple | 10    | nice pineapple      |
        | 3          | Apple     | 10    | also nice pineapple |
      And an empty order for current customer
      And a set of OrderItems in the Order
        | order_id   | product_id      | quantity |
        | 1          | 1               | 1        |
        | 1          | 2               | 3        |
        | 1          | 3               | 3        |
    When i check order total price
    Then i see 90.0