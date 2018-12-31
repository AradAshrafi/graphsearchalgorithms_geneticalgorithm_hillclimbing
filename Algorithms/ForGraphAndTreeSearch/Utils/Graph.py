from collections import defaultdict


class Graph:
    def __init__(self):
        self.graphAdjacencyList = defaultdict(list)
        self.maximumNodeNumber = 0

    def add_edge(self, u, v):
        self.graphAdjacencyList[u].append(v)
        self.maximumNodeNumber = max(u, v, self.maximumNodeNumber)

    def print_edges(self):
        for i in self.graphAdjacencyList:
            print(i, self.graphAdjacencyList[i])
