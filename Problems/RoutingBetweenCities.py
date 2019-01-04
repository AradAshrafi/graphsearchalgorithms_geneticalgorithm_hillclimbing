from Utils.Node import Node


class RoutingBetweenCities:
    def __init__(self):
        # holds each city with it's neighbours and their distance
        self.initialStateAdjacencyList = {"Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
                                          "Zerind": {"Oradea": 71, "Arad": 75},
                                          "Timisoara": {"Arad": 118, "Lugoj": 111},
                                          "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80},
                                          "Oradea": {"Sibiu": 151, "Zerind": 71},
                                          "Lugoj": {"Timisoara": 111, "Mehadia": 70},
                                          "Fagaras": {"Sibiu": 99, "Bucharest": 211},
                                          "Rimnicu Vilcea": {"Sibiu": 80, "Pitesti": 97, "Craiova": 146},
                                          "Mehadia": {"Lugoj": 70, "Dobreta": 75},
                                          "Dobreta": {"Mehadia": 75, "Craiova": 120},
                                          "Craiova": {"Dobreta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
                                          "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101},
                                          "Bucharest": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90},
                                          "Giurgiu": {"Bucharest": 90}}

        # heuristic distance of each city to goal(bucharest)
        self.initialStateHeuristics = {"Arad": 366, "Zerind": 374, "Timisoara": 329, "Sibiu": 253,
                                       "Oradea": 380,
                                       "Lugoj": 244, "Fagaras": 178, "Rimnicu Vilcea": 193, "Mehadia": 241,
                                       "Dobreta": 242,
                                       "Craiova": 160, "Pitesti": 98, "Bucharest": 0, "Giurgiu": 77}

    def get_initial_graph(self):
        # creating a dictionary based on city names
        # each entry of this dict holds a node that's created with this name [i've use it kinda like hashMap in java]
        graph_details_dictionary = {}
        # creating graph nodes with their names and heuristic values
        for x in self.initialStateAdjacencyList:
            current_node = Node(name=x, heuristic=self.initialStateHeuristics[x])
            graph_details_dictionary.update({x: current_node})

        # fill children field of each node and assign pointers to it's children with it's corresponding cost
        # children field is a dictionary consist of children nodes and their cost
        # in this form -> a.children = {"city a" : 200 , "city b" : 400}
        for x in graph_details_dictionary:
            for y in self.initialStateAdjacencyList[x]:
                graph_details_dictionary[x].children.update(
                    {graph_details_dictionary[y]: self.initialStateAdjacencyList[x][y]})  # update children dictionary
                # like the form specified above :{"child city x" :200}

        return graph_details_dictionary


if __name__ == '__main__':
    routingBetweenCities = RoutingBetweenCities()
    a = routingBetweenCities.get_initial_graph()
    print()
