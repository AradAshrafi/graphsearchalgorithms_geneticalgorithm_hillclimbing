def uniform_cost(start_node, dest_node):
    expanded_nodes = set()  # to compare it with other algorithms
    visited_nodes_list = []  # must sort them base on their costFromOrigin
    expanded_nodes.add(start_node)
    start_node.visited = True
    current_node = start_node
    start_node.costFromOrigin = 0
    while True:
        if expanded_nodes.__contains__(dest_node):
            break
        for x in current_node.children:
            if not x.visited:
                x.visited = True
                x.parent = current_node
                x.costFromOrigin = current_node.costFromOrigin + current_node.children[
                    x]  # parent's costFromOrigin from origin + distance between'em
                visited_nodes_list.append(x)
            else:
                new_cost = current_node.costFromOrigin + current_node.children[x]  # maybe new path has shorter distance
                if new_cost < x.costFromOrigin:
                    x.costFromOrigin = new_cost
                    x.parent = current_node

        current_node = find_next_node_with_lowest_cost(visited_nodes_list=visited_nodes_list)
        visited_nodes_list.remove(current_node)
        expanded_nodes.add(current_node)
    return expanded_nodes.__len__(), visited_nodes_list.__len__()


def find_next_node_with_lowest_cost(visited_nodes_list):
    lowest_cost_node = visited_nodes_list[0]
    for node in visited_nodes_list:
        if node.costFromOrigin < lowest_cost_node.costFromOrigin:
            lowest_cost_node = node
    return lowest_cost_node


# in Tree mode we won't check if node is visited or not
def tree_uniform_cost(start_node, dest_node):
    expanded_nodes = set()  # to compare it with other algorithms
    visited_nodes_list = []  # must sort them base on their costFromOrigin
    expanded_nodes.add(start_node)
    current_node = start_node
    start_node.costFromOrigin = 0
    while True:
        if expanded_nodes.__contains__(dest_node):
            break
        for x in current_node.children:
            x.parent = current_node
            x.costFromOrigin = current_node.costFromOrigin + current_node.children[
                x]  # parent's costFromOrigin from origin + distance between'em
            visited_nodes_list.append(x)

        current_node = find_next_node_with_lowest_cost(visited_nodes_list=visited_nodes_list)
        visited_nodes_list.remove(current_node)
        expanded_nodes.add(current_node)
    return expanded_nodes.__len__(), visited_nodes_list.__len__()
