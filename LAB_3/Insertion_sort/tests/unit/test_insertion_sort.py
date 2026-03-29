import unittest

import pytest

from Insertion_sort import insertion_sort

pytestmark = pytest.mark.unit
class TestInsertionSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(insertion_sort([]), [])

    def test_single_element(self):
        self.assertEqual(insertion_sort([10]), [10])

    def test_reverse_sorted(self):
        data = [10, 8, 6, 4, 2, 0]
        self.assertEqual(insertion_sort(data), [0, 2, 4, 6, 8, 10])

    def test_already_sorted(self):
        self.assertEqual(insertion_sort([1, 2, 3]), [1, 2, 3])

    def test_duplicates(self):
        """Checks if the algorithm handles duplicate values correctly."""
        self.assertEqual(insertion_sort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3])

    def test_negative_numbers(self):
        """Checks handling of negative integers."""
        self.assertEqual(insertion_sort([0, -5, 2, -1]), [-5, -1, 0, 2])

    def test_floats(self):
        """Checks handling of floating point numbers."""
        self.assertEqual(insertion_sort([1.5, 0.2, 1.1]), [0.2, 1.1, 1.5])

    def test_large_numbers(self):
        """Boundary test with very large integers."""
        large = 10 ** 18
        self.assertEqual(insertion_sort([large, 1, large - 1]), [1, large - 1, large])

    def test_invalid_input(self):
        """Negative scenario: passing something non-iterable."""
        with self.assertRaises(TypeError):
            insertion_sort(None)

    def test_mixed_types_throws_error(self):
        """Negative Scenario: Mixed numbers and strings should raise TypeError."""
        with self.assertRaises(TypeError):
            insertion_sort([10, "20", 30])

if __name__ == '__main__':
    unittest.main()

"""
Test results:
tests/unit/test_insertion_sort.py::TestInsertionSort::test_already_sorted PASSED
tests/unit/test_insertion_sort.py::TestInsertionSort::test_duplicates PASSED
tests/unit/test_insertion_sort.py::TestInsertionSort::test_empty_list PASSED
tests/unit/test_insertion_sort.py::TestInsertionSort::test_floats PASSED
tests/unit/test_insertion_sort.py::TestInsertionSort::test_invalid_input PASSED
tests/unit/test_insertion_sort.py::TestInsertionSort::test_large_numbers PASSED
tests/unit/test_insertion_sort.py::TestInsertionSort::test_mixed_types_throws_error PASSED
tests/unit/test_insertion_sort.py::TestInsertionSort::test_negative_numbers PASSED
tests/unit/test_insertion_sort.py::TestInsertionSort::test_reverse_sorted PASSED
tests/unit/test_insertion_sort.py::TestInsertionSort::test_single_element PASSED
"""