from Algorithm.traversal_of_binary_tree import binary_tree_constructor

# python函数传递参数奇怪的地方 如果是int str之类的 是不可变参数 list dict是可变参数
# 但是一个对象居然也是不可变 为了使之成为可变参数的 就需要将它放到一个list中 用来传递值


def convert(root):
    last_node_in_list = [None]
    convert_node(root, last_node_in_list)
    list_head = last_node_in_list[0]
    while list_head and list_head.left:
        list_head = list_head.left

    return list_head


def convert_node(tree_node, last_node_in_list):
    if not tree_node:
        return
    cur = tree_node

    if cur.left is not None:
        convert_node(cur.left, last_node_in_list)

    cur.left = last_node_in_list[0]
    if last_node_in_list[0] is not None:
        last_node_in_list[0].right = cur

    last_node_in_list[0] = cur

    if cur.right is not None:
        convert_node(cur.right, last_node_in_list)


root = binary_tree_constructor([10, 6, 4, 8, 14, 12, 16], [4, 6, 8, 10, 12, 14, 16])
h = convert(root)

while h:
    print(h.val)
    h = h.right
