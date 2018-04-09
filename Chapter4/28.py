from Algorithm.traversal_of_binary_tree import binary_tree_constructor


class BinaryTreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def is_symmetrical(root):
    return _is_symmetrical(root, root)


def _is_symmetrical(root1, root2):
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    if root1.val != root2.val:
        return False

    return _is_symmetrical(root1.left, root2.right) and _is_symmetrical(root1.right, root2.left)


root = binary_tree_constructor([8, 6, 5, 7, 6, 7, 5], [5, 6, 7, 8, 7, 6, 5])

print(is_symmetrical(root))
