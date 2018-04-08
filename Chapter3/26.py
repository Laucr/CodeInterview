class BinaryTreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def compare_two_tree(root1, root2):
    if not root1 or not root2:
        if root1 == root2:
            return True
        else:
            return False

    if root1.val == root2.val:
        if compare_two_tree(root1.left, root2.left) and compare_two_tree(root1.right, root2.right):
            return True
        else:
            return False
    else:
        return False


c = BinaryTreeNode('c', None, None)
b = BinaryTreeNode('b', c, None)
a = BinaryTreeNode('a', b, None)

b_ = BinaryTreeNode('b', None, None)
c_ = BinaryTreeNode('c', None, None)
a_ = BinaryTreeNode('a', b_, c_)

print(compare_two_tree(a_, b_))


def is_subtree(root1, root2):
    res = False
    if not root1 and not root2:
        if root1.val == root2.val:
            res = tree1_contains_tree2(root1, root2)
        if not res:
            res = is_subtree(root1.left, root2)
        if not res:
            res = is_subtree(root1.right, root2)

    return res


def tree1_contains_tree2(root1, root2):
    if not root2:
        return True
    if not root1:
        return False

    if root1.val != root2.val:
        return False

    return tree1_contains_tree2(root1.left, root2.left and tree1_contains_tree2(root1.right, root2.right))
