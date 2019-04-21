# Created by alina at 20.04.2019
Feature: Changes in statuses

  Scenario: Delivery starts when producer forms an order
    Given a user paid for the order OR order status is Paid
    And producer is assigned to the order
    When producer formed the order
    Then app sends a notification with "Your courier is on his way!"
    And order status is changed to Delivery

  Scenario: User confirms the order and want to pay
    # где-то тут должна быть дополнительная проверка на доступность продюсера
    Given user has entered available location of delivery
    And order status is Pre-Order
    When a user clicks Confirm button
    Then order status is changed to delivery

  # Scenario: A user payed for his order

  # Scenario: a courier delivers the order to user

  # Scenario: canceled order



