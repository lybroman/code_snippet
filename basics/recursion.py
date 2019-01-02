# hanoi recursive solution
def hanoi(n, source, helper, target):
	if n > 0:
		# move tower of size n - 1 to helper:
		hanoi(n - 1, source, target, helper)
		# move disk from source peg to target peg
		if source:
			target.append(source.pop())
		# move tower of size n-1 from helper to target
		hanoi(n - 1, helper, source, target)


source = [4, 3, 2, 1]
target = []
helper = []

print source, helper, target
hanoi(len(source), source, helper, target)
print source, helper, target


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


fb = memoizer({0: 0, 1: 1}, fb)

for i in xrange(10):
	print fb(i)


def fac(recur, n):
	return n * recur(n - 1)


memo = {1: 1}
fac = memoizer(memo, fac)

for i in xrange(1, 5):
	print fac(i), memo