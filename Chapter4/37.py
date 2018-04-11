from Algorithm.traversal_of_binary_tree import binary_tree_constructor


class BinaryTreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def serialize(root, t):
    if root is None:
        return t.append("Null")
    t.append(root.val)
    if root.left:
        serialize(root.left, t)
    else:
        t.append("Null")
    if root.right:
        serialize(root.right, t)
    else:
        t.append("Null")


def deserialize(s):
    pass


r = binary_tree_constructor([1, 2, 4, 3, 5, 6], [4, 2, 1, 5, 3, 6])
s = [1, 2, 4, 'Null', 'Null', 'Null', 3, 5, 'Null', 'Null', 6, 'Null', 'Null']
t = []
serialize(r, t)
print(t)
