from basics import tree

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def leafSimilar(self, root1, root2):

		if not root1 or not root2:
			return []

		ans1, ans2 = [], []

		def traverse(root, ans):
			if not root:
				return

			if root.left: traverse(root.left, ans)
			if root.right: traverse(root.right, ans)
			if not root.left and not root.right:
				ans.append(root.val)

		traverse(root1, ans1)
		traverse(root2, ans2)

		return ans1 == ans2


a = [3,5,1,6,2,9,8,'null','null',7,4]
b = [3,5,1,6,7,4,2,'null','null','null','null','null','null',9,8]

a = tree.generate_tree_from_list(a)
b = tree.generate_tree_from_list(b)

print Solution().leafSimilar(a, b)
