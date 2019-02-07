from functools import wraps


def test_splk():
	def knapsack_01(obj_list, package_size):
		obj_num = len(obj_list)
		data = [[0] * (package_size + 1) for _ in xrange(obj_num)]
		for j in xrange(package_size + 1):
			for i in xrange(obj_num):
				if i > 0:
					data[i][j] = data[i - 1][j]
				if j >= obj_list[i]:
					max_without_i = data[i - 1][j - obj_list[i]] if i > 0 else 0
					data[i][j] = max(data[i][j], max_without_i + obj_list[i])
		return data[obj_num - 1][package_size]

	jobs = [1, 3, 4, 5, 6, 2]
	jobs.sort()

	jobs_sum = sum(jobs)
	aim = jobs_sum / 2

	res = knapsack_01(jobs, aim)
	print jobs_sum - res


weights = [23, 26, 20, 18, 32, 27, 29, 26, 30, 27]
values = [505, 352, 458, 220, 354, 414, 498, 545, 473, 543]


def memo(func):
	cache = {}

	@wraps(func)
	def wrapper(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]

	return wrapper


def rec_unbounded_knapsack(w, v, c):
	@memo
	def m(r):
		if r == 0:
			return 0
		val = m(r - 1)
		for ith, weight in enumerate(w):
			if weight <= r:
				val = max(m(r - weight) + v[ith], val)
		return val
	return m(c)


print rec_unbounded_knapsack(weights, values, 67)


def iter_unbounded_knapsack(w, v, c):
	m = [0]
	for i in xrange(1, c + 1):
		val = m[i - 1]
		for ith, weight in enumerate(w):
			if weight <= i :
				val = max(val, m[i - weight] + v[ith])

		m.append(val)
	return m[-1]


print iter_unbounded_knapsack(weights, values, 67)


def rec_01_knapsack(w, v, c):
	@memo
	def m(k, r):
		if k == 0 or r == 0:
			return 0

		drop = m(k - 1, r)

		if w[k - 1] <= r:
			return max(drop, m(k - 1, r - w[k - 1]) + v[k - 1])

		return drop

	return m(len(w), c)


print rec_01_knapsack(weights, values, 67)


def iter_01_knapsack(w, v, c):
	m = [[0] * (c + 1) for _ in xrange(len(w) + 1)]
	for k in xrange(1, len(m)):
		for r in xrange(1, len(m[0])):
			if r >= w[k - 1]:
				m[k][r] = max(m[k - 1][r], m[k - 1][r - w[k - 1]] + v[k - 1])
			else:
				m[k][r] = m[k - 1][r]

	return m[-1][-1]


print iter_01_knapsack(weights, values, 67)
