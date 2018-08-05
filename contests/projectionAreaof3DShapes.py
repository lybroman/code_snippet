from collections import defaultdict
class Solution(object):
	def projectionArea(self, grid):

		area_xy = 0
		same_x_map = defaultdict(int)
		same_y_map = defaultdict(int)

		for i, row in enumerate(grid):
			for j, v in enumerate(row):
				if v!= 0: area_xy += 1
				same_x_map[i] = max(same_x_map[i], v)
				same_y_map[j] = max(same_y_map[j], v)

		#print sum(same_x_map.values())
		#print sum(same_y_map.values())
		#print area_xy

		return sum(same_x_map.values()) + area_xy + sum(same_y_map.values())


print Solution().projectionArea([[]])