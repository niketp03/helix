import numpy as np

class Genetic:

	def __init__(self, individual_size, individual_count,
		mutation = True, mutation_rate = 0.01, mutation_factor = 0.01, children = True, child_mutant_factor = 0.1, immigrants = 1):
		self.individual_size = individual_size
		self.individual_count =individual_count
		self.mutation = mutation
		self.mutation_rate = mutation_rate
		self.mutation_factor = mutation_factor
		self.children = children
		self.child_mutant_factor = child_mutant_factor
		self.immigrants = immigrants
		self.population = np.empty((individual_count,), dtype=object)
		for i in range(individual_count):	
			self.population[i-1] = Individual(individual_size)
		self.fitness = np.zeros((individual_count,))

	def generation(self):
		self.population = self.population[self.fitness.argsort()]
		toKill = np.array(range(int(self.individual_count/2), self.individual_count))
		toSurvive = np.array(range(0,int(self.individual_count/2)))
		
		if self.children:
			for i in toKill:
					index = np.random.choice(toSurvive)
					self.population[i] = Individual(self.individual_size)
					self.population[i].set_dna(self.population[index].dna)
					self.population[i].mutate(1, self.child_mutant_factor)

		else:
			for i in toKill:
				self.population[i] = Individual(self.individual_size)
		if self.mutation:
			for i in range(self.individual_count):
				self.population[i].mutate(self.mutation_rate, self.mutation_factor)

	def evolve(self, fit_func, gens):
		for gen in range(gens):
			print(f"Generation:{gen}")
			for individual in self.population:
				self.fitness[np.where(self.population == individual)] = fit_func(individual.dna)	
			self.generation()
			print(f"Best individual fitness score:{self.fitness[0]}")
			print(f"Median individual fitness score:{np.median(self.fitness)}")
			print(f"Worst individual fitness score:{self.fitness[self.individual_count - 1]}")

		print("Evolution Complete!")
		print(f"Here is the best individual:{self.population[0].dna[0] * 10} * {self.population[0].dna[1] * 10}")
		print(f"it has a fitness score of {self.fitness[0]}")
		print("++++++++++++++++++++++++++++++++++++++++++++++++")


class Individual:

	def __init__(self, size):
		self.dna = np.zeros(size)
		for i in range(size):
			self.dna[i] = np.random.random()

	def sigmoid(x):	
		return 1/(1+np.exp(-x))

	def mutate(self, mr, mf):
		if np.random.random() < mr:
			for i in range(len(self.dna)):
				self.dna[i] *= ((np.tanh(np.random.uniform(-1,1)) * mf) + 1)
				self.dna[i] = 1/(1+np.exp(-(self.dna[i])))

	def set_dna(self, toSet):
		self.dna = toSet

def fitness(dna):
	return abs(42 - ((dna[0] * dna[1]) * 100)) / 100

darwin = Genetic(2, 10, children = True, mutation = True)
darwin.evolve(fitness, 200)