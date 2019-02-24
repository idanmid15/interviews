

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "TreeNode({}, {}, {})".format(str(self.value), self.left, self.right)


def in_order_str(tree):
    if tree is None:
        return ""
    return str(in_order_str(tree.left)) + str(tree.value) + str(in_order_str(tree.right))


def num_tree_nodes(tree):
    if tree is None:
        return 0
    return num_tree_nodes(tree.left) + 1 + num_tree_nodes(tree.right)


def create_n_spaces(n):
    return "".join([" " for _ in range(n - 1)])


def pretty_print_tree(tree):
    """
    Given a tree node, this function prints the tree in a pretty manner.
    For example:
                        w
                 /            \
          a                         v
        /    \                    /    \
      b         c               o         u
   /   \      /   \          /   \      /   \
d       z   e       f     x       1   q       t
  \          \     / \      \          \     / \
    g         h   i   j       m         p   r   s
   /                         /
  k                         l

    :param tree: the given tree to print out
    """
    def calculate_element_location(tree_node, current_spaces, depth=0):
        def calculate_directional_element_location(root, last_index, direction_symbol):
            if root is not None:
                next_index = in_order_tree.index(root.value)
                if depth + 1 not in rows_to_elements:
                    rows_to_elements[depth + 1] = []
                rows_to_elements[depth + 1] += [(direction_symbol, current_spaces + (next_index - last_index))]
                calculate_element_location(root, current_spaces + (next_index - last_index) * 2, depth + 2)

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


def serialize_tree(tree):
    """
    Given a tree's root, serializes it into a string.
    For example:
    tree = TreeNode("a", TreeNode("b", TreeNode("c")), TreeNode("d"))
    serialize_tree(tree) ====>>> abc***d**  (using pre-order traversal)
    """
    if tree is None:
        return "*"
    return str(tree.value) + serialize_tree(tree.left) + serialize_tree(tree.right)


def deserialize_tree(tree_str):
    """
    Given a string, turns the string into a TreeNode
    For example:
    tree_str = abc***d**
    deserialize_tree(tree_str) ====>>> TreeNode("a", TreeNode("b", TreeNode("c")), TreeNode("d"))
    """

    def inner_helper(idx_dict):
        idx_dict["idx"] += 1
        str_idx = idx_dict["idx"]
        if str_idx == len(tree_str) or tree_str[str_idx] == "*":
            return None
        return TreeNode(tree_str[str_idx], inner_helper(idx_dict), inner_helper(idx_dict))
    return inner_helper({"idx": -1})


def num_unival_trees(root):
    """
    A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
    Given the root to a binary tree, count the number of unival subtrees.
    For example, the following tree has 5 unival subtrees:

       0
      / \
     1   0
        / \
       1   0
      / \
     1   1
    """
    def unival_helper(tree_node):
        """
        returns the number of unival trees and the value of the nodes. If -1 is the value, not all nodes are equal.
        """
        if tree_node.left is None and tree_node.right is None:
            return 1, tree_node.value
        if tree_node.left is None:
            right_tree = unival_helper(tree_node.right)
            if right_tree[1] == tree_node.value:
                return right_tree[0] + 1, right_tree[1]
            else:
                return right_tree[0], -1
        if tree_node.right is None:
            left_tree = unival_helper(tree_node.left)
            if left_tree[1] == tree_node.value:
                return left_tree[0] + 1
            else:
                return left_tree[0], -1
        left_tree = unival_helper(tree_node.left)
        right_tree = unival_helper(tree_node.right)
        if right_tree[1] == tree_node.value and right_tree[1] == left_tree[1]:
            return left_tree[0] + right_tree[0] + 1, tree_node.value
        else:
            return left_tree[0] + right_tree[0], -1
    if root is None:
        return 0
    return unival_helper(root)[0]


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
    l1 = TreeNode("l")
    m = TreeNode("m", l1)
    x = TreeNode("x", right=m)
    z1 = TreeNode("1")
    o = TreeNode("o", x, z1)
    p = TreeNode("p")
    q = TreeNode("q", right=p)
    r = TreeNode("r")
    s = TreeNode("s")
    t = TreeNode("t", r, s)
    u = TreeNode("u", q, t)
    tree_node2 = TreeNode("v", o, u)
    tree_node3 = TreeNode("w", tree_node1, tree_node2)
    pretty_print_tree(tree_node3)
    print(deserialize_tree(serialize_tree(TreeNode("a", TreeNode("b", TreeNode("c")), TreeNode("d")))))
    print(num_unival_trees(TreeNode("0", TreeNode("1"), TreeNode("0", TreeNode("1", TreeNode("1"), TreeNode("1")),
                                                                 TreeNode("0")))))  # 5
