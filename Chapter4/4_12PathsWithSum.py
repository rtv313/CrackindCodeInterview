from Helper import Node, create_tree

def paths_with_sum(root_node,target,list_previous,list_results):

    if root_node is None:
        return

    list_path = list_previous.copy()
    list_path.append(root_node.data)

    sum_result = 0
    for element in list_path:
        sum_result += element

    if sum_result == target:
        list_results.append(list_path)
        return

    paths_with_sum(root_node.left_son,target,list_path,list_results)
    paths_with_sum(root_node.right_son, target, list_path, list_results)

def call_paths_with_sum(root,target):
    list_previous = list()
    list_results = list()
    paths_with_sum(root,target,list_previous,list_results)

    if len(list_results) == 0:
        print('There is no path for ' + str(target))
        return

    for result in list_results:
        print(result)

sorted_array = [0, 1, 2, 3, 4, 5, 6, 7]
root_node_balanced = create_tree(sorted_array, 0, len(sorted_array) - 1)

call_paths_with_sum(root_node_balanced,6)