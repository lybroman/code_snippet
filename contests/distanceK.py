from collections import defaultdict
import heapq


class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def distanceK(self, root, target, K):
		edges = defaultdict(dict)

		def bfs(root):
			queue = [root]
			while queue:
				node = queue.pop(0)
				if node.left:
					queue.append(node.left)
					edges[node][node.left] = 1
					edges[node.left][node] = 1

				if node.right:
					queue.append(node.right)
					edges[node][node.right] = 1
					edges[node.right][node] = 1

		if root:
			bfs(root)
		else:
			return []

		def dijkstra(source):
			queue = [(0, source)]
			nodes = set()
			dists = {source: 0}

			while queue:
				dist, node = heapq.heappop(queue)

				if node in nodes:
					continue
				else:
					nodes.add(node)

				if dist > K:
					break

				for dest, weight in edges[node].items():
					if dest in nodes:
						continue

					prev_min_dist = dists.get(dest, None)
					cur_dist = dist + weight

					if not prev_min_dist or cur_dist < prev_min_dist:
						dists[dest] = cur_dist
						heapq.heappush(queue, (cur_dist, dest))
			return dists

		dists = dijkstra(target)
		res = []
		for node, dist in dists.items():
			if dist == K:
				res.append(node.val)

		return res


tree = [3,5,1,6,2,0,8,'null', 'null',7,4]

a = TreeNode(3)
b = TreeNode(5)
c = TreeNode(1)
d = TreeNode(6)
e = TreeNode(2)
f = TreeNode(0)
g = TreeNode(8)
h = TreeNode(7)
i = TreeNode(4)

a.left, a.right = b, c
b.left, b.right = d, e
c.left, c.right = f, g
e.left, e.right = h, i

print Solution().distanceK(a, a, 2)


