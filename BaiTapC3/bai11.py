import random

def fitness(candidate, password):
    return sum(c1 == c2 for c1, c2 in zip(candidate, password))

def crossover(parent1, parent2):
    point = random.randint(0, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

def mutate(candidate, mutation_rate=0.1):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    return ''.join(
        c if random.random() > mutation_rate else random.choice(chars)
        for c in candidate
    )

def genetic_algorithm(password, population_size=100, generations=1000):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    length = len(password)
    population = [''.join(random.choices(chars, k=length)) for _ in range(population_size)]
    for generation in range(generations):
        population = sorted(population, key=lambda x: -fitness(x, password))
        best_candidate = population[0]
        correct_chars = fitness(best_candidate, password)
        print(f"Generation {generation}: Best candidate = {best_candidate}, Correct chars = {correct_chars}")
        
        if correct_chars == length:
            return best_candidate, generation
        new_population = population[:population_size // 2]
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(new_population[:population_size // 4], 2)
            child = mutate(crossover(parent1, parent2))
            new_population.append(child)
        population = new_population
    return population[0], generations

# Chạy GA
password = "hoilamgi"
result, gen = genetic_algorithm(password)
print(f"Mật khẩu tìm được: {result} trong {gen} thế hệ")

import random

def fitness_pso(candidate, password):
    return sum(c1 == c2 for c1, c2 in zip(candidate, password))

def pso(password, population_size=100, iterations=1000):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    length = len(password)
    particles = [''.join(random.choices(chars, k=length)) for _ in range(population_size)]
    velocities = [[random.choice([-1, 1]) for _ in range(length)] for _ in range(population_size)]
    personal_best = particles[:]
    global_best = max(particles, key=lambda x: fitness_pso(x, password))
    for iteration in range(iterations):
        for i in range(population_size):
            particles[i] = ''.join(
                chars[(chars.index(c) + v) % len(chars)] if c in chars else c
                for c, v in zip(particles[i], velocities[i])
            )
            velocities[i] = [
                random.choice([-1, 0, 1]) if random.random() < 0.5 else 0
                for _ in range(length)
            ]
            if fitness_pso(particles[i], password) > fitness_pso(personal_best[i], password):
                personal_best[i] = particles[i]
        global_best = max(personal_best, key=lambda x: fitness_pso(x, password))
        correct_chars = fitness_pso(global_best, password)
        print(f"Iteration {iteration}: Best candidate = {global_best}, Correct chars = {correct_chars}")
        
        if correct_chars == length:
            return global_best, iteration
    return global_best, iterations

# Chạy PSO
password = "hoilamgi"
result, iter = pso(password)
print(f"Mật khẩu tìm được: {result} trong {iter} lần lặp")
