import itertools
class Solution(object):
	def shortestPathAllKeys(self, grid):
		R, C = len(grid), len(grid[0])
		locations = {grid[i][j]: (i, j) for j in xrange(C) for i in xrange(R) if grid[i][j] not in '.#'}

		def neighbours(i, j):
			for n_i, n_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
				if 0 <= n_i < R and 0 <= n_j < C:
					yield n_i, n_j

		def bfs(source, target, keys):
			sr, sc = locations[source]
			tr, tc = locations[target]
			queue = [(sr, sc,  0)]
			visited = [[0] * C for _ in xrange(R)]
			visited[sr][sc] = 1
			while queue:
				r, c, d = queue.pop(0)
				if r == tr and c == tc:
					return d

				for nr, nc in neighbours(r, c):
					if not visited[nr][nc] and grid[nr][nc] != '#':
						if grid[nr][nc].isupper() and grid[nr][nc].lower() not in keys:
							continue
						visited[nr][nc] = 1
						queue.append((nr, nc, d+1))
			return float('inf')

		keys = ''.join(chr(ord('a') + i) for i in xrange(len(locations) / 2))

		min_steps = float('inf')
		for perm in itertools.permutations(keys):
			path = '@' + ''.join(perm)
			steps = 0
			for i in xrange(1, len(path)):
				if steps >= min_steps:
					break
				steps += bfs(path[i - 1], path[i], path[1:i])
			else:
				min_steps = min(min_steps, steps)

		return min_steps if min_steps != float('inf') else -1

class Solution1(object):
	def shortestPathAllKeys(self, grid):
		R, C = len(grid), len(grid[0])

		locations = {p: (r, c) for r, row in enumerate(grid) for c, p in enumerate(row) if p != '.#'}

		def neighbours(i, j):
			for n_i, n_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
				if 0 <= n_i < R and 0 <= n_j < C:
					yield n_i, n_j

		def bfs(source):
			sr, sc = locations[source]
			queue = [(sr, sc, 0)]
			visited = [[0] * C for _ in xrange(R)]
			visited[sr][sc] = 1
			dist = {}
			while queue:
				r, c, d = queue.pop(0)

				if source != grid[r][c] != '.':
					dist[grid[r][c]] = d
					continue

				for nr, nc in neighbours(r, c):
					if not visited[nr][nc] and grid[nr][nc] != '#':
						visited[nr][nc] = 1
						queue.append((nr, nc, d + 1))

			return dist

		print bfs('@')



g = ["@..aA","..B#.","....b"]
gg = [[ch for ch in strs] for strs in g]
print Solution1().shortestPathAllKeys(gg)


