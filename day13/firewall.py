from typing import List, Dict

class Scanner(object):
	def __init__(self, depth: int, width: int, pos: int = 0, dir = 1) -> None:
		self.depth = depth
		self.width = width
		self.pos = pos
		self.dir = 1

	def update(self):
		pos = (self.pos + 1) % self.width
		return Scanner(self.depth, self.width, pos)

	def __repr__(self) -> str:
		blocks = ['[ ]'] * self.width
		blocks[self.pos] = '[S]'
		blocks = ' '.join(blocks)
		return blocks

def update(scanner: Scanner) -> Scanner:
	scanner.pos += scanner.dir
	if scanner.pos == scanner.width or scanner.pos == -1:
		scanner.dir *= -1
		scanner.pos += scanner.dir
	return Scanner(scanner.depth, scanner.width, scanner.pos, scanner.dir)

def parse_scanners(string: str) -> Dict[int, Scanner]:
	scanners: Dict[int, Scanner] = {}
	for line in string.split('\n'):
		depth, width = line.split(': ')
		depth, width = int(depth), int(width)
		scanners[depth] = Scanner(depth, width)
	return scanners

def update_scanners(scanners: Dict[int, Scanner]) -> Dict[int, Scanner]:
	return {layer : update(scanners[layer]) for layer in scanners}

def severity(scanners: Dict[int, Scanner]) -> int:
	num_layers = max(scanners)
	total_severity = 0
	for i in range(num_layers):
		print(scanners)
		if i in scanners:
			if scanners[i].pos == 0:
				print('found!')
				total_severity += i * scanners[i].width
			print(i, scanners[i].width, total_severity)
		scanners = update_scanners(scanners)
	return total_severity

def rep_scanners(scanners: List[Scanner]) -> str:
	reprs = [scanner.__repr__() for scanner in scanners]
	return '\n'.join(reprs)




TEST_INPUT = """0: 3
1: 2
4: 4
6: 4"""

test_scanners = parse_scanners(TEST_INPUT)
print(severity(test_scanners))
# print(test_scanners)
# print(update_scanners(test_scanners))
# print(rep_scanners(test_scanners))
# print()

# for i in range(5):
# 	test_scanners = update_scanners(test_scanners)
# 	print(rep_scanners(test_scanners))
# 	print()
