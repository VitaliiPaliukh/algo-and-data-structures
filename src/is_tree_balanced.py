class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_height(node: BinaryTree) -> int:
    if node is None:
        return 0

    left_tree_height = get_height(node.left)
    right_tree_height = get_height(node.right)

    if abs(left_tree_height - right_tree_height) > 1 or left_tree_height == -1 or right_tree_height == -1:
        return -1

    return 1 + max(left_tree_height, right_tree_height)


def is_tree_balanced(node: BinaryTree) -> bool:
    if node is None:
        return True

    left_tree_height = get_height(node.left)
    right_tree_height = get_height(node.right)

    if left_tree_height == -1 or right_tree_height == -1:
        return False

    return abs(left_tree_height - right_tree_height) <= 1
