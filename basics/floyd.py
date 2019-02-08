# D{i,j,k} = min(D{i,j,k-1},D{i,k,k-1} + D{k,j,k-1})
# all pairs min dist
# negative weight
# O(V^3)
import pprint
from functools import wraps
from copy import deepcopy


def floyd_warshall(graph):
	graph = deepcopy(graph)
	length = len(graph) + 1
	for k in range(1, length):
		for i in range(1, length):
			for j in range(1, length):
				graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

	return graph


def memo(func):
	cache = {}

	@wraps(func)
	def wrapper(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]

	return wrapper


def rec_floyd_warshall(G):
	@memo
	def d(u, v, k):
		if k == 0:
			return G[u][v]
		return min(d(u, v, k - 1), d(u, k, k - 1) + d(k, v, k - 1))

	return {(u, v): d(u, v, len(G)) for u in G for v in G}


if __name__ == "__main__":
	inf = float('inf')
	graph = {
		1: {1: 0, 2: 3, 3: 8, 4: inf, 5: -4},
		2: {1: inf, 2: 0, 3: inf, 4: 1, 5: 7},
		3: {1: inf, 2: 4, 3: 0, 4: inf, 5: inf},
		4: {1: 2, 2: inf, 3: -5, 4: 0, 5: inf},
		5: {1: inf, 2: inf, 3: inf, 4: 6, 5: 0}
	}
	pprint.pprint(floyd_warshall(graph))

	pprint.pprint(rec_floyd_warshall(graph))


