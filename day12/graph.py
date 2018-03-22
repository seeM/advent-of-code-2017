from typing import List, Dict

def parse_graph(text: str) -> Dict[int, List[int]]:
	graph: Dict[int, List[int]] = {}
	for line in text.split('\n'):
		from_node, to_nodes = line.split(' <-> ')
		from_node = int(from_node)
		to_nodes = [int(x) for x in to_nodes.split(', ')]
		graph[from_node] = to_nodes

	return graph

def find_connected(graph: Dict[int, List[int]], center: int) -> List[int]:
	"""
	Returns a list of nodes in an undirected graph all connected to `center`.
	"""
	assert center in graph, f"center = {center} is not in graph = {graph}"
	
	visited = {node : False for node in graph}

	def search(graph: Dict[int, List[int]], center: int) -> None:
		if visited[center]:
			return None
		else:
			visited[center] = True
			for node in graph[center]:
				search(graph, node)

	search(graph, center)

	return [x for x in visited if visited[x]]

def find_groups(graph: Dict[int, List[int]]) -> List[List[int]]:
	"""
	Find all groups of connected nodes in an undirected graph.
	"""
	groups = []
	for node in graph:
		has_group = any(node in group for group in groups)
		if not has_group:
			groups.append(find_connected(graph, node))

	return groups

TEST_INPUT = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""

TEST_GRAPH = parse_graph(TEST_INPUT)
assert len(find_connected(TEST_GRAPH, 0)) == 6
assert len(find_groups(TEST_GRAPH)) == 2

if __name__ == '__main__':
	with open('input.txt', 'r') as f:
		graph_input = f.read().strip()
	graph = parse_graph(graph_input)
	
	print(len(find_connected(graph, 0)))
	print(len(find_groups(graph)))
