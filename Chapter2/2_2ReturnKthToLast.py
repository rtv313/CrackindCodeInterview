from LinkedList import LinkedList

link_list = LinkedList()

link_list.add_node(1)
link_list.add_node(2)
link_list.add_node(3)
link_list.add_node(4)
link_list.add_node(1)
link_list.add_node(2)
link_list.add_node(3)

def return_k_last(link_list,k_last):
    counter = 0
    runner = link_list.head

    while runner != None:
        counter+=1
        runner = runner.next

    counter -= k_last
    runner = link_list.head

    for x in range(counter):

        if x == counter-1:
            print(runner.data)
            return

        runner = runner.next

link_list.print_list()
return_k_last(link_list,2)
return_k_last(link_list,1)
return_k_last(link_list,0)