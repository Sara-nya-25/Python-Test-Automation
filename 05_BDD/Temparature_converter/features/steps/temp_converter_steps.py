
from behave import given, when, then
from src.temp_converter import fahrenheit_to_celsius, celsius_to_fahrenheit

@given('the temperature is {value:d} degrees Fahrenheit')
def step_given_fahrenheit(context, value):
    context.input_temp = value

@when('I convert it to Celsius')
def step_when_to_celsius(context):
    context.result = fahrenheit_to_celsius(context.input_temp)

@then('the result should be {expected:d} degrees Celsius')
def step_then_celsius(context, expected):
    assert context.result == expected

@given('the temperature is {value:d} degrees Celsius')
def step_given_celsius(context, value):
    context.input_temp = value

@when('I convert it to Fahrenheit')
def step_when_to_fahrenheit(context):
    context.result = celsius_to_fahrenheit(context.input_temp)

@then('the result should be {expected:d} degrees Fahrenheit')
def step_then_fahrenheit(context, expected):
    assert context.result == expected

"""
behave --format plain
USING RUNNER: behave.runner:Runner
Feature: Temperature Conversion

  Scenario: Convert Fahrenheit to Celsius
    Given the temperature is 32 degrees Fahrenheit ... passed in 0.003s
    When I convert it to Celsius ... passed in 0.001s
    Then the result should be 0 degrees Celsius ... passed in 0.001s

  Scenario: Convert Celsius to Fahrenheit
    Given the temperature is 100 degrees Celsius ... passed in 0.000s
    When I convert it to Fahrenheit ... passed in 0.001s
    Then the result should be 212 degrees Fahrenheit ... passed in 0.001s

1 feature passed, 0 failed, 0 skipped
2 scenarios passed, 0 failed, 0 skipped
6 steps passed, 0 failed, 0 skipped
Took 0min 0.007s
"""