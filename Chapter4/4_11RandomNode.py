class Node:
    def __init__(self, data):
        self.data = data
        self.left_son = None
        self.right_son = None


class BST:

    def __init__(self):
        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = Node(data)
            return

        runner = self.root

        while runner is not None:

            if data <= runner.data:
                if runner.left_son is None:
                    runner.left_son = Node(data)
                    break
                runner = runner.left_son
            else:
                if runner.right_son is None:
                    runner.right_son = Node(data)
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

    def delete(self):
        pass

    def get_random_node(self):
        pass


tree = BST()
# 3,5,1,6,4,2,0,

list_nodes = [3, 5, 1, 6, 4, 2, 0]

for data in list_nodes:
    if data == 5:
        tree.insert(data)
    else:
        tree.insert(data)


node = tree.find(9)

print('Hola')
