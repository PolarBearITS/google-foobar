def connection(n, route=[]):
	c = []
	for i in [1, 2]:
		for j in [-1, 1]:
			for k in [-1, 1]:
				g = n + 8*i*j + k*(3-i)
				if -1 < g < 64 and 0 < abs(n%8 - g%8) < 3 and n//8 != g//8 and g not in route:
					c.append(g)
	return c

def path(src, dest, route=[]):
	if src == dest:
		return 0
	conn = connection(src, route + [src])
	if dest in conn:
		return 1
	else:
		route_lens = []
		for c in conn:
			if len(route) < 5:
				rl = path(c, dest, route + [src])
				if rl != None:
					route_lens.append(1 + rl)
		if route_lens != []:
			return min(route_lens)
