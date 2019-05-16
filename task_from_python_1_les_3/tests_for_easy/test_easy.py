import unittest
from task_from_python_1_les_3.easy import *


class TestEasy(unittest.TestCase):

    def test_get_max(self):
        self.assertEqual(get_max(10, 10, 100), 100, 'тест не пройден')


    def test_max_str(self):
        self.assertEqual(max_str('aa', 'bbb'), 'bbb')


if __name__ == '__main__':
    unittest.main()
