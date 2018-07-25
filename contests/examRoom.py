import bisect
class ExamRoom(object):
	def __init__(self, N):
		self.N = N
		self.all_positions = []

	def seat(self):
		if not self.all_positions:
			next_p = 0
		else:
			max_dist = self.all_positions[0]
			p = 0
			next_p = 0
			for i, p in enumerate(self.all_positions):
				if i == 0:
					continue
				cur_dist = (p - self.all_positions[i - 1])/2
				if cur_dist > max_dist:
					next_p = cur_dist + self.all_positions[i - 1]
					max_dist = cur_dist

				# print p, cur_dist, next_p

			if self.N - 1 - p > max_dist:
				next_p = self.N - 1

		bisect.insort(self.all_positions, next_p)
		return next_p

	def leave(self, p):
		self.all_positions.remove(p)


obj = ExamRoom(10)
print obj.seat()
print obj.seat()
print obj.seat()
print obj.leave(0)
print obj.seat()
print obj.leave(4)
print obj.seat()
# [null,0,9,4,2,null,5]


