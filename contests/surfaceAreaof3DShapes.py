class Solution(object):
	def surfaceArea(self, grid):
		pos = set()
		area = 0
		for i in xrange(0, len(grid)):
			for j in xrange(0, len(grid[i])):
				for k in range(0, grid[i][j]):
					base = 6
					if (i - 1, j, k) in pos:
						base -= 2
					if (i + 1, j, k) in pos:
						base -= 2
					if (i, j - 1, k) in pos:
						base -= 2
					if (i, j + 1, k) in pos:
						base -= 2
					if (i, j, k - 1) in pos:
						base -= 2
					if (i, j, k + 1) in pos:
						base -= 2
					area += base
					pos.add((i, j, k))

		return area


grid = [[1,1,1],[1,0,1],[1,1,1]]
print Solution().surfaceArea(grid)
grid = [[2,2,2],[2,1,2],[2,2,2]]
print Solution().surfaceArea(grid)