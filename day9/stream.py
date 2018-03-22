"""
You can't have nested garbage. Once you're open a piece of garbage,
you're just looking for the end symbol '>'.

You can have nested groups.

You have two states: is_garbage and is_cancel.
You can be in both states concurrently.
If you're in is_cancel, you ignore the next symbol and return to not is_cancel.
If you're in is_garbage, you still check for is_cancel, but you ignore
  everything else except the exit_garbage symbol.
"""
from typing import List

def compute_groups(stream: str) -> List[int]:
	groups = []
	curr_group_score = 0
	is_garbage = False
	is_cancel = False
	for char in stream:
		if is_cancel:
			is_cancel = False		
		elif char == '!':
			is_cancel = True
		elif is_garbage:
			if char == '>':
				is_garbage = False
		elif char == '<':
			is_garbage = True
		elif char == '{':
			curr_group_score += 1            # one layer deeper
			groups.append(curr_group_score)  # open a group
		elif char == '}':
			curr_group_score -= 1            # one layer shallower

	assert curr_group_score == 0, 'Invalid stream, mismatched group brackets.'

	return groups

assert len(compute_groups('{}')) == 1
assert len(compute_groups('{{{}}}')) == 3
assert len(compute_groups('{{},{}}')) == 3
assert len(compute_groups('{{{},{},{{}}}}')) == 6
assert len(compute_groups('{<{},{},{{}}>}')) == 1
assert len(compute_groups('{<a>,<a>,<a>,<a>}')) == 1
assert len(compute_groups('{{<a>},{<a>},{<a>},{<a>}}')) == 5
assert len(compute_groups('{{<!>},{<!>},{<!>},{<a>}}')) == 2

assert sum(compute_groups('{}')) == 1
assert sum(compute_groups('{{{}}}')) == 6
assert sum(compute_groups('{{},{}}')) == 5
assert sum(compute_groups('{{{},{},{{}}}}')) == 16
assert sum(compute_groups('{<a>,<a>,<a>,<a>}')) == 1
assert sum(compute_groups('{{<ab>},{<ab>},{<ab>},{<ab>}}')) == 9
assert sum(compute_groups('{{<!!>},{<!!>},{<!!>},{<!!>}}')) == 9
assert sum(compute_groups('{{<a!>},{<a!>},{<a!>},{<ab>}}')) == 3

def compute_garbage(stream: str) -> List[int]:
	garbage = []
	curr_garbage = 0
	curr_group_score = 0
	is_garbage = False
	is_cancel = False
	for char in stream:
		if is_cancel:
			is_cancel = False		
		elif char == '!':
			is_cancel = True
		elif is_garbage:
			if char == '>':
				is_garbage = False
				garbage.append(curr_garbage)
				curr_garbage = 0
			else:
				curr_garbage += 1
		elif char == '<':
			is_garbage = True
		elif char == '{':
			curr_group_score += 1            # one layer deeper
		elif char == '}':
			curr_group_score -= 1            # one layer shallower

	assert curr_group_score == 0, 'Invalid stream, mismatched group brackets.'

	return garbage


assert sum(compute_garbage('<>')) == 0
assert sum(compute_garbage('<random characters>')) == 17
assert sum(compute_garbage('<<<<>')) == 3
assert sum(compute_garbage('<{!>}>')) == 2
assert sum(compute_garbage('<!!>')) == 0
assert sum(compute_garbage('<!!!>>')) == 0
assert sum(compute_garbage('<{o"i!a,<{i<a>')) == 10

assert sum(compute_garbage('{<a>,<a>,<a>,<a>}')) == 4
assert sum(compute_garbage('{{<ab>},{<ab>},{<ab>},{<ab>}}')) == 8
assert sum(compute_garbage('{{<!!>},{<!!>},{<!!>},{<!!>}}')) == 0
assert sum(compute_garbage('{{<a!>},{<a!>},{<a!>},{<ab>}}')) == 17

if __name__ == '__main__':
	with open('input.txt', 'r') as f:
		stream = f.read()
	print(sum(compute_groups(stream)))
	print(sum(compute_garbage(stream)))
