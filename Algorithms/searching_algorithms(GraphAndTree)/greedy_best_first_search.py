import queue as queue


def greedy_best_first_search(start_node, dest_node):
    expanded_nodes = []  # to compare it with other algorithms
    visited_nodes_queue = queue.PriorityQueue()  # to sort them base on their heuristic
    maximum_memory_usage = 0  # to compare it with other algorithms
    expanded_nodes.append(start_node)
    start_node.visited = True
    current_node = start_node
    while True:
        # check if we reach to dest or not
        if dest_node.visited:
            break
        for x in current_node.children:
            if not x.visited:
                x.visited = True
                x.parent = current_node
                # x's cost from origin = parent's costFromOrigin from origin + distance between'em
                x.costFromOrigin = current_node.costFromOrigin + current_node.children[x]
                visited_nodes_queue.put((x.heuristic, x))
        maximum_memory_usage = max(maximum_memory_usage, visited_nodes_queue.qsize())
        current_node = visited_nodes_queue.get(0)[1]
        expanded_nodes.append(current_node)
    return expanded_nodes.__len__(), visited_nodes_queue.qsize(), maximum_memory_usage


# won't check if they're visited or not
def tree_greedy_best_first_search(start_node, dest_node):
    expanded_nodes = []  # to compare it with other algorithms
    visited_nodes_queue = queue.PriorityQueue()  # to sort them base on their heuristic to get next best node to visit
    maximum_memory_usage = 0  # to compare it with other algorithms
    expanded_nodes.append(start_node)
    current_node = start_node
    while True:
        if expanded_nodes.__contains__(dest_node):
            break
        for x in current_node.children:
            x.parent = current_node
            visited_nodes_queue.put((x.heuristic, x))
        maximum_memory_usage = max(maximum_memory_usage, visited_nodes_queue.qsize())
        current_node = visited_nodes_queue.get(0)[1]
        expanded_nodes.append(current_node)
    return expanded_nodes.__len__(), visited_nodes_queue.qsize(), maximum_memory_usage
