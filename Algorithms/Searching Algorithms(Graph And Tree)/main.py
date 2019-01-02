from Problems.RoutingBetweenCities import RoutingBetweenCities
from Utils.Utils import path_to_destination  # function that finds path from parent nodes
from BFS import tree_bfs, graph_bfs
from DFS import tree_dfs, graph_dfs
from greedy_best_first_search import greedy_best_first_search


def main():
    problem = RoutingBetweenCities()
    graph_city_details_dictionary = problem.get_initial_graph()
    # define mode to perform algorithm
    mode = "Graph"
    Algorithm = "Greedy_Best_First_Search"
    if mode == "Graph":
        # Graph
        print("traversal of graph is")
        expanded_nodes_size = 0
        visited_node_size = 0
        max_memory_usage = 0
        start_node = graph_city_details_dictionary["Arad"]
        dest_node = graph_city_details_dictionary["Bucharest"]

        if Algorithm == "BFS":
            # preform BFS on graph
            expanded_nodes_size, visited_node_size, max_memory_usage = graph_bfs(start_node=start_node,
                                                                                 destination_node=dest_node)

        if Algorithm == "DFS":
            # preform DFS on graph
            graph_dfs(start_node=start_node, destination_node=dest_node)

        if Algorithm == "Greedy_Best_First_Search":
            expanded_nodes_size, visited_node_size = greedy_best_first_search(start_node=start_node,
                                                                              dest_node=dest_node)
            max_memory_usage = expanded_nodes_size + visited_node_size



        # trace back path from destination
        path_to_dest = path_to_destination(destination_node=dest_node)
        print("observed nodes : ", visited_node_size)
        print("expanded nodes : ", expanded_nodes_size)
        print("maximum memory usage based on nodes : ", max_memory_usage)

    if mode == "Tree":
        print("traversal of tree is : ")
        if Algorithm == "BFS":
            max_memory_usage = tree_bfs(graph_city_details_dictionary["Arad"],
                                        graph_city_details_dictionary["Bucharest"])
        if Algorithm == "DFS":
            max_memory_usage = tree_dfs(graph_city_details_dictionary["Arad"],
                                        graph_city_details_dictionary["Bucharest"])
        print("maximum memory usage of tree bfs (nodes held in queue) :", max_memory_usage)


if __name__ == '__main__':
    main()
