graph = {"a": ["c"],
         "b": ["c", "e"],
         "c": ["a", "b", "d", "e"],
         "d": ["c"],
         "e": ["c", "b"],
         "f": []
         }


# Breadth First Search
def route_between(graph, node_a, node_target):
    if node_a not in graph:
        print(node_a + ' this node not exist')
        return

    if node_target not in graph:
        print(node_target + ' this node not exist')
        return

    # Breadth First Search
    nodes_to_visit_queue = list()
    nodes_to_visit_queue.append(node_a)
    nodes_visited_queue = list()

    while len(nodes_to_visit_queue) > 0:
        # Get neighbours
        neighbours = graph[nodes_to_visit_queue[0]]
        # Visit Node
        visited_node = nodes_to_visit_queue.pop(0)
        nodes_visited_queue.append(visited_node)

        if visited_node == node_target:
            print('There is a path between ' + node_a + ' and ' + node_target)
            return

        for neighbour in neighbours:
            if nodes_visited_queue.count(neighbour) == 0:
                nodes_to_visit_queue.append(neighbour)

    print('No path between ' + node_a + ' and ' + node_target)
    return


route_between(graph, 'z', 'e')
route_between(graph, 'a', 'z')
route_between(graph, 'a', 'e')
route_between(graph, 'a', 'f')
