def graph_ldfs(start_node, destination_node, depth_limit):
    # first check if it's exceeded the allowed depth
    if start_node.depth > depth_limit:
        return
        # first visit starting node
    start_node.visited = True
    for x in start_node.children:
        if destination_node.visited:
            break
        if not x.visited:
            x.parent = start_node
            x.depth = start_node.depth + 1
            graph_ldfs(x, destination_node, depth_limit)


# in tree mode we won't check if a node is visited or not before
def tree_ldfs(root, destination_node, depth_limit):
    # first check if it's exceeded the allowed depth
    if root.depth > depth_limit:
        return
    # check if we found destination node or not
    if destination_node.parent is not None:
        return
    for x in root.children:
        x.parent = root
        x.depth = root.depth + 1
        graph_ldfs(x, destination_node, depth_limit)
