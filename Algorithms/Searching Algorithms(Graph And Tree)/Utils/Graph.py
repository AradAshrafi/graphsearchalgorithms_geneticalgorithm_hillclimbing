from collections import defaultdict


class Graph:
    def __init__(self):
        self.graphAdjacencyList = defaultdict(list)

    def add_bidirectional_edge(self, u, v):
        self.graphAdjacencyList[u].append(v)
        self.graphAdjacencyList[v].append(u)

    def print_edges(self):
        for i in self.graphAdjacencyList:
            print(i, self.graphAdjacencyList[i])
