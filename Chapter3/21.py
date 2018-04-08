def reorder(s, f):
    if len(s) == 0:
        return
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and f(s[i]):
            i += 1
        while i < j and not f(s[j]):
            j -= 1

        if i < j:
            s[i], s[j] = s[j], s[i]


a = [1, 2, 3, 4, 5]


def odd(x):
    if x & 0x1 == 1:
        return True
    return False


reorder(a, odd)
print(a)
