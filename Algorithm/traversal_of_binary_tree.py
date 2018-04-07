class BinaryTreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


"""
        10
     6       14
   4   8  12    16
     5      13

pre  10 6 4 5 8 14 12 13 16
 in  4 5 6 8 10 12 13 14 16
post 5 4 8 6 13 12 16 14 10
lev  10 6 14 4 8 12 16 5 13
"""
_5 = BinaryTreeNode(5, None, None)
_13 = BinaryTreeNode(13, None, None)
_4 = BinaryTreeNode(4, None, _5)
_8 = BinaryTreeNode(8, None, None)
_12 = BinaryTreeNode(12, None, _13)
_16 = BinaryTreeNode(16, None, None)
_6 = BinaryTreeNode(6, _4, _8)
_14 = BinaryTreeNode(14, _12, _16)
_10 = BinaryTreeNode(10, _6, _14)
r = _10


def pre_order_recursively(root, t):
    if root is not None:
        t.append(root.val)
        if root.left is not None:
            pre_order_recursively(root.left, t)
        if root.right is not None:
            pre_order_recursively(root.right, t)
    else:
        return


def in_order_recursively(root, t):
    if root is not None:
        if root.left is not None:
            in_order_recursively(root.left, t)
        t.append(root.val)
        if root.right is not None:
            in_order_recursively(root.right, t)
    else:
        return


def post_order_recursively(root, t):
    if root is not None:
        if root.left is not None:
            post_order_recursively(root.left, t)
        if root.right is not None:
            post_order_recursively(root.right, t)
        t.append(root.val)
    else:
        return


# def level_traversal_recursively(root):
#     pass


def level_traversal(root):
    if root is None:
        return
    queue = [root]
    t = []
    while len(queue) != 0:
        ptr = queue[0]
        queue.pop(0)
        t.append(ptr.val)
        if ptr.left is not None:
            queue.append(ptr.left)
        if ptr.right is not None:
            queue.append(ptr.right)
    return t


def pre_order(root):

    pass


def in_order(root):
    pass


def post_order(root):
    pass
