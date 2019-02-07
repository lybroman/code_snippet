from functools import wraps

W = {
	'a': {'a': float('inf'), 'b': 2, 'c': float('inf'), 'd': float('inf'), 'e': float('inf'), 'f': 9},
	'b': {'a': float('inf'), 'b': float('inf'), 'c': 1, 'd': 2, 'e': float('inf'), 'f': 6},
	'c': {'a': float('inf'), 'b': float('inf'), 'c': float('inf'), 'd': 2, 'e': float('inf'), 'f': float('inf')},
	'd': {'a': float('inf'), 'b': float('inf'), 'c': float('inf'), 'd': float('inf'), 'e': 2, 'f': 3},
	'e': {'a': float('inf'), 'b': float('inf'), 'c': float('inf'), 'd': float('inf'), 'e': float('inf'), 'f': 4},
	'f': {'a': float('inf'), 'b': float('inf'), 'c': float('inf'), 'd': float('inf'), 'e': float('inf'), 'f': float('inf')},
}


def memo(func):
	cache = {}

	@wraps(func)
	def wrapper(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]

	return wrapper


def rec_dag_shortest_path(s, t):
	@memo
	def d(u):
		if u == t:
			return 0
		return min(W[u][v] + d(v) for v in W[u] if W[u][v] < float('inf'))

	return d(s)


print rec_dag_shortest_path('a', 'f')


def top_sort(W):
	from collections import defaultdict
	ind_graph = defaultdict(int)

	for u in W:
		for v in W[u]:
			if W[u][v] < float('inf'):
				ind_graph[v] += 1

	q = []
	for u in W:
		if not ind_graph[u]:
			q.append(u)

	while q:
		n = q.pop()
		yield n
		for v in W[n]:
			if W[n][v] < float('inf'):
				ind_graph[v] -= 1
				if not ind_graph[v]:
					q.append(v)


def dag_sp(s, t):
	d = {u: float('inf') for u in W}
	d[s] = 0
	for u in top_sort(W):
		if u == t:
			return d[u]
		for v in W[u]:
			d[v] = min(d[v], d[u] + W[u][v])

	return d[t]


print dag_sp('a', 'f')


