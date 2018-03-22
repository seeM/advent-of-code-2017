from maze import steps_to_exit, steps_to_exit_strange

def test_steps_to_exit():
	assert steps_to_exit([0, 3, 0, 1, -3])[0] == 5
	assert steps_to_exit([0, 3, 0, 1, -3])[1] == [2, 5, 0, 1, -2]

def test_steps_to_exit_strange():
	assert steps_to_exit_strange([0, 3, 0, 1, -3])[0] == 10
	assert steps_to_exit_strange([0, 3, 0, 1, -3])[1] == [2, 3, 2, 3, -1]

test_steps_to_exit()
test_steps_to_exit_strange()
