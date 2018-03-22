from typing import List, NamedTuple
from collections import Counter

class Program():
	"""
	A program has a name, weight, children, and a parent.
	"""
	def __init__(self, name, weight, children):
		self.name = name
		self.weight = weight
		self.children = children
		self.parent = ''

		if len(children) == 0:
			self.total_weight = weight
		else:
			self.total_weight = None

	def __repr__(self):
		return f'Tower({self.name}, {self.weight}, {self.children}, ' \
		       + f'{self.parent})'

def read_tower(file):
	"""
	Read tower from text file to ...
	"""
	with open(file, 'r') as f:
		tower = {}
		for line in f:
			splitted = line[:-1].split(' ')
			name = splitted[0]
			weight = int(splitted[1][1:-1])
			children = [splitted[i].replace(',', '')
			            for i in range(3, len(splitted))]
			tower[name] = Program(name, weight, children)
	return tower

def set_parents(tower):
	"""
	Set the parent of each program in a tower.
	"""
	for key in tower:
		for child in tower[key].children:
			tower[child].parent = tower[key].name
	return tower

def get_bottom(tower):
	"""
	Get the bottom program, i.e., the program with no parent.
	"""
	for key in tower:
		if len(tower[key].parent) == 0:
			return tower[key].name

def solve_towers(file):
	"""
	Read tower from string, set parents, return bottom tower.
	"""
	return get_bottom(set_parents(read_tower(file)))

# def compare_weights(tower, name):
# 	weights = []
# 	for child in tower[name].children:
# 		weights.append(compute_weights(tower, child))
# 	return weights

# def compute_weights(tower, name):
# 	program = tower[name]
# 	if len(program.children):
# 		weight = program.weight
# 		for child in program.children:
# 			curr_weight = compute_weights(tower, child)
# 			if prev_weight != curr_weight:
# 				print(child)
# 			weight += curr_weight
# 			prev_weight = curr_weight
# 	else:
# 		weight = program.weight
# 	return weight

# def test(tower, name):
# 	weights = []
# 	if len(tower[name].children) > 0:
# 		for child in tower[name].children:
# 			weights.append(test(tower, child))
# 	return tower[name].weight, weights

# def test2(tower, name):
# 	weights = test(tower, name)
# 	totals = []
# 	for x in weights:



# Start at the bottom...
#   Go to the first child.
#   Start summing weights, start with the first child
#     Go to the first child (of this child)
#     Start summing weights, start with the first child
#     ... repeat until we reach the end of the tree ...
#     Sum weights of all children, and ensure that the weights are equal.
#   


# def find_error(tower, bottom):
# 	"""
# 	Find the tower with incorrect weight.
# 	"""
# 	for child in tower[bottom].children:
# 		weight = 0
# 		name = child
# 		while True:
# 			for child in tower[name].children:

INPUT_FILE = 'input.txt'
# INPUT_FILE = 'test_input.txt'

tower = set_parents(read_tower(INPUT_FILE))

def correct_weights(tower):
	unbalanced_towers = []
	weights = {}

	def compute_weights(tower, name):
		program = tower[name]

		if len(program.children):
			subweights = { child : compute_weights(tower, child)
			               for child in program.children }

			distinct_weights = set(subweights.values())
			num_distinct_weights = len(distinct_weights)
			if num_distinct_weights > 1:
				unbalanced_towers.append(subweights)

			weights[name] = program.weight + sum(subweights.values())
		else:
			weights[name] = program.weight

		return weights[name]

	bottom = get_bottom(tower)
	compute_weights(tower, bottom)

	print(unbalanced_towers)

	# unbalanced = unbalanced_towers[0]
	# print(unbalanced)
	# inverted = {}
	# for name, weight in unbalanced.items():
	# 	if weight in inverted:
	# 		inverted[weight].append(name)
	# 	else:
	# 		inverted[weight] = [name]
	# print(inverted)

	# error = [{names[0] : weight} for weight, names in inverted.items()
	#          if len(names) == 1][0]

	# # other_weight = 
	# print(error)


correct_weights(tower)

# print(weights)

# if __name__ == '__main__':
# 	# print(solve_towers(INPUT_FILE))
# 	tower = set_parents(read_tower(INPUT_FILE))
# 	bottom = get_bottom(tower)
# 	# compute_weights(tower, bottom)
# 	# print(compare_weights(tower, bottom))
# 	print(test2(tower, bottom))
# 	# print(tower[bottom].children)

# Answer is 1458