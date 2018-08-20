import itertools
def bombs(M, F):
	M, F = int(M), int(F)
	gen = 0
	while (M, F) != (1, 1):
		if M == F or M < 1 or F < 1: return "impossible"
		if M > F:
			n = M//F - int(F == 1)
			M -= n*F
			gen += n
		elif M < F:
			n = F//M - int(M == 1)
			F -= n*M
			gen += n
	return str(gen)

print(bombs(4, 7))