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


# tod
def tree_ldfs(root, destination_node):
    if destination_node.visited:
        return
    for child in root.children:
        tree_ldfs(child, destination_node)
