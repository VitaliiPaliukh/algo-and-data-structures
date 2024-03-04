import unittest
from src.lab2 import min_long


class TestMinLong(unittest.TestCase):

    def test_increasing_sequence(self):
        n, w, h = 10, 2, 3
        result = min_long(n, w, h)
        self.assertEqual(result, 9)

    def test_decreasing_sequence(self):
        n, w, h = 4, 1, 1
        result = min_long(n, w, h)
        self.assertEqual(result, 2)

    def test_non_monotone_sequence(self):
        n, w, h = 2, 100000, 99999
        result = min_long(n, w , h)
        self.assertEqual(result, 199998)


if __name__ == "__main__":
    unittest.main()
