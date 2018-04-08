def quick_sort(s):
    if len(s) <= 1:
        return s
    _quick_sort(s, 0, len(s) - 1)


def _quick_sort(s, low, high):
    if low < high:
        pivot_pos = partition(s, low, high)
        _quick_sort(s, low, pivot_pos - 1)
        _quick_sort(s, pivot_pos + 1, high)


def partition(s, i, j):
    pivot = s[i]
    while i < j:
        while i < j and s[j] > pivot:
            j -= 1
        if i < j:
            s[i] = s[j]
            i += 1
        while i < j and s[i] < pivot:
            i += 1
        if i < j:
            s[j] = s[i]
            j -= 1
    s[i] = pivot
    return i


a = [5, 3, 9, 8, 4, 7, 1]
quick_sort(a)
print(a)
