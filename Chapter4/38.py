def permutation(chars):
    t = []
    if not chars:
        return t
    _permutation(chars, 0, t)
    return t


def _permutation(chars, index, t):
    if index == len(chars) - 1:
        t.append(''.join(chars))
    else:
        for i in range(index, len(chars)):
            chars[i], chars[index] = chars[index], chars[i]
            _permutation(chars, index + 1, t)
            chars[i], chars[index] = chars[index], chars[i]


t = permutation(['a', 'b', 'c'])
print(t)
