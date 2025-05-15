import numpy as np
import random

def objective_function(position):
    return abs(3 * position[0] + 2 * position[1] + position[2] + position[3] - 34)

class Particle:
    def __init__(self, bounds):
        self.position = np.array([random.randint(bounds[0], bounds[1]) for _ in range(4)])
        self.velocity = np.random.uniform(-1, 1, 4)
        self.best_position = np.copy(self.position)
        self.best_value = objective_function(self.position)

    def update_velocity(self, global_best_position, w, c1, c2):
        r1, r2 = np.random.random(4), np.random.random(4)
        cognitive = c1 * r1 * (self.best_position - self.position)
        social = c2 * r2 * (global_best_position - self.position)
        self.velocity = w * self.velocity + cognitive + social

    def update_position(self, bounds):
        self.position = np.clip(self.position + self.velocity, bounds[0], bounds[1]).astype(int)
        value = objective_function(self.position)
        if value < self.best_value:
            self.best_value = value
            self.best_position = np.copy(self.position)

class PSO:
    def __init__(self, num_particles, num_generations, bounds, w, c1, c2):
        self.num_particles = num_particles
        self.num_generations = num_generations
        self.bounds = bounds
        self.swarm = [Particle(bounds) for _ in range(num_particles)]
        self.global_best_position = self.swarm[0].best_position
        self.global_best_value = self.swarm[0].best_value
        self.w, self.c1, self.c2 = w, c1, c2

    def optimize(self):
        for generation in range(self.num_generations):
            for particle in self.swarm:
                particle.update_velocity(self.global_best_position, self.w, self.c1, self.c2)
                particle.update_position(self.bounds)
                if particle.best_value < self.global_best_value:
                    self.global_best_value = particle.best_value
                    self.global_best_position = particle.best_position

            print(f"Generation {generation + 1}: Best Value = {self.global_best_value}, Best Position = {self.global_best_position}")
            if self.global_best_value == 0:
                break

        return self.global_best_position, self.global_best_value

# Tham số của PSO
pso = PSO(10, 100, [1, 20], 0.7, 1.5, 1.5)
best_position, best_value = pso.optimize()

print("\nBest Solution:")
print("Position (x, y, z, q):", best_position)
print("Objective Value:", best_value)