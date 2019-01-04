from random import randint
from copy import deepcopy as clone
import matplotlib.pyplot as plt


def genetic(initial_state, number_of_generations, population_size, tournament_size, mutation_rate):
    number_of_generations = number_of_generations
    population_size = population_size
    tournament_size = tournament_size
    mutation_rate = mutation_rate
    # total mutated genomes =  genome numbers in each chromosome * population size of chromosomes * mutation rate -->
    number_of_each_chromosomes_genome = len(initial_state.graphStructure)
    total_mutated_genomes = number_of_each_chromosomes_genome * mutation_rate * population_size

    # these sets are defined to draw plots and save them in work report
    best_chromosomes_of_each_generation_value = []
    worst_chromosomes_of_each_generation_value = []
    avg_chromosomes_of_each_generation_value = []

    # create initial population based on population_size (INITIAL POPULATION step)
    population = generate_population(initial_state=initial_state, population_size=population_size)
    # create new generations
    for i in range(number_of_generations):
        # choose some how more qualified parents (SELECTION step)
        parents = tournament_to_choose_parents(population=population, tournament_size=tournament_size)
        # generate new population with chosen parents (MATING & CROSS OVER step)
        population = new_generations_population(population_size, parents)
        # mutate some genomes in current generation (MUTATION step)
        apply_mutation_on_new_generation(population=population,
                                         population_size=population_size,
                                         number_of_each_chromosomes_genome=number_of_each_chromosomes_genome,
                                         mutated_genomes_number=total_mutated_genomes)
        population.sort(key=lambda x: x.evaluate_value(), reverse=True)
        # append the best state to it's array to plot best states per generation
        best_chromosomes_of_each_generation_value.append(population[0].evaluate_value())
        # append the worst state to it's array to plot worst states per generation
        worst_chromosomes_of_each_generation_value.append(population[population_size - 1].evaluate_value())
        # append the avg value of all states to it's array to plot avg values per generation
        avg_chromosomes_of_each_generation_value.append(find_avg_value_of_chromosomes(population=population,
                                                                                      population_size=population_size))
    print("number of generation : " + str(number_of_generations) + "\n" +
          "population size : " + str(population_size) + "\n" +
          "tournament size : " + str(tournament_size) + "\n" +
          "mutation rate : " + str(mutation_rate) + "\n" +
          "AVERAGE VALUE CONVERGENCE : " + str(avg_chromosomes_of_each_generation_value[number_of_generations-1]))


# plot_generations_evaluated_value(best_chromosomes=best_chromosomes_of_each_generation_value,
#                                  avg_chromosomes=avg_chromosomes_of_each_generation_value,
#                                  worst_chromosomes=worst_chromosomes_of_each_generation_value,
#                                  details="number of generation : " + str(number_of_generations) + "\n" +
#                                          "population size : " + str(population_size) + "\n" +
#                                          "tournament size : " + str(tournament_size) + "\n" +
#                                          "mutation rate : " + str(mutation_rate)
#                                  )


def generate_population(initial_state, population_size):
    population = []
    while population_size > 0:
        population.append(initial_state.new_random_state())
        population_size -= 1
    return population


# perform some tournaments based on tournament size to choose parents
def tournament_to_choose_parents(population, tournament_size):
    number_of_tournaments = len(population) / tournament_size
    parents = []
    for i in range(int(number_of_tournaments)):
        parents.append(__choose_parent_within_random_tournament(population, tournament_size))
    return parents


# it uses inside tournament_to_choose_parents function
# establishes one tournament and returns the winner state among contestants
def __choose_parent_within_random_tournament(population, tournament_size):
    current_tournament_chromosomes = []
    for j in range(tournament_size):
        random_index = randint(0, len(population) - 1)
        current_tournament_chromosomes.append(population[random_index])
    winner_state = current_tournament_chromosomes[0]
    for state in current_tournament_chromosomes:
        if state.evaluate_value() > winner_state.evaluate_value():
            winner_state = state
    return winner_state


# perform crossover on parents to create new generation's population
def new_generations_population(population_size, parents):
    new_population = []
    parents_number = len(parents)
    for i in range(population_size):
        # generating new states from their parents (parent chromosomes)
        new_population.append(
            __crossover(parents[randint(0, parents_number) - 1], parents[randint(0, parents_number) - 1]))
    return new_population


# crossover function
# each chromosome is a state
def __crossover(first_chromosome, second_chromosome):
    child_chromosome = clone(first_chromosome)  # first initiate the child chromosome values
    child_chromosome_similarity_to_first_chromosome = randint(0, 10)  # child's possible similarity to first parent
    for i in range(len(child_chromosome.graphStructure)):  # or len(parents_chromosome.graphStructure)
        # skip parent's common value
        if first_chromosome.graphStructure[i].colour == second_chromosome.graphStructure[i].colour:
            continue
        # child must have some of non common value from both parent's
        else:
            winner_parent = __apply_child_similarity_dosage(child_chromosome_similarity_to_first_chromosome)
            if winner_parent == 1:
                continue
            else:
                child_chromosome.graphStructure[i].colour = second_chromosome.graphStructure[i].colour
    return child_chromosome


# choose current gene inheritance
def __apply_child_similarity_dosage(child_chromosome_similarity_to_first_chromosome):
    distributed_probability_array = []
    distributed_probability_array.extend([1] * child_chromosome_similarity_to_first_chromosome)
    distributed_probability_array.extend([2] * (10 - child_chromosome_similarity_to_first_chromosome))
    winner_parent_for_current_gene = distributed_probability_array[
        randint(0, len(distributed_probability_array) - 1)]
    return winner_parent_for_current_gene


# perform mutation on newly populated generation
def apply_mutation_on_new_generation(population, population_size, number_of_each_chromosomes_genome,
                                     mutated_genomes_number):
    while mutated_genomes_number > 0:
        # choose one state (chromosome) to mutate
        chosen_chromosome_to_mutate = population[randint(0, population_size) - 1]
        # choose one of it's genome to mutate
        genomes_to_mutate = chosen_chromosome_to_mutate.graphStructure[
            randint(0, number_of_each_chromosomes_genome) - 1]
        # my way to mutate colour number
        genomes_to_mutate.colour = (genomes_to_mutate.colour + randint(-10, 10)) % 3
        mutated_genomes_number -= 1


def find_avg_value_of_chromosomes(population, population_size):
    total_value = 0
    for state in population:
        total_value += state.evaluate_value()
    return total_value / population_size


# plot worst state value,best state value and avg value of each state per generation
def plot_generations_evaluated_value(best_chromosomes, avg_chromosomes, worst_chromosomes, details=""):
    plt.plot(best_chromosomes)
    plt.plot(avg_chromosomes)
    plt.plot(worst_chromosomes)
    plt.legend(["best chromosome's value ", "avg chromosomes' value ",
                "worst chromosome's value "], loc='lower right')
    plt.ylabel("evaluated values")
    plt.xlabel("generation")

    plt.figtext(x=0.4, y=0.4, s=details, fontsize=10)
    plt.show()
