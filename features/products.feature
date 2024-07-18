Feature: Manage Products

  Background:
    Given the following products
      | name     | category    | available | price |
      | Product1 | Electronics | True      | 100   |
      | Product2 | Clothing    | False     | 50    |

  Scenario: Read a product
    When I get the product with id 1
    Then the response status code should be 200
    And the response should contain "Product1"

  Scenario: Update a product
    When I update the product with id 1
      | name | Updated Product |
    Then the response status code should be 200
    And the response should contain "Updated Product"

  Scenario: Delete a product
    When I delete the product with id 1
    Then the response status code should be 204

  Scenario: List all products
    When I list all products
    Then the response status code should be 200
    And the response should contain 2 products

  Scenario: Find product by name
    When I search for products with name "Product1"
    Then the response status code should be 200
    And the response should contain "Product1"

  Scenario: Find product by category
    When I search for products with category "Electronics"
    Then the response status code should be 200
    And the response should contain "Product1"

  Scenario: Find product by availability
    When I search for products with availability "True"
    Then the response status code should be 200
    And the response should contain "Product1"

