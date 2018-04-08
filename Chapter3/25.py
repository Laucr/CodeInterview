class ListNode:
    def __init__(self, val, right):
        self.val = val
        self.right = right


def merge(head1, head2):
    if not head1:
        return head2
    elif not head2:
        return head1

    if head1.val < head2.val:
        merged_head = head1
        merge(head1.right, head2)
    else:
        merged_head = head2
        merge(head1, head2.right)

    return merged_head
