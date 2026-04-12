
Feature: Bank Account Management

  Scenario: Create new account
    Given I create a new account for "Alice"
    Then the balance should be 0

  Scenario: Deposit money
    Given an account for "Alice" with 100
    When I deposit 50 into the account
    Then the balance should be 150

  Scenario: Withdraw money
    Given an account for "Alice" with 100
    When I withdraw 30 from the account
    Then the balance should be 70

  Scenario: Apply interest
    Given an account for "Alice" with 200
    When I apply 5% interest
    Then the balance should be 210

  Scenario: Transfer money between accounts
    Given an account for "Alice" with 100
    And an account for "Bob" with 50
    When "Alice" transfers 40 to "Bob"
    Then "Alice" should have 60
    And "Bob" should have 90