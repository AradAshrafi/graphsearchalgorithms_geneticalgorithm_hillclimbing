def simple_hill_climbing(initial_state):
    current_state = initial_state
    number_of_steps = 0
    while True:
        print(current_state.evaluate_value())
        next_states = current_state.possible_next_states() # find all possible next states better than current one
        if len(next_states) == 0:
            break
        else:
            best_next_state = next_states[0]
            for state in next_states:
                if state.evaluate_value() > best_next_state.evaluate_value():
                    best_next_state = state
            current_state = best_next_state
            number_of_steps += 1
    print(current_state.evaluate_value(), number_of_steps)
