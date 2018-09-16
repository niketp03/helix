import numpy as np

class Genetic:

	def __init__(self, individual_size, individual_count,
		mutation = True, mutation_rate = 0.1, mutation_factor = 0.001, children = True, child_mutant_factor = 0.001, immigrants = 1):
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
		toKill = np.array(range(int(self.individual_count/2)+1, self.individual_count))
		toSurvive = np.array(range(0,int(self.individual_count/2)+1))
		
		if self.children:
			for i in toKill:
				if i !=6:
					index = np.random.choice(toSurvive)
					self.population[i] = Individual(self.individual_size)
					self.population[i].set_dna(self.population[index].dna)
					self.population[i].mutate(1, self.child_mutant_factor)
				else:
					self.population[i] = Individual(self.individual_size)

		else:
			for i in toKill:
				self.population[i] = Individual(self.individual_size)
		if self.mutation:
			print("yeet")
			for i in range(self.individual_count):
				self.population[i].mutate(self.mutation_rate, self.mutation_factor)

class Individual:

	def __init__(self, size):
		self.dna = np.zeros(size)
		for i in range(size):
			self.dna[i] = np.random.random()

	def mutate(self, mr, mf):
		if np.random.random() < mr:
			for i in range(len(self.dna)):
				self.dna[i] *= ((np.random.uniform(-1,1) * mf) + 1)

	def set_dna(self, toSet):
		self.dna = toSet
