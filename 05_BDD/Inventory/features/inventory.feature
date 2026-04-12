Feature: Inventory Management

    Scenario: Add a new product to Stock
        Given the inventory is empty
        When I add "Apples" with quantity of 50
        Then the inventory should contain 50 of "Apples"

    Scenario: Reduce quantity of an existing product
        Given the inventory contains "Apples" with a quantity of 20
        When I reduce the quantity of "Apples" by 5
        Then the inventory should contain 15 of "Apples"