# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def constructFromPrePost(self, pre, post):
		if not pre:
			return None
		root = TreeNode(pre[0])
		if len(pre) == 1:
			return root
		left_l = post.index(pre[1]) + 1
		root.left = self.constructFromPrePost(pre[1:left_l+1], post[:left_l])
		root.right = self.constructFromPrePost(pre[left_l+1:], post[left_l:-1])
		return root