from reallocation import string_to_list, redistribute, reallocate

TEST_INPUT = '14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4'
TEST_OUTPUT = [14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]

def test_string_to_list():
	assert string_to_list(TEST_INPUT) == TEST_OUTPUT

def test_redistribute():
	assert redistribute([0, 2, 7, 0]) == [2, 4, 1, 2]
	assert redistribute([2, 4, 1, 2]) == [3, 1, 2, 3]
	assert redistribute([3, 1, 2, 3]) == [0, 2, 3, 4]
	assert redistribute([0, 2, 3, 4]) == [1, 3, 4, 1]
	assert redistribute([1, 3, 4, 1]) == [2, 4, 1, 2]

def test_reallocate():
	assert reallocate([0, 2, 7, 0]) == (5, 4)

test_string_to_list()
test_redistribute()
test_reallocate()
