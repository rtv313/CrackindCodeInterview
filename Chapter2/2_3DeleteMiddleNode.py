from LinkedList import LinkedList

link_list = LinkedList()
link_list.add_node(1)
link_list.add_node(2)
node = link_list.add_node(3)
link_list.add_node(4)
link_list.add_node(5)


def delete_middle_node(node):
    node.data = node.next.data
    node.next = node.next.next


link_list.print_list()
delete_middle_node(node)
link_list.print_list()
