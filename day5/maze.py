import test

def read_maze(file):
	"""
	Read maze from text to list.
	"""
	maze = []
	with open(file, 'r') as f:
		for line in f:
			maze.append(int(line[:-1]))
	return maze

def steps_to_exit(arr):
	"""
	Return the number of steps required to exit the maze.
	"""
	step = 0
	pos = 0
	while True:
		try:
			offset = arr[pos]
			arr[pos] += 1
			pos += offset
			step += 1
		except IndexError:
			return step, arr

def steps_to_exit_strange(arr):
	"""
	Return the number of steps required to exit the maze, offsets increase
	or decrease more strangely than before!
	"""
	step = 0
	pos = 0
	while True:
		try:
			offset = arr[pos]
			if offset >= 3:
				arr[pos] -= 1
			else:
				arr[pos] += 1
			pos += offset
			step += 1
		except IndexError:
			return step, arr

INPUT_FILE = 'maze.txt'

if __name__ == '__main__':
	print(steps_to_exit(read_maze(INPUT_FILE))[0])
	print(steps_to_exit_strange(read_maze(INPUT_FILE))[0])
