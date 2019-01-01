from Utils.Graph import Graph
from Utils.Node import Node


def graph_bfs(graph, starting_node):
    # Mark all the vertices as not visited
    visited = {key: False for key in graph.graphAdjacencyList}
    # BFS traversal
    # first visit starting node
    nodes_to_visit_queue = [starting_node]
    while nodes_to_visit_queue.__len__() > 0:
        # visit current node
        print(nodes_to_visit_queue[0])
        visited[nodes_to_visit_queue[0]] = True
        # check for unvisited neighbours
        for x in graph.graphAdjacencyList[nodes_to_visit_queue[0]]:
            if not visited[x]:
                nodes_to_visit_queue.append(x)
                visited[x] = True
        nodes_to_visit_queue.pop(0)


def tree_bfs(starting_node):
    nodes_to_visit_queue = [starting_node]
    while nodes_to_visit_queue.__len__() > 0:
        nodes_to_visit_queue.extend(nodes_to_visit_queue[0].children)
        print(nodes_to_visit_queue[0].name)
        nodes_to_visit_queue.pop(0)


if __name__ == '__main__':
    # Graph
    g = Graph()
    # g.add_bidirectional_edge(0, 1)
    # g.add_bidirectional_edge(0, 2)
    # g.add_bidirectional_edge(1, 2)
    # # g.add_bidirectional_edge(2, 0)
    # g.add_bidirectional_edge(2, 3)
    g.add_bidirectional_edge("1","2")
    g.add_bidirectional_edge("2", "Arad")
    g.add_bidirectional_edge("Arad", "Araaad")
    g.add_bidirectional_edge("Araaaad", "NNN")

    print("traversal of graph is")
    graph_bfs(graph=g, starting_node="Arad")

    # Tree
    root = Node(1)
    root.children.append(Node(2))
    root.children.append(Node(3))
    root.children[0].children.append(Node(4))
    root.children[1].children.append(Node(5))

    print("traversal of tree is")
    tree_bfs(root)
