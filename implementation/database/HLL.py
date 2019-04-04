"""
HyperLogLog: Cardinality estimation of multi-set
References:
[1] https://blog.acolyer.org/2016/03/17/hyperloglog-in-practice-algorithmic-engineering-of-a-state-of-the-art-cardinality-estimation-algorithm/
[2] http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf
"""
import hashlib
import math


class HyperLogLog(object):
	def __init__(self):
		self.p = 14
		self.m = 1 << self.p
		self.b = [0] * self.m

	@staticmethod
	def k(x):
		i = 0
		while (x >> i) & 1 == 0:
			i += 1
		return i + 1

	@staticmethod
	def h(x):
		sha1 = hashlib.sha1()
		sha1.update(x)
		return int(sha1.hexdigest(), 16)

	def add(self, val):
		hash_val = self.h(val)
		index = hash_val & (self.m - 1)
		cur_k = self.k(hash_val >> self.p)
		self.b[index] = max(self.b[index], cur_k)

	def __len__(self):
		a_m = 0.7213 / (1 + 1.079 / self.m)
		E = a_m * self.m ** 2 * sum(2 ** (-Mj) for Mj in self.b) ** (-1)
		if E < (5 / 2.0 * self.m):
			V = len([b for b in self.b if b == 0])
			if V:
				E = self.m * math.log(self.m / float(V))
		elif E > (1 / 30.0) * 2 ** 32:
			E = -(2 ** 32) * math.log(1 - (E / 2 ** 32))
		return E


if __name__ == '__main__':
	import uuid
	hll = HyperLogLog()
	s = set()
	for i in xrange(1000):
		val = str(uuid.uuid1())
		hll.add(val)
		s.add(val)
	print len(s), len(hll)
