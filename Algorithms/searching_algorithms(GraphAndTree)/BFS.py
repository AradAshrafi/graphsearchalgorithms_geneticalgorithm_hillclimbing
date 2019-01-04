def graph_bfs(start_node, destination_node):
    # BFS traversal
    nodes_to_visit_queue = [start_node]
    expanded_nodes = []  # just to compare it with other algorithms
    max_mem_usage = 0
    # first visit starting node
    start_node.visited = True
    while nodes_to_visit_queue.__len__() > 0:
        # visit current node
        # check for unvisited neighbours
        for x in nodes_to_visit_queue[0].children:
            if not x.visited:
                nodes_to_visit_queue.append(x)
                x.visited = True
                x.parent = nodes_to_visit_queue[0]
        last_visited_node = nodes_to_visit_queue.pop(0)
        expanded_nodes.append(last_visited_node)
        # check for memory usage
        max_mem_usage = max(max_mem_usage, len(nodes_to_visit_queue) + len(expanded_nodes))
        # check if we reach destination
        if last_visited_node == destination_node:
            break
    return expanded_nodes.__len__(), nodes_to_visit_queue.__len__(), max_mem_usage


# we won't check whether a node is visited or not in tree mode
def tree_bfs(start_node, destination_node):
    nodes_to_visit_queue = [start_node]
    max_mem_usage = 0
    # loop till we visit the destination node
    while destination_node.parent is None:
        nodes_to_visit_queue.extend(nodes_to_visit_queue[0].children)
        for x in nodes_to_visit_queue[0].children:
            x.parent = nodes_to_visit_queue[0]

        max_mem_usage = max(max_mem_usage, len(nodes_to_visit_queue))
        nodes_to_visit_queue.pop(0)
        if destination_node.parent is not None:
            break
    print()
    return max_mem_usage
