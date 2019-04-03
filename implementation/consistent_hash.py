import hashlib
import bisect


class ConsistentHash(object):
	def __init__(self, cache_servers):
		self.server_map = {}
		self.hash_ring = []

		for server in cache_servers:
			self.add_node(server)

	@staticmethod
	def h(key):
		md5 = hashlib.md5()
		md5.update(key)
		return long(md5.hexdigest(), 16)

	def add_node(self, server):
		hash_val = self.h(server)
		self.server_map[hash_val] = server
		bisect.insort(self.hash_ring, hash_val)

	def get_node(self, server):
		index = bisect.bisect(self.hash_ring, self.h(server))
		if index == len(self.hash_ring):
			return self.server_map[self.hash_ring[0]]
		else:
			return self.server_map[self.hash_ring[index]]


if __name__ == '__main__':
	cache_servers = ['10.211.0.6:5000', '10.211.0.7:5000', '10.211.0.8:5000']
	ch = ConsistentHash(cache_servers)

	servers = ['www.aaa.com', 'localhost', 'asfdaf', '59.78.10.236', '59.78.10.237']

	for sr in servers:
		print ch.get_node(sr)

	ch.add_node('10.211.0.10:5000')

	print '-' * 30

	for sr in servers:
		print ch.get_node(sr)
