from collections import defaultdict
import math
def graph(entrances, exits, path):
	flow = defaultdict(dict)
	for room in range(-1, len(path) + 1):
		flow[room] = defaultdict(int)

	#supersource
	for entrance in entrances:
		flow[-1][entrance] = [0, math.inf] #[0, sum(path[entrance])]

	#network
	for node, corridors in enumerate(path):
		for i, c in enumerate(corridors):
			if c != 0:
				flow[node][i] = [0, c]

	#supersink
	for exit in exits:
		flow[exit][len(path)] = [0, math.inf] #[0, sum(path[i][exit] for i in range(len(path)))]
	return flow

def print_graph(d):
	for k, v in d.items():
		print(f'\t{k}: {{')
		for i, j in v.items():
			print(f'\t\t{i}: {j},')
		print('\t},')

def answer(entrances, exits, path):
	g = graph(entrances, exits, path)
	print_graph(g)

entrances = [0, 1]
exits = [4, 5]
path = [[0, 0, 4, 6, 0, 0], 
		[0, 0, 5, 2, 0, 0], 
		[0, 0, 0, 0, 4, 4], 
		[0, 0, 0, 0, 6, 6], 
		[0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0]]
answer(entrances, exits, path)