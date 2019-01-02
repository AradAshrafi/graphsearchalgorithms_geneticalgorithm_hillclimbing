def graph_bfs(start_node, destination_node):
    # BFS traversal
    nodes_to_visit_queue = [start_node]
    expanded_nodes = []
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
    return expanded_nodes, nodes_to_visit_queue, max_mem_usage


def tree_bfs(start_node, destination_node):
    nodes_to_visit_queue = [start_node]
    max_mem_usage = 0
    while nodes_to_visit_queue.__len__() > 0:
        nodes_to_visit_queue.extend(nodes_to_visit_queue[0].children)
        print(nodes_to_visit_queue[0].name, end=" ")
        max_mem_usage = max(max_mem_usage, len(nodes_to_visit_queue))
        last_visited_node = nodes_to_visit_queue.pop(0)
        if last_visited_node == destination_node:
            break
    print()
    return max_mem_usage
