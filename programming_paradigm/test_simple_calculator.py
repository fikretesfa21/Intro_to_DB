import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(5, 3), 8)
    
    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-5, -3), -8)
    
    def test_addition_mixed_numbers(self):
        self.assertEqual(self.calc.add(5, -3), 2)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
    
    def test_subtraction_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)
    
    def test_subtraction_mixed_numbers(self):
        self.assertEqual(self.calc.subtract(5, -3), 8)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(6, 7), 42)
    
    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-6, 7), -42)
    
    def test_multiplication_by_zero(self):
        self.assertEqual(self.calc.multiply(6, 0), 0)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    
    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
    
    def test_division_fraction_result(self):
        self.assertEqual(self.calc.divide(5, 2), 2.5)
    
    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
