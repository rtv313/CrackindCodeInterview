import random

class Node:

    def __init__(self, data,parent):
        self.data = data
        self.left_son = None
        self.right_son = None
        self.parent = parent


class BST:

    def __init__(self):
        self.root = None
        self.nodes_dict = dict()

    def insert(self, data):

        if self.root is None:
            self.root = Node(data,None)
            self.nodes_dict[self.root.__hash__()] = self.root
            return

        runner = self.root

        while runner is not None:

            if data <= runner.data:
                if runner.left_son is None:
                    runner.left_son = Node(data,runner)
                    self.nodes_dict[runner.left_son.__hash__()] = runner.left_son
                    break
                runner = runner.left_son
            else:
                if runner.right_son is None:
                    runner.right_son = Node(data,runner)
                    self.nodes_dict[runner.right_son .__hash__()] = runner.right_son
                    break
                runner = runner.right_son

        return

    def find(self, data):

        if self.root.data == data:
            return self.root

        runner = self.root

        while runner is not None:

            if runner.data == data:
                return runner

            if data < runner.data:
                runner = runner.left_son

            if data > runner.data:
                runner = runner.right_son

        return None

    def get_min(self,node):

        runner = node

        while runner is not None:

            if runner.left_son is None and runner.right_son is None:
                return runner

            if runner.left_son is not None:
                runner = runner.left_son
            if runner.right_son is not None:
                runner = runner.right_son

        return runner

    def delete(self,data):

        node_to_delete = self.find(data)

        if node_to_delete is None:
            return

        # Node to delete has no children
        if node_to_delete.left_son is None and node_to_delete.right_son is None:

            parent = node_to_delete.parent

            if parent.left_son == node_to_delete:
                parent.left_son = None
            else:
                parent.right_son = None

            del self.nodes_dict[node_to_delete.__hash__()]

        # Node has only one child and is right son
        if node_to_delete.left_son is None and node_to_delete.right_son is not None:

            parent = node_to_delete.parent

            if parent.left_son == node_to_delete:
                parent.left_son = node_to_delete.right_son
            else:
                parent.right_son = node_to_delete.right_son

            del self.nodes_dict[node_to_delete.__hash__()]

        # Node has only one child and is left son
        if node_to_delete.left_son is not None and node_to_delete.right_son is None:

            parent = node_to_delete.parent

            if parent.left_son == node_to_delete:
                parent.left_son = node_to_delete.left_son
            else:
                parent.right_son = node_to_delete.left_son

            del self.nodes_dict[node_to_delete.__hash__()]

        # Node to delete has two children i need to find the min in the right son and replace
        if node_to_delete.left_son is not None and node_to_delete.right_son is not None:

            min = self.get_min(node_to_delete.right_son)
            node_to_delete.data = min.data

            parent = min.parent
            if parent.left_son == min:
                parent.left_son = None
            else:
                parent.right_son = None

            del self.nodes_dict[min.__hash__()]

    def get_random_node(self):
        selected_node = random.choice(list(self.nodes_dict.keys()))
        node_selected = self.nodes_dict[selected_node]
        return node_selected


def serialize(root,list_path):

    if root is None:
        list_path.append('x')
        return

    list_path.append(root.data)
    serialize(root.left_son,list_path)
    serialize(root.right_son,list_path)


def deserialize(serialize_list,index):

    if serialize_list[index] == 'x':
        return None,index

    root = Node(serialize_list[index],None)
    root.left_son,actual_index = deserialize(serialize_list,index + 1)
    root.right_son,actual_index = deserialize(serialize_list,actual_index + 1)
    return root,actual_index


tree = BST()
# 3,5,1,6,4,2,0
list_nodes = [3, 5, 1, 6, 4, 2, 0]

for data in list_nodes:
    tree.insert(data)

list_serialize = list()
serialize(tree.root,list_serialize)
root = deserialize(list_serialize,0)[0]

