# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def subtreeWithAllDeepest(self, root):
		queue = list()
		if not root: return root
		queue.append(root)
		index_map = {}
		results = []
		index = 1

		while True:
			next_queue = []
			b_deepest = True
			this_level_list = []
			while len(queue) > 0:
				top = queue.pop(0)
				if top:
					b_deepest = False
				index_map[index] = top
				this_level_list.append((index, top))
				index += 1
				next_queue.append(top.left if top else None)
				next_queue.append(top.right if top else None)

			if b_deepest:
				break
			else:
				results.append(this_level_list)

			queue =next_queue[:]

		i = 0
		first = None
		second = None

		while i < len(results[len(results) - 1]):
			if not first and results[len(results) - 1][i][1]:
				first = results[len(results) - 1][i]
			if results[len(results) - 1][i][1] and results[len(results) - 1][i] != first:
				second = results[len(results) - 1][i]
			i += 1
		print first[0], second[0]
		if first and second:
			index0 = first[0]
			index1 = second[0]
			while index0 / 2 != index1 / 2:
				index0 /= 2
				index1 /= 2

			return index_map[index0 / 2]
		elif first:
			return first[1]

class Solution1(object):
	def subtreeWithAllDeepest(self, root):
		max_depth = self.find_max_depth(root)
		return self.find_subtree(root, max_depth, 0)

	def find_max_depth(self, root):
		if not root:
			return 0

		return 1 + max(self.find_max_depth(root.left), self.find_max_depth(root.right))

	def find_subtree(self, root, max_depth, cur_depth):
		if not root:
			return root

		cur_depth += 1

		left = self.find_subtree(root.left, max_depth, cur_depth)
		right = self.find_subtree(root.right, max_depth, cur_depth)

		if cur_depth == max_depth:
			return root

		return root if left and right else left if left else right if right else None





# [0,3,1,4,null,2,null,null,6,null,5]

a = TreeNode(0)
b = TreeNode(3)
c = TreeNode(1)
d = TreeNode(4)
e = TreeNode(2)
f = TreeNode(6)
g = TreeNode(5)

a.left = b
a.right = c
b.left = d
c.left = e
d.right = f
d.left = g

print Solution1().subtreeWithAllDeepest(a) == d


