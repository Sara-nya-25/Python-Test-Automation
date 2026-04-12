
Feature: Temperature Conversion

  Scenario: Convert Fahrenheit to Celsius
    Given the temperature is 32 degrees Fahrenheit
    When I convert it to Celsius
    Then the result should be 0 degrees Celsius

  Scenario: Convert Celsius to Fahrenheit
    Given the temperature is 100 degrees Celsius
    When I convert it to Fahrenheit
    Then the result should be 212 degrees Fahrenheit