class Solution(object):
	def numMagicSquaresInside(self, grid):
		m = len(grid)
		if m < 3: return 0
		n = len(grid[0])
		if n < 3: return 0

		count = 0

		def gcs(ii,jj):
			return grid[ii][jj] + grid[ii][jj + 1] + grid[ii][jj + 2]

		def isMagic(ii, jj):
			dm = {_: 0 for _ in xrange(1, 10)}
			for x in range(3):
				for y in range(3):
					if grid[ii + x][jj + y] in dm and dm[grid[ii + x][jj + y]] == 0:
						dm[grid[ii + x][jj + y]] = 1
					else:
						return False

			if sum(grid[ii][jj: jj + 3]) == sum(grid[ii + 1][jj: jj + 3]) == sum(grid[ii + 2][jj: jj + 3]) == \
					gcs(ii, jj) == gcs(ii,jj)== gcs(ii,jj) == \
					(grid[ii][jj] + grid[ii + 1][jj + 1] + grid[ii + 2][jj + 2]) == \
					(grid[ii][jj + 2] + grid[ii + 1][jj + 1] + grid[ii + 2][jj]):
				return True
			else:
				return False


		for i in xrange(0, m - 3 + 1):
			for j in xrange(0, n -3 + 1):
				if isMagic(i, j):
					count += 1

		return count

c = [[10,3,5],[1,6,11],[7,9,2]]

print Solution().numMagicSquaresInside(c)
