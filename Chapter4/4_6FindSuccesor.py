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


def get_min(node):
    runner = node

    while runner is not None:

        if runner.left_son is None and runner.right_son is None:
            return runner

        if runner.left_son is not None:
            runner = runner.left_son
        if runner.right_son is not None:
            runner = runner.right_son

    return runner


def find_successor(node):
    if node.right_son is not None:
        return get_min(node.right_son)

    runner = node

    while runner.parent is not None:

        if runner == runner.parent.left_son:
            return runner.parent
        else:
            runner = runner.parent

    return runner


sorted_array = [0, 1, 2, 3, 4, 5, 6, 7]
root_node = create_tree_with_parent(sorted_array, 0, len(sorted_array) - 1, None)
print(root_node.data)
print(find_successor(root_node).data)

# Node 4 , next 5
node = root_node.right_son.left_son
print(find_successor(node).data)

# Node 2, next 3
node = root_node.left_son.right_son
print(find_successor(node).data)

# Node 7, next null(no succesor)
node = root_node.right_son.right_son.right_son
if find_successor(node).parent is None:
    print('No succesor')
