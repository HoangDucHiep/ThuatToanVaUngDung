import numpy as np
import random

def objective_function(chromosome):
    x, y, z, q = chromosome
    return abs(3*x + 2*y + z + q - 34)

# create random population
def create_population(pop_size, bounds):
    return [np.random.randint(bounds[0], bounds[1]+1, 4) for _ in range(pop_size)]  

# selection based on objective function
def selection(population, fitnesses, num_parents):
    parents = []
    sorted_indices = np.argsort(fitnesses)  # sort by fitness
    for i in range(num_parents):
        parents.append(population[sorted_indices[i]])
    return parents

# crossover
def crossover(parent1, parent2):
    crossover_point = np.random.randint(1, len(parent1))
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2

# mutation
def mutate(chromosome, bounds, mutation_rate):
    for i in range(len(chromosome)):
        odd = np.random.rand()
        if odd < mutation_rate:
            chromosome[i] = np.random.randint(bounds[0], bounds[1]+1)
            print(f'\tmutant at {chromosome[i]} with odd {odd}')
    return chromosome

# Generic Alg
def genetic_algorithm(pop_size, bounds, mutation_rate, max_generation):
    population = create_population(pop_size, bounds)
    best_solution = None
    best_fitness = float('inf')
    gen = 1
    
    for lo in range(max_generation):
    
        if best_fitness == 0:
            break
        
        fitnesses = np.array([objective_function(chromosome) for chromosome in population])

        min_fitness_idx = np.argmin(fitnesses)
        if fitnesses[min_fitness_idx] < best_fitness:
            best_fitness = fitnesses[min_fitness_idx]
            best_solution = population[min_fitness_idx]
            
        print(f"Generation {gen} : Best Fitness = {best_fitness}, Best Solution = {best_solution}")
        gen += 1
        
        num_parents = pop_size // 2 * 2 
        parents = selection(population, fitnesses, num_parents)
        new_population = []
        for i in range(0, num_parents, 2):
            parent1 = parents[i]
            parent2 = parents[i + 1]
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([child1, child2])
            

        new_population = [mutate(chromosome, bounds, mutation_rate) for chromosome in new_population]
        population = new_population
    
    return best_solution, best_fitness


pop_size = 10
bounds = [1, 20]
mutation_rate = 0.1
max_generation = 1000
best_solution, best_fitness = genetic_algorithm(pop_size, bounds, mutation_rate, max_generation)

print("\nBest Solution:")
print("Position (x, y, z, q):", best_solution)
print("Objective Value:", best_fitness)
