class Solution(object):
	def sumSubarrayMins(self, A):
		stack = []
		N = len(A)
		prev = [None] * N
		for i in xrange(N):
			while stack and A[i] <= A[stack[-1]]:
				stack.pop()
			prev[i] = stack[-1] if stack else -1
			stack.append(i)

		stack = []
		nxt = [None] * N
		for j in xrange(N - 1, -1, -1):
			while stack and A[j] < A[stack[-1]]:
				stack.pop()

			nxt[j] = stack[-1] if stack else N
			stack.append(j)

		return sum([(i - prev[i])*(nxt[i] - i)*A[i] for i in xrange(N)]) % (10**9 + 7)


print Solution().sumSubarrayMins([3, 1, 2, 4])