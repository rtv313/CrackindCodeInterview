import sys
sys.path.append('../Chapter4/')
from Helper import Node,create_tree

def map_tree_levels(root_node,levels_list,depth):

    if root_node is None:
        return

    if len(levels_list) <= depth:
        levels_list.append(list())

    levels_list[depth].append(root_node.data)
    map_tree_levels(root_node.left_son,levels_list,depth + 1)
    map_tree_levels(root_node.right_son, levels_list, depth + 1)

def call_map_tree_levels(root_node):

    levels_list = list()
    map_tree_levels(root_node,levels_list,0)
    return levels_list

def zig_zag(root_node):

    list_for_zig_zag = call_map_tree_levels(root_node)

    counter = 0
    for list in list_for_zig_zag:
        if counter % 2 == 0:
            print(list)
        else:
            print(list[::-1])
        counter += 1

sorted_array = [0, 1, 2, 3, 4, 5, 6, 7]
root_node = create_tree(sorted_array, 0, len(sorted_array) - 1)
zig_zag(root_node)