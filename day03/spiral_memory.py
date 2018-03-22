import test

def spiral_distance(n, debug=None):
	"""
	Return the distance of the nth element in the spiral list from the center.
	"""
	val = 1
	x, y = (0, 0)

	if debug: print((x, y), val)

	spiral = 0
	while val < n:
		# Next outer concentric spiral
		spiral += 1

		# Move right
		while x < spiral and val < n:
			x += 1
			val += 1
			if debug: print((x, y), val)

		# Move up
		while y < spiral and val < n:
			y += 1
			val += 1
			if debug: print((x, y), val)

		# Move left
		while x > -spiral and val < n:
			x -= 1
			val += 1
			if debug: print((x, y), val)

		# Move down
		while y > -spiral and val < n:
			y -= 1
			val += 1
			if debug: print((x, y), val)

		# Move right
		while x < spiral and val < n:
			x += 1
			val += 1
			if debug: print((x, y), val)

	return abs(x) + abs(y)

def nearest_neighbours(arr, coords):
	"""
	Return the values of nearest neighbours in a dictionary with keys
	corresponding to xy co-ordinates.
	"""
	x0, y0 = coords

	vals = []
	for (x1, y1) in arr:
		if abs(x1 - x0) <= 1 and abs(y1 - y0) <= 1:
			vals.append(arr[x1, y1])

	return vals

def spiral_sum(max_val, debug=None):
	"""
	Return the first value in the spiral sum stress test that is greater than
	max_val.
	"""
	val = 1
	x, y = (0, 0)
	arr = {(x, y): val}

	if debug: print((x, y), arr)

	spiral = 0
	while val < max_val:
		# Next outer concentric spiral
		spiral += 1

		# Move right
		while x < spiral and val < max_val:
			x += 1
			val = sum(nearest_neighbours(arr, (x, y)))
			if debug: print(nearest_neighbours(arr, (x, y)))
			arr[x, y] = val
			if debug: print((x, y), arr)

		# Move up
		while y < spiral and val < max_val:
			y += 1
			val = sum(nearest_neighbours(arr, (x, y)))
			if debug: print(nearest_neighbours(arr, (x, y)))
			arr[x, y] = val
			if debug: print((x, y), arr)

		# Move left
		while x > -spiral and val < max_val:
			x -= 1
			val = sum(nearest_neighbours(arr, (x, y)))
			if debug: print(nearest_neighbours(arr, (x, y)))
			arr[x, y] = val
			if debug: print((x, y), arr)

		# Move down
		while y > -spiral and val < max_val:
			y -= 1
			val = sum(nearest_neighbours(arr, (x, y)))
			if debug: print(nearest_neighbours(arr, (x, y)))
			arr[x, y] = val
			if debug: print((x, y), arr)

		# Move right
		while x < spiral and val < max_val:
			x += 1
			val = sum(nearest_neighbours(arr, (x, y)))
			if debug: print(nearest_neighbours(arr, (x, y)))
			arr[x, y] = val
			if debug: print((x, y), arr)

	return arr[x, y]

def plot_spiral(arr):
	"""
	Plot the spiral array dictionary
	"""
	y_prev = None
	result = [[]]
	for (x, y) in sorted(arr, key=lambda x: (-x[1], x[0])):
		if y_prev is not None and y != y_prev:
			result.append([])
			print()
		result[-1].append(arr[x, y])
		print(arr[x, y], end=' ')
		y_prev = y
	return result

INPUT = 361527

if __name__ == '__main__':
	print(spiral_distance(INPUT))
	print(spiral_sum(INPUT))
