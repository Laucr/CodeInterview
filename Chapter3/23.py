class ListNode:
    def __init__(self, val, right):
        self.val = val
        self.right = right


def meeting_node(head):
    if not head:
        return None

    slow = head.right
    if not slow:
        return None

    fast = slow.right

    while not fast.right and not slow.right:
        if fast == slow:
            return fast
        slow = slow.right
        fast = fast.right
        if not fast.right:
            fast = fast.right

    return None


def entry_node_of_loop(head):
    node_meeting = meeting_node(head)
    if not node_meeting:
        return None

    node_in_loop = 1
    node_1 = node_meeting
    while node_1.right != node_meeting:
        node_1 = node_1.right
        node_in_loop += 1

    node_1 = head
    for i in range(node_in_loop):
        node_1 = node_1.right
    node_2 = head
    while node_1 != node_2:
        node_1 = node_1.right
        node_2 = node_2.right

    return node_1
