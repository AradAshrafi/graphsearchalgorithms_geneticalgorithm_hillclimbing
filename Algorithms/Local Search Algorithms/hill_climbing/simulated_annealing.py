from random import randint


def simulated_annealing(initial_state):
    current_state = initial_state
    expanded_states = 0
    viewed_states = 0
    # boolean that notify us when cooling process has been stopped
    cooling_in_process = True
    while cooling_in_process:
        # print(current_state.evaluate_value())
        next_states = current_state.possible_next_states(
            only_better_states=False)  # find all possible next states better or worse than current one
        if len(next_states) == 0:
            break
        else:
            # find next state based on cooling scheduler function of simulated annealing
            current_state, cooling_in_process = cooling_scheduler(next_states=next_states,
                                                                  current_step_number=expanded_states)
            expanded_states += 1
            viewed_states += len(next_states)

    print("expanded states number : ", expanded_states)
    print("viewed states number : ", viewed_states)
    print("final state colours : ", end="")
    current_state.print_state()


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
            current_step_number / 5)  # explained completely why it's divided by 2 above current function
        # my created functionality to inject possibility in choosing the next state
        # node with the most value will eventually become the node the most chance to be picked randomly after a while
        new_next_states.extend([next_states[i]] * int((len(next_states) - i) / (phase_of_cooling + 1)))
    if len(new_next_states) == 0:
        return next_states[0], False
    return new_next_states[randint(0, len(new_next_states) - 1)], True
