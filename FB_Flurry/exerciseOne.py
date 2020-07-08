def get_middle(str):
    length = len(str)
    index = length / 2

    if (length % 2) == 0:
        print('Even');
        return str[index - 1] + str[index]
    else:
        print('Odd')
        return str[index]