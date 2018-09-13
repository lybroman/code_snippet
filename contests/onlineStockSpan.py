class StockSpanner(object):

	def __init__(self):
		self.prices = []
		self.consecutive = {}
		self.n = 0

	def next(self, price):
		if not self.prices:
			self.prices.append(price)
			self.consecutive[self.n] = self.n
			self.n += 1
			return 1

		ptr = self.n - 1
		ans = 1
		while price >= self.prices[ptr] and ptr >= 0:
			ans += ptr - self.consecutive[ptr] + 1
			ptr = self.consecutive[ptr] - 1

		self.consecutive[self.n] = ptr + 1
		self.prices.append(price)
		self.n += 1
		return ans


s = StockSpanner()
print s.next(1)
print s.next(31)
print s.next(41)
print s.next(48)
print s.next(59)
print s.next(79)
