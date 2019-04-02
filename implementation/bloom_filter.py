import math
import mmh3
from bitset import MmapBitSet


class NaiveBloomFilter(object):
	def __init__(self, n, p):
		self.n = n  # num of items to be inserted
		self.p = p  # expected error rate

		# k = -lnp / ln2, num of hash functions
		self.k = int(math.ceil(-1 * math.log(p, math.e) / math.log(2, math.e)))
		# m = - n * lnp / (ln2) ^ 2, len of bit array
		self.m = int(math.ceil(self.k * self.n * 1.0 / math.log(2, math.e)))
		self.bit_array = MmapBitSet(self.m)

	def _hashes(self, key):
		for i in xrange(self.k):
			yield mmh3.hash(key, self.k)

	def _hashes_opt(self, key):
		# Kirsch - Mitzenmacher - Optimization
		h0 = mmh3.hash(key, 1)
		h1 = mmh3.hash(key, 10)
		for i in xrange(self.k):
			yield h0 + i * h1

	def insert(self, val):
		val = str(val)
		for h in self._hashes(val):
			self.bit_array.set(h % self.m, True)

	def __contains__(self, val):
		val = str(val)
		return all([self.bit_array.get(h % self.m) for h in self._hashes(val)])


if __name__ == '__main__':
	nbf = NaiveBloomFilter(20, 0.05)

	print nbf.m, nbf.k

	for i in xrange(20):
		nbf.insert(i)

	for i in xrange(50):
		if i in nbf:
			if i in range(20):
				print 'Definitely IN set: {}'.format(i)
			else:
				print 'False positive: {}'.format(i)
		else:
			print 'Definitely NOT-IN set: {}'.format(i)

