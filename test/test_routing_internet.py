from src.routing_internet import *
import unittest


class TestRoutingInternet(unittest.TestCase):
    def test_file(self):
        read_data("../resource/input_route.csv", "../resource/output_route.txt")
        file = open("../resource/output_route.txt")
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 900)

    def test_undirect_file(self):
        read_data("../resource/input_undirected.csv", "../resource/output_undirected_route.txt")
        file = open("../resource/output_undirected_route.txt")
        result = int(file.readline())
        file.close()
        self.assertEqual(result, -1)