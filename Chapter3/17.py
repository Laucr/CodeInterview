def print_numbers_of_n_digits(n):
    if n <= 0:
        return
    nums = ['0' for j in range(n)]
    print(nums)
    t = []
    for i in range(10):
        nums[0] = str(i)
        generate_numbers(nums, n, 0, t)
    return t


def generate_numbers(nums, length, index, t):
    if index == length - 1:
        t.append(''.join(nums).lstrip('0'))
        return

    for i in range(10):
        nums[index + 1] = str(i)
        generate_numbers(nums, length, index + 1, t)


num_list = print_numbers_of_n_digits(2)
for num in num_list[1:]:
    print(num)
