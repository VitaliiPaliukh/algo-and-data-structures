import unittest
from src.is_tree_balanced import *


class TestIsTreeBalanced(unittest.TestCase):

    def test_balanced_tree(self):
        """
        #    10
        #    / \
        #   5   20
        #  / \
        # 8   1
        """

        root = BinaryTree(10)
        root.left = BinaryTree(5)
        root.right = BinaryTree(20)
        root.left.left = BinaryTree(1)
        root.left.right = BinaryTree(8)
        self.assertTrue(is_tree_balanced(root))

    def test_unbalanced_tree(self):
        """
                10
              /   \
             5    20
            / \
           3   8
          /     \
         1       9
        """

        root = BinaryTree(10)
        root.left = BinaryTree(5)
        root.right = BinaryTree(20)
        root.left.left = BinaryTree(3)
        root.left.right = BinaryTree(8)
        root.left.left.left = BinaryTree(1)
        root.left.right.right = BinaryTree(9)
        self.assertFalse(is_tree_balanced(root))

    def test_empty_tree(self):
        self.assertTrue(is_tree_balanced(None))
        
