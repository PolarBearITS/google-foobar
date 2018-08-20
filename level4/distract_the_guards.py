import itertools
import math
from collections import defaultdict

def is_forever(x, y):
	if x > y:
		x, y = y, x
	z, r = divmod(y, x)
	if r:
		return True
	return bool(z & (z+1))

def answer(banana_list):
	infinites = defaultdict(list)
	for indexes in itertools.combinations(range(len(banana_list)), 2):
		pair = [banana_list[i] for i in indexes]
		print(pair, is_forever(*pair))
		if is_forever(*pair):
			x, y = indexes
			infinites[x].append(y)
			infinites[y].append(x)
	print(infinites)

answer([1, 7, 3, 21, 13, 19])