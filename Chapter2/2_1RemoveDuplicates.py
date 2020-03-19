from LinkedList import LinkedList

link_list = LinkedList()
link_list.add_node(1)
link_list.add_node(2)
link_list.add_node(3)
link_list.add_node(4)
link_list.add_node(1)
link_list.add_node(2)
link_list.add_node(3)


def remove_duplicates(linked_list):
    current = link_list.head

    while current != None:

        runner = current

        while runner != None:

            if runner.next != None:
                if current.data == runner.next.data:
                    runner.next = runner.next.next

            runner = runner.next

        current = current.next


link_list.print_list()
remove_duplicates(link_list)
link_list.print_list()
