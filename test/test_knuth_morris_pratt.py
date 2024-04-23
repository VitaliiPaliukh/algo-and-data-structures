from src.Knuth_Morris_Pratt import knuth_morris_pratt_search
import unittest


class TestFindPatternInString(unittest.TestCase):
    def test_empty_pattern(self):
        result = knuth_morris_pratt_search("abcdef", "")
        self.assertEqual(result, 0)

    def test_empty_string_and_pattern(self):
        result = knuth_morris_pratt_search("", "")
        self.assertEqual(result, 0)

    def test_long_pattern_found(self):
        result = knuth_morris_pratt_search("abcabcabcabc", "abcabc")
        self.assertEqual(result, 0)

    def test_long_pattern_not_found(self):
        result = knuth_morris_pratt_search("abcabcabcabc", "abcd")
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
