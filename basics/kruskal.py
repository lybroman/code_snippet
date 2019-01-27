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


def find_rep(C, u):
	if C[u] == u:
		return u
	else:
		return find_rep(C, C[u])


def union(C, R, u, v):
	u, v = find_rep(C, u), find_rep(C, v)
	if R[u] > R[v]:
		C[v] = u
	else:
		C[u] = v
	if R[u] == R[v]:
		R[v] += 1


def kruskal(nodes, edges):
	C = {n: n for n in nodes}
	R = {n: 0 for n in nodes}
	E = [(e[2], e[0], e[1]) for e in edges]
	E.sort()
	mst = set()
	for w, u, v in E:
		if find_rep(C, u) != find_rep(C, v):
			mst.add((u, v, w))
			union(C, R, u, v)
	return mst


print kruskal(nodes, edges)
