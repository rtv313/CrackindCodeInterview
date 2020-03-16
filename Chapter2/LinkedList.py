class Node():
    def __init__(self):
        self.data = None
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def add_node(self,data):

        if self.head == None:
            self.head = Node()
            self.head.data = data
            return self.head
        else:
            runner = self.head
            while runner != None:

                if runner.next == None:
                    runner.next = Node()
                    runner.next.data = data
                    return runner.next
                else:
                    runner = runner.next

    def print_list(self):
        runner = self.head
        string = ''

        while runner != None:
            string += str(runner.data)
            runner = runner.next
        print(string)