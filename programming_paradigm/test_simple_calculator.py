import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(5, 3), 8)
    
    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-5, -3), -8)
    
    def test_add_mixed_numbers(self):
        self.assertEqual(self.calc.add(5, -3), 2)
    
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
    
    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)
    
    def test_subtract_mixed_numbers(self):
        self.assertEqual(self.calc.subtract(5, -3), 8)
    
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(6, 7), 42)
    
    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-6, 7), -42)
    
    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(6, 0), 0)
    
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    
    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
    
    def test_divide_fraction_result(self):
        self.assertEqual(self.calc.divide(5, 2), 2.5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
