class ListNode:
    def __init__(self, val, right):
        self.val = val
        self.right = right


def print_list_reversely(head):
    s = []
    while head.right is not None:
        s.append(head.right.val)
        head = head.right
    while s:
        print(s.pop())


def print_list_reversely_recursively(head):
    if head is not None:
        if head.right is not None:
            print_list_reversely(head.right)
        print(head.right.val)


def generate_list(length):
    head = ListNode(None, None)
    ptr = None
    for i in range(length, 0, -1):
        node = ListNode(i, None)
        node.right = ptr
        ptr = node
    head.right = ptr
    return head


h = generate_list(10)
# while h.right is not None:
#     h = h.right
#     print(h.val)

# print_list_reversely(h)
print_list_reversely_recursively(h)
