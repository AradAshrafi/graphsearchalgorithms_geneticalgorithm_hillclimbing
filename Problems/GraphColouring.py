class GraphColouring:
    def __init__(self):
        self.initialState = {"A": {"C", "D", "F", "J"},
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
