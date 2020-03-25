class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None


# Creat list with random nodes
root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)

root.random = root.next.next
root.next.random = root.next.next.next
root.next.next.random = root.next.next.next.next
root.next.next.next.random = root
root.next.next.next.next.random = root.next

# 1 2 3 4 5
# 3 4 5 1 2


def copy_list_with_random_nodes(root):

    dictionary_copy_original = dict()
    dictionary_original_copy = dict()
    dictionary_randoms = dict()
    runner = root
    runner_copy = None
    root_copy_original = None

    while runner != None:

        print('Runner data:' + str(runner.data))
        dictionary_randoms[runner] = runner.random

        if runner_copy is None:
            runner_copy = Node(runner.data)
            root_copy_original = runner_copy
            dictionary_copy_original[runner_copy] = runner
            dictionary_original_copy[runner] = runner_copy

        elif runner_copy.next is None:
            runner_copy.next = Node(runner.data)
            runner_copy = runner_copy.next
            dictionary_copy_original[runner_copy] = runner
            dictionary_original_copy[runner] = runner_copy

        runner = runner.next

    runner = root_copy_original

    while runner != None:

        original_node = dictionary_copy_original[runner]
        random_original = dictionary_randoms[original_node]
        random_copy = dictionary_original_copy[random_original]
        runner.random = random_copy
        runner = runner.next

    return root_copy_original

root_copy = copy_list_with_random_nodes(root)

runner = root_copy

while runner != None:
    print(runner.random.data)
    runner = runner.next