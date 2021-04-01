import unittest
from task_5 import my_func


class Test1(unittest.TestCase):


    def test_equals(self):
        self.assertEqual(my_func(4, 2), 8)

    def test_not_equals(self):
        self.assertNotEqual(my_func(4, 2), 2)


if __name__ == '__main__':
    unittest.main()
