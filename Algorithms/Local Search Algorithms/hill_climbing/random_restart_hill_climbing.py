def random_restart_hill_climbing(initial_state):
    # total time of restarts
    restart_times = 10
    current_state = initial_state
    best_state = initial_state  # to have the best state among all these iterations[restarts]
    expanded_states = 0
    viewed_states = 0
    while True:
        # print(current_state.evaluate_value())
        next_states = current_state.possible_next_states()  # find all possible next states better than current one
        if len(next_states) == 0:
            if best_state.evaluate_value() < current_state.evaluate_value():
                best_state = current_state
            if restart_times > 0:
                current_state = current_state.new_random_state()
                restart_times -= 1
            else:
                break
        else:
            best_next_state = next_states[0]
            for state in next_states:
                if state.evaluate_value() > best_next_state.evaluate_value():
                    best_next_state = state
            current_state = best_next_state
            expanded_states += 1
            viewed_states += len(next_states)
    print("expanded states number : ", expanded_states)
    print("viewed states number : ", viewed_states)
    print("final state colours : ", end="")
    best_state.print_state()
