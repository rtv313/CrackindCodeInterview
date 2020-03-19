from LinkedList import LinkedList

link_list = LinkedList()
link_list.add_node(4)
link_list.add_node(5)
link_list.add_node(3)
link_list.add_node(1)
link_list.add_node(2)


def partition_around_x(link_list, value):
    lower_x_list = LinkedList()
    equal_x_list = LinkedList()
    greater_x_list = LinkedList()
    last_node_lower = None
    last_node_equal = None
    runner = link_list.head

    while runner != None:
        if runner.data < value:
            last_node_lower = lower_x_list.add_node(runner.data)
        elif runner.data == value:
            last_node_equal = equal_x_list.add_node(runner.data)
        else:
            greater_x_list.add_node(runner.data)
        runner = runner.next

    last_node_lower.next = equal_x_list.head
    last_node_equal.next = greater_x_list.head
    link_list.head = lower_x_list.head


link_list.print_list()
partition_around_x(link_list, 3)
link_list.print_list()
