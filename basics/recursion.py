# hanoi recursive solution
def hanoi(n, source, helper, target):
	if n > 0:
		# move tower of size n - 1 to helper:
		hanoi(n - 1, source, target, helper)
		# move disk from source peg to target peg
		print 'move disk {} from {} to {}'.format(n, source, target)
		# move tower of size n-1 from helper to target
		hanoi(n - 1, helper, source, target)


source = 'src'
target = 'target'
helper = 'helper'
hanoi(3, source, helper, target)


# memoization optimization with closure
def memoizer(memo, func):
	def recur(n):
		if n in memo:
			return memo[n]

		result = func(recur, n)
		memo[n] = result

		return result

	return recur


def fb(recur, n):
	return recur(n - 1) + recur(n - 2)


# cache
f = {0: 1, 1: 1}

for i in xrange(2, 11):
	f[i] = f[i - 1] + f[i - 2]
print 'f(10):',  f[10]

# general
a, b = 1, 1
for i in xrange(2, 11):
	c = a + b
	a, b = b, c

print 'f(10):',  c

fb = memoizer({0: 0, 1: 1}, fb)

for i in xrange(10):
	print fb(i)


def factorial(recur, n):
	return n * recur(n - 1)


memo = {1: 1}
factorial = memoizer(memo, factorial)

for i in xrange(1, 5):
	print factorial(i), memo

# memo decorator
# python3 lru_cache
from functools import wraps


def memo(func):
	cache = {}

	@wraps(func)
	def wrapper(*args):
		if args in cache:
			return cache[args]
		cache[args] = func(*args)
		return cache[args]

	return wrapper


# binomial coefficient
# pascal triangle
# path count
n, k = 10, 7
row = {}
for i in xrange(n + 1):
	row[(i, 0)], row[(i, i)] = 1, 1
	if i == 0 or i == 1:
		continue
	for j in xrange(1, i):
		row[(i, j)] = row[(i - 1, j - 1)] + row[(i - 1, j)]

print row[(10, 7)]




