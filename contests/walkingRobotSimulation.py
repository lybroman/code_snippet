class Solution(object):
	def robotSim(self, commands, obstacles):
		dx = [0, 1, 0, -1]
		dy = [1, 0, -1, 0]
		x = y = di = 0
		obstacleSet = set(map(tuple, obstacles))
		ans = 0

		for cmd in commands:
			if cmd == -2:  # left
				di = (di - 1) % 4
			elif cmd == -1:  # right
				di = (di + 1) % 4
			else:
				for k in xrange(cmd):
					if (x + dx[di], y + dy[di]) not in obstacleSet:
						x += dx[di]
						y += dy[di]
						ans = max(ans, x * x + y * y)

		return ans

print Solution().robotSim([-2,-1,-2,3,7], [[1,-3],[2,-3],[4,0],[-2,5],[-5,2],[0,0],[4,-4],[-2,-5],[-1,-2],[0,2]])


