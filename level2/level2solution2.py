import math

memo = {0:1, 1:1}
def fib(n):
	if n in memo:
		return memo[n]
	f = fib(n-2) + fib(n-1)
	memo[n] = f
	return f

def total_lambs(l):
	if l < 4:
		return 0
	i = 0
	while l >= fib(i):
		i += 1
	powers = []
	p = 0
	while l - sum(powers) >= 2**p:
		powers.append(2**p)
		p += 1
	if l - sum(powers) >= sum(powers[-2:]):
		powers.append(l - sum(powers))
	return (i-2) - len(powers)

print(total_lambs(10**9))