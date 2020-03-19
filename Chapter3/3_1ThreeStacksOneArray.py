class StackWithArray:

    def __init__(self):
        self.stack = list()
        self.size = 5

        for x in range(self.size):
            self.stack.append(0)

        self.index_position = self.size - 1

    def push(self, new_element):
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

print('Peek: ' + str(stackArray.peek()))
print('Pop: ' + str(stackArray.pop()))
print('Pop: ' + str(stackArray.pop()))
print('Pop: ' + str(stackArray.pop()))
print('Pop: ' + str(stackArray.pop()))
print('Pop: ' + str(stackArray.pop()))
print('Pop: ' + str(stackArray.pop()))

stackArray.push(5)
stackArray.push(4)
stackArray.push(3)
stackArray.push(2)
stackArray.push(1)
stackArray.push(1)


class ThreeStacksOneArray:

    def __init__(self):
        self.stack = list()
        self.size = 15

        for x in range(self.size):
            self.stack.append(0)

        self.index_position_1 = 4  # stack_1 0-4
        self.index_position_2 = 9  # stack_2 5-9
        self.index_position_3 = 14  # stack 3 10-14

    def push(self, stack_id, new_element):

        if stack_id == 1:

            if self.index_position_1 >= 0:
                self.stack[self.index_position_1] = new_element
                self.index_position_1 -= 1
            else:
                print('Stack 1 Full')

        if stack_id == 2:

            if self.index_position_2 >= 5:
                self.stack[self.index_position_2] = new_element
                self.index_position_2 -= 1
            else:
                print('Stack 2 Full')

        if stack_id == 3:

            if self.index_position_3 >= 10:
                self.stack[self.index_position_3] = new_element
                self.index_position_3 -= 1
            else:
                print('Stack 3 Full')

    def peek(self, stack_id):

        if stack_id == 1:
            if self.index_position_1 < 0:
                return self.stack[0]
            return self.stack[self.index_position_1]

        if stack_id == 2:
            if self.index_position_2 < 5:
                return self.stack[5]
            return self.stack[self.index_position_2]

        if stack_id == 3:
            if self.index_position_3 < 10:
                return self.stack[10]
            return self.stack[self.index_position_3]

    def pop(self, stack_id):

        if stack_id == 1:

            if self.index_position_1 >= 5:
                print('Stack 1 Empty')
                self.index_position_1 = 4
                return None

            if self.index_position_1 < 0:
                value = self.stack[0]
                self.index_position_1 = 1
                return value
            else:
                value = self.stack[self.index_position_1]
                self.index_position_1 += 1
                return value

        if stack_id == 2:

            if self.index_position_2 >= 10:
                print('Stack 2 Empty')
                self.index_position_2 = 9
                return None

            if self.index_position_2 < 5:
                value = self.stack[5]
                self.index_position_2 = 6
                return value
            else:
                value = self.stack[self.index_position_2]
                self.index_position_2 += 1
                return value

        if stack_id == 3:

            if self.index_position_3 >= 15:
                print('Stack 3 Empty')
                self.index_position_3 = 14
                return None

            if self.index_position_3 < 10:
                value = self.stack[10]
                self.index_position_3 = 11
                return value
            else:
                value = self.stack[self.index_position_3]
                self.index_position_3 += 1
                return value

    def print(self):
        for x in range(self.size):
            print(str(self.stack[x]))


print('ThreeStacks')
threeStacks = ThreeStacksOneArray()
threeStacks.push(1, 5)
threeStacks.push(1, 4)
threeStacks.push(1, 3)
threeStacks.push(1, 2)
threeStacks.push(1, 1)
threeStacks.push(1, 1)

threeStacks.push(2, 5)
threeStacks.push(2, 4)
threeStacks.push(2, 3)
threeStacks.push(2, 2)
threeStacks.push(2, 1)
threeStacks.push(2, 1)

threeStacks.push(3, 5)
threeStacks.push(3, 4)
threeStacks.push(3, 3)
threeStacks.push(3, 2)
threeStacks.push(3, 1)
threeStacks.push(3, 1)

print('Stack1:' + str(threeStacks.peek(1)))
print('Stack2:' + str(threeStacks.peek(2)))
print('Stack3:' + str(threeStacks.peek(3)))

threeStacks.pop(1)
threeStacks.pop(1)
threeStacks.pop(1)
threeStacks.pop(1)
threeStacks.pop(1)
threeStacks.pop(1)

threeStacks.pop(2)
threeStacks.pop(2)
threeStacks.pop(2)
threeStacks.pop(2)
threeStacks.pop(2)
threeStacks.pop(2)

threeStacks.pop(3)
threeStacks.pop(3)
threeStacks.pop(3)
threeStacks.pop(3)
threeStacks.pop(3)
threeStacks.pop(3)

threeStacks.push(1, 5)
threeStacks.push(1, 4)
threeStacks.push(1, 3)
threeStacks.push(1, 2)
threeStacks.push(1, 1)
threeStacks.push(1, 1)

threeStacks.push(2, 5)
threeStacks.push(2, 4)
threeStacks.push(2, 3)
threeStacks.push(2, 2)
threeStacks.push(2, 1)
threeStacks.push(2, 1)

threeStacks.push(3, 5)
threeStacks.push(3, 4)
threeStacks.push(3, 3)
threeStacks.push(3, 2)
threeStacks.push(3, 1)
threeStacks.push(3, 1)
