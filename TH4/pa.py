import numpy as np
import random

def objective_function(chromosome):
    x, y, z, q = chromosome
    return abs(3 * x + 2 * y + z + q - 34)

def create_population(pop_size, bounds):
    return [np.random.randint(bounds[0], bounds[1] + 1, 4) for _ in range(pop_size)]

def selection(population, fitnesses, num_parents):
    sorted_indices = np.argsort(fitnesses)
    return [population[i] for i in sorted_indices[:num_parents]]

def crossover(parent1, parent2):
    point = np.random.randint(1, len(parent1))
    child1 = np.concatenate((parent1[:point], parent2[point:]))
    child2 = np.concatenate((parent2[:point], parent1[point:]))
    return child1, child2

def mutate(chromosome, bounds, mutation_rate):
    for i in range(len(chromosome)):
        if np.random.rand() < mutation_rate:
            chromosome[i] = np.random.randint(bounds[0], bounds[1] + 1)
    return chromosome

def genetic_algorithm(pop_size, bounds, mutation_rate, max_generation):
    population = create_population(pop_size, bounds)
    best_solution, best_fitness = None, float('inf')

    for gen in range(1, max_generation + 1):
        fitnesses = [objective_function(c) for c in population]

        min_fitness_idx = np.argmin(fitnesses)
        if fitnesses[min_fitness_idx] < best_fitness:
            best_fitness = fitnesses[min_fitness_idx]
            best_solution = population[min_fitness_idx]

        print(f"Generation {gen}: Best Fitness = {best_fitness}, Best Solution = {best_solution}")
        if best_fitness == 0:
            break

        num_parents = pop_size // 2 * 2
        parents = selection(population, fitnesses, num_parents)

        new_population = []
        for i in range(0, num_parents, 2):
            child1, child2 = crossover(parents[i], parents[i + 1])
            new_population.extend([child1, child2])

        population = [mutate(c, bounds, mutation_rate) for c in new_population]

    return best_solution, best_fitness

# Parameters
pop_size = 10
bounds = [1, 20]
mutation_rate = 0.1
max_generation = 1000

best_solution, best_fitness = genetic_algorithm(pop_size, bounds, mutation_rate, max_generation)

print("\nBest Solution:")
print("Position (x, y, z, q):", best_solution)
print("Objective Value:", best_fitness)