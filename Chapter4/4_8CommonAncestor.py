class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left_son = None
        self.right_son = None
        self.parent = parent


def create_tree_with_parent(sorted_array, min_index, max_index, parent):
    if max_index < min_index:
        return None

    center_index = (min_index + max_index) // 2
    data = sorted_array[center_index]

    new_node = Node(data, parent)
    new_node.left_son = create_tree_with_parent(sorted_array, min_index, center_index - 1, new_node)
    new_node.right_son = create_tree_with_parent(sorted_array, center_index + 1, max_index, new_node)

    return new_node


def get_ancestors_list(node):
    list_ancestors = list()
    runner = node.parent
    while runner is not None:
        list_ancestors.append(runner)
        runner = runner.parent

    return list_ancestors


def find_common_ancestor(node_one, node_two):
    list_ancestors_one = get_ancestors_list(node_one)
    list_ancestors_two = get_ancestors_list(node_two)

    concatenate_lists = list_ancestors_one + list_ancestors_two

    dictionary = dict()

    for node in concatenate_lists:

        if node.__hash__() in dictionary:
            dictionary[node.__hash__()] += 1

            if dictionary[node.__hash__()] == 2:
                return node
        else:
            dictionary[node.__hash__()] = 1

    return None


sorted_array = [0, 1, 2, 3, 4, 5, 6, 7]
root_node = create_tree_with_parent(sorted_array, 0, len(sorted_array) - 1, None)

node_one = root_node.left_son.left_son #0
node_two = root_node.right_son.right_son #6

common_ancestor = find_common_ancestor(node_one,node_two)
print(common_ancestor.data)

