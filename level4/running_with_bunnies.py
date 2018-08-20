from collections import defaultdict
import itertools
# times = [
# 			[0, 1, 1, 1, 1], 
# 			[1, 0, 1, 1, 1], 
# 			[1, 1, 0, 1, 1], 
# 			[1, 1, 1, 0, 1], 
# 			[1, 1, 1, 1, 0]
# 		]
# time_limit = 3
# times = [
# 			[0, 2, 2, 2, -1], 
# 			[9, 0, 2, 2, -1], 
# 			[9, 3, 0, 2, -1], 
# 			[9, 3, 2, 0, -1],
# 			[9, 3, 2, 2, 0]
# 		]
# time_limit = 1
# times = [
# 			[0, 2, 2, 2, 2, 2, -1],
# 			[9, 0, 2, 2, 2, 2, -1],
# 			[9, 3, 0, 2, 2, 2, -1],
# 			[9, 3, 2, 0, 2, 2, -1],
# 			[9, 3, 2, 2, 0, 2, -1],
# 			[9, 3, 2, 2, 2, 0, -1],
# 			[9, 3, 2, 2, 2, 2, 0]
# ]
# time_limit = 1
times = [
	[0, 1, 1, 2, 1],
	[3, 0, 1, 1, 1],
	[1, 4, 0, 1, 5],
	[-2, 1, 2, 0, 1],
	[-5, 1, 7, 1, 0],
]
time_limit = 1

# def DFS(source, dest, graph, goal, route=[], length=0):
# 	routes = defaultdict(list)
# 	if route == []:
# 		route = [source]
# 	if route[-1] == dest:
# 		routes[length].append(route)
# 	else:
# 		for room, corridor in graph[source].items():
# 			if room not in route:
# 				for k, v in DFS(room, dest, graph, goal, route + [room], length+corridor).items():
# 					routes[k].extend(v)
# 	return routes

# def answer(times, time_limit):
# 	graph = defaultdict(dict)
# 	for node, edges in enumerate(times):
# 		for edge, weight in enumerate(edges):
# 			if edge != node:
# 				graph[node][edge] = weight
# 	print(graph)
# 	recursion(len(times), graph, [0], 0, 0, [])

# def recursion(depth, graph, path, previous_node, score, results):
# 	if len(path) <= depth:
# 		if score == 1:
# 			print(path, score)
# 		# print(path, score)
# 		for node in graph[previous_node]:
# 			recursion(depth, graph, path + [node], node, score + graph[previous_node][node], results)

def DFS(graph, depth, v, target, path=[]):
	results = []
	if depth == 0 and v == target:
		return [path + [v]]
	if len(path) < len(graph)+1:
		for u, weight in enumerate(graph[v]):
			if u != v:
				results.extend(DFS(graph, depth-weight, u, target, path + [v]))
	return results

def get_walk_set(walk, times):
	return set(walk) - {0, len(times)-1}

def answer(times, time_limit):
	walks = DFS(times, time_limit, 0, len(times)-1)
	walk_sets = [get_walk_set(w, times) for w in walks]
	max_walk = []
	max_set = set()
	max_sets = []
	max_len = len(max(walk_sets, key=len))
	for l, s in zip(walks, walk_sets):
		if len(s) == max_len:
			# print(l, len(l), len(max_walk), s, )
			max_sets.append(l)
			if (len(l) <= len(max_walk) or max_walk == []) and (sum(s) <= sum(max_set)) or max_set == set():
				print(l, s)
				max_walk = l.copy()
				max_set = s.copy()
	# print(max_sets)
	# print(max_walk)
	# print(max_set)
	return [x - 1 for x in max_set]

# print(DFS(time_limit, 0, len(times)-1, [], times))
a = answer(times, time_limit)
print(a)