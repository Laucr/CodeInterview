class ComplexListNode:
    def __init__(self, val, p_next, p_sibling):
        self.val = val
        self.p_next = p_next
        self.p_sibling = p_sibling


def clone(p_head):
    clone_node(p_head)
    connect_sibling(p_head)
    return reconnect_node(p_head)


def clone_node(p_head):
    node = p_head
    while node:
        cloned = ComplexListNode(node.val, node.p_next, None)
        node.p_next = cloned
        node = cloned.p_next


def connect_sibling(p_head):
    node = p_head
    while node:
        cloned = node.p_next
        if node.p_sibling:
            cloned.p_sibling = node.p_sibling.p_next
        node = cloned.p_next


def reconnect_node(p_head):
    node = p_head
    cloned_head = None
    cloned = None

    if node:
        cloned_head, cloned = node.p_next, node.p_next
        node.p_next = cloned.p_next
        node = node.p_next

    while node:
        cloned.p_next = node.p_next
        cloned = cloned.p_next
        node.p_next = cloned.p_next
        node = node.p_next

    return cloned_head
