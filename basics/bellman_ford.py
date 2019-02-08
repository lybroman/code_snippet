# Non-negative cycle graph
a, b, c, d, e, f, g, h = range(8)
G = {
	a: {b: 2, c: 1, d: 3, e: 9, f: 4},
	b: {c: 4, e: 3},
	c: {d: 8},
	d: {e: 7},
	e: {f: 5},
	f: {c: 2, g: 2, h: 2},
	g: {f: 1, h: 6},
	h: {f: 9, g: 8}
}


def relax(W, u, v, D, P):
	inf = float('inf')
	d = D.get(u, inf) + W[u][v]
	if d < D.get(v, inf):
		D[v], P[v] = d, u
		return True
	return False


def bellman_ford(G, s):
	# set source to 0
	D, P = {s: 0}, {}

	# at most n - 1 rounds
	for rnd in G:
		changed = False
		for u in G:
			for v in G[u]:
				if relax(G, u, v, D, P):
					changed = True

		if not changed:
			break
	else:
		raise ValueError("negative cycle")

	return D, P


print bellman_ford(G, a)
