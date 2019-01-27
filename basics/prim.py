from heapq import heappush, heappop
from collections import defaultdict
edges = [
		("A", "B", 7),
		("A", "D", 5),
		("B", "C", 8),
		("B", "D", 99),
		("B", "E", 9),
		("C", "E", 5),
		("D", "E", 15),
		("D", "F", 6),
		("E", "F", 8),
		("E", "G", 9),
		("F", "G", 11)
	]

nodes = 'ABCDEFG'


def prim(nodes, edges):
	P, Q = {}, [(0, None, nodes[0])]
	G = defaultdict(lambda: defaultdict(lambda: float('inf')))
	for e in edges:
		G[e[0]][e[1]] = e[2]

	while Q:
		_, p, v = heappop(Q)
		if v in P:
			continue
		P[v] = p

		for vv, ww in G[v].iteritems():
			heappush(Q, (ww, v, vv))

	return P


print prim(nodes, edges)
