import pytest
from logger import Logger
from bank_account import BankAccount
from transaction import Transaction

# Mark the whole file
pytestmark = pytest.mark.integration
@pytest.fixture
def bank_setup(mocker):
    logger = Logger()
    # Create a spy on the log method
    spy_log = mocker.spy(logger, 'log')

    acc1 = BankAccount("Alice", 1000, logger)
    acc2 = BankAccount("Bob", 500, logger)

    return acc1, acc2, spy_log


def test_deposit_logging(bank_setup):
    acc1, _, spy_log = bank_setup
    acc1.deposit(200)

    # Verify the specific string was sent to the logger
    spy_log.assert_called_with("deposit: 200 kr, balance 1200 kr")


def test_withdraw_insufficient_funds_logging(bank_setup):
    acc1, _, spy_log = bank_setup
    acc1.withdraw(2000)  # More than balance

    spy_log.assert_called_with("withdraw: could not withdraw 2000 kr from account")


def test_transfer_integration_logging(bank_setup):
    acc1, acc2, spy_log = bank_setup

    # Act
    Transaction.transfer(300, acc1, acc2)

    # Assert: Transfer calls withdraw(acc1) then deposit(acc2)
    # We check that the logger was called twice with the correct sequence
    assert spy_log.call_count == 2

    # Check the first call (Withdraw)
    assert spy_log.call_args_list[0].args[0] == "withdraw: 300 kr, balance 700 kr"

    # Check the second call (Deposit)
    assert spy_log.call_args_list[1].args[0] == "deposit: 300 kr, balance 800 kr"


def test_failed_transfer_integration(bank_setup):
    """Ensures no money moves and error is logged if funds are low."""
    alice, bob, spy_log= bank_setup

    # Action: Try to transfer more than Alice has
    success = Transaction.transfer(5000, alice, bob)

    assert success is False
    assert alice.balance == 1000  # Unchanged
    assert bob.balance == 500  # Unchanged

    # Check that the failure message was sent to logger
    spy_log.assert_called_with("withdraw: could not withdraw 5000 kr from account")

"""
tests\\integration\\test_bank_transactions.py ...                                                                                                                              [100%]

===================================================================================== PASSES ======================================================================================
______________________________________________________________________________ test_deposit_logging _______________________________________________________________________________
------------------------------------------------------------------------------ Captured stdout call -------------------------------------------------------------------------------
deposit: 200 kr, balance 1200 kr
____________________________________________________________________ test_withdraw_insufficient_funds_logging _____________________________________________________________________
------------------------------------------------------------------------------ Captured stdout call -------------------------------------------------------------------------------
withdraw: could not withdraw 2000 kr from account
________________________________________________________________________ test_transfer_integration_logging ________________________________________________________________________
------------------------------------------------------------------------------ Captured stdout call -------------------------------------------------------------------------------
withdraw: 300 kr, balance 700 kr
deposit: 300 kr, balance 800 kr
============================================================================= short test summary info =============================================================================
PASSED tests/integration/test_bank_transactions.py::test_deposit_logging
PASSED tests/integration/test_bank_transactions.py::test_withdraw_insufficient_funds_logging
PASSED tests/integration/test_bank_transactions.py::test_transfer_integration_logging
================================================================================ 3 passed in 0.04s =========
"""