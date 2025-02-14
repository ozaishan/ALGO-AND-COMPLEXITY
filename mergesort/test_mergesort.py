import unittest
from mergesort import MERGESORT 

class TestSorts(unittest.TestCase):

    def test_quick_sort(self):
        arr = [90, 81, 77, 56, 54, 40, 3, 20, 1]
        expected = [1, 3, 20, 40, 54, 56, 77, 81, 90]
        MERGESORT(arr, 0, len(arr) - 1)
        self.assertListEqual(arr, expected)

if __name__ == '__main__':
    unittest.main()
