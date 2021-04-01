import unittest
from task_4 import my_func


class Test1(unittest.TestCase):
    def test_in(self):
        self.assertIn(2, [2, -2])

    def test_equals(self):
        self.assertEqual(my_func(2, -2), 0.25)

    def test_not_equals(self):
        self.assertNotEqual(my_func(2, -2), 4)

    def test_isnone(self):
        self.assertIsNotNone(my_func(2, -2))


if __name__ == '__main__':
    unittest.main()
