class Solution(object):
	def maxDistToClosest(self, seats):
		positions = [i for i, _ in enumerate(seats) if _ == 1]

		max_dist = positions[0]
		p = 0
		for i, p in enumerate(positions):
			if i:
				cur_dist = (p - positions[i - 1]) / 2
				max_dist = max(cur_dist, max_dist)

		max_dist = max(len(seats) - 1 - p, max_dist)

		return max_dist


print Solution().maxDistToClosest([1,0, 0, 0 ])
