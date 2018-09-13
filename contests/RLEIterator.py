class RLEIterator(object):
	def __init__(self, A):
		self.ptr = 0
		self.vol = A[0]
		self.val = A[1]
		self.A = A

	def next(self, n):
		total = self.vol
		if self.ptr == -1:
			return -1
		while total < n:
			if self.ptr + 2 < len(self.A):
				self.ptr += 2
				total += self.A[self.ptr]
				self.val = self.A[self.ptr + 1]
			else:
				self.ptr = -1
				return -1
		self.vol = total - n
		return self.val


rle = RLEIterator([635,606,576,391,370,981,36,21,961,185,124,210,801,937,22,426,101,260,221,647,350,180,504,39,101,989,199,358,732,839,919,169,673,967,58,676,846,342,250,597,442,174,472,410,569,509,311,357,838,251])
print rle.next(5039)
print rle.next(62)
print rle.next(3640)
print rle.next(671)
print rle.next(67)
print rle.next(395)
print rle.next(262)
print rle.next(839)
print rle.next(74)
print rle.next(43)
print rle.next(42)
print rle.next(77)
print rle.next(13)
print rle.next(6)