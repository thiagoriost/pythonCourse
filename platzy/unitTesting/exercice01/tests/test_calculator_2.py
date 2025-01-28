import unittest
from calculator import mul, div

class CalculatorTests(unittest.TestCase):
    
    def test_mul(self):
        assert mul(2,3) == 6
        
    def test_div(self):
        assert div(10, 5) == 2
        