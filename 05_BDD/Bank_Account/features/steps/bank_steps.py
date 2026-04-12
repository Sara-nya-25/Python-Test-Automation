from behave import given, when, then
from src.bank import BankAccount, BankSystem

@given('I create a new account for "{name}"')
def step_impl_create(context, name):
    context.accounts[name] = BankAccount(name)
    context.active_account = context.accounts[name]

@given('an account for "{name}" with {amount:g}')
def step_impl_existing(context, name, amount):
    acc = BankAccount(name)
    acc.deposit(float(amount))
    context.accounts[name] = acc
    context.active_account = acc

@when('I deposit {amount:g} into the account')
def step_impl_deposit(context, amount):
    context.active_account.deposit(float(amount))

@when('I withdraw {amount:g} from the account')
def step_impl_withdraw(context, amount):
    context.active_account.withdraw(float(amount))

@when('I apply {rate:g}% interest')
def step_impl_interest(context, rate):
    context.active_account.apply_interest(float(rate))

@when('"{sender}" transfers {amount:g} to "{receiver}"')
def step_impl_transfer(context, sender, receiver, amount):
    BankSystem.transfer(context.accounts[sender], context.accounts[receiver], float(amount))

@then('the balance should be {expected:g}')
def step_impl_balance(context, expected):
    # Using float comparison
    assert abs(context.active_account.balance - float(expected)) < 0.01

@then('"{name}" should have {expected:g}')
def step_impl_specific_balance(context, name, expected):
    assert abs(context.accounts[name].balance - float(expected)) < 0.01