def more_than_half(nums, length):
    res = nums[0]
    times = 1
    for i in range(1, length):
        if times == 0:
            res = nums[i]
            times = 1
        elif nums[i] == res:
            times += 1
        else:
            times -= 1

    if check_if_more_than_half(nums, res):
        return res
    else:
        return 0


def check_if_more_than_half(nums, num):
    times = 0
    for n in nums:
        if n == num:
            times += 1
    if times * 2 > len(nums):
        return True
    else:
        return False


n = [1, 2, 3, 2, 2, 2, 5, 4, 2]
r = more_than_half(n, len(n))
print(r)
