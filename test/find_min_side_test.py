import unittest
from src.find_min_side import find_min_side


class TestMinLong(unittest.TestCase):

    def test_increasing_sequence(self):
        n, w, h = 10, 2, 3
        result = find_min_side(n, w, h)
        self.assertEqual(result, 9)

    def test_decreasing_sequence(self):
        n, w, h = 4, 1, 1
        result = find_min_side(n, w, h)
        self.assertEqual(result, 2)

    def test_non_monotone_sequence(self):
        n, w, h = 2, 100000, 99999
        result = find_min_side(n, w, h)
        self.assertEqual(result, 199998)


if __name__ == "__main__":
    unittest.main()
