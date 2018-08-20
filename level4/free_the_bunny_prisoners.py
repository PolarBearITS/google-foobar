import itertools
import math
x = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 6, 7, 8], [0, 3, 4, 6, 7, 9], [1, 3, 5, 6, 8, 9], [2, 4, 5, 7, 8, 9]]

def ncr(n, k):
	f = math.factorial
	return f(n) // (f(k) * f(n-k))

def answer(num_buns, num_required):
	b = [[] for _ in range(num_buns)]
	for lock, indexes in enumerate(itertools.combinations(range(num_buns), num_buns-num_required+1)):
		for index in indexes:
			b[index].append(lock)
	return b

answer(5, 3)