import unittest

import pytest

from merge_sort import merge_sort

pytestmark = pytest.mark.unit
class TestMergeSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element(self):
        self.assertEqual(merge_sort([10]), [10])

    def test_sorting_reverse(self):
        data = [10, 8, 6, 4, 2, 0]
        self.assertEqual(merge_sort(data), [0, 2, 4, 6, 8, 10])

    def test_duplicates(self):
        self.assertEqual(merge_sort([3, 1, 3, 2]), [1, 2, 3, 3])

    def test_negative_numbers(self):
        self.assertEqual(merge_sort([0, -5, 2, -1]), [-5, -1, 0, 2])

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            merge_sort([1, "string"])

    def test_large_numbers(self):
        big = 10 ** 15
        self.assertEqual(merge_sort([big, -big, 0]), [-big, 0, big])

if __name__ == '__main__':
    unittest.main()

"""
Test results:
tests/unit/test_merge_sort.py::TestMergeSort::test_duplicates PASSED
tests/unit/test_merge_sort.py::TestMergeSort::test_empty_list PASSED
tests/unit/test_merge_sort.py::TestMergeSort::test_invalid_types PASSED
tests/unit/test_merge_sort.py::TestMergeSort::test_large_numbers PASSED
tests/unit/test_merge_sort.py::TestMergeSort::test_negative_numbers PASSED
tests/unit/test_merge_sort.py::TestMergeSort::test_single_element PASSED
tests/unit/test_merge_sort.py::TestMergeSort::test_sorting_reverse PASSED
"""