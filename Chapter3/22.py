class ListNode:
    def __init__(self, val, right):
        self.val = val
        self.right = right


def k_th_to_tail(head, k):
    if not head or k == 0:
        return None
    a_ptr = head
    for i in range(k):
        if not a_ptr.right:
            a_ptr = a_ptr.right
        else:
            return None

    b_ptr = head
    while not a_ptr.right:
        a_ptr = a_ptr.right
        b_ptr = b_ptr.right

    return b_ptr
