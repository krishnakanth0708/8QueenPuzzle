import random
import math
import numpy as np

def crossover(individual1, individual2):
    n = len(individual1)
    child1 = []
    child2 = []
    for i in range(n):
        child1.append(-1)
        child2.append(-1)
    cross_over_point = random.randint(1, n - 1)
    for i in range(cross_over_point):
        child1[i] = individual1[i]
        child2[i] = individual2[i]
    for i in range(cross_over_point, n):
        for j in range(n):
            if (not(individual2[(j + cross_over_point) % n] in child1)
            and (child1[i] == -1)):
                child1[i] = individual2[(j + cross_over_point) % n]
            if (not(individual1[(j + cross_over_point) % n] in child2)
            and (child2[i] == -1)):
                child2[i] = individual1[(j + cross_over_point) % n]
    return child1, child2

# mutation method
def mutation(individual):
    n = len(individual)
    rnd = random.random()
    mutation_prob = 0.2
    if rnd < mutation_prob:
        loci1 = random.randint(0, n - 1)
        loci2 = random.randint(0, n - 1)
        while loci2 == loci1:
            loci2 = random.randint(0, n - 1)
        result = copy.deepcopy(individual)
        result[loci1], result[loci2] = result[loci2], result[loci1]
        return result
    return individual

def generate_individual(n):
    result = list(range(1, n + 1))
    np.random.shuffle(result)
    return result

class EightQueen(object):

    def __init__(self, n ,pop_size):
        #initial population entered by user
        self.queens = []
        for i in range(pop_size):
            self.queens.append(generate_individual(n))

    def generate_population(self, random_selections=5):
        candid_parents = []
        candid_fitness = []
        #individuals from queens
        for i in range(random_selections):
            candid_parents.append(self.queens[random.randint(0, len(self.queens) - 1)])
            candid_fitness.append(fitness(candid_parents[i]))
        sorted_fitness = copy.deepcopy(candid_fitness)
        sorted_fitness.sort(reverse=True)
        parent1 = candid_parents[candid_fitness.index(sorted_fitness[0])]
        candid_parents.remove(parent1)
        parent2 = candid_parents[candid_fitness.index(sorted_fitness[1]) - 1]
        #crossover
        child1, child2 = crossover(parent1, parent2)
        child1 = mutation(child1)
        child2 = mutation(child2)
        if fitness(child1) > fitness(child2):
            child1, child2 = child2, child1
        child1_swaped = False
        child2_swaped = False
        for i in range(len(self.queens)):
            if ((fitness(self.queens[i]) > fitness(child1))
            and (child1_swaped is False)):
                self.queens[i] = child1
                child1_swaped = True
            if ((fitness(self.queens[i]) > fitness(child2))
            and (child2_swaped is False)):
                self.queens[i] = child2
                child2_swaped = True
                break

    def finished(self):
        for i in self.queens:
            if fitness(i) == 0:
                return [True, i]
        return [False]

    def start(self, random_selections=5):
        while not self.finished()[0]:
            self.generate_population(random_selections)
        final_state = self.finished()
        print(('Solution : ' + str(final_state[1])))


Input = """ 8-Queen Puzzle"""
print(Input)
n=8
initial_population=1000

Model = EightQueen(n=n,pop_size=initial_population)
Model.start()
