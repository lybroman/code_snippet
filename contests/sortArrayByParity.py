class Solution(object):
	def sortArrayByParity(self, A):
		ans = []
		for digit in A:
			if digit % 2 == 0:
				ans.insert(0, digit)
			else:
				ans.append(digit)
		return ans


print Solution().sortArrayByParity([0, 1])