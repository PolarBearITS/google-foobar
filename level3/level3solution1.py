def checksum(start, length):
	check = 0
	for cut in range(length):
		check ^= running_xor(start + length * cut, start + length*(cut+1) - cut)
	return check

def range_xor(a):
	n = a % 4
	if n == 0: return a
	if n == 1: return 1
	if n == 2: return a + 1
	if n == 3: return 0

def running_xor(a, b):
	return range_xor(a-1) ^ range_xor(b-1)