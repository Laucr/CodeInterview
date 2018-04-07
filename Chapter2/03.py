s = [2, 3, 1, 0, 2, 3, 5]


def duplicated_nums(nums):
    for i in nums:
        if i < 0 or i > len(nums) - 1:
            return None
    for i in range(len(nums)):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            m = nums[i]
            nums[i], nums[m] = nums[m], nums[i]
    return None


def duplicated_nums_2(nums):
    dup = []
    for i in nums:
        if i < 0 or i > len(nums) - 1:
            return None
    bucket = [0] * len(nums)
    for i in nums:
        bucket[i] += 1
    for i in range(len(bucket)):
        if bucket[i] > 1:
            dup.append(i)
    return dup


print(duplicated_nums_2(s))
