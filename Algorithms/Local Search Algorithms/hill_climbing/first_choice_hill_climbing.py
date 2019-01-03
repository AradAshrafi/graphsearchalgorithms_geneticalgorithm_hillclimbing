def first_choice_hill_climbing(initial_state):
    current_state = initial_state
    number_of_steps = 0
    while True:
        print(current_state.evaluate_value())
        next_states = current_state.possible_next_states()  # find all possible next states better than current one
        if len(next_states) == 0:
            break
        else:
            current_state = next_states[0]
            number_of_steps += 1
    print(current_state.evaluate_value(), number_of_steps)
