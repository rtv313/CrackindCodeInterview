
def print_stack(stack):
    string = ''
    for element in stack:
        string+=str(element)

    print(string)

def sort_stack():

    stack_1 = list()
    stack_2 = list()
    stack_1.insert(0,3)
    stack_1.insert(0,5)
    stack_1.insert(0,8)
    stack_1.insert(0,1)
    stack_1.insert(0,4)

    print_stack(stack_1)
    print_stack(stack_2)

    for x in range(len(stack_1)):

        while len(stack_1) > 0:

            temp = stack_1[0]

            if len(stack_2) == 0:
                temp = stack_1.pop(0)
                stack_2.insert(0,temp)
            else:
                if stack_2[0] > temp:
                    temp_1 = stack_1.pop(0)
                    temp_2 = stack_2.pop(0)
                    stack_1.insert(0,temp_2)
                    stack_2.insert(0,temp_1)

                else:
                    stack_2.insert(0,stack_1.pop(0))

        while len(stack_2) > 0:
            stack_1.insert(0,stack_2.pop(0))

    print_stack(stack_1)

sort_stack()