def graph_dfs(start_node, destination_node):
    # first visit starting node
    start_node.visited = True
    for x in start_node.children:
        if destination_node.visited:
            break
        if not x.visited:
            x.parent = start_node
            graph_dfs(x, destination_node)


def dfs_visited_nodes_counter(graph_city_details_dictionary):
    number_of_visited = 0
    for node_name in graph_city_details_dictionary:
        node = graph_city_details_dictionary[node_name]
        if node.visited:
            number_of_visited += 1
    return number_of_visited


def tree_dfs(root, destination_node):
    if root == destination_node:
        return
    if destination_node.parent is not None:
        return
    for child in root.children:
        child.parent = root
        tree_dfs(child, destination_node)
