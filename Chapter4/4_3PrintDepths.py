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


sorted_array = [0, 1, 2, 3, 4, 5, 6, 7]
root_node = create_tree(sorted_array, 0, len(sorted_array) - 1)
list_depths = list()
create_list_depths(list_depths, root_node, 0)

for list in list_depths:
    string = ''
    for element in list:
        string += str(element) + ','

    print(string)
