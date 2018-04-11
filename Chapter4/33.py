def is_post_order_traversal(s):
    if len(s) == 0:
        return False
    root = s[-1]
    i = 0
    while i < len(s) - 1:
        if s[i] > root:
            break
        i += 1
    j = i
    while j < len(s) - 1:
        if s[j] < root:
            return False
        j += 1
    left = True
    if i > 0:
        left = is_post_order_traversal(s[:i])
    right = True
    if i < len(s) - 1:
        right = is_post_order_traversal(s[i:len(s) - 1])

    return left and right

t = [5, 7, 6, 9, 11, 10, 8]
print(is_post_order_traversal(t))
