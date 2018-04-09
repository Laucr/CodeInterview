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
    pivot = root
    stack, t = [], []

    while pivot is not None or len(stack) != 0:
        t.append(pivot.val)
        stack.append(pivot)
        pivot = pivot.left
        while pivot is None and len(stack) != 0:
            pivot = stack.pop()
            pivot = pivot.right

    return t


def in_order(root):
    pivot = root
    stack, t = [], []

    while pivot is not None or len(stack) != 0:
        if pivot.left is not None:
            stack.append(pivot)
            pivot = pivot.left
        else:
            t.append(pivot.val)
            pivot = pivot.right
            while pivot is None and len(stack) != 0:
                pivot = stack.pop()
                t.append(pivot.val)
                pivot = pivot.right

    return t


def post_order(root):
    stack, t = [root], []
    cur, pre = None, None
    while len(stack) != 0:
        cur = stack[-1]
        if (cur.left is None and cur.right is None) or \
           (pre is not None and (cur.left == pre or cur.right == pre)):
            t.append(cur.val)
            stack.pop()
            pre = cur
        else:
            if cur.right is not None:
                stack.append(cur.right)
            if cur.left is not None:
                stack.append(cur.left)

    return t


def binary_tree_constructor(_pre_order, _in_order):
    if _pre_order is None or _in_order is None:
        return None
    return construct_core(_pre_order, _in_order)


def construct_core(_pre_order, _in_order):
    root = BinaryTreeNode(_pre_order[0], None, None)
    if len(_pre_order) == 1:
        return root
    root_index = 0
    for i in range(len(_in_order)):
        if _in_order[i] == root.val:
            root_index = i
            break
    if root_index == 0:
        root.left = None
        root.right = construct_core(_pre_order[root_index + 1:], _in_order[root_index + 1:])

    elif root_index < len(_in_order) - 1:
        root.left = construct_core(_pre_order[1:root_index + 1], _in_order[:root_index])
        root.right = construct_core(_pre_order[root_index + 1:], _in_order[root_index + 1:])

    else:
        root.left = construct_core(_pre_order[1:], _in_order[root_index + 1:])
        root.right = None

    return root
