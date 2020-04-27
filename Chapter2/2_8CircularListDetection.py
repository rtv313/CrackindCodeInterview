from LinkedList import LinkedList

link_list = LinkedList()
link_list.add_node('a')
link_list.add_node('b')
node_c = link_list.add_node('c')
link_list.add_node('d')
node_e = link_list.add_node('e')
node_e.next = node_c


def detect_start_node_cicle(head):
    nodesSet = set()
    runner = head

    while (runner != None):

        if runner in nodesSet:
            return runner
        else:
            nodesSet.add(runner)

        runner = runner.next

    print('No cycle')
    return None


print(detect_start_node_cicle(link_list.head).data)
