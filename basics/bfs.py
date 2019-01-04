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


def recur_bfs(G):
	seen = set()
	res = []

	def _recur(G, level):
		if not level: return
		tmp = []
		for n in level:
			if n not in seen:
				seen.add(n)
				res.append(n)
				for child in G[n]:
						tmp.append(child)
		_recur(G, tmp)

	for n in G:
		_recur(G, [n])

	return res


print recur_bfs(G)


def iter_bfs(G):
	from collections import deque
	seen = set()
	res = []

	def _iter(G, s):
		fifo = deque([s])
		while fifo:
			first = fifo.popleft()
			if first not in seen:
				seen.add(first)
				res.append(first)
				for n in G[first]:
					fifo.append(n)

	for n in G:
		_iter(G, n)

	return res


print iter_bfs(G)
