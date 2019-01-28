

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def in_order_str(tree):
    if tree is None:
        return ""
    return str(in_order_str(tree.left)) + str(tree.value) + str(in_order_str(tree.right))


def num_tree_nodes(tree):
    if tree is None:
        return 0
    return num_tree_nodes(tree.left) + 1 + num_tree_nodes(tree.right)


def create_n_spaces(n):
    return "".join([" " for i in range(n - 1)])


def pretty_print_tree(tree):
    def calculate_element_location(tree_node, current_spaces, depth=0):
        def calculate_directional_element_location(tree, last_index, direction_symbol):
            if tree is not None:
                next_index = in_order_tree.index(tree.value)
                if depth + 1 not in rows_to_elements:
                    rows_to_elements[depth + 1] = []
                rows_to_elements[depth + 1] += [(direction_symbol, current_spaces + (next_index - last_index))]
                calculate_element_location(tree, current_spaces + (next_index - last_index) * 2, depth + 2)

        if tree_node is not None:
            if depth not in rows_to_elements:
                rows_to_elements[depth] = []
            rows_to_elements[depth] += [(tree_node.value, current_spaces)]
            cur_in_order_index = in_order_tree.index(tree_node.value)
            calculate_directional_element_location(tree_node.left, cur_in_order_index, left_slash)
            calculate_directional_element_location(tree_node.right, cur_in_order_index, right_slash)

    left_slash = "/"
    right_slash = "\\"
    in_order_tree = in_order_str(tree)
    rows_to_elements = {}
    calculate_element_location(tree, num_tree_nodes(tree))

    for idx, elements_in_row in rows_to_elements.items():
        row = ""
        current_element_space = 0
        for element, element_index in elements_in_row:
            spaces_to_fill = element_index - current_element_space
            row += create_n_spaces(spaces_to_fill)
            row += element
            current_element_space = element_index
        print(row)


if __name__ == '__main__':
    k = TreeNode("k")
    g = TreeNode("g", k)
    d = TreeNode("d", right=g)
    z = TreeNode("z")
    b = TreeNode("b", d, z)
    h = TreeNode("h")
    e = TreeNode("e", right=h)
    i = TreeNode("i")
    j = TreeNode("j")
    f = TreeNode("f", i, j)
    c = TreeNode("c", e, f)
    tree_node1 = TreeNode("a", b, c)
    l = TreeNode("l")
    m = TreeNode("m", l)
    n = TreeNode("n", right=m)
    z1 = TreeNode("1")
    o = TreeNode("o", n, z1)
    p = TreeNode("p")
    q = TreeNode("q", right=p)
    r = TreeNode("r")
    s = TreeNode("s")
    t = TreeNode("t", r, s)
    u = TreeNode("u", q, t)
    tree_node2 = TreeNode("v", o, u)
    tree_node = TreeNode("w", tree_node1, tree_node2)
    pretty_print_tree(tree_node)
