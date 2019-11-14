import unittest
from znajdz_blad1 import compute_the_lowest_value


class TestFindMistake1(unittest.TestCase):

    def test_first_sample(self):
        numbers = [4, 2, 0, 5, 11, 9, 2]
        self.assertEqual(compute_the_lowest_value(numbers), 0)

    def test_second_sample(self):
        numbers = [-5, 3, 2, -1, 9]
        self.assertEqual(compute_the_lowest_value(numbers), -5)

    def test_third_sample(self):
        numbers = [1, 6, -2, 8, 10, -3]
        self.assertEqual(compute_the_lowest_value(numbers), -3)


if __name__ == '__main__':
    unittest.main()
