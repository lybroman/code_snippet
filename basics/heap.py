class MyHeap(object):
	def __init__(self):
		self.data = []

	def heapify(self, data):
		self.data = data
		for i in reversed(range(len(data))):
			self._sift_up(i)

	def heap_push(self, x):
		self.data.append(x)
		self._sift_down(0, len(self.data) -1)

	def _sift_down(self, start, pos):
		new_item = self.data[pos]
		while pos > start:
			parent = (pos - 1) >> 1
			if self.data[parent] > new_item:
				self.data[pos] = self.data[parent]
				pos = parent
				continue
			break
		self.data[pos] = new_item

	def heap_pop(self):
		last_item = self.data.pop()
		if self.data:
			return_item = self.data[0]
			self.data[0] = last_item
			self._sift_up(0)
			return return_item
		return last_item

	def _sift_up(self, pos):
		l = len(self.data)
		new_item = self.data[pos]
		start_pos = pos
		child_index = 2 * pos + 1
		while child_index < l:
			if child_index + 1 < l and self.data[child_index + 1] < self.data[child_index]:
				child_index += 1

			self.data[pos] = self.data[child_index]
			pos = child_index
			child_index = 2 * child_index + 1
		self.data[pos] = new_item
		self._sift_down(start_pos, pos)


data = [97, 38, 27, 50, 76, 65, 49, 13]

heap = MyHeap()

heap.heapify(data)

print heap.data

