class RoutingBetweenCities:
    def __init__(self):
        # First index of each city is it's own heuristic to goal(bucharest)
        self.initialState = [{"Arad": [366, {"Zerind": [75, 374]}, {"Timisoara": [118, 329]}, {"Sibiu": [140, 253]}]},
                             {"Zerind": [374, {"Oradea": 71}, {"Arad": 75}]},
                             {"Timisoara": [329, {"Arad": 118}, {"Lugoj": 111}]},
                             {"Sibiu": [253, {"Arad": 140}, {"Oradea": 151}, {"Fagaras": 99}, {"RimnicuVilcea": 80}]},
                             {"Oradea": [380, {"Zerind ": 71}, {"Sibiu ": 151}]},
                             {"Lugoj": [244, {"Timisoara": 111}, {"Mehadia ": 70}]},
                             {"Fagaras": [178, {"Sibiu": 99}, {"Bucharest": 211}]},
                             {"Rimnicu Vilcea": [193, {"Sibiu ": 80}, {"Pitesti": 97}, {"Craiova": 146}]},
                             {"Mehadia": [241, {"Lugoj ": 70}, {"Dobreta": 75}]},
                             {"Dobreta": [242, {"Mehadia": 75}, {"Craiova ": 120}]},
                             {"Craivoa": [160, {"Dobreta": 120}, {"RimnicuVilcea": 146}, {"Pitesti": 138}]},
                             {"Pitesti": [98, {"RimnicuVilcea ": 97}, {"Craiova": 138}, {"Bucharest": 101}]},
                             {"Bucharest": [0, {"Fagaras": 211}, {"Pitesti": 101}, {"Giurgiu": 90}]},
                             {"Giurgiu": [77, {"Bucharest": 90}]}
                             ]
