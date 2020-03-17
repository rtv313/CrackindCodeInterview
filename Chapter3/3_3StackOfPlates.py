
class StackOfPlates():

    def __init__(self,size):
        self.stacks_list = list()
        self.stacks_list.append(list())
        self.size = size

    def push(self,data):

        if len(self.stacks_list) == 0:
            self.stacks_list.append(list())

        if len(self.stacks_list[0]) < self.size:
            self.stacks_list[0].insert(0,data)
        else:
            self.stacks_list.insert(0,list())
            self.stacks_list[0].insert(0,data)

    def peek(self):
        if len(self.stacks_list) == 0:
            return None

        value = self.stacks_list[0][0]
        return value

    def pop(self):

        if len(self.stacks_list) == 0:
            return None

        value = self.stacks_list[0].pop(0)

        if len(self.stacks_list[0]) <= 0:
            self.stacks_list.pop(0)

        return value

    def print_stacks(self):

        for stack in self.stacks_list:
            string = ''
            for element in stack:
                string += str(element)+','
            print(string)



stack_plates = StackOfPlates(5)

stack_plates.push(1)
stack_plates.push(2)
stack_plates.push(3)
stack_plates.push(4)
stack_plates.push(5)

stack_plates.push(1)
stack_plates.push(2)
stack_plates.push(3)
stack_plates.push(4)
stack_plates.push(5)

stack_plates.push(1)
stack_plates.push(2)
stack_plates.push(3)
stack_plates.push(4)
stack_plates.push(5)

stack_plates.print_stacks()
print('#####')
print('Peek:'+str(stack_plates.peek()))
print('Pop:'+str(stack_plates.pop()))
stack_plates.print_stacks()

print('#####')
print('Peek:'+str(stack_plates.peek()))
print('Pop:'+str(stack_plates.pop()))
stack_plates.print_stacks()

print('#####')
print('Peek:'+str(stack_plates.peek()))
print('Pop:'+str(stack_plates.pop()))
stack_plates.print_stacks()

print('#####')
print('Peek:'+str(stack_plates.peek()))
print('Pop:'+str(stack_plates.pop()))
stack_plates.print_stacks()

print('#####')
print('Peek:'+str(stack_plates.peek()))
print('Pop:'+str(stack_plates.pop()))
stack_plates.print_stacks()

print('#####')
print('Peek:'+str(stack_plates.peek()))
print('Pop:'+str(stack_plates.pop()))
stack_plates.print_stacks()