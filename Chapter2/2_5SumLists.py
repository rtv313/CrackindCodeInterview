from LinkedList import LinkedList

link_list_one = LinkedList()
link_list_one.add_node(7)
link_list_one.add_node(7)
link_list_one.add_node(7)

link_list_two = LinkedList()
link_list_two.add_node(8)
link_list_two.add_node(8)
link_list_two.add_node(8)

def sum_lists_easy(list_one,list_two):

    runner = list_one.head
    str_list_one = ''
    str_list_two = ''

    while runner != None:
        str_list_one+=str(runner.data)
        runner = runner.next

    runner = list_two.head
    while runner != None:
        str_list_two+=str(runner.data)
        runner = runner.next

    str_list_one = str_list_one[::-1]
    str_list_two = str_list_two[::-1]

    int_list_one = int(str_list_one)
    int_list_two = int(str_list_two)

    result = int_list_one + int_list_two

    result_list = LinkedList()
    result_str = str(result)

    for digit in result_str:
        result_list.add_node(digit)

    return result_list


sum_lists_easy(link_list_one,link_list_two).print_list()