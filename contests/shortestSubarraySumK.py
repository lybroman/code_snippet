class Solution(object):
	def shortestSubarray(self, A, K):
		"""O(N^3)"""
		for j in xrange(1, len(A) + 1):
			for i in xrange(0, len(A) - j + 1):
				if sum(A[i: i + j]) >= K:
					return j

		return -1


class Solution1(object):
	def shortestSubarray(self, A, K):
		"""O(N^2)"""

		ans = []
		min_len = float('inf')

		def update_array(ans):
			j = 0
			for j in xrange(len(ans) - 1, -1, -1):
				if sum(ans[j:]) >= K:
					break

			return ans[j:]

		for i in xrange(0, len(A)):
			if A[i] < 0:
				if sum(ans) + A[i] > 0:
					ans.append(A[i])
				else:
					ans = []
			elif A[i] >= 0:
				ans.append(A[i])
				if sum(ans) >= K:
					ans = update_array(ans)
					min_len = min(min_len, len(ans))

		return min_len if min_len != float('inf') else -1


class Solution2(object):
	def shortestSubarray(self, A, K):
		"""O(N)"""
		if not A:
			return -1
		sum_array = [0]
		for i in xrange(len(A)):
			sum_array.append(sum_array[-1] + A[i])

		print sum_array

		queue = []
		min_depth = len(A) + 1
		for k, sum_k in enumerate(sum_array):

			while queue and sum_k <= sum_array[queue[-1]]:
				queue.pop()

			i = 0
			while queue and sum_k - sum_array[queue[i]] >= K:
				min_depth = min(min_depth, k - queue.pop(0))

			queue.append(k)

		return min_depth if min_depth < len(A) + 1 else -1

#print Solution2().shortestSubarray([11,47,97,35,-46,59,46,51,59,80,14,-6,2,20,96,1,18,74,-17,71], 282)
#print Solution2().shortestSubarray([1], 1)
#print Solution2().shortestSubarray([12,13,13], 10)
#print Solution2().shortestSubarray([8,-7,13], 10)
print Solution2().shortestSubarray([8,-7,9], 10)
#print Solution2().shortestSubarray([0], 0)
#print Solution2().shortestSubarray([8,-7,9], 10)
#print Solution2().shortestSubarray([-1,1,0,1,2], 3)

