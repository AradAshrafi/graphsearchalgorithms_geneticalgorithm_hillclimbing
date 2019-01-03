from Utils.Node import Node2


class GraphColouring:
    def __init__(self):
        # description of the problem's graph
        self.initialStateAdjacencyList = {"A": {"C", "D", "F", "J"},
                                          "B": {"D", "E", "F", "G"},
                                          "C": {"A", "E", "G", "H"},
                                          "D": {"A", "B", "H", "I"},
                                          "E": {"B", "C", "I", "J"},
                                          "F": {"A", "B", "K"},
                                          "G": {"B", "C", "K"},
                                          "H": {"C", "D", "K"},
                                          "I": {"D", "E", "K"},
                                          "J": {"D", "A", "K"},
                                          "K": {"F", "G", "H", "I", "J"}
                                          }

    def get_initial_graph(self):
        # creating a dictionary based on city names
        # each entry of this dict holds a node that's created with this name [i've use it kinda like hashMap in java]
        graph_details_dictionary = {}
        # creating graph nodes with their names and heuristic values
        for x in self.initialStateAdjacencyList:
            current_node = Node2(name=x)
            graph_details_dictionary.update({x: current_node})

        # fill children field of each node and assign corresponding pointers to it's neighbours
        # neighbours field is a set of cities
        for x in graph_details_dictionary:
            for y in self.initialStateAdjacencyList[x]:
                graph_details_dictionary[x].neighbours.add(graph_details_dictionary[y])
        # return graph nodes in an array
        graph_structure = (list(graph_details_dictionary.values()))
        return graph_structure
