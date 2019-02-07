"""
i	1	2	3	4	5
ki	k1	k2	k3	k4	k5
pi	0.25	0.20	0.05	0.20	0.30
"""

from functools import wraps
from collections import defaultdict


p = [0.25, 0.20, 0.05, 0.20, 0.30]


def memo(func):
	cache = {}

	@wraps(func)
	def wrapper(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]

	return wrapper


def rec_opt_bst(p):
	@memo
	def s(i, j):
		if i == j:
			return 0
		return s(i, j - 1) + p[j - 1]

	@memo
	def e(i, j):
		if i == j:
			return 0
		sub = min(e(i, r) + e(r + 1, j) for r in xrange(i, j))
		return sub + s(i, j)

	return e(0, len(p))


print rec_opt_bst(p)


def iter_opt_bst(p):
	n = len(p)
	s, e = defaultdict(int), defaultdict(int)
	for k in xrange(1, n + 1):
		for i in xrange(0, n - k + 1):
			j = i + k
			s[i, j] = s[i, j - 1] + p[j - 1]
			e[i, j] = min(e[i, r] + e[r + 1, j] for r in xrange(i, j))
			e[i, j] += s[i, j]

	return e[0, n]


print iter_opt_bst(p)


