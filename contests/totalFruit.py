class Solution(object):
	def totalFruit(self, tree):
		ntree = [[tree[0], 1]]
		for i in xrange(1, len(tree)):
			if tree[i] == ntree[-1][0]:
				ntree[-1][1] += 1
			else:
				ntree.append([tree[i], 1])

		selected = []
		stree = []
		l = 0
		max_l = -1
		for it in ntree:
			if it[0] in selected:
				stree.append(it)
				l += it[1]
				max_l = max(max_l, l)
				selected.append(it[0])
			elif len(selected) < 2:
				selected.append(it[0])
				stree.append(it)
				l += it[1]
				max_l = max(max_l, l)
			else:
				l = stree[-1][1] + it[1]
				max_l = max(max_l, l)
				stree = [stree[-1], it]
				selected = [selected[-1], it[0]]

		return max_l


print Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4])
print Solution().totalFruit([1,2,3,2,2])
print Solution().totalFruit([0,1,2,2])
print Solution().totalFruit([1,2,1])
print Solution().totalFruit([1,0,1,4,1,4,1,2,3])