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


def recur_dfs(G, s, S=None):
	pass




def iter_dfs():
	pass


def iddfs():
	pass


def dfs_topsort(G):
	visited = set()
	res = []

	def recur_dfs(s):
		if s in visited:
			return

		visited.add(s)

		for v in G[s]:
			recur_dfs(v)

		print s
		res.append(s)

	for n in G:
		recur_dfs(n)

	res.reverse()
	return res


print dfs_topsort(G)