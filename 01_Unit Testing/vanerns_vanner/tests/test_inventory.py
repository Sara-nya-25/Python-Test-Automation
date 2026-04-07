import unittest
from src.inventory import Inventory, Item

class TestInventory(unittest.TestCase):
    def test_set_and_get_amount(self):
        inv = Inventory()
        inv.set_item("Compass", 10, 5)
        self.assertEqual(inv.get_amount_left("Compass"), 5)

    def test_rent_reduces_amount(self):
        inv = Inventory()
        inv.set_item("Tent", 50, 2)
        inv.rent("Tent")
        self.assertEqual(inv.get_amount_left("Tent"), 1)

if __name__ == '__main__':
    unittest.main()
