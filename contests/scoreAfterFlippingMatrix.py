class Solution(object):
	def matrixScore(self, A):
		R, C = len(A), len(A[0])
		ans = 0
		for c in xrange(C):
			col = 0
			for r in xrange(R):
				col += A[r][c] ^ A[r][0]
			print max(col, R - col) * 2 ** (C - 1 - c)
			ans += max(col, R - col) * 2 ** (C - 1 - c)
		return ans


print Solution().matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]])
