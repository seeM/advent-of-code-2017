from spiral_memory import spiral_distance, spiral_sum

def test_spiral_distance():
	assert spiral_distance(1) == 0
	assert spiral_distance(12) == 3
	assert spiral_distance(23) == 2
	assert spiral_distance(1024) == 31

def test_spiral_sum():
	assert spiral_sum(1) == 1
	assert spiral_sum(12) == 23
	assert spiral_sum(800) == 806

test_spiral_distance()
test_spiral_sum()
