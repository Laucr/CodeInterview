def has_path_core(m, r, c, path, index, visited):
    if index == len(path):
        return True
    ret = False
    if 0 <= r < len(m) and 0 <= c < len(m[0]) and m[r][c] == path[index] and not visited[r][c]:
        index += 1
        visited[r][c] = True
        ret = \
            has_path_core(m, r, c - 1, path, index, visited) or \
            has_path_core(m, r - 1, c, path, index, visited) or \
            has_path_core(m, r, c + 1, path, index, visited) or \
            has_path_core(m, r + 1, c, path, index, visited)
        if not ret:
            index -= 1
            visited[r][c] = False

    return ret


def has_path(m, path):
    row = len(m)
    col = len(m[0])
    if m is None or row < 1 or col < 1 or len(path) == 0:
        return False
    # caution: shallow copies
    visited = [([False] * col) for i in range(row)]
    index = 0
    for r in range(row):
        for c in range(col):
            if has_path_core(m, r, c, path, index, visited):
                return True
    del visited
    return False


matrix = [['a', 'b', 't', 'g'], ['c', 'f', 'c', 's'], ['j', 'd', 'e', 'h']]
p = 'bfce'
print(has_path(matrix, p))
