
class QueueWithStack:

    def __init__(self):
        self.stack_one = list()
        self.stack_two = list()

    def push(self,data):
        self.stack_one.insert(0,data)

    def pop(self):

        while len(self.stack_one) > 0:
            value_stack_one = self.stack_one.pop(0)
            self.stack_two.insert(0,value_stack_one)

        return_value = self.stack_two.pop(0)

        while len(self.stack_two) > 0:
            value_stack_two = self.stack_two.pop(0)
            self.stack_one.insert(0,value_stack_two)

        return return_value


queue_with_stacks = QueueWithStack()
queue_with_stacks.push(1)
queue_with_stacks.push(2)
queue_with_stacks.push(3)
queue_with_stacks.push(4)
queue_with_stacks.push(5)

print(str(queue_with_stacks.pop()))
print(str(queue_with_stacks.pop()))
print(str(queue_with_stacks.pop()))
print(str(queue_with_stacks.pop()))
print(str(queue_with_stacks.pop()))