import unittest
from task_3 import Road


class Test1(unittest.TestCase):
    def test_in(self):
        self.assertIn(2, [4, 2])

    def test_in_instance(self):
        self.assertIsInstance(Road(5000, 20), Road)


if __name__ == '__main__':
    unittest.main()
