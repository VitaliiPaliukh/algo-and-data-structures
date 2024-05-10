from src.routing_internet import *
import unittest


class TestRoutingInternet(unittest.TestCase):
    def test_normal_case(self):
        read_data("../resource/input_route.csv", "../resource/output_route.txt")
        file = open("../resource/output_route.txt")
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 1720)

    def test_undirected_graph(self):
        read_data("../resource/input_undirected.csv", "../resource/output_undirected_route.txt")
        file = open("../resource/output_undirected_route.txt")
        result = int(file.readline())
        file.close()
        self.assertEqual(result, -1)
