from copy import deepcopy as clone
from random import randint as randint


class State:
    def __init__(self, graph_structure, edges_number):
        self.graphStructure = graph_structure  # list of nodes
        self.edgesNumber = edges_number  # total edges in a graph

    # evaluate current state value based on evaluation function
    def evaluate_value(self):
        delta = 0
        for x in self.graphStructure:
            for y in x.neighbours:
                if x.colour != y.colour:
                    delta += 1
        delta /= self.edgesNumber
        return delta

    # calculate possible next moves(states) among neighbours state
    def possible_next_states(self, only_better_states=True):
        possible_next_states = []
        current_value = self.evaluate_value()
        for i in range(len(self.graphStructure)):
            # we must clone it
            # otherwise we will be changing the source structure for ever and we'll only get one new state at the end
            new_state = clone(self)
            new_state2 = clone(self)
            increase_node_color(new_state.graphStructure[i])
            decrease_node_color(new_state2.graphStructure[i])
            if only_better_states:
                if new_state.evaluate_value() > current_value:
                    possible_next_states.append(new_state)
                if new_state2.evaluate_value() > current_value:
                    possible_next_states.append(new_state2)
            else:
                possible_next_states.extend([new_state, new_state2])
        return possible_next_states

    def new_random_state(self):  # will be used in random restart and genetic
        new_state = clone(self)
        # must clone last graph,otherwise our source graph will change,because it contains pointers to nodes,and we are
        # -changing that same nodes colour
        for node in new_state.graphStructure:
            node.colour = randint(0, 3)
        return new_state

    def print_state(self):
        for node in self.graphStructure:
            print(node.name, ":", node.colour, ",", end=" ")


def increase_node_color(node):
    node.colour = (node.colour + 1) % 3


def decrease_node_color(node):
    node.colour = (node.colour - 1) % 3
