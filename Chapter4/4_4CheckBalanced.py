from Helper import Node,create_tree

# Create balanced tree
sorted_array = [0,1,2,3,4,5,6,7]
root_node_balanced = create_tree(sorted_array,0,len(sorted_array)-1)

# Create unbalanced tree
root_node_unbalanced = Node(2)
left_root_son = root_node_unbalanced.left_son = Node(0)
right_root_son = root_node_unbalanced.left_son = Node(1)
right_root_son.left_son = Node(0)
right_root_son.right_son = Node(1).right_son = Node(0)


def get_height(root_node,depth):

    if root_node == None:
        return depth

    left_height = get_height(root_node.left_son,depth + 1)
    right_height = get_height(root_node.right_son, depth + 1)

    return max(left_height,right_height)

def balanced(root_node,height):

    if root_node == None:
        return True

    result_height = abs(get_height(root_node.left_son,height) - get_height(root_node.right_son,height))

    if result_height > 1:
        return False
    else:
        return balanced(root_node.left_son,height + 1) and balanced(root_node.right_son,height + 1)


print(balanced(root_node_balanced,0))
print(balanced(root_node_unbalanced,0))