class Solution(object):
	def nthMagicalNumber(self, N, A, B):
		gcd = lambda a, b: (gcd(b, a % b) if a % b else b)
		g = gcd(A, B)
		lo = 0
		hi = 10 ** 20

		gg = A * B / g

		while lo < hi:
			mid = (lo + hi) / 2
			n = mid/A + mid/B - mid/gg
			if n < N:
				lo = mid + 1
			else:
				hi = mid

		return lo % (1000000007)


print Solution().nthMagicalNumber(1000000000, 4000, 4000)