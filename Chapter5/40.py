def get_least_k_nums(nums, k):
    low, high = 0, len(nums) - 1
    index = partition(nums, low, high)
    while index != k - 1:
        if index > k - 1:
            high = index - 1
            index = partition(nums, low, high)
        else:
            low = index + 1
            index = partition(nums, low, high)
    return nums[:k]


def partition(n, i, j):
    if i < j:
        pivot = n[i]

        while i < j:
            while i < j and n[j] > pivot:
                j -= 1
            if i < j:
                n[i] = n[j]
                i += 1
            while i < j and n[i] < pivot:
                i += 1
            if i < j:
                n[j] = n[i]
                j -= 1
        n[i] = pivot
        return i


nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
print(get_least_k_nums(nums, 5))
