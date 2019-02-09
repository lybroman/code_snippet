from functools import wraps


def memo(func):
	cache = {}

	@wraps(func)
	def wrapper(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]

	return wrapper


def rec_lcs(a, b):

	@memo
	def L(i, j):
		if i < 0 or j < 0:
			return 0
		if a[i] == b[j]:
			return L(i - 1, j - 1) + 1
		else:
			return max(L(i - 1, j), L(i, j - 1))

	return L(len(a) - 1, len(b) - 1)


print rec_lcs('spock', 'aosoka')


def iter_lcs(a, b):
	cur, pre = [0] * (len(b) + 1), [0] * (len(b) + 1)
	for i in xrange(1, len(a) + 1):
		pre, cur = cur, pre
		for j in xrange(1, len(b) + 1):
			if a[i - 1] == b[j - 1]:
				cur[j] = pre[j - 1] + 1
			else:
				cur[j] = max(cur[j - 1], pre[j])

	return cur[len(b)]


print iter_lcs('spock', 'aosoka')
