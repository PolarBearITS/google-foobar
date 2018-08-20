import operator
def roundness(n):
	r = 0
	while n % 2 == 0 and n > 0:
		n >>= 1
		r += 1
	return r

def fuel(n):
	if n == 1: return 0
	rl = [roundness(n+i) for i in range(-1, 2)]
	index, r = max(enumerate(rl, -1), key=operator.itemgetter(1))
	if n == 3: index = -1
	if index != 0: 
		return 1 + fuel(n + index)
	return r + fuel(n // (2**r))
print(fuel(10**309))