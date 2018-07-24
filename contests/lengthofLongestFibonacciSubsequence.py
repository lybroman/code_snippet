from collections import defaultdict


class Solution(object):
	def lenLongestFibSubseq(self, A):
		index = {x: i for i, x in enumerate(A)}
		longest = defaultdict(lambda: 2)
		overall_longest = 0
		for k, z in enumerate(A):
			for j in xrange(k):
				i = index.get(z - A[j], None)
				if i is not None and i < j:
					print i, j
					longest[j, k] = longest[i, j] + 1
					overall_longest = max(overall_longest, longest[j, k])

		return overall_longest if overall_longest > 2 else 0

	def lenLongestFibSubseq_brute_force(self, A):
		max_length = 2
		nums = set()
		for i in xrange(0,len(A)):
			nums.add(A[i])

		for i in xrange(0, len(A)):
			for j in xrange(i + 1, len(A)):
				l = 2
				x = A[i]
				y = A[j]

				while x + y in nums:
					l += 1
					x, y = y, x + y
					max_length = max(l, max_length)

		return max_length if max_length > 2 else 0


print Solution().lenLongestFibSubseq([1,2,3,4,5,6,7,8])
print Solution().lenLongestFibSubseq_brute_force([1,2,3,4,5,6,7,8])