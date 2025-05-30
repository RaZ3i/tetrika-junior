import unittest

from task_1.solution import sum_two, sum_two_bool, sum_three_float


class DecoratorTest(unittest.TestCase):

    def test_sum_two_good(self):
        self.assertEqual(sum_two(1, 2), 3)

    def test_sum_two_bad(self):
        self.assertEqual(sum_two(1, True), "TypeError")

    def test_sum_two_bool_good(self):
        self.assertEqual(sum_two_bool(True, True), 2)

    def test_sum_two_bool_bad(self):
        self.assertEqual(sum_two_bool(True, "str_data"), "TypeError")

    def test_sum_three_float_good(self):
        self.assertEqual(sum_three_float(1.0, 4.5, 10.5), 16.0)

    def test_sum_three_float_bad(self):
        self.assertEqual(sum_three_float(1.0, 4.5, 3), "TypeError")


if __name__ == "__main__":
    unittest.main()
