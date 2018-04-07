matrix = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]


def find(m, row, col, x):
    if row <= 0 or col <= 0 or len(m) == 0:
        return False

    r = 0
    c = col - 1
    while r < row and c >= 0:
        if m[r][c] == x:
            return True
        elif m[r][c] > x:
            c -= 1
        else:
            r += 1
    return False


print(find(matrix, 4, 4, 4))
