"""
https://adventofcode.com/2017/day/11

Reference:

A very interesting and useful link, also the first google search result:
    http://keekerdc.com/2011/03/hexagon-grids-coordinate-systems-and-distance-calculations/
"""
from typing import Dict, Tuple, List
# from enum import Enum

# class Dir(Enum):
# 	ne = 0

DIRECTION: Dict[str, Tuple[int, int]] = {
	'n': (0, 1),
	's': (0, -1),
	'nw': (-1, 1) ,
	'se': (1, -1),
	'ne': (1, 0),
	'sw': (-1, 0)
}

def parse_path(path: str) -> List[Tuple[int, int]]:
	return [DIRECTION[x] for x in path.split(',')]

def sum_vectors(vectors: List[Tuple[int, int]]):
	x, y = (0, 0)
	for xi, yi in vectors:
		x += xi
		y += yi

	return (x, y)

def find_coords(path: str) -> Tuple[int, int]:
	steps = parse_path(path)
	x, y = sum_vectors(steps)
	return x, y

def distance(coords: Tuple[int, int]) -> int:
	x, y = coords
	z = -x - y
	return max(x, y, z)

def find_furthest(path: str) -> Tuple[int, int]:
	steps = parse_path(path)

	x, y = (0, 0)
	furthest_distance = float('-inf')
	for xi, yi in steps:
		x, y = (x + xi, y + yi)
		dist = distance((x, y))
		if dist > furthest_distance:
			furthest_distance = dist

	return furthest_distance

assert distance(find_coords('ne,ne,ne')) == 3
assert distance(find_coords('ne,ne,sw,sw')) == 0
assert distance(find_coords('ne,ne,s,s')) == 2
assert distance(find_coords('se,sw,se,sw,sw')) == 3

assert find_furthest('ne,ne,ne') == 3
assert find_furthest('ne,ne,sw,sw') == 2
assert find_furthest('ne,ne,s,s') == 2
assert find_furthest('se,sw,se,sw,sw') == 3

if __name__ == '__main__':
	with open('input.txt', 'r') as f:
		path = f.read().strip()
	print(distance(find_coords(path)))
	print(find_furthest(path))
