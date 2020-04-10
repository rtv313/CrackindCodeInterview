from Helper import Node, create_tree


def collect_nodes(root_node, nodes_set):
    if root_node == None:
        return
    nodes_set.add(root_node.data)
    collect_nodes(root_node.left_son, nodes_set)
    collect_nodes(root_node.right_son, nodes_set)
    return


def get_min(root_node):
    nodes_set = set()
    collect_nodes(root_node, nodes_set)
    return min(list(nodes_set))


def get_max(root_node):
    nodes_set = set()
    collect_nodes(root_node, nodes_set)
    return max(list(nodes_set))


def check_bst(root_node):
    if root_node.left_son == None and root_node.right_son == None:
        return True

    if root_node.left_son == None and root_node.right_son != None and root_node.data <= get_min(root_node.right_son):
        return True and check_bst(root_node.right_son)

    if root_node.left_son != None and root_node.right_son == None and root_node.data >= get_max(root_node.left_son):
        return True and check_bst(root_node.left_son)

    max_value_left = get_max(root_node.left_son)
    min_value_right = get_min(root_node.right_son)

    if max_value_left <= root_node.data and root_node.data <= min_value_right:
        return True and check_bst(root_node.left_son) and check_bst(root_node.right_son)

    return False


sorted_array = [0, 1, 2, 3, 4, 5, 6, 7]
root_node = create_tree(sorted_array, 0, len(sorted_array) - 1)
sorted_array2 = [0, 1, 8, 3, 4, 5, 6, 7]
root_node2 = create_tree(sorted_array2, 0, len(sorted_array2) - 1)
print(check_bst(root_node))
print(check_bst(root_node2))
