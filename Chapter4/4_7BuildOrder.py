graph = {'a': [],
         'b': ['f'],
         'c': ['d'],
         'd': ['a', 'b'],
         'e': [],
         'f': ['a'],
         }

# Cant solve
graph2 = {'a': [],
          'b': ['f'],
          'c': ['d'],
          'd': ['a', 'b', 'c'],
          'e': [],
          'f': ['a'],
          }


def build_order(graph):
    build_order_queue = list()
    nodes = list(graph.keys())

    for x in range(len(nodes)):

        for node in nodes:

            if node in graph and len(graph[node]) == 0:

                build_order_queue.append(node)
                graph.pop(node)

                for node_two in nodes:
                    if node_two in graph and graph[node_two].count(node) != 0:
                        graph[node_two].remove(node)

    if len(build_order_queue) != len(nodes):
        print('Error')
        return None

    string = ''
    for node in build_order_queue:
        string += node + ','
    print(string)

    return build_order_queue


build_order(graph)
build_order(graph2)
