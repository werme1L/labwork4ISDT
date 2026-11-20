import unittest
from calculator import add, subtract, multiply, divide
print(add(2, 3))
print(add.__code__.co_filename)

class CalculatorTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_add_negative(self):
        self.assertEqual(add(-5, -3), -8)

    def test_add_zero(self):
        self.assertEqual(add(10, 0), 10)

    def test_multiply_zero(self):
        self.assertEqual(multiply(10, 0), 0)

    def test_subtract_negative(self):
        self.assertEqual(subtract(5, -3), 8)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
