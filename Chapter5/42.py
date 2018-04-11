def sum_of_continuous_sub_array(nums):
    sum_ = 0
    maximum = 0
    for i in nums:
        sum_ += i
        if sum_ < 0:
            sum_ = 0
        if sum_ > maximum:
            maximum = sum_
    return maximum


t = [1, -2, 3, 10, -4, 7, 2, -5]
print(sum_of_continuous_sub_array(t))
