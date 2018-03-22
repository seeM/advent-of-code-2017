from typing import List, NamedTuple, Callable, Dict
from operator import add, sub, lt, le, eq, ne, ge, gt
from collections import defaultdict

class Operation(NamedTuple):
	register: str
	operator: Callable[[int, int], int]
	value: int

class Condition(NamedTuple):
	register: str
	comparator: Callable[[int, int], bool]
	value: int

class Instruction(NamedTuple):
	operation: Operation
	condition: Condition

def read_instruction(instruction: str) -> Instruction:
	operation, condition = instruction.split(' if ')

	register, operator, value = operation.split()
	operator = add if operator == 'inc' else sub
	value = int(value)

	c_register, comparator, c_value = condition.split()
	if comparator == '<':
		comparator = lt
	elif comparator == '<=':
		comparator = le
	elif comparator == '==':
		comparator = eq
	elif comparator == '!=':
		comparator = ne
	elif comparator == '>=':
		comparator = ge
	elif comparator == '>':
		comparator = gt
	c_value = int(c_value)

	operation = Operation(register, operator, value)
	condition = Condition(c_register, comparator, c_value)
	return Instruction(operation, condition)

def find_largest(instructions: List[Instruction]) -> int:
	registers = defaultdict(int)
	for instruction in instructions:
		# First evaluate the condition
		condition = instruction.condition
		is_condition = condition.comparator(registers[condition.register],
		                                    condition.value)
		if is_condition:
			# Then perform the operation
			operation = instruction.operation
			registers[operation.register] = operation.operator(
				registers[operation.register], operation.value)
	return max(registers.values())

def find_largest_ever(instructions: List[Instruction]) -> int:
	largests = []
	registers = defaultdict(int)
	for instruction in instructions:
		# First evaluate the condition
		condition = instruction.condition
		is_condition = condition.comparator(registers[condition.register],
		                                    condition.value)
		if is_condition:
			# Then perform the operation
			operation = instruction.operation
			registers[operation.register] = operation.operator(
				registers[operation.register], operation.value)
		largests.append(max(registers.values()))
	return max(largests)

TEST_INPUT = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

TEST_INSTRUCTIONS = [read_instruction(line) for line in TEST_INPUT.split('\n')]

assert find_largest(TEST_INSTRUCTIONS) == 1

assert find_largest_ever(TEST_INSTRUCTIONS) == 10

if __name__ == '__main__':
	with open('input.txt', 'r') as f:
		instructions = [read_instruction(line) for line in f]
	print(find_largest(instructions))
	print(find_largest_ever(instructions))
