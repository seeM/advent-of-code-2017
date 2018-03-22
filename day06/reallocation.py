import test

def string_to_list(string):
	"""
	Convert tab-delimited string to list of integers.
	"""
	return [int(x) for x in string.split('\t')]

def redistribute(arr):
	"""
	Evenly redistribute blocks in the largest bank.

	E.g.,

	arr = [0, 2, 7, 0]
	returns: [2, 4, 1, 2]
	"""
	len_arr = len(arr)
	n = arr.index(max(arr))  # ties settled by taking first largest

	pos = n + 1
	for i in range(arr[n]):
		if pos >= len_arr:
			pos = 0
		arr[n] -= 1
		arr[pos] += 1
		pos += 1

	return arr

def list_to_string(arr):
	"""
	Convert a list of integers (0-9) to a string.
	"""
	return ''.join([str(x) for x in arr])

def reallocate(arr):
	"""
	Repeatedly redistribute blocks in the largest bank until an old state
	has been revisted.
	"""
	states = {}
	step = 0
	while True:
		arr = redistribute(arr)
		arr_str = list_to_string(arr)
		step += 1
		if arr_str in states:
			cycle = step - states[arr_str]
			return step, cycle
		else:
			states[arr_str] = step

INPUT = '14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4'

if __name__ == '__main__':
	print(reallocate(string_to_list(INPUT))[0])
	print(reallocate(string_to_list(INPUT))[1])
