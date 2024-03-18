class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class Heap:
    def __init__(self):
        self.heap = []

    @staticmethod
    def left_child(index):
        return 2 * index + 1

    @staticmethod
    def right_child(index):
        return 2 * index + 2

    @staticmethod
    def parent(index):
        return (index - 1) // 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def up_heapify(self):
        index = len(self.heap) - 1
        while index > 0:
            parent = self.parent(index)
            if self.heap[index].priority > self.heap[parent].priority:
                self.swap(index, parent)
                index = parent
            else:
                break

    def down_heapify(self):
        index = 0
        while index < len(self.heap):
            left = self.left_child(index)
            right = self.right_child(index)
            largest = index
            if left < len(self.heap) and self.heap[left].priority > self.heap[largest].priority:
                largest = left
            if right < len(self.heap) and self.heap[right].priority > self.heap[largest].priority:
                largest = right
            if largest != index:
                self.swap(index, largest)
                index = largest
            else:
                break

    def insert(self, value, priority):
        new_node = Node(value, priority)
        self.heap.append(new_node)
        self.up_heapify()

    def delete(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.down_heapify()
        return root

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

