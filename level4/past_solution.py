def graph_output(room, exits, path, route, room_outputs={}):
	if room in room_outputs:
		return room_outputs[room], room_outputs
	if room in exits:
		room_outputs[room] = float('inf')
		print(room, exits)
		return float('inf'), room_outputs
	out = {i:r for i, r in enumerate(path[room]) if r != 0 and i not in route}
	total = 0
	for corridor in out:
		print(' '*len(route), '-', room, corridor)
		t, o = graph_output(corridor, exits, path, route + [corridor], room_outputs)
		n = min(t, out[corridor])
		total += n
		for k, v in o.items():
			if k not in room_outputs:
				room_outputs[k] = v
	room_outputs[room] = total
	return total, room_outputs

def answer(entrances, exits, path):
	bunnies = [0]*len(path)
	outputs = {}
	for e in entrances:
		t, o = graph_output(e, exits, path, [e])
		for k, v in o.items():
			if k not in outputs:
				outputs[k] = v
		bunnies[e] = outputs[e]
	# print(outputs)
	# quit()
	rooms = entrances[:]
	visited = []
	while rooms not in [exits, []]:
	# for _ in range(5):
		new_rooms = []
		for room in rooms:
			corridors = path[room]
			ordered_corridors = []
			for i, r in enumerate(corridors):
				if r != 0 and i not in visited + rooms:
					# print(i, corridors[i])
					ordered_corridors.append(i)
			# print(ordered_corridors, [outputs[x] for x in ordered_corridors], sorted(ordered_corridors, key=lambda x: outputs[x], reverse=True))
			try:
				ordered_corridors = sorted(ordered_corridors, key=lambda x: outputs[x], reverse=True)
			except:
				print(outputs)
				# print(room, ordered_corridors)
				raise
			for c in ordered_corridors:
				if bunnies[room] < corridors[c]:
					bunnies[c] += bunnies[room]
					bunnies[room] = 0
				else:
					bunnies[room] -= corridors[c]
					bunnies[c] += corridors[c]
				if c not in new_rooms + exits:
					new_rooms.append(c)
				if room not in visited + exits:
					visited.append(room)
		rooms = new_rooms[:]
	return sum(bunnies[exit] for exit in exits)

entrances = [7]
exits =  [4]
path = [[41, 0, 20, 95, 0, 8, 18, 0],
		[0, 0, 25, 0, 4, 0, 0, 0],
		[0, 87, 0, 7, 0, 0, 0, 0],
		[67, 47, 0, 26, 0, 0, 0, 0],
		[81, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 20, 0, 0, 0],
		[0, 0, 0, 0, 0, 77, 0, 0],
		[0, 0, 0, 56, 0, 0, 0, 0]]

b = answer(entrances, exits, path)
print(b)
for e in entrances:
	print(e, graph_output(e, exits, path, [e]))
"""
import random
while True:
	size = random.randint(4, 9)
	n = random.randint(1, size//2)
	ee = []
	while len(ee) < n*2:
		x = random.randint(0, size-1)
		while x in ee:
			x = random.randint(0, size-1)
		ee.append(x)
	entrances = ee[:n]
	exits = ee[n:]
	path = []
	for i in range(size):
		row = []
		for j in range(size):
			if random.randint(1, 5) == 1:
				row.append(random.randint(1, 100))
			else:
				row.append(0)
		path.append(row)
	# print(size, entrances, exits)
	# for row in path:
	# 	print(row)
	try:
		b = answer(entrances, exits, path)
		# print(b)
		# print()
	except Exception as e:
		print(f'# {size}\nentrances = {entrances}\nexits =  {exits}\npath = [')
		for row in path:
			print(f'{row},')
		print(']\n# FAILED', repr(e), end='\n\n')
		for entrance in entrances:
			print(entrance, graph_output(entrance, exits, path, [entrances]))
		break
	"""#"""