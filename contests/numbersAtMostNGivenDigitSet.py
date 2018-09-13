class Solution(object):
	def atMostNGivenDigitSet(self, D, N):
		ans = []

		def dfs(val, D, N, ans):
			if val > N:
				return
			else:
				ans.append(val)

			for digit in D:
				dfs(val * 10 + int(digit), D, N, ans)

		for digit in D:
			dfs(int(digit), D, N, ans)

		return ans, len(ans)


D = ["1", "3", "5", "7"]
N = 100
print Solution().atMostNGivenDigitSet(D, N)