

def sum_lists(list_one,list_two):

    list_one = list_one[::-1]
    list_two = list_two[::-1]
    list_result = list()

    max_len = max(len(list_one),len(list_two))
    carry = 0

    for x in range(max_len):

        if x < len(list_one):
            value_1 = list_one[x]
        else:
            value_1 = 0

        if x < len(list_two):
            value_2 = list_two[x]
        else:
            value_2 = 0

        result = value_1 + value_2 + carry
        result_str = str(result)

        if len(result_str) > 1:
            carry = int(result_str[0])
            result = int(result_str[1])
            list_result.insert(0,result)
        else:
            list_result.insert(0, result)
            carry = 0

    if carry != 0:
        list_result.insert(0, carry)

    print(list_result)

sum_lists([1,2,3],[1,2])
sum_lists([1,1,1],[1,1,1])
sum_lists([9,0,0],[1,0,0])