from random import randint as randint


def stochastic_hill_climbing(initial_state):
    current_state = initial_state
    expanded_states = 0
    viewed_states = 0
    while True:
        # print(current_state.evaluate_value())
        next_states = current_state.possible_next_states()  # find all possible next states better than current one
        if len(next_states) == 0:
            break
        else:
            current_state = choose_next_state_with_distributed_probability(next_states)
            expanded_states += 1
            viewed_states += len(next_states)
    print("expanded states number : ", expanded_states)
    print("viewed states number : ", viewed_states)
    print("final state colours : ", end="")
    current_state.print_state()


def choose_next_state_with_distributed_probability(next_states):
    new_next_states = []
    next_states.sort(key=lambda x: x.evaluate_value(), reverse=True)  # sort next states by their value
    for i in range(len(next_states)):
        # create new next state list in the way that node with the most value have the most chance to be picked randomly
        # so nodes with more values must be repeated more in the new list
        new_next_states.extend([next_states[i]] * (len(next_states) - i))
    return new_next_states[randint(0, len(new_next_states) - 1)]
