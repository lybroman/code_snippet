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


def recur_dfs(G):
	seen = set()
	res = []

	def _recur(G, s):
		if s not in seen:
			seen.add(s)
			res.append(s)
			for n in G[s]:
					_recur(G, n)

	for n in G:
		if n not in seen:
			_recur(G, n)

	return res


print recur_dfs(G)


def iter_dfs(G):
	seen = set()
	res = []

	def _iter(G, s):
		lifo = [s]
		while lifo:
			top = lifo.pop()
			if top not in seen:
				seen.add(top)
				res.append(top)
				for n in G[top]:
					lifo.append(n)

	for n in G:
		_iter(G, n)

	return res


print iter_dfs(G)


# iterative deepening dfs
def iddfs(G, max_depth):
	seen = set()
	res = []
	r = []

	def _iddfs(G, s, d):
		if s not in seen and d >= 0:
			seen.add(s)
			res.append(s)
			for n in G[s]:
				_iddfs(G, n, d - 1)

	for n in G:
		res = []
		_iddfs(G, n, max_depth)
		if res: r.append(res)

	return r


print iddfs(G, 2)
