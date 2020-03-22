# Graphs for testing
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

# Function for build graph
def build_graph(list_projects,list_dependencies):
    graph = dict()

    for node in list_projects:
        graph[node] = list()

    for dependency,actual_node in list_dependencies:
        if graph[actual_node].count(dependency) == 0:
            graph[actual_node].append(dependency)

    return graph


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

projects = ['a','b','c','d','e','f']
dependencies=[('a','d'),('f','b'),('b','d'),('f','a'),('d','c')]
b_graph = build_graph(projects,dependencies)

build_order(graph)
build_order(graph2)
build_order(b_graph)
