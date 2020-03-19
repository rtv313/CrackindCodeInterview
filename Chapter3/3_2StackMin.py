class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.min = None


class StackMin:

    def __init__(self):
        self.head = None
        self.min = None

    def add_node(self, data):

        if self.head == None:
            self.head = Node(data)
            self.min = self.head

        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

            if new_node.data < self.min.data:
                temp = self.min
                self.min = new_node
                self.min.min = temp

    def peek(self):
        return self.head.data

    def pop(self):
        value = self.head.data

        if self.head == self.min:
            self.min = self.head.min

        self.head = self.head.next
        return value

    def print_stack(self):
        runner = self.head

        while runner != None:
            print(str(runner.data))
            runner = runner.next

    def min_node(self):
        return self.min.data


stackMin = StackMin()
stackMin.add_node(5)
stackMin.add_node(4)
stackMin.add_node(3)
stackMin.add_node(2)
stackMin.add_node(1)
stackMin.print_stack()

print('Min:' + str(stackMin.min_node()))
stackMin2 = StackMin()
stackMin2.add_node(5)
stackMin2.add_node(4)
stackMin2.add_node(3)
stackMin2.add_node(2)
stackMin2.add_node(1)
stackMin2.print_stack()

print('#######################')
stackMin2.pop()
stackMin2.print_stack()
print('Min:' + str(stackMin2.min_node()))
stackMin2.pop()
stackMin2.print_stack()
print('Min:' + str(stackMin2.min_node()))

print('#######################')
stackMin3 = StackMin()
stackMin3.add_node(1)
stackMin3.add_node(2)
stackMin3.add_node(3)
stackMin3.add_node(4)
stackMin3.add_node(5)
stackMin3.print_stack()
print('Min:' + str(stackMin3.min_node()))
stackMin3.pop()
stackMin3.print_stack()
print('Min:' + str(stackMin3.min_node()))
