import helix.helix as hlx
import numpy as np

def fitness(dna):
	return abs(42 - ((dna[0] * dna[1]) * 100)) / 100

darwin = hlx.Genetic(2, 10, children = False, mutation = True)
darwin.evolve(fitness, 20)
