import helix as hlx
import numpy as np

def fitness(dna):
	return abs(52 - ((dna[0] * dna[1]) * 100)) / 100

darwin = hlx.Genetic(2, 5, children = False, mutation = True)
for gen in range(10):
	print(f"Generation:{gen}")
	for individual in darwin.population:
		darwin.fitness[np.where(darwin.population == individual)] = fitness(individual.dna)	
	darwin.generation()
	print(f"Best individual fitness score:{darwin.fitness[0]}")
	print(f"Median individual fitness score:{np.median(darwin.fitness)}")
	print(f"Worst individual fitness score:{darwin.fitness[darwin.individual_count - 1]}")

print("Evolution Complete!")
print(f"Here is the best individual:{darwin.population[0].dna[0] * 10} * {darwin.population[0].dna[1] * 10}")
print(f"it has a fitness score of {darwin.fitness[0]}")
print("++++++++++++++++++++++++++++++++++++++++++++++++")
