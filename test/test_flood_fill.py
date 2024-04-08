from src.flood_fill import *
import unittest


class TestFloodFill(unittest.TestCase):
    def test_positive(self):
        read_input("../resource/input.txt", "../resource/output.txt")
        file = open("../resource/output.txt")
        matrix = []
        for line in file:
            line = line.replace("[", "").replace("]", "").replace("\n", "").replace("'", "")
            line = list(line.split(", "))
            matrix.append(line)
        file.close()
        self.assertEqual(matrix, [['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
                                         ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'G', 'G', 'G'],
                                         ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
                                         ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'G'],
                                         ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'G', 'G', 'G'],
                                         ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'G', 'G', 'G'],
                                         ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'G'],
                                         ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'G', 'G', 'G'],
                                         ['W', 'B', 'B', 'G', 'B', 'B', 'B', 'B', 'G', 'G'],
                                         ['W', 'B', 'B', 'G', 'G', 'G', 'G', 'G', 'G', 'G']])

    def test_empty_file(self):
        read_input("../resource/empty_input.txt", "../resource/empty_output.txt")
        file = open("../resource/empty_output.txt")
        result = int(file.readline())
        file.close()
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
