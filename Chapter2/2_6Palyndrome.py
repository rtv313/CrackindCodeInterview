from LinkedList import LinkedList
# A mí me mima.
link_list = LinkedList()
link_list.add_node('a')
link_list.add_node('m')
link_list.add_node('i')
link_list.add_node('m')
link_list.add_node('e')
link_list.add_node('m')
link_list.add_node('i')
link_list.add_node('m')
link_list.add_node('a')

link_list2 = LinkedList()
link_list2.add_node('a')
link_list2.add_node('m')
link_list2.add_node('i')
link_list2.add_node('m')
link_list2.add_node('e')
link_list2.add_node('m')
link_list2.add_node('i')
link_list2.add_node('m')
link_list2.add_node('t')

def check_list_palindrome(link_list):
    runner = link_list.head
    str_list = ''

    while runner != None:
        str_list += runner.data
        runner = runner.next
    rev_str = str_list[::-1]

    for index in range(len(str_list)):
        if str_list[index]!=rev_str[index]:
            return False

    return True

print(check_list_palindrome(link_list))
print(check_list_palindrome(link_list2))