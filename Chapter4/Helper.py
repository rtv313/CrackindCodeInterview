class Node:
    def __init__(self,data):
        self.data=data
        self.left_son = None
        self.right_son = None


def create_tree(sorted_array,min_index,max_index):

    if max_index < min_index:
        return None

    center_index = (min_index + max_index) // 2
    data = sorted_array[center_index]
    new_node = Node(data)

    new_node.left_son = create_tree(sorted_array,min_index,center_index - 1)
    new_node.right_son = create_tree(sorted_array,center_index + 1,max_index)

    return new_node