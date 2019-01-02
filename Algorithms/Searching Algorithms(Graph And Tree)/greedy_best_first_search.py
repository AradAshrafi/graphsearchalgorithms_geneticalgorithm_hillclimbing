import queue as queue
from Utils.Node import Node


def greedy_best_first_search(start_node, dest_node):
    expanded_nodes = []  # to compare it with other algorithms
    visited_nodes_queue = queue.PriorityQueue()  # to sort them base on their heuristic
    expanded_nodes.append(start_node)
    start_node.visited = True
    current_node = start_node
    while True:
        if dest_node.visited:
            break
        for x in current_node.children:
            if not x.visited:
                x.visited = True
                x.parent = current_node
                visited_nodes_queue.put((x.heuristic, x))
        current_node = visited_nodes_queue.get(0)[1]
        expanded_nodes.append(current_node)
    return expanded_nodes.__len__(), visited_nodes_queue.qsize()
