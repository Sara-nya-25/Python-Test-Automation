from behave import given, when, then
from src.inventory import Stock, StockItem

@given('the inventory is empty')
def step_impl_empty(context):
    context.stock = Stock()

@when('I add "{name}" with quantity of {quantity:d}')
def step_impl_add_product(context, name, quantity):
    new_item = StockItem(name, quantity)
    context.stock.add_product(new_item)

@given('the inventory contains "{name}" with a quantity of {amount:d}')
def step_impl_existing(context, name, amount):
    context.stock = Stock()
    item = StockItem(name, amount)
    context.stock.add_product(item)

@when('I reduce the quantity of "{name}" by {amount:d}')
def step_impl_reduce(context, name, amount):
    context.stock.reduce_quantity(name, amount)

@then('the inventory should contain {expected:d} of "{name}"')
def step_impl_check(context, expected, name):
    actual_quantity = context.stock.get_quantity(name)
    assert actual_quantity == expected, f"Expected {expected}, but got {actual_quantity}"

"""
USING RUNNER: behave.runner:Runner
Feature: Inventory Management # features/inventory.feature:1

    Then the inventory should contain 50 of "Apples" # features/steps/inventory_steps.py:23 0.005s
    Then the inventory should contain 50 of "Apples" # features/steps/inventory_steps.py:23
    Then the inventory should contain 15 of "Apples"            # features/steps/inventory_steps.py:23 0.002s
    Then the inventory should contain 15 of "Apples"            # features/steps/inventory_steps.py:23
1 feature passed, 0 failed, 0 skipped
2 scenarios passed, 0 failed, 0 skipped
6 steps passed, 0 failed, 0 skipped
Took 0min 0.019s
"""