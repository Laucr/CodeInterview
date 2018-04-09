from Algorithm.traversal_of_binary_tree import binary_tree_constructor, in_order


class BinaryTreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def mirror(root):
    if not root:
        return
    if not root.left and not root.right:
        return

    root.left, root.right = root.right, root.left

    if root.left:
        mirror(root.left)
    if root.right:
        mirror(root.right)


root = binary_tree_constructor([8, 6, 5, 7, 10, 9, 11], [5, 6, 7, 8, 9, 10, 11])
mirror(root)
t = in_order(root)

print(t)
