class Solution(object):
	def spiralMatrixIII(self, R, C, r0, c0):
		total = R * C
		count = 1
		edge = 0
		ans = [[r0, c0]]
		r, c = r0, c0

		if count == total:
			return ans

		while True:

			# right
			edge += 1
			r += 0
			c += edge
			for cc in range(c - edge + 1, c + 1):
				if 0 <= r < R and 0 <= cc < C:
					ans.append([r, cc])
					count += 1
					if count == total:
						return ans




			# down
			r += edge
			c += 0
			for rr in range(r - edge + 1, r + 1):
				if 0 <= rr < R and 0 <= c < C:
					ans.append([rr, c])
					count += 1
					if count == total:
						return ans


			# left
			edge += 1

			r -= 0
			c -= edge

			for cc in range(c + edge - 1, c - 1, -1):
				if 0 <= r < R and 0 <= cc < C:
					ans.append([r, cc])
					count += 1
					if count == total:
						return ans

			# up
			r -= edge
			c -= 0
			for rr in range(r + edge - 1, r - 1, -1):
				if 0 <= rr < R and 0 <= c < C:
					ans.append([rr, c])
					count += 1
					if count == total:
						return ans


R = 1
C = 1
r0 = 0
c0 = 0
print Solution().spiralMatrixIII(R, C, r0, c0)