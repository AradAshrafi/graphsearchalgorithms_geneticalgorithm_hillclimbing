from Problems.RoutingBetweenCities import RoutingBetweenCities
from Utils.Utils import path_to_destination  # function that finds path from parent nodes
from BFS import tree_bfs, graph_bfs
from DFS import tree_dfs, graph_dfs, dfs_visited_nodes_counter
from greedy_best_first_search import greedy_best_first_search, tree_greedy_best_first_search
from uniform_cost import uniform_cost, tree_mode_uniform_cost
from LDFS import graph_ldfs, tree_ldfs
from IDFS import graph_idfs, tree_idfs
from a_star import a_star, tree_mode_a_star


def main():
    problem = RoutingBetweenCities()
    graph_city_details_dictionary = problem.get_initial_graph()
    # start_node = graph_city_details_dictionary["Arad"]
    dest_node = graph_city_details_dictionary["Bucharest"]
    # expanded_nodes = 0
    # visited_nodes = 0
    # max_memory_usage = 0
    # define mode to perform algorithm
    mode = "Graph"
    algorithm = "A*"
    expanded_nodes, visited_nodes, max_memory_usage = algorithms_switcher(graph_mode_or_tree_mode=mode,
                                                                          algorithm=algorithm
                                                                          ,
                                                                          graph_city_details_dictionary=
                                                                          graph_city_details_dictionary
                                                                          )

    # trace back path from destination
    path_to_dest = path_to_destination(destination_node=dest_node)

    if dest_node.costFromOrigin != 0:
        cost = dest_node.costFromOrigin  # for cost based algorithms :a*,uniform cost ,...
    else:
        cost = path_to_dest.__len__() - 1  # for non cost based algorithm :dfs,bfs
    print("observed nodes : ", visited_nodes)
    print("expanded nodes : ", expanded_nodes)
    print("maximum memory usage based on nodes : ", max_memory_usage)
    print("path cost : ", cost)


def algorithms_switcher(graph_mode_or_tree_mode, algorithm, graph_city_details_dictionary):
    start_node = graph_city_details_dictionary["Arad"]
    dest_node = graph_city_details_dictionary["Bucharest"]
    expanded_nodes = 0
    visited_nodes = 0
    max_memory_usage = 0
    if graph_mode_or_tree_mode == "Graph":
        # Graph
        print("traversal of graph is : ")

        if algorithm == "BFS":
            # preform BFS on graph
            expanded_nodes, unexpanded_nodes, max_memory_usage = graph_bfs(start_node=start_node,
                                                                           destination_node=dest_node)
            visited_nodes = expanded_nodes + unexpanded_nodes

        if algorithm == "DFS":
            # preform DFS on graph
            graph_dfs(start_node=start_node, destination_node=dest_node)
            max_memory_usage = expanded_nodes = visited_nodes = dfs_visited_nodes_counter(graph_city_details_dictionary)

        if algorithm == "LDFS":
            graph_ldfs(start_node=start_node, destination_node=dest_node, depth_limit=2)
            max_memory_usage = expanded_nodes = visited_nodes = dfs_visited_nodes_counter(graph_city_details_dictionary)

        if algorithm == "IDFS":
            graph_city_details_dictionary = graph_idfs(graph_city_details_dictionary=graph_city_details_dictionary)
            # because i clone graph city details dictionary i need to rebuild start and dest nodes
            start_node = graph_city_details_dictionary["Arad"]
            dest_node = graph_city_details_dictionary["Bucharest"]
            visited_nodes = dfs_visited_nodes_counter(graph_city_details_dictionary)
            max_memory_usage = visited_nodes
            expanded_nodes = visited_nodes

        if algorithm == "GREEDY BEST FIRST SEARCH":
            expanded_nodes, unexpanded_nodes, max_memory_usage = greedy_best_first_search(start_node=start_node,
                                                                                          dest_node=dest_node)
            visited_nodes = expanded_nodes + unexpanded_nodes

        if algorithm == "UNIFORM COST":
            expanded_nodes, unexpanded_nodes = uniform_cost(start_node=start_node, dest_node=dest_node)
            visited_nodes = expanded_nodes + unexpanded_nodes
            max_memory_usage = visited_nodes

        if algorithm == "A*":
            expanded_nodes, unexpanded_nodes = a_star(start_node=start_node, dest_node=dest_node)
            visited_nodes = expanded_nodes + unexpanded_nodes
            max_memory_usage = visited_nodes

    if graph_mode_or_tree_mode == "Tree":
        print("traversal of tree is : ")
        if algorithm == "BFS":
            max_memory_usage = tree_bfs(graph_city_details_dictionary["Arad"],
                                        graph_city_details_dictionary["Bucharest"])
        if algorithm == "DFS":
            max_memory_usage = tree_dfs(graph_city_details_dictionary["Arad"],
                                        graph_city_details_dictionary["Bucharest"])
        if algorithm == "LDFS":
            max_memory_usage = tree_ldfs(graph_city_details_dictionary["Arad"],
                                         graph_city_details_dictionary["Bucharest"])
        if algorithm == "IDFS":
            graph_city_details_dictionary = tree_idfs(graph_city_details_dictionary=graph_city_details_dictionary)
            # because i clone graph city details dictionary i need to rebuild start and dest nodes
            start_node = graph_city_details_dictionary["Arad"]
            dest_node = graph_city_details_dictionary["Bucharest"]
            visited_nodes = dfs_visited_nodes_counter(graph_city_details_dictionary)
            max_memory_usage = visited_nodes
            expanded_nodes = visited_nodes

        if algorithm == "GREEDY BEST FIRST SEARCH":
            expanded_nodes, unexpanded_nodes, max_memory_usage = tree_greedy_best_first_search(start_node=start_node,
                                                                                               dest_node=dest_node)
            visited_nodes = expanded_nodes + unexpanded_nodes

        if algorithm == "UNIFORM COST":
            expanded_nodes, unexpanded_nodes = tree_mode_uniform_cost(start_node=start_node, dest_node=dest_node)
            visited_nodes = expanded_nodes + unexpanded_nodes
            max_memory_usage = visited_nodes

        if algorithm == "A*":
            expanded_nodes, unexpanded_nodes = tree_mode_a_star(start_node=start_node, dest_node=dest_node)
            visited_nodes = expanded_nodes + unexpanded_nodes
            max_memory_usage = visited_nodes

    return expanded_nodes, visited_nodes, max_memory_usage


if __name__ == '__main__':
    main()
