from copy import deepcopy as clone


class State:
    def __init__(self, graph_structure, edges_number):
        self.graphStructure = graph_structure
        self.edgesNumber = edges_number

    def evaluate_value(self):
        delta = 0
        for x in self.graphStructure:
            for y in x.neighbours:
                if x.colour != y.colour:
                    delta += 1
        delta /= self.edgesNumber
        return delta

    # calculate possible next moves(states) among neighbours state
    def possible_next_states(self):
        possible_next_states = []
        current_value = self.evaluate_value()
        for i in range(self.graphStructure):
            new_state = clone(self)
            new_state2 = clone(self)
            increase_node_color(new_state.graphStructure[i])
            decrease_node_color(new_state2.graphStructure[i])
            if new_state.evaluate_value() > current_value:
                possible_next_states.append(new_state)
            if new_state2.evaluate_value() > current_value:
                possible_next_states.append(new_state2)
        return possible_next_states


def increase_node_color(node):
    node.colour = (node.colour + 1) % 3


def decrease_node_color(node):
    node.colour = (node.colour - 1) % 3
