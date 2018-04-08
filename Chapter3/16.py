def power_unsigned_exp(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    res = power_unsigned_exp(base, exponent >> 1)
    res *= res
    if exponent & 0x1 == 1:
        res *= base
    return res


def power(base, exponent):
    if base == 0 and exponent < 0:
        return 0
    abs_exp = int(exponent)
    if exponent < 0:
        abs_exp = int(-exponent)
    res = power_unsigned_exp(base, abs_exp)
    if exponent < 0:
        res = 1.0 / res
    return res


print(power(100, -1))
