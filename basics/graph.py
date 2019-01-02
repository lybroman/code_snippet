G = {
	'a': {'b', 'c'},
	'b': {'a', 'c'},
	'c': {'a', 'b'},
	'd': {'e'},
	'e': {'d'}
}


def walk(G, s, S=set()):
	P, Q = dict(), set()
	# predecessor of start node is none
	P[s] = None
	Q.add(s)
	while Q:
		u = Q.pop()
		for v in G[u].difference(P, S):
			Q.add(v)
			P[v] = u
	return P

def components(G):
	seen = set()
	compo = []
	for v in G:
		if v in seen:continue
		# O(E + V)
		p = walk(G, v)
		seen.update(p)
		compo.append(p)

	return compo


print walk(G, 'a')
print components(G)