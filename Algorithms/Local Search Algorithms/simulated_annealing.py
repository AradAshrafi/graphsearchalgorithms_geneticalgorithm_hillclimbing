from math import ceil
from random import randint


def simulated_annealing(initial_state):
    current_state = initial_state
    number_of_steps = 0
    while True:
        print(current_state.evaluate_value())
        next_states = current_state.possible_next_states()  # find all possible next states better than current one
        if len(next_states) == 0:
            break
        else:
            # find next state based on cooling scheduler function of simulated annealing
            current_state = cooling_scheduler(next_states=next_states, current_step_number=number_of_steps)
            number_of_steps += 1
    print(current_state.evaluate_value(), number_of_steps)


# cooling function every TWO STEPS increasing chance of better situation in graph
# number of steps for increasing the chance are configurable
# I've chosen to increase the chance every TWO steps based on hill climbing algorithms total steps (total steps O(10))
def cooling_scheduler(next_states, current_step_number):
    new_next_states = []
    next_states.sort(key=lambda x: x.evaluate_value(), reverse=True)  # sort next states by their value
    for i in range(len(next_states)):
        # create new next state list with cooling function in the way that:
        # node with the most value will eventually become the node the most chance to be picked randomly after a while
        # so nodes with more values must be repeated more in the new list
        phase_of_cooling = int(
            current_step_number / 2)  # explained completely why it's divided by 2 above current function
        # my created functionality to inject possibility in choosing the next state
        # node with the most value will eventually become the node the most chance to be picked randomly after a while
        new_next_states.extend([next_states[i]] * (((len(next_states) - i) * phase_of_cooling) + 1))
    return new_next_states[randint(0, len(new_next_states) - 1)]
