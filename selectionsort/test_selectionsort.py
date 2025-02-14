import unittest
from selectionsort import selection_sort

class TestSorts(unittest.TestCase):
 
    
    def test_selection_sort(self):
        arr = [90,81,77,56,54,40,3,20,1]
        expected= [1,3,20,40,54,56,77,81,90]
        selection_sort(arr)
        self.assertListEqual(arr, expected)

if __name__ == '__main__':
    unittest.main()