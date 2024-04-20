from src.career import *
import unittest


class TestCareer(unittest.TestCase):
    def test_default(self):
        read_input("../resource/career_input.txt", "../resource/career_output.txt")
        file = open("../resource/career_output.txt")
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 12)

    def test_empty_file(self):
        read_input("../resource/empty_career_input.txt", "../resource/empty_career_output.txt")
        file = open("../resource/empty_career_output.txt")
        result = int(file.readline())
        file.close()
        self.assertEqual(result, -1)

    def test_all_zero(self):
        read_input("../resource/input_zero.txt", "../resource/output_zero.txt")
        file = open("../resource/output_zero.txt")
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 0)
