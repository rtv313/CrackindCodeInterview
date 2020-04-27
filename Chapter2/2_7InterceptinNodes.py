from LinkedList import LinkedList

# List intercepts
# 1-> 2-> 3-> 4->5
# 1-> 2-> from here it points to 3 from the above list

link_list_one = LinkedList()
link_list_two = LinkedList()

# First list
link_list_one.add_node(1)
link_list_one.add_node(2)
intercept_node = link_list_one.add_node(3)
link_list_one.add_node(4)
link_list_one.add_node(5)

# Second list
link_list_two.add_node(1)
second_node = link_list_two.add_node(2)
second_node.next = intercept_node

link_list_one.print_list()
link_list_two.print_list()


def check_list_intercept(head1,head2):

    nodesSet = set()
    runner_one = head1
    runner_two = head2

    while runner_one is not None:
        nodesSet.add(runner_one)
        runner_one = runner_one.next

    while runner_two is not  None:
        if runner_two in nodesSet:
            return runner_two
        runner_two = runner_two.next


    print('The links not intercept')
    return None

print(str(check_list_intercept(link_list_one.head,link_list_two.head).data))