def cut_the_rope(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    times_of_3 = int(length / 3)
    if length - times_of_3 * 3 == 1:
        times_of_3 -= 1

    times_of_2 = int(length - times_of_3 * 3) / 2
    count = int(3 ** times_of_3) * int(2 ** times_of_2)
    return count


print(cut_the_rope(20))
