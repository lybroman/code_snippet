import random
MAX_HEIGHT = 4


class SkipListNode(object):
	def __init__(self, val=float('-inf'), max_height=MAX_HEIGHT):
		self.val = val
		self.forward = [None] * max_height


class SkipList(object):
	def __init__(self, prob, max_height=MAX_HEIGHT):
		self.prob = prob
		self.current_height = 0
		self.max_height = max_height
		self.header = SkipListNode(float('-inf'), MAX_HEIGHT)

	def _random_height(self):
		height = 1
		while random.random() <= self.prob and height < self.max_height:
			height += 1
		return height

	def insert(self, val):
		expected_height = self._random_height()
		current_node = self.header
		update = [None] * self.max_height
		i = self.current_height - 1
		while i >= 0:
			while current_node.forward[i] and current_node.forward[i].val < val:
				current_node = current_node.forward[i]

			update[i] = current_node

			i -= 1

		if current_node.forward[0] and current_node.forward[0].val == val:
			return False

		if expected_height > self.current_height:
			for i in range(self.current_height, expected_height):
				update[i] = self.header
			self.current_height = expected_height

		added_node = SkipListNode(val)
		for i in range(0, expected_height):
			added_node.forward[i] = update[i].forward[i]
			update[i].forward[i] = added_node

		return True

	def remove(self, val):
		update = [None] * self.max_height
		i = self.current_height - 1
		current_node = self.header
		while i >= 0:
			while current_node.forward[i] and current_node.forward[i].val < val:
				current_node = current_node.forward[i]

			update[i] = current_node

			i -= 1

		if current_node.forward[0] and current_node.forward[0].val == val:
			target_node = current_node.forward[0]
			for i in range(self.current_height):
				if update[i].forward[i] == target_node:
					update[i].forward[i] = target_node.forward[i]
					if not self.header.forward[i]:
						self.current_height -= 1
			del target_node

			return True
		else:
			return False

	def search(self, val):
		current_node = self.header
		i = self.current_height - 1
		while i >= 0:
			while current_node.forward[i] and current_node.forward[i].val < val:
				current_node = current_node.forward[i]

			if current_node.forward[i].val == val:
				print('find element {} on layer {}'.format(val, i))
				return val
			else:
				i -= 1

		return None

	def __repr__(self):
		layers = []
		for i in range(self.current_height):
			x = self.header
			layer = []
			while x.forward[self.current_height - i - 1]:
				layer.append(str(x.forward[self.current_height - i - 1].val))
				x = x.forward[self.current_height - i - 1]
			layers.append(' '.join(layer))

		return '\r\n'.join(layers)


if __name__ == '__main__':

	skpl = SkipList(0.5, MAX_HEIGHT)
	skpl.insert(4)
	skpl.insert(1)
	skpl.insert(2)
	skpl.insert(0)
	skpl.insert(3)
	skpl.insert(4)

	print(skpl)

	print('*' * 30)

	skpl.remove(4)

	print(skpl)

	print('*' * 30)

	print(skpl.search(0))









