import unittest
from task_1 import my_func


class Test1(unittest.TestCase):
    def test_in(self):
        self.assertIn(1, [1, 2, 3])

    def test_equals(self):
        self.assertEqual(my_func(1, 2, 3), 5)

    def test_not_equals(self):
        self.assertNotEqual(my_func(1, 2, 3), 5)


if __name__ == '__main__':
    unittest.main()
