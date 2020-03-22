from itertools import permutations
from Helper import Node, create_tree


def create_list_depths(list_depths, root_node, depth):
    if root_node == None:
        return

    if len(list_depths) == depth:
        list_depths.append(list())

    if len(list_depths[depth]) == 0:
        list_depths.append(list())
        list_depths[depth].append(root_node.data)
    else:
        list_depths[depth].append(root_node.data)

    create_list_depths(list_depths, root_node.left_son, depth + 1)
    create_list_depths(list_depths, root_node.right_son, depth + 1)


def all_combinations(list_depths, level_index):
    if level_index > (len(list_depths) - 1):
        return None

    level_combinations = list(permutations(list_depths[level_index]))
    level_combinations = [list(ele) for ele in level_combinations]
    result = list()
    next_level_combinations = all_combinations(list_depths, level_index + 1)

    for level in level_combinations:

        if next_level_combinations is None:
            result.append(level)
        else:
            for next_level in next_level_combinations:
                result.append(level + next_level)

    return result


sorted_array = [0, 1, 2, 3, 4, 5, 6]
root_node = create_tree(sorted_array, 0, len(sorted_array) - 1)
list_depths = list()
create_list_depths(list_depths, root_node, 0)
list_depths = list_depths[:-1]
results = all_combinations(list_depths, 0)


for result in results:
    string = ''

    for x in result:
        string += str(x) + ','

    print(string)