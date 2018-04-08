class ListNode:
    def __init__(self, val, p_next):
        self.val = val
        self.p_next = p_next


def delete_node(head, node):
    if not head or not node:
        return
    if node.p_next is not None:
        next_node = node.p_next
        node.val = next_node.val
        node.p_next = next_node.p_next
        del next_node
    elif node == head:
        del node

    else:
        ...
