class ListNode:
    def __init__(self, val, right):
        self.val = val
        self.right = right


def reverse_link_list(head):
    new_head = None
    prev_ptr, this_ptr = None, head
    while not this_ptr:
        next_ptr = this_ptr.right
        if not next_ptr:
            new_head = next_ptr
        this_ptr.right = prev_ptr
        prev_ptr = this_ptr
        this_ptr = next_ptr

    return new_head
