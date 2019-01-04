def path_to_destination(destination_node):
    # Iterative Implementation ------------>
    if destination_node.parent is None:  # it may happen in LDFS with not sufficient depth
        print("There's no path with the given situation to destination")
        return
    node = destination_node
    path_to_dest = []
    while node is not None:
        path_to_dest.append(node)
        node = node.parent
    path_to_dest.reverse()
    for x in path_to_dest:
        print(x.name, "      ", end=" ")
    print()
    return path_to_dest
    # Recursive Implementation ------------->
    # if ending_node is not None:
    #     path_to_destination(ending_node.parent)
    #     print(ending_node.name)
