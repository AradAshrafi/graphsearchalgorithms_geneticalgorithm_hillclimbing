from LDFS import graph_ldfs, tree_ldfs
from copy import deepcopy as clone


def graph_idfs(graph_city_details_dictionary):
    i = 1
    while True:
        new_graph_city_details_dictionary = clone(graph_city_details_dictionary)
        start_node = new_graph_city_details_dictionary["Arad"]
        destination_node = new_graph_city_details_dictionary["Bucharest"]
        graph_ldfs(start_node, destination_node, i)
        if destination_node.parent is not None:
            return new_graph_city_details_dictionary
        else:
            i += 1


# in tree mode we won't check if a node is visited or not before
def tree_idfs(graph_city_details_dictionary):
    i = 1
    while True:
        new_graph_city_details_dictionary = clone(graph_city_details_dictionary)
        start_node = new_graph_city_details_dictionary["Arad"]
        destination_node = new_graph_city_details_dictionary["Bucharest"]
        tree_ldfs(start_node, destination_node, i)
        if destination_node.parent is not None:
            return new_graph_city_details_dictionary
        else:
            i += 1
