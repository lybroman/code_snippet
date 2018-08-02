class Solution(object):
	def longestMountain(self, A):
		ans = 0
		cur_l = 1
		cur_d = 1
		peek = -1
		i = 0
		while i < len(A):
			while cur_d == 1 and i + 1 < len(A) and A[i + 1] > A[i]:
				i += 1
				peek = i
				cur_l += 1

			if peek != -1:
				cur_d = -1

			if peek != -1:
				while cur_d == -1 and i + 1 < len(A) and A[i + 1] < A[i]:
					i += 1
					cur_l += 1
					peek = -1

				if peek == -1:
					ans = max(ans, cur_l)
				else:
					i += 1

				peek = -1
				cur_l = 1
				cur_d = 1

			else:
				cur_l = 1
				i += 1

		return ans

A = [2,1,4,7,3,2,5]
B = [2,2,2]
C = [1,4,7,3,2,1,4,5,6,7,8,5,4]
D = [7,4,1,2,3,2,1]
E = [1,2,3,2,1]
F = [2,3,3,2,0,2]

print Solution().longestMountain(A)
print Solution().longestMountain(B)
print Solution().longestMountain(C)
print Solution().longestMountain(D)
print Solution().longestMountain(E)
print Solution().longestMountain(F)
