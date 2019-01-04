def first_choice_hill_climbing(initial_state):
    current_state = initial_state
    expanded_states = 0
    viewed_states = 0
    while True:
        print(current_state.evaluate_value())
        next_states = current_state.possible_next_states()  # find all possible next states better than current one
        if len(next_states) == 0:
            break
        else:
            current_state = next_states[0]
            expanded_states += 1
            viewed_states += len(next_states)
    print("expanded states number : ", expanded_states)
    print("viewed states number : ", viewed_states)
    print("final state colours : ", end="")
    current_state.print_state()
