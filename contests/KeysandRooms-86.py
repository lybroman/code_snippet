class Solution(object):
	def canVisitAllRooms(self, rooms):
		keys = set()
		keys.add(0)
		visited = [False for i in xrange(len(rooms))]
		visited[0] = True
		while keys:
			key = keys.pop()
			for nk in rooms[key]:
				if not visited[nk]:
					keys.add(nk)
					visited[nk] = True

		if all(visited):
			return True
		else:
			return False


print Solution().canVisitAllRooms([[1],[3],[2],[2]])