def graph_dfs(start_node, destination_node):
    # first visit starting node
    start_node.visited = True
    for x in start_node.children:
        if destination_node.visited:
            break
        if not x.visited:
            x.parent = start_node
            graph_dfs(x, destination_node)


def tree_dfs(root, destination_node):
    if destination_node.visited:
        return
    for child in root.children:
        tree_dfs(child, destination_node)
