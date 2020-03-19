from Helper import Node,create_tree

def collect_nodes(root_node,nodes_set):

    if root_node == None:
        return
    nodes_set.add(root_node.data)
    collect_nodes(root_node.left_son,nodes_set)
    collect_nodes(root_node.right_son,nodes_set)
    return

def get_min(root_node):
    nodes_set = set()
    collect_nodes(root_node,nodes_set)
    return min(list(nodes_set))

def get_max(root_node):
    nodes_set = set()
    collect_nodes(root_node, nodes_set)
    return max(list(nodes_set))

def check_bst(root_node):

    if root_node == None:
        return True

    left_value = None
    if root_node.left_son != None:
        left_value = get_max(root_node.left_son)

    right_value = None
    if root_node.right_son != None:
        right_value = get_min(root_node.right_son)

    value_general = False



    if left_value <= root_node.data and root_node.data <= right_value:
        value_general = True
        if check_bst(root_node.left_son) and check_bst(root_node.right_son) and value_general:
            return True
        else:
            return False

    return value_general

sorted_array = [0,1,2,3,4,5,6,7]
root_node = create_tree(sorted_array,0,len(sorted_array)-1)

print(check_bst(root_node))

