import pytest
from order import Order
from payment_gateway import PaymentGateway

pytestmark = pytest.mark.integration

def test_successful_payment_flow(mocker):
    # 1. Setup: Create order and a mock gateway
    my_order = Order({"Laptop": 1, "Mouse": 1})  # Total: 20
    mock_gateway = mocker.Mock(spec=PaymentGateway)

    # Define behavior: Payment succeeds
    mock_gateway.execute_payment.return_value = True

    # 2. Act
    my_order.make_payment(mock_gateway)

    # 3. Assert
    # Check if gateway was called with the correct calculated amount (20)
    mock_gateway.execute_payment.assert_called_once_with(20)
    # Check if status updated
    assert my_order.status == "paid"


def test_failed_payment_flow(mocker):
    # 1. Setup
    my_order = Order({"Banana": 3})  # Total: 30
    mock_gateway = mocker.Mock(spec=PaymentGateway)

    # Define behavior: Payment fails
    mock_gateway.execute_payment.return_value = False

    # 2. Act
    my_order.make_payment(mock_gateway)

    # 3. Assert
    mock_gateway.execute_payment.assert_called_once_with(30)
    assert my_order.status == "error"