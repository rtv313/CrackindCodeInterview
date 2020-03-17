
class StackWithArray:

    def __init__(self):
        self.stack = list()
        self.size = 5

        for x in range(self.size):
            self.stack.append(0)

        self.index_position = self.size - 1

    def push(self,new_element):
        if self.index_position >= 0:
            self.stack[self.index_position] = new_element
            self.index_position -= 1
        else:
            print('StackFull')

    def peek(self):
        if self.index_position < 0:
            return self.stack[0]
        return self.stack[self.index_position]

    def pop(self):
        if self.index_position >= self.size:
            print('Stack Empty')
            self.index_position = self.size - 1
            return None

        if self.index_position < 0:
            value = self.stack[0]
            self.index_position = 1
            return value
        else:
            value = self.stack[self.index_position]
            self.index_position += 1
            print('StackEmpty')
            return value


    def print(self):
        for x in range(self.size):
            print(str(self.stack[x]))


stackArray = StackWithArray()
stackArray.push(5)
stackArray.push(4)
stackArray.push(3)
stackArray.push(2)
stackArray.push(1)
stackArray.push(1)

print('Peek: '+ str(stackArray.peek()))
print('Pop: '+ str(stackArray.pop()))
print('Pop: '+ str(stackArray.pop()))
print('Pop: '+ str(stackArray.pop()))
print('Pop: '+ str(stackArray.pop()))
print('Pop: '+ str(stackArray.pop()))
print('Pop: '+ str(stackArray.pop()))

stackArray.push(5)
stackArray.push(4)
stackArray.push(3)
stackArray.push(2)
stackArray.push(1)
stackArray.push(1)
