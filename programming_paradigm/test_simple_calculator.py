import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class, ensuring all arithmetic
    methods behave as expected across various inputs, including edge cases.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each individual test method is run.
        This ensures each test starts with a fresh instance.
        """
        self.calc = SimpleCalculator()

    # --- REQUIRED TEST METHODS ---

    def test_addition(self):
        """Test the addition method with various combinations."""
        # Standard positive integers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Mixed positive/negative
        self.assertEqual(self.calc.add(-10, 5), -5)
        # Floating point numbers
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0)
        # Zeros
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test the subtraction method with various combinations."""
        # Standard positive result
        self.assertEqual(self.calc.subtract(10, 5), 5)
        # Negative result
        self.assertEqual(self.calc.subtract(5, 10), -5)
        # Subtracting a negative number
        self.assertEqual(self.calc.subtract(5, -5), 10)
        # Subtracting zero
        self.assertEqual(self.calc.subtract(100, 0), 100)

    def test_multiplication(self):
        """Test the multiplication method with various combinations and zero."""
        # Positive result
        self.assertEqual(self.calc.multiply(3, 4), 12)
        # Negative result
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        # Multiplication by zero (critical edge case)
        self.assertEqual(self.calc.multiply(100, 0), 0)
        # Floating point multiplication
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0)

    def test_division(self):
        """Test the division method, including the division by zero edge case."""
        # Standard division (integer result)
        self.assertEqual(self.calc.divide(10, 5), 2)
        # Division resulting in a float
        self.assertAlmostEqual(self.calc.divide(10, 4), 2.5)
        # Division with negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5)
        
        # Test the crucial edge case: division by zero must return None
        self.assertIsNone(self.calc.divide(10, 0))
        # Test case where both are zero (still returns None as per implementation)
        self.assertIsNone(self.calc.divide(0, 0))