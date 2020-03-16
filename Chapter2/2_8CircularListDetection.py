from LinkedList import LinkedList

link_list = LinkedList()
link_list.add_node('a')
link_list.add_node('b')
node_c = link_list.add_node('c')
link_list.add_node('d')
node_e = link_list.add_node('e')
node_e.next = node_c

def detect_start_node_cicle(head):
    list_dict = dict()
    runner = head

    while (runner!=None):

        node_id = runner.__hash__()

        if node_id in list_dict:
            list_dict[node_id] += 1
            if list_dict[node_id] > 1:
                print(runner.data)
                return runner
        else:
            list_dict[node_id] = 1

        runner = runner.next

    print('No cycle')
    return None


detect_start_node_cicle(link_list.head)
