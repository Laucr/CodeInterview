from Algorithm.traversal_of_binary_tree import pre_order, in_order


class BinaryTreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_constructor(pre_order, in_order):
    if pre_order is None or in_order is None:
        return None
    return construct_core(pre_order, in_order)


def construct_core(pre_order, in_order):
    root = BinaryTreeNode(pre_order[0], None, None)
    if len(pre_order) == 1:
        return root
    root_index = 0
    for i in range(len(in_order)):
        if in_order[i] == root.val:
            root_index = i
            break
    if root_index == 0:
        root.left = None
        root.right = construct_core(pre_order[root_index + 1:], in_order[root_index + 1:])

    elif root_index < len(in_order) - 1:
        root.left = construct_core(pre_order[1:root_index + 1], in_order[:root_index])
        root.right = construct_core(pre_order[root_index + 1:], in_order[root_index + 1:])

    else:
        root.left = construct_core(pre_order[1:], in_order[root_index + 1:])
        root.right = None

    return root


pre_ = [10, 6, 4, 5, 8, 14, 12, 13, 16]
in_ = [4, 5, 6, 8, 10, 12, 13, 14, 16]
r = binary_tree_constructor(pre_, in_)
print(pre_order(r))
print(in_order(r))
