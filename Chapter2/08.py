class BinaryTreeNode:

    def __init__(self, val, left, right, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def get_next(node):
    # case 3

    the_next = None
    if node is None:
        return the_next
    # case 1
    # right != None, left most in right subtree
    if node.right is not None:
        ptr = node.right
        while ptr.left is not None:
            ptr = ptr.left
        the_next = ptr

    # right == None
    else:
        if node.parent is not None:
            cur = node
            parent = node.parent
            # if cur isn't left node of father node, search back while the node is the left son
            while parent is not None and cur == parent.right:
                cur = parent
                parent = parent.parent
            # if cur is left node of father node, ret father node
            the_next = parent
    return the_next


i = BinaryTreeNode('i', None, None)
h = BinaryTreeNode('h', None, None)
g = BinaryTreeNode('g', None, None)
f = BinaryTreeNode('f', None, None)
e = BinaryTreeNode('e', h, i)
d = BinaryTreeNode('d', None, None)
c = BinaryTreeNode('c', f, g)
b = BinaryTreeNode('b', d, e)
a = BinaryTreeNode('a', b, c)

b.parent = a
c.parent = a
d.parent = b
e.parent = b
f.parent = c
g.parent = c
h.parent = e
i.parent = e

n = get_next(h)
if n is not None:
    print(n.val)
else:
    print(n)
