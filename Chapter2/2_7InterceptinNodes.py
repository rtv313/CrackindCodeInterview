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

    list_dict = dict()
    list_dict_nodes = dict()
    runner_one = head1
    runner_two = head2

    while(runner_one!=None):
        node_id = runner_one.__hash__()

        if node_id in list_dict:
            list_dict[node_id]+=1
        else:
            list_dict[node_id]=1
            list_dict_nodes[node_id] = runner_one

        runner_one = runner_one.next

    while (runner_two != None):
        node_id = runner_two.__hash__()

        if node_id in list_dict:
            list_dict[node_id] += 1
        else:
            list_dict[node_id] = 1

        runner_two = runner_two.next

    for key in list_dict.keys():

        if list_dict[key] > 1:
            print('The links intercepts')
            return list_dict_nodes[key]

    print('The links not intercept')

print(str(check_list_intercept(link_list_one.head,link_list_two.head).data))