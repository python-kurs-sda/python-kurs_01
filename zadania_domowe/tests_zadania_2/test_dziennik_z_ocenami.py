import unittest
from zadania_domowe.zadania_2.dziennik_z_ocenami import *


class TestClassRegister(unittest.TestCase):

    def test_get_max_rate(self):
        item = {'Ola': 5.0, 'Jola': 2.0}
        max_item = get_max_rate(item)
        self.assertEqual(max_item, 5.0)

    def test_get_all_rate(self):
        item = {'Ola': 5.0, 'Jola': 2.0}
        list_items = get_all_rate(item)
        self.assertEqual(list_items, [5.0, 2.0])

    def test_get_rate_equla_2(self):
        item = {'Ola': 5.0, 'Jola': 2.0}
        sum_items = get_rate_equal_2(item)
        self.assertEqual(sum_items, 1)

    def test_get_name_with_best_rate(self):
        item = {'Ola': 5.0, 'Jola': 2.0}
        name = get_name_with_best_rate(item)
        self.assertEqual(name, 'Ola')


if __name__ == '__main__':
    unittest.main()