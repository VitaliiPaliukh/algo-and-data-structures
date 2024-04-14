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

    def test_same_color(self):
        read_input("../resource/input_same_color.txt", "../resource/output_same_color.txt")
        file = open("../resource/output_same_color.txt")
        table = []
        for row in file:
            row = row.replace("[", "").replace("]", "").replace("\n", "").replace("'", "")
            row = list(row.split(", "))
            table.append(row)
        file.close()
        self.assertEqual(table, [['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
                                        ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
                                        ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
                                        ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
                                        ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
                                        ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
                                        ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
                                        ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
                                        ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
                                        ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']])


if __name__ == '__main__':
    unittest.main()