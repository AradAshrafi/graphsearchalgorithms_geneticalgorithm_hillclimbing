def a_star(start_node, dest_node):
    expanded_nodes = set()  # to
    visited_nodes_list = {}  # must sort them base on their h(n) + g(n) = f(n)
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
                # if this child is added to expanded nodes set before,it has found it's shortest path from origin
                # we can't update this node better than this -> we pass to current_node's next child
                continue
            if not x.visited:
                # x is not visited,it's the first time that we reach this node from origin
                # so we must update it's parent node,and it's cost in addition to it's visited field
                x.visited = True
                x.parent = current_node
                x.costFromOrigin = current_node.costFromOrigin + current_node.children[
                    x]  # parent's costFromOrigin from origin + distance between'em
                heuristic_plus_cost = x.costFromOrigin + x.heuristic
                visited_nodes_list.update({x: heuristic_plus_cost})
            else:
                # x has been visited before
                # so we must compare this new path with previous one and assign minimum of them to x's cost
                new_cost = current_node.costFromOrigin + current_node.children[x]  # maybe new path has shorter distance
                # reminder : current_node.children[x] will return path between current node and child x in children dict
                if new_cost < x.costFromOrigin:
                    x.costFromOrigin = new_cost
                    x.parent = current_node
                    # f(n) of x is also changed,so i must update it's value in visited_nodes dictionary
                    # to do so,i'll first remove it from dictionary and then add correct value of it
                    # actually i could add another field to Node named f or something like that
                    # that will avoid this deleting and adding to dictionary,like what i did in uniform cost
                    # i just liked to try this new approach as well :D,and don't complicate my Node structure further
                    del visited_nodes_list[x]
                    visited_nodes_list.update({x: (x.costFromOrigin + x.heuristic)})

        # find next node with lowest cost to be expanded next
        current_node = find_next_node_with_lowest_predicted_cost(visited_nodes_list=visited_nodes_list)
        # remove it from unexpanded nodes list and add it to expanded set
        del visited_nodes_list[current_node]
        expanded_nodes.add(current_node)

    return expanded_nodes.__len__(), visited_nodes_list.__len__()  # return them to compare with other algorithms


# function that finds node with lowest cost in unexpanded nodes list
def find_next_node_with_lowest_predicted_cost(visited_nodes_list):
    lowest_cost = 1000000
    lowest_cost_node = None
    for node in visited_nodes_list:
        if visited_nodes_list[node] < lowest_cost:
            lowest_cost_node = node
            lowest_cost = visited_nodes_list[node]
    return lowest_cost_node


# in Tree mode we won't check if node is visited or not (obvious though)
def tree_mode_a_star(start_node, dest_node):
    expanded_nodes = set()  # to
    visited_nodes_list = {}  # must sort them base on their h(n) + g(n) = f(n)
    expanded_nodes.add(start_node)
    current_node = start_node
    start_node.costFromOrigin = 0
    while True:
        # if dest_node is visited and has parent,algorithm reaches to end and it has found the path with lowest cost
        # compare it with graph mode for more clarification
        if dest_node.parent is not None:
            break
        for x in current_node.children:
            # reminder:we don't check if this node has been visited before or not in tree
            # for more clarity read comments of graph mode
            x.parent = current_node
            x.costFromOrigin = current_node.costFromOrigin + current_node.children[
                x]  # parent's costFromOrigin from origin + distance between'em
            heuristic_plus_cost = x.costFromOrigin + x.heuristic
            visited_nodes_list.update({x: heuristic_plus_cost})

        # find next node with lowest cost to be expanded next
        current_node = find_next_node_with_lowest_predicted_cost(visited_nodes_list=visited_nodes_list)
        # remove it from unexpanded nodes list and add it to expanded set
        del visited_nodes_list[current_node]
        expanded_nodes.add(current_node)

    return expanded_nodes.__len__(), visited_nodes_list.__len__()  # return them to compare with other algorithms
