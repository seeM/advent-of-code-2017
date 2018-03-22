from checksum import (
	string_to_list,
	range_,
	checksum,
	divisibles,
	checksum_divisible
)

TEST_STRING1 = "5\t1\t9\t5\n7\t5\t3\n2\t4\t6\t8"
TEST_LIST1 = [
    [5, 1, 9, 5],
    [7, 5, 3],
    [2, 4, 6, 8]
]

TEST_STRING2 = "5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5"
TEST_LIST2 = [
	[5, 9, 2, 8],
	[9, 4, 7, 3],
	[3, 8, 6, 5]
]

def test_string_to_list():
    assert string_to_list(TEST_STRING1) == TEST_LIST1

def test_range_():
	assert range_(TEST_LIST1[0]) == 8
	assert range_(TEST_LIST1[1]) == 4
	assert range_(TEST_LIST1[2]) == 6

def test_checksum():
    assert checksum(TEST_STRING1) == 18

def test_divisibles():
	assert divisibles(TEST_LIST2[0]) == 4
	assert divisibles(TEST_LIST2[1]) == 3
	assert divisibles(TEST_LIST2[2]) == 2

def test_checksum_divisible():
	assert checksum_divisible(TEST_STRING2) == 9

test_string_to_list()
test_range_()
test_checksum()
test_divisibles()
test_checksum_divisible()
