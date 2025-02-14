import unittest
from linear_search import linear_search

class TestLinearSearch(unittest.TestCase):
    
    def test_element_found(self):
        n = 100
        arr1 = list(range(1, n + 1))
        result1 = linear_search(arr1, n)
        self.assertEqual(result1, n)
    
    def test_element_not_found(self):
        n = 100
        arr2 = list(range(1, n + 1))
        result2 = linear_search(arr2, n+1)
        self.assertEqual(result2, -1)
    
    def test_single_element_found(self):
        arr = [5]
        result = linear_search(arr, 5)
        self.assertEqual(result, 5)
    
    def test_single_element_not_found(self):
        arr = [5]
        result = linear_search(arr, 10)
        self.assertEqual(result, -1)
    
    def test_empty_array(self):
        arr = []
        result = linear_search(arr, 10)
        self.assertEqual(result, -1)
    
    def test_first_element_found(self):
        arr = [10, 20, 30, 40]
        result = linear_search(arr, 10)
        self.assertEqual(result, 10)
    
    def test_last_element_found(self):
        arr = [10, 20, 30, 40]
        result = linear_search(arr, 40)
        self.assertEqual(result, 40)
    

if __name__ == '__main__':
    unittest.main()
