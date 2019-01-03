from random import randint as randint
from copy import deepcopy as clone


def random_restart_hill_climbing(initial_state):
    # total time of restarts
    restart_times = 10
    current_state = initial_state
    best_state = initial_state  # to have the best state among all these iterations[restarts]
    number_of_steps = 0
    while True:
        print(current_state.evaluate_value())
        next_states = current_state.possible_next_states()  # find all possible next states better than current one
        if len(next_states) == 0:
            if best_state.evaluate_value() < current_state.evaluate_value():
                best_state = current_state
            if restart_times > 0:
                current_state = random_restart(current_state)
                restart_times -= 1
            else:
                break
        else:
            best_next_state = next_states[0]
            for state in next_states:
                if state.evaluate_value() > best_next_state.evaluate_value():
                    best_next_state = state
            current_state = best_next_state
            number_of_steps += 1
    print(best_state.evaluate_value(), number_of_steps)


def random_restart(current_state):
    new_state = clone(current_state)
    # must clone last graph,otherwise our best_state value will change too,because it's pointer to a node,and we are
    # -changing that nodes colour
    for node in new_state.graphStructure:
        node.colour = randint(0, 3)
    return new_state
