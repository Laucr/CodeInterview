def print_circle(m, start, r, c, t):
    end_x, end_y = r - 1 - start, c - 1 - start
    for i in range(start, end_x + 1):
        t.append(m[start][i])
    if start < end_y:
        for i in range(start + 1, end_y + 1):
            t.append(m[i][end_y])
    if start < end_x and start < end_y:
        for i in range(end_x - 1, start - 1, -1):
            t.append(m[end_x][i])
    if start < end_x and start < end_y - 1:
        for i in range(end_y, start, -1):
            t.append(m[i][start])

    return t


def print_matrix(m):
    if not m:
        return []
    row, col = len(matrix), len(matrix[0])
    start = 0
    t = []
    while col > start * 2 and row > start * 2:
        print_circle(m, start, row, col, t)
        start += 1
    return t


matrix = [[1, 2, 3], [5, 6, 7], [9, 10, 11], [13, 14, 15]]
# t = []
# print_circle(matrix, 0, len(matrix), len(matrix[0]), t)
# print(t)
"""
 1  2  3
 5  6  7
 9 10 11
13 14 15
"""
out = print_matrix(matrix)


print(out)

