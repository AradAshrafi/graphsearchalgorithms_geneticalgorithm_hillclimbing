from Problems.GraphColouring import GraphColouring
from Utils.State import State
from hill_climbing.stochastic_hill_climbing import stochastic_hill_climbing
from hill_climbing.simple_hill_climbing import simple_hill_climbing
from hill_climbing.first_choice_hill_climbing import first_choice_hill_climbing
from hill_climbing.random_restart_hill_climbing import random_restart_hill_climbing
from genetic import genetic

if __name__ == '__main__':
    # Create Graph Colouring Problem
    problem = GraphColouring()
    # Catch Initial Graph
    graph_structure = problem.get_initial_graph()
    # Calculate edges number from graph structure
    # edges number will be needed in evaluating graph state
    edges_number = 0
    for x in graph_structure:
        edges_number += len(x.neighbours)
    edges_number /= 2
    # Create Initial State with structure and edges number
    initial_state = State(graph_structure=graph_structure, edges_number=edges_number)
    # Perform Algorithms :
    algorithm = "GENETIC"
    if algorithm == "SIMPLE HILL CLIMBING":
        simple_hill_climbing(initial_state)

    if algorithm == "STOCHASTIC HILL CLIMBING":
        stochastic_hill_climbing(initial_state)

    if algorithm == "FIRST CHOICE HILL CLIMBING":
        first_choice_hill_climbing(initial_state)

    if algorithm == "RANDOM RESTART HILL CLIMBING":
        random_restart_hill_climbing(initial_state)

    if algorithm == "GENETIC":
        number_of_generations = 50
        population_size = 10
        tournament_size = 5
        mutation_rate = 0.01
        genetic(initial_state=initial_state, number_of_generations=number_of_generations,
                population_size=population_size, tournament_size=tournament_size,
                mutation_rate=mutation_rate)
