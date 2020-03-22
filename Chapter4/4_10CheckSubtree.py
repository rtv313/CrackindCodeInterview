from Helper import Node, create_tree

def pre_order_traversal(list,root):

    if root is not None:
        list.append(root.data)
        pre_order_traversal(list,root.left_son)
        pre_order_traversal(list,root.right_son)
    else:
        list.append('x')

def check_is_sub_tree(root_one,root_two):

    tree_one_preorder = list()
    pre_order_traversal(tree_one_preorder,root_one)

    tree_two_preorder = list()
    pre_order_traversal(tree_two_preorder, root_two)

    for x in range(tree_one_preorder.count('x')):
        tree_one_preorder.remove('x')

    for x in range(tree_two_preorder.count('x')):
        tree_two_preorder.remove('x')

    str_tree_one = ''.join(str(e) for e in tree_one_preorder)
    str_tree_two = ''.join(str(e) for e in tree_two_preorder)

    if str_tree_two in str_tree_one:
        print('T2 is a Subtree from T1')
        return True
    else:
        print('T2 is NOT a Subtree from T1')
        return False


# T2 is subtree
list_nodes_t1 = [1,2,3,4,5,6,7]
list_nodes_t2 = [5,6,7]
root_tree_one = create_tree(list_nodes_t1, 0, len(list_nodes_t1) - 1)
root_tree_two = create_tree(list_nodes_t2, 0, len(list_nodes_t2) - 1)
check_is_sub_tree(root_tree_one,root_tree_two)


# T2 is not subtree
list_nodes_t1 = [1,2,3,4,5,6,7]
list_nodes_t2 = [5,6,7,8]
root_tree_one = create_tree(list_nodes_t1, 0, len(list_nodes_t1) - 1)
root_tree_two = create_tree(list_nodes_t2, 0, len(list_nodes_t2) - 1)
check_is_sub_tree(root_tree_one,root_tree_two)

