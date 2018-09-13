class Solution(object):

	def fairCandySwap(self, A, B):
		total_a = sum(A)
		total_b = sum(B)
		A.sort()
		B.sort()

		if total_a == total_b:
			return [A[0], B[0]]

		def binary_search(Ai, B, diff):
			i = 0
			j = len(B)

			while i <= j:
				mid = (i + j) / 2
				print B[mid], (B[mid] - Ai) * 2
				if (B[mid] - Ai) * 2 == diff:
					return B[mid]
				elif (B[mid] - Ai) * 2 > diff:
					j = mid - 1
				else:
					i = mid + 1

			return None

		if total_b > total_a:
			for i in xrange(len(A)):
				Bj = binary_search(A[i], B, total_b - total_a)
				if Bj:
					return [A[i], Bj]

		else:
			for i in xrange(len(B)):
				print '....', B[i]
				Aj = binary_search(B[i], A, total_a - total_b)
				if Aj:
					return [Aj, B[i]]

print Solution().fairCandySwap([35,17,4,24,10], [63,21])