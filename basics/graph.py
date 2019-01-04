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


# print walk(G, 'a')
# print components(G)


G = {
	'a': {'b', 'c'},
	'b': {'e', 'd', 'i'},
	'c': {'d'},
	'd': {'a', 'h'},
	'e': {'f'},
	'f': {'g'},
	'g': {'e', 'h'},
	'h': {'i'},
	'i': {'h'}
}


# strongly connected components
def ssc(G):
	from collections import defaultdict
	inv_G = defaultdict(set)

	for n in G:
		for child in G[n]:
			inv_G[child].add(n)

	def dfs_top_sort(G):
		seen = set()
		res = []

		def _recur(G, s):
			if s not in seen:
				seen.add(s)
				for n in G[s]:
					_recur(G, n)

				res.append(s)

		for n in G:
			_recur(G, n)

		res.reverse()
		return res

	seq = dfs_top_sort(G)

	def iter_dfs(G):
		seen = set()

		def _iter(G, s):
			res = set()
			lifo = [s]
			while lifo:
				top = lifo.pop()
				if top not in seen:
					seen.add(top)
					res.add(top)
					for n in G[top]:
						lifo.append(n)

			return res


		sscs = []
		for n in G:
			res = _iter(G, n)
			if res: sscs.append(res)

		return sscs

	return iter_dfs(inv_G)

print ssc(G)