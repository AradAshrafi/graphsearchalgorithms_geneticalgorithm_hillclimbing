class Node:
    def __init__(self, name, heuristic=0, is_goal=False):
        self.name = name
        self.children = {}  # this will be a list of nodes with their corresponding distance
        self.heuristic = heuristic  # this will be used in greedy best first and A*
        self.visited = False
        self.parent = None  # this will be used to find the path
        self.costFromOrigin = 0  # will be used for uniform cost & A*


class Node2:
    def __init__(self, name):
        self.name = name
        self.neighbours = set()
        self.color = 0
