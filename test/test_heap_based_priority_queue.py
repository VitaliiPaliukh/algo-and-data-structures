import unittest
from src.heap_based_priority_queue import *


class TestHeap(unittest.TestCase):
    def test_insert(self):
        heap = Heap()
        heap.insert('z', 3)
        heap.insert('x', 5)
        heap.insert('c', 2)
        self.assertEqual(heap.peek().value, 'x')
        self.assertEqual(len(heap.heap), 3)

    def test_delete(self):
        heap = Heap()
        heap.insert('z', 3)
        heap.insert('x', 5)
        heap.insert('c', 2)
        deleted = heap.delete()
        self.assertEqual(deleted.value, 'x')
        self.assertEqual(len(heap.heap), 2)
        self.assertEqual(heap.peek().value, 'z')

    def test_peek(self):
        heap = Heap()
        heap.insert('z', 3)
        heap.insert('x', 5)
        heap.insert('c', 2)
        self.assertEqual(heap.peek().value, 'x')
        heap.delete()
        self.assertEqual(heap.peek().value, 'z')

    def test_empty_heap(self):
        heap = Heap()
        self.assertIsNone(heap.peek())
        self.assertIsNone(heap.delete())


if __name__ == '__main__':
    unittest.main()
