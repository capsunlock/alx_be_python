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

    # --- Test Methods for Addition ---

    def test_add_positive_numbers(self):
        """Test addition with two positive integers."""
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_add_negative_numbers(self):
        """Test addition with two negative integers."""
        self.assertEqual(self.calc.add(-10, -5), -15)

    def test_add_mixed_numbers(self):
        """Test addition with a positive and a negative integer."""
        self.assertEqual(self.calc.add(-10, 5), -5)
        self.assertEqual(self.calc.add(15, -5), 10)

    def test_add_floats(self):
        """Test addition with floating-point numbers."""
        # Using assertAlmostEqual for floats to handle potential precision issues
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0)

    # --- Test Methods for Subtraction ---
    
    def test_subtract_positive_numbers(self):
        """Test subtraction of two positive integers."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_subtract_negative_numbers(self):
        """Test subtraction involving negative results."""
        self.assertEqual(self.calc.subtract(5, -5), 10)
        self.assertEqual(self.calc.subtract(-5, 5), -10)
        self.assertEqual(self.calc.subtract(-5, -5), 0)

    def test_subtract_zero(self):
        """Test subtracting zero."""
        self.assertEqual(self.calc.subtract(100, 0), 100)

    # --- Test Methods for Multiplication ---

    def test_multiply_positive_numbers(self):
        """Test multiplication of two positive integers."""
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_negative_numbers(self):
        """Test multiplication of two negative integers (should be positive)."""
        self.assertEqual(self.calc.multiply(-3, -4), 12)

    def test_multiply_by_zero(self):
        """Test multiplication where one factor is zero (should be zero)."""
        self.assertEqual(self.calc.multiply(99, 0), 0)
        self.assertEqual(self.calc.multiply(0, 99), 0)

    def test_multiply_floats(self):
        """Test multiplication with floats."""
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0)

    # --- Test Methods for Division ---

    def test_divide_normal(self):
        """Test standard division resulting in an integer."""
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_divide_float_result(self):
        """Test division resulting in a float."""
        self.assertAlmostEqual(self.calc.divide(10, 4), 2.5)

    def test_divide_negative_numbers(self):
        """Test division involving negative numbers."""
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_by_zero(self):
        """
        Test the crucial edge case: division by zero.
        The SimpleCalculator implementation explicitly returns None.
        """
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0)) # 0/0 is also handled by the b==0 check