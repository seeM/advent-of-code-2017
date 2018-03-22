from typing import List, Iterator

def pinch_twist(arr: List[int], pos: int, length: int) -> List[int]:
	arr_size = len(arr)

	assert length <= arr_size, "Lengths larger than the size of the list are invalid."
	
	# select the subarray (with circular list)
	if pos + length > arr_size:
		excess = pos + length - arr_size
		subarray = arr[pos:] + arr[:excess]
	else:
		subarray = arr[pos:(pos + length)]

	# twist it
	twisted = subarray[::-1]

	# combine with the remaining array elements
	if pos + length > arr_size:
		result = twisted[-excess:] + arr[excess:pos] + twisted[:-excess]
	else:
		result = arr[:pos] + twisted + arr[(pos + length):]

	return result

def knot_hash(arr_size: int, lengths: List[int]) -> int:
	arr = [i for i in range(arr_size)]

	skip_size = 0
	pos = 0
	for length in lengths:
		# print(pos, skip_size, length, arr, end=' ')
		arr = pinch_twist(arr, pos, length)
		# print(arr)
		pos = (pos + length + skip_size) % arr_size
		skip_size += 1

	return arr[0] * arr[1]

TEST_LENGTHS = [3, 4, 1, 5]

assert knot_hash(5, TEST_LENGTHS) == 12

def decode_lengths(inputs: str) -> List[int]:
	return [ord(str(x)) for x in inputs] + [17, 31, 73, 47, 23]

assert decode_lengths('1,2,3') == [49,44,50,44,51,17,31,73,47,23]

def xor(block: List[int]) -> int:
	block_xor = 0
	for x in block:
		block_xor ^= x
	return block_xor

assert xor([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]) == 64

def partition(arr: List[int], block_size: int = 16) -> Iterator[List[int]]:
	arr_size = len(arr)
	for block_start in range(0, arr_size, block_size):
		block_end = block_start + block_size
		yield arr[block_start:block_end]

def strip(x: str) -> str:
	return x.replace('0x', '')

def pad(x: str, length: int = 2, char: str = '0') -> str:
	pad_length = length - len(x)
	return pad_length * char + x

def knot_hash2(lengths: str,
               arr_size: int = 256,
               block_size: int = 16,
               num_iterations: int = 64) -> int:
	arr = [i for i in range(arr_size)]

	lengths = decode_lengths(lengths)

	skip_size = 0
	pos = 0
	for i in range(num_iterations):
		for length in lengths:
			# print(pos, skip_size, length, arr, end=' ')
			arr = pinch_twist(arr, pos, length)
			# print(arr)
			pos = (pos + length + skip_size) % arr_size
			skip_size += 1

	blocked = partition(arr)
	xored = map(xor, blocked)
	hexed = map(hex, xored)
	stripped = map(strip, hexed)
	padded = map(pad, stripped)
	hashed = ''.join(list(padded))

	assert len(hashed) == 32

	return hashed

assert knot_hash2('') == 'a2582a3a0e66e6e86e3812dcb672a272'
assert knot_hash2('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
assert knot_hash2('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
assert knot_hash2('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'

if __name__ == '__main__':
	INPUT = [147, 37, 249, 1, 31, 2, 226, 0, 161, 71, 254, 243, 183, 255, 30, 70]
	print(knot_hash(256, INPUT))

	INPUT2 = '147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70'
	print(knot_hash2(INPUT2))
