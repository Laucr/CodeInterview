from Algorithm.traversal_of_binary_tree import binary_tree_constructor


def find_path(root, sum):
    if not root:
        return None

    current_sum = 0
    path = []
    _find_path(root, sum, path, current_sum)


def _find_path(root, sum, path, current_sum):
    current_sum += root.val
    path.append(root.val)
    is_leaf = not root.left and not root.right
    if current_sum == sum and is_leaf:
        print(path)

    if root.left:
        _find_path(root.left, sum, path, current_sum)
    if root.right:
        _find_path(root.right, sum, path, current_sum)

    path.pop()


root = binary_tree_constructor([10, 5, 4, 7, 12], [4, 5, 7, 10, 12])

find_path(root, 22)
