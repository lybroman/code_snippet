class Solution(object):
	def transpose(self, A):
		rows = len(A)
		if rows == 0: return A
		cols = len(A[0])
		return [[A[i][j] for i in range(rows)] for j in range(cols)]



print Solution().transpose([[1,2,3],[4,5,6],[7,8,9]])
print Solution().transpose([[1,2,3],[4,5,6]])