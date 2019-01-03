from LDFS import graph_ldfs
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


# tod
def tree_idfs(root, destination_node):
    if destination_node.visited:
        return
    for child in root.children:
        tree_idfs(child, destination_node)
