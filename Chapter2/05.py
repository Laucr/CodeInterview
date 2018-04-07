s_ = "We are happy."


def replace_space(s):
    spaces = 0
    for c in s:
        if c == ' ':
            spaces += 1

    replaced = [' '] * (len(s) + spaces * 2)

    j = len(replaced) - 1
    i = len(s) - 1
    while i >= 0:
        if s[i] != ' ':
            replaced[j] = s[i]
            j -= 1
            i -= 1
        else:
            replaced[j - 2:j + 1] = '%20'
            j -= 3
            i -= 1
    return ''.join(replaced)


print(replace_space(s_))
