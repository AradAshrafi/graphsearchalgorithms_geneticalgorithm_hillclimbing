from Utils.Graph import Graph
from Utils.Node import Node


def graph_dfs(graph, starting_node):
    # Mark all the vertices as not visited
    visited = [False] * (graph.maximumNodeNumber + 1)

    # Call the recursive helper function to print
    # DFS traversal
    graph_dfs_operation(graph, starting_node, visited)


def graph_dfs_operation(graph, starting_node, visited_array):
    # first visit starting node
    visited_array[starting_node] = True
    print(starting_node)

    # then visit it's neighbours
    for i in graph.graphAdjacencyList[starting_node]:
        if not visited_array[i]:
            graph_dfs_operation(graph, i, visited_array)


def tree_dfs(root):
    print(root.name)
    for child in root.children:
        tree_dfs(child)


if __name__ == '__main__':
    # Graph
    g = Graph()
    g.add_bidirectional_edge(0, 1)
    g.add_bidirectional_edge(0, 2)
    g.add_bidirectional_edge(1, 2)
    g.add_bidirectional_edge(2, 0)
    g.add_bidirectional_edge(2, 3)

    print("traversal of graph is")
    graph_dfs(graph=g, starting_node=1)

    # Tree
    root = Node(1)
    root.children.append(Node(2))
    root.children.append(Node(3))
    root.children[0].children.append(Node(4))
    root.children[1].children.append(Node(5))

    print("traversal of tree is")
    tree_dfs(root)
