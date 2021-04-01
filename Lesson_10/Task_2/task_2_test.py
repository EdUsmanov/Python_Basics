import unittest
from task_2 import DivisionByZero


class Test1(unittest.TestCase):
    def test_in(self):
        self.assertIn(2, [4, 2])

    def test_equals(self):
        self.assertEqual(DivisionByZero.divide_by_zero(4, 2), 2)

    def test_not_equals(self):
        self.assertNotEqual(DivisionByZero.divide_by_zero(4, 2), 1)

    def test_raises(self):
        self.assertRaises(Exception)


if __name__ == '__main__':
    unittest.main()
