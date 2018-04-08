def count_bit_1(n):
    count = 0
    while n > 0:
        count += 1
        n = (n - 1) & n
    return count


print(count_bit_1(15))
