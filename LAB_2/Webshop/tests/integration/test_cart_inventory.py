import pytest
from inventory import Inventory, InventoryItem
from shopping_cart import ShoppingCart

pytestmark = pytest.mark.integration
@pytest.fixture
def store_setup():
    """Sets up a fresh inventory and an empty cart."""
    inv = Inventory()
    cart = ShoppingCart()

    # Add an item with limited stock (5 units)
    bread = InventoryItem(id=101, name="Sourdough", price=5.0, amount_in_stock=5)
    inv.add_to_stock(bread)

    return inv, cart, bread


def test_cannot_add_more_than_stock(store_setup):
    """Integration Test: Ensures cart respects inventory limits."""
    inventory, cart, bread = store_setup

    # 1. Try to add 10 units (but only 5 are in stock)
    result = cart.add_inventory_item(bread, 10, inventory)

    # 2. Assertions
    assert result is False, "Should not be able to add items exceeding stock"
    assert len(cart.items) == 0, "Cart should remain empty if stock check fails"


def test_can_add_available_stock(store_setup):
    """Integration Test: Ensures cart allows adding items within stock limits."""
    inventory, cart, bread = store_setup

    # 1. Add 3 units (within the 5 available)
    result = cart.add_inventory_item(bread, 3, inventory)

    # 2. Assertions
    assert result is True
    assert cart.items[101].amount_in_cart == 3