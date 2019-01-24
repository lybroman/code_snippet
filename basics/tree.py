class TreeNode(object):
	"""Definition of a Tree Node"""
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def generate_tree_from_list(ls):
	if not ls:
		return None

	root = TreeNode(ls[0])
	queue = [(root, 0)]
	l = len(ls)

	while queue:
		node, index = queue.pop(0)

		if 2 * index + 1 < l and ls[2 * index + 1] != 'null':
			left = TreeNode(ls[2 * index + 1])
			node.left = left
			queue.append((left, 2 * index + 1))

		if 2 * index + 2 < l and ls[2 * index + 2] != 'null':
			right = TreeNode(ls[2 * index + 2])
			node.right = right
			queue.append((right, 2 * index + 2))

	return root


def inorder_traverse_1(root, ans):
	if not root:
		return
	if root.left: inorder_traverse_1(root.left, ans)
	ans.append(root.val)
	if root.right: inorder_traverse_1(root.right, ans)


def preorder_traverse_1(root, ans):
	if not root:
		return
	ans.append(root.val)
	if root.left: preorder_traverse_1(root.left, ans)
	if root.right: preorder_traverse_1(root.right, ans)


def postorder_traverse_1(root, ans):

	if not root:
		return
	if root.left: postorder_traverse_1(root.left, ans)
	if root.right: postorder_traverse_1(root.right, ans)
	ans.append(root.val)


def inorder_traverse_2(root):
	if not root:
		return []
	ans = []
	queue = []
	node = root
	while node or queue:
		if node:
			queue.append(node)
			node = node.left
		else:
			node = queue.pop()
			ans.append(node.val)
			node = node.right

	return ans


def preorder_traverse_2(root):
	if not root:
		return []

	queue = []
	node = root
	ans= []

	while node or queue:
		if node:
			ans.append(node.val)
			queue.append(node)
			node = node.left

		else:
			node = queue.pop()
			node = node.right

	return ans


def postorder_traverse_2(root):
	if not root:
		return []

	ans = []
	node = root
	queue = []
	last_peek = 0

	while node or queue:
		if node:
			queue.append(node)
			node = node.left
		else:
			# peek first
			peek = queue[len(queue) - 1]

			if peek.right and last_peek != peek.right:
				node = peek.right
			else:
				peek = queue.pop()
				ans.append(peek.val)
				last_peek = peek

	return ans


def postorder_traverse_3(root):
	if not root:
		return []

	ans = []
	node = root
	queue = []
	peeks = set()

	while node or queue:
		if node:
			queue.insert(0, node)
			node = node.left
		else:
			peek = queue[0]

			if peek in peeks:
				peek = queue.pop(0)
				ans.append(peek.val)
			else:
				peeks.add(peek)
				if peek.right:
					node = peek.right

	return ans


def level_order_traverse(root):
	if not root: return []
	next_queue = [root]
	res = []
	while next_queue:
		queue = next_queue[:]
		next_queue = []
		ans = []
		while queue:
			node = queue.pop(0)
			ans.append(node.val)
			if node.left:
				next_queue.append(node.left)
			if node.right:
				next_queue.append(node.right)
		res.append(ans)
	return res


def generate_binary_tree_from_sorted_array(sorted_list):
	
	if not sorted_list: return None

	l = len(sorted_list)
	mid = l / 2

	root = TreeNode(sorted_list[mid])

	if mid != 0:
		root.left = generate_binary_tree_from_sorted_array(sorted_list[:mid])
		root.right = generate_binary_tree_from_sorted_array(sorted_list[mid + 1:])

	return root


def tree_depth(root):
	if not root:
		return 0
	else:
		return max(tree_depth(root.left), tree_depth(root.right)) + 1


def is_balanced(root):
	if not root:
		return True

	lh = tree_depth(root.left)
	rh = tree_depth(root.right)

	return (lh - rh) <= 1 and is_balanced(root.left) and is_balanced(root.right)


if __name__ == '__main__':

	root = generate_tree_from_list(
		['F', 'B', 'G', 'A', 'D', 'null', 'I', 'null', 'null', 'C', 'E',
			'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'H'])
	print level_order_traverse(root)

	print tree_depth(root)
	print is_balanced(root)

	ans = []
	inorder_traverse_1(root, ans)
	print ans

	ans = []
	preorder_traverse_1(root, ans)
	print ans

	ans = []
	postorder_traverse_1(root, ans)
	print ans

	print inorder_traverse_2(root)
	print preorder_traverse_2(root)
	print postorder_traverse_2(root)
	print postorder_traverse_3(root)
	print level_order_traverse(root)

	sorted_list = [1, 2, 3, 4, 5, 6, 7, 8]
	root = generate_binary_tree_from_sorted_array(sorted_list)
	print level_order_traverse(root)








