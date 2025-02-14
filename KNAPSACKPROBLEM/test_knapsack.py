from bruteforcemethod01 import brute_force_01_knapsack  
from bruteforcemethod01 import brute_force_fractional_knapsack  
from dynamic01 import knapsack_01
from greedymethod import fractional_knapsack
import unittest

class TestKnapsack(unittest.TestCase):
    def test_01_brute_case1(self):
        p = [20, 30, 40, 50]
        w = [5, 10, 15, 20]
        m = 25
        input = brute_force_01_knapsack(p, w, m)
        output = 70  
        self.assertEqual(input, output)
        
    def test_frac_brute_case1(self):
        p = [20, 30, 40, 50]
        w = [5, 10, 15, 20]
        m = 25
        input = brute_force_fractional_knapsack(p, w, m)
        output = 76.66666666666666
        self.assertEqual(input, output)

    def test_frac_greedy_case1(self):
        p = [100, 60, 120]
        w = [20, 10, 30]
        m = 50
        input = fractional_knapsack(p, w, m)
        output = 240.0  # Expected maximum profit
        self.assertEqual(input, output)

    def test_01_dynamic_case1(self):
        p = [15, 25, 35, 45]
        w = [5, 10, 20, 30]
        m = 50
        input = knapsack_01(p, w, m)
        output = 85 
        self.assertEqual(input, output)

    def test_01_dynamic_case2(self):
        p = [10, 40, 50, 70]
        w = [1, 3, 4, 5]
        m = 7
        input = knapsack_01(p, w, m)
        output = 90 
        self.assertEqual(input, output)

if __name__ == '__main__':
    unittest.main()
