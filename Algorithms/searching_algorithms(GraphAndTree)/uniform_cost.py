def uniform_cost(start_node, dest_node):
    expanded_nodes = set()  # to
    visited_nodes_list = []  # must sort them base on their costFromOrigin
    expanded_nodes.add(start_node)
    start_node.visited = True
    current_node = start_node
    start_node.costFromOrigin = 0
    while True:
        # if dest_node is added to expanded nodes,algorithm reaches to end and it has found the path with lowest cost
        if expanded_nodes.__contains__(dest_node):
            break
        for x in current_node.children:
            if expanded_nodes.__contains__(x):
                # if this children is added to expanded node,it has found it's shortest path from origin
                # we can't update this node better than this -> we pass to current_node's next child
                continue
            if not x.visited:
                # x is not visited,it's the first time that we reach this node from origin
                # so we must update it's parent node,and it's cost in addition to it's visited field
                x.visited = True
                x.parent = current_node
                x.costFromOrigin = current_node.costFromOrigin + current_node.children[
                    x]  # parent's costFromOrigin from origin + distance between'em
                visited_nodes_list.append(x)
            else:
                # x has been visited before
                # so we must compare this new path with previous one and assign minimum of them to x's cost
                new_cost = current_node.costFromOrigin + current_node.children[x]  # maybe new path has shorter distance
                if new_cost < x.costFromOrigin:
                    x.costFromOrigin = new_cost
                    x.parent = current_node
        # find next node with lowest cost to be expanded next
        current_node = find_next_node_with_lowest_cost(visited_nodes_list=visited_nodes_list)
        # remove it from unexpanded nodes list and add it to expanded set
        visited_nodes_list.remove(current_node)
        expanded_nodes.add(current_node)

    return expanded_nodes.__len__(), visited_nodes_list.__len__()  # return them to compare with other algorithms


# function that finds node with lowest cost in unexpanded nodes list
def find_next_node_with_lowest_cost(visited_nodes_list):
    lowest_cost_node = visited_nodes_list[0]
    for node in visited_nodes_list:
        if node.costFromOrigin < lowest_cost_node.costFromOrigin:
            lowest_cost_node = node
    return lowest_cost_node


# in Tree mode we won't check if node is visited or not (obvious though)
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
