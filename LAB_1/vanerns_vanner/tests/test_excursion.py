import unittest
from src.excursion import Excursion

class TestExcursion(unittest.TestCase):
    def test_add_and_remove_member(self):
        exc = Excursion()
        exc.add_member("Alice")
        exc.add_member("Bob")
        exc.remove_member("Alice")
        self.assertEqual(exc.get_members(), ["Bob"])

    def test_rent_and_return_flow(self):
        exc = Excursion()
        exc.add_member("Alice")
        exc.register_item_rented("Alice", "Backpack")

        # Should be in the "not returned" list
        self.assertIn("Alice", exc.get_all_who_has_not_returned_items())

        # After return, list should be empty
        exc.register_item_returned("Alice", "Backpack")
        self.assertEqual(exc.get_all_who_has_not_returned_items(), [])



if __name__ == '__main__':
    unittest.main()
